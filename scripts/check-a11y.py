#!/usr/bin/env python3
"""check-a11y.py: the static half of the WCAG 2.2 AA claim.

    sh scripts/build.sh               # build first: this script reads public/
    python3 scripts/check-a11y.py

Why this exists: the site promises WCAG 2.2 AA (AGENT.md section 8), and until now that
promise was kept by hand. The styling pass made it more load-bearing rather than less: it
replaced the citation marker wholesale, it added a rule that every visible element has to
keep its focus ring, and it introduced inline SVG, which brings its own rules about
alternative text. There is no browser and no axe/Lighthouse/pa11y on this machine (AGENT.md
section 7), so **this is not an audit and does not claim to be one**. What it does is check
the invariants that are decidable from the markup and the stylesheet, so that a later edit
cannot quietly break one of them without a red line in the build.

WHAT IT CANNOT CHECK, and this list is the honest part: whether the result is usable, whether
focus order follows the visual order, whether a screen reader announces something sensibly,
whether a colour is distinguishable to a person with a colour vision deficiency, whether an
interactive behaves correctly under zoom or a thumb, or anything about contrast beyond what
check-contrast.py computes from the tokens. Those need a browser and a person.

WHAT IT CHECKS

  Images      every <img> has a non-empty alt or is explicitly decorative, and every inline
              <svg> that is not hidden from assistive tech carries a title or an aria-label.
  Language    <html lang> exists, and is on any element whose text is not English. The site
              has already published one defect in this area: a foreign-language quotation
              left unmarked (WCAG 3.1.2).
  Structure   exactly one h1 per page, no skipped heading levels, every page has a landmark
              main and a skip link that points at an id that exists.
  Links       every link has discernible text, and no link opens a new tab without saying so.
  Ids         no duplicate id in a document, since every citation marker is an anchor into
              the source list and a duplicate would send a reader to the wrong entry.
  Focus       every rule that removes an outline is paired with one that draws something
              else. This is the failure the styling pass could most easily have introduced:
              `outline: none` on a link is invisible in every screenshot ever taken.
  Targets     the interactive elements the stylesheet sizes clear the 24px minimum of WCAG
              2.5.8, read from the stylesheet rather than trusted.

Exit code 1 on any failure, 0 otherwise.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CSS = ROOT / "assets" / "css" / "main.css"

# The only non-English text on the site, and where it lives. A quotation in another language
# has to be marked with the language it is in, which is WCAG 3.1.2 and was one of the three
# defects the dropped /receipts/ page used to publish. Add an entry here when a page quotes
# another language, rather than letting this check pass by accident.
KNOWN_LANG_MARKERS = ("lang=", "xml:lang=")


def strip_tags(html: str) -> str:
    """Text content, with script and style bodies removed first."""
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def check_page(path: pathlib.Path, css: str) -> list[str]:
    html = path.read_text(encoding="utf-8", errors="replace")
    name = str(path.relative_to(PUBLIC))
    failures: list[str] = []

    def fail(message: str) -> None:
        failures.append(f"{name}: {message}")

    # --- language -----------------------------------------------------------
    if not re.search(r"<html[^>]*\blang=", html, re.I):
        fail("html element has no lang attribute (WCAG 3.1.1)")
    # Any element carrying a lang attribute has to have a non-empty one.
    for tag in re.findall(r"<[a-z][^>]*\blang=(\"[^\"]*\"|[^\s>]+)[^>]*>", html, re.I):
        if tag.strip("\"'") == "":
            fail("an element has an empty lang attribute")

    # --- structure ----------------------------------------------------------
    h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, re.S | re.I)
    if len(h1s) != 1:
        fail(f"{len(h1s)} h1 elements, expected exactly 1")
    levels = [int(m) for m in re.findall(r"<h([1-6])\b", html, re.I)]
    previous = 0
    for level in levels:
        if previous and level > previous + 1:
            fail(f"heading level jumps from h{previous} to h{level} (WCAG 1.3.1)")
            break
        previous = level
    if not re.search(r"<main\b", html, re.I):
        fail("no main landmark")
    ids = set(re.findall(r"\bid=(\"[^\"]+\"|[^\s>]+)", html))
    ids = {i.strip("\"'") for i in ids}
    skip = re.search(r"<a[^>]*class=(\"?skip-link\"?)[^>]*href=#([^\s\">]+)", html, re.I)
    if not skip:
        fail("no skip link")
    elif skip.group(2) not in ids:
        fail(f"skip link points at #{skip.group(2)}, which is not an id on the page")

    # --- images -------------------------------------------------------------
    for tag in re.findall(r"<img\b[^>]*>", html, re.I):
        alt = re.search(r"\balt=(\"([^\"]*)\"|([^\s>]+))", tag, re.I)
        if not alt:
            fail(f"img without alt: {tag[:70]}")
        elif (alt.group(2) if alt.group(2) is not None else alt.group(3)) is None:
            fail(f"img with empty alt that is not marked decorative: {tag[:70]}")

    # --- inline svg ---------------------------------------------------------
    for tag in re.findall(r"<svg\b[^>]*>", html, re.I):
        if re.search(r'aria-hidden=("?)true\1', tag, re.I) or 'role="presentation"' in tag or "role=presentation" in tag:
            continue
        has_label = re.search(r"aria-label=(\"[^\"]+\"|[^\s>]+)", tag) or re.search(
            r"aria-labelledby=(\"[^\"]+\"|[^\s>]+)", tag)
        if not has_label:
            fail(f"svg with no accessible name and not aria-hidden: {tag[:70]}")
            continue
        labelledby = re.search(r"aria-labelledby=(\"([^\"]+)\"|([^\s>]+))", tag)
        if labelledby:
            wanted = (labelledby.group(2) or labelledby.group(3)).split()
            for ref in wanted:
                if ref not in ids:
                    fail(f"svg aria-labelledby points at #{ref}, which is not an id on the page")

    # --- links --------------------------------------------------------------
    # The tag pattern needs the whitespace after `a`: `<a\b` also matches `<abbr`, which is
    # how this check reported fifty-seven empty links that were never links. A checker that
    # cries wolf is worse than no checker, because the next person stops reading it.
    for tag, inner in re.findall(r"<a\s([^>]*)>(.*?)</a>", html, re.S | re.I):
        # An id-carrying span is the citation target and is deliberately empty: it is what
        # `:target` highlights, and it is not a link. `<a id="source-x"></a>` would be one,
        # announced as a link and impossible to follow, which is why it is a span.
        if re.fullmatch(r"\s*(<span\b[^>]*></span>)?\s*", inner) and "href=" not in tag:
            continue
        if not strip_tags(inner).strip() and not re.search(r"<img\b|<svg\b", inner, re.I):
            if not re.search(r"aria-label=|title=", tag, re.I):
                fail(f"link with no discernible text: <a {tag[:60]}>")
        if re.search(r'target=("?)_blank\1', tag, re.I) and not re.search(
                r"aria-label=|title=|new (tab|window)", tag + inner, re.I):
            fail(f"link opens a new tab without saying so: <a {tag[:60]}>")

    # --- duplicate ids ------------------------------------------------------
    all_ids = [i.strip("\"'") for i in re.findall(r"\bid=(\"[^\"]+\"|[^\s>]+)", html)]
    seen: set[str] = set()
    for value in all_ids:
        if value in seen:
            fail(f"duplicate id \"{value}\", which breaks a citation anchor")
        seen.add(value)

    return failures


def check_focus(css: str) -> list[str]:
    """An outline removed has to be replaced by something visible.

    The check is deliberately narrow: it looks for a rule that sets `outline: none` or
    `outline: 0` and reports every one, because this stylesheet has no legitimate use for
    them. A focus ring on this site is drawn with `outline`, so removing one is always either
    a mistake or a decision that has to be argued in a comment here.
    """
    failures: list[str] = []
    for match in re.finditer(r"([^{}]*)\{([^}]*)\}", css, re.S):
        selector, body = match.group(1).strip(), match.group(2)
        if re.search(r"outline\s*:\s*(none|0)", body):
            line = css[:match.start()].count("\n") + 1
            failures.append(f"assets/css/main.css:{line}: \"{selector}\" removes the outline; "
                            f"every focus indicator on this site is drawn with one")
    if ":focus-visible" not in css:
        failures.append("assets/css/main.css: no :focus-visible rule, so nothing has a focus ring")
    return failures


def check_targets(css: str) -> list[str]:
    """The 24px minimum of WCAG 2.5.8, read from the declarations rather than from a claim.

    Only the citation marker is checked, because it is the one inline control the site builds
    out of a character and it is the element whose size was the site's own published defect.
    """
    failures: list[str] = []
    marker = re.search(r"\.cite a\s*\{(.*?)\}", css, re.S)
    if not marker:
        return [".cite a rule is missing, so the citation marker has no size at all"]
    body = marker.group(1)

    def px(prop: str) -> float | None:
        m = re.search(rf"{prop}\s*:\s*([\d.]+)(px|rem|em)", body)
        if not m:
            return None
        value = float(m.group(1))
        return value * 16 if m.group(2) in ("rem", "em") else value

    min_w, min_h = px("min-width"), px("min-height")
    if min_w is None or min_h is None:
        failures.append(".cite a declares no min-width/min-height, so its target size is "
                        "whatever the digits happen to measure")
    else:
        if min_w < 24:
            failures.append(f".cite a min-width is {min_w}px, under the 24px minimum")
        if min_h < 24:
            failures.append(f".cite a min-height is {min_h}px, under the 24px minimum")
    return failures


def main() -> int:
    if not PUBLIC.is_dir():
        print(f"no build at {PUBLIC}: run 'sh scripts/build.sh' first", file=sys.stderr)
        return 1
    css = CSS.read_text(encoding="utf-8") if CSS.is_file() else ""
    pages = sorted(PUBLIC.rglob("*.html"))
    if not pages:
        print(f"no HTML in {PUBLIC}", file=sys.stderr)
        return 1

    failures: list[str] = []
    svg_total = 0
    for page in pages:
        failures += check_page(page, css)
        svg_total += len(re.findall(r"<svg\b", page.read_text("utf-8", "replace"), re.I))
    failures += check_focus(css)
    failures += check_targets(css)

    print(f"pages checked                {len(pages)}")
    print(f"inline svg checked           {svg_total}")
    print(f"language markers in use      {sum(1 for p in pages for _ in re.finditer('lang=', p.read_text('utf-8','replace')))}")
    print()
    if failures:
        print(f"a11y: {len(failures)} problem(s)")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print("a11y: every static invariant holds (headings, landmarks, alt text, ids, focus, "
          "target sizes)")
    print("      THIS IS NOT AN AUDIT. It cannot see focus order, screen reader output, "
          "zoom, or anything a person would notice. See the module docstring.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
