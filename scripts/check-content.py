#!/usr/bin/env python3
"""
check-content.py: content integrity check for the ethical-web site.

Run before every commit:  python3 scripts/check-content.py

Why this exists: the site's central claim is that its sources are real, dated, and
checkable. That claim degrades silently as pages get added. This script makes the
degradation loud.

Checks:
  1. every YAML file in data/ parses
  2. every content page's frontmatter parses as TOML
  3. every id in a page's `sources` list exists in data/sources.yaml
  4. every {{< cite "id" >}} used inline exists in data/sources.yaml
  5. declared-but-uncited and cited-but-undeclared sources
  6. sources still missing a URL or a verified_on date
  7. pages missing status_as_of
  8. source ids that are declared twice
  9. source records whose `supports` items are not strings (see the note in load_sources)

Exit code 1 if any ERROR is found, 0 otherwise. Warnings do not fail the build.
"""

from __future__ import annotations

import pathlib
import re
import sys
import tomllib

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"
DRAFTS = ROOT / "drafts"

CITE_RE = re.compile(r'\{\{<\s*cite\s+"([^"]+)"\s*>\}\}')
# Malformed shortcodes that render as literal text. `{cite id}` (single braces) is
# the one that actually happens: it fails silently, so the page ends up declaring
# sources it never cites and citing sources it never declares.
BAD_CITE_RE = re.compile(r'(?<!\{)\{\{?\s*cite\b(?!\s*>)')

errors: list[str] = []
warnings: list[str] = []


def rel(p: pathlib.Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


# ---------------------------------------------------------------- 1. data files
def load_sources() -> dict[str, dict]:
    index: dict[str, dict] = {}
    if not DATA.is_dir():
        errors.append("data/ directory not found")
        return index

    for path in sorted(DATA.glob("*.y*ml")):
        try:
            parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel(path)}: YAML does not parse ({exc})")
            continue

        if not isinstance(parsed, list):
            warnings.append(f"{rel(path)}: top level is not a list; skipped")
            continue

        for entry in parsed:
            if not isinstance(entry, dict):
                warnings.append(f"{rel(path)}: non-mapping entry skipped")
                continue
            sid = entry.get("id")
            if not sid:
                errors.append(f"{rel(path)}: an entry has no `id`")
                continue
            if sid in index:
                errors.append(f"{rel(path)}: duplicate source id `{sid}`")
            entry["_file"] = rel(path)
            index[sid] = entry

    # Structural types the templates rely on. This exists because of a real defect:
    # an unquoted colon inside a YAML list item (`- Foo: bar`) makes YAML read the
    # item as a *mapping* rather than a sentence, so /sources/ would render a dict
    # where a claim belongs. Nothing else in the pipeline notices, because the file
    # still parses and the citation graph is unaffected.
    for sid, entry in index.items():
        supports = entry.get("supports")
        if supports is None:
            continue
        if not isinstance(supports, list):
            errors.append(f"{entry['_file']}: `{sid}`: `supports` is not a list")
            continue
        for item in supports:
            if not isinstance(item, str):
                errors.append(
                    f"{entry['_file']}: `{sid}`: a `supports` item is not a string "
                    f"({item!r}). An unquoted ': ' in a list item makes YAML build a "
                    f"mapping; quote the item or rephrase it."
                )

    return index


# ------------------------------------------------------------------- 2. pages
def split_frontmatter(path: pathlib.Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        raise ValueError("does not start with +++ TOML frontmatter")
    parts = text.split("+++", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter is not closed with +++")
    meta = tomllib.loads(parts[1])
    return meta, parts[2]


def check_page(path: pathlib.Path, sources: dict[str, dict]) -> None:
    try:
        meta, body = split_frontmatter(path)
    except (ValueError, tomllib.TOMLDecodeError) as exc:
        msg = f"{rel(path)}: frontmatter problem ({exc})"
        # Missing frontmatter is fatal in content/ (it is a broken Hugo page)
        # but not in drafts/, where a file may legitimately be a loose note.
        if CONTENT in path.parents:
            errors.append(msg)
        else:
            warnings.append(f"{msg} (ignored: not under content/)")
        return

    declared = list(meta.get("sources") or [])
    cited = CITE_RE.findall(body)

    # Malformed cite shortcodes fail silently, so check for them explicitly.
    for m in BAD_CITE_RE.finditer(body):
        line = body[: m.start()].count("\n") + 1
        snippet = body[m.start() : m.start() + 40].split("\n")[0]
        errors.append(
            f"{rel(path)}: malformed cite shortcode at line {line}: "
            f"'{snippet}'. Use {{{{< cite \"id\" >}}}} with angle brackets."
        )

    if not meta.get("status_as_of"):
        warnings.append(f"{rel(path)}: no `status_as_of` date")

    # 3. declared ids must exist
    for sid in declared:
        if sid not in sources:
            errors.append(f"{rel(path)}: declares unknown source id `{sid}`")

    # 4. inline ids must exist
    for sid in set(cited):
        if sid not in sources:
            errors.append(f"{rel(path)}: cites unknown source id `{sid}`")

    # 5. cross-check declared vs cited
    for sid in declared:
        if sid not in cited:
            warnings.append(
                f"{rel(path)}: declares `{sid}` but never cites it inline"
            )
    for sid in set(cited):
        if sid not in declared:
            warnings.append(
                f"{rel(path)}: cites `{sid}` inline but omits it from frontmatter"
            )

    words = len(body.split())
    if words < 400:
        warnings.append(f"{rel(path)}: only {words} words of body text")


def main() -> int:
    sources = load_sources()
    print(f"data/: {len(sources)} sources loaded")

    # Bail out now if the source data itself is broken. Continuing would emit one
    # "unknown source id" error per citation across every page, burying the cause.
    if errors:
        return fail_fast("\n".join(f"  ERROR  {e}" for e in errors))

    pages: list[pathlib.Path] = []
    for base in (CONTENT, DRAFTS):
        if base.is_dir():
            pages += [
                p
                for p in sorted(base.glob("**/*.md"))
                if p.is_file() and p.name.lower() != "readme.md"
            ]
    print(f"pages: {len(pages)} found across content/ and drafts/\n")

    for page in pages:
        check_page(page, sources)

    # 6. unverified sources
    unverified = [
        s for s in sources.values() if not s.get("verified_on") or not s.get("url")
    ]
    for s in unverified:
        missing = []
        if not s.get("url"):
            missing.append("no url")
        if not s.get("verified_on"):
            missing.append("not verified")
        warnings.append(f"source `{s['id']}`: {', '.join(missing)}")

    for w in warnings:
        print(f"  warn   {w}")
    for e in errors:
        print(f"  ERROR  {e}")

    print()
    print(f"{len(warnings)} warning(s), {len(errors)} error(s)")
    return 1 if errors else 0


def fail_fast(reason: str) -> int:
    """Bail out before citation checks, which would otherwise cascade."""
    print("\n" + reason)
    print("\nAborted: source data could not be loaded, so citation integrity")
    print("cannot be checked. Fix data/ first, the cascade below this point")
    print("would be noise rather than information.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
