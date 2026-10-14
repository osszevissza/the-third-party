#!/usr/bin/env python3
"""
render-bibliography.py: generate the bibliography block on /sources/.

Run:  python3 scripts/render-bibliography.py
      python3 scripts/render-bibliography.py --check   # exit 1 if the page is stale

Why this exists: /sources/ is the page where the project's sourcing claim is either true
or decorative, and a hand-maintained bibliography drifts from its data within a week.
This script renders the block between the two markers in content/sources/index.md from
data/sources.yaml and from the `sources` lists in every page's frontmatter, so the page
cannot disagree with the citation graph that check-content.py validates.

It edits exactly one file, and only between the markers. Everything outside them is
prose and is left untouched, no matter what this script does.

Markers:
    <!-- BEGIN GENERATED BIBLIOGRAPHY -->
    <!-- END GENERATED BIBLIOGRAPHY -->

Exit codes: 0 on success, 1 if a marker is missing, the data will not parse, or (in
--check mode) the generated block is out of date.
"""

from __future__ import annotations

import pathlib
import sys
import tomllib

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "sources.yaml"
PAGE = ROOT / "content" / "sources" / "index.md"
CONTENT = ROOT / "content"

BEGIN = "<!-- BEGIN GENERATED BIBLIOGRAPHY -->"
END = "<!-- END GENERATED BIBLIOGRAPHY -->"

# Source `type` values, folded into the four groups a reader actually wants. A type
# that is not listed here stops the script rather than landing in a silent "other"
# bucket, because a new kind of source is a decision, not an accident.
GROUPS: list[tuple[str, str, set[str]]] = [
    (
        "evidence",
        "Research and evidence",
        {"research", "law-review", "book", "taxonomy", "dataset", "audit",
         "industry-report", "methodology"},
    ),
    (
        "law",
        "Law, regulation and regulators",
        {"regulator", "regulation", "statute", "judgment", "legal-filing",
         "legal-summary"},
    ),
    (
        "journalism",
        "Journalism",
        {"news"},
    ),
    (
        "vendors",
        "The projects and companies themselves",
        {"tool", "vendor-doc", "vendor-blog", "directory"},
    ),
]


def fail(message: str) -> None:
    sys.exit(f"render-bibliography.py: {message}")


def load_sources() -> tuple[list[dict], dict[str, dict]]:
    if not SOURCES.is_file():
        fail(f"{SOURCES.relative_to(ROOT)} not found")
    try:
        records = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"data/sources.yaml does not parse ({exc})")
    if not isinstance(records, list):
        fail("data/sources.yaml is not a list of records")
    return records, {r["id"]: r for r in records}


