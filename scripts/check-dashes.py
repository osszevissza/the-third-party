#!/usr/bin/env python3
"""
check-dashes.py: enforce the house punctuation rule.

Run before ending a session:  python3 scripts/check-dashes.py

Why this exists: the maintainer asked in round 8 that em dashes not be used, on the
grounds that people rarely use them and only where nothing else will do. That kind of
rule rots the way every editorial rule rots, one convenient dash at a time, so this
script makes the rot loud instead of gradual.

Scope: the published pages in content/ and drafts/, the citation data in data/, the
scripts in scripts/, and the working documents at the root, because those are read by
humans too.

The one exception: text inside quotation marks that quotes a source, a law, a company or
a document title stays exactly as it was published, em dash included, because a quotation
you have tidied is no longer a quotation. When a finding is one of those, add its
file and line to ALLOWED below with a one-line reason rather than editing the quote.

Generated regions are skipped. Text between a `BEGIN GENERATED` marker and its matching
`END GENERATED` marker is machine-written from data/sources.yaml, which this script
checks on its own terms, and a generated line number is not something anyone can
maintain an allowlist against.

Exit code 1 if any unallowed em dash is found, 0 otherwise.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
EM_DASH = "\u2014"

# (relative path, line number): why this one is allowed to keep its em dash.
# Empty as of 2026-10-14, and the reason is worth keeping. The single entry that used to
# live here said the CNIL self-assessment PDF's title was "quoted as published", but it had
# never been checked: cnil.fr answers 503 for every path while its site is in maintenance,
# so the title could not be re-read when the sweep ran. The archived copy of CNIL's own page
# turned out to be readable, and it contains no em dash at all (0 in the page, 0 in the PDF),
# so the title was our own compression of the publisher's words, not a quotation of them.
# The record now carries CNIL's actual title and this allowlist is empty.
# Re-add an entry only for a dash genuinely inside text a source published, and name the
# snapshot you checked it against. Note the key is a line number, so it goes stale whenever
# data/sources.yaml is edited above the line it points at: re-verify it, do not just bump it.
ALLOWED: dict[tuple[str, int], str] = {}

TARGETS = ["content/**/*.md", "drafts/**/*.md", "data/*.yaml", "scripts/*.py"]
ROOT_DOCS = ["AGENT.md", "SITE_PLAN.md", "FOR-REVIEW.md"]


def files() -> list[pathlib.Path]:
    found: list[pathlib.Path] = []
    for pattern in TARGETS:
        found += [p for p in sorted(ROOT.glob(pattern)) if p.is_file()]
    found += [ROOT / name for name in ROOT_DOCS if (ROOT / name).is_file()]
    return found


def main() -> int:
    findings: list[str] = []
    allowed_seen: set[tuple[str, int]] = set()

    for path in files():
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        if EM_DASH not in text:
            continue
        generated = False
        for number, line in enumerate(text.splitlines(), start=1):
            if "BEGIN GENERATED" in line:
                generated = True
                continue
            if "END GENERATED" in line:
                generated = False
                continue
            if generated or EM_DASH not in line:
                continue
            reason = ALLOWED.get((rel, number))
            if reason:
                allowed_seen.add((rel, number))
                continue
            findings.append(f"  {rel}:{number}\n      {line.strip()[:160]}")

    stale = set(ALLOWED) - allowed_seen
    for rel, number in sorted(stale):
        findings.append(
            f"  {rel}:{number}\n      allowlisted but no em dash is there any more; "
            f"remove the entry from ALLOWED in this script"
        )

    if findings:
        print("Em dashes found, and this project does not use them:\n")
        print("\n".join(findings))
        print()
        print("Use a comma, a colon, a full stop, a semicolon, or parentheses.")
        print("If the dash is inside quoted material, allowlist it in this script")
        print("with a reason instead of editing the quotation (AGENT.md section 3).")
        return 1

    print(f"no em dashes in {len(files())} file(s), {len(allowed_seen)} allowlisted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
