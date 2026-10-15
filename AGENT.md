# AGENT.md: working notes for the next session

Read this first. It assumes no memory of previous sessions.

**Session date when written:** 2026-10-14. Run `date -u`. The repo has no timestamp
authority and several pages carry `status_as_of` fields that need refreshing if a lot
of time has passed.

**▶ ACTIVE: the site is live, and the styling pass is next.** Everything below in this header
block was true at the end of round 11, and a second session on the same day (2026-10-14)
changed rather more than a session usually does. **Read this list before the round-11 history
further down, because several of those statements have been superseded.**

What that session did, in the order it happened:

1. **The domain was decided and set**: `baseURL` is now
   `https://third-party.statichost.page/`, replacing the `example.invalid` placeholder that had
   been deliberate. §9 item 7.
2. **The GitHub remote was connected and the history pushed**, after auditing what was about to
   become public. §7.
3. **The site is live**, deployed by hand from statichost's dashboard, and verified by reading
   each page's own title rather than by trusting a status code. §7 has the serving facts, and
   `/receipts/` published them under "What the host sends" until that page was dropped on
   2026-10-15. **A push does not deploy** (§7).
4. **`/receipts/` was cut from 3,129 words to 1,338** at the maintainer's request, and its
   median row now covers the other eleven pages rather than all twelve, because a page cannot
   report a statistic it is part of. §5 and §7.
5. **The search swap now recommends Ecosia first**, using `ecosia-eusp-index`, a source that had
   been recorded and verified but cited by no page. §5.
6. **Two wrong causes were written down and corrected** (§7 gotcha 15), which is why that gotcha
   exists at all: it caught itself twice in one afternoon.

**A third session, on 2026-10-15, dropped two pages at the maintainer's request.** The friend
who originated the project was part of that conversation, so treat the decision as settled
rather than as an experiment to be revisited. What changed, and what it costs:

1. **`/swap-shop/` and `/receipts/` are gone**, directories and all. The site is now **ten
   pages: the home page plus nine content pages.** §5 records what each page carried, what
   replaced it and why nothing did. `SITE_PLAN.md` keeps both outlines with the reasoning, the
   way it keeps the dropped `/the-rules/` outline, so a later session does not re-add them out
   of tidiness.
2. **Nothing on the site publishes its own measured numbers any more.** `/receipts/` was the
   only page that did. The three defects it published (no `content-security-policy`, citation
   markers below the WCAG 2.5.8 target size, unmarked foreign-language text) are now tracked in
   §6 and §9 instead of on a page, and `scripts/measure-pages.py` stays as an internal check of
   the 100 KB budget rather than as the source of a page.
