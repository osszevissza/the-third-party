# Voice comparison, and the decision that came out of it

**Status: decided, 2026-10-14.** The maintainer's friend, who originated the project,
reviewed both drafts of `/nothing-to-hide/` and agreed with the both-by-purpose
recommendation below. The fork is closed. This file now records the outcome rather than
posing the question, and it is the reference for how the remaining pages should be
written.

---

## The decision

> **Use both shapes, chosen by what the page is for.**
>
> - **B's shape for objection pages**, the ones a reader arrives at with a *doubt*.
>   "I have nothing to hide", the myths page.
> - **A's shape for explanatory pages**, the ones a reader arrives at with a *question*.
>   What leaves your browser, how consent banners work, the one-page-load narrative.

The format follows the job, and the site stops being either an essay collection or a
FAQ. B's shape is not the "winner" and A's is not the loser: they are two registers, and
each page is assigned the one it needs.

### What this means per page

| Page | Register | Why |
|---|---|---|
| `nothing-to-hide/` | **B**, objections | The reader arrives with a doubt, and the doubt has a sentence attached to it |
| `myths/` | **B**, standalone units | Same: a misconception the reader holds, each checkable in a browser |
| `consent-theatre/` | **A**, explanatory | A question about how something works |
| `what-leaves-your-browser/` | **A** | Kept as written |
| `one-page-load/` | **A** | Kept as written, and the ledger is its own fallback |
| `analytics/` | **A**, practical | A question, answered in order |
| `start-here/`, `dark-patterns/` | reference | Lists of records, not arguments |
| `the-rules/` | reference, per instrument | One card per law, status-dated |
| `sources/` | reference | Generated, not argued |

**Three of the pages in this register are history, not a to-do.** `the-rules/` was dropped in
round 11, and `swap-shop/` and `receipts/` were dropped by the maintainer on 2026-10-15,
after discussing the site with the friend who originated the project. The two dropped on
2026-10-15 have been taken off the table above; the `the-rules/` row stays as the record of
what was planned.

Nothing already written has to change shape. The decision settles what shape the
*unwritten* pages take, which is why it mattered enough to wait for.

---

## What the merged page actually does

`/nothing-to-hide/` is now the B shape with A's best material folded in, rather than
either draft unaltered:

- **The AOL set-piece opens the page**, compressed to four short paragraphs. It is the
  single most persuasive passage in either draft, and in B it was buried inside
  objection 2. It now does the work a hook is supposed to do.
- **Nine objections, not eight.** The friend's suggestion added one: your choices carry
  other people's data with them. See below.
- **A short "where this page is wrong" section**, kept because conceding ground in a
  dedicated section is what earns the right to argue, and because B's inline
  concessions were the only place that fairness lived.
- **The phone test** stays where B put it, answering the objection immediately.
- **Solove's distinction** between privacy and secrecy survives from A, in two
  sentences rather than a section.

The old A text is not in the repository any more; it is inside `Archívum.tar.gz` at the
repository root, along with the pre-decision copies of `SITE_PLAN.md`, `index.md` and
this project's earlier review notes.

---

## The ninth objection, and why it was worth adding

The friend's point: *your choices easily affect other people's information, because you
might expose their phone numbers or other personal data, which can lead to fraud
attempts against them or to a loan being refused.*

That is a real gap in both drafts, and it is now objection 6, "It's my data. If I don't
mind, that's the end of it." It is the one argument on the page that survives the
objection it answers, because "I personally don't mind" is not a claim about anyone
else. It cites three sources that did not exist in the file before:

- `garcia-shadow-profiles`: the shadow profile hypothesis, tested on Friendster's
  abandoned data: contact lists contain non-members, and what users disclose predicts
  personal details about people with no account at all.
- `phone-number-recycling`: 259 numbers available to new subscribers at two US
  carriers: 171 still tied to accounts, 100 linked to leaked credentials.
- `ftc-data-brokers-2014`: brokers hold files on almost every US consumer, assembled
  from sources those consumers never dealt with, and those files feed decisions about
  credit, employment, insurance and housing.

**The honest limit:** nobody publishes a count of loans refused because of someone
else's data. The page states the mechanism the sources support and stops there.

---

## A boundary to respect

Draft B and the planned `/myths/` page could easily become the same page written twice.
Keep them apart:

- **`/nothing-to-hide/`** handles **arguments**: "I have nothing to hide", "it's legal",
  "everyone does this". Claims about what follows from the facts.
- **`/myths/`** handles **misconceptions**: "HTTPS means private", "incognito is
  anonymous", "we anonymise your data". Claims about how things technically work, each
  with a 60-second way to check it yourself.

If a section could go on either page, it belongs on `/myths/` when it is falsifiable
with a browser and on `/nothing-to-hide/` when it is not.

---

## Note on the sources

Both drafts cited from the same `data/sources.yaml`, so adopting B's shape and folding in
A's material cost nothing in citation work. The merged page declares 15 sources, all of
them cited inline. Three sources in the file still carry no verified live URL (Solove's
2006 taxonomy, the EDPB opinion on consent-or-pay, and now the 2014 FTC data broker
report, whose domain blanket-blocks automated checks); `python3 scripts/check-content.py`
reports all of this as warnings. The convention for the last one is the one to copy: the
entry keeps `verified_on: null` with a comment saying so, and carries an `archive:` link,
because the archived copy is what was actually read.
