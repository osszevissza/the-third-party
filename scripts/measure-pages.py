#!/usr/bin/env python3
"""measure-pages.py: measure what each built page actually weighs.

    sh scripts/build.sh          # build first: this script reads public/, it does not build
    python3 scripts/measure-pages.py

Why this exists: the site sets itself a budget of under 100 KB per page (AGENT.md section 8),
and a budget nobody measures is a wish. This script prints every built page's weight, the
median, the heaviest page, the ratio between them and the site-wide total, so that a stylesheet
edit or a new source entry cannot quietly push a page past the line.

Until 2026-10-15 these figures were also published on /receipts/. That page was dropped at the
maintainer's request, along with /swap-shop/, so nothing on the site publishes its own numbers
any more and this is an internal check rather than the source of a page. It is still worth
running, because the styling pass is the next piece of work and the stylesheet is part of every
page's weight. Run it after any edit to a page or to assets/css/main.css.

Two rules are encoded here, both learned the hard way, and both matter more than the arithmetic:

1. MEASURE WHAT THE PAGE FETCHES, NOT WHAT THE DIRECTORY CONTAINS. A page's weight is the
   document plus the files its own <link> tags reference: the stylesheet and the icon. Summing
   public/ instead inflates every page by the stale fingerprinted stylesheet an edit leaves
   behind, because Hugo Pipes output is not a static file and --cleanDestinationDir does not
   remove it (AGENT.md section 7, gotcha 13).

2. THE SITE-WIDE ROW COUNTS THE SHARED FILES ONCE. The stylesheet and the icon are counted once
   each rather than once per page, which is the only reading under which the shared files are
   not double-counted.

The carbon figures apply the published Sustainable Web Design model to the measured bytes
rather than measuring anything: 0.300 kWh/GB at 494 gCO2e/kWh, so 148 grams of CO2e per
gigabyte. Both decimal GB and GiB are printed, because the difference is about 7% and which one
to quote is the maintainer's call (AGENT.md section 10). Nothing on the site publishes these
numbers, so they are printed rather than resolved.
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
BUDGET = 100 * 1024  # the per-page budget in AGENT.md section 8


def gz(data: bytes) -> int:
    """Gzipped size at level 9, mtime zeroed so runs are comparable."""
    return len(gzip.compress(data, 9, mtime=0))


# Rel values whose <link> the browser actually fetches. This used to name stylesheet and
# icon only, which was every linked asset the site had until 2026-10-15. The styling pass
# added preloaded fonts, and a preload is a request like any other: leaving it out would
# under-report every page by the body face, which is the exact class of error rule 1 above
# exists to prevent.
FETCHED_RELS = ("stylesheet", "icon", "preload")

# Extensions a stylesheet can pull in through url(). The self-hosted fonts are referenced
# from assets/css/main.css, so a page's request list is not complete without following the
# stylesheet one level. One level is enough and is all that is done: the site has no
# @import and no second stylesheet.
CSS_ASSET_RE = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)")


def resolve(ref: str, base: str = "") -> str | None:
    """Turn a reference into a path relative to public/, or None if it is not ours.

    Absolute URLs are skipped rather than counted: the site makes no third-party requests,
    so a hit here would itself be the finding.
    """
    ref = ref.strip()
    if not ref or ref.startswith(("http://", "https://", "//", "data:")):
        return None
    if ref.startswith("/"):
        return ref.lstrip("/")
    return f"{base}{ref}" if base else ref


def assets_of(html: str, root: pathlib.Path | None = None) -> list[str]:
    """Every file the page fetches from this origin, as paths relative to public/.

    The document itself is not included. With `root`, the stylesheet is followed one level
    so its own url() references are counted, because they are part of what a reader
    downloads to see the page.
    """
    refs: list[str] = []
    for tag in re.findall(r"<link\b[^>]*>", html):
        rel = re.search(r'rel=("([^"]*)"|([^\s>]+))', tag)
        rel_value = (rel.group(2) or rel.group(3)) if rel else ""
        if not any(name in rel_value for name in FETCHED_RELS):
            continue
        href = re.search(r'href=("([^"]*)"|([^\s>]+))', tag)
        if href:
            path = resolve(href.group(2) or href.group(3) or "")
            if path:
                refs.append(path)
    if root is not None:
        for ref in list(refs):
            if not ref.endswith(".css"):
                continue
            css_path = root / ref
            if not css_path.is_file():
                continue
            base = ref.rsplit("/", 1)[0] + "/" if "/" in ref else ""
            for url in CSS_ASSET_RE.findall(css_path.read_text("utf-8", "replace")):
                path = resolve(url, base)
                if path:
                    refs.append(path)
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
        for ref in assets_of(raw_html.decode("utf-8", "replace"), ROOT):
            data = (ROOT / ref).read_bytes()
            raw_total += len(data)
            gz_total += gz(data)
        rows.append((str(page.relative_to(ROOT)), raw_total, gz_total))

    rows.sort(key=lambda r: r[2])
    print(f"{'page':34} {'raw':>8} {'gzip':>7}")
    for name, raw, gz_size in rows:
        print(f"{name:34} {raw:8d} {gz_size:7d}")

    median_gz = int(statistics.median([r[2] for r in rows]))
    median_raw = int(statistics.median([r[1] for r in rows]))
    heaviest = max(rows, key=lambda r: r[2])
    heaviest_raw = max(rows, key=lambda r: r[1])

    # The site-wide row is the documents plus the shared files (stylesheet, fonts, icon),
    # counted once each, which is the only reading under which they are not double-counted.
    shared = {}
    for ref in assets_of((ROOT / "index.html").read_text(), ROOT):
        shared[ref] = gz((ROOT / ref).read_bytes())
    site_gz = sum(gz((ROOT / r[0]).read_bytes()) for r in rows) + sum(shared.values())

    print()
    print(f"pages measured               {len(rows)}")
    print(f"median page                  gzip {median_gz}   raw {median_raw}")
    print(f"heaviest page                {heaviest[0]}  gzip {heaviest[2]}   raw {heaviest_raw[1]}")
    print(f"ratio heaviest / median      {heaviest[2] / median_gz:.2f}")
    print(f"all pages + shared assets    {site_gz} bytes = {site_gz / 1024:.1f} KiB")
    print()
    print(f"budget, {BUDGET} bytes per page:")
    print(f"  as transferred (gzip)      {'met' if heaviest[2] <= BUDGET else 'OVER BUDGET'}"
          f"  (heaviest {heaviest[2]})")
    print(f"  as raw bytes               {'met' if heaviest_raw[1] <= BUDGET else 'OVER BUDGET'}"
          f"  (heaviest {heaviest_raw[1]})")
    print()
    print("carbon, from the median page and the model (148 g CO2e per GB):")
    for label, divisor, unit in (("decimal GB", DECIMAL_GB, "GB"),
                                 ("binary GiB", BINARY_GB, "GiB")):
        median_mg = median_gz / divisor * GRAMS_PER_GB * 1000
        heaviest_mg = heaviest[2] / divisor * GRAMS_PER_GB * 1000
        site_mg = site_gz / divisor * GRAMS_PER_GB * 1000
        print(f"  {label:38} median {median_mg:.2f} mg  heaviest {heaviest_mg:.2f} mg  site {site_mg:.2f} mg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