def load_pages() -> list[dict]:
    """Each page's title, url and declared source ids, for the reverse index."""
    pages = []
    for path in sorted(CONTENT.glob("*/index.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("+++"):
            fail(f"{path.relative_to(ROOT)} has no TOML frontmatter")
        try:
            meta = tomllib.loads(text.split("+++", 2)[1])
        except tomllib.TOMLDecodeError as exc:
            fail(f"{path.relative_to(ROOT)} frontmatter does not parse ({exc})")
        pages.append(
            {
                "slug": path.parent.name,
                "url": f"/{path.parent.name}/",
                "title": meta.get("title") or path.parent.name,
                "sources": list(meta.get("sources") or []),
            }
        )
    return pages


def cite(record: dict) -> str:
    """One line of bibliographic detail, with the links a reader needs."""
    bits = []
    authors = record.get("authors") or []
    if authors:
        bits.append(", ".join(authors))
    bits.append(record["publisher"])
    if record.get("date"):
        bits.append(str(record["date"]))
    else:
        bits.append("no date on the document")
    line = " · ".join(bits)

    links = []
    if record.get("url"):
        links.append(f"[the source itself]({record['url']})")
    else:
        links.append("no stable URL found yet")
    if record.get("archive"):
        links.append(f"[archived copy]({record['archive']})")
    if record.get("doi"):
        links.append(f"doi:{record['doi']}")
    return f"{line} · " + " · ".join(links)


def status(record: dict) -> str:
    if not record.get("url"):
        return "**Status: no URL.** Cited, but not yet publishable."
    if not record.get("verified_on"):
        return (
            "**Status: not verified.** The link has not been opened and confirmed, "
            "so the claim it carries is unproven."
        )
    when = record["verified_on"]
    if record.get("archive"):
        return f"**Status: verified {when}, archived.**"
    return f"**Status: verified {when}, not archived yet.**"


def flat(text: str) -> str:
    """Collapse a YAML block scalar into one paragraph."""
    return " ".join(str(text).split())


def render(records: list[dict], by_id: dict[str, dict], pages: list[dict]) -> str:
    used_by: dict[str, list[dict]] = {sid: [] for sid in by_id}
    for page in pages:
        for sid in page["sources"]:
            if sid not in by_id:
                fail(f"{page['slug']} declares unknown source id `{sid}`")
            used_by[sid].append(page)

    grouped: dict[str, list[dict]] = {key: [] for key, _, _ in GROUPS}
    known = {t for _, _, types in GROUPS for t in types}
    for record in records:
        if record["type"] not in known:
            fail(
                f"source `{record['id']}` has type `{record['type']}`, which is in no "
                f"group. Add it to GROUPS in this script, deliberately."
            )
        for key, _, types in GROUPS:
            if record["type"] in types:
                grouped[key].append(record)
                break

    total = len(records)
    verified = sum(1 for r in records if r.get("verified_on"))
    archived = sum(1 for r in records if r.get("archive"))
    no_url = sum(1 for r in records if not r.get("url"))
    no_date = sum(1 for r in records if not r.get("date"))
    cited = sum(1 for r in records if used_by.get(r["id"]))

    out: list[str] = []
    add = out.append

    add("Generated from `data/sources.yaml` by `scripts/render-bibliography.py`. "
        "Do not edit this block by hand: run the script.")
    add("")
    add("| What this counts | Number |")
    add("|---|---|")
    add(f"| Sources in the file | {total} |")
    add(f"| Cited by at least one page | {cited} |")
    add(f"| Link opened and confirmed, with a date | {verified} |")
    add(f"| Snapshotted to the Wayback Machine | {archived} |")
    add(f"| No stable URL found yet | {no_url} |")
    add(f"| The document itself carries no date | {no_date} |")
    add("")
    add("Every number above is computed from the citation file when this page is built. "
        "If the site claims a source is verified and this table disagrees, the table is "
        "right.")
    add("")

    for key, heading, _ in GROUPS:
        entries = grouped[key]
        if not entries:
            continue
        add(f"## {heading}")
        add("")
        for record in sorted(
            entries, key=lambda r: (str(r.get("date") or "9999"), r["id"])
        ):
            # The explicit `source-` anchor matters: the `cite` shortcode links to
            # `#source-<id>` on every page, so without it an inline citation made *on this
            # page* points at nothing. Goldmark's own heading id stays as it was, and the
            # reverse index below links to the same anchor the shortcode uses.
            add(f'### <a id="source-{record["id"]}"></a>{record["id"]}')
            add("")
            add(f"**{record['title']}**")
            add("")
            add(cite(record))
            add("")
            add(status(record))
            add("")
            add(f"**Weak at:** {flat(record['weakness'])}")
            add("")
            add("**Carries:**")
            add("")
            for item in record.get("supports") or []:
                add(f"- {flat(item)}")
            add("")

    add("## Which page rests on which sources")
    add("")
    for page in pages:
        if page["slug"] == "sources":
            continue
        if not page["sources"]:
            add(f"**{page['title']}**: no declared sources.")
            continue
        links = ", ".join(f"[`{sid}`](#source-{sid})" for sid in page["sources"])
        add(f"**{page['title']}** ({len(page['sources'])}): {links}")
        add("")

    orphans = [r["id"] for r in records if not used_by.get(r["id"])]
    if orphans:
        add("**Not cited by any page yet:** " + ", ".join(f"`{sid}`" for sid in orphans))
        add("")
        add("A source nothing rests on is either waiting for a page or dead weight. This "
            "list should be empty.")
        add("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    records, by_id = load_sources()
    pages = load_pages()
    block = render(records, by_id, pages)

    if not PAGE.is_file():
        fail(f"{PAGE.relative_to(ROOT)} not found")
    page = PAGE.read_text(encoding="utf-8")
    if BEGIN not in page or END not in page:
        fail(
            f"{PAGE.relative_to(ROOT)} is missing a marker. Both of these must be "
            f"present, on their own lines:\n    {BEGIN}\n    {END}"
        )

    head, rest = page.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    rebuilt = f"{head}{BEGIN}\n\n{block}\n{END}{tail}"

    if check_only:
        if rebuilt != page:
            print(
                "content/sources/index.md is out of date. Run "
                "python3 scripts/render-bibliography.py"
            )
            return 1
        print("bibliography is up to date")
        return 0

    if rebuilt == page:
        print("bibliography unchanged")
        return 0

    PAGE.write_text(rebuilt, encoding="utf-8")
    print(
        f"wrote {len(records)} entries in {len(GROUPS)} groups, "
        f"{len(rebuilt.splitlines())} lines in content/sources/index.md"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
