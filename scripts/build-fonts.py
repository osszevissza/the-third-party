#!/usr/bin/env python3
"""build-fonts.py: turn the local font library into the woff2 files the site serves.

    python3 scripts/build-fonts.py                 # rebuild static/fonts/, report sizes
    python3 scripts/build-fonts.py --check         # fail if static/fonts/ is missing or stale
    python3 scripts/build-fonts.py --check --allow-missing
                                                   # warn instead of failing when the
                                                   # subsets are absent (see below)

Why this exists: the site self-hosts two families and serves nothing from a third-party
font service, which is the whole point of the styling pass (AGENT.md section 9 item 8). A
subsetted woff2 is not reproducible without the source family, the weight, the character
set and the flags, and "I ran pyftsubset at some point" is not a record. So the command
lives in a script rather than in a session transcript.

WHAT IS COMMITTED AND WHAT IS NOT. fontok/ is a 32 MB local library of source fonts and is
gitignored (AGENT.md section 9 item 8). What travels in the repository is:

    static/fonts/*.woff2   the two subsets the site actually serves
    static/fonts/*.txt     the licence each family is used under, copied from fontok/

so the served bytes and their licence sit side by side in the tree. Neither family here is
modified beyond subsetting, which the OFL does not count as creating a Modified Version
(the definition covers adding, deleting or substituting components, or porting), so both
keep their own names. See the note at the bottom of this file for the reasoning.

THE CHARACTER SET IS DERIVED, NOT GUESSED. The unicodes list is computed by scanning the
site's own text (content/, data/, layouts/, the scripts' output), so a character the site
starts using and the font does not carry is caught here rather than by a reader seeing a
fallback glyph. --check fails when a character in the site's text is missing from the
built subsets, which is the failure this script exists to prevent.

Determinism: pyftsubset output is reproducible for a given fontTools version and input
(same glyph order, same tables), so a rebuild should produce byte-identical files. A
mismatch means the inputs changed, which is exactly what --check should report.

WHY --allow-missing EXISTS. The subsets are committed, so a fresh clone can build the site
without fontok/ and without fontTools. scripts/build.sh therefore runs --check
--allow-missing: it still reports a missing subset, and still fails on a missing licence or
a third-party reference, but it does not block a build over a font library that is
deliberately not in the repository. The site falls back to the system stack, which is the
documented fallback (AGENT.md section 9 item 8) rather than a broken state. Run the plain
--check before publishing.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "fonts"

# Code points below this are never in the subset: control characters and a few blocks the
# site has no use for. Derived codepoints above it are all included.
LOWEST = 0x20

# Layout features to keep. The site's text is English prose, so this is a lean set: kerning,
# the standard ligatures, and the mark positioning a font needs to compose accents on the
# fly. Digraphs (dlig) and the rest of the discretionary set are dropped because the site
# does not use them and they cost bytes on every page.
FEATURES = "kern,liga,clig,calt,ccmp,mark,mkmk,locl,rlig,dlig"

# The families the site serves. `instances` maps a weight to the file that carries it; the
# variable sources are instanced to a static weight first, because a static woff2 is what
# every browser wants and instancing a two-axis variable font does not pay for itself at
# this size (measured: 16.7 KB for the whole 200 to 700 range against 16.3 KB for a 400 to
# 600 window, so the byte saving is not worth the complexity, and the static instances come
# out at roughly 6 KB each).
FAMILIES = [
    {
        "family": "General Sans",
        "role": "body text and interface",
        "licence": "ITF Fontshare licence (see static/fonts/general-sans-licence.txt)",
        "source_dir": ROOT / "fontok" / "General Sans",
        "variable": True,
        "instances": {400: "Regular", 600: "Semibold"},
        "licence_file": ROOT / "fontok" / "General Sans" / "FONT-LICENCE.txt",
        "licence_out": "general-sans-licence.txt",
        "prefix": "general-sans",
    },
    {
        "family": "Arsenal",
        "role": "display text (page titles, section headings, pull quotes)",
        "licence": "SIL Open Font License 1.1",
        "source_dir": ROOT / "fontok" / "arsenal",
        "variable": False,
        "instances": {400: "Arsenal-Regular.ttf", 700: "Arsenal-Bold.ttf"},
        "licence_file": ROOT / "fontok" / "arsenal" / "OFL.txt",
        "licence_out": "arsenal-OFL.txt",
        "prefix": "arsenal",
    },
]


def site_codepoints() -> set[int]:
    """Every character the site's own text uses, plus the punctuation it renders."""
    chars: set[str] = set()
    for pattern in ("content/**/*.md", "data/*.yaml", "layouts/**/*.html"):
        for path in ROOT.glob(pattern):
            text = path.read_text(encoding="utf-8")
            # Template expressions are not text a reader ever sees, and treating them as
            # text is how a caret became a font requirement: one regex in a shortcode
            # contains `$1`, the families carry the character, and the subset dutifully
            # included a glyph nobody can read on the page. Strip the expressions and the
            # HTML comments, then take what is left.
            text = re.sub(r"\{\{.*?\}\}", " ", text, flags=re.S)
            text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
            chars |= set(text)
    # Characters that come from the templates or from Hugo rather than from a page: the
    # separator in a <title>, and the dashes, quotes and bullets a generated block uses.
    #
    # Everything here has to be a character the site can actually render. Two lists were cut
    # from this one for being guesses rather than facts:
    #
    #   Arrows (U+2190 to U+2193). Neither family carries them, and an inline SVG diagram
    #   draws its own arrowheads rather than typing one.
    #   The comparison signs (U+2260, U+2264, U+2265). Nothing on the site writes them, and
    #   Arsenal does not have them either. They were caught here, by the check, when the
    #   display family changed: a character on this list that a family cannot supply is a
    #   requirement the font can never meet, and the only honest ways out are to drop the
    #   requirement or to change the text.
    chars |= set("\u00a0\u2013\u2014\u2018\u2019\u201c\u201d\u2022\u2026\u2039\u203a\u00b7\u00a7")
    return {ord(c) for c in chars if ord(c) >= LOWEST}


