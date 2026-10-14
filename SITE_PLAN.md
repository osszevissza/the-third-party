# The Ethical Web: Site Plan

**Working title options:** *The Third Party* (recommended) · *Consent Theatre* · *Follow the Packet* · *Nothing to Hide*

**Language:** English
**Scope:** the ethical web specifically, the browser, the page, the business model behind it. Not "ethical tech" in general.
**Format:** static site, 13 core pages, 2 interactive pieces, 0 third-party requests.

---

## 1. Editorial spine

Every page follows the same four-beat argument:

> **Problem → Pattern → Alternative → Receipt**

- **Problem:** here is what actually happens, concretely, with a number or a named script.
- **Pattern:** here is the design/business model that makes it happen, and who profits.
- **Alternative:** here is what a less extractive version looks like, and what it costs.
- **Receipt:** here is where I got this, dated, and here is this site's own number for the same metric.

Repeating the beats is what makes the site feel *designed* rather than a pile of articles, and it scales: when you run out of time, you can drop whole pages without breaking the structure.

**The organising principle:** organise around *problems*, never around *tools*. A tool page is only interesting in contrast to what the dominant option does to you. A "Top 10 private tools" list is the weakest possible version of this project. It teaches nothing, dates instantly, and reads as an advert.

---

## 2. Page template

Every content page uses this skeleton, in order. Non-negotiable, because consistency is what carries the "designed" impression.

| # | Block | Purpose | Rough length |
|---|-------|---------|--------------|
| 1 | **Hook** | One concrete, surprising, verifiable fact. No preamble. | 1–2 sentences |
| 2 | **What's happening** | The mechanics, plainly. Name specific scripts, companies, numbers. | 300–600 words |
| 3 | **Why it matters / who benefits** | The incentive structure. Follow the money. | 200–400 words |
| 4 | **The other side, stated fairly** | Steelman the practice before you critique it. | 100–250 words |
| 5 | **What you can do** | One primary action, then 2–3 escalation options. | 150–300 words |
| 6 | **Sources** | Dated, linked, with a "status as of" line for anything legal. | n/a |

