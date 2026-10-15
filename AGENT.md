# AGENT.md: working notes for the next session

Read this first. It assumes no memory of previous sessions.

**Session date when written:** 2026-10-15. Run `date -u`. The repository keeps no other
timestamp, and pages carry `status_as_of` fields that need refreshing after a long gap.

**State: the site is live, ten pages, all four checks pass, and the styling pass is next
(§9 item 8).** Nothing is blocked. What is left is the styling, the source worklist in §6,
and the small hosting gaps in §9 item 7.

Three rules about this file itself: no em dashes anywhere (§3), commit messages are a few
words on one line (§7), and the reasoning behind a change belongs here rather than in a
commit body. **History that is not a live constraint has been deliberately cut**; `git log`
and `SITE_PLAN.md` hold the rest.

---

## 0. Orientation in thirty seconds

**The brief.** The maintainer's stated priority, in their own words: **the content quality
must be high enough to include in a portfolio.** It is not a course exercise, and it
outranks speed, page count and completeness. Three consequences:

1. **Never pad.** A page that exists to fill an outline slot is worse than a missing page,
   and an honest "I could not verify X" is worth more than a confident sentence without a
   source.
2. **Never overstate.** One invented statistic, or one `verified_on` that was not actually
   verified, costs more credibility than the page adds.
3. **Keep pages readable.** Roughly 2,400 words is a prompt to ask whether a page has earned
   its length, not a wall: `/consent-theatre/` (2,996) and `/nothing-to-hide/` (3,009) are
   both deliberate. `/sources/` is exempt because it is a bibliography. **Never cut good
   content to hit a number**, and the nine-objection page is a ceiling in the sense that a
   tenth objection needs something else to go.

The project was **someone else's idea**, a friend of the maintainer, and that friend has a
say in the voice. That is settled (§1).