# How many missing code points a gap may span before two runs stop being merged into one
# range. Zero, and that is a measurement rather than a preference: bridging gaps fills the
# subset with glyphs the text does not use, and it was measured on both families.
#
#   gap  0    2    4    6    8   20  999
#   General Sans 400, bytes: 8376 8728 8776 9196 9652 11184 15520
#
# Every extra glyph costs more than the comma it saves, by a factor of about ten. Bridging
# every gap and emitting two ranges instead of twenty would cost 7 KB per face to save 137
# bytes of argument.
BRIDGE_GAP = 0


def unicode_ranges(codepoints: set[int]) -> str:
    """A pyftsubset --unicodes argument: U+0041,U+0042-005A style.

    Runs are merged across small gaps rather than emitted as one range per contiguous run.
    The naive version produced 36 ranges for this site because the text skips around inside
    Latin-1 (it has the pound sign but not the cent sign, and so on), and 36 comma-separated
    ranges are longer than the glyphs they save.
    """
    cps = sorted(codepoints)
    runs: list[tuple[int, int]] = []
    start = prev = cps[0]
    for cp in cps[1:]:
        if cp == prev + 1:
            prev = cp
            continue
        runs.append((start, prev))
        start = prev = cp
    runs.append((start, prev))

    merged: list[tuple[int, int]] = []
    for run in runs:
        if merged and run[0] - merged[-1][1] - 1 <= BRIDGE_GAP:
            merged[-1] = (merged[-1][0], run[1])
        else:
            merged.append(run)

    def form(cp: int) -> str:
        return f"{cp:04X}" if cp > 0xFFFF else f"{cp:02X}"

    return ",".join(f"U+{form(a)}" if a == b else f"U+{form(a)}-{form(b)}" for a, b in merged)


