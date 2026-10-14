# For review: the ethical web project

Hello. This is a summary of where the project has got to, and what happened after the
last round of review.

---

## Outcome of the review, 2026-10-14

You agreed with the both-by-purpose recommendation, so the voice question is closed:

- **Objection pages take Draft B's shape.** `/nothing-to-hide/` and `/myths/`.
- **Explanatory pages keep Draft A's register.** `/what-leaves-your-browser/`,
  `/one-page-load/`, `/consent-theatre/` when it is written.

`/nothing-to-hide/` was then rebuilt as the B shape with the strongest parts of A folded
in, rather than one draft simply replacing the other:

- It opens on the AOL re-identification, which is the best passage in either draft and
  was buried inside an objection in B.
- It answers **nine** objections instead of eight, because your suggestion about other
  people's data was a real gap. See below.
- It keeps a short "where this page is wrong" section, because conceding ground in a
  named section is what earns the right to argue.

The full record, including the per-page register for everything still unwritten, is in
`drafts/README.md`.

---

## Your point, and what it turned into

You suggested that the "nothing to hide" argument misses how easily your choices affect
*other people's* information: exposing their phone numbers and other personal data, and
with it the risk of fraud against them, or a loan refused in their name.

That is now objection 6, headed **"It's my data. If I don't mind, that's the end of
it."** Three sources were added to carry it, and each is a primary source:

- A 2017 study in *Science Advances* that tested the shadow profile hypothesis on
  Friendster's abandoned data: the contact lists users uploaded contained non-members,
  and what those users disclosed predicted personal details about people who had no
  account at all.
- A 2021 study of 259 phone numbers available to new subscribers at two US carriers: 171
  were still tied to accounts at popular websites, and 100 were linked to credentials
  that had already leaked. Most also produced hits on people-search services, which
  publish names, addresses and relatives.
- The FTC's 2014 study of nine data brokers: files on almost every US consumer,
  assembled from sources those consumers never dealt with, feeding decisions about
  credit, employment, insurance and housing.

**One thing it does not claim**, deliberately: nobody publishes a count of loans refused
because of someone else's data. The page states the mechanism the sources support and
stops there, which is the same discipline that kept the fingerprinting percentage off
the site.

---

## What this is

An informative website about the ethics of the web. Not "ethical tech" in general, but
the specific slice you can point a browser at: what a page load actually sends, how dark
patterns are designed, what the law does and doesn't cover, and what the alternatives
cost.

The aim is advocacy people actually finish reading. That means no lectures, no purity
tests, and every claim checkable. The site is being built to *pass its own test*: no
trackers, no third-party requests, no cookie banner, and a page publishing its own
measured numbers.

**Working title:** *The Third Party*. It carries both meanings at once: third-party
scripts, and the uninvited third party in the room.

---

## Where it's got to

**Nine pages written and sourced**, about 23,000 words, plus the two drafts kept as the
record of the voice decision.

| Page | What it does |
|---|---|
| **Nine Things People Say** | Takes the most common objections seriously and answers nine of them |
| **What Leaves Your Browser** | Three buckets: what you hand over, what's observed, what's deduced |
| **One Page Load** | One page view, followed from the browser into the ad auction |
| **Seven Things That Aren't True** | Myths about HTTPS, incognito, "we anonymise your data", each with a way to check it yourself |
| **The Dark Patterns Field Guide** | 17 deceptive patterns, with the legal hook for each |
| **The Swap Shop** | Eight substitutions, each with the honest price of switching |
| **You Don't Need Google Analytics** | The practical page for anyone who runs a site |
| **Start Here** | Two action ladders, and a list of what the site *won't* ask you to do |
| **Sources** | The methodology, the annotated bibliography, and the gaps stated as gaps |

Behind them: **61 sources**, each with full bibliographic detail, a note on what it is
weak at, and a link. A script checks every URL over the network, so "the sources are
real" is a checked claim rather than an assertion, and another script writes the
bibliography page from the same data, so the two cannot disagree.

---

## A sample of what's holding up well

**From the myths page**, on "we don't sell your data": *scroll to the footer and look for
a link reading "Do Not Sell or Share My Personal Information." In California that link is
legally required only of businesses that do. The presence of the opt-out is the
admission.* Thirty seconds, no technical skill, and it can't really be argued with.

**From the analytics page**, the honest caveat that *cookieless is not consent-free*.
Using a privacy-friendly tool doesn't automatically exempt you from consent law; that
depends on jurisdiction and configuration. A site complaining about hidden disclosures
has no business creating one.

**From the action ladders**, a section headed **"What this site won't ask you to do"**:
delete your accounts, stop using the web, be consistent, care about all of it, become an
expert, feel guilty. Written because the honest answer to "should I care about all of
this?" is *no, not all of it*. Pick one thing.

---

## What's honest about the gaps

- **Archiving has started but is not done.** Ideally every source is snapshotted to the
  Wayback Machine before publishing. Three of the 61 now carry archive links, because
  those are the ones added this round. The other 58 are still `null`, and it remains the
  largest gap between what the site claims and what it has done.
- **Two sources still need locating.** Solove's 2006 taxonomy and an EU data protection
  opinion. Both are cited correctly; the official URLs haven't been found, so they are
  flagged rather than guessed at. A third, the FTC's 2014 data broker report, sits on a
  domain that reserves judgement: its link cannot be verified automatically, so the
  entry says so and points at the archived copy that was actually read.
- **Nothing is built yet.** These are content files. The Hugo site, the design, and the
  interactive pieces come after the writing is settled.
- **Legal pages date fastest.** "The Rules" will need a status date on every claim, and a
  maintenance plan.

---

## What's next

Four of the thirteen core pages remain: the home page, **Consent Theatre**, **The
Rules**, and **Receipts**.

**`/sources/` is written**, and it is the page the project has been promising since the
first round: how sources are chosen, what "verified" does and does not mean, the archive
gap stated as a failure, a conflict-of-interest statement, how to report an error, and
then the whole annotated bibliography generated from the citation file, with the reverse
index of which page rests on what. It is long, because a bibliography is, and the prose
part at the top is the part worth reading.

Next up is **Consent Theatre**, which needs the EDPB's cookie banner taskforce report
located and verified before a word of it is written.

---

## What would help most

1. **Read the merged `/nothing-to-hide/`** and say whether the mix reads as one page
   rather than two. It is the page most likely to be judged by someone sceptical.
2. **The ninth objection**: does it land the way you meant it to, and is there another
   consequence of the same kind that belongs beside it?
3. **Anything obviously missing still.** You had the original idea; there may be an angle
   the site should carry that isn't in the plan.