**What the project is.** A static Hugo site arguing that the web is more extractive than it
looks, built to **pass its own test**: no third-party requests, no cookies, no consent
banner, WCAG AA. **Working title:** *The Third Party*. **Live at
[third-party.statichost.page](https://third-party.statichost.page/)** since 2026-10-14,
served by statichost.eu from the public GitHub repository. **Author and licence:** Underdog
Guild ([barsimarina.hu](https://barsimarina.hu)), site text under **CC0 1.0** apart from
quotations, which stay with their sources. Both were supplied by the maintainer, so do not
invent a different author string or licence.

**State:** ten pages, which is every page the site intends to have: the home page plus nine
content pages, 26,895 words of body text by the count in §5, 58 sources, four checks, a
build that renders every page with no errors. Three pages have been dropped: `/the-rules/`
(round 11), then `/swap-shop/` and `/receipts/` on 2026-10-15 at the maintainer's request,
after a conversation with the friend who originated the project (§5). **The site is live,
but the live site is one deploy behind** until the maintainer triggers one (§7).

**Read next:** `FOR-REVIEW.md` (concept, and the outcome of the review), `SITE_PLAN.md`
(full IA and rationale, including the outlines of the dropped pages), then the header of
`data/sources.yaml` (citation rules).

---

## 1. The voice decision: CLOSED on 2026-10-14

The friend reviewed both drafts of `/nothing-to-hide/` and agreed with the both-by-purpose
recommendation. This is the house style:

> **B's shape for objection pages**, the ones a reader arrives at with a *doubt*:
> standalone units, each headed by the objection in the reader's own words.
>
> **A's shape for explanatory pages**, the ones a reader arrives at with a *question*:
> an essay that builds, with the strongest argument held back.

| Page | Register |
|---|---|
| `nothing-to-hide/` | **B**, merged with A's opening and A's concession section |
| `myths/` | **B**, standalone units, each checkable in a browser |
| `consent-theatre/`, `what-leaves-your-browser/`, `one-page-load/`, `analytics/` | **A** |
| `start-here/`, `dark-patterns/` | reference: lists of records |
| `sources/` | reference: generated, never argued |

`drafts/README.md` records the decision with the per-page reasoning. **Do not re-open the
fork**, and if a new objection page is ever added it takes B's shape.

`content/nothing-to-hide/index.md` is the B shape rather than a third draft: it opens on the
AOL set piece, answers **nine** objections (the ninth, "It's my data. If I don't mind, that's
the end of it", came from the friend and is the best addition anyone has made, because "I
don't mind" says nothing about the person whose number you just handed over), keeps a short
"where this page is wrong" section, and cites 15 sources, all declared and all cited inline.

**The old Draft A text is deliberately gone.** It used to sit in `Archívum.tar.gz`, which the
maintainer removed and confirmed was temporary, along with two stale duplicates in the repo
root. Do not look for it and do not reconstruct it from memory: the adopted shape is the
merged page, and a copy that looks canonical is a trap for the next session.

---

## 2. Commands

```bash
python3 scripts/check-content.py   # frontmatter, YAML, citation graph. exit 1 on error
python3 scripts/check-links.py     # resolves every source URL. exit 1 only if truly dead
python3 scripts/check-dashes.py    # house punctuation rule. exit 1 on any em dash
python3 scripts/render-bibliography.py --check   # exit 1 if /sources/ is out of date
```

Run all four before ending a session, and run `render-bibliography.py` **without** `--check`
whenever `data/sources.yaml` or a page's `sources` list changes, because that rewrites the
generated block on `/sources/`.

A fifth script is deliberately not a check and does not run in the build:
`python3 scripts/measure-pages.py` prints every built page's weight, the median, the heaviest
page, the ratio, the site-wide total, both readings of the 100 KB budget and the carbon
estimates, using the referenced-asset method in §7 gotcha 13. **Run it after any edit to a
page or the stylesheet, and always after the styling pass.** Nobody publishes these numbers
any more, so it is an internal check: use it rather than a `du` of `public/`.

**Expected output as of 2026-10-15**, and what the numbers mean:

- `check-dashes.py` → `no em dashes in 21 file(s), 0 allowlisted`. The allowlist is empty and
  that is a real state, not an oversight: the one entry it held claimed a CNIL document title
  was "quoted as published", and the archived copy of CNIL's own page showed the title
  contained no em dash, so the dash had been ours. Generated blocks are skipped by the check,
  since they are machine-written from a file the check already covers. **Add an entry rather
  than editing a quotation**, but only for a dash genuinely inside text a source published,
  and name the snapshot you checked it against. The key is a **line number**, so it goes stale
  the moment `data/sources.yaml` is edited above it: re-verify the text, do not bump the number.
- `check-content.py` → `19 warning(s), 0 error(s)`. Warnings are the source worklist:
  unverified or blanket-blocked URLs awaiting a human, plus one with no URL at all (§6).
  **A falling count is only progress when a link was genuinely opened.** The fall to 19 was
  bookkeeping: `codeberg` left the file with the dropped pages. Round 11's fall by one did
  count, because `edpb-consent-or-pay` gained a URL and a date verified by reading the page.
- `check-links.py` → `45 resolving, 6 bot-blocked, 0 dead, 0 inconclusive, 6 unverifiable`,
  plus 4 URLs whose 404 was treated as bot-blocking because the domain root refused too.
  **`unverifiable` is not a pass**: it means the status code proved nothing and a human must
  open the link (§7 gotcha 2). **Treat any single run as a snapshot, not a result.** Three runs
  in one session over a file that was only growing gave `47/7/0/4/6`, `48/8/0/3/5` and
  `53/7/0/3/6`, so never quote one as a measure of the site's health. Two verdicts are known
  bugs rather than results: `cjeu-planet49` reports `OK 202` while EUR-Lex serves nothing
  readable, and `edpb-consent-or-pay` reports `OK 200` on a host that answers 200 for paths
  that cannot exist, so the evidence there was the page's own title, read by hand.

**Every page must show a perfect citation match**: every declared source cited inline, every
inline citation declared. §7 gotcha 7 has the failure mode that breaks it.

**No check edits anything, deliberately.** Whether a source still supports the claim attached
to it is an editorial judgement, not a status code.

---

## 3. Content architecture

**The spine: every page runs Problem → Pattern → Alternative → Receipt.** Problem is what
happens, with a number or a named script; Pattern is the model behind it and who profits;
Alternative is the less extractive version and what it costs; Receipt is where the claim came
from, dated. Repeating the beats is what makes the site read as designed rather than as a pile
of articles, and it lets a page be cut without the structure failing.

**The page template:** hook (one concrete, surprising, verifiable fact, no preamble) · what is
happening · why it matters and who benefits · **the other side, stated fairly** (never skip
this) · what you can do · sources via `{{< source-list >}}`. Frontmatter is TOML (`+++`) and
requires `title`, `description`, `status_as_of`, `weight`, `sources`.

**Voice rules: these are the product, not decoration.**

- Second person, present tense, short sentences.
- **Concrete beats abstract every time.** Not "trackers collect data" but "this page sent 47
  requests before you scrolled".
- **Punch up at systems, never down at users.** The reader is not stupid; the design is
  hostile. That is the whole difference between advocacy and smugness.
- **No doom without an action.** Every page ends with something to do, however small.
- **Steelman before dismantling.** Explain why a small business uses Google Analytics before
  explaining why it might not.
- **Organise around problems, never tools.** A "top 10 private tools" list is the weakest
  possible version of this project: it teaches nothing and dates instantly.
- **No vendor worship.** Disclose your own choices.
- **No em dashes.** Use a comma, a colon, a full stop, a semicolon or parentheses instead. The
  site contains none, and `check-dashes.py`'s allowlist is empty (§2). **Text inside quotation
  marks that quotes a source, a law or a company stays exactly as published**, dash and all,
  because a quotation you have tidied is no longer a quotation. If a sentence collapses
  without a dash, restructure the sentence.

**Structural rules that keep pages from collapsing.**

- One claim, one citation, attached where the claim is made. Never bolt a cluster of citations
  onto a sentence that does not need them.
- One idea per section, and let a section be short.
- Concede real ground in a dedicated section. `/nothing-to-hide/` and
  `/what-leaves-your-browser/` both do this, and it is what earns the right to argue.
- Use dividers with intent: `/nothing-to-hide/` uses `---` in exactly two places so the nine
  answers read as one sequence rather than nine database entries.

---

## 4. Citation discipline: the point of the whole project

`data/sources.yaml` is the **single source of truth**. Pages declare ids in frontmatter and
reference them inline with `{{< cite "source-id" >}}`. The claim that the sources are real,
dated and checkable degrades silently as pages are added, which is why the checks exist.

**Fields.**

- `id`: referenced by pages and by the `cite` shortcode.
- `url`: `null` means **not publishable**. Do not invent or guess one.
- `verified_on`: the date the URL was last confirmed. `null` blocks publishing. **A status
  code is not a confirmation**: control-probe the domain first by requesting a path that
  cannot exist, and if it answers with the same code the code proves nothing (§7 gotchas 2
  and 10).
- `archive`: Wayback snapshot. **10 of the 58 are `null`; 48 are filled**, and the 10 are 9
  with no snapshot anywhere plus `solove-taxonomy`, which has no URL to snapshot. Do not
  re-run the archiving pass over the whole file: it is done, and the 9 blanks were each
  confirmed against six or more well-formed API responses (§6 item 1).
- `weakness`: what the source is bad at. Every source has one; recording it is the difference
  between a bibliography and a decoration.
- `supports`: the specific claims the source can carry.

**Rules.**

- Every factual claim gets a dated, linked source. No exceptions. Anything legal or policy
  also gets a "status as of" line and `status_as_of` frontmatter.
- **Prefer primary sources**: the ruling, the study, the regulator's decision, the project's
  own documentation. News coverage only when it is the only record.
- **When a number cannot be verified, do not state it.** Three deliberate examples on the
  site: the fingerprintability percentage was omitted, readers are told to check current Web
  Almanac figures rather than trusting one "including in this sentence", and the harms page
  describes the mechanism by which someone else's exposure reaches a credit decision while
  saying nothing about how often that happens, because nobody publishes that count.
  **Descriptive honesty beats false precision.**
- **A source on a blanket-blocked domain gets an `archive:` link and `verified_on: null` with
  a comment naming the block.** The archived copy is then what was actually read, and the
  entry says so. Copy that pattern for `ftc.gov`, `nytimes.com`, `dl.acm.org`, `reuters.com`
  and the other domains in §7 gotcha 2.
- **`supports` items must be plain strings.** An unquoted colon in a list item (`- Foo: bar`)
  makes YAML build a mapping, so `/sources/` renders a dictionary where a claim belongs, and
  nothing else notices because the file still parses. One such item sat in `sludge-audits` for
  several rounds before it was found; `check-content.py` now fails on it.
- **Watch for unsourced background knowledge**, the failure mode an AI-written page is most
  prone to. A sentence on the dropped swap-shop page called Quad9 "a non-profit rather than a
  company", which is probably true and was sourced to nothing; the phrase turned out to appear
  only in a *sponsor's quote* on Quad9's homepage, so the clause was cut. The rule catches it:
  if the sentence would need a citation in someone else's article, it needs one here.

---

## 5. File map

```
hugo.toml              site config. Typographer DISABLED on purpose, see §7 gotcha 11
.tool-versions         Hugo pinned to 0.150.0 (there is no Go, so `hugo mod` cannot pin it)
.gitignore             public/, resources/, tmp/, .wayback-work/, .directory, __pycache__/
LICENSE                CC0 1.0 legal code, fetched verbatim, plus a two-line header
FOR-REVIEW.md          concept summary, plus the outcome of the review
SITE_PLAN.md           full IA, page outlines (including the dropped pages), build constraints
AGENT.md               this file
data/sources.yaml      58 sources. SINGLE SOURCE OF TRUTH
scripts/build.sh       checks, then builds. Run the site through this, see below
scripts/check-content.py   frontmatter + citation graph, fails fast on broken data
scripts/check-links.py     network URL resolver with bot-block detection
scripts/check-dashes.py    the house punctuation rule, with a reasoned allowlist
scripts/render-bibliography.py   regenerates the generated block on /sources/ (writes)
scripts/measure-pages.py   page weights against the 100 KB budget (reads public/, never writes)
content/_index.md      the home page
content/<slug>/index.md    one directory per page
layouts/               baseof.html, index.html (home), _default/single.html
layouts/partials/      head.html, nav.html (generated from the page tree), footer.html, source-record.html
layouts/shortcodes/    cite.html, source-list.html, interactive.html
assets/                css/main.css, favicon.svg (Hugo Pipes: minify + fingerprint)
drafts/README.md       the voice decision, and the reasoning behind it
drafts/nothing-to-hide--B-objections.md   the adopted shape, marked superseded
```

### Build

```bash
sh scripts/build.sh          # checks, then builds into public/
sh scripts/build.sh serve    # checks, then http://localhost:1313 with live reload
```

**Always build through `scripts/build.sh`, not a bare `hugo`.** It sets `HUGO_CACHEDIR` to
`tmp/hugo_cache`, because Hugo's default is `$HOME/.cache/hugo_cache` and where `$HOME` is
read-only a bare `hugo` fails with `mkdir ... read-only file system` and **exits 1 even though
the site rendered fine** (`cacheDir` cannot fix this in `hugo.toml`: it requires an absolute
path, which would make the config machine-specific). It also runs the four checks first, which
matters because a page can pass every script and still fail to render.

**Traps found while building it, all still live:**

- **`{{< cite >}}` numbers by frontmatter position.** Marker N is source N in the page's
  `sources` list, and `{{< source-list >}}` numbers the same list the same way. Pages do *not*
  declare sources in first-citation order, so markers jump around (`/nothing-to-hide/` reads
  1, 10, 9, 2, 3): cosmetic, consistent, every link resolves, left alone on purpose. The check
  that matters is that marker N resolves to entry N.
- **`.Site.Data.sources` is a slice, not a map.** `index .Site.Data.sources "id"` fails. The
  id-to-record map has to be built with a loop, and it cannot live in a partial because Hugo
  cannot return a value from one, so the `source-list` shortcode builds it and passes it down.
- **Do not use `reflect.IsTime` on these dates.** Hugo returns a **string** for `2019-10-01`
  and an **int** for a bare year like `2016`, never a `time.Time`, and `reflect.IsTime` errors
  on an `interface{}`. `printf "%v"` renders every case correctly. Probed, not assumed.
- **The menu is generated, because a hand-written one lied.** It ranges over
  `.Site.RegularPages.ByWeight` and takes its label from an optional `nav` frontmatter field,
  so a page cannot be left out and a page can be headed "Nine Things People Say" while
  appearing as "Nothing to hide". A page without a label falls back to its title, and the
  current page is marked `aria-current="page"`. Two of the pages that were once missing from
  the old hand-written list have since been dropped, and the generated menu followed with no
  edit: nine links, in weight order, no gap.
- **When checking minified output, accept both attribute forms.** `--minify` strips quotes
  from simple attributes (`<sup class=cite>`), so a quote-only regex reports zero citations on
  a page that has seventeen.

### Page inventory

All ten pages, measured on 2026-10-15 as body words after frontmatter, whitespace-split,
generated text included:

| Page | Words | Shape |
|---|---|---|
| `sources/` | 8,870 | reference. *Mostly generated from `data/sources.yaml`* |
| `nothing-to-hide/` | 3,009 | B, merged: nine objections, A's opening and concession, two harms argued |
| `consent-theatre/` | 2,996 | A, explanatory, with the static eight-click walkthrough |
| `dark-patterns/` | 2,351 | field guide, 17 patterns |
| `what-leaves-your-browser/` | 1,979 | A |
| `one-page-load/` | 1,922 | A. *Is itself the interactive's fallback* |
| `myths/` | 1,671 | B-style units, 7 myths |
| `analytics/` | 1,597 | A, practical |
| `start-here/` | 1,148 | reference |
| `/` (home) | 704 | thesis, three doors, no-banner callout |

The count is reproducible and is the one measurement this file uses:

```bash
awk 'BEGIN{fm=0} /^\+\+\+$/{fm++; next} fm>=2' content/_index.md content/*/index.md | wc -w
```

### The three dropped pages, and what went with them

All three were written and published before the maintainer asked for them to go, and none was
replaced by anything. That is a decision, not an oversight. **Their outlines and the reasoning
survive in `SITE_PLAN.md` §4**, so a later session does not re-add them out of tidiness.

- **`/the-rules/`** (round 11). It is the one page whose whole value is being current, on a
  site whose footer says it is not maintained on a schedule, and its argument is already
  carried by `/consent-theatre/`, `/nothing-to-hide/` section 3 and `/analytics/`.
- **`/swap-shop/`** (2026-10-15), 2,705 words over eight substitutions. Its fifteen sources
  were the only thing in the file nothing else used: twelve were cited by no other page and
  were deleted the same day. **The search material survives in reduced form** in the
  `/sources/` disclosure. Nothing else on the site carries the swap argument, so treat "which
  tools do I use instead" as a deliberate gap rather than a page somebody forgot to write.
- **`/receipts/`** (2026-10-15), 1,338 words of the site's own measured numbers, already cut
  from 3,129 on 2026-10-14. Its content is gone rather than moved, so **no page publishes the
  site's own figures any more**, and the three defects it published (unmarked foreign-language
  text, WCAG 3.1.2; citation markers below the 2.5.8 target size; no
  `content-security-policy`) are tracked in §6 and §9 instead. The home page lost its receipts
  section, and `measure-pages.py` survives as an internal check (§2).

### Page notes worth carrying

- **`/sources/` is the one page exempt from the length rule** (§0): a bibliography, 8,870
  words, most of it generated in four groups plus a reverse index. The generated block sits
  between two HTML markers and is written by `scripts/render-bibliography.py`; **never edit
  inside the markers by hand**, because the next run overwrites it. The markers also make the
  page splittable: moving the block to `/sources/bibliography/` is one path constant in the
  script, not a rewrite. The disclosure headed **"What I actually run"** cites
  `ecosia-eusp-index`, `mullvad-public-dns` and `mullvad-dns-shutdown`, which is why those
  three stayed in the file when the other twelve swap-shop sources went. **The Ecosia caveat
  is load-bearing and must not be trimmed**: it is the company's own account, published in
  French, and it establishes only that the joint index Ecosia built with Qwant exists and that
  French users are served from it directly, saying nothing about coverage elsewhere or result
  quality.
- **The interactives have no scripts, and that is the correct state.** Two were planned
  (`SITE_PLAN.md` §5). `layouts/shortcodes/interactive.html` renders any content as static
  HTML inside `<section class="interactive" data-interactive>`, so the enhancement hook and
  the no-JavaScript fallback are the same thing. Use it as
  `{{< interactive >}} ... {{< /interactive >}}`. `/consent-theatre/`'s "Eight clicks through
  one banner" is the model: an eight-step walkthrough where **every step is a defect the EDPB
  Cookie Banner Taskforce recorded**, ordered the way a user meets them, with the page saying
  out loud that it is a composite and not a measurement. The planned 47-click counter was
  abandoned because a counter has to count something real, and inventing "47" is exactly the
  false precision §4 forbids. **If a real click count is ever measured, add it as
  enhancement**; do not replace the sourced content with it.
- **`/nothing-to-hide/` is complete.** The seven harms are listed with a one-line explanation
  and a pointer to the section arguing each, and the two that had only been named, `secondary
  use` and `dignity`, are written out in "Two harms that needed arguing". Two things to know
  before quoting it: the dignity passage is labelled in the prose as the page's only normative
  claim, and its factual predicates rest on two sources that still carry `verified_on: null`
  (`ftc-data-brokers-2014`, `zuboff-surveillance-capitalism`), which the page displays next to
  them. The `secondary use` passage leans on `google-build-profiles`, whose own record says to
  quote it verbatim, so it is quoted.
- **`/one-page-load/`'s timed request ledger *is* the fallback** the interactive needs: render
  the `<ol>` of requests from that content and let the scroll animation merely enhance it. Do
  not move the sequence into a JS data structure and leave the prose behind.
- **Weights:** `weight = 3` is duplicated on `one-page-load` and
  `what-leaves-your-browser` and nothing depends on the order, so leave it. Dropping pages left
  8 and 11 unused, which is harmless: the menu orders by weight and never displays it. New
  pages take an unused weight, and do not renumber nine pages to close the gap.
- **Should-tier pages** (build if time): accessibility, sustainability, attention, open-source,
  ai-crawl, browser-power, subscriptions, decision-guide, glossary, tracker.

---

## 6. Known issues & worklist

**Blocking publication. Item numbers are stable: other files refer to them.**

1. **`archive:` is `null` on 10 of the 58 sources.** The 10 are **not a to-do that another
   pass will fix**: 9 have no Wayback snapshot anywhere (`netflix-prize`,
   `eckersley-fingerprinting`, `ecc-encrypted-client-hello`, `austrian-dsb-google-analytics`,
   `ga4-consent-mode`, `plausible`, `matomo`, `ftc-amazon-25b`,
   `ftc-click-to-cancel-rosca`) and `solove-taxonomy` has no URL to snapshot. Two things make
   this cheaper than it looks. **Save Page Now works over plain HTTP with no account**:
   `curl -sSL "https://web.archive.org/save/<url>"`, then fetch the returned snapshot and
   check its title rather than trusting the tool. And **use the CDX API** to establish whether
   a snapshot exists at all (§7 gotcha 10), because the availability API has returned empty on
   eight consecutive passes for a URL with a working snapshot, so a blank from it is not a
   negative.
2. **Sources that need a human to open them**, because their domains answer any path with the
   same 401/403/404 and the code proves nothing (§7 gotcha 2). Five are unverifiable
   (`ali-ad-delivery`, `eckersley-fingerprinting`, `penney-chilling`, `ftc-amazon-25b`,
   `ftc-click-to-cancel-rosca`) and four are treated as bot-blocked after a 404
   (`ftc-mobilewalla`, `ftc-gravy-venntel`, `ftc-surveillance-pricing`,
   `ftc-data-brokers-2014`). **The four CNIL sources left this list on 2026-10-15**, when the
   maintenance block ended, so they can be read and dated by hand now: `cnil-analytics-exemption`,
   `cnil-analytics-self-assessment`, `cnil-dark-patterns-quiz` and `cnil-google-san-2025-004`
   all still carry `verified_on: null` because nobody has done it. **Never set `verified_on`
   without actually opening the link.**
3. **`cjeu-iab-europe-tcf` is a press release, not the judgment.** It carries the holdings and
   the court's disclaimer, so it is usable, but the reasoning is missing. The full judgment is
   readable as an archived EUR-Lex PDF (§7 gotcha 10 has the URL): adding it alongside would
   let `/consent-theatre/` cite the reasoning.
4. **`cjeu-planet49`'s `verified_on` is not evidence.** It was set from a `202` that
   `check-links.py` reports as `OK`, on a domain that returns that code for paths that cannot
   exist. Open it in a browser and record that, or set it to `null` with a comment. The entry
   is used by `/myths/` and `/consent-theatre/`, so it is load-bearing.
5. **`solove-taxonomy` still has no URL.** Solove, *A Taxonomy of Privacy*, 154 U. Pa. L. Rev.
   477 (2006). Only mirrors of the PDF and works citing it have been found, and this project
   does not cite a mirror as the record. Find the publisher's or SSRN's own page. **This is the
   only item in §6 an agent could finish without a human.** (`edpb-consent-or-pay` was the
   other and closed in round 11: it gained a URL, `verified_on: 2026-10-14` and a snapshot.
   Two corrections came with it, both now in the entry: the PDF lives under
   `/system/files/**documents**/2024-04/...`, and the opinion carries an **October 2024
   corrigendum** correcting two paragraphs and five footnotes, which matters because the site
   paraphrases it on two pages.)
6. ~~**No Hugo build exists.**~~ **Closed.** The build exists and renders all ten pages. Kept
   as a stub so the numbering does not shift; if you came looking for a missing piece, it is
   not missing.
7. ~~**Two deliberate gaps on `/sources/`.**~~ **Closed.** The contact route and the tools
   disclosure are both published, and the disclosure is now headed "What I actually run". One
   sub-item is still open and lives in §9 item 4: whether GitHub accepts anonymous issue filing
   on the repository, which decides whether the published contact route can receive anything.

**Nice to have, each a small edit to `data/sources.yaml`.** Each was read and control-probed
before being recorded, so these are upgrades rather than guesses.

- `ccpa-sale-definition` links a third-party mirror. `leginfo.legislature.ca.gov` answers 403
  to everything, but an **archived copy of the official page is readable**:
  `http://web.archive.org/web/20261002012921/https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140`.
- `ec-x-fine-120m` cites ABC News. The Commission's own press release is a readable PDF:
  `https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_2934/IP_25_2934_EN.pdf`.
  The press-corner HTML pages are soft 404s, so use the PDF.
- `cjeu-iab-europe-tcf`: the full judgment is readable as an archived PDF, 17 pages,
  `https://web.archive.org/web/20250224023804/https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=celex:62022CJ0604`.
- `penney-chilling` links Reuters coverage, not the *Berkeley Technology Law Journal* article.
  Replace it and quote the effect size from the paper, which the page deliberately avoids.
- `ecc-encrypted-client-hello`: the author list is only partly confirmed (Hajda, Oezdil), and
  the open-access `dl.ifip.org` copy did not respond, so the IEEE record is linked.
- `austrian-dsb-google-analytics` links a law-firm summary. The primary is case
  DSB-2021-0.586.257.
- **Fines levied against fines collected is verifiable per member state only.** Ireland's
  regulator publishes both (over 4.4 billion euro levied against roughly 20 million collected)
  at `https://www.dataprotection.ie/en/dpc-guidance/decisions/fines`, which control-probes
  cleanly. No EU-wide aggregate was found, so an honest page may state Ireland's figures and
  must not present them as Europe's. Nothing on the site makes this claim.

---

## 7. Environment & gotchas

**Installed:** Hugo `v0.150.0+extended`, Python 3.14.8 with PyYAML 6.0.3, Node v22.22.2
(unused by this build), git 2.56.0, curl 8.18.0, `pdftotext` 26.01.0. Fedora Linux 44.

**Not installed:** Go, so `hugo mod` cannot pin the Hugo version and `.tool-versions` does it
instead. **No headless browser tooling at all** (no Lighthouse, axe, Playwright, Puppeteer,
geckodriver, pa11y), and the flatpak Firefox cannot be launched from an agent shell
(`Unable to allocate instance id`). **The agent cannot see the rendered result**, which is why
no LCP figure or audit score was ever published and why the styling pass has to be reviewed by
the maintainer (§9 item 8).

**Git.** Branch `main`, first commit `09f1643`, remote
`git@github.com:osszevissza/the-third-party.git`, public, with `main` tracking `origin/main`.
**Do not quote a head hash in this file**: use `git log --oneline -1` and expect
`git log origin/main..HEAD` to be empty. Before any future public push, repeat the audit: no
key, token, password or absolute home path in any tracked file, and
`git status --untracked-files=all` showing that every untracked path is ignored rather than
merely unnoticed. **Commit messages are a few words on one line** (§7, and the maintainer
restated it), with one exception: a correction of something already published earns a sentence
saying what was wrong, because a reader may come looking for it.

**A push does not deploy.** The deploy is triggered by hand from statichost's dashboard and has
always worked that way, so the manual step is routine rather than a fault: do not re-diagnose
it, do not look for a webhook setting, and do not spend a session on it. **The consequence is
that the live site is a past version of itself and can be confidently wrong.** Nothing in the
repository says which commit is live, and `last-modified` is not the answer either, because it
is per file and only moves when bytes change. **The check that works is a phrase**: pick one
from the commit, `curl` the page and grep for it, and read the page's own title for a deploy
you are confirming from scratch. Deploy as soon as a published claim changes rather than
batching, because the cost of waiting is a live page that contradicts itself. The 2026-10-15
drop is the largest version of this yet: until a deploy happens, the live site serves the two
pages the repository no longer contains.

**What the host sends**, measured from outside: HTTP/2 and HTTP/3, HSTS with `preload`,
`x-content-type-options: nosniff`, `cache-control: public, max-age=0, must-revalidate`, `etag`,
`last-modified`, `vary: Accept-Encoding`, **gzip but no brotli**, and **no
`content-security-policy`**. It discriminates correctly (a path that cannot exist returns `404`
with a 13-byte body), which is what makes its codes worth reading. Local `gzip -9` figures are
the reproducible ones and the host compresses more loosely, so the wire runs about 3% larger.

**Known-good state on 2026-10-15.** All four checks pass with 19 warnings and 0 errors, the
build renders all ten pages, and `data/sources.yaml` is:

```
md5  fda82cb39476a96c1ea458fc69b3859a
58 sources: 48 with an `archive:` value, 10 without, 19 `verified_on: null`
```

**Page weights, measured after the drop:** median 9,126 bytes gzipped and 25,216 raw; heaviest
`/sources/` at 26,440 gzipped and 89,184 raw, 2.90 times the median; the whole site with its
shared stylesheet and icon counted once at 91,789 bytes gzipped. **Both readings of the 100 KB
budget pass for the first time**, because `/sources/` lost 1,453 words of generated
bibliography with the 12 deleted records; the raw row used to be over the line at 103,681.
These move with any content edit, since `/sources/` is both the heaviest page and the
bibliography. **The old rule that excluded `/receipts/` from the median is retired**: it existed
to protect a published statistic, and nothing publishes one now. Do not reintroduce an
exclusion to match an old sentence.

### Gotchas that have already cost time: don't repeat them

1. **YAML: never start a list item with a quoted scalar followed by a comma.**
   `- "Sale" is defined broadly` parses the quote as a complete scalar and chokes on the comma.
   This broke `data/sources.yaml` twice. `check-content.py` fails fast on it rather than
   emitting 80 cascading citation errors.
2. **A non-OK status code is usually meaningless: control-probe before trusting one.** Reuters
   answers 401, DLA Piper 429, and `dl.acm.org`, `nytimes.com`, `lexology.com`, `loc.gov` and
   `ftc.gov` answer 403 or 404 for any path at all, including paths that cannot exist and their
   own roots. `check-links.py` requests a deliberately bogus path and downgrades those to
   `N/A`. **Automated verification is impossible for those domains**, and a `BLCK` verdict is
   not reassurance either, since rate limiting changes results between runs. Every non-OK
   result needs a human, and the archive link is how a blocked page gets read from a terminal.
   These sources carry `verified_on: null` with a comment. **Never set `verified_on` on a
   source whose domain blanket-blocks probes**: that mistake was made on ten sources and had
   to be reversed.
3. **Hugo extended's Sass is libsass 3.6.6: deprecated and frozen.** It cannot parse native
   nesting, `@container` or modern colour functions. **Write plain CSS.**
4. **`hugo mod` needs Go, which is absent**: pin the version in `.tool-versions` instead.
5. **Do not use a Hugo theme.** Nearly all pull Google Fonts, Font Awesome, jQuery or a CDN,
   which breaks the zero-third-party rule outright.
6. **Editing a file after running or `chmod`-ing it invalidates the read cache**, and the edit
   will be refused until the file is re-read. Expect this with the scripts.
7. **Citation syntax is `{{< cite "source-id" >}}` with the angle brackets.** Writing
   `{cite source-id}` fails silently: it renders as literal text, the checker's regex misses
   it, and the page declares sources it never cites while citing sources it never declared. If
   a page produces a sudden cluster of "unknown source id" errors, check the shortcode syntax
   before hunting for typos.
8. **Two citation conventions, used deliberately.** `{{< cite >}}` is for *claims* and must be
   declared in frontmatter. A plain markdown link is for *pointers* ("here is the project's
   website") and needs no entry. Keeping them separate stops the sources file becoming a link
   dump while keeping every claim attributable.
9. **A bulk punctuation sweep is verifiable, so verify it.** When the em dashes were removed,
   every file was copied to a scratch directory first and diffed afterwards on the *word
   sequence only*, ignoring punctuation and case. That catches the failure the edit actually
   has: a word changing along with the comma. Two files were edited badly by a subagent and
   both were caught. Never rewrite a file wholesale when a targeted edit will do.
10. **A passing status code is not a verified source, and neither is a failing one.** Open the
    thing, or say you did not. What to know before probing a domain:

    - **CNIL is unblocked again as of 2026-10-15.** From round 8 to round 11 every URL on
      `www.cnil.fr` returned 503 with a 15 KB maintenance page, including its own root and
      impossible paths, and four sources had `verified_on` set on the strength of that code
      before being corrected to `null`. Today it returns 301 for its root, 404 (71176 bytes)
      for a path that cannot exist and 200 (636667 bytes, `application/pdf`) for the
      SAN-2025-004 PDF; `linc.cnil.fr` returns 200 for its quiz page and 404 for an impossible
      path. **Read the pages and date them, from the content rather than the code.**
    - **Use response size as a second control probe.** That is how the CNIL block was caught:
      two hosts, two uniform signatures (15184 and 19336 bytes) across good and bad URLs alike.
      Today's 404 template at 71176 against 71173 bytes for two different impossible paths is
      the same test in its healthy form.
    - **EUR-Lex is empty, not merely awkward.** Every URL returns 202 with 0 bytes, and fifteen
      URL shapes were tried across five instruments and four judgments. `data.europa.eu/eli/`
      behaves the same. **The route in is an archived copy from before the breakage**, found
      with the CDX API rather than the availability API:
      `curl -sS "http://web.archive.org/cdx/search/cdx?url=<url>&output=json&filter=statuscode:200&limit=5"`.
      Two traps sit on it: recent snapshots are often replays of the empty shell or a robot
      wall, so read the body before believing it, and the availability API returns empty for
      URLs that do have working snapshots.
    - **`curia.europa.eu/jcms/upload/docs/...` serves real PDFs and control-probes correctly**,
      which is how the C-604/22 press release was verified. Use it for CJEU material.
    - **`hudoc.echr.coe.int` (ECtHR) cannot be read or verified from a terminal**: 403 for a
      real document, a bogus id and its own root, with three body sizes. A promising source on
      retaining the fingerprints of people never convicted was **dropped rather than cited
      sight-unseen**, which is the rule working.
    - **One host can control-probe cleanly on one path shape and prove nothing on another.**
      `edpb.europa.eu`'s file server returns 404 for a bogus path and 200 for a real PDF, but a
      bogus path under `/documents/` returns **200 with a generic listing** (94043 bytes
      against the real page's 44610). **Compare size and read the body before believing a 200
      on a CMS-style path**, and settle it by checking that the page's own title is the title of
      the thing being cited.
    - **Discipline varies by host, so test the host you are citing.** `uitspraken.rechtspraak.nl`
      answers identically for a real judgment and an impossible path, while
      `data.rechtspraak.nl/uitspraken/content?id=<ECLI>` returns the judgment as XML for a real
      ECLI and 404 for a bogus one, so the second is the citation target. `uscode.house.gov`
      returns byte-identical 5792-byte shells for a real section and a nonexistent one, while
      `govinfo.gov` has a distinguishable not-found. `sustainablewebdesign.org` and
      `conseil-etat.fr` probe cleanly. `leginfo.legislature.ca.gov` sits behind a Cloudflare
      challenge and answers 403 to everything.
11. **Hugo generates em dashes that no script on this site can see.** Goldmark's typographer
    is on by default and rewrites punctuation in the *output*: `---` becomes `&mdash;` and `--`
    becomes `&ndash;`. `check-dashes.py` reads source files only, so a page can pass the house
    rule and still render em dashes. **It is disabled in `hugo.toml` for that reason, and must
    stay disabled**, which costs automatic curly quotes and is still the right trade: house
    punctuation the house check cannot see is not checkable.
12. **`hugo server` does not always pick up a NEWLY ADDED template file.** After adding a
    shortcode, the running server logged `Template added` and then failed every rebuild with
    `template for shortcode "x" not found`, serving HTTP 500 until restarted. **Restart the
    server after adding a template file.** Two related traps: **never delete `public/` while
    `hugo server` is running** (it has its own in-memory build), and **`hugo server` serves its
    own memory rather than the last `hugo` build**, so check which one you are looking at
    before debugging templates. When the two disagree, trust the CLI.
13. **A fingerprinted asset leaves a stale twin behind, and it will lie to you about page
    weight.** Editing `assets/css/main.css` gives the stylesheet a new filename, and the old
    fingerprint stays in `public/` forever, unreferenced but present:
    `--cleanDestinationDir` does not remove it, because Hugo Pipes output is not a static file.
    Summing `public/` inflated every page by about 1.5 KB of a stylesheet no browser would
    fetch, and wrong numbers were published twice before it was caught. Two rules came out of
    it, both enforced: **`scripts/build.sh` deletes `public/` before building**, so the output
    is a pure function of the input, and **measure what the page fetches**, by parsing its own
    `<link>` tags, which is what `measure-pages.py` does. The general lesson is the project's
    own: a number from a convenient method is not a measurement until the method has been
    checked against the definition it claims to serve. **A stylesheet edit is exactly what
    creates the stale twin**, so this is the gotcha the styling pass has to keep in mind.
14. **Every file under `/etc/ssh` on this machine is owned by `nobody:nobody`, so plain `ssh`
    and `git push` fail before they reach the network.** The error is `Bad owner or permissions
    on /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`, which reads like a broken key or a
    network fault and is neither. **The workaround is repo-local and already applied**:
    `.git/config` carries
    `core.sshCommand = ssh -F /dev/null -i ~/.ssh/github_key -o IdentitiesOnly=yes`. It is
    untracked and machine-specific. **The real fix needs root and is the maintainer's**:
    `sudo chown -R root:root /etc/ssh`. Until then, **do not diagnose a connection failure here
    as a key, credential or network fault** before checking that ownership.
15. **An error you can observe is not a cause you can name.** Before the first deploy the site
    failed TLS with `tlsv1 alert internal error`, and a hostname that cannot exist failed the
    same way. The observation was sound; the explanation published with it was wrong, because
    the certificate had been issued an hour before the probe, so what was missing was the name
    answering rather than a certificate existing. The same afternoon, a deploy landing minutes
    after a push was written up as "pushing appears to deploy", and the next two pushes did not
    deploy at all. **Record what a probe showed and leave the cause unknown, or name a cause
    only from evidence that can still be checked afterwards.** Two related traps: the domain's
    DNS is a wildcard, so resolution proves nothing and the host's TLS layer is what
    discriminates, and `last-modified` is per file rather than per deploy.

---

## 8. Standing build constraints: the site must pass its own test

These are load-bearing. The project's claim is credibility, and it dies the moment the site
itself is hypocritical.

- **Zero third-party requests.** No Google Fonts (system stack or self-hosted woff2), no CDN
  scripts, no embeds (click-to-load placeholders instead), inline SVG, no third-party comments.
- **Analytics:** GoatCounter or equivalent, and **no cookies, so no consent banner at all**,
  which is the site's best demonstration. Say so on the home page.
- **Progressive enhancement is mandatory.** Every interactive's full content must be readable
  with JS disabled; JS adds motion and filtering only. This satisfies the architecture and the
  WCAG requirement at once (`SITE_PLAN.md` §6b has the single-source-of-truth pattern).
- **Accessibility: WCAG 2.2 AA.** Semantic HTML, keyboard-operable interactives, visible focus,
  4.5:1 contrast, meaningful alt text, and `prefers-reduced-motion` respected, which is
  critical because the flagship page is scroll-animated.
- **Performance budget:** under 100 KB per page, under 20 requests, LCP under 1.5 s. Both
  readings of the weight line pass as of 2026-10-15 (§7).
- **Every figure the site publishes must be measured, not asserted, with its method named.**
  Nothing publishes the site's own figures any more (`/receipts/` was dropped), so this is now
  about any future page: re-adding a page of them is a decision the maintainer has already
  taken once, and it should not be undone quietly.
- **Response headers are part of passing the test, and one is missing.** The host sends HSTS,
  `nosniff` and a revalidating cache policy, and no `content-security-policy`. A site claiming
  "no third-party requests" should have the browser check that claim rather than a reader
  taking it on trust, so the missing header is tracked here rather than waved away as somebody
  else's server. `robots.txt` also does not point at the sitemap.
- **Honesty about maintenance belongs on the page, not only in this file.** The footer states
  on every page that the site was written in October 2026, that it is not maintained on a
  schedule, that there is no capacity to keep every page current, and that the claims dating
  fastest are about law, enforcement and prices. A `status_as_of` date alone implies someone is
  watching it, so this was asked for deliberately. **Do not quietly remove it**, and any future
  page whose whole value is being current inherits the requirement.

---

## 9. Suggested next steps

Items 1 to 6 are closed and are kept as stubs so the numbering does not shift.

1. ~~Write `/consent-theatre/`.~~ **Done**, including its interactive: "Eight clicks through one
   banner", eight documented defects as a static walkthrough, no JavaScript (§5).
2. ~~Finish the `/nothing-to-hide/` interactive.~~ **Done.** `secondary use` and `dignity` are
   argued in "Two harms that needed arguing", and both list entries point at an argument that
   exists. See §5 for the one caveat: the dignity passage is normative and leans on two sources
   still marked unverified.
3. **Clear the remaining archiving gaps**: 9 sources with no snapshot at all, out of 58, of
   which 48 are archived. Tedious, unglamorous, and the difference between a claim and a
   checked claim. **Do not start over**: §6 item 1 lists the 9 and explains the API's
   spurious-empty trap, Save Page Now works over plain HTTP, and the CDX API answers the
   "does a snapshot exist" question properly. **Cheapest item on this list, new on
   2026-10-15: the four CNIL sources can be opened again** (§7 gotcha 10), which would move the
   warning count for the right reason.
4. ~~Fill the two `/sources/` TODOs.~~ **Both published**, and **one sub-item is still open**:
   whether GitHub accepts anonymous issue filing on the public repository, which decides
   whether the published correction route can receive anything. Check it logged out in a
   private window before treating the route as live.
5. ~~Fix the `edpb-consent-or-pay` entry.~~ **Done**, and it took more than two lines (§6
   item 5). `solove-taxonomy` is what remains.
6. ~~Write `/` and `/receipts/`, drop `/the-rules/`, wire up hosting.~~ **All closed.** What
   followed was the work that is not writing: the source worklist in §6, the cheap source
   upgrades there, and hosting.
7. **~~Set up the repo and statichost.eu.~~ Done: the site is live.** `origin` is
   `git@github.com:osszevissza/the-third-party.git`, `main` tracks it, and the maintainer's
   domain is `baseURL`. §7 has the serving facts. **What the deploy left open**, none of it
   blocking and all of it cheap:

   - **There is no `statichost.yml` in the repository**, so the host's build configuration
     lives in its dashboard, is not version-controlled and cannot be reviewed from the source
     tree. Committing one would make the build reproducible from the repository alone.
   - **Whether the host runs the four checks is unknown, and assume it does not.** The deployed
     stylesheet fingerprint matches a local build exactly, so the host ran the same Hugo, but
     that image carries Hugo rather than Python and PyYAML. **Assume the checks ran locally and
     nowhere else**: a push that fails one and is not caught locally would deploy anyway.
   - **No `content-security-policy`, and `robots.txt` does not point at the sitemap.** Both are
     one-line fixes on a host that already sends HSTS and `nosniff` (§8).
   - **Do not read a resolving hostname as proof of a deploy.** Every `*.statichost.page` name
     resolves, including names that cannot exist, and all refuse TLS until a site is
     provisioned, so the DNS record is a wildcard. Verify by fetching a page and reading its
     own title, which is how the 2026-10-14 deploy was checked: twelve pages, twelve correct
     titles and canonicals.
8. **The styling pass. This is the next job, and the maintainer sets the direction.** They said
   they would describe what they want rather than approving a proposal, so **do not start
   designing unilaterally**: ask for the direction, or implement the one you are given.

   **What exists, so nothing is rebuilt from scratch.** `assets/css/main.css` is a token layer
   in `:root` (`--bg`, `--surface`, `--ink`, `--ink-muted`, `--rule`, `--accent`,
   `--accent-ink`, `--measure`, two font stacks), a full dark scheme under
   `prefers-color-scheme`, visible focus everywhere, the skip link, the header and its
   generated nav, `main`/`.page`/`.page-header`, a heading scale, paragraphs, `hr` dividers,
   lists, blockquote, inline `code`, images, tables, the citation marker, the source list and
   its records, the footer, and a print stylesheet. It goes through Hugo Pipes (minify,
   fingerprint), so CSS edits need no build changes and no new tooling.

   **Two concrete defects it should close**, both of which used to be published on the dropped
   `/receipts/` page and are recorded here instead:

   - **`section.interactive` has no styling at all.** The shortcode emits
     `<section class="interactive" data-interactive>` and no rule matches it, so the eight-click
     walkthrough on `/consent-theatre/` and the harms block on `/nothing-to-hide/` render as
     bare stacked text. This is the largest visual hole on the site, and where a new visual idea
     would show first.
   - **Citation markers.** `.cite` is `font-size: 0.75em; line-height: 0`, which is the WCAG
     2.5.8 target-size failure: the clickable area is a few pixels high, and with CSS off they
     are bare numbers with no affordance. Both are style problems rather than markup ones.

   **Before touching colour, build the contrast check.** The site used to publish that contrast
   is computed from the values in that file rather than trusted, with a lowest ratio of 6.66:1
   and every pair passing 4.5:1 in both schemes. Nothing publishes it now, and it is worth
   keeping true anyway, because it was maintained by hand and a colour edit can break AA with
   nothing to say so. **Write `scripts/check-contrast.py` first**: parse the `:root` tokens and
   the dark block, compute WCAG 2.1 relative luminance for each pair the site renders (`--ink`
   and `--ink-muted` on `--bg` and on `--surface`, `--accent` on `--bg`, `--accent-ink` on
   `--accent`, and the focus ring against both backgrounds), fail below 4.5:1 for text and 3:1
   for the ring, and wire it into `scripts/build.sh` as a fifth check. Then update the places
   that state how many checks run: `/sources/` says "four scripts" in prose, and §2 and §8 of
   this file.

   **The constraints are not negotiable and are all in §8**: plain CSS (Hugo's bundled Sass is
   frozen libsass, §7 gotcha 3), no framework, no webfont, no CDN, zero third-party requests,
   WCAG 2.2 AA, `prefers-reduced-motion` honoured (which matters because
   `scroll-behavior: smooth` is already set for the flagship page), and the under-100 KB page
   budget. A page that loads a webfont to look better than the other pages has lost the
   argument the site is making.

   **The loop, and its one limitation.** There is no browser and no headless tooling here (§7),
   so **the agent cannot see the result**. Write CSS, hand it to the maintainer to look at, and
   iterate on what they describe. `sh scripts/build.sh serve` gives them
   `http://localhost:1313` with live reload, but remember gotcha 12: restart the server after
   adding any template file, and never delete `public/` while it runs. Everything measurable is
   still checkable here: contrast, page weight, the static accessibility list, and zero
   third-party requests.

   **When it is done, re-measure**, because the stylesheet is in every page's weight: run
   `python3 scripts/measure-pages.py` (§2) and check that both readings of the budget still
   pass. Then commit, push, and the maintainer deploys (§7).

---

## 10. What "done" means for the current goal

Ten core pages of portfolio-quality, fully sourced Markdown, with every factual claim grounded
in a verified, dated citation. **All ten exist**, all four scripts pass with 0 errors, and the
build renders every page.

**Two conditions of the original definition of done are still open, and neither is writing
work.** The source worklist in §6 is not clear: 19 sources carry `verified_on: null`, several
because no terminal can verify them at all, and 10 have no archive. Both are honest limitations
rather than oversights, both are tracked in §6, and the count of 19 fell on 2026-10-15 for a
reason that was not progress. The third condition that used to sit here, the unsupported
disclosure sentence on `/sources/`, closed in round 11 (§9 item 4).

**The written work is done, and the last piece of unwritten work is the styling** (§9 item 8).
The maintainer is choosing its direction, so ask rather than design. Everything else left is
maintenance of the kind §6 tracks.

**Open questions carried forward, both small and both the maintainer's call:**

- **The carbon figures divide by 2^30 rather than by a decimal billion**, which is correct as
  GiB and wrong as GB, a difference of about 7%. `measure-pages.py` prints both, and **nothing
  on the site depends on it any more**, because the page that published the milligram figure
  was dropped on 2026-10-15. The model itself says "gigabytes per kilowatt-hour" without
  settling which, which is why it stays a question rather than a bug to fix quietly.
- **Four commits in the middle of the history carry paragraph-length messages**, from before
  the short-commit rule was set on 2026-10-14. Rewriting them means a force-push to a public
  repository, so they were left alone and offered instead. The offer stands.

**The repository is public, and so is the site.** The source is on GitHub, which is what gives
the correction route printed on `/sources/` something behind it, and the site is live at
`https://third-party.statichost.page/`, verified by reading each page's own title. The
2026-10-15 drop is pushed but not deployed, so the live site is one version behind until the
maintainer triggers it (§7).

**Not blocked, and no longer blocked on content.** What remains needs a human rather than an
agent: the links that have to be opened by hand, the 9 possible Wayback gaps, and the GitHub
tracker setting that decides whether anonymous issue filing works (§9 item 4). The four CNIL
links left that list on 2026-10-15, when the domain started answering again.