**Voice rules** (this is the "edutainment" part, and it's a discipline not a vibe):

- Second person, present tense, short sentences.
- Concrete beats abstract every time. Not "trackers collect data" but "this page sent 47 requests before you scrolled; 31 went to nine companies you've never heard of."
- Humour as a scalpel, never a sneer. **Punch up at systems, never down at users.** The reader is not stupid; the design is hostile. That distinction is the whole difference between advocacy and smugness.
- No doom without an action. Every page ends with something to *do*, even if it's small.
- Steelman before you dismantle. A site that explains why small businesses use Google Analytics before explaining why they shouldn't is more persuasive than one that moralises.
- No vendor worship. Disclose your own choices honestly.

---

## 3. Information architecture

Tiered honestly, because 30 pages is not a course project; it's a way to finish nothing.

### CORE: build these (12 pages + 2 interactives)

```
/
├── start-here/                      orientation + reading paths + action ladder
├── one-page-load/                   ★ INTERACTIVE #1, flagship narrative
├── what-leaves-your-browser/        the data taxonomy
├── nothing-to-hide/                 the harms taxonomy
├── myths/                           myth-busting with self-verification
├── dark-patterns/                   ★ INTERACTIVE #2, the field guide
├── consent-theatre/                 cookie banners as a genre
├── the-rules/                       DROPPED in round 11. Law in plain language, see section 4
├── swap-shop/                       alternatives hub
├── analytics/                       "you don't need GA4" (site-owner angle)
├── receipts/                        this site's own measured numbers
└── sources/                         methodology + annotated bibliography
```

### SHOULD: build if the schedule holds

```
├── accessibility/                   the ethical issue nobody calls ethical
├── sustainability/                  the web has a weight
├── attention/                       infinite scroll and the engagement economy
├── open-source/                     the unpaid foundation (xz, Log4Shell)
├── ai-crawl/                        robots.txt and the new enclosure
├── browser-power/                   Manifest V3 and who controls your defences
├── subscriptions/                   roach motel, confirm-shaming, drip pricing
├── decision-guide/                  choose-your-path routing
├── glossary/
└── tracker/                         living enforcement & news tracker
```

### COULD: stretch, or fold into the above as sections

Net neutrality & zero-rating · encryption & certificate authority trust · DNS/domain centralisation · platform monoculture (browser engines) · content moderation labour · e-waste & the material supply chain · children's privacy (UK AADC, COPPA) · academic-research ethics of scraping.

**Explicit non-goals.** Write these on the About page and defend them:
- Not a tool directory.
- Not a threat-model guide for activists (that's a different project; link out to real ones).
- Not legal advice.
- Not comprehensive. It's an argument, illustrated.

---

## 4. Page-by-page outline

### `/` Home
**Argument:** The web you use is not the web you think you're using, and the difference is measurable.
**Blocks:** one-sentence thesis · three audience doors (*I just use the web* / *I run a website* / *I'm here for the research*) · teaser for the flagship interactive · the action ladder preview · a small badge linking to `/receipts/` · a one-line callout: *"This site has no cookie banner because it has no cookies or trackers. That should not be remarkable."*
**Avoid:** a hero carousel, a newsletter signup, a "trusted by" strip. Every one of those is a dark pattern in miniature and would be self-refuting.

### `/start-here/`
**Argument:** You don't have to care about all of this. Here's the shortest path to caring about the part that affects you.
**Blocks:** how to read the site (10 min / 1 hour / one afternoon) · the **action ladder:** 13 actions, escalating commitment, one per page: install uBlock Origin → switch default search → try a privacy front-end → audit your own browser with Cover Your Tracks → read one privacy policy → disable a tracker in your CMS → move one service → self-host analytics → move email → … · a "start with this one" recommendation · what this site won't ask you to do (no purity test, no "delete all your accounts").
**Tone note:** the action ladder is the single most important anti-doom device on the site. It converts a lecture into a curriculum.

### `/one-page-load/` ★ INTERACTIVE #1: flagship
**Argument:** Nothing you did was unusual. Everything you did was recorded.
**Format:** scroll-driven narrative. One simulated pageview of a fictional local news site. A side panel accumulates requests as you scroll: your IP and user agent, the referrer, a first-party cookie ID, then third-party beacons, a fingerprint hash, a session-replay snippet, and finally a real-time-bid request carrying inferred interests.
**Climax:** a summary card ("here is what one page load told fourteen companies about you") with a note on what was *inferred* rather than observed.
**Resolution:** the same page load on a static, tracker-free site: 0 third-party requests. Show the honest difference in what you lose (nothing you'd notice).
**Build:** a self-contained vanilla JS module in `assets/js/`, bundled through Hugo's built-in esbuild (`js.Build`). **No data leaves the browser.** Say that explicitly on the page; it's an ethical obligation and also good copy. 2–3 days of work. This is the piece that carries the project.
**Sources:** ICC *The Biggest Data Breach* · Web Almanac third-parties chapter · academic RTB research · EFF Cover Your Tracks.

### `/what-leaves-your-browser/`
**Argument:** The dangerous data isn't what you gave away. It's what was inferred from it.
**Blocks:** three columns: (a) what you hand over knowingly, (b) what's collected quietly, (c) what's **inferred** · why inference is the real problem: you can't delete a deduction, and inferences about health, sexuality, finances and pregnancy are exactly what gets bought · fingerprinting entropy explained without maths (why "clearing cookies" fails) · server-side tracking and why your ad blocker sometimes doesn't see it.
**Sources:** Cover Your Tracks · AmIUnique · Web Almanac privacy chapter · re-identification research · data-broker reporting.

### `/nothing-to-hide/`
**Argument:** Privacy isn't about secrets. It's about power.
**Blocks:** the objection stated fairly and at length. Do not strawman it · then a taxonomy of harms that survive "I'm innocent": **aggregation** (harmless facts combine into something else) · **secondary use** · **exclusion and discrimination** · **chilling effects** (measurable, documented) · **dignity** · **insecurity** (the breach you didn't choose) · **power asymmetry** (they know everything about you; you know nothing about them) · a short interactive: "which of these six outcomes would bother you?" The reader picks, the page responds with why each one is structurally likely.
**Sources:** Solove's privacy taxonomy · chilling-effect studies · breach reporting.
**Why this page is load-bearing:** it's the one sceptical readers, non-technical readers, and possibly your grader will land on. It has to be the most fair-minded page on the site.

### `/myths/`
**Argument:** Most of what you were told about staying safe on the web is a comforting half-truth.
**Format:** repeating unit: *what people think* / *what's actually true* / *how to check it yourself in 60 seconds*.
**Myths:** HTTPS means private · Incognito means anonymous · "we anonymise your data" · "we don't sell your data" (they share it, inside a bid request, in real time) · "accept all or pay" is a real choice · cookies are the whole problem (fingerprinting and server-side tracking say otherwise) · "we take your privacy seriously."
**Interactive:** a before/after: one real page counted with and without uBlock Origin, with the request counts on screen.
**Sources:** ICO/CNIL guidance · CJEU rulings · re-identification studies · the specific privacy policies you quote (archive them).

### `/dark-patterns/` ★ INTERACTIVE #2: the centrepiece
**Argument:** You are not being manipulated by accident. This is a design discipline with a budget line.
**Format:** a filterable card grid of 12–15 patterns. Each card: **name** · one-line definition · a **live mini-demo** · where you'll meet it · the legal hook (which regulator has already acted on this one).
**The 12–15, grouped by category:**
- *Sneaking:* sneak into basket · hidden costs · drip pricing · disguised ads
- *Urgency:* fake countdown · "3 people are viewing this" · low-stock lies
- *Obstruction:* roach motel (easy in, impossible out) · hard-to-cancel · privacy zuckering
- *Forced action:* forced enrolment · "accept all" as the only real path · account wall on cancellation
- *Social proof & shame:* confirm-shaming · activity notifications
- *Interface interference:* pre-ticked boxes (explicitly unlawful in the EU since *Planet49*) · misdirection · aesthetic manipulation
**Then:** the honest caveat section, why "dark patterns" is contested terminology, and how the field split between *dark patterns*, *deceptive design*, and *sludge*.
**Build tip:** do **not** screenshot real companies' funnels. Build your own mock "evil shop" and implement the patterns yourself. It is legally cleaner, ethically cleaner, easier to control, and more impressive as coursework.
**Sources:** deceptive.design taxonomy · Mathur et al. 2019 (≈11k sites, ~1,800 patterns, 15 types) · DSA/DMA enforcement actions · FTC actions · *Planet49*.

### `/consent-theatre/`
**Argument:** The cookie banner doesn't protect you from tracking. It manufactures your consent to it.
**Blocks:** why banners exist at all (ePrivacy + the GDPR consent standard: freely given, specific, informed, unambiguous) · why they're broken by design. The site owner wants a "yes," the vendor wants a "yes," and the reader wants the page · the structural conflict inside the ad-tech consent framework · **the pay-or-consent debate** and what regulators said about it · browser-level signals as the actual fix (Global Privacy Control, Consent-O-Matic) · a taxonomy of banner dark patterns with demos.
**Interactive (cheap, high-impact):** a simulated site where the honest opt-out takes 47 clicks, with a visible click counter. Genuinely funny, genuinely true, extremely shareable.
**Sources:** EDPB cookie-banner taskforce reports · CNIL decisions and fines · *Planet49* · CJEU ruling on the ad-tech consent framework · EDPB opinion on consent-or-pay.
**⚠ Verify current status** of every enforcement item before publishing; several are in flux.

### `/the-rules/`: DROPPED in round 11

**Not written, and the decision is deliberate.** The outline below is kept as a record of what was
planned and why it was abandoned, so that nobody re-adds it out of tidiness.

**Argument:** You have rights on paper. Here's what they're actually worth.
**Why it was dropped:** this is the one page whose entire value is being current, on a site whose
footer now states plainly that it is not maintained on a schedule. Its claims would be the most
damaging to get wrong, because a stale sentence about what the law requires invites reliance on a
page that already says it is not legal advice. Its primary sources turned out to be the least
readable on the whole site: `eur-lex.europa.eu` answers **202 with 0 bytes for every path,
including its own domain root**, so nothing on it can be verified or even read from a terminal,
and California's official code site returns 403 to everything. The argument it was meant to make is
already made, with dated and verified sources, on `/consent-theatre/` (the EDPB taskforce report,
the CJEU ruling on the TCF, the Conseil d'État upholding the Yahoo fine), in `/nothing-to-hide/`
section 3 (the FTC location actions, and legality as a floor) and in `/analytics/`.
**Format, for the record:** one card per instrument: **what it's for / what it actually requires / what it doesn't cover / who enforces it / status as of [date]**.
**Instruments:** GDPR · ePrivacy Directive · Digital Services Act · Digital Markets Act · European Accessibility Act · FTC Act and US state privacy laws · sectoral rules where relevant.
**Rulings that changed things:** Schrems I and II · *Planet49* · the ad-tech consent framework ruling · the analytics-and-transfers decisions.
**Closing section:** enforcement reality: fines issued vs. fines collected vs. revenue; who actually gets caught and who doesn't; why "there's a law" is not a defence strategy.
**If it is ever revived**, read AGENT.md section 7 gotcha 10 first: it records which of these sources can actually be read, and the one route that works (the Wayback CDX API, filtered to status code 200, for archived copies from before EUR-Lex broke).

### `/swap-shop/`
**Argument:** Switching is possible, and it costs something specific. Here's the price.
**Format:** one row per swap, in a table that works on mobile.

> what you probably use → what it does to you → the alternative → what switching costs → what you give up

**Categories:** email · VPN · search · browser · analytics · documents & files · code hosting · video · chat · DNS.
**The "what you give up" column is mandatory.** Without it the page is an advert. Examples of the honest costs: custom-domain and integration support, feature depth, deliverable-to-spam reputation for smaller providers, no free tier, self-hosting maintenance, ecosystem lock-in, and the friction of being the only person you know who uses it.
**The "what it does to you" column is where the argument lives.** Be specific and sourced, or cut the row.

### `/analytics/`
**Argument:** You do not need Google Analytics. You need about four numbers.
**Why this page matters more than it looks:** it is the page a small-business owner, a student journalist, or a course mate who runs a blog will actually act on. It turns the project from complaint into transferable advice, and it is the strongest possible answer to "but what's the alternative?"
**Blocks:** what GA4 actually gives you vs. the four or five reports you actually open · what GoatCounter, Plausible, Matomo and Umami each do and don't do · the cookieless question, and the honest caveat that "no cookies" and "no consent needed" are not the same thing in every jurisdiction · **server logs as the baseline nobody mentions** · migration cost and effort · the integration you'll lose.
**⚠ Verify** the jurisdictional consent claims and any current regulator exemption guidance before publishing.
**Sources:** each project's own docs · the analytics-transfer decisions · CNIL guidance on consent exemptions.

### `/receipts/`
**Argument:** I can prove this site does what it says. Can the sites you use?
**Blocks: all real, measured, dated:**
- total requests on a page load, split first-party / third-party (target: 0 third-party)
- page weight, and how it compares to the median page
- carbon estimate, with the methodology named
- Lighthouse scores, plus axe/WAVE accessibility results and the actual known failures
- fonts, embeds, CDN status, and what was replaced and why
- the analytics dashboard itself: GoatCounter, no cookies, no personal data
- **the reframe:** "Every site could publish this page. Almost none do. That's not a technical limitation."

**Why this page is the project's secret weapon:** it is self-reflexive, it is verifiable, no listicle can copy it, and it earns credibility for everything else you claim. It also converts directly into marks if your rubric mentions evidence, critical reflection, or technical implementation.

### `/sources/`
**Argument:** You should be able to check everything on this site, and tell me when I'm wrong.
**Blocks:** how sources were chosen and dated · a claim-by-claim table (claim / source / date / status) · **conflict-of-interest statement:** which recommended tools I use, whether I've been paid or given anything by any of them (the answer will be no, and saying so explicitly is worth points) · how to report an error and what happens when you do · annotated bibliography grouped by topic, with one line on why each source is trustworthy and what it's weakest at.
**This page is worth more marks than any content page.** Rubrics in web design and media courses nearly always reward sourcing and critical apparatus, and almost nobody builds this page.

---

## 5. Interactive pieces

| Piece | Page | Effort | Why it earns its place |
|-------|------|--------|------------------------|
| **One Page Load** | `/one-page-load/` | 2–3 days | Teaches the entire system in one scroll. The flagship. |
| **Dark Pattern Field Guide** | `/dark-patterns/` | 2 days | Visual, funny, interactive, immediately demonstrable. |
| **Cookie Banner Hell** | `/consent-theatre/` | 4 hours | The 47-click joke. Cheapest laugh on the site. |
| **Before/After Tracker Count** | `/myths/` | 3 hours | Makes an abstract claim self-verifiable in 60 seconds. |
| **Optional: "what are you worth?"** | `/what-leaves-your-browser/` | 1 day | Data-broker valuation calculator. Strong hook, but only build it if the numbers can be sourced. Do not invent them. |

**Technical ground rule for all interactives:** everything runs client-side, no data leaves the browser, and each page says so. For a site about surveillance, an interactive that phones home would be fatal, and a sharp grader will check.

**Progressive enhancement is mandatory, not aspirational.** Hugo renders static HTML first, so lean on that: the full content of every interactive must be present and readable with JavaScript disabled, and JS should only add motion and filtering. Concretely, `/one-page-load/` renders the complete sequence of requests as a plain ordered list and the scroll animation enhances it; `/dark-patterns/` renders all 15 cards and the filter enhances them. That is what keeps the flagship piece working when a grader opens it with scripting off, on a slow connection, or with `prefers-reduced-motion` set, and it is the same discipline the accessibility audit will demand anyway.

---

## 6. Build constraints (the site must pass its own test)

These are not nice-to-haves. The project's central claim is credibility, and it dies the moment the site itself is hypocritical.

**Stack: Hugo, chosen deliberately**
- Static site generator: **Hugo extended.** You have v0.150.0+extended installed, which is current. Write **plain CSS, not SCSS**: the extended edition's Sass support is libsass 3.6.6, which is deprecated upstream and frozen at an old CSS level, so it cannot parse native nesting, `@container`, or modern colour functions. A 13-page design system does not need a preprocessor. (You still want the extended build, for its image and WebP processing.) Pin the version in the README. Hugo's template lookup rules shift between minor releases and unpinned builds break quietly.
- **No theme.** Nearly every popular Hugo theme ships Google Fonts, Font Awesome, jQuery, or a CDN. Writing your own `layouts/` for 13 pages is less work than stripping a theme, and it is the only way to hold the zero-third-party rule.
- Content in Markdown, one file per page. Everything repeating lives in `data/`: see §6b.
- Assets through Hugo Pipes only: `resources.Get` → `minify` → `fingerprint` for CSS and JS. Nothing loads from another origin.
- **No `node_modules`.** Hugo is a single binary whose JS pipeline is built-in esbuild, so the project has no npm dependency tree at all.
- Hosting: Codeberg Pages / GitHub Pages / Netlify. Note in `/receipts/` who hosts it and what logging they do.
- Public repository with a license. Being inspectable is part of the argument.

**Why this is a good fit, not merely an acceptable one.** This project has two unusual properties: it is almost entirely prose, and it is full of small repeating records (patterns, swaps, myths, laws, sources). Hugo is strong at both, and its data-file model suits the structured pages better than a component framework would. There is a thematic argument too: a site about supply-chain ethics that ships 1,200 transitive npm packages is making an unintentional joke. Hugo's dependency surface is one binary.

**The one honest cost:** no component model, so the two interactives are hand-written JavaScript rather than isolated components. For one scroll narrative and one filter, that is roughly 200–300 lines each. Acceptable, and it keeps the JS payload small, which is on-message.

**Zero third-party requests.** No Google Fonts (system font stack, or self-hosted woff2 with `font-display: swap`) · no CDN-injected scripts · no embedded YouTube or Twitter/X (use click-to-load placeholders or self-hosted video) · no icon CDNs (inline SVG) · no third-party comment system.

**Analytics:** GoatCounter, hosted on their EU instance or self-hosted. No cookies, so **no consent banner is needed at all**: which is itself a quiet, powerful demonstration. Point this out on the home page.

**Accessibility: WCAG 2.2 AA, and treat it as content, not decoration:** semantic HTML and correct heading order · keyboard-operable everything, especially the interactives · visible focus indicators · 4.5:1 contrast minimum · alt text that carries meaning · `prefers-reduced-motion` respected (critical: the flagship interactive is scroll-animated) · no colour-only information · test with axe DevTools plus one manual keyboard pass.

**Performance budget:** < 100 KB per page · < 20 requests · LCP < 1.5 s. A site arguing "the web has a weight" cannot itself be heavy.

**Also:** working dark mode · a print stylesheet (graders do print things) · RSS for the enforcement tracker · no client-side routing.

---

## 6b. Hugo project structure

```
.
├── hugo.toml
├── content/
│   ├── _index.md
│   ├── start-here/index.md
│   ├── one-page-load/index.md
│   ├── dark-patterns/index.md
│   └── …                      one folder per page, so URLs stay clean
├── data/                      ← the content model for everything repeating
│   ├── sources.yaml           every citation, keyed by id
│   ├── patterns.yaml          the dark-pattern library
│   ├── swaps.yaml             the swap-shop rows
│   ├── myths.yaml
│   ├── laws.yaml
│   └── actions.yaml           the action ladder
├── layouts/
│   ├── baseof.html
│   ├── index.html
│   ├── _default/single.html
│   └── partials/
│       ├── head.html  nav.html  footer.html
│       ├── source-list.html   renders a page's citations
│       ├── status-as-of.html
│       ├── pattern-card.html
│       └── swap-row.html
├── shortcodes/
│   ├── cite.html              {{< cite "planet49" >}} → numbered link
│   ├── demo.html              a live dark-pattern demo
│   ├── verify.html            the ⚠ verify badge
│   └── reveal.html            the hook callout
├── assets/
│   ├── css/main.css
│   ├── js/{one-page-load,pattern-filter,banner-hell}.js
│   └── fonts/
└── static/favicon.svg
```

### Data files, not duplicated markup

Every page with repeating units should render from `data/`, never from hand-written HTML. `/dark-patterns/` is 15 cards, `/swap-shop/` is 10 categories, `/myths/` is 7 units, `/the-rules/` is 8 instruments: all lists of records with identical fields. One partial renders the card; one page template loops the data.

```yaml
# data/patterns.yaml
- id: pre-ticked
  name: Pre-ticked box
  category: forced-action
  definition: The opt-in is already on; you have to notice it to undo it.
  where: Newsletter signups, insurance add-ons, donation pages.
  legal: Unlawful in the EU since Planet49 (CJEU, 2019); consent must be an active act.
  source: planet49
```

### The single-source-of-truth trick for interactive filters

Render the list server-side **and** emit the same data as JSON for the client-side filter:

```go-html-template
{{ $patterns := site.Data.patterns }}
{{ range $patterns }}{{ partial "pattern-card.html" . }}{{ end }}

<script type="application/json" id="patterns-data">
  {{ $patterns | jsonify }}
</script>
```

No duplication, and the page still works with JavaScript disabled, because every card is in the HTML and the filter is pure enhancement. That one technique satisfies the architecture and the WCAG requirement at the same time.

### Automate the `/sources/` page

The highest-leverage Hugo-specific idea here, because `/sources/` is the most tedious page in the plan and the one worth the most marks. Put every citation in `data/sources.yaml` with an id, and have pages declare which ones they use in frontmatter:

```toml
+++
title = "Consent Theatre"
status_as_of = 2026-02-01
sources = ["edpb-banners", "planet49", "cnil-cookies"]
+++
```

A shortcode renders inline numbered references from the same ids, and `/sources/` is **generated**: full bibliography plus a reverse index of which pages cite what. Nothing to maintain by hand, and the claim-by-claim table becomes nearly free. It also makes an unsourced page glaringly obvious, which is exactly the pressure you want on yourself.

### Config to set on day one

- `disableKinds = ["taxonomy", "term"]` unless you actually use them, otherwise Hugo emits empty pages.
- `[markup.goldmark.renderer] unsafe = true` if you inline SVG or HTML in Markdown. Safe here (single author, no user-submitted content), but leave a comment in the config saying why.
- `enableRobotsTXT = true`, and disclose the sitemap on `/receipts/`.
- Pin the Hugo version in the README. `hugo mod` needs Go installed and you do not have it, so record the version in a `.tool-versions` file or a README note instead, or pin it in your CI workflow, which matters if a CI runner or your grader builds the site.
- Production build: `hugo --minify --gc`.

---

## 7. Source conventions

Adopt these on day one; retrofitting citations is miserable.

- Every factual claim gets an inline link with the source's own date visible.
- Anything legal or policy gets a **"status as of [date]"** line, and a `status_as_of` frontmatter field that renders in the page header.
- Archive every page you cite (Wayback Machine) and link the archive alongside the live URL. Privacy policies and pricing pages change quietly. This is exactly the kind of thing this site is about.
- Mark uncertain claims rather than rounding them off. "I could not verify X" is a strength on a site like this.
- Prefer primary sources: the ruling, the study, the regulator's decision, the project's own documentation. News coverage only when it's the only record of something.
- When you quote a privacy policy, quote it verbatim and link the archived version.

### Enforcement tooling

Two scripts, both runnable at any time. Neither edits anything: deciding whether a
source still supports the claim it's attached to is an editorial judgement, not
something a status code can settle.

**`python3 scripts/check-content.py`**, validates every YAML file in `data/`, every
page's TOML frontmatter, and the citation graph. It cross-checks declared sources
against inline `{{< cite >}}` calls, which catches the most common failure mode in a
data-driven site: a source declared but never used, or cited but not declared. It
bails out early if `data/` won't parse, rather than emitting one cascading
"unknown source id" error per citation. Exit 1 on error.

**`python3 scripts/check-links.py`**, resolves every URL in `data/sources.yaml` over
the network and classifies it: resolving, bot-blocked, dead, or inconclusive. Two
things it knows that a naive checker gets wrong:

- Several domains in this field (`ftc.gov`, `nytimes.com`, `acm.org`, `reuters.com`,
  `lexology.com`, `loc.gov`) answer automated requests with **403 or even 404** while
  working perfectly in a browser. A checker that trusts the status code will report
  live sources as dead. This one probes the domain root too, and reclassifies a 404
  as bot-blocking when the root also refuses.
- A "blocked" verdict still requires a human. The status code proves the URL resolves;
  only reading the page proves the content matches the claim.

### The archiving obligation

`archive:` is null on every source in the file right now, and that is a genuine gap
rather than an oversight to ignore. Press releases get restructured, pricing pages
change, and privacy policies are edited quietly, which is the exact behaviour this
site documents. Snapshot each source to the Wayback Machine and fill the field in
before publishing. A site arguing that claims should be checkable has to survive its
own sources being taken down.

---

## 8. Build order (8 weeks, adaptable)

| Week | Deliverable |
|------|-------------|
| 1 | Hugo scaffold, design system, `data/sources.yaml` begun early, `/` and `/start-here/`, repo and deploy pipeline live |
| 2 | `/one-page-load/`: the flagship interactive |
| 3 | `/what-leaves-your-browser/`, `/nothing-to-hide/`, `/myths/` |
| 4 | `/dark-patterns/` field guide and mock "evil shop" |
| 5 | `/consent-theatre/`, `/the-rules/` |
| 6 | `/swap-shop/`, `/analytics/` |
| 7 | `/receipts/`, `/sources/`, plus 2–3 SHOULD pages if the schedule holds |
| 8 | Accessibility audit, performance budget, content edit pass, **freeze the receipts numbers** |

**Sequencing logic:** the two interactives land early, while you still have energy for them, and the meta pages land last because they describe a finished site. If you slip, cut SHOULD pages, never the receipt or sources pages, which is where the marks are.

---

## 9. Open questions to settle before writing

1. **Course constraints:** is there a required page count, a required CMS, or a presentation component? Any of these could reshape the IA.
2. **Assessment stance:** is advocacy acceptable, or does the rubric require neutrality? If neutrality is required, shift the framing from "here's what's wrong" to "here are the trade-offs, here is the evidence, you decide". The four-beat spine survives that change intact.
3. **Timeline:** how many weeks, and how many hours per week?
4. **Hosting and domain:** do you have them, and do you want the domain's DNS provider discussed openly on `/receipts/`?
5. **Analytics:** will you actually run GoatCounter, or only document it? Actually running it makes `/receipts/` far stronger.
6. **Working title:** *The Third Party* is the strongest of the options; it carries both meanings at once (third-party scripts, and the uninvited third party in the room).

---

## 10. Why there is more than enough material

Rough count of the core pages against the source base: ~13 pages, each needing 4–8 sources, against a field with academic literature (Mathur et al., Solove, Zuboff, Doctorow), primary legal texts and rulings from three jurisdictions, annual quantitative datasets (Web Almanac, WebAIM Million, ICC's RTB report), regulator decisions, and a dozen open-source projects with public documentation. That is comfortably 60–100 citable sources without stretching.

**The risk was never scarcity. It is scope, and rot.** Bound the scope with the core/SHOULD/COULD split, and fight rot with dated claims, archived sources, and one living enforcement tracker page.
