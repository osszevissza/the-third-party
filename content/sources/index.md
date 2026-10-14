+++
title = "Sources"
subtitle = "Everything on this site is checkable, including the parts that are not checked yet"
description = "How the sources behind this site were chosen, what verification does and does not mean, the ones that could not be confirmed, and how to tell me I am wrong."
status_as_of = 2026-10-14
weight = 12
nav = "Sources"
sources = [
  "ecosia-eusp-index",
  "mullvad-public-dns",
  "mullvad-dns-shutdown"
]
+++

A site that tells you to check things had better be checkable itself. So this page is the
whole apparatus: every source this site rests on, what each one is used for, what each
one is bad at, and the ones I could not confirm.

There is no short version. A bibliography that lists titles and nothing else is a
decoration.

## How a source gets in

1. **Every factual claim gets a dated, linked source.** If a claim cannot be sourced, it
   is not stated. That rule has already cost this site two sentences, both deliberately:
   a widely repeated fingerprintability percentage was left out rather than guessed, and
   the Web Almanac's numbers are pointed at rather than quoted, because today's figures
   will not be next year's.
2. **Primary sources first**: the ruling, the study, the regulator's decision, the
   project's own documentation. News coverage only when it is the only record of
   something, and the entry says so when it is.
3. **Two kinds of link, kept apart.** A citation is a claim and is recorded below. A
   plain link ("here is the project's website") is a pointer, and is not. Blurring the
   two is how a bibliography turns into a link dump.
4. **Every source records what it is bad at.** That is the difference between a
   bibliography and a decoration, and it is the field I would defend hardest. A source
   with no weakness is a source I have not read carefully.
5. **Anything legal or policy carries a date**, on the page and in the entry, because
   enforcement positions move and a legal claim without a date is a claim about the past
   pretending to be about now.

## What "verified" means, and what it does not

**Verified means one thing:** on the date recorded, a person opened the link and
confirmed that the page exists and carries the claim attached to it.

It does not mean the source is right. A regulator can be wrong, a study can be
replicated and fail, and a company's documentation can describe a feature it has since
removed. Verification is a statement about the link, not a guarantee about the truth.

**Automatic checking cannot do this job, and this site does not pretend otherwise.**
Some domains answer any request, including requests for pages that cannot possibly
exist, with the same 401 or 403 or 404: Reuters, the FTC, the New York Times, the ACM
library and several others. A script that trusted the status code would call live
sources dead and blocked ones fine. The checker therefore requests a deliberately bogus
path on the same domain first, and marks the source **unverifiable** when the domain
refuses everything. Unverifiable is not a pass. It means the code proved nothing and a
person has to look.

Where a domain cannot be probed at all, the entry says so, and where an archived copy
exists it is linked and named as the copy that was actually read.

## The gaps, stated as gaps

**Most of these sources are not archived yet.** This site argues that a claim should
survive its source being taken down, and a site whose own sources are unarchived is
making a claim rather than a demonstration. The count is in the table below, and it is
the largest honest gap in this project. Snapshots are being filled in as sources are
verified, which is why the newest entries have them and the older ones do not.

**Some documents carry no date of their own.** Where a project page, a browser
documentation page or a vendor's pricing page is undated, the entry says "no date on the
document" rather than inventing one.

**Two sources have no stable URL at all.** Solove's 2006 taxonomy and the European Data
Protection Board's opinion on consent-or-pay are both cited correctly and both flagged
rather than guessed at: only secondary mirrors were found, and a mirror is not a source.
Those claims are marked as not publishable until the primary documents are located.

**Legal claims rot fastest.** Where a page rests on an enforcement decision, the page
carries a status date in its header, and the entry carries the date of the document. If
you are reading this a year from now, assume the legal position has moved.

## How to tell me I am wrong

The fastest route is the issue tracker on the repository: **<https://github.com/osszevissza/the-third-party/issues>**. It is public, so a correction lands where everyone can see it rather than only in my inbox, and it stays there after I have read it.

