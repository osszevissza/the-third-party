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
# In CI or on statichost.eu, chain the same commands in statichost.yml.

set -e

cd "$(dirname "$0")/.."

export HUGO_CACHEDIR="$PWD/tmp/hugo_cache"
mkdir -p "$HUGO_CACHEDIR"

echo "==> checks"
python3 scripts/check-content.py
python3 scripts/check-dashes.py
python3 scripts/render-bibliography.py --check

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
