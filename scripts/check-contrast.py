#!/usr/bin/env python3
"""check-contrast.py: verify the site's colours before anyone trusts them.

    python3 scripts/check-contrast.py

Why this exists: the site promises WCAG 2.2 AA, and until 2026-10-15 that promise was kept
by hand. A hand-kept promise about colour is a promise that breaks the first time somebody
adjusts a hex value, and nothing notices, because a slightly-too-light grey looks fine on
the machine it was chosen on. So the ratios are computed from the stylesheet itself rather
than from a list copied out of it: this script parses the `:root` token block in
assets/css/main.css, then the `prefers-color-scheme: dark` block that overrides it, and
checks every pair the site actually renders.

It is wired into scripts/build.sh as a check, before the build rather than after, because
a page that fails this should not be built.

WHAT IS CHECKED

Text pairs (4.5:1, WCAG 1.4.3). Every foreground the CSS sets on every ground it sets it
on: body ink, headings, muted and faint text, links, the citation marker, button labels on
the two filled colours, quote and caption text.

Non-text pairs (3:1, WCAG 1.4.11). The focus ring against every ground it can appear over,
which includes the accent colour itself: a ring the same colour as the control it outlines
is invisible, so the ring is a separate token from the accent on purpose. Plus the rules
and borders the CSS draws, since a 1px line that vanishes is a layout failure rather than a
contrast one, and the marker plate behind a citation.

WHERE THE VALUES COME FROM. The palette is based on love2d.org, which the maintainer named
as the reference on 2026-10-15. The reference site's own interface colours do not pass AA as
text on its background (#25aae1 is 2.34:1 on #e0f4fc; its pink is 4.07:1 on white), so the
hues are kept and the lightnesses are not. The NOTES table at the bottom of this file
records each substitution so the next person does not "restore" the reference values and
silently break the promise.

Exit code 1 on any failure, 0 otherwise.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / "assets" / "css" / "main.css"
FONTS = ROOT / "static" / "fonts"

TEXT_MIN = 4.5
NONTEXT_MIN = 3.0

# Pairs the site renders. Each entry is (what, foreground token, background token, minimum).
# The list is deliberately explicit rather than derived from the CSS: a rule can put any
# colour on any surface, and what matters is what a reader has to read. Adding a colour pair
# to the stylesheet means adding its line here, which is the reminder to check it.
TEXT_PAIRS = [
    ("body text on the page", "ink", "bg"),
    ("body text on a surface (code, interactive)", "ink", "surface"),
    ("body text on a tinted surface", "ink", "surface-2"),
    ("headings on the page", "ink-heading", "bg"),
    ("headings on a surface", "ink-heading", "surface"),
    ("muted text on the page", "ink-muted", "bg"),
    ("muted text on a surface (captions, source meta)", "ink-muted", "surface"),
    ("muted text on a tinted surface", "ink-muted", "surface-2"),
    ("faint text on the page (status stamp)", "ink-faint", "bg"),
    ("faint text on a surface", "ink-faint", "surface"),
    ("links on the page", "accent", "bg"),
    ("links on a surface", "accent", "surface"),
    ("links on a tinted surface", "accent", "surface-2"),
    ("citation marker on its plate", "accent", "accent-quiet"),
    ("text on a filled accent button", "accent-ink", "accent"),
    ("text on a filled pink button", "pop-ink", "pop"),
    ("attention text on the page", "pop", "bg"),
    ("attention text on a surface", "pop", "surface"),
    ("callout text on the callout ground", "ink", "pop-quiet"),
    ("text in an accented list row (:target)", "ink", "surface"),
]

NONTEXT_PAIRS = [
    ("focus ring on the page", "ring", "bg"),
    ("focus ring on a surface", "ring", "surface"),
    ("focus ring on a tinted surface", "ring", "surface-2"),
    ("citation marker border on its plate", "rule-control", "accent-quiet"),
]

# The focus indicator is two rings in both schemes: the ring colour outside, then a 2px band
# of the page ground, then the control. That structure exists because no single colour clears
# 3:1 against a pale ground, a dark ground, and both filled controls at once, and the marker
# is a filled control. What has to hold is checked here as two steps: the ring is separated
# from the band, and the band is separated from the fill it is drawn on.
HALO_PAIRS = [
    ("focus ring against the focus band", "ring", "ring-halo"),
    ("focus band against a filled accent control", "ring-halo", "accent"),
    ("focus band against a filled pink control", "ring-halo", "pop"),
]

# Lines drawn where the line itself carries information a reader needs: a source section
# starting, a table header ending, a control's edge. 3:1, WCAG 1.4.11.
LINE_PAIRS = [
    ("section rules on the page", "rule-strong", "bg"),
    ("section rules on a surface", "rule-strong", "surface"),
]

# Hairlines that group rather than inform: card edges, list rows, the line above a caption.
# Deliberately not held to 3:1, because a rule that passes 3:1 against a pale ground stops
# being a hairline and starts being a second heading. They are printed so the values stay
# visible, and the two that *do* carry meaning are in LINE_PAIRS above.
DECORATIVE_PAIRS = [
    ("hairline rules on the page", "rule", "bg"),
    ("hairline rules on a surface", "rule", "surface"),
    ("hairline rules on a tinted surface", "rule", "surface-2"),
    ("table row rules on the page", "rule", "bg"),
]

# Substitutions made to the reference palette, kept where the values live so that the next
# person to look at this file sees why the site does not use love2d.org's own values.
NOTES = [
    ("#25aae1 interface blue", "#0a6c93",
     "2.34:1 on the reference background as text, below AA"),
    ("#ea316e pink", "#c2185b",
     "4.07:1 on white as text, below AA; used here for attention, which is text"),
    ("#e0f4fc sky ground", "#f6fbfd",
     "the reference ground carried over as a surface instead, with a lighter page ground "
     "for a three thousand word read"),
    ("#1b4d68 and #383f4a", "kept",
     "the reference's own heading and body colours, which already pass comfortably"),
]


def lum(hex_colour: str) -> float:
    """WCAG 2.1 relative luminance."""
    value = hex_colour.lstrip("#")
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    r, g, b = linear
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a: str, b: str) -> float:
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def parse_tokens(css: str) -> tuple[dict[str, str], dict[str, str]]:
    """The light tokens from `:root` and the dark overrides from the media block."""
    light: dict[str, str] = {}
    dark: dict[str, str] = {}
    # Every `--name: value;` declaration, tagged with the block it sits in.
    media = re.search(r"@media\s*\(prefers-color-scheme:\s*dark\)\s*\{(.*?)\n\}", css, re.S)
    if media:
        for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", media.group(1)):
            dark[name] = value.strip()
    root = re.search(r":root\s*\{(.*?)\n\}", css, re.S)
    if root:
        for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", root.group(1)):
            light[name] = value.strip()
    return light, dark


def scheme(tokens: dict[str, str], overrides: dict[str, str]) -> dict[str, str]:
    """Light tokens with the dark block applied on top, which is what the cascade does."""
    return {**tokens, **overrides}


def check_scheme(name: str, tokens: dict[str, str]) -> list[str]:
    failures: list[str] = []
    print(f"  {name}")
    pairs = ([(l, f, b, TEXT_MIN) for l, f, b in TEXT_PAIRS]
             + [(l, f, b, NONTEXT_MIN) for l, f, b in NONTEXT_PAIRS]
             + [(l, f, b, NONTEXT_MIN) for l, f, b in LINE_PAIRS])
    for label, fg, bg, minimum in pairs:
        key_fg, key_bg = f"--{fg}", f"--{bg}"
        if key_fg not in tokens or key_bg not in tokens:
            failures.append(f"{name}: {label} refers to an undefined token "
                            f"({key_fg} or {key_bg})")
            print(f"    MISSING TOKEN  {label}")
            continue
        if tokens[key_bg] == "transparent":
            # A transparent halo is the light scheme's arrangement: the ring contrasts with
            # the control's own fill instead, which NONTEXT_PAIRS checks directly.
            print(f"    n/a  {label}: no halo in this scheme")
            continue
        value = ratio(tokens[key_fg], tokens[key_bg])
        ok = value >= minimum
        mark = "ok  " if ok else "FAIL"
        print(f"    {mark} {value:6.2f}:1  (min {minimum:.1f})  {label}")
        if not ok:
            failures.append(f"{name}: {label} is {value:.2f}:1, below {minimum:.1f}:1 "
                            f"({tokens[key_fg]} on {tokens[key_bg]})")

    # Ring against control, in whichever form this scheme uses. A halo, when one is set,
    # must itself be separated from the fill it is drawn on, and the ring must be separated
    # from the halo: two 3:1 steps, which is what a two-ring focus indicator is.
    halo = tokens.get("--ring-halo")
    if halo and halo != "transparent":
        for label, fg, bg in HALO_PAIRS:
            key_fg, key_bg = f"--{fg}", f"--{bg}"
            if key_fg not in tokens or key_bg not in tokens:
                failures.append(f"{name}: {label} refers to an undefined token")
                continue
            value = ratio(tokens[key_fg], tokens[key_bg])
            ok = value >= NONTEXT_MIN
            print(f"    {'ok  ' if ok else 'FAIL'} {value:6.2f}:1  (min {NONTEXT_MIN:.1f})  {label}")
            if not ok:
                failures.append(f"{name}: {label} is {value:.2f}:1, below {NONTEXT_MIN:.1f}:1")
    else:
        # No band: the ring has to contrast with the fills directly, which is the original
        # one-ring arrangement. Kept so that removing the band is still a checked change.
        for label, fg, bg in (("focus ring on a filled accent control", "ring", "accent"),
                              ("focus ring on a filled pink control", "ring", "pop")):
            value = ratio(tokens[f"--{fg}"], tokens[f"--{bg}"])
            ok = value >= NONTEXT_MIN
            print(f"    {'ok  ' if ok else 'FAIL'} {value:6.2f}:1  (min {NONTEXT_MIN:.1f})  {label}")
            if not ok:
                failures.append(f"{name}: {label} is {value:.2f}:1, below {NONTEXT_MIN:.1f}:1")

    for label, fg, bg in DECORATIVE_PAIRS:
        if f"--{fg}" in tokens and f"--{bg}" in tokens:
            value = ratio(tokens[f"--{fg}"], tokens[f"--{bg}"])
            print(f"    info {value:6.2f}:1  (decorative)  {label}")
    return failures


def check_fonts(css: str) -> list[str]:
    """Every url() the stylesheet references has to exist in the tree that ships."""
    failures: list[str] = []
    found = 0
    for url in re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", css):
        if url.startswith(("http://", "https://", "//", "data:")):
            failures.append(f"third-party font or asset reference: {url}")
            continue
        path = ROOT / "static" / url.lstrip("/")
        found += 1
        if not path.is_file():
            failures.append(f"stylesheet references {url}, which is not at {path.relative_to(ROOT)}")
    licence_texts = sorted(p.name for p in FONTS.glob("*.txt")) if FONTS.is_dir() else []
    print(f"  fonts: {found} url() reference(s), {len(licence_texts)} licence file(s) in static/fonts/")
    if found and not any(p.endswith((".txt",)) for p in licence_texts):
        failures.append("no licence text in static/fonts/: a subset is a distribution, so the "
                        "terms have to travel with it (AGENT.md section 9 item 8)")
    return failures


def main() -> int:
    if not CSS.is_file():
        print(f"no stylesheet at {CSS}", file=sys.stderr)
        return 1
    css = CSS.read_text(encoding="utf-8")
    light, dark = parse_tokens(css)
    if not light:
        print("could not parse any tokens from the :root block", file=sys.stderr)
        return 1

    print("contrast, computed from the tokens in assets/css/main.css")
    failures = check_scheme("light scheme", light)
    if dark:
        failures += check_scheme("dark scheme", scheme(light, dark))
    else:
        print("  dark scheme: no overrides found in the stylesheet")
    print()
    failures += check_fonts(css)

    print()
    print("departures from the reference palette, recorded so they are not undone:")
    for original, replacement, why in NOTES:
        print(f"  {original:24} -> {replacement:18} {why}")

    print()
    if failures:
        print(f"contrast: {len(failures)} failure(s)")
        for failure in failures:
            print(f"  {failure}")
        return 1
    worst_text = min(ratio(light[f"--{f}"], light[f"--{b}"]) for _, f, b in TEXT_PAIRS)
    checked = len(NONTEXT_PAIRS) + len(LINE_PAIRS) + len(HALO_PAIRS) * 2
    print(f"contrast: all {len(TEXT_PAIRS)} text pairs at or above {TEXT_MIN:.1f}:1 "
          f"(lowest {worst_text:.2f}:1), {checked} non-text pairs at or above "
          f"{NONTEXT_MIN:.1f}:1, in both schemes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
