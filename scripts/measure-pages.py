#!/usr/bin/env python3
"""measure-pages.py: re-measure the figures published on /receipts/.

    sh scripts/build.sh          # build first: this script reads public/, it does not build
    python3 scripts/measure-pages.py

Why this exists as a script rather than a shell one-liner: the numbers on /receipts/ are
published as exact and reproducible, and every time they were taken by hand in round 11 and
the sessions after it, the method drifted or a definition was quietly forgotten. Two of those
drifts are now encoded here so they cannot recur.

3. MEASURE WHAT THE PAGE FETCHES, NOT WHAT THE DIRECTORY CONTAINS. A page's weight is the
   document plus the files its own <link> tags reference: the stylesheet and the icon. Summing
   public/ instead inflates every page by the stale fingerprinted stylesheet an edit leaves
   behind, because Hugo Pipes output is not a static file and --cleanDestinationDir does not
   remove it (AGENT.md gotcha 13).

2. THE MEDIAN EXCLUDES /receipts/ ITSELF. That page is part of the twelve, so a median
   including it changes whenever the page is edited, and the number would move in a way the
   page cannot observe, because the measurement necessarily happens before the sentence that
   reports it. The published row therefore reads "the other 11". Do not "fix" this back to
   twelve to look tidier: see AGENT.md section 7.

3. THE CARBON FIGURES USE THE PUBLISHED MODEL, NOT A MEASUREMENT. The Sustainable Web Design
   model gives 0.300 kWh/GB and a default grid intensity of 494 gCO2e/kWh, so 148 grams of CO2e
   per gigabyte. This script prints the size in both decimal GB and GiB, and the milligram
   figures for each, because /receipts/ currently divides by 2**30 while writing "GB": that is
   correct as GiB and is flagged as an open question in AGENT.md. Printed, not resolved.
"""

import gzip
import pathlib
import re
import statistics
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "public"
GRAMS_PER_GB = 148.0  # SWD model: 0.300 kWh/GB at 494 gCO2e/kWh
DECIMAL_GB = 1_000_000_000
BINARY_GB = 2**30


def gz(data: bytes) -> int:
    """Gzipped size at level 9, mtime zeroed so runs are comparable."""
    return len(gzip.compress(data, 9, mtime=0))


def assets_of(html: str) -> list[str]:
    """The stylesheet and icon paths the page itself declares, as root-relative strings."""
    refs = []
    for tag in re.findall(r"<link\b[^>]*>", html):
        if re.search(r'rel=(?:"(?:stylesheet|icon)"|(?:stylesheet|icon)\b)', tag):
            href = re.search(r'href=("([^"]*)"|([^\s>]+))', tag)
            if href:
                refs.append((href.group(2) or href.group(3)).lstrip("/"))
    return refs


def main() -> int:
    if not ROOT.is_dir():
        print(f"no build at {ROOT}: run 'sh scripts/build.sh' first", file=sys.stderr)
        return 1

    rows = []
    for page in sorted(ROOT.rglob("index.html")):
        raw_html = page.read_bytes()
        gz_total = gz(raw_html)
        raw_total = len(raw_html)
        for ref in assets_of(raw_html.decode("utf-8", "replace")):
            data = (ROOT / ref).read_bytes()
            raw_total += len(data)
            gz_total += gz(data)
        rows.append((str(page.relative_to(ROOT)), raw_total, gz_total))

    rows.sort(key=lambda r: r[2])
    print(f"{'page':34} {'raw':>8} {'gzip':>7}")
    for name, raw, gz_size in rows:
        mark = "  <- excluded from the median" if name.startswith("receipts/") else ""
        print(f"{name:34} {raw:8d} {gz_size:7d}{mark}")

    others = [r for r in rows if not r[0].startswith("receipts/")]
    median_gz = int(statistics.median([r[2] for r in others]))
    median_raw = int(statistics.median([r[1] for r in others]))
    heaviest = max(rows, key=lambda r: r[2])
    heaviest_raw = max(rows, key=lambda r: r[1])

    # The site-wide row is the twelve documents plus the shared stylesheet and icon, counted
    # once each, which is the only reading under which the shared files are not double-counted.
    shared = {}
    for ref in assets_of((ROOT / "index.html").read_text()):
        shared[ref] = gz((ROOT / ref).read_bytes())
    site_gz = sum(gz((ROOT / r[0]).read_bytes()) for r in rows) + sum(shared.values())

    print()
    print(f"median of the other 11   gzip {median_gz}   raw {median_raw}")
    print(f"heaviest page            {heaviest[0]}  gzip {heaviest[2]}   raw {heaviest_raw[1]}")
    print(f"ratio heaviest / median  {heaviest[2] / median_gz:.2f}")
    print(f"all 12 + shared assets   {site_gz} bytes = {site_gz / 1024:.1f} KiB")
    print()
    print("carbon, from the median page and the model (148 g CO2e per GB):")
    for label, divisor, unit in (("decimal GB", DECIMAL_GB, "GB"),
                                 ("binary GiB (what /receipts/ publishes)", BINARY_GB, "GiB")):
        median_mg = median_gz / divisor * GRAMS_PER_GB * 1000
        heaviest_mg = heaviest[2] / divisor * GRAMS_PER_GB * 1000
        site_mg = site_gz / divisor * GRAMS_PER_GB * 1000
        print(f"  {label:38} median {median_mg:.2f} mg  heaviest {heaviest_mg:.2f} mg  site {site_mg:.2f} mg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