If you would rather not use GitHub, email works too. The address is on [my site](https://barsimarina.hu/) rather than printed here, which keeps it away from the address harvesters. I transcribe emailed corrections into the tracker, for the same reason a correction belongs in public: a fix only I can see is worth less than one anybody can check.

I read everything, and I fix things when I can. I am not promising a response time, because I would rather not promise one I cannot keep.

<!-- The contact route is settled and published. The GitHub tracker above is the primary
     route, email via barsimarina.hu is the fallback, and there is deliberately no promised
     response time. One thing to check before the site goes live: GitHub only allows
     anonymous issue filing on a public repository if that is enabled in its settings, so
     open the tracker in a private window while logged out and confirm the form appears.
     Do not publish a channel you cannot receive. -->

Report any of these, and I will treat it as a defect rather than a difference of opinion:

- a link that no longer resolves, or resolves to something other than what the entry says
- a number that does not match the source it is attached to
- a claim with no source attached
- a source that says something other than what the page says it says
- an argument the site is missing, or a counter-argument it handles badly

What happens next: the claim gets checked against the source. If it is wrong, the page is
corrected, and the correction is dated in the page's `status_as_of` field rather than
applied silently. What will not happen is a source being quietly swapped for a different
one that happens to support the same sentence. If a source stops supporting a claim, the
claim changes.

## Conflict of interest

Nobody has paid for a mention on this site, there are no affiliate links, there is no
sponsorship, and nothing recommended here has been given to me. The site carries no
advertising, sells nothing, and has no newsletter to grow.

Two things worth admitting anyway. I have preferences, and they show: the alternatives
pages reflect what I think is worth the trouble, not a neutral survey. And where I
recommend something I use myself, I have said so, with the honest cost of switching on
the same page. A recommendation without its cost is an advert.

**Which of these swaps I have actually made.** That sentence commits me to naming them, so here they are, including the ones I have not made and the one I have made badly.

- **Search: Ecosia.** Not one of the three engines that page recommends, and the difference is worth explaining rather than glossing. Ecosia has been building its own index with Qwant, and says that results for its users in France now come from it directly {{< cite "ecosia-eusp-index" >}}, which is the criterion the search section tells you to apply. I have not compared it against the three engines it does recommend, so the recommendation there is unchanged and this is not an endorsement of mine.
- **Email: Posteo.** The option this site calls the purist's choice, and the one I run.
- **Ad blocking: uBlock Origin**, on Firefox, which is the only browser where the page says the unrestricted version still runs. That pairing is the swap rather than a detail of it.
- **Chat: Signal**, with the caveat that page carries. The caveat is about who your contacts are, not about the tool.
- **DNS: Mullvad, and changing to Quad9.** A different company holds the lookups than held them before, which is the whole of what that swap does and all the page claims for it. That company is about to change again: Mullvad is shutting its public encrypted DNS servers down on 2 November 2026 and sponsoring Quad9 rather than running a resolver itself {{< cite "mullvad-public-dns" >}} {{< cite "mullvad-dns-shutdown" >}}, and this line is switching with it. The resolver built into the Mullvad VPN is a separate service and that shutdown does not touch it.
- **Code hosting: not properly.** I have a Codeberg account, and this project lives on GitHub, because that is where its readers and its corrections are. The recommendation stands and my practice is partial.
- **Video: not made.** I watch YouTube. PeerTube is recommended here and not adopted, for the reason that page gives: my attention is the thing that would have to move, and it has not.
- **Documents: not made.** The swap is on the list and I have not done it.

Listing the ones I have not done costs me something, which is the point. A disclosure that named only the swaps I had finished would be an advert with extra steps.

## How this site is built and checked

The site's own choices are part of what a reader is entitled to know, so here they are.

**Made by hand with a static site generator.** Hugo 0.150.0 extended renders it, with no theme: every layout and shortcode in `layouts/` is written for this site. A theme was avoided deliberately, because nearly every popular one pulls in a font service, an icon library or a CDN, which would break the first rule this site sets itself. It is built on Fedora Linux 44. The stylesheet is a single plain CSS file rather than Sass, because Hugo's bundled Sass is frozen at an old CSS level and a preprocessor would buy nothing here.

**Checked by four scripts before every build.** Python 3.14 runs them: the citation graph and the frontmatter, the house punctuation rule, the freshness of the bibliography, and a network check of every source URL. They live in `scripts/` and anybody can run them.

**Verified with ordinary tools rather than a service.** Corroborating the sources meant `curl` for control-probing hosts, the Wayback Machine for archived copies of pages that block automated requests or have vanished, `pdftotext` for reading the decisions published as PDFs, and `gzip` for the transfer sizes on [Receipts](/receipts/). Nothing here is a paid service and nothing is a black box.

**The repository is public, and hosting is a static host.** The source is on GitHub, which is also the correction route above. Hosting is statichost.eu, which builds from the repository: there is no server of mine holding logs of your visit and no CDN in front of it.

**Written with an AI agent, which is worth saying plainly.** The prose, the code and much of the source verification were produced by an AI agent, DeepSeek V4 Flash, running in a local harness under my direction. I set the rules and made the editorial decisions, including cutting a planned page on the law because it could not be kept current; the agent wrote, measured and checked, and its mistakes are recorded in the project's own working notes rather than quietly fixed. The caveats throughout [Receipts](/receipts/) and the "not verified" lines in the bibliography are a direct result of that arrangement: verification is done by something that documents its failures.

**Edited in Helix, Sublime Text and Neovim**, roughly in that order of use. None of them is recommended anywhere on this site, and they are listed because the question this section answers is what I actually run rather than what I would like to be seen running.

**Not used anywhere:** a CMS, a CSS or JavaScript framework, a bundler, a font service, a CDN, third-party analytics, or generated imagery. There is no newsletter, because a newsletter is a mailing list and this site is not collecting one. Analytics is planned as a cookieless counter and is not running yet, which is why the claim here is the stronger "no analytics" rather than the weaker "no cookies".

<!-- The three claims in that section are dated by their nature and should be re-read
     before publishing: the Hugo and Python versions, whether statichost.eu is still the
     host, and whether the AI agent disclosure still describes how the text was actually
     produced. The AI paragraph is a judgement call about voice and belongs to the
     maintainer; if it should be shorter, shorter is fine, but deleting it while keeping
     "no vendor worship" would not be. -->

## What this page is not

It is not a reading list of everything written about privacy. It is the record of what
this site rests on, which is a shorter and more checkable thing.

It is also not a claim that these sources are neutral. Regulators, companies, academics
and journalists all have positions, and a source's position is part of what you need to
know about it. That is what the "weak at" line is for.

---

<!-- BEGIN GENERATED BIBLIOGRAPHY -->

Generated from `data/sources.yaml` by `scripts/render-bibliography.py`. Do not edit this block by hand: run the script.

| What this counts | Number |
|---|---|
| Sources in the file | 70 |
| Cited by at least one page | 70 |
| Link opened and confirmed, with a date | 50 |
| Snapshotted to the Wayback Machine | 58 |
| No stable URL found yet | 1 |
| The document itself carries no date | 26 |

Every number above is computed from the citation file when this page is built. If the site claims a source is verified and this table disagrees, the table is right.

## Research and evidence

### <a id="source-sweeney-demographics"></a>sweeney-demographics

**Simple Demographics Often Identify People Uniquely**

Latanya Sweeney · Carnegie Mellon University, Data Privacy Working Paper 3 · 2000 · [the source itself](https://kilthub.cmu.edu/articles/journal_contribution/Simple_Demographics_Often_Identify_People_Uniquely/6625769) · [archived copy](http://web.archive.org/web/20251216173239/https://kilthub.cmu.edu/articles/journal_contribution/Simple_Demographics_Often_Identify_People_Uniquely/6625769)

**Status: verified 2026-10-13, archived.**

**Weak at:** 2000 US census data. The precise 87% figure is a property of that population and that era, and should be presented as an illustration of the mechanism rather than as a current statistic.

**Carries:**

- 87% of the US population likely identifiable from ZIP + birth date + sex.
- Anonymity by field-deletion is not anonymity.

### <a id="source-solove-taxonomy"></a>solove-taxonomy

**A Taxonomy of Privacy**

Daniel J. Solove · University of Pennsylvania Law Review, vol. 154, p. 477 · 2006 · no stable URL found yet

**Status: no URL.** Cited, but not yet publishable.

**Weak at:** A taxonomy, not a measurement. Useful for organising harms precisely; it provides no evidence about how often any of them occur.

**Carries:**

- Harms of collection, processing, dissemination and intrusion are distinct.
- Aggregation, secondary use and exclusion are three distinct named harms.

### <a id="source-solove-nothing-to-hide"></a>solove-nothing-to-hide

**"I've Got Nothing to Hide" and Other Misunderstandings of Privacy**

Daniel J. Solove · San Diego Law Review, vol. 44, no. 4, p. 745 · 2007 · [the source itself](https://digital.sandiego.edu/sdlr/vol44/iss4/5/) · [archived copy](http://web.archive.org/web/20260519004224/https://digital.sandiego.edu/sdlr/vol44/iss4/5/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A normative argument, not empirical evidence. It is the best available answer to the "nothing to hide" claim, but it does not by itself demonstrate that any particular harm occurs.

**Carries:**

- Privacy is a family of concerns, not a synonym for secrecy.
- The "nothing to hide" argument answers a question nobody asked.

### <a id="source-netflix-prize"></a>netflix-prize

**How to Break Anonymity of the Netflix Prize Dataset (FAQ)**

Arvind Narayanan, Vitaly Shmatikov · Cornell University / IEEE Symposium on Security and Privacy 2008 · 2008 · [the source itself](https://www.cs.cornell.edu/~shmat/netflix-faq.html)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** The link is the authors' plain-language FAQ, not the peer-reviewed paper ("Robust De-anonymization of Large Sparse Datasets"). Cite the paper for the method; use this for readers who want the intuition.

**Carries:**

- Cross-referencing an "anonymous" dataset against an unrelated public one breaks anonymity.
- The join, not the record, is where the harm lives.

### <a id="source-brignull-dark-patterns"></a>brignull-dark-patterns

**Deceptive Patterns (book), and the origin of the term**

Harry Brignull · deceptive.design · 2010 · [the source itself](https://www.deceptive.design/book) · [archived copy](http://web.archive.org/web/20261001052817/https://deceptive.design/book/)

**Status: verified 2026-10-13, archived.**

**Weak at:** The exact date of coinage is reported inconsistently: 2010 for the site and the term, 2011 in some academic citations of a talk. The page says 2010; if that precision cannot be confirmed, drop the year rather than pick one.

**Carries:**

- The term dark patterns was coined by Harry Brignull.
- Brignull now prefers the term deceptive design.

### <a id="source-eckersley-fingerprinting"></a>eckersley-fingerprinting

**How Unique Is Your Web Browser?**

Peter Eckersley · Privacy Enhancing Technologies (PETS) 2010, Springer · 2010 · [the source itself](https://dl.acm.org/doi/abs/10.5555/1881151.1881152)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** Sixteen years old, and the specific uniqueness rates are a property of browsers that had Flash or Java installed. The MECHANISM is the durable finding and is what this site relies on; do not quote the percentage as current.

**Carries:**

- Browser configuration alone can single out a visitor without stored state.
- Fingerprinting defeats cookie deletion by design.

### <a id="source-penney-chilling"></a>penney-chilling

**Chilling Effects: Online Surveillance and Wikipedia Use**

Jonathon W. Penney · Berkeley Technology Law Journal, vol. 31, p. 117 · 2016 · [the source itself](https://www.reuters.com/article/us-wikipedia-usage-idUSKCN0XO080/) · [archived copy](http://web.archive.org/web/20230529160016/http://www.reuters.com/article/us-wikipedia-usage-idUSKCN0XO080)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** IMPORTANT: the URL above is Reuters coverage of the study, not the study. Replace with the Berkeley Tech. L.J. version before publishing, and quote the effect size from the paper rather than from the news report. Traffic decline is also a proxy for behaviour, not a direct measurement of self-censorship.

**Carries:**

- Measurable behavioural change following disclosure of mass surveillance.
- Chilling effects operate without any enforcement action being taken.

### <a id="source-garcia-shadow-profiles"></a>garcia-shadow-profiles

**Leaking privacy and shadow profiles in online social networks**

David Garcia · Science Advances, vol. 3, no. 8, e1701172 · 2017-08-04 · [the source itself](https://pmc.ncbi.nlm.nih.gov/articles/PMC5544396/) · [archived copy](http://web.archive.org/web/20260417163947/https://pmc.ncbi.nlm.nih.gov/articles/PMC5544396/) · doi:10.1126/sciadv.1701172

**Status: verified 2026-10-14, archived.**

**Weak at:** One network, audited years after it closed. Friendster is a historical case, and the study shows that information about non-members can be predicted from what members disclose. It does not measure any harm that followed from that.

**Carries:**

- Contact lists uploaded by users contain people who never used the service.
- Data disclosed by users predicts personal information about non-users.
- One person's privacy decision changes what can be inferred about other people.

### <a id="source-zuboff-surveillance-capitalism"></a>zuboff-surveillance-capitalism

**The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power**

Shoshana Zuboff · PublicAffairs · 2019 · [the source itself](https://www.loc.gov/item/2018003901/) · [archived copy](http://web.archive.org/web/20250716182142/https://www.loc.gov/item/2018003901/)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A work of theory and interpretation. Its descriptive claims about the industry are well documented; its concepts ("instrumentarian power") are analytical tools, not findings, and are contested by other scholars.

**Carries:**

- Instrumentarian power (power exercised through the instrumentation of behaviour).
- The asymmetry of knowledge is itself the structural harm.

### <a id="source-ali-ad-delivery"></a>ali-ad-delivery

**Discrimination through Optimization: How Facebook's Ad Delivery Can Lead to Biased Outcomes**

Muhammad Ali, Piotr Sapiezynski, Miranda Bogen, Aleksandra Korolova, Alan Mislove, Aaron Rieke · Proceedings of the ACM on Human-Computer Interaction, vol. 3, CSCW · 2019-11 · [the source itself](https://dl.acm.org/doi/10.1145/3359301) · [archived copy](http://web.archive.org/web/20250106222952/https://dl.acm.org/doi/10.1145/3359301) · doi:10.1145/3359301

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** Facebook's ad system has changed substantially since 2019. The finding (that optimisation produces skewed delivery from neutral targeting) is the durable part; the specific measured skews are historical.

**Carries:**

- Identical targeting inputs produce systematically different delivery by race and gender.
- Not everyone is seen equally, so "being seen" is not a uniform cost.

### <a id="source-mathur-dark-patterns-2019"></a>mathur-dark-patterns-2019

**Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites**

Arunesh Mathur, Gunes Acar, Michael Friedman, Eli Lucherini, Jonathan Mayer, Marshini Chetty, Arvind Narayanan · Proceedings of the ACM on Human-Computer Interaction, vol. 3, CSCW · 2019-11 · [the source itself](https://webtransparency.cs.princeton.edu/dark-patterns/assets/dark-patterns-v2.pdf) · [archived copy](http://web.archive.org/web/20261011180616/https://webtransparency.cs.princeton.edu/dark-patterns/assets/dark-patterns-v2.pdf) · doi:10.1145/3359183

**Status: verified 2026-10-13, archived.**

**Weak at:** A crawl of shopping websites in 2019, so the prevalence figures are historical and specific to e-commerce. It also detects pattern-shaped markup, which cannot distinguish deliberate deception from careless design; the page says so rather than overclaiming.

**Carries:**

- 1,818 dark patterns found across 1,254 of roughly 11,000 shopping sites.
- 15 pattern types identified, concentrated on cart and checkout pages.

### <a id="source-phone-number-recycling"></a>phone-number-recycling

**Security and Privacy Risks of Number Recycling at Mobile Carriers in the United States**

Kevin Lee, Arvind Narayanan · 2021 APWG Symposium on Electronic Crime Research (eCrime) · 2021-12-01 · [the source itself](https://docs.apwg.org/ecrimeresearch/2021/ecrime2021-paper45.pdf) · [archived copy](http://web.archive.org/web/20240803134040/https://docs.apwg.org/ecrimeresearch/2021/ecrime2021-paper45.pdf) · doi:10.1109/eCrime54498.2021.9738792

**Status: verified 2026-10-14, archived.**

**Weak at:** Two US carriers and a sample of 259 numbers offered to new subscribers at the time of writing. The counts describe that sample rather than all recycled numbers, and the paper assesses whether attacks are feasible, not how often they happen.

**Carries:**

- A phone number is a key to accounts, not only a label.
- Recycled numbers carry the previous owner's accounts and leaked credentials.
- People-search services publish personal data about previous number owners.

### <a id="source-pohlmann-first-party-cookies"></a>pohlmann-first-party-cookies

**Towards Understanding First-Party Cookie Tracking in the Field**

Norbert Pohlmann et al. · ACM Internet Measurement Conference (IMC) · 2022 · [the source itself](https://norbert-pohlmann.com/wp-content/uploads/2022/04/435-Towards-Understanding-First-Party-Cookie-Tracking-in-the-Field-Prof-Norbert-Pohlmann.pdf) · [archived copy](http://web.archive.org/web/20251205052449/https://norbert-pohlmann.com/wp-content/uploads/2022/04/435-Towards-Understanding-First-Party-Cookie-Tracking-in-the-Field-Prof-Norbert-Pohlmann.pdf)

**Status: verified 2026-10-13, archived.**

**Weak at:** The linked URL is an author-hosted PDF rather than the publisher's version; replace with the ACM IMC DOI once confirmed. The underlying CNAME-cloaking technique continues to evolve, so the measured prevalence is historical.

**Carries:**

- Third-party tracking is routinely served from first-party subdomains.
- Blocklists based on third-party domain matching can be evaded.

### <a id="source-mullvad-audit-cure53"></a>mullvad-audit-cure53

**Mullvad VPN: Pentest Report (2024)**

Cure53 · Cure53 · 2024 · [the source itself](https://cure53.de/pentest-report_mullvad_2024_v1.pdf) · [archived copy](http://web.archive.org/web/20260823120243/https://cure53.de/pentest-report_mullvad_2024_v1.pdf)

**Status: verified 2026-10-13, archived.**

**Weak at:** An audit commissioned by the vendor, covering a defined scope at a point in time. It is evidence about the audited components, not a continuing guarantee, and it does not validate the parts of the system outside its scope.

**Carries:**

- Mullvad commissions and publishes independent third-party security audits.
- A published audit is a materially stronger claim than a self-description.

### <a id="source-web-almanac"></a>web-almanac

**Web Almanac**

HTTP Archive · HTTP Archive · 2025 · [the source itself](https://almanac.httparchive.org/en/2025/) · [archived copy](http://web.archive.org/web/20261013204808/https://almanac.httparchive.org/en/2025/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Reports aggregates across a large crawl. Figures change every edition, so any specific number must be quoted with its edition year, and none should be quoted second-hand, including from this site.

**Carries:**

- Annual public measurement of third-party requests and page composition.
- The authoritative dataset for "how many requests does a typical page make".

### <a id="source-ecc-encrypted-client-hello"></a>ecc-encrypted-client-hello

**The Fragile Privacy of Encrypted Client Hello: Quantifying Systemic Gaps in a Centralized Ecosystem**

Hajda, Oezdil · IFIP Networking 2026 · 2026 · [the source itself](https://ieeexplore.ieee.org/document/11579185)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** Author list only partially confirmed (surnames Hajda and Oezdil as indexed). The finding concerns the deployment ecosystem rather than ECH being broken in principle, so present it as "the fix is partial", not "the fix does not work". An open-access copy was indexed at dl.ifip.org, but that host did not respond when checked; the publisher record is the link above.

**Carries:**

- Encrypted Client Hello protects the visited hostname only partially.
- Centralisation reintroduces metadata leaks that a protocol fix cannot close.

### <a id="source-verizon-dbir"></a>verizon-dbir

**Data Breach Investigations Report**

Verizon Business · Verizon · 2026 · [the source itself](https://www.verizon.com/business/resources/reports/dbir/) · [archived copy](http://web.archive.org/web/20261014053535/https://www.verizon.com/business/resources/reports/dbir/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Produced by a company that sells security services, so it has an interest in emphasising breach prevalence. Methodology and contributor set change between editions, which breaks year-on-year comparison.

**Carries:**

- Data compromise is routine and recurring rather than exceptional.
- Every dataset held is a liability independent of collector intent.

### <a id="source-deceptive-design-types"></a>deceptive-design-types

**Deceptive Patterns: the pattern types**

Harry Brignull, and contributors · deceptive.design · no date on the document · [the source itself](https://www.deceptive.design/types) · [archived copy](http://web.archive.org/web/20261008031926/https://deceptive.design/types/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A catalogue maintained by the person who coined the term, so it is authoritative on naming while also being a project with a book to sell. Type lists grow and get renamed; the eighteen recorded here are a snapshot of the date above.

**Carries:**

- Eighteen catalogued deceptive pattern types as of October 2026.
- The canonical names used throughout the field guide.

### <a id="source-sludge-audits"></a>sludge-audits

**Dark patterns and sludge audits: an integrated approach**

Behavioural Public Policy (Cambridge University Press) · no date on the document · [the source itself](https://www.cambridge.org/core/journals/behavioural-public-policy/article/dark-patterns-and-sludge-audits-an-integrated-approach/8675A269B8FE79D2ECE0A8952D182C0B) · [archived copy](http://web.archive.org/web/20260706011949/https://www.cambridge.org/core/journals/behavioural-public-policy/article/dark-patterns-and-sludge-audits-an-integrated-approach/8675A269B8FE79D2ECE0A8952D182C0B)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** Author list and publication year are unconfirmed, and the URL is constructed from the Cambridge Core pattern rather than copied from a verified record. Confirm both before this source carries any weight in print.

**Carries:**

- Sludge is distinct from dark patterns: friction against a legitimate action.
- The two are argued to require joint auditing.

### <a id="source-swd-emissions-model"></a>swd-emissions-model

**Estimating Digital Emissions**

Sustainable Web Design · Sustainable Web Design · no date on the document · [the source itself](https://sustainablewebdesign.org/estimating-digital-emissions/) · [archived copy](http://web.archive.org/web/20261014182609/https://sustainablewebdesign.org/estimating-digital-emissions/)

**Status: verified 2026-10-14, archived.**

**Weak at:** A model rather than a measurement, and its inputs are global averages. The energy intensities come from industry-wide totals, and its default grid intensity of 494 gCO2e/kWh is a world average that the page itself tells you to replace with your own. Any figure derived from it is an estimate. This site derives one on /receipts/ and labels it as an estimate for exactly that reason.

**Carries:**

- Website emissions can be estimated from bytes transferred, energy intensity per gigabyte and grid carbon intensity.
- The model's default grid intensity is 494 gCO2e per kWh, the global average for electricity.
- Its energy intensities total 0.300 kWh per gigabyte across data centres, networks and user devices, operational and embodied combined.
- Roughly a third of the modelled total is embodied emissions, from manufacturing devices and networks rather than from running them.

## Law, regulation and regulators

### <a id="source-ftc-data-brokers-2014"></a>ftc-data-brokers-2014

**Data Brokers: A Call for Transparency and Accountability**

Federal Trade Commission · US Federal Trade Commission · 2014-05 · [the source itself](https://www.ftc.gov/system/files/documents/reports/data-brokers-call-transparency-accountability-report-federal-trade-commission-may-2014/140527databrokerreport.pdf) · [archived copy](http://web.archive.org/web/20261010115101/https://www.ftc.gov/system/files/documents/reports/data-brokers-call-transparency-accountability-report-federal-trade-commission-may-2014/140527databrokerreport.pdf)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** Nine data brokers, studied in 2014, and the industry has consolidated since. What it documents is the structure of the business, which has not changed, and every quotation taken from it here was read in the archived copy, not on ftc.gov.

**Carries:**

- Brokers hold files on consumers they have never dealt with.
- Broker data feeds decisions about credit, employment, insurance and housing.
- A risk-scoring product can refuse a transaction without explaining why.

### <a id="source-ccpa-sale-definition"></a>ccpa-sale-definition

**California Consumer Privacy Act: definition of 'sale', Cal. Civ. Code § 1798.140(ad)**

State of California · California Legislative Information · 2018 · [the source itself](https://california.public.law/codes/civil_code_section_1798.140) · [archived copy](http://web.archive.org/web/20260710111344/https://california.public.law/codes/civil_code_section_1798.140)

**Status: verified 2026-10-13, archived.**

**Weak at:** California only, and the operative definition has been amended more than once since enactment. The precise subsection number should be confirmed against the current text before publication, as it has moved.

**Carries:**

- The word sale is defined more broadly than an exchange of money.
- Sharing for cross-context behavioural advertising can fall within it.

### <a id="source-cjeu-planet49"></a>cjeu-planet49

**Bundesverband der Verbraucherzentralen v Planet49 GmbH, Case C-673/17**

Court of Justice of the European Union · Court of Justice of the European Union · 2019-10-01 · [the source itself](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62017CJ0673) · [archived copy](http://web.archive.org/web/20260624151027/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A62017CJ0673)

**Status: verified 2026-10-13, archived.**

**Weak at:** Concerns cookies and consent under the ePrivacy Directive and GDPR as they stood at the time. The holding on pre-ticked boxes is settled; its application to newer banner designs is inference, not holding.

**Carries:**

- A pre-ticked checkbox is not valid consent; consent needs an active act.
- Consent must be specific and informed to be valid.

### <a id="source-austrian-dsb-google-analytics"></a>austrian-dsb-google-analytics

**Transfer of Personal Data and the Use of Google Analytics: Austrian Data Protection Authority's Decision**

Lexology (summary of the Austrian DSB decision) · 2022 · [the source itself](https://www.lexology.com/library/document.ashx?g=bf263b49-f519-4925-9863-94f1a7a15a58)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** IMPORTANT: this is a law-firm summary, not the decision. The primary source is the Austrian DSB decision (case DSB-2021-0.586.257). Also, the legal position has moved since 2022 following subsequent adequacy arrangements, so this must be presented as history rather than current status.

**Carries:**

- EU regulators have found Google Analytics transfers unlawful in specific cases.
- The legal position has been unstable and is worth checking rather than assuming.

### <a id="source-dsa-regulation"></a>dsa-regulation

**Regulation (EU) 2022/2065: the Digital Services Act**

European Parliament and Council of the European Union · EUR-Lex · 2022-10-19 · [the source itself](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) · [archived copy](http://web.archive.org/web/20261010193345/https://eur-lex.europa.eu/eli/reg/2022/2065/oj)

**Status: verified 2026-10-13, archived.**

**Weak at:** The full regulation is long and its obligations apply to online platforms specifically, not to every website; a distinction the page must not blur. Article numbering should be checked against the current consolidated text.

**Carries:**

- Online platforms may not design interfaces that deceive or manipulate users.
- The DSA creates the enforcement power behind the examples on the page.

### <a id="source-edpb-cookie-banner-taskforce"></a>edpb-cookie-banner-taskforce

**Report of the work undertaken by the Cookie Banner Taskforce**

European Data Protection Board · European Data Protection Board · 2023-01-17 · [the source itself](https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-cookie-banner-taskforce_en) · [archived copy](http://web.archive.org/web/20260615211551/https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-cookie-banner-taskforce_en)

**Status: verified 2026-10-14, archived.**

**Weak at:** The report says itself that its positions are a minimum common denominator agreed between supervisory authorities, are not standalone findings, and do not prejudge any individual complaint. It is a coordination record, not a ruling, and it concerns the banner designs complained about by one complainant rather than banners in general. Colour and contrast questions are explicitly left to case-by-case review.

**Carries:**

- Supervisory authorities met thirteen times to coordinate on cookie banner complaints.
- The absence of a reject option on the layer carrying a consent button was held by a vast majority of authorities to infringe the consent standard.
- Pre-ticked boxes to opt in do not produce valid consent.
- Reject offered only as a link inside a paragraph, or outside the banner, does not produce valid consent without sufficient visual support.
- A reject button whose text is unreadable against its own background was treated as manifestly misleading.
- Legitimate interests cannot be the legal basis for placing or reading cookies.
- Cookies classified as essential when they are not is a recognised problem.

### <a id="source-cjeu-iab-europe-tcf"></a>cjeu-iab-europe-tcf

**Press release No 44/24: Judgment of the Court in Case C-604/22, IAB Europe**

Court of Justice of the European Union · Court of Justice of the European Union · 2024-03-07 · [the source itself](https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240044en.pdf) · [archived copy](http://web.archive.org/web/20251101015834/https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-03/cp240044en.pdf)

**Status: verified 2026-10-14, archived.**

**Weak at:** This is the court's own press release, not the judgment, and it carries the court's disclaimer that it is an unofficial document for media use and not binding. Use it for the shape of the holdings, not for the court's reasoning, and replace it with the judgment text (Case C-604/22, ECLI:EU:C:2024:214) once a stable full-text link is confirmed. The full judgment was not retrievable from a terminal: EUR-Lex serves a JavaScript challenge instead of the document and curia.europa.eu serves a script shell, so neither could be read here. The proceedings remain live before the referring court on the points the Court left to it.

**Carries:**

- A Transparency and Consent String encodes a user's consent choices and is shared across the advertising system.
- The Court held that a TC String constitutes personal data.
- Combined with an identifier such as an IP address, a TC String can be used to profile and identify a user.
- IAB Europe was held to be a joint controller for the recording of consent choices in a TC String.
- The Court did not treat IAB Europe as controller of the processing that happens after that recording unless it influenced those purposes and means.

### <a id="source-edpb-consent-or-pay"></a>edpb-consent-or-pay

**Opinion 08/2024 on Valid Consent in the Context of Consent or Pay Models Implemented by Large Online Platforms**

European Data Protection Board · European Data Protection Board · 2024-04-17 · [the source itself](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-082024-on-valid-consent-in-the-context-of-consent-or_en) · [archived copy](http://web.archive.org/web/20261014174517/https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-082024-on-valid-consent-in-the-context-of-consent-or_en)

**Status: verified 2026-10-14, archived.**

**Weak at:** An advisory opinion, not binding law, and explicitly framed around LARGE online platforms rather than all sites. Do not present it as a general rule for every consent-or-pay banner. A corrigendum of October 2024 makes editorial corrections to paragraphs 49 and 60 and footnotes 14, 24, 50, 76 and 131, so any passage quoted or paraphrased from the opinion should be checked against the corrected text.

**Carries:**

- Whether "consent or pay" is freely given is contested at EU level.
- Regulators treat banner design as a consent-validity question.

### <a id="source-ftc-gravy-venntel"></a>ftc-gravy-venntel

**FTC Takes Action Against Gravy Analytics, Venntel for Unlawfully Selling Location Data Tracking Consumers to Sensitive Sites**

Federal Trade Commission · US Federal Trade Commission · 2024-12 · [the source itself](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-gravy-analytics-venntel-unlawfully-selling-location-data-tracking-consumers) · [archived copy](http://web.archive.org/web/20261007010458/https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-gravy-analytics-venntel-unlawfully-selling-location-data-tracking-consumers)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** US jurisdiction only, and an enforcement action is an allegation resolved by settlement rather than a judicial finding of fact.

**Carries:**

- Location data collected for advertising was sold into unforeseen contexts.
- Sensitive-location inference (clinics, worship, protest) is a named harm.

### <a id="source-amsterdam-court-dsa-2025"></a>amsterdam-court-dsa-2025

**Rechtbank Amsterdam, ECLI:NL:RBAMS:2025:7253**

Rechtbank Amsterdam · de Rechtspraak (Netherlands Judiciary) · 2025 · [the source itself](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBAMS:2025:7253) · [archived copy](http://web.archive.org/web/20260913095228/https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3ARBAMS%3A2025%3A7253)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A Dutch-language national court judgment, so any summary depends on translation. The precise holding and its scope should be read in the original before the page characterises it. National case law does not bind other member states.

**Carries:**

- A national court applied the DSA to interface design.
- Non-persistent settings, where a refusal does not stick, were treated as a dark pattern.

### <a id="source-ftc-mobilewalla"></a>ftc-mobilewalla

**FTC Finalizes Order Banning Mobilewalla from Selling Sensitive Location Data**

Federal Trade Commission · US Federal Trade Commission · 2025-01 · [the source itself](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data) · [archived copy](http://web.archive.org/web/20260716183753/https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A settlement with one company. It is evidence of a practice, not evidence of how widespread the practice is.

**Carries:**

- Regulators have treated sensitive location data as a categorical harm.

### <a id="source-ftc-surveillance-pricing"></a>ftc-surveillance-pricing

**FTC Surveillance Pricing Study Indicates Wide Range of Personal Data Used to Set Individualized Consumer Prices**

Federal Trade Commission · US Federal Trade Commission · 2025-01 · [the source itself](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer) · [archived copy](http://web.archive.org/web/20261003073808/https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A press release summarising a study, not the study itself. It establishes that personal data feeds individualised pricing; it does not quantify how much consumers were overcharged. Link the underlying orders for specifics.

**Carries:**

- Personal data unrelated to the transaction is used to set individual prices.
- Inferred attributes have direct financial consequences.

### <a id="source-cnil-analytics-self-assessment"></a>cnil-analytics-self-assessment

**Outil d'auto-évaluation relatif à la mise en œuvre d'une solution de mesure d'audience exemptée de consentement**

CNIL · Commission nationale de l'informatique et des libertés (France) · 2025-07 · [the source itself](https://www.cnil.fr/sites/default/files/2025-07/outil_d_auto-evaluation_mesure_d_audience.pdf) · [archived copy](http://web.archive.org/web/20260515212331/https://cnil.fr/sites/default/files/2025-07/outil_d_auto-evaluation_mesure_d_audience.pdf)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A PDF published in French in July 2025. It is a self-assessment aid rather than a binding determination, and it post-dates some of the guidance it supports, so confirm it is still the current version.

**Carries:**

- Regulators provide a configuration-level test rather than a product list.
- Compliance is assessable by the site owner without legal counsel.

### <a id="source-ftc-click-to-cancel-rosca"></a>ftc-click-to-cancel-rosca

**Click-to-cancel lives on under ROSCA and Section 5**

DLA Piper · DLA Piper · 2025-09 · [the source itself](https://www.dlapiper.com/en-ar/insights/publications/2025/09/click-to-cancel-lives-on-under-rosca-and-section-5)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A law-firm client note, not the court ruling that vacated the rule. Use it to establish that enforcement continued under other statutes; cite the appellate decision itself for the vacatur, and check the current enforcement position.

**Carries:**

- The FTC click-to-cancel rule was struck down in 2025.
- Subscription-trap enforcement continued under ROSCA and the FTC Act.

### <a id="source-cnil-google-san-2025-004"></a>cnil-google-san-2025-004

**Deliberation of restricted committee No SAN-2025-004 of 1 September 2025 concerning Google LLC and Google Ireland Limited**

CNIL · Commission nationale de l'informatique et des libertés (France) · 2025-09-01 · [the source itself](https://www.cnil.fr/sites/default/files/2025-09/cnil_sanction_google_en.pdf) · [archived copy](http://web.archive.org/web/20261010075923/https://www.cnil.fr/sites/default/files/2025-09/cnil_sanction_google_en.pdf)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** An English courtesy translation, published with a warning that the French version prevails. The decision concerns advertising attached to a signed-in email service rather than cookie banners as such, and its consent and tracer findings are one company's case. Only the parts of it read here are relied on. Every URL on the cnil.fr website itself was serving a maintenance page when this was checked, and only the file server answered, so the decision page cannot currently be read in a browser either.

**Carries:**

- The CNIL opened a verification mission specifically into tracers read and placed on the devices of signed-in users.
- A national regulator treats advertising linked to a signed-in account as a consent question, not a terms-of-service question.

### <a id="source-conseil-etat-yahoo-cookies"></a>conseil-etat-yahoo-cookies

**Conseil d'État, 10ème et 9ème chambres réunies, 7 October 2025, No 494300 (Yahoo EMEA Limited)**

Conseil d'État · Conseil d'État (France) · 2025-10-07 · [the source itself](https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-10-07/494300) · [archived copy](http://web.archive.org/web/20260615104518/https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-10-07/494300)

**Status: verified 2026-10-14, archived.**

**Weak at:** French, and in French. It is a ruling on one company and largely on questions of the regulator's competence and procedure rather than on what a good banner looks like. The underlying sanction is a national transposition of the ePrivacy rules, so the amounts and the procedural findings do not transfer to other jurisdictions. The decision was read here in French and its reasoning is described rather than quoted.

**Carries:**

- The CNIL fined Yahoo EMEA 10 million euros over cookie advertising without prior consent and over the means of withdrawing consent.
- The Conseil d'État upheld the finding that users faced an obstacle to withdrawing consent.
- The Conseil d'État held that the CNIL can act on cookie rules even where the operation is not processing of personal data.
- Consent can be expressed through settings of the user's device or another device under the user's control.

### <a id="source-cnil-analytics-exemption"></a>cnil-analytics-exemption

**Cookies: solutions pour les outils de mesure d'audience**

CNIL · Commission nationale de l'informatique et des libertés (France) · no date on the document · [the source itself](https://www.cnil.fr/fr/cookies-solutions-pour-les-outils-de-mesure-daudience) · [archived copy](http://web.archive.org/web/20261003033711/https://www.cnil.fr/fr/cookies-solutions-pour-les-outils-de-mesure-daudience)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** French jurisdiction only. The exemption conditions are specific to French implementation of EU rules and change; do not present them as a general EU rule. The page is in French.

**Carries:**

- Some audience-measurement configurations can be exempt from consent.
- Exemption depends on configuration and conditions, not on the product brand.

### <a id="source-search-index-concentration"></a>search-index-concentration

**Filing in United States v. Google LLC, No. 1:20-cv-03010 (D.D.C.)**

US District Court for the District of Columbia (via CourtListener RECAP) · no date on the document · [the source itself](https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1304.1.pdf) · [archived copy](http://web.archive.org/web/20260613193128/https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1304.1.pdf)

**Status: verified 2026-10-13, archived.**

**Weak at:** IMPORTANT: this is a filing within litigation, so the statement is a party's or court's characterisation rather than a neutral measurement, and the document type and date are unconfirmed. It also speaks to the US market specifically, so it does not account for non-US engines such as Mojeek. Use it to establish that independent indices are scarce, not to claim an exact count.

**Carries:**

- Only a small number of general search engines run independent proprietary indices.
- DuckDuckGo's dependence on a licensed index is a structural limitation.

### <a id="source-website-wiretap-litigation"></a>website-wiretap-litigation

**Veradigm Ruling Highlights Website Tracker and Wiretap Litigation Risk**

Thompson Coburn LLP · Thompson Coburn LLP · no date on the document · [the source itself](https://www.thompsoncoburn.com/insights/veradigm-ruling-highlights-website-tracker-and-wiretap-litigation-risk-102n9r7/) · [archived copy](http://web.archive.org/web/20260711080420/https://www.thompsoncoburn.com/insights/veradigm-ruling-highlights-website-tracker-and-wiretap-litigation-risk-102n9r7/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A law firm's client-facing analysis of one ruling, so it is neither neutral nor a survey of the field, and it covers US jurisdiction only. If the page keeps this claim it should eventually cite the underlying decisions, or be softened to a general statement that such litigation exists and is ongoing.

**Carries:**

- Website tracking technology has attracted wiretap-style litigation in the US.
- Healthcare contexts have been a particular focus of that litigation.

## Journalism

### <a id="source-aol-4417749"></a>aol-4417749

**A Face Is Exposed for AOL Searcher No. 4417749**

Michael Barbaro, Tom Zeller Jr. · The New York Times · 2006-08-09 · [the source itself](https://www.nytimes.com/2006/08/10/learning/featuredarticle/20060810thursday.html) · [archived copy](http://web.archive.org/web/20240603055457/https://www.nytimes.com/2006/08/10/learning/featuredarticle/20060810thursday.html)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** Contemporary journalism, not research. It documents the re-identification convincingly, but the ~658,000-user and ~20-million-query figures come from AOL's own withdrawn release and are reported second-hand here.

**Carries:**

- Aggregation harms require no breach or malice.
- Pseudonymised data is re-identifiable from content alone.

### <a id="source-gmail-scanning-2017"></a>gmail-scanning-2017

**Google will stop scanning content of personal emails**

The Guardian · The Guardian · 2017-06-26 · [the source itself](https://www.theguardian.com/technology/2017/jun/26/google-will-stop-scanning-content-of-personal-emails)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** News coverage; the primary source is Google's own 2017 announcement, which should be located and linked. Note the scope carefully: this applies to FREE CONSUMER Gmail, and ending ad-personalisation scanning is not the same as collecting nothing. Do not let the site imply the practice continues, or that its absence means Gmail is private; the page's structural criticisms stand either way.

**Carries:**

- Google ended ad-personalisation scanning of consumer Gmail in 2017.
- The widely repeated claim that Google reads Gmail to target ads is out of date.

### <a id="source-signal-usernames"></a>signal-usernames

**Signal Finally Rolls Out Usernames, So You Can Keep Your Phone Number Private**

Wired · Wired · 2024-02 · [the source itself](https://www.wired.com/story/signal-launches-usersnames-phone-number-privacy/) · [archived copy](http://web.archive.org/web/20260927221952/https://www.wired.com/story/signal-launches-usersnames-phone-number-privacy/)

**Status: verified 2026-10-13, archived.**

**Weak at:** News coverage of a feature launch. The phone-number requirement was a long-standing criticism and usernames mitigate rather than remove it; registration still requires a number. Do not present this as the concern being fully resolved.

**Carries:**

- Signal now supports usernames, reducing phone-number exposure to contacts.
- The phone-number-based criticism is well enough established to be the premise.

### <a id="source-google-incognito-settlement"></a>google-incognito-settlement

**Google to delete billions of browser records to settle 'Incognito' lawsuit**

CNN Business · CNN · 2024-04-01 · [the source itself](https://www.cnn.com/2024/04/01/tech/google-to-delete-data-records-to-settle-incognito-lawsuit/index.html) · [archived copy](http://web.archive.org/web/20251124101304/https://www.cnn.com/2024/04/01/tech/google-to-delete-data-records-to-settle-incognito-lawsuit/index.html)

**Status: verified 2026-10-13, archived.**

**Weak at:** News coverage of a settlement, not the court record. It establishes that the claim was settled and records were to be deleted; it is not a finding that incognito mode was misrepresented. Cite the court filing for the specifics.

**Carries:**

- The gap between what private browsing does and what users believe was substantial enough to litigate.
- Billions of records were collected from private sessions.

### <a id="source-ftc-amazon-25b"></a>ftc-amazon-25b

**Amazon to pay $2.5 billion to settle Prime deception allegations**

Reuters · Reuters · 2025-09-25 · [the source itself](https://www.reuters.com/world/amazon-pay-25-billion-settle-prime-deception-allegations-2025-09-25/)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** News coverage of a settlement, and a settlement is not a finding of liability. Reuters is behind a bot filter and the URL pattern was reconstructed, so confirm it resolves and prefer the FTC's own announcement as the primary source.

**Carries:**

- A multi-billion dollar US settlement over subscription enrolment and cancellation.
- The alleged harm was the design of the cancellation flow, not the product.

### <a id="source-ec-x-fine-120m"></a>ec-x-fine-120m

**EU fines X 120m euros for breaching online content rules**

ABC News (Australian Broadcasting Corporation) · ABC News · 2025-12-06 · [the source itself](https://www.abc.net.au/news/2025-12-06/eu-fines-x-120m-euros-for-breaching-online-content-rules/106109626) · [archived copy](http://web.archive.org/web/20260309110630/https://www.abc.net.au/news/2025-12-06/eu-fines-x-120m-euros-for-breaching-online-content-rules/106109626)

**Status: verified 2026-10-13, archived.**

**Weak at:** News coverage of a regulatory decision, not the decision itself. The Commission's own press release and the non-compliance decision are the primary sources and should replace this once located. The fine covers transparency failures as well as dark patterns, so it is not a dark-patterns-only precedent.

**Carries:**

- The first DSA non-compliance fine was issued against X, reported at EUR 120m.
- Dark patterns featured among the findings.

## The projects and companies themselves

### <a id="source-matomo-log-analytics"></a>matomo-log-analytics

**What is Web Log Analytics and Why You Should Use It**

Matomo · Matomo · 2024-06 · [the source itself](https://matomo.org/blog/2024/06/web-log-analytics/) · [archived copy](http://web.archive.org/web/20260519075647/https://matomo.org/blog/2024/06/web-log-analytics/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Written by a company selling analytics software, so it has an interest in the framing and it is not neutral about server logs being sufficient. Use it for the technical description of what logs contain, not for the recommendation.

**Carries:**

- Server logs are first-party, require no JavaScript and cannot be blocked.
- Log analysis is a viable baseline before buying any tool.

### <a id="source-ecosia-eusp-index"></a>ecosia-eusp-index

**L'émergence d'un meilleur Internet : notre index de recherche européen vient d'être déployé**

Ecosia · Ecosia · 2025-08-12 · [the source itself](https://fr.blog.ecosia.org/notre-index-de-recherche-europeen-vient-detre-deploye/) · [archived copy](http://web.archive.org/web/20261014185333/https://fr.blog.ecosia.org/notre-index-de-recherche-europeen-vient-detre-deploye/)

**Status: verified 2026-10-14, archived.**

**Weak at:** A company's own account of its own product, published in French, and the only source here for what Ecosia's results are built from. It establishes that the joint index exists and that results for users in France are served from it. It says nothing about coverage elsewhere, about result quality, or about how much of a query is still answered by a licensed index, so it is not evidence that Ecosia is independent of the large indexes everywhere. The "European" in the index's name should not be read as "complete".

**Carries:**

- Ecosia and Qwant built a search index together, called European Search Perspective.
- Ecosia states that search results for its users in France now come from that index directly.
- Ecosia states that only a handful of companies have built their own index.

### <a id="source-mullvad-dns-shutdown"></a>mullvad-dns-shutdown

**Shutting down our public encrypted DNS servers and sponsoring Quad9 instead**

Mullvad · Mullvad VPN · 2026-09-03 · [the source itself](https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead) · [archived copy](http://web.archive.org/web/20261014185932/https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead)

**Status: verified 2026-10-14, archived.**

**Weak at:** A company announcing the end of its own service, which makes it authoritative about the date and about nothing else. It says what Mullvad will sponsor and does not evaluate Quad9, so it is not evidence that Quad9 is good, only that Mullvad is paying for it. The post is also the whole record for the successor: there is no independent assessment here of how Quad9 compares on logging, blocking policy or jurisdiction.

**Carries:**

- Mullvad has operated public encrypted DNS servers since 2022.
- Mullvad is shutting those public encrypted DNS servers down, with 2 November 2026 given as the date to switch by.
- Mullvad states that it will sponsor Quad9 rather than run a public resolver itself.

### <a id="source-mullvad-public-dns"></a>mullvad-public-dns

**DNS over HTTPS and DNS over TLS**

Mullvad · Mullvad VPN · 2026-09-03 · [the source itself](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) · [archived copy](http://web.archive.org/web/20261014185705/https://mullvad.net/en/help/dns-over-https-and-dns-over-tls)

**Status: verified 2026-10-14, archived.**

**Weak at:** A company's own help page about a service it is in the middle of switching off, so it is a notice rather than a stable description, and it says nothing about the successor. The page's "last updated" date is 3 September 2026 and the discontinuation it announces is dated 2 November 2026, which means anything cited from it is time-limited by design. Read it for the date, not for a recommendation.

**Carries:**

- Mullvad runs a public encrypted DNS service.
- Mullvad states that the public encrypted DNS service will be discontinued on 2 November 2026.
- The DNS resolver built into the Mullvad VPN is a separate service from the public one.

### <a id="source-ublock-origin-chrome"></a>ublock-origin-chrome

**uBlock Origin on Chrome**

uBlock Origin project · ublockorigin.com · 2026-09-22 · [the source itself](https://ublockorigin.com/chrome/) · [archived copy](http://web.archive.org/web/20261011125809/https://ublockorigin.com/chrome/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A project page describing its own situation, and the situation is moving: browser extension platform rules continue to change. Treat the specifics as a snapshot with the stated update date, not as settled.

**Carries:**

- Full uBlock Origin no longer runs in current Chrome.
- uBlock Origin Lite is a separate Manifest V3 extension by the same developer.
- The Lite version is not equivalent for sites that resist blocking.

### <a id="source-awesome-privacy-analytics"></a>awesome-privacy-analytics

**Awesome Privacy-Friendly Web Analytics**

spekulatius (community-maintained) · GitHub · no date on the document · [the source itself](https://github.com/spekulatius/awesome-privacy-friendly-web-analytics) · [archived copy](http://web.archive.org/web/20251126075142/https://github.com/spekulatius/awesome-privacy-friendly-web-analytics)

**Status: verified 2026-10-13, archived.**

**Weak at:** A community list with no editorial standard and no verification of the claims made by the projects it includes. Inclusion is not an endorsement, and some listed tools may be abandoned.

**Carries:**

- A more current field of alternatives than any article can maintain.
- Demonstrates the category is large enough to choose within.

### <a id="source-cnil-dark-patterns-quiz"></a>cnil-dark-patterns-quiz

**Quiz: will you be able to recognize dark patterns?**

CNIL (LINC) · Commission nationale de l'informatique et des libertés (France) · no date on the document · [the source itself](https://linc.cnil.fr/en/quizz-will-you-be-able-recognize-dark-patterns) · [archived copy](http://web.archive.org/web/20260516023819/https://linc.cnil.fr/en/quizz-will-you-be-able-recognize-dark-patterns)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** An educational exercise rather than evidence, published by a regulator with an interest in the subject. It is included as a reader action, not as a source for any factual claim.

**Carries:**

- A regulator-built interactive exercise in recognising deceptive design.
- Useful as a reader action at the end of the page.

### <a id="source-codeberg"></a>codeberg

**Codeberg: a non-profit home for free and open source projects**

Codeberg e.V. · Codeberg e.V. · no date on the document · [the source itself](https://codeberg.org/) · [archived copy](http://web.archive.org/web/20261013122315/https://codeberg.org/)

**Status: not verified.** The link has not been opened and confirmed, so the claim it carries is unproven.

**Weak at:** A platform describing itself. Resource limits and acceptable-use policy are set by the association and have changed before, so the governance claim is the durable part and the operational specifics are not.

**Carries:**

- Non-profit, donation-funded hosting running Forgejo.
- An alternative to a single company owning open-source infrastructure.

### <a id="source-eff-cover-your-tracks"></a>eff-cover-your-tracks

**Cover Your Tracks**

Electronic Frontier Foundation · Electronic Frontier Foundation · no date on the document · [the source itself](https://coveryourtracks.eff.org/) · [archived copy](http://web.archive.org/web/20261013235610/https://coveryourtracks.eff.org/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A measurement tool, not a study. It reports what your browser exposes at the moment you run it, which can vary between runs and does not by itself prove that any particular site is fingerprinting you.

**Carries:**

- Lets a reader measure their own fingerprint instead of trusting a claim.
- Demonstrates what survives opening a private window.

### <a id="source-ga4-consent-mode"></a>ga4-consent-mode

**Consent Mode v2 in Practice: What Actually Gets Sent to Google Ads and GA4 After Consent Is Denied**

Sii Poland · Sii Poland · no date on the document · [the source itself](https://sii.pl/blog/en/consent-mode-v2-in-practice-what-actually-gets-sent-to-google-ads-and-ga4-after-consent-is-denied/)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** A practitioner explainer from an agency that implements these systems, undated at the time of writing, describing behaviour that Google changes. Verify against Google's own Consent Mode documentation before relying on the specifics.

**Carries:**

- Consent Mode still transmits reduced events after a visitor declines.
- The technical behaviour differs from what visitors likely assume refusal means.

### <a id="source-goatcounter"></a>goatcounter

**GoatCounter**

Martin Tournoij · GoatCounter · no date on the document · [the source itself](https://www.goatcounter.com/) · [archived copy](http://web.archive.org/web/20261008022424/https://www.goatcounter.com/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Deliberately limited by design, so it will not suit anyone needing sessions, funnels or attribution. Commercial-use terms and hosting options have changed since launch; check the current licence and pricing.

**Carries:**

- A visit counter can work with no cookies and no personal data.
- Open source and self-hostable as well as hosted.

### <a id="source-google-build-profiles"></a>google-build-profiles

**Use bid requests to build user profiles**

Google · Google for Developers (Authorized Buyers RTB) · no date on the document · [the source itself](https://developers.google.com/authorized-buyers/rtb/build-profiles-with-bid-requests) · [archived copy](http://web.archive.org/web/20260929210210/https://developers.google.com/authorized-buyers/rtb/build-profiles-with-bid-requests)

**Status: verified 2026-10-13, archived.**

**Weak at:** Vendor documentation, which is the point: it is evidence of what the ad industry says its own systems are for, not an independent finding about harm. It also sets conditions on the practice, so it must not be presented as an unconditional authorisation. Quote it verbatim rather than paraphrasing.

**Carries:**

- Google defines a user profile as a mapping of a user identifier to information about the user, built from bid requests.
- The bid request carries the Google User ID in the BidRequest.user.id field.
- Building profiles from bid request data is documented as a supported practice.

### <a id="source-google-cookie-matching"></a>google-cookie-matching

**Cookie Matching**

Google · Google for Developers (Authorized Buyers RTB) · no date on the document · [the source itself](https://developers.google.com/authorized-buyers/rtb/cookie-guide) · [archived copy](http://web.archive.org/web/20261011063053/https://developers.google.com/authorized-buyers/rtb/cookie-guide)

**Status: verified 2026-10-13, archived.**

**Weak at:** Describes Google's mechanism only, and cookie matching is implemented differently across the ecosystem. It presumes access to Authorized Buyers tooling that most readers will not have, so use it as a description of a documented capability rather than something the reader can go and inspect.

**Carries:**

- Cookie matching links a bidder's user ID to a corresponding Google User ID.
- Match tables map identifiers between domains.

### <a id="source-google-openrtb-guide"></a>google-openrtb-guide

**OpenRTB Integration**

Google · Google for Developers (Authorized Buyers RTB) · no date on the document · [the source itself](https://developers.google.com/authorized-buyers/rtb/openrtb-guide) · [archived copy](http://web.archive.org/web/20260929210210/https://developers.google.com/authorized-buyers/rtb/openrtb-guide)

**Status: verified 2026-10-13, archived.**

**Weak at:** Google's implementation of OpenRTB specifically, so field names and extensions are Google-specific and other ad systems differ. It documents structure, not volume: it says what a bid request contains, not how many are sent or to whom.

**Carries:**

- Bid requests contain BidRequest, Device, User and Geo objects.
- Geo information is coarse device location approximated from the IP address.

### <a id="source-mailbox-org"></a>mailbox-org

**mailbox.org: pricing and features**

mailbox.org · Heinlein Support GmbH · no date on the document · [the source itself](https://mailbox.org/en/)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** Prices and storage tiers change without notice and the page carries no status date, so the figures quoted must be presented as "at the time of writing" and re-checked before publishing. Commercial provider describing its own product.

**Carries:**

- Custom domain names are supported, including on the entry paid tier.
- Entry tier includes mail, calendar, address book and drive storage.

### <a id="source-matomo"></a>matomo

**Matomo**

Matomo · Matomo · no date on the document · [the source itself](https://matomo.org/)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** The heaviest of the open-source options and correspondingly more complex to run, which is itself a cost the page should not undersell. Being a near drop-in GA replacement means it also invites re-creating the same over-collection.

**Carries:**

- Open source analytics available self-hosted or as a service.
- Closest feature-comparable replacement for a full analytics platform.

### <a id="source-mullvad"></a>mullvad

**Mullvad VPN**

Mullvad VPN AB · Mullvad VPN AB · no date on the document · [the source itself](https://mullvad.net/) · [archived copy](http://web.archive.org/web/20171206015215/https://www.mullvad.net/)

**Status: verified 2026-10-13, archived.**

**Weak at:** A commercial provider describing its own product, so the account model is verifiable but the no-logs claim is a statement of policy. The audit report below is the better evidence; this entry is for the account and payment model only.

**Carries:**

- Accounts are numbered rather than tied to an email address.
- Cash payment is accepted, reducing the identity attached to an account.

### <a id="source-peertube"></a>peertube

**PeerTube: federated video hosting**

Framasoft · Framasoft · no date on the document · [the source itself](https://joinpeertube.org/) · [archived copy](http://web.archive.org/web/20261011023510/https://joinpeertube.org/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Describes the software and its federation model, not adoption. It says nothing about audience size, which is the actual obstacle to using it as a YouTube replacement, and the page is promotional in tone.

**Carries:**

- Federated video hosting across independent instances.
- No single platform decides recommendation or removal.

### <a id="source-plausible"></a>plausible

**Plausible Analytics**

Plausible Analytics · Plausible Analytics · no date on the document · [the source itself](https://plausible.io/)

**Status: verified 2026-10-13, not archived yet.**

**Weak at:** A commercial hosted service, so its own claims about compliance are marketing rather than certification. Cookieless operation does not by itself settle the consent question in every jurisdiction.

**Carries:**

- Hosted cookieless analytics with a pay-for-service rather than ad-funded model.
- EU-based operation, relevant to transfer concerns.

### <a id="source-posteo"></a>posteo

**Posteo FAQ**

Posteo e.K. · Posteo · no date on the document · [the source itself](https://posteo.de/en/site/faq) · [archived copy](http://web.archive.org/web/20260920123326/https://posteo.de/en/site/faq)

**Status: verified 2026-10-13, archived.**

**Weak at:** The provider describing itself. Vendor claims about business model and policy are checkable against their published terms, but claims about security are not independently verified here. Pricing has no status date on the page.

**Carries:**

- Posteo does not support custom domains, and states the reason as policy.
- Supporting custom domains would require storing customer identity data.
- Ad-free, paid model with no free tier.

### <a id="source-prebid-bidder-count"></a>prebid-bidder-count

**How many bidders should I work with for header bidding?**

Prebid.org · Prebid.org · no date on the document · [the source itself](https://docs.prebid.org/overview/how-many-bidders-for-header-bidding) · [archived copy](http://web.archive.org/web/20250518045716/https://docs.prebid.org/overview/how-many-bidders-for-header-bidding)

**Status: verified 2026-10-13, archived.**

**Weak at:** Publisher-facing guidance from the organisation maintaining the leading header-bidding library, addressing revenue optimisation rather than privacy. The roughly-ten-bidders figure is an industry rule of thumb the page itself discusses critically, not a measured constant, so it must not be presented as exact.

**Carries:**

- Around ten bidders per auction is a common industry practice.
- Publishers weigh bidder count against page latency.

### <a id="source-signal-donate"></a>signal-donate

**Donate to Signal**

Signal Technology Foundation · Signal Technology Foundation · no date on the document · [the source itself](https://signal.org/donate/) · [archived copy](http://web.archive.org/web/20261014191124/https://signal.org/donate/)

**Status: verified 2026-10-14, archived.**

**Weak at:** A donation page, which is the one page where an organisation has an interest in how its legal status reads. It establishes what the Signal Technology Foundation is, and it says nothing about how the organisation behaves, what it retains, or what it can be compelled to hand over. Nonprofit status is a statement about ownership and profit, not a privacy guarantee, and it should never be presented as one.

**Carries:**

- Signal Technology Foundation is a nonprofit under section 501c3 of the US Internal Revenue Code.
- Signal describes itself as an independent nonprofit, supported by grants and donations.

### <a id="source-themarkup-blacklight"></a>themarkup-blacklight

**Blacklight**

The Markup · The Markup · no date on the document · [the source itself](https://themarkup.org/blacklight) · [archived copy](http://web.archive.org/web/20261010072240/https://themarkup.org/blacklight)

**Status: verified 2026-10-13, archived.**

**Weak at:** Reports techniques detected on a single page load, so it can miss anything loaded conditionally and cannot detect server-side tracking at all. Its value is as a counter-argument to self-description, not as a complete audit.

**Carries:**

- Lets a reader measure a site rather than read its privacy policy.
- Detects session recording, fingerprinting and ad targeting on a live page.

### <a id="source-ublock-origin"></a>ublock-origin

**uBlock Origin**

Raymond Hill · GitHub · no date on the document · [the source itself](https://github.com/gorhill/uBlock) · [archived copy](http://web.archive.org/web/20261011204436/https://github.com/gorhill/uBlock)

**Status: verified 2026-10-13, archived.**

**Weak at:** Maintained largely by one person, which is a supply-chain consideration the site elsewhere argues matters. Its full version does not run under Chrome's Manifest V3, so availability differs by browser and this is worth stating rather than glossing.

**Carries:**

- A single free action substantially reduces third-party requests per page.
- Open source with an independently maintained blocklist ecosystem.

### <a id="source-umami"></a>umami

**Umami**

Umami · Umami · no date on the document · [the source itself](https://umami.is/) · [archived copy](http://web.archive.org/web/20261005062612/https://umami.is/)

**Status: verified 2026-10-13, archived.**

**Weak at:** Self-hosting shifts the maintenance and the compliance obligations onto the site owner, which the page presents as a benefit and is also a liability. Feature set is narrower than Matomo's.

**Carries:**

- Lightweight open-source analytics suitable for existing self-hosters.
- Self-hosting keeps all measurement data first-party.

## Which page rests on which sources

**You Don't Need Google Analytics** (11): [`cnil-analytics-exemption`](#source-cnil-analytics-exemption), [`cnil-analytics-self-assessment`](#source-cnil-analytics-self-assessment), [`matomo-log-analytics`](#source-matomo-log-analytics), [`austrian-dsb-google-analytics`](#source-austrian-dsb-google-analytics), [`ga4-consent-mode`](#source-ga4-consent-mode), [`web-almanac`](#source-web-almanac), [`goatcounter`](#source-goatcounter), [`plausible`](#source-plausible), [`matomo`](#source-matomo), [`umami`](#source-umami), [`awesome-privacy-analytics`](#source-awesome-privacy-analytics)

**Consent Theatre** (6): [`edpb-cookie-banner-taskforce`](#source-edpb-cookie-banner-taskforce), [`cjeu-iab-europe-tcf`](#source-cjeu-iab-europe-tcf), [`conseil-etat-yahoo-cookies`](#source-conseil-etat-yahoo-cookies), [`cnil-google-san-2025-004`](#source-cnil-google-san-2025-004), [`edpb-consent-or-pay`](#source-edpb-consent-or-pay), [`cjeu-planet49`](#source-cjeu-planet49)

**The Dark Patterns Field Guide** (11): [`deceptive-design-types`](#source-deceptive-design-types), [`mathur-dark-patterns-2019`](#source-mathur-dark-patterns-2019), [`brignull-dark-patterns`](#source-brignull-dark-patterns), [`sludge-audits`](#source-sludge-audits), [`dsa-regulation`](#source-dsa-regulation), [`ec-x-fine-120m`](#source-ec-x-fine-120m), [`ftc-amazon-25b`](#source-ftc-amazon-25b), [`amsterdam-court-dsa-2025`](#source-amsterdam-court-dsa-2025), [`ftc-click-to-cancel-rosca`](#source-ftc-click-to-cancel-rosca), [`cjeu-planet49`](#source-cjeu-planet49), [`cnil-dark-patterns-quiz`](#source-cnil-dark-patterns-quiz)

**Seven Things That Aren't True** (12): [`eckersley-fingerprinting`](#source-eckersley-fingerprinting), [`eff-cover-your-tracks`](#source-eff-cover-your-tracks), [`themarkup-blacklight`](#source-themarkup-blacklight), [`ecc-encrypted-client-hello`](#source-ecc-encrypted-client-hello), [`google-incognito-settlement`](#source-google-incognito-settlement), [`sweeney-demographics`](#source-sweeney-demographics), [`netflix-prize`](#source-netflix-prize), [`aol-4417749`](#source-aol-4417749), [`ccpa-sale-definition`](#source-ccpa-sale-definition), [`cjeu-planet49`](#source-cjeu-planet49), [`edpb-consent-or-pay`](#source-edpb-consent-or-pay), [`pohlmann-first-party-cookies`](#source-pohlmann-first-party-cookies)

**Nine Things People Say** (16): [`aol-4417749`](#source-aol-4417749), [`sweeney-demographics`](#source-sweeney-demographics), [`netflix-prize`](#source-netflix-prize), [`ftc-surveillance-pricing`](#source-ftc-surveillance-pricing), [`ali-ad-delivery`](#source-ali-ad-delivery), [`ftc-gravy-venntel`](#source-ftc-gravy-venntel), [`ftc-mobilewalla`](#source-ftc-mobilewalla), [`penney-chilling`](#source-penney-chilling), [`solove-nothing-to-hide`](#source-solove-nothing-to-hide), [`solove-taxonomy`](#source-solove-taxonomy), [`zuboff-surveillance-capitalism`](#source-zuboff-surveillance-capitalism), [`verizon-dbir`](#source-verizon-dbir), [`garcia-shadow-profiles`](#source-garcia-shadow-profiles), [`phone-number-recycling`](#source-phone-number-recycling), [`ftc-data-brokers-2014`](#source-ftc-data-brokers-2014), [`google-build-profiles`](#source-google-build-profiles)

**One Page Load** (9): [`google-openrtb-guide`](#source-google-openrtb-guide), [`google-cookie-matching`](#source-google-cookie-matching), [`google-build-profiles`](#source-google-build-profiles), [`prebid-bidder-count`](#source-prebid-bidder-count), [`website-wiretap-litigation`](#source-website-wiretap-litigation), [`web-almanac`](#source-web-almanac), [`eff-cover-your-tracks`](#source-eff-cover-your-tracks), [`pohlmann-first-party-cookies`](#source-pohlmann-first-party-cookies), [`ftc-surveillance-pricing`](#source-ftc-surveillance-pricing)

**Receipts** (2): [`web-almanac`](#source-web-almanac), [`swd-emissions-model`](#source-swd-emissions-model)

**Start Here** (3): [`eff-cover-your-tracks`](#source-eff-cover-your-tracks), [`ublock-origin`](#source-ublock-origin), [`themarkup-blacklight`](#source-themarkup-blacklight)

**The Swap Shop** (14): [`posteo`](#source-posteo), [`mailbox-org`](#source-mailbox-org), [`gmail-scanning-2017`](#source-gmail-scanning-2017), [`mullvad`](#source-mullvad), [`mullvad-audit-cure53`](#source-mullvad-audit-cure53), [`ublock-origin`](#source-ublock-origin), [`ublock-origin-chrome`](#source-ublock-origin-chrome), [`signal-usernames`](#source-signal-usernames), [`search-index-concentration`](#source-search-index-concentration), [`codeberg`](#source-codeberg), [`peertube`](#source-peertube), [`mullvad-public-dns`](#source-mullvad-public-dns), [`mullvad-dns-shutdown`](#source-mullvad-dns-shutdown), [`signal-donate`](#source-signal-donate)

**What Leaves Your Browser** (6): [`eckersley-fingerprinting`](#source-eckersley-fingerprinting), [`eff-cover-your-tracks`](#source-eff-cover-your-tracks), [`web-almanac`](#source-web-almanac), [`pohlmann-first-party-cookies`](#source-pohlmann-first-party-cookies), [`ftc-surveillance-pricing`](#source-ftc-surveillance-pricing), [`sweeney-demographics`](#source-sweeney-demographics)

<!-- END GENERATED BIBLIOGRAPHY -->

---

## One thing to do with this page

Pick the claim you find least believable, find it in the list above, and open the source.
If it does not say what this site says it says, that is worth an issue, and the page
changes.

That is the whole test this site sets itself. Everything else here is an attempt to pass
it.
