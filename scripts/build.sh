#!/bin/sh
# build.sh — build the site, and run the content checks first.
#
# Usage:
#   scripts/build.sh          build into public/
#   scripts/build.sh serve    build, then serve on http://localhost:1313 with live reload
#
# Why this exists rather than a bare `hugo` call:
#
# 1. HUGO_CACHEDIR. Hugo defaults to $HOME/.cache/hugo_cache. In a sandbox or any
#    environment with a read-only $HOME, `hugo` fails with
#    "mkdir ... read-only file system" and exits 1 even though the site built fine.
#    Pointing the cache inside the project fixes that and makes builds reproducible.
#    hugo.toml cannot do this, because cacheDir must be an absolute path.
#
# 2. The checks run FIRST. A page can pass every script and still fail to render (an
#    undefined shortcode is a hard build error, which is how the interactive on
#    /nothing-to-hide/ was caught), so both halves matter. But a broken citation graph
#    should stop the build before Hugo spends time on it.
#
# 3. The contrast check runs here rather than in a browser, because there is no browser
#    (AGENT.md section 7) and because a colour edit that breaks AA should fail the build
#    rather than wait for a reader to notice. It reads the tokens out of assets/css/main.css.
#
# In CI or on statichost.eu, chain the same commands in statichost.yml.

set -e

cd "$(dirname "$0")/.."

export HUGO_CACHEDIR="$PWD/tmp/hugo_cache"
mkdir -p "$HUGO_CACHEDIR"

echo "==> checks"
python3 scripts/check-content.py
python3 scripts/check-dashes.py
python3 scripts/check-contrast.py
python3 scripts/render-bibliography.py --check

# The accessibility check reads public/, so it runs after the build rather than before it.
# That is the one ordering exception in this script, and it is deliberate: everything above
# checks the source, and this checks what the source produced.

# The font subsets are checked rather than rebuilt: rebuilding writes to the working tree,
# and a build that silently rewrites its own inputs is not reproducible. A missing subset
# is quiet rather than loud in a browser (the reader gets the fallback stack and never knows
# the page was meant to look different), which is exactly why it is a check.
python3 scripts/build-fonts.py --check --allow-missing

echo "==> hugo"
if [ "$1" = "serve" ]; then
  exec hugo server --bind 127.0.0.1 --port 1313 --disableFastRender
fi

# The destination is emptied first, and that is deliberate. The stylesheet is fingerprinted,
# so every edit to assets/css/main.css produces a NEW filename, and the old fingerprint would
# otherwise stay in public/ forever, unreferenced but present. `--cleanDestinationDir` does
# not fix it: that flag cleans files not found in the static directories, and Hugo Pipes
# output is not a static file. This bit twice in round 11, because "the site's weight" was
# being measured by summing the files in public/ rather than the files a page references, and
# a stale stylesheet inflated every number by about 1.5 KB. A build whose output directory is
# a pure function of its input cannot mislead that way.
#
# Do not run this while a `hugo server` is running: it has its own in-memory build and
# deleting the output directory underneath it is not supported (AGENT.md gotcha 12).
rm -rf public
hugo --gc --minify
echo "==> built into public/"

echo "==> accessibility, on the built output"
python3 scripts/check-a11y.py