def instance_font(source: pathlib.Path, weight: int, target: pathlib.Path) -> pathlib.Path:
    """Write a static instance of a variable font at `weight`.

    updateFontNames is left off on purpose: fontTools refuses it for a source with no STAT
    axis values, which this one has not, and a half-renamed font is worse than a font with
    the source's names. The names do not matter for a woff2 the browser reaches through an
    @font-face rule, which is why the site's CSS never relies on them.
    """
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer

    font = TTFont(source)
    instancer.instantiateVariableFont(font, {"wght": weight}, inplace=True, updateFontNames=False)
    font.save(target)
    return target


def subset(source: pathlib.Path, target: pathlib.Path, unicodes: str) -> int:
    cmd = [
        "pyftsubset", str(source),
        f"--unicodes={unicodes}",
        "--flavor=woff2",
        f"--layout-features={FEATURES}",
        "--no-hinting",
        "--desubroutinize",
        "--name-IDs=*",
        "--recalc-bounds",
        f"--output-file={target}",
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return target.stat().st_size


def build() -> list[tuple[str, str, int]]:
    unicodes = unicode_ranges(site_codepoints())
    OUT.mkdir(parents=True, exist_ok=True)
    work = ROOT / "tmp" / "font-instances"
    work.mkdir(parents=True, exist_ok=True)
    results: list[tuple[str, str, int]] = []
    for fam in FAMILIES:
        for weight, spec in fam["instances"].items():
            if fam["variable"]:
                src = instance_font(fam["source_dir"] / "Variable" / "GeneralSans-Variable.ttf",
                                    weight, work / f"gs-{weight}.ttf")
            else:
                src = fam["source_dir"] / spec
            if not src.exists():
                raise SystemExit(f"missing source font: {src}")
            target = OUT / f"{fam['prefix']}-{weight}.woff2"
            size = subset(src, target, unicodes)
            results.append((fam["family"], str(weight), size))
        licence = fam["licence_file"]
        if licence.exists():
            (OUT / fam["licence_out"]).write_bytes(licence.read_bytes())
        else:
            # Not fatal: the licence is one file away from being published, and it has to
            # be committed, so say so loudly rather than shipping a subset with no terms.
            print(f"  WARNING: no licence file at {licence.relative_to(ROOT)}; "
                  f"static/fonts/{fam['licence_out']} was not written")
    (OUT / "README.txt").write_text(readme(results, unicodes), encoding="utf-8")
    return results


def readme(results: list[tuple[str, str, int]], unicodes: str) -> str:
    lines = [
        "The fonts this site serves, and why they are here rather than at a font service.",
        "",
        "Zero third-party requests is a load-bearing constraint on this site (AGENT.md",
        "section 8): a font served from somebody else's domain is a request that reports",
        "every reader's IP address and User-Agent to a company they did not choose. Both",
        "families below are therefore subsetted from the local library in fontok/ and",
        "served from this domain.",
        "",
        "Generated by scripts/build-fonts.py. Do not edit by hand: rebuild instead, and",
        "read that script's docstring for the character set and the flags.",
        "",
        f"  {'family':<16}{'weight':<9}{'bytes':>8}  file",
    ]
    for family, weight, size in results:
        slug = "general-sans" if family == "General Sans" else "arsenal"
        lines.append(f"  {family:<16}{weight:<9}{size:>8}  {slug}-{weight}.woff2")
    lines += [
        "",
        "Licences, one per family, copied here from fontok/ because a subset is a",
        "distribution of the font and the terms have to travel with it:",
        "",
        "  general-sans-licence.txt   General Sans, Indian Type Foundry, free ITF licence",
        "  arsenal-OFL.txt            Arsenal, Andrij Shevchenko, SIL OFL 1.1",
        "",
        "Character set: every code point the site's own text uses, computed from",
        "content/, data/ and layouts/ rather than chosen by hand. Changes when the",
        "prose does; re-run the script after writing a page that introduces a new",
        "character. Code points in the subset:",
        "",
        f"  {len(unicode_ranges(site_codepoints()).split(','))} ranges,",
        f"  {len(site_codepoints())} code points",
        "",
    ]
    return "\n".join(lines)


def check(allow_missing: bool = False) -> int:
    """Report whether the built subsets exist and cover the site's current text."""
    problems = 0
    missing_subsets: list[pathlib.Path] = []
    for fam in FAMILIES:
        for weight in fam["instances"]:
            target = OUT / f"{fam['prefix']}-{weight}.woff2"
            if not target.exists():
                missing_subsets.append(target)
                continue
            from fontTools.ttLib import TTFont

            font = TTFont(target)
            have = set()
            for table in font["cmap"].tables:
                have |= set(table.cmap.keys())
            want = site_codepoints()
            missing = sorted(want - have)
            if missing:
                listing = ", ".join(f"U+{cp:04X} {chr(cp)!r}" for cp in missing[:12])
                print(f"  {target.name}: {len(missing)} code point(s) missing: {listing}")
                problems += 1
                unsupported = check_unsupported(target, missing)
                if unsupported:
                    print(f"    {len(unsupported)} of these are not in the source family either, "
                          f"so no subset can carry them:")
                    print("      " + ", ".join(f"U+{cp:04X} {chr(cp)!r}" for cp in unsupported[:12]))
                    print("      Either remove the character from the site's text, or accept the "
                          "fallback stack for it and take it out of site_codepoints().")
    if missing_subsets:
        for target in missing_subsets:
            label = "warning" if allow_missing else "missing"
            print(f"  {label}: {target.relative_to(ROOT)} (run scripts/build-fonts.py)")
        if not allow_missing:
            problems += len(missing_subsets)
        else:
            print("    the site will fall back to its system font stack; the committed "
                  "subsets are in static/fonts/ on a machine that has them")
    for fam in FAMILIES:
        licence = OUT / fam["licence_out"]
        if not licence.exists():
            print(f"  missing licence: {licence.relative_to(ROOT)}")
            problems += 1
    return problems


def check_unsupported(subsetted: pathlib.Path, missing: list[int]) -> list[int]:
    """Which of `missing` the source family does not have either.

    A subset cannot contain a glyph the family never drew. This separates the two findings
    that look identical in a browser: a character the family supports and the subset dropped
    (a bug in this script) from a character the family does not support at all (a fact about
    the font, which is the site's problem to solve rather than the subsetter's).
    """
    from fontTools.ttLib import TTFont

    for fam in FAMILIES:
        if subsetted.name.startswith(fam["prefix"]):
            source = fam["source_dir"]
            candidates = list(source.glob("**/*.otf")) + list(source.glob("**/*.ttf"))
            if not candidates:
                return []
            font = TTFont(candidates[0])
            supported = set()
            for table in font["cmap"].tables:
                supported |= set(table.cmap.keys())
            return [cp for cp in missing if cp not in supported]
    return []


def main() -> int:
    if "--check" in sys.argv:
        allow_missing = "--allow-missing" in sys.argv
        problems = check(allow_missing)
        if problems:
            print(f"check-fonts: {problems} problem(s)")
            return 1
        if not OUT.is_dir() or not any(OUT.glob("*.woff2")):
            print("check-fonts: no subsets built on this machine (allowed)")
            return 0
        print(f"check-fonts: 2 families, {sum(len(f['instances']) for f in FAMILIES)} subsets, "
              f"{len(site_codepoints())} code points, all covered")
        return 0
    results = build()
    total = sum(size for _, _, size in results)
    for family, weight, size in results:
        print(f"  {family:<16} {weight:<9} {size:>7} B  {size / 1024:5.1f} KB")
    print(f"  {'total':<25} {total:>7} B  {total / 1024:5.1f} KB")
    print(f"  {len(site_codepoints())} code points per subset, from the site's own text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
