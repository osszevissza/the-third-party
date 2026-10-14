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

hugo --gc --minify
echo "==> built into public/"