3. **12 source records cited only by those two pages were deleted** from `data/sources.yaml`,
   which is now 58 entries, 48 archived. The new md5 and the counts are in §7. The disclosure on
   `/sources/` was kept and rewritten as "what I actually run", so the three sources it cites
   (Ecosia, and Mullvad's DNS notice) are still cited.
4. **Five published pages were edited so that nothing on the site claims what is no longer
   true**: the home page lost its "receipts" section, `/start-here/` and `/analytics/` lost
   their self-references to it, `/one-page-load/` and `/nothing-to-hide/` lost their swap-shop
   links, and `/sources/` lost a `gzip` clause and a `Receipts` pointer along with the two
   stale counts in its "gaps" section. One unrelated false sentence on the home page was fixed
   at the same time: it still said the harms page had two harms it had not finished arguing,
   which stopped being true in round 11.
5. **The deploy is the maintainer's, as always** (§7), so until one is triggered the live site
   is still the twelve-page version and still serves both dropped pages. That is expected
   rather than a fault, and the check afterwards is the same as ever: fetch a page and read a
   phrase that exists only in the new commit.

**All ten pages exist, all four checks pass, and the site is published.** What is left is
not writing:

1. **The styling pass, and it is next.** The maintainer is setting the direction themselves;
   §9 item 8 has the constraints, the two concrete defects it should close, and the one thing
   this environment cannot do. Nothing about it is blocked.
2. **The small things the deploy exposed**, none of them blocking and all of them cheap:
   no `statichost.yml` in the repository, so the host's build command is configured in its
   dashboard and is not version-controlled; no `content-security-policy` header on a site
   whose central claim one would enforce; and a `robots.txt` that does not point at the
   sitemap. §9 item 7 has the detail.
3. **The source worklist in §6**: 19 sources without a `verified_on` date, 10 without an
   archive, and the cheap upgrades to existing entries that round 11's verification found.

---

## 0. Orientation in thirty seconds

### The brief: read this before anything else

The maintainer's stated priority, in their own words: **the content quality must be high
enough to include in a portfolio.** This is not a course exercise to be got through; it
is a piece of work someone intends to show people. It is the primary requirement, and it
outranks speed, page count, and completeness.

Three consequences that shape everything below:

1. **Never pad.** A page that exists to fill an outline slot is worse than a missing page.
   An honest "I could not verify X" is worth more than a confident sentence without a source.
2. **Never overstate.** The project's whole argument is that claims should be checkable.
   One unsourced number, one invented statistic, or one `verified_on` field that wasn't
   actually verified costs more credibility than the page adds. This has already gone
   wrong once (§7, gotcha 2) and was corrected at the cost of a whole round.
3. **Keep pages readable.** The maintainer asked for this explicitly in round 8. Prefer a
   shorter page that gets read to a complete one that doesn't. **Confirmed again in round
   10: the ~2,400-word figure is a soft signal, not a rule.** The maintainer's own words:
   the limit is flexible, what matters is not exceeding it excessively, because the real
   risk is that readers get tired partway through. Long-form is welcome; fatigue is the
   thing to avoid.
   
   So the correct reading is: 2,400 is where you should *ask whether the page has earned
   its length*, not a wall. A page at 2,800 that reads well is fine. A page at 2,000 with
   padding in it is not. `/consent-theatre/` grew by roughly 600 words in round 10 when its
   interactive was written, and that was accepted rather than trimmed. (The word figures
   quoted in this file before round 11 were measured inconsistently and did not agree with
   each other; §5 now carries one reproducible measurement, and use that one.)
   
   **Do not cut good content to hit a number.** The nine-objection ceiling was shown to
   the maintainer and approved, so do not trim `/nothing-to-hide/` for its own sake. The
   one page genuinely exempt from length pressure is `/sources/`, which is a bibliography
   rather than an argument: it is 8,870 words, most
   of it generated, and §5 explains why that is the right shape for it.

A related piece of context: the project was **someone else's idea**, a friend of the
maintainer, and that friend has a say in the voice. That decision has now landed (§1).

### What the project is

A static Hugo site arguing that the web is more extractive than it looks, built to
**pass its own test**: no third-party requests, no cookies, no consent banner, WCAG AA.
Until 2026-10-15 that list ended with "and a page publishing its own measured numbers".
`/receipts/` was that page and it was dropped, so the self-measurement half of the test is
internal now rather than published (§5, §9 item 8).

**Working title:** *The Third Party*.

**Live at [third-party.statichost.page](https://third-party.statichost.page/)** since
2026-10-14, served by statichost.eu from the public GitHub repository. The deploy is real and
verified: the twelve pages that existed then each answered `200` with their own correct title
and canonical. The site is ten pages as of 2026-10-15 and no deploy has been triggered since,
so the live site is still the twelve-page version until the maintainer runs one. See §7 for
what the host sends and §9 item 7 for what the deploy left open.

**Author and licence:** Underdog Guild ([barsimarina.hu](https://barsimarina.hu)), and the
site's own text is released under **CC0 1.0**, apart from quotations, which stay with the
sources they came from. Both facts were supplied by the maintainer in round 11 rather than
inferred, and both are stated in the footer. Do not invent a different author string or a
different licence for this project.

**State:** ten pages, which is every page the site intends to have: the home page plus 9
content pages. 26,895 words of body text by the count in §5, of which 8,870 is `/sources/`
and mostly its generated bibliography. 2 archived drafts, 58 sources, four scripts, a
LICENSE, and a Hugo build that passes all four checks and renders all ten pages with no
errors. `/the-rules/` was dropped in round 11, and `/swap-shop/` and `/receipts/` were
dropped on 2026-10-15, so the target has moved from 13 core pages to 10. **It is live, and
that is new**: the writing being finished and the site being published are two different
states, and only the first was true before 2026-10-14.

**Read next, in this order:** `FOR-REVIEW.md` (concept, and the review outcome),
`SITE_PLAN.md` (full IA and rationale), `data/sources.yaml` header (citation rules).

---

## 1. The voice decision: CLOSED on 2026-10-14

The friend reviewed both drafts of `/nothing-to-hide/` and agreed with the
both-by-purpose recommendation. The rule, which is now the house style:

> **B's shape for objection pages**, the ones a reader arrives at with a *doubt*.
> Standalone units, each headed by the objection in the reader's own words.
>
> **A's shape for explanatory pages**, the ones a reader arrives at with a *question*.
> An essay that builds, with the strongest argument held back.

| Page | Register |
|---|---|
| `nothing-to-hide/` | **B**, objections, merged with A's opening and A's concession section |
| `myths/` | **B**, standalone units, each checkable in a browser |
| `consent-theatre/` | **A**, explanatory. Written in round 10 |
| `what-leaves-your-browser/`, `one-page-load/`, `analytics/` | **A**, as written |
| `start-here/`, `dark-patterns/` | reference: lists of records. `the-rules/` sat in this row until it was dropped in round 11, and `swap-shop/` until it was dropped on 2026-10-15, see §5 |
| `sources/` | reference: generated, never argued. `receipts/` sat beside it until it was dropped on 2026-10-15 |

`drafts/README.md` records the decision in full, with the per-page reasoning. Do not
re-open the fork. If a new objection page is ever added, it takes B's shape.

### What the merged page contains

`content/nothing-to-hide/index.md` is the B shape, not a third draft:

- **Opens on the AOL set piece** in four short paragraphs, which is the most persuasive
  passage either draft had.
- **Nine objections**, up from B's eight. The ninth, "It's my data. If I don't mind,
  that's the end of it", came from the friend in round 8 and is the best addition anyone
  has made to the page: it is the one argument that survives the objection it answers,
  because "I don't mind" says nothing about the person whose phone number you just
  handed over.
- **A short "where this page is wrong" section**, kept because AGENT.md's structural
  rules require a dedicated concession and it is the fairest thing on the page.
- Cites 15 sources, all declared, all cited inline. Three of them are new in round 8 and
  are listed in §4.

The old Draft A text is no longer in the repository. This file used to say it was inside
`Archívum.tar.gz` at the root, along with the pre-decision copies of `SITE_PLAN.md`,
`index.md` and `nothing-to-hide--B-objections.md`. **The maintainer removed that tarball in
round 11 and confirmed it was only ever temporary**, so those copies are deliberately gone
rather than misplaced. Do not go looking for them, and do not try to reconstruct Draft A
from memory: the adopted shape is the merged page, and `drafts/README.md` holds the
reasoning behind it. Two stale duplicates that used to sit in the repo root (`index.md`,
`nothing-to-hide--B-objections.md`) were removed in round 8 for the same reason: a copy
that looks canonical is a trap for the next session.

---

## 2. Commands

```bash
python3 scripts/check-content.py   # frontmatter, YAML, citation graph. exit 1 on error
python3 scripts/check-links.py     # resolves every source URL. exit 1 only if truly dead
python3 scripts/check-dashes.py    # house punctuation rule. exit 1 on any em dash
python3 scripts/render-bibliography.py --check   # exit 1 if /sources/ is out of date
```

There is a fifth script that is deliberately not a check and does not run in the build:
`python3 scripts/measure-pages.py` measures what each built page actually weighs, by the
referenced-asset method in §7 gotcha 13, and prints every page, the median, the heaviest page,
the ratio, the site-wide total, both readings of the 100 KB budget and the carbon estimates.
**Run it after any edit to a page or the stylesheet, and always after the styling pass.** Until
2026-10-15 it existed to keep the figures published on `/receipts/` honest and reproducible;
that page is gone, so it is an internal check now and nothing on the site publishes its numbers.
It still prints the carbon figures in both decimal GB and GiB, because which one to quote was
the maintainer's open question and nothing on the site depends on it any more (§10).

Run all four before ending any session, and run `scripts/render-bibliography.py` without
`--check` whenever `data/sources.yaml` or any page's `sources` list changes, because that
is what rewrites the generated block on `/sources/`. Expected output as of 2026-10-15:

- `check-dashes.py` → `no em dashes in 21 file(s), 0 allowlisted`. **The allowlist is empty
  as of round 11**, and that is a real state rather than an oversight: the single entry it
  held claimed a CNIL document title was "quoted as published", and the archived copy of
  CNIL's own page showed that title contained no em dash at all. The dashes were ours, not
  theirs. Add an entry rather than editing a quotation, but only for a dash genuinely
  inside text a source published, and name the snapshot you checked it against. Generated
  blocks are skipped by that check, since they are machine-written from a data file the
  check already covers. **The allowlist key is a line number**, so it goes stale the moment
  data/sources.yaml is edited above the line it points at: that is what broke the check in
  round 11, and the fix is to re-verify the text, not to bump the number.

- `check-content.py` → `19 warning(s), 0 error(s)` as of 2026-10-15, down from 20. Warnings
  are the source worklist: blanket-blocked or unverified URLs awaiting a human, plus 1 with
  no URL at all (§6). **This fall is not progress**: the count dropped because `codeberg`,
  which was one of the 20, left the file along with the two dropped pages (§5). Nothing was
  verified. The count fell by one in round 11 for a different reason, and that one did count:
  `edpb-consent-or-pay` gained a URL and a date (§6 item 5), verified by content rather than
  by status code, because its host answers 200 for paths that cannot exist (§7, gotcha 10).
  In every earlier round this count rising was the honest direction: a warning means a human
  still has to open the link.
- `check-links.py` → `45 resolving, 6 bot-blocked, 0 dead, 0 inconclusive, 6
  unverifiable` on the 2026-10-15 run, and it lists 4 further URLs whose 404 was treated
  as bot-blocking because the domain root refused the probe too. **`unverifiable` is not a
  pass.** It
  means the status code proved nothing and a human must open the link (§7, gotcha 2).
  **These counts drift between runs, and round 11 measured how much**: three runs in one
  session, over a source file that was changing only by additions, gave `47/7/0/4/6`,
  `48/8/0/3/5` and `53/7/0/3/6`. Treat any single run as a snapshot rather than a result, and
  never quote one as a measurement of the site's health. **Some verdicts in this output are
  actively misleading and are known bugs, not results**: `cjeu-planet49` reports `OK 202` while
  EUR-Lex returns nothing but a JavaScript shell (§7, gotcha 10), and `edpb-consent-or-pay`
  reports `OK 200`, which is true but proves nothing on its own, because that host returns 200
  for paths that cannot exist: the evidence was the page's own title, read by hand.
  **The four CNIL rows are no longer among the misleading ones**, which is a change of state
  rather than a change of tool: on 2026-10-15 they report `OK 200`, the maintenance block is
  over and the domain control-probes cleanly again. See §7 gotcha 10 for the measurement, and
  §6 item 2 for what that reopens.

**Every page must show a perfect citation match**: every declared source cited inline,
every inline citation declared. There is a one-liner in §7, gotcha 7, explaining the
failure mode that breaks this.

**Neither script edits anything, deliberately.** Whether a source still supports the
claim attached to it is an editorial judgement, not a status code.

---

## 3. Content architecture

### The spine: every page runs these four beats

> **Problem → Pattern → Alternative → Receipt**

- **Problem**: what actually happens, with a number or a named script.
- **Pattern**: the design or business model behind it, and who profits.
- **Alternative**: what a less extractive version looks like, and what it costs.
- **Receipt**: where the claim came from, dated, plus this site's own number.

Repeating the beats is what makes the site read as designed rather than as a pile of
articles, and it allows pages to be cut under deadline without the structure failing.

### The page template

1. **Hook**: one concrete, surprising, verifiable fact. No preamble.
2. **What's happening**: the mechanics, plainly, naming specifics.
3. **Why it matters / who benefits**: follow the money.
4. **The other side, stated fairly**: steelman before critiquing. *Never skip this.*
5. **What you can do**: one primary action, then escalation options.
6. **Sources**: `{{< source-list >}}` at the end.

Frontmatter (TOML, `+++` delimited) requires `title`, `description`, `status_as_of`,
`weight`, `sources`.

### Voice rules: these are the product, not decoration

- Second person, present tense, short sentences.
- **Concrete beats abstract every time.** Not "trackers collect data" but "this page
  sent 47 requests before you scrolled; 31 went to nine companies you've never heard of."
- **Punch up at systems, never down at users.** The reader is not stupid; the design is
  hostile. This is the entire difference between advocacy and smugness.
- **No doom without an action.** Every page ends with something to do, however small.
- **Steelman before dismantling.** Explain why small businesses use Google Analytics
  before explaining why they might not.
- **Organise around problems, never tools.** A "Top 10 private tools" list is the
  weakest possible version of this project: it teaches nothing and dates instantly.
- **No vendor worship.** Disclose your own choices.
- **No em dashes.** The maintainer asked for this in round 8, in these words: people
  rarely use them, so use one only when it is necessary. Write a comma, a colon, a full
  stop, a semicolon, or a pair of parentheses instead. Every page was swept clean in round
  8 and the repository's last one went in round 11, so the site contains none at all and
  `check-dashes.py`'s allowlist is empty. **That empty allowlist is a real state rather
  than an oversight**: the single entry it held claimed a CNIL document title was quoted
  as published, and the archived copy of CNIL's own page showed the title contained no em
  dash, so the dash had been ours. See §2 for what a failed check means, and add an entry
  rather than editing a quotation if one is ever genuinely a source's own punctuation.
  This is a hard rule for new prose, not a preference. The
  exception worth keeping: **text inside quotation marks that quotes a source, a law, or
  a company stays exactly as it is**, em dash and all, because a quotation you have
  tidied is no longer a quotation. If a sentence genuinely collapses without a dash,
  restructure the sentence; that is nearly always cheaper than the dash was.

### Structural rules that keep pages from collapsing

- Never end with a cluster of citations bolted onto a sentence that doesn't need them.
  This mistake was made once and removed; don't reintroduce it. One claim, one citation,
  attached where the claim is made.
- One idea per section, and let a section be short.
- Concede real ground in a dedicated section. `/nothing-to-hide/` and
  `/what-leaves-your-browser/` both do this and it is what earns the right to argue.
- Aim a page at roughly 2,400 words, and read §0 item 3 before treating that as a wall.
  The maintainer's clarification in round 10 is that the number is a prompt to ask whether
  a page has earned its length, because the risk being managed is reader fatigue rather
  than a word count. `/consent-theatre/` was allowed to land at 2,996 words in round 11 and
  `/nothing-to-hide/` at 3,030, both deliberately. The nine-objection page is still the
  ceiling in one sense: a tenth objection needs something else to go.
- Use section dividers with intent. `/nothing-to-hide/` uses `---` in exactly two places
  so the nine answers read as one sequence rather than nine entries in a database.

---

## 4. Citation discipline: the point of the whole project

`data/sources.yaml` is the **single source of truth**. Pages declare source ids in
frontmatter and reference them inline with `{{< cite "source-id" >}}`. The site's claim is
that its sources are real, dated, and checkable, and that claim degrades silently as
pages are added.

### Fields

- `id`: referenced by pages and by the `cite` shortcode.
- `url`: `null` means **not publishable**. Do not invent or guess one.
- `verified_on`: the date the URL was last confirmed to resolve. `null` blocks publishing.
  **A status code is not a confirmation.** Before setting a date here, control-probe the
  domain: request a path that cannot exist. If it answers with the same code, the code
  proves nothing and the value is `null` (§7, gotcha 2 and gotcha 10).
- `archive`: Wayback snapshot. **10 of the 58 sources are `null` here; 48 are filled.**
  This was 3 of 61 before round 10, so the largest publishing blocker is now most of the
  way closed. The 10 are 9 with no snapshot in the Wayback Machine at all, plus
  `solove-taxonomy`, which has no URL to snapshot. Two of the 11 that used to be in that
  list, `mailbox-org` and `gmail-scanning-2017`, left the file with the two dropped pages on
  2026-10-15, so that fall is bookkeeping rather than archiving and should not be reported as
  progress. `edpb-consent-or-pay` was the other of the pre-round-11 pair until round 11 gave
  it a URL and snapshotted the page in the same session, so that count moved by work rather
  than by luck. Do not re-run the archiving pass over the whole file; it is done, and the 9
  blanks were confirmed against six or more separate well-formed API responses each.
- `weakness`: what the source is bad at. Every source has one. Recording it is the
  difference between a bibliography and a decoration.
- `supports`: the specific claims this source can carry.

### Rules

- Every factual claim gets a dated, linked source. No exceptions.
- Anything legal or policy gets a **"status as of"** line, and `status_as_of` frontmatter.
- **Prefer primary sources**: the ruling, the study, the regulator's decision, the
  project's own documentation. News coverage only when it's the only record.
- **When a number can't be verified, do not state it.** Two examples in the existing
  pages, both deliberate: the fingerprintability percentage was omitted rather than
  guessed, and readers are told to check current Web Almanac figures rather than trusting
  a quoted one "including in this sentence." The merged `/nothing-to-hide/` adds a third:
  it says the mechanism by which someone else's exposure reaches a credit decision, and
  says nothing about how often that happens, because nobody publishes that count. A
  plausible invented number would be fatal here. **Descriptive honesty beats false
  precision.**
- **The new convention, from round 8: a source on a blanket-blocked domain gets an
  `archive:` link and `verified_on: null` with a comment naming the block.** The archived
  copy is then the thing that was actually read, and the entry says so. Copy this pattern
  for `ftc.gov`, `nytimes.com`, `dl.acm.org`, `reuters.com` and the other domains in
  §7 gotcha 2.
- **Watch for unsourced background knowledge, which is the failure mode an AI-written page
  is most prone to.** Round 11 produced a clean example, on a page that was itself dropped on
  2026-10-15: a sentence on `/swap-shop/` said
  Quad9 is "a non-profit rather than a company", which is probably true and was not sourced
  to anything. Checking it found the phrase only in a *sponsor's quote* on Quad9's homepage,
  not in Quad9's own description of itself, so the clause was cut. The rule that catches this
  is the one already in §4, applied to yourself: if the sentence would need a citation in
  someone else's article, it needs one here, and plausible is not the same as verified.
- **`supports` items must be plain strings.** An unquoted colon inside a list item
  (`- Foo: bar`) makes YAML build a mapping instead of a sentence, so `/sources/` would
  render a dictionary where a claim belongs. Nothing else notices, because the file still
  parses and the citation graph is unaffected. One such item sat in `sludge-audits` for
  several rounds and was found and fixed in round 8; `check-content.py` now fails on it
  (check 9 in its docstring).
- Archiving: snapshot each source and fill `archive:` before publishing.

### Sources added in round 10

| id | What it carries |
|---|---|
| `edpb-cookie-banner-taskforce` | EDPB, 17 January 2023. Thirteen coordinated meetings on cookie banner complaints. The documented list of banner practices regulators consider invalid, including no reject button, pre-ticked boxes, and reject offered only as an unmarked link. Official PDF read in full. |
| `cjeu-iab-europe-tcf` | CJEU press release 44/24, Case C-604/22. The Transparency and Consent String is personal data, and IAB Europe is a joint controller for recording consent choices in it. Press release, not the judgment: see the worklist in §6. |
| `conseil-etat-yahoo-cookies` | Conseil d'État, 7 October 2025, No 494300. Upheld a 10 million euro CNIL fine over cookie advertising without prior consent and over the obstacles to withdrawing consent. Primary judicial source for the withdrawal point. |
| `cnil-google-san-2025-004` | CNIL deliberation SAN-2025-004, 1 September 2025. A verification mission into tracers on the devices of signed-in users. Read from the CNIL file server, because the site itself was in maintenance. |

### Sources added in round 8

| id | What it carries |
|---|---|
| `garcia-shadow-profiles` | Science Advances 2017. Contact lists contain non-members; what users disclose predicts personal data about people with no account. Open access via PMC, verified, archived. |
| `phone-number-recycling` | Lee and Narayanan, eCrime 2021. 259 numbers, 171 tied to accounts, 100 linked to leaked credentials. Verified, archived. |
| `ftc-data-brokers-2014` | The FTC's study of nine brokers. Files on almost every US consumer, feeding credit, employment, insurance and housing decisions. Read via the Wayback copy. |

---

## 5. File map

```
hugo.toml              site config. Typographer DISABLED on purpose, see §7 gotcha 11
.tool-versions         Hugo pinned to 0.150.0 (there is no Go, so `hugo mod` cannot pin it)
.gitignore             public/, resources/, tmp/, .wayback-work/, .directory, __pycache__/
LICENSE                CC0 1.0 legal code, fetched verbatim, plus a two-line header
FOR-REVIEW.md          concept summary, plus the outcome of the review
SITE_PLAN.md           full IA, page-by-page outline, build constraints (§6b = Hugo)
AGENT.md               this file
data/sources.yaml      58 sources. SINGLE SOURCE OF TRUTH
scripts/build.sh       checks, then builds. Run the site through this, see below
scripts/check-content.py   frontmatter + citation graph, fails fast on broken data
scripts/check-links.py     network URL resolver with bot-block detection
scripts/check-dashes.py    the house punctuation rule, with a reasoned allowlist
scripts/render-bibliography.py   regenerates the generated block on /sources/ (writes)
scripts/measure-pages.py   page weights against the 100 KB budget (reads public/, never writes)
content/_index.md      the home page. Written in round 11
content/<slug>/index.md    one directory per page
layouts/               baseof.html, index.html (home, renders the page), _default/single.html
layouts/partials/      head.html, nav.html (generated from the page tree), footer.html, source-record.html
layouts/shortcodes/    cite.html, source-list.html
assets/                css/main.css, favicon.svg (Hugo Pipes: minify + fingerprint)
drafts/README.md       the voice decision, and the reasoning behind it
drafts/nothing-to-hide--B-objections.md   the adopted shape, marked superseded
```

### Build (scaffolded in round 10)

The site builds and serves as of round 10. There is no Hugo build **error** any more,
and the missing-pieces note that used to sit in §6 is closed.

```bash
sh scripts/build.sh          # checks, then builds into public/
sh scripts/build.sh serve    # checks, then http://localhost:1313 with live reload
```

**Always build through `scripts/build.sh`, not a bare `hugo`.** Two reasons, both of
which cost time in round 10:

1. It sets `HUGO_CACHEDIR` to `tmp/hugo_cache`. Hugo defaults to `$HOME/.cache/hugo_cache`,
   and where `$HOME` is read-only (sandboxes, some CI) a bare `hugo` fails with
   `mkdir ... read-only file system` and **exits 1 even though the site rendered fine**.
   `cacheDir` cannot fix this in `hugo.toml`, because Hugo requires an absolute path there
   and hardcoding one makes the config machine-specific.
2. It runs the four checks before Hugo. A page can pass every script and still fail to
   render, so both halves are load-bearing, and a broken citation graph should stop the
   build before Hugo spends time on it.

**What was built, and the three traps found while building it:**

- **`{{< cite >}}` numbers by frontmatter position.** The marker number is the source's
  index in the page's `sources` list, and `{{< source-list >}}` numbers the same list the
  same way, so marker N always resolves to entry N. Re-verified on all 11 pages in round 11.
  **One claim this bullet used to make is false and should not have been written as
  verified**: that pages declare their sources in *first-citation* order, so the markers run
  1, 2, 3 down the page. Eight of the eleven do not, and their markers jump around as a
  result (`/nothing-to-hide/` reads 1, 10, 9, 2, 3 ...). Nothing is broken: the numbers are
  internally consistent and every link resolves. It is a cosmetic ordering issue, left
  alone on purpose rather than renumbered across eight pages in round 11. The check that
  matters is the one that passes: marker N resolves to entry N.
- **`.Site.Data.sources` is a slice, not a map.** `data/sources.yaml` is a list at the
  root, so `index .Site.Data.sources "some-id"` fails with *cannot index slice/array with
  type string*. The id to record map has to be built with a loop. It cannot live in a
  partial either, because Hugo cannot return a value from a partial, so the `source-list`
  shortcode builds it and passes the record down.
- **Do not use `reflect.IsTime` on these dates.** Hugo returns a **string** for
  `2019-10-01` and an `int` for a bare year like `2016`, never a `time.Time`, and
  `reflect.IsTime` errors on an `interface{}`. `printf "%v"` renders every case correctly.
  This was probed, not assumed; the comment in `source-record.html` says so.
- **The menu is generated now, because a hand-written one lied.** Until round 11 `nav.html`
  listed six pages by hand, and five of the twelve pages that then existed were simply absent
  from it: `/swap-shop/`, `/analytics/`, `/myths/`, `/what-leaves-your-browser/` and
  `/receipts/`. Nobody noticed until the maintainer went looking for a page and could not find
  it. It now ranges over
  `.Site.RegularPages.ByWeight`, so a page cannot be left out, and the label comes from an
  optional `nav` frontmatter field, so a page can be headed "Nine Things People Say" and still
  appear in the menu as "Nothing to hide". Every content page carries a label; a page
  without one falls back to its title. The current page is marked with `aria-current="page"`.
  Two of the five pages named above were dropped on 2026-10-15 and the generated menu followed
  without an edit, which is the point of generating it: nine links, in weight order, no gap.
- **Watch out when checking minified output.** `--minify` strips quotes from simple
  attributes (`<sup class=cite>`), so any verification regex must accept both `class=cite`
  and `class="cite"`. A quote-only regex reports zero citations on a page that has
  seventeen, which is how a false alarm was raised in round 10.

### Page inventory

**Done: all ten pages** (the home page plus `content/`, 26,895 words, measured on
2026-10-15 as body words after frontmatter, whitespace-split, generated text included):

| Page | Words | Shape |
|---|---|---|
| `sources/` | 8,870 | reference. *Mostly generated from `data/sources.yaml`* |
| `nothing-to-hide/` | 3,009 | B, merged: nine objections, A's opening, A's concession, two harms argued |
| `consent-theatre/` | 2,996 | A, explanatory, with the static eight-click walkthrough |
| `dark-patterns/` | 2,351 | field guide, 17 patterns |
| `what-leaves-your-browser/` | 1,979 | A |
| `one-page-load/` | 1,922 | A. *Is itself the interactive's fallback* |
| `myths/` | 1,671 | B-style units, 7 myths |
| `analytics/` | 1,597 | A, practical |
| `start-here/` | 1,148 | reference |
| `/` (home) | 704 | thesis, three doors, no-banner callout |

**On those numbers.** The count comes from one command run over the whole tree, so it is
reproducible and the two halves of this file cannot disagree:

```bash
awk 'BEGIN{fm=0} /^\+\+\+$/{fm++; next} fm>=2' content/_index.md content/*/index.md | wc -w
```

for the total, and the same expression with a single file for one page. Treat it as one
measurement, not as a target.

**No core pages remain, and the target shrank twice:** `/the-rules/` went in round 11, and
`/swap-shop/` and `/receipts/` went on 2026-10-15, so the site is ten pages.

**The two pages dropped on 2026-10-15, and what went with them.** Both were written, sourced
and published before the maintainer asked for them to go, after discussing the site with the
friend who originated the project. Neither was replaced by anything, and that is a decision
rather than an oversight:

- **`/swap-shop/`** was 2,705 words over eight substitutions, each carrying what the switch
  costs. Its sources were the fifteen in the `swap-shop` block of `data/sources.yaml`, twelve
  of which no other page cited and all twelve of which were deleted the same day. **The search
  material survives in a reduced form**: the Ecosia claim and its caveat are now in the
  disclosure on `/sources/`, together with the Mullvad DNS notice. Nothing else on the site
  carries the swap argument, so treat "which tools do I use instead" as a deliberate gap
  rather than as a page somebody forgot to write.
- **`/receipts/`** was 1,338 words of the site's own measured numbers, already cut from 3,129
  on 2026-10-14. Its content is gone rather than moved, so no page publishes the site's
  figures any more, and the three defects it published (WCAG 3.1.2 language of parts, citation
  markers below the 2.5.8 target size, and a missing `content-security-policy`) are tracked in
  §6 and §9 instead. `scripts/measure-pages.py` survives as an internal check, and **both of
  its budget rows now pass**: the heaviest page is `/sources/` at 26,440 bytes gzipped and
  89,184 raw, where the raw row was over 100 KB before the drop. See §7 for the figures.

`/the-rules/` was dropped by the maintainer, for reasons worth not re-litigating: it is the
one page whose whole value is being current, on a site whose footer now states that it is not
maintained on a schedule; its primary sources are the least readable on the web (§7, gotcha
10); and the argument it would have made is already carried by `/consent-theatre/`,
`/nothing-to-hide/` section 3 and `/analytics/`.

**All three dropped outlines survive in `SITE_PLAN.md` §4 with the reasoning attached**, so a
future session does not re-add them out of tidiness.

**`/` had a receipts section, and no longer does.** It was written in round 11 with a badge
pointing at `/receipts/`, which `SITE_PLAN.md` §4 asked for, and the section came out on
2026-10-15 with the page. The rest is unchanged: thesis, three audience doors, the flagship
teaser, the action-ladder preview, and the "nothing to ask your permission for" callout. No
carousel, no newsletter box, no "trusted by" strip, each of which is a dark pattern in
miniature.

**Note on the interactives, written in round 10.** Two were planned. `SITE_PLAN.md` §5
calls them *Cookie Banner Hell* on `/consent-theatre/` and *would-this-bother-you* on
`/nothing-to-hide/`. **Neither has a script, and that is the correct state for both.**
`layouts/shortcodes/interactive.html` exists and renders any content as static HTML inside
`<section class="interactive" data-interactive>`, so the enhancement hook and the
no-JavaScript fallback are already one and the same thing. Use it as
`{{< interactive >}} ... {{< /interactive >}}`.

- **`/nothing-to-hide/` is complete.** The seven harms are listed with a one-line
  explanation each and a pointer to the section that argues it, it needs no script, and it
  closes a dangling promise: the page used to say "the interactive below" and point at
  nothing. **Round 11 closed the last gap on it**, by writing the two harms that had only
  been named, `secondary use` and `dignity`, into a section headed "Two harms that needed
  arguing", and by replacing the line that admitted they had no section of their own. The
  page went from 2,467 to 3,030 words and was allowed to land there (§0 item 3). Two things
  to know before quoting it: the dignity passage is labelled in the prose as the page's only
  normative claim, and its factual predicates rest on two sources that still carry
  `verified_on: null` (`ftc-data-brokers-2014`, `zuboff-surveillance-capitalism`), which the
  page displays next to them. The `secondary use` passage leans on `google-build-profiles`,
  which is verified and archived, and whose own record says to quote it verbatim, so it is
  quoted.
- **`/consent-theatre/` is written, and its interactive is written too.** See the
  description below; the 47-click counter was the wrong design and has been replaced.

### The `/consent-theatre/` interactive: how the 47-click problem was solved

`SITE_PLAN.md` §5 asked for a "simulated site where the honest opt-out takes 47 clicks,
with a visible click counter." **That specific design was abandoned in round 10, and the
reason matters because the same trap will come up again.**

A counter has to count something, and the only honest thing to count is a *measured*
sequence from a real banner. That could not be measured here (it needs a browser and a
real site), and inventing "47" to make the counter work is exactly the false precision §4
forbids: a made-up statistic on a site whose whole argument is that claims should be
checkable, sitting in the very place a sceptical reader is most likely to check it.

What was built instead is **"Eight clicks through one banner"**: an eight-step walkthrough
of one composite banner, where **every step is a defect the EDPB Cookie Banner Taskforce
already recorded**, taken from the report in a plausible order. The page says out loud that
it is a composite rather than a survey of real sites, and that the sequence is not a
measurement.

So the interactive works because it is not an invented measurement. It is a *reading* of a
sourced document, ordered the way a user meets it. That distinction is the trick, and it
applies to the remaining interactives on the should-tier list.

It ships with **no JavaScript**. It renders as static HTML through
`layouts/shortcodes/interactive.html`, so it is readable with scripting off, and a script
that adds a counter or a reveal later attaches to `section.interactive[data-interactive]`
without the content changing.

**If a real click count is ever measured**, the upgrade is additive: keep the eight
documented defects, and add the counter as enhancement on top. Do not replace the sourced
content with the counter.

**Note on Ecosia, changed on 2026-10-14 and moved on 2026-10-15.** The search-index claim was
the one section of the swap shop that rested on a source nothing else carried, and it is why
`ecosia-eusp-index` is still in `data/sources.yaml` after the page that used it was dropped.
The maintainer asked on 2026-10-14 for Ecosia to lead the search section, on the criterion that
section already applied, which is whose index answers your query, since Ecosia has been
building one with Qwant. The page it led is gone; the claim and its caveat are now in the
disclosure on `/sources/` headed "What I actually run". **The caveat is load-bearing and must
not be trimmed**: that source is the company's own account, published in French, and it
establishes only that the joint index exists and that French users are served from it directly.
It says nothing about coverage elsewhere, about result quality, or about how much of a query is
still answered by a licensed index. `/sources/` used to say that the swap-shop recommendation
was unchanged and that this was not an endorsement; that wording had to change on 2026-10-15,
because the recommendation it described no longer exists anywhere on the site.

**Note on `/sources/`, written in round 9 and re-measured on 2026-10-15.** It is the one page
exempt from the length rule in §0, because it is a bibliography rather than an argument:
8,870 words in total, of which the great majority is the generated entries, in four groups,
with a reverse index at the end. The generated block sits between two HTML markers and is
written by `scripts/render-bibliography.py`; **never edit inside the markers by hand**,
because the next run overwrites it. The markers also make the page splittable: if 8,870
words turns out to be too much for one page at build time, moving the block to
`/sources/bibliography/` is a change to one path constant in the script, not a rewrite.

**Both `/sources/` TODOs are now closed as page text**, the contact route and the tools
disclosure, and one check on the first is still outstanding: §9 item 4 has it. The disclosure
became "What I actually run" on 2026-10-15, when the swap shop it pointed at was dropped, and
it cites three sources (`ecosia-eusp-index`, `mullvad-public-dns`, `mullvad-dns-shutdown`),
which is why those three stayed in the file when the other twelve swap-shop sources went.

**Note on `/one-page-load/`:** the page's timed request ledger *is* the progressive
enhancement fallback the interactive needs. When the Hugo build happens, the `<ol>` of
requests should be rendered from that content and the scroll animation should merely
enhance it. Do not rewrite the sequence as a JS data structure and leave the prose
behind.

**Should-tier** (build if time): accessibility, sustainability, attention, open-source,
ai-crawl, browser-power, subscriptions, decision-guide, glossary, tracker.

**One known duplicate to leave alone:** `weight = 3` is set on both `one-page-load` and
`what-leaves-your-browser`, and has been since before round 10. `check-content.py` does
not flag it and nothing depends on the order, so changing it now would be churn. New
pages should take a weight that is not already used. **The dropped pages left two weights
unused, 8 and 11**, which is harmless: the menu orders by weight and never shows it. Do not
renumber nine pages to close the gap.

---

## 6. Known issues & worklist

**Blocking publication:**

1. **`archive:` is `null` on 10 of the 58 sources, down from 62.** Round 10 filled 52 and
   round 11 added six more; two further entries left the file with the dropped pages on
   2026-10-15 (`mailbox-org`, `gmail-scanning-2017`), and that is bookkeeping rather than
   archiving, so do not read the smaller number as progress. The remaining 10 are **not a
   to-do that another pass will fix**: 9 have no Wayback snapshot at all (`netflix-prize`,
   `eckersley-fingerprinting`, `ecc-encrypted-client-hello`,
   `austrian-dsb-google-analytics`, `ga4-consent-mode`, `plausible`, `matomo`,
   `ftc-amazon-25b`, `ftc-click-to-cancel-rosca`) and `solove-taxonomy` has no URL to
   snapshot. `edpb-consent-or-pay` left this list in round 11 when it gained a URL, and its
   snapshot was taken the same session over plain HTTP, with no account:

   ```bash
   curl -sSL "https://web.archive.org/save/<the-url>"
   ```

   **That is worth trying before calling the 9 a human-only job.** Save Page Now worked on
   the first attempt for a page the availability API had reported as unarchived on four
   consecutive passes, and the archived copy still contained the PDF link that made the
   page worth citing. Verify it afterwards by fetching the returned snapshot URL and
   checking the title, not by trusting the tool's own output.

   **The API trap, learned the hard way in round 10.** The Wayback availability API
   returns *spurious empty results* and "Temporarily Offline" HTML, so a single empty
   `{}` means "ask again", not "no snapshot". The round-10 pass reported 35 empties on
   its first run and recovered **24** real snapshots by re-querying across six passes
   (12/7/1/2/2). Anything that treats one empty response as a negative will silently
   under-report coverage. Retry, and only believe a blank after several clean passes.

   **Round 11 made that trap worse, and it matters here.** The API returned empty on
   **eight consecutive passes** for a URL whose snapshot replays perfectly, and on four
   for another, so "several clean passes" is not enough either. **The list of 9 blanks
   above should therefore be read as "no snapshot found by that method", not "no snapshot
   exists".** The reliable check is the CDX API with a status filter, which is recorded in
   §7 gotcha 10, and the practical fallback is Save Page Now, which worked here on the
   first attempt for a page the API had denied four times.
2. **Sources that cannot be verified automatically and need a human to open them.**
   Their domains answer any path, including impossible ones, with the same 401/403/404,
   so the status code proves nothing (§7, gotcha 2). As of round 8 the unverifiable six
   were `ali-ad-delivery`, `eckersley-fingerprinting`, `penney-chilling`, `codeberg`,
   `ftc-amazon-25b` and `ftc-click-to-cancel-rosca`, and `codeberg` has since left the file
   with the dropped pages, so the list is **five**. Four more are treated as
   bot-blocked after a 404 (`ftc-mobilewalla`, `ftc-gravy-venntel`,
   `ftc-surveillance-pricing`, `ftc-data-brokers-2014`). **The four CNIL sources left this
   category on 2026-10-15**, when the maintenance block that put them here was measured to be
   over (§7, gotcha 10), so they can be opened and dated by hand now; nobody has done that, so
   they still carry `verified_on: null`. **Do not set
   `verified_on` on any of these without actually opening the link.**
3. **`cjeu-iab-europe-tcf` is a press release, not the judgment.** It carries the
   official holdings and the court's own disclaimer, so it is usable, but the reasoning
   is missing from it. The full text of Case C-604/22 needs a browser: EUR-Lex serves a
   JavaScript challenge to anything automated and `curia.europa.eu/juris` serves a
   script shell (§7, gotcha 10). Replace the entry's URL, or add the judgment alongside
   it, once a human has opened it and confirmed a stable link.
4. **`cjeu-planet49`'s `verified_on` is not evidence.** It was set from a `202` that
   `check-links.py` reports as `OK`, and round 10 established that EUR-Lex returns that
   code for paths that cannot exist. Either open it in a browser and record that, or set
   it to `null` with an explanatory comment (§7, gotcha 10). The entry is used by
   `/myths/` and `/consent-theatre/`, so it is load-bearing.
5. ~~**Two sources have no URL** and are flagged, not guessed.~~ **Half closed in round
   11; the half still open is the one that needs a real search.**
   - `edpb-consent-or-pay` now carries the official document page as `url`, with
     `verified_on: 2026-10-14` and a Wayback snapshot taken the same session. Following the
     round-10 notes turned up two corrections worth keeping: the PDF lives under
     `/system/files/**documents**/2024-04/...` (the shorter path recorded here only
     redirects to it), and the opinion carries an **October 2024 corrigendum** correcting
     two paragraphs and five footnotes, which is now in the entry's `weakness` because this
     site paraphrases that opinion on two pages. The date rests on the page's own title,
     not on its status code: this host answers 200 for paths that cannot exist (§7, gotcha
     10).
   - `solove-taxonomy`: **still open.** Solove, *A Taxonomy of Privacy*, 154 U. Pa. L. Rev.
     477 (2006). Round 11 searched again and found only mirrors of the PDF and works that
     cite it. This project does not cite a mirror as the record, so it stays `url: null`.
     Find the publisher's or SSRN's own page. **This is now the only item in §6 that an
     agent could finish without a human.**
6. ~~**No Hugo build exists.**~~ **Closed in round 10, and this entry was left behind by
   mistake.** The build exists: all four checks pass and `hugo` renders all ten pages
   with no errors through `scripts/build.sh` (§5). It is kept as a stub only so the numbering of
   this list does not shift, because other sections refer to these items by number. If you
   are reading this looking for a missing piece, it is not missing.
7. ~~**Two deliberate gaps on `/sources/`, both marked with an HTML comment TODO in the
   page.**~~ **Closed in round 11, and re-checked on 2026-10-15.** Both are published: the
   contact route for reporting an error, and the tools disclosure, which is now headed "What I
   actually run" because the swap shop it used to point at was dropped. One sub-item is still
   open and lives in §9 item 4: whether GitHub accepts anonymous issue filing on the
   repository, which decides whether the published contact route can receive anything. Kept as
   a stub so the numbering does not shift.

**Nice to have:**

- `penney-chilling` currently links Reuters coverage, not the *Berkeley Technology Law
  Journal* article. The entry says so in capitals. Replace and quote the effect size
  from the paper; the page deliberately avoided stating one.
- `ecc-encrypted-client-hello`: author list only partially confirmed (Hajda, Oezdil).
  The open-access `dl.ifip.org` copy did not respond; the IEEE record is linked instead.
- `austrian-dsb-google-analytics` links a law-firm summary, not the decision. Primary is
  case DSB-2021-0.586.257.
- `ccpa-sale-definition` links a third-party mirror. `leginfo.legislature.ca.gov` is
  official; the subsection number has moved and needs confirming.
- **The CNIL block is over, found on 2026-10-15, and this reopens four sources.** Round 8 saw
   the CNIL sources return 503, and round 11 re-measured the domain as still blanket-blocked.
  Neither is true any more: on 2026-10-15 `www.cnil.fr` answered **301** for its root, **404
  with 71176 bytes** for a path that cannot exist, and **200 with 636667 bytes** for a real
  decision PDF, while an impossible sibling PDF returned **404 with 71173 bytes**. `linc.cnil.fr`
  discriminates too (200 for its quiz page against 404 for an impossible path, 93914 and 39766
  bytes). **So the four CNIL sources can be verified by hand now**, which is the cheap work this
  finding reopens: `cnil-analytics-exemption`, `cnil-analytics-self-assessment`,
  `cnil-dark-patterns-quiz` and `cnil-google-san-2025-004` all carry `verified_on: null`
  because the pages could not be read when they were recorded. Reading them is a verification
  step rather than a status code, and the archived copies read in rounds 10 and 11 remain the
  fallback if the domain blocks again.

**Found in round 11: cheap upgrades to sources the site already cites.** Each was read and
control-probed before being recorded here, and each is a small edit to `data/sources.yaml`.

- `ccpa-sale-definition` links a third-party mirror. The official `leginfo.legislature.ca.gov`
  now answers 403 to everything, but an **archived copy of that official page is readable**
  (200, 205439 bytes): `http://web.archive.org/web/20261002012921/https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140`.
  That closes the "official source" nice-to-have below, without using the mirror.
- `ec-x-fine-120m` cites ABC News. The European Commission's own press release is readable as
  a PDF and control-probes cleanly (a bogus reference returns 404 in JSON):
  `https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_2934/IP_25_2934_EN.pdf`.
  Note that the press-corner HTML pages are soft 404s: they return 200 with a generic shell.
- `cjeu-iab-europe-tcf` cites the press release, which states the holdings without the
  reasoning (§6 item 3). The **full judgment is readable as an archived EUR-Lex PDF**
  (598182 bytes, 17 pages): `https://web.archive.org/web/20250224023804/https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=celex:62022CJ0604`.
  Adding it alongside the press release would let `/consent-theatre/` cite the reasoning.
- `cnil-google-san-2025-004` now records in its `weakness` that the PDF it links is the
  **English courtesy translation**, with the French text prevailing. Round 11 read that warning
  off the PDF itself, and also confirmed the /sites/ file server genuinely discriminates (a
  real file returns 200 application/pdf while a missing one returns the 503 maintenance page),
  which is a weaker claim than round 10 made for that host.
- **Fines levied against fines collected is verifiable, but only per member state.** Ireland's
  Data Protection Commission publishes both on its own page
  (`https://www.dataprotection.ie/en/dpc-guidance/decisions/fines`, over 4.4 billion euro levied
  against roughly 20 million collected) and that page control-probes correctly. No EU-level
  aggregate was found, and the EDPB pages requested returned 404, so an honest page may state
  Ireland's figures and must not present them as Europe's. Nothing on the site currently makes
  this claim.

---

## 7. Environment & gotchas

**Installed:** Hugo `v0.150.0+extended`, Python 3.14.8 with PyYAML 6.0.3, Node v22.22.2
(installed on the machine but **unused by this build**), git 2.56.0, curl 8.18.0,
`pdftotext` 26.01.0 from poppler. The machine is Fedora Linux 44 (KDE Plasma).

**Not installed:** Go, so `hugo mod` cannot pin the Hugo version and `.tool-versions` does it
instead. **No headless browser tooling at all**: no Lighthouse, axe, Playwright, Puppeteer,
geckodriver or pa11y. A flatpak Firefox exists at `~/.local/bin/flatpak/firefox` but cannot
be launched from an agent shell (`Unable to allocate instance id`), which is why the site
published no LCP figure and no audit scores while `/receipts/` existed, and why it publishes
none now: there is nothing to run, rather than checks that passed. The styling pass in §9 item
8 is the next thing this limitation bites: the maintainer has to look at the result.

**Git: initialised in round 11 and connected to GitHub on 2026-10-14.** Branch `main`, first
commit `09f1643`, 39 files. The repository is no longer unprotected, so a maintenance sweep
can be diffed instead of copied first, and the `md5` records below are a convenience rather
than the only evidence of drift. The remote is `origin` =
`git@github.com:osszevissza/the-third-party.git`, **connected and pushed on 2026-10-14**, with
`main` tracking `origin/main`. That first push carried the eight round-11 commits and the
remote was empty beforehand, so nothing needed reconciling; two commits followed the same day.
**Do not quote a head hash in this file**, it was already stale within the hour: use
`git log --oneline -1` and `git log origin/main..HEAD` instead, and expect the second to be
empty.

**Commit messages are a few words on one line.** Round 11 wrote them that way and the
maintainer restated it on 2026-10-14, so it is the house rule rather than a preference: the
reasoning behind a change belongs in this file, and `git log --oneline` should read as a list
of subjects rather than as paragraphs. One exception, and only one: a correction of something
already published on the site earns a sentence saying what was wrong, because that is the kind
of thing a reader may come looking for.
`public/`, `resources/`, `tmp/`, `__pycache__/` and the scratch directories are ignored, so
the repository holds source rather than build output. The audit that preceded the push is
worth repeating before any future public push: 39 tracked files, no key, token or password
in any of them, no absolute home path, and `git status --untracked-files=all` showing that
every untracked path is ignored rather than merely unnoticed.

**The site went live on 2026-10-14 at 19:31:35 UTC**, which is the `last-modified` header on
the deployed pages, roughly an hour after the domain was registered in statichost's panel and
its TLS certificate was issued (18:34:14, Let's Encrypt, that hostname alone, valid to
12 January 2027). **The deploy is verified by content**, not by a status code: all twelve
pages were fetched and each one's own `<title>` and `rel=canonical` read off the response.
What the host sends, measured from outside with `curl`: HTTP/2 and HTTP/3 both work, HSTS
with `preload`, `x-content-type-options: nosniff`, `cache-control: public, max-age=0,
must-revalidate`, `etag`, `last-modified`, `vary: Accept-Encoding`, **gzip but no brotli**,
and **no `content-security-policy`**. It discriminates correctly, which is what makes its
codes worth reading: a path that cannot exist returns `404` with a 13-byte body while a real
page returns `200`. All of that was published on `/receipts/` under "What the host sends"
until that page was dropped on 2026-10-15; the measurements above are the record now, and the
missing header is still a defect (§8).
**A push to `main` does not deploy: the deploy is triggered by hand on statichost's own
dashboard.** The maintainer confirmed this on 2026-10-14, adding that it has always worked
that way and that they do it every time. **So the manual step is routine, not a fault**: do not
re-diagnose it, do not read it as a broken webhook, and do not spend a session looking for a
setting to switch on. Why statichost requires it is unknown and does not matter.

**The part worth keeping is that this was first written up wrongly.** The first deploy landed
within a couple of minutes of the push carrying the domain change, and §7 recorded that as
"pushing appears to deploy". The next two pushes did not deploy at all: the live `last-modified`
stayed at 19:31:35 and the new text never appeared, checked over several minutes. The timing was
a coincidence, and the coincidence was the entire evidence. **Pushing is not publishing.** After
a push the deploy is the maintainer's step, and the check afterwards is ours: fetch the page and
read its own title, or grep the served HTML for a phrase that exists only in the new commit.
`curl -sS https://third-party.statichost.page/sources/ | grep -c "a phrase from the commit"` is
the whole check, and `/sources/` is the page to point it at when the change is this one, since
the drop is invisible there until a deploy happens.

**Until somebody triggers one, the live site is a past version of itself, and it can be a
confidently wrong one.** Before the second deploy of 2026-10-14, the live `/receipts/` was
telling readers that nothing was published at the site, in the very deploy that had made that
sentence false. Nothing in the repository can tell you which commit is live, and **the
`last-modified` header is not the answer either**: it is per file, so it only moves for files
whose bytes changed. After that second deploy, `/receipts/` and `/swap-shop/` served new text
while the home page still reported 19:31:35, because the home page had not been edited.
**The check that works is a phrase**, picked from the commit and grepped out of the served
HTML, which is how both deploys here were confirmed. Deploy as soon as a published claim
changes rather than batching commits, because the cost of waiting is a live page that
contradicts itself. **The 2026-10-15 drop is the largest version of this the site has had**:
until the maintainer deploys, the live site serves ten pages plus the two that the repository
no longer contains, and the five edited pages still carry their old wording.

**The host's gzip is looser than local measurements.** The figures `scripts/measure-pages.py`
prints are a local `gzip -9` measurement and are the reproducible ones; statichost compresses at
a lower level and sends the icon uncompressed, so the wire runs about 3% larger. **Nothing on
the site publishes either number any more** (the page that did was dropped on 2026-10-15), so
this is a note for reading the script's output rather than for keeping a page true. If a future
measurement is taken from the live site instead of the build, say which of the two it is,
because they are not interchangeable.

**Known-good state on 2026-10-15**, for use as a reference point if something is later
suspected of having drifted. All four scripts pass with 19 warnings and 0 errors, the build
renders all ten pages, and `data/sources.yaml` is:

```
md5  fda82cb39476a96c1ea458fc69b3859a
58 sources: 48 with an `archive:` value, 10 without, 19 `verified_on: null`
```

The round-11 figure it replaces was `md5 5ab9db839c23cf21bd756ecd51ca9484`, 70 sources, 58
archived, 12 without, 20 null; the difference is the 12 deleted records plus this file's own
edits. Git was initialised in round 11 (`main`, first commit `09f1643`), so the md5 is a
cross-check rather than the only record of the file's state, and `git diff` is the better tool
when something looks wrong.

**The page weights, measured on 2026-10-15 after the drop** (a rebuild reproduces them, and
`scripts/measure-pages.py` prints them): ten pages, median 9,126 bytes gzipped and 25,216 raw,
heaviest `/sources/` at 26,440 gzipped and 89,184 raw, which is 2.90 times the median, and the
whole site with its shared stylesheet and icon counted once at 91,789 bytes gzipped. **Both
readings of the 100 KB budget pass for the first time**, because `/sources/` lost 1,453 words
of generated bibliography with the 12 deleted records: the raw row used to be over the line at
103,681 bytes. **These go stale the moment anything changes, and round 11 proved it four
times.** Every one of those was caused by an ordinary content edit, because `/sources/` is both
the heaviest page and the bibliography, so adding or rewriting a source moves the numbers.
**Re-measure using the referenced-asset method in gotcha 13.**

**The exclusion rule for the median is retired, and it should not come back.** Until
2026-10-15 `/receipts/` was left out of the median, because a page that is part of a statistic
it publishes can never report that statistic exactly: editing it moves the number in a way the
page cannot observe, since the measurement necessarily precedes the sentence describing it. The
row read "the other 11" for that reason. Nothing publishes the figures now, so the whole set of
ten is the honest median and the script no longer excludes anything. **Do not reintroduce an
exclusion to match an old sentence**: the rule existed to protect a published claim, and there
is no claim to protect.

### Gotchas that have already cost time: don't repeat them

1. **YAML: never start a list item with a quoted scalar followed by a comma.**
   `- "Sale" is defined broadly` parses the quote as a complete scalar and then chokes
   on the comma. This broke `data/sources.yaml` **twice**. Write
   `- The word sale is defined broadly` instead. `check-content.py` fails fast on this
   rather than emitting 80 cascading citation errors, but it's avoidable.

2. **A non-OK status code is usually meaningless: control-probe before trusting one.**
   Reuters answers **401**, DLA Piper **429**, and `dl.acm.org`, `nytimes.com`,
   `lexology.com`, `loc.gov` and `ftc.gov` answer **403 or 404 for any path at all**,
   including paths that cannot possibly exist and their own roots. `check-links.py` now
   requests a deliberately bogus path on the same origin and downgrades those sources to
   **UNVERIFIABLE** (`N/A`), because calling them "blocked but probably fine" manufactures
   false confidence.

   The real conclusion: **automated verification is impossible for those domains.** The
   control probe is itself noisy, since rate limiting changes results between runs and
   the shape of the bogus path affects the code returned, so a `BLCK` verdict is not
   reassurance either. Every non-OK result needs a human to open it, and the archive link
   is the practical way to read a blocked page from a terminal.

   These sources are marked `verified_on: null` with an explanatory comment. **Never set
   `verified_on` on a source whose domain blanket-blocks probes.** That mistake was made
   on ten sources and had to be reversed.

3. **Hugo extended's Sass is libsass 3.6.6: deprecated and frozen at an old CSS
   level.** It cannot parse native nesting, `@container`, or modern colour functions.
   **Write plain CSS.** Use the extended build for image/WebP processing, not Sass.

4. **`hugo mod` requires Go, which is absent.** Pin the Hugo version in the README or a
   `.tool-versions` file instead.

5. **Do not use a Hugo theme.** Nearly all of them pull Google Fonts, Font Awesome,
   jQuery or a CDN, which violates the zero-third-party rule outright.

6. **Editing a file after running or `chmod`-ing it invalidates the read cache** and the
   edit will be refused until the file is re-read. Expect this with the scripts.

7. **Citation syntax is `{{< cite "source-id" >}}`, a Hugo shortcode, with the angle
   brackets.** Writing `{cite source-id}` (single braces) fails silently: it renders as
   literal text, the checker's regex doesn't match it, and the page ends up *declaring*
   sources it never *cites* while *citing* sources it never *declares*. This happened on
   the first draft of `/swap-shop/` (11 broken citations) and produced 18 errors at
   once. If a page produces a sudden cluster of "unknown source id" errors, check the
   shortcode syntax before hunting for typos in the ids. The page it happened on has since
   been dropped, which changes nothing about the trap.

8. **Two citation conventions, used deliberately.** `{{< cite >}}` is for *claims* and
   must be declared in frontmatter. A plain markdown link is for *pointers* ("here is
   the project's website") and needs no source entry. Keeping these separate stops the
   sources file degenerating into a link dump while keeping every claim attributable.

9. **A bulk punctuation sweep is verifiable, so verify it.** When the em dashes were
   removed in round 8, every file was first copied to a scratch directory and then
   diffed afterwards on the *word sequence only*, ignoring punctuation and case. That
   check catches the failure mode a punctuation edit actually has: a word quietly
   changing along with the comma. Two files were edited by a subagent that made exactly
   one bad edit each, and both were caught. If you ever do another sweep, do it this
   way, and never rewrite a file wholesale when a targeted edit will do.

10. **Found in round 10: two source verdicts that are actively false, on domains nobody
    had control-probed.** Both were being read as healthy by `check-links.py`.

    **CNIL was a blanket-blocked domain and its site was in maintenance, and that is over as of
    2026-10-15.** From round 8 to round 11, every URL on `www.cnil.fr`, including its own domain
    root and paths that cannot exist, returned **503** with a 15 KB page reading `Le site de la
    CNIL est actuellement en maintenance`. That was the loudest possible version of gotcha 2: a
    503 from cnil.fr was not a signal about the URL, it was a signal about cnil.fr. **Four
    sources had `verified_on` set on the strength of that code and were corrected to `null` in
    round 10** (`cnil-analytics-exemption`, `cnil-analytics-self-assessment`,
    `cnil-dark-patterns-quiz`, `cnil-google-san-2025-004`), and they still carry `null`, because
    nobody has read the pages since the block lifted.

    **Re-measured on 2026-10-15, and the domain discriminates again.** `www.cnil.fr` returns
    **301** for its root, **404 with 71176 bytes** for a path that cannot exist, and **200 with
    636667 bytes** for the SAN-2025-004 PDF, against **404 with 71173 bytes** for an impossible
    sibling. `linc.cnil.fr` returns **200 with 93914 bytes** for its quiz page and **404 with
    39766 bytes** for an impossible path. **So the four entries can be verified by hand now**,
    which is the work §6 item 2 hands to the next session. Do not set `verified_on` from the
    status code either way: read the page. If the block returns, the archived copies read in
    rounds 10 and 11 are the fallback, and they are readable.

    **Use response size as a second control probe, not just the status code.** That is how the
    CNIL block was originally caught: the two hosts blocked differently and the body length gave
    it away. Measured in round 10, `www.cnil.fr` answered **503 with 15184 bytes** for its root,
    a real page and an impossible path alike, while `linc.cnil.fr` answered **503 with 19336
    bytes** for both its quiz page and an impossible path: two hosts, two uniform signatures,
    identical size across good and bad URLs. Size is cheap to compare, costs no extra request,
    and catches blocks that a status code alone would hide. **The 404 pages above are the same
    test in its healthy form**: 71176 against 71173 bytes for two different impossible paths is
    a template, while 636667 bytes of `application/pdf` for the real one is not.

    **Interlude, kept because it was the practical route in:** while the website was in
    maintenance, **the CNIL file server still worked.** `www.cnil.fr/sites/...` served real
    files (a bogus path there returned 503, a real one returned 200 with the PDF), so primary
    CNIL decisions remained readable mid-maintenance. That is how `cnil-google-san-2025-004` was
    obtained in round 10, as 636667 bytes against 15184 for a nonexistent sibling, and the same
    PDF answers 200 with the same size today.

    **EUR-Lex serves a JavaScript challenge instead of documents.** `check-links.py`
    reports `cjeu-planet49` as `OK 202`, which reads as healthy. It is not. A real CELEX
    URL returns 202 with a 2036-byte HTML shell, a nonexistent one returns 202 with an
    empty body, and `curia.europa.eu/juris/document/` returns 200 with a `RPEX` script
    shell. **No EUR-Lex URL can be verified from a terminal and none of their content
    can be read there**, so `cjeu-planet49`'s `verified_on` is not evidence.

    What to do instead: for CJEU material, `curia.europa.eu/jcms/upload/docs/...` serves
    real PDFs and *does* control-probe correctly (real file 200, bogus file 404), which
    is how the C-604/22 press release was verified. For a case where the newspaper
    record is not enough and the full judgment is needed, a human has to open EUR-Lex in
    a browser. Do not paper over either problem by setting a date.

    **Found in round 11: one host can control-probe cleanly on one path shape and prove
    nothing on another.** `edpb.europa.eu` was recorded here as trustworthy because a bogus
    path under `/system/files/` returns 404 while a real PDF there returns 200. That is
    still true of the **file server**. It is not true of the **document pages**: a bogus
    path under `/documents/opinion-of-the-board-art-64/` returns **200 with 94043 bytes**,
    a generic "Documents" listing, while the real opinion page returns 200 with 44610. Same
    host, opposite verdicts, decided by the path prefix. **Compare response size, and read
    the body, before believing a 200 on a CMS-style path.** The practical rule that settled
    it: fetch the page and check that its own title is the title of the thing being cited.

    **Found in round 11: `hudoc.echr.coe.int` (ECtHR judgments) cannot be verified or read
    from a terminal at all.** It answers **403** for a real document URL, for a bogus
    document id, and for its own root, with three different body sizes (6171, 5966, 5589).
    That is gotcha 2's shape, so no ECtHR judgment can be checked here. A promising source
    (`S. and Marper v. the United Kingdom`, on retaining the fingerprints and DNA of people
    who were never convicted) was **dropped rather than cited sight-unseen** when the
    dignity argument was written, which is the rule working: the alternative was a
    confident paragraph about a judgment nobody had opened. The Wayback item page for a
    HUDOC record does resolve, so an archived copy is the route in for a human who wants it.

    **Found in round 11: EUR-Lex is not merely awkward, it is empty, and the way around it
    is the CDX API.** Every URL on `eur-lex.europa.eu`, including its own domain root and
    paths that cannot exist, now returns **202 with 0 bytes**: not a JavaScript shell with
    content behind it, an empty body. Fifteen URL shapes were tried across five instruments
    and four judgments, and none returned a single byte. `data.europa.eu/eli/...` behaves
    the same way, and `publications.europa.eu` returns only RDF metadata and citation
    graphs. **The route that works is an archived copy from before the breakage**, found
    with the CDX API rather than the availability API:

    ```bash
    curl -sS "http://web.archive.org/cdx/search/cdx?url=<url>&output=json&filter=statuscode:200&limit=5"
    ```

    That returns real snapshots from 2014, 2019 and 2022 for the instruments, plus readable
    copies of the Schrems I and Schrems II and IAB Europe judgments. **Two traps sit on top
    of it.** Recent snapshots of EUR-Lex pages are frequently replays of the empty 202 shell
    or of a JavaScript robot wall (3746 bytes), so an archived EUR-Lex URL has to have its
    body read before it is believed. And the availability API returns empty for URLs that do
    have working snapshots, on eight consecutive passes in one measured case.

    **Found in round 11: some hosts answer identically for a real document and an impossible
    one, and some do the opposite.** The Dutch judiciary makes the point with two hosts:
    `uitspraken.rechtspraak.nl/details?id=<ECLI>` returns **200 with 3892 bytes for a real
    judgment and for an impossible path**, so its codes mean nothing, while
    `data.rechtspraak.nl/uitspraken/content?id=<ECLI>` returns the judgment as 75971 bytes of
    XML for a real ECLI and **404 for a bogus one**, so it can be trusted and is the right
    citation target. Similar pairs measured this round: `govinfo.gov` serves the US Code with
    a distinguishable not-found (200, but titled "Page Not Found", 44172 bytes against
    47198), whereas `uscode.house.gov` returns byte-identical 5792-byte shells for a real
    section and a nonexistent one; `sustainablewebdesign.org` control-probes correctly (real
    200 / 82900 bytes, bogus 404 / 31088); and `leginfo.legislature.ca.gov` sits behind a
    Cloudflare challenge that answers 403 to everything, so California's code is readable
    only as an archived copy of the official page.

    **The general lesson, which is the expensive one:** a passing status code is not a
    verified source, and neither is a *failing* one. Open the thing, or say you did not.
    `conseil-etat.fr` control-probes cleanly (real path 200, impossible path 404), and so
    does the `edpb.europa.eu` file server, with the caveat above about its document pages.
    Most of this file's domains have not been tested this way and should be before their
    `verified_on` is believed.

12. **`hugo server` does not always pick up a NEWLY ADDED template file.** Found in round
    10. After adding `layouts/shortcodes/interactive.html`, the running dev server logged
    `Template added /shortcodes/interactive.html` and then failed every subsequent rebuild
    with `template for shortcode "interactive" not found`, serving **HTTP 500** on the
    affected page until it was restarted. Adding a new shortcode or partial to a *running*
    server is therefore not reliable. Restart the server after adding a template file.

    Two related traps from the same round:

    - **Do not delete `public/` while `hugo server` is running.** It has its own in-memory
      build; removing the output directory out from under it is not a supported thing to
      do. Stop the server, or use a separate output directory.
    - **`hugo server` serves its own memory, not the last `hugo` build.** When a page looks
      right in the browser but wrong in `public/`, or the reverse, check which one you are
      actually looking at before debugging templates.

    The CLI build in `scripts/build.sh` was correct throughout this: it failed loudly and
    accurately while the server was returning 500s. When the two disagree, trust the CLI.

11. **Verified in round 10 by test build: Hugo generates em dashes that no script on this
    site can see.** Goldmark's typographer extension is **on by default** and rewrites
    markdown punctuation in the *output*. Measured in a scratch Hugo 0.150.0 build:

    | Source markdown | Output HTML |
    |---|---|
    | `A -- dash` | `A &ndash; dash` (en dash) |
    | `B --- dash` | `B &mdash; dash` (**em dash**) |
    | `D` a literal em dash typed in the source | passes through unchanged |
    | `E "quote"` | `E &ldquo;quote&rdquo;` |

    **Why this matters more than it looks.** `check-dashes.py` reads source files only. So
    a page can pass the house rule perfectly and still render em dashes in every browser,
    and nothing in the current toolchain would say a word. The rule in §3 is about what
    the reader sees, so a build that emits em dashes breaks it while reporting a pass.

    **The fix, when `hugo.toml` is written:** disable the typographer.

    ```toml
    [markup.goldmark.extensions.typographer]
    disable = true
    ```

    With it off, `--` and `---` reach the output as plain ASCII and the only em dash that
    can appear is one actually typed in a source file, which is exactly the thing
    `check-dashes.py` already covers. It costs the site automatic curly quotes, which is
    a real loss for a prose site, and the trade is still correct: this project's whole
    argument is that its own claims should be checkable, and house punctuation that the
    house check cannot see is not checkable.

    **A second reason to scaffold Hugo sooner rather than later:** this was found by
    building the site, not by reading it. Expect more of the same. Anything asserted
    about the rendered output (page weight, request count, accessibility) is unverified
    until a build exists to measure it, which is what `/receipts/` used to publish and what
    `scripts/measure-pages.py` measures internally now.

13. **A fingerprinted asset leaves a stale twin behind, and it will lie to you about page
    weight.** Found in round 11, and it produced wrong numbers twice before it
    was caught. Editing `assets/css/main.css` gives the stylesheet a new filename, and the old
    fingerprint **stays in `public/` forever**, unreferenced but present. `--cleanDestinationDir`
    does not remove it: that flag cleans files not found in the static directories, and Hugo
    Pipes output is not a static file. The measurement was summing every file in `public/`
    rather than the files a page actually references, so every page was inflated by about
    1.5 KB of a stylesheet no browser would fetch. Two rules came out of it, and both are
    enforced:

    1. **`scripts/build.sh` deletes `public/` before building**, so the output directory is a
       pure function of the input. Do not do that while `hugo server` runs (gotcha 12).
    2. **Measure what the page fetches, not what the directory contains.** Parse each page's own
       `<link>` tags for the stylesheet and the icon, and sum those. It is the only definition
       that matches what a reader actually downloads, and it is immune to this whole class of
       error. `scripts/measure-pages.py` does exactly this; use it rather than a `du` of
       `public/`.

    The general lesson is the project's own: a number produced by a convenient method is not a
    measurement until the method has been checked against the definition it claims to serve.
    This is also the one gotcha here that the maintainer's CSS work block has to keep in mind,
    because a stylesheet edit is exactly what creates the stale twin.

14. **Every file under `/etc/ssh` on this machine is owned by `nobody:nobody`, so plain `ssh`
    and `git push` fail before they reach the network.** Found on 2026-10-14 while connecting
    the GitHub remote. The error is `Bad owner or permissions on
    /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`, which reads like a broken key or a
    network problem and is neither: `ssh` refuses to read a system config file it does not
    consider root-owned, and stops. The whole tree is affected, not one file
    (`ssh_config`, `moduli`, the `ssh_config.d` symlink and `sshd_config` all list as
    `nobody:nobody`), which points at how this environment was assembled rather than at
    anything in this project.

    **The workaround is repo-local and already applied.** `.git/config` carries
    `core.sshCommand = ssh -F /dev/null -i ~/.ssh/github_key -o IdentitiesOnly=yes`, so
    `-F /dev/null` skips system config entirely and git works with no environment variable.
    It is untracked and machine-specific, so it does not follow the repository anywhere.
    Remove it with `git config --unset core.sshCommand` once the ownership is fixed.

    **The real fix needs root and is the maintainer's**: `sudo chown -R root:root /etc/ssh`.
    Until then, any other `ssh` on this machine fails the same way, so **do not diagnose a
    connection failure here as a key, credential or network fault** before checking the
    ownership of `/etc/ssh`. Both `~/.ssh/github_key` and `~/.ssh/id_ed25519` authenticate as
    `osszevissza` at GitHub when the config problem is bypassed, which is how this was
    separated from a bad key.

15. **An error you can observe is not a cause you can name, and this project published the
    wrong cause once.** Before the first deploy, `https://third-party.statichost.page/` failed
    TLS with `tlsv1 alert internal error`, and a hostname that cannot exist failed the same
    way. The observation was sound and was published on the page that then carried these
    figures, with an explanation attached to it,
    that the two behaved alike "because neither has a certificate, since no site has been
    provisioned". **The certificate contradicts that**: the one now serving this site was
    issued at 18:34:14, before the probe was taken, so what was missing was the name answering
    rather than a certificate existing. Reading the certificate's own `notBefore` an hour later
    is what caught it.

    **The rule that follows:** record what a probe showed and leave the cause unknown, or name
    a cause only from evidence that can still be checked afterwards. This is gotcha 10 one
    level down. There a status code proves nothing about a URL; here a TLS error proved nothing
    about why. Both mistakes come from reading a symptom as a finding, which is the failure
    mode this whole project documents.

    **Two related traps from the same afternoon.** The domain's DNS is a wildcard, so the real
    name and an impossible name share both an `A` and an `AAAA` record and **resolution proves
    nothing**; the host's TLS layer is what discriminates. And the two record types point at
    different addresses, only one of which answered from this machine, which is why the page
    reports the IPv4 result and says nothing about IPv6 either way.

    **This gotcha immediately caught itself again.** The same afternoon, a first deploy landing
    minutes after a push was written up in §7 as "pushing appears to deploy". The next two
    pushes did not deploy at all, because deploys are in fact triggered by hand on the host's
    dashboard and always have been. Two coincidences, one afternoon, both recorded as causes,
    both wrong. When the temptation is to explain rather than to describe, describe.

---

## 8. Standing build constraints: the site must pass its own test

These are load-bearing. The project's central claim is credibility, and it dies the
moment the site itself is hypocritical.

- **Zero third-party requests.** No Google Fonts (system stack or self-hosted woff2),
  no CDN scripts, no embeds (click-to-load placeholders), inline SVG, no third-party
  comments.
- **Analytics:** GoatCounter or equivalent. No cookies, so **no consent banner at all**,
  which is itself the site's best demonstration. Say so on the home page.
- **Progressive enhancement is mandatory.** Every interactive's full content must be
  present and readable with JS disabled; JS adds motion and filtering only. This
  satisfies the architecture and the WCAG requirement simultaneously. See the
  single-source-of-truth pattern in `SITE_PLAN.md` §6b.
- **Accessibility:** WCAG 2.2 AA. Semantic HTML, keyboard-operable interactives,
  visible focus, 4.5:1 contrast, meaningful alt text, and `prefers-reduced-motion`
  respected, **critical**, since the flagship page is scroll-animated.
- **Performance budget:** < 100 KB/page, < 20 requests, LCP < 1.5 s. Both readings of the
  page-weight line pass as of 2026-10-15, measured by `scripts/measure-pages.py` (§7).
- **The site used to have to publish real measured numbers, and no longer does.** `/receipts/`
  existed to satisfy that requirement and was dropped on 2026-10-15 at the maintainer's request.
  **Nothing on the site now publishes its own figures**, and a future session should not treat
  that as a defect to repair quietly: re-adding a page of them is a decision the maintainer has
  already taken once. What remains of the requirement is the internal one, which is that any
  figure the site ever does publish must be measured rather than asserted, with its method
  named. `scripts/measure-pages.py` is how the weights and the model estimate are taken.
- **Response headers are part of passing the site's own test, and one is missing.** The host
  sends HSTS, `nosniff` and a revalidating cache policy, and it does not send a
  `content-security-policy`. A site whose central claim is "no third-party requests" should
  have a browser check that claim rather than a reader take it on trust, so the missing header
  is tracked as a defect here rather than waved away as a detail of somebody else's server.
  It used to be tracked on `/receipts/` as well. `robots.txt` also does not point at the
  sitemap.
- **Honesty about maintenance, and it belongs on the page, not only in this file.** The
  footer states on every page that the site was written in October 2026, that it is not
  maintained on a schedule, that there is no capacity to keep every page current, and that
  the claims dating fastest are the ones about law, enforcement and prices. This was asked
  for by the maintainer in round 11 and the reasoning is worth keeping: every page already
  renders a `status_as_of` date, but a date alone implies someone is watching it. Stating
  the opposite in the footer is cheaper than a site whose central claim is that its claims
  are checkable quietly going stale. **Do not quietly remove it.** This used to end by
  promising that `/the-rules/` would carry a stronger, page-level version of the same
  warning in its own header, since that page was the one rot would hit first. That page was
  dropped in round 11, so the footer carries the warning alone. If a page whose whole value
  depends on being current is ever added, it inherits that requirement (`SITE_PLAN.md` §4).

---

## 9. Suggested next steps

1. ~~**Write `/consent-theatre/`.**~~ **Done in round 10.** The EDPB cookie banner
   taskforce report was located and read, the CNIL URLs were diagnosed rather than
   retried, and the page is written. **Its interactive is also done**: "Eight clicks
   through one banner", eight documented defects as a static walkthrough, no JavaScript.
   See §5 for why the planned 47-click counter was abandoned and what replaced it. The
   four new worklist items it produced are in §6.
2. ~~**Finish the `/nothing-to-hide/` interactive.**~~ **Done in round 11.** `secondary
   use` and `dignity` are written out in a section headed "Two harms that needed arguing",
   the line admitting they had no section of their own is gone, and both list entries now
   point at an argument that exists. The other five one-liners already pointed at sections
   that argue them, so they were left alone. The page is 3,009 words and that was accepted
   (§0 item 3). See §5 for the one caveat to carry forward: the dignity passage is
   explicitly normative and leans on two sources still marked unverified.
3. **Clear the remaining archiving gaps**: 9 sources with no snapshot at all, out of 58
   entries, of which 48 are archived. Tedious, unglamorous, and the difference between a claim
   and a checked claim. **Do not start over**: read §6 item 1, which lists the 9 and explains
   the API's spurious-empty trap. Two things changed in round 11, and both make this easier
   than round 10 assumed:

   - **Save Page Now works over plain HTTP with no account**:
     `curl -sSL "https://web.archive.org/save/<url>"`, then fetch the returned snapshot and
     check its title. Four sources were archived that way in round 11, each on the first
     attempt, so this is not a browser-only job.
   - **Use the CDX API to find out whether a snapshot exists at all** (§7 gotcha 10). The
     availability API returned empty on eight consecutive passes for a URL that has a working
     snapshot, so a blank from it is not a negative.
   - **New on 2026-10-15, and it is the cheapest item on this list: the CNIL sources can be
     opened again.** The block lifted (§7 gotcha 10, §6 item 2), and four entries
     (`cnil-analytics-exemption`, `cnil-analytics-self-assessment`, `cnil-dark-patterns-quiz`,
     `cnil-google-san-2025-004`) carry `verified_on: null` only because they could not be read
     when they were recorded. Reading them is a real verification step, not a status code: the
     archived copies already read in rounds 10 and 11 are the fallback if the domain blocks
     again. That would move the warning count for the right reason, which the drop on the same
     day did not.
4. ~~**Fill the two `/sources/` TODOs** (contact route, tools disclosure).~~ **Both were
   actioned in round 11, and one sub-item is still open.**

   - **Contact route: done and published.** The tracker URL is in the page
     (`https://github.com/osszevissza/the-third-party/issues`), email is offered as the
     fallback by pointing at `barsimarina.hu` rather than printing the address, emailed
     reports are committed to being transcribed into the tracker, and there is deliberately
     no promised response time. **One check before publishing**: GitHub only allows
     anonymous issue filing on a public repository if that setting is enabled, so open the
     tracker logged out in a private window and confirm the form appears. That is the old
     warning, "do not publish a channel you will not read", applied to whether the channel
     accepts input.
   - **Tools disclosure: closed in round 11, and rewritten on 2026-10-15.** Both halves are
     published on `/sources/`: the build disclosure in "How this site is built and checked"
     (Hugo with no theme, Python for the four checks, `curl` and the Wayback Machine and
     `pdftotext` for verification, GitHub and statichost.eu, an AI agent named as the writer of
     the prose and the code, and Helix, Sublime Text and Neovim as the editors), and the
     narrower disclosure the page committed to, which used to be headed "Which of these swaps I
     have actually made" and is now "What I actually run". Five things are run (Ecosia for
     search, Posteo for email, uBlock Origin on Firefox, Signal, Mullvad for DNS and moving to
     Quad9), one is partial (a Codeberg account, with this project on GitHub anyway) and two are
     not changed (YouTube, and documents). **Nothing on `/sources/` is unsupported any more.**
5. ~~**Fix the two-line `edpb-consent-or-pay` entry** (§6 item 5).~~ **Done in round 11**,
   and it took more than two lines. See §6 item 5 for what was corrected along the way (the
   PDF path, the corrigendum of October 2024, and a date that had to rest on the page's
   title rather than on its status code). `solove-taxonomy` is the item that remains, and it
   is now the only one on this list an agent could finish without a human.
6. ~~**Then `/` (home), then `/the-rules/`, then `/receipts/`, then wire up hosting.**~~
   **All of it closed in round 11.** `/` and `/receipts/` were written, `/the-rules/` was
   dropped deliberately rather than left undone, and `/swap-shop/` and `/receipts/` were
   dropped on 2026-10-15: §5 has the reasoning and `SITE_PLAN.md` §4 keeps all three abandoned
   outlines. **The content target is met, at ten pages.** What follows
   from here is the work that is not writing: the source worklist in §6, the cheap source
   upgrades listed there, and hosting.
7. **~~Set up the GitHub repo and statichost.eu.~~ Done, and the site is live as of
   2026-10-14.** The repo is public, the local checkout is connected to it, and the
   maintainer's chosen domain was set as `baseURL` and deployed at 19:31:35 UTC. `origin` is
   `git@github.com:osszevissza/the-third-party.git` with `main` tracking it; `.gitignore`,
   `.tool-versions`, `LICENSE`, the build script and the domain are all in place. §7 holds
   the serving facts and the verification method. **What the deploy left open:**

   - **There is no `statichost.yml` in the repository.** The host's build configuration lives
     in its dashboard, so it is not version-controlled and cannot be reviewed from the source
     tree. If statichost.eu accepts one (image `hugomods/hugo:exts-0.150.0`,
     `command: hugo`, `public: public`), committing it would make the build reproducible from
     the repository alone.
   - **Whether the host runs the four checks is unknown, and the safe assumption is that it
     does not.** The deployed stylesheet fingerprint matches a local build exactly, so the
     host ran the same Hugo and the same asset pipeline, but nothing in the output says
     whether `scripts/build.sh` ran, and that image carries Hugo rather than Python and
     PyYAML. **Assume the checks ran locally and nowhere else**: a push that fails one and is
     not caught locally would deploy anyway.
   - **No `content-security-policy`, and `robots.txt` does not point at the sitemap.** Both
     are gaps tracked in §8, and both are one-line fixes on a host
     that already sends HSTS and `nosniff`. They used to be published on `/receipts/` as well.
   - See §7 gotcha 10 for the source-verification consequences of being public while 19
     sources still carry `verified_on: null`.

   **The domain is decided as of 2026-10-14: `https://third-party.statichost.page/`.** It is
   set as `baseURL` in `hugo.toml`, replacing the `https://example.invalid/` placeholder
   that round 11 deliberately left in place, and the maintainer chose it. That one edit
   rewrites every page's `<link rel=canonical>` and `sitemap.xml`, plus the RSS `alternate`
   link on the home page, and it costs 12 bytes per page and 24 on the home page. **The
   page weights were re-measured after it**, which is the pattern to expect for
   any later domain or hosting change: the heaviest-page rows moved by a few bytes while the
   median did not. **Do not read a resolving hostname as proof of a
   deploy.** Every `*.statichost.page` name resolves, including names that cannot exist
   (`this-cannot-exist-9f2a.statichost.page` answers identically), and all of them refuse TLS
   with the same alert until a site is provisioned, so the DNS record is a wildcard and
   proves nothing. Verify a deploy the way this project verifies sources: fetch the page and
   read its own title. **That is how this deploy was checked on 2026-10-14**: twelve pages
   fetched, twelve correct titles and canonicals, which is the only evidence that a name is
   serving this site rather than nothing.

8. **The styling pass. This is the next job, and the maintainer sets the direction.** On
   2026-10-14 they said they would describe what they want rather than approving a proposal,
   so **do not start designing unilaterally**: ask for the direction, or implement the one you
   are given. Everything else about the pass is known and written down here.

   **What already exists, so that nothing is rebuilt from scratch.** `assets/css/main.css` is
   279 lines and 7,263 bytes: a token layer in `:root` (`--bg`, `--surface`, `--ink`,
   `--ink-muted`, `--rule`, `--accent`, `--accent-ink`, `--measure`, two font stacks), a full
   dark scheme under `prefers-color-scheme`, visible focus everywhere, the skip link, the
   header and its generated nav, `main`/`.page`/`.page-header`, heading scale, paragraphs,
   `hr` dividers, lists, blockquote, inline `code`, images, tables, the citation marker, the
   source list and its records, the footer, and **a print stylesheet** that `SITE_PLAN.md` §6b
   asks for. It goes through Hugo Pipes (minify, fingerprint), so CSS edits need no build
   changes and no new tooling.

   **Two concrete defects the pass should close, and both were published on the dropped
   `/receipts/` page, which is why they are written out here instead:**

   - **`section.interactive` has no styling at all.** `layouts/shortcodes/interactive.html`
     emits `<section class="interactive" data-interactive>` and no rule anywhere matches it, so
     the eight-click walkthrough on `/consent-theatre/` and the harms block on
     `/nothing-to-hide/` render as bare stacked text. This is the largest visual hole on the
     site, and it is where a new visual idea would show first.
   - **Citation markers.** `.cite` is `font-size: 0.75em; line-height: 0`, which is the
     WCAG 2.5.8 target-size failure: the clickable area is a few pixels high. With CSS off they
     are bare numbers with no affordance. Both are style problems rather than markup ones, so
     both are fixable here, and fixing them retires two defects that used to be published.

   **Before touching colour, build the contrast check.** The dropped page published that the
   site's contrast is computed from the values in this file rather than trusted, with a lowest
   ratio of 6.66:1 and every pair passing 4.5:1 in both schemes. Nothing publishes that claim
   now, and it is worth keeping true anyway, because it was measured by hand and a colour edit
   can break AA with nothing to say so. **Write
   `scripts/check-contrast.py` first**, parse the `:root` tokens plus the dark block, compute
   WCAG 2.1 relative luminance for each pair the site actually renders (`--ink` on `--bg`,
   `--ink-muted` on `--bg`, `--accent` on `--bg`, `--ink` and `--ink-muted` on `--surface`,
   `--accent-ink` on `--accent`, and the focus ring colour against both backgrounds), fail
   below 4.5:1 for text and 3:1 for the ring, and wire it into `scripts/build.sh` as a fifth
   check. Then update the two places that state how many checks run: `/sources/` says "four
   scripts" in prose, and §2 and §8 of this file.

   **The constraints are not negotiable and are all in §8**: plain CSS (Hugo's bundled Sass is
   frozen libsass, §7 gotcha 3), no framework, no webfont, no CDN, zero third-party requests,
   WCAG 2.2 AA, `prefers-reduced-motion` honoured (which matters because
   `scroll-behavior: smooth` is already set for the flagship page), and the under-100 KB page
   budget. A page that loads a webfont to look better than the other pages has lost the
   argument the site is making.

   **The loop, and its one limitation.** There is no browser and no headless tooling that
   launches from this environment (§7), so **the agent cannot see the result**. Write CSS, then
   hand it to the maintainer to look at, and iterate on what they describe. `sh scripts/build.sh
   serve` gives them `http://localhost:1313` with live reload if they prefer a local build to
   the live site, but remember gotcha 12: restart the server after adding any template file,
   and never delete `public/` while it runs. Everything measurable is still checkable here:
   contrast, page weight, the static accessibility list, and zero third-party requests.

   **When it is done, re-measure, because the stylesheet is shared by every page.** Run
   `python3 scripts/measure-pages.py` (§2): the median moves as well as
   the heaviest page, since the CSS is in every page's weight. There is no page to patch any
   more, so the check is the budget itself: both readings must stay inside 100 KB. Then commit,
   push, and the maintainer deploys (§7, hand-triggered).

---

## 10. What "done" means for the current goal

Ten core pages of portfolio-quality, fully sourced Markdown, with every factual claim
grounded in a verified, dated citation. **All ten exist** as of 2026-10-15: `/`, `sources`,
`nothing-to-hide`, `consent-theatre`, `what-leaves-your-browser`, `one-page-load`,
`dark-patterns`, `myths`, `analytics`, `start-here`. `/the-rules/` was dropped by the
maintainer in round 11 and `/swap-shop/` and `/receipts/` on 2026-10-15, so the target moved
from thirteen pages to twelve to ten. All four
scripts pass with 0 errors and the build renders every page.

**Two conditions of the original definition of done are still open, and neither is writing
work.** The source worklist in §6 is not clear: 19 sources still carry `verified_on: null`,
several of them because no terminal can verify them at all. And 10 sources are not archived.
Both are tracked in §6, and both are honest limitations rather than oversights. **The count of
19 fell on 2026-10-15 for a reason that is not progress** (a deleted record, not a verified
one), while the CNIL entries in it became verifiable for the first time (§9 item 3). The third
condition that used to sit here, the unsupported disclosure sentence on `/sources/`, closed in
round 11 (§9 item 4).

**The written work is done, and the last piece of unwritten work is the styling** (§9 item 8).
The maintainer is choosing the direction for that themselves, so a session that picks this file
up should ask rather than design. Everything else that is left is maintenance of the kind §6
tracks: source records a human has to open, and the cheap upgrades listed there.

**Open questions carried forward, both small and both the maintainer's call:**

- **The carbon figures divide by 2^30 rather than by a decimal billion.** That is correct as GiB
  and wrong as GB, and the difference is about 7%. `scripts/measure-pages.py` prints both so the
  choice is one line wide, and **nothing on the site depends on it any more**, because the page
  that published the milligram figure was dropped on 2026-10-15. What was published as 1.3
  milligrams was 1.26 GiB-based and 1.35 decimal, which is where the question came from. The
  model's own documentation says "gigabytes per kilowatt-hour" without settling which, which is
  why it stays a question rather than a bug to fix quietly.
- **The long commit messages in the middle of the history.** The maintainer asked for short
  commits on 2026-10-14 and the rule is recorded in §7, but four commits from that session
  still carry paragraph-length bodies. Rewriting them means a force-push to a public
  repository, so it was left alone and offered instead. The offer stands.

**The repository is now a repository, and it is public.** Round 11 initialised git (`main`)
and added a `LICENSE` carrying the CC0 1.0 legal code verbatim, which is what makes the
footer's licence line true rather than aspirational. **The eight commits were pushed to
`origin` on 2026-10-14** (`git@github.com:osszevissza/the-third-party.git`), so the source is
public and the correction route printed on `/sources/` now has something behind it. **The
site itself is public too as of the same day**: it is live at
`https://third-party.statichost.page/`, verified by reading each page's own title, so the
project has moved from "finished" to "published" and the footer's honesty about maintenance
is now a promise made in public rather than a note in a file. The 2026-10-15 drop is pushed but
not deployed, so the live site is one version behind until the maintainer triggers it (§7).

**Not blocked, and no longer blocked on content.** Round 11 closed `/`, `/receipts/`, the two
unargued harms, the `edpb-consent-or-pay` record and both `/sources/` TODOs, removed the
site's last em dash after discovering that the title it was protecting was not the publisher's
wording, and dropped `/the-rules/` on the maintainer's instruction. 2026-10-15 dropped
`/swap-shop/` and `/receipts/` on the same instruction and rewrote every published sentence
that depended on them. **What remains needs a
human rather than an agent**: the blanked links that have to be opened by hand, the 9 possible
Wayback gaps, and the GitHub tracker setting that decides whether
anonymous issue filing works (see §9 item 4). The four CNIL links left this list on
2026-10-15, when the domain started answering again.
