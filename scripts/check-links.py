#!/usr/bin/env python3
"""
check-links.py: resolve every URL in data/sources.yaml and report its status.

Run:  python3 scripts/check-links.py

A source with `verified_on: null` is an unverified claim. This script resolves the
URL over the network so the field can be filled in honestly rather than assumed.

Status meanings:
  2xx / 3xx   resolves, safe to set verified_on
  401 / 403 / 429   resolves but refuses automated requests (paywall, bot filter).
              A human opening it in a browser will normally see the page, so this
              still counts as a working URL, but open it yourself before claiming
              the content matches what the citation says.
  404 / 410   DEAD. The source is gone. Fix or drop it.
  other / err  inconclusive: retry later, or check by hand.

This script does NOT edit the YAML. Deciding whether a source still supports the
claim it is attached to is an editorial judgement, not an HTTP status code.
"""

from __future__ import annotations

import concurrent.futures
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TIMEOUT = 15
WORKERS = 8
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

OK = "ok"
BLOCKED = "blocked"
DEAD = "dead"
UNKNOWN = "unknown"
UNVERIFIABLE = "unverifiable"


def probe(url: str) -> tuple[str, int | str, str]:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "text/html,*/*"}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return OK, resp.status, resp.geturl()
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403, 429):
            return BLOCKED, exc.code, url
        if exc.code in (404, 410):
            return DEAD, exc.code, url
        return UNKNOWN, exc.code, url
    except Exception as exc:  # noqa: BLE001 - network errors are the point here
        return UNKNOWN, type(exc).__name__, url


def origin_root(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    return f"{parts.scheme}://{parts.netloc}/"


def resolve_bot_blocks(results: list) -> list:
    """Reclassify suspicious 404s as bot-blocks.

    Some sites answer automated requests with 404 rather than 403, ftc.gov does
    this, and its press releases are otherwise perfectly reachable. A URL a search
    engine indexes happily is not dead; the bot is being turned away.

    Heuristic: if the site's own root also fails, the domain blocks us and every
    404 on it is suspect. Returns the ids that were reclassified.
    """
    dead = [r for r in results if r[1] == DEAD]
    if not dead:
        return []

    roots = sorted({origin_root(r[3]) for r in dead})
    root_ok: dict = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(probe, root): root for root in roots}
        for fut in concurrent.futures.as_completed(futures):
            root = futures[fut]
            state, _code, _final = fut.result()
            root_ok[root] = state == OK

    reclassified = []
    for i, (sid, state, code, final) in enumerate(results):
        if state != DEAD:
            continue
        if not root_ok.get(origin_root(final), False):
            results[i] = (sid, BLOCKED, f"{code}?", final)
            reclassified.append(sid)
    return reclassified


def control_probe(results: list) -> list:
    """Test whether a non-OK status code means anything.

    A 403 or 404 from a domain that returns the same code for a path that cannot
    possibly exist tells us NOTHING about whether our URL is live. Reuters answers
    401, DLA Piper 429, and ACM, the NYT, Lexology, loc.gov and ftc.gov all answer
    403 or 404 for any path at all, including their own roots.

    So for every blocked or dead result, request a deliberately bogus path on the
    same origin. If the status matches, the code is uninformative and the source
    is UNVERIFIABLE by automation: a human has to open it. Reporting those as
    "blocked, but probably fine" is how a link checker quietly manufactures
    false confidence.

    Returns the ids downgraded to UNVERIFIABLE.
    """
    suspect = [
        (i, r)
        for i, r in enumerate(results)
        if r[1] in (BLOCKED, DEAD) and isinstance(r[2], int)
    ]
    if not suspect:
        return []

    targets = {}
    for i, (sid, state, code, final) in suspect:
        bogus = origin_root(final) + "zzz-unlikely-path-9f3a/"
        targets[i] = bogus

    bogus_code: dict = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(probe, u): i for i, u in targets.items()}
        for fut in concurrent.futures.as_completed(futures):
            i = futures[fut]
            state, code, _final = fut.result()
            bogus_code[i] = code if isinstance(code, int) else state

    downgraded = []
    for i, (sid, state, code, final) in suspect:
        if bogus_code.get(i) == code:
            results[i] = (sid, UNVERIFIABLE, code, final)
            downgraded.append(sid)
    return downgraded


def main() -> int:
    entries: list[dict] = []
    for path in sorted(DATA.glob("*.y*ml")):
        parsed = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        entries += [e for e in parsed if isinstance(e, dict)]

    with_url = [e for e in entries if e.get("url")]
    no_url = [e for e in entries if not e.get("url")]

    print(f"probing {len(with_url)} URL(s), {WORKERS} at a time...\n")

    results: list[tuple[str, str, int | str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {
            pool.submit(probe, e["url"]): e for e in with_url
        }
        for fut in concurrent.futures.as_completed(futures):
            e = futures[fut]
            state, code, final = fut.result()
            results.append((e["id"], state, code, final))

    order = {OK: 0, DEAD: 1, UNKNOWN: 2, UNVERIFIABLE: 3, BLOCKED: 4}
    reclassified = resolve_bot_blocks(results)
    downgraded = control_probe(results)
    results.sort(key=lambda r: (order[r[1]], r[0]))

    glyph = {
        OK: "OK  ",
        BLOCKED: "BLCK",
        DEAD: "DEAD",
        UNKNOWN: "????",
        UNVERIFIABLE: "N/A ",
    }
    for sid, state, code, final in results:
        note = ""
        if final and final.rstrip("/") != (next((e["url"] for e in with_url if e["id"] == sid), "")).rstrip("/"):
            note = f"  -> {final}"
        print(f"  {glyph[state]} {str(code):>4}  {sid}{note}")

    counts = {k: sum(1 for r in results if r[1] == k) for k in order}
    print()
    print(
        f"{counts[OK]} resolving, {counts[BLOCKED]} bot-blocked, "
        f"{counts[DEAD]} dead, {counts[UNKNOWN]} inconclusive, "
        f"{counts[UNVERIFIABLE]} unverifiable"
    )

    if downgraded:
        print(
            f"\n{len(downgraded)} source(s) CANNOT be verified automatically. The domain\n"
            "returns the same status for a path that cannot exist, so the code proves\n"
            "nothing. These must be opened by hand before publishing:\n"
        )
        for sid in downgraded:
            print(f"  - {sid}")

    if no_url:
        print(f"\n{len(no_url)} source(s) have no URL at all:")
        for e in no_url:
            print(f"  MISSING  {e['id']}")

    if reclassified:
        print(
            f"\n{len(reclassified)} 404(s) treated as bot-blocking rather than dead,\n"
            "because the domain root also refused us:\n"
        )
        for sid in reclassified:
            print(f"  - {sid}")

    dead = [r[0] for r in results if r[1] == DEAD]
    if dead:
        print("\nDead links must be fixed or the source dropped:")
        for sid in dead:
            print(f"  - {sid}")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
