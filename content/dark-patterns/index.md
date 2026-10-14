+++
title = "The Dark Patterns Field Guide"
subtitle = "Seventeen ways an interface is built to defeat you"
description = "A field guide to deceptive design: what each pattern does, where you meet it, how to spot it, and what the law has actually done about it, including the first DSA fine."
status_as_of = 2026-10-13
weight = 6
nav = "Dark patterns"
sources = [
  "deceptive-design-types",
  "mathur-dark-patterns-2019",
  "brignull-dark-patterns",
  "sludge-audits",
  "dsa-regulation",
  "ec-x-fine-120m",
  "ftc-amazon-25b",
  "amsterdam-court-dsa-2025",
  "ftc-click-to-cancel-rosca",
  "cjeu-planet49",
  "cnil-dark-patterns-quiz"
]
+++

You have almost certainly been manipulated by a piece of interface design today. Not persuaded, *manipulated*, which is a different thing: the interface was arranged so that the option you'd have chosen with full attention is harder to choose than the option that profits someone else.

The term was coined in 2010 by the user-experience designer Harry Brignull, who catalogued these practices and gave them names. {{< cite "brignull-dark-patterns" >}} He has since argued that "dark patterns" is too soft a phrase for what's happening, and now prefers **deceptive design**, because "dark" sounds like an aesthetic, and the practice is a form of deception. This site uses both, with a preference for the accurate one.

A related term is worth knowing, because it covers something the dark-pattern literature often misses. Where a dark pattern manipulates a *decision*, **sludge** is friction placed in the way of a legitimate *action*: the cancellation that requires a phone call, the deletion request that takes six weeks, the form demanding information you have no reason to give. Sludge is often not deceptive at all, which is what makes it slippery: nobody lied to you, the process was simply made expensive enough that you gave up. Researchers have argued the two need auditing together rather than treated as separate problems. {{< cite "sludge-audits" >}}

The useful thing about a field guide is that it converts a vague unease into a checklist. Once you can name *hidden costs* or *confirmshaming*, you stop experiencing them as your own confusion and start recognising them as something done to you. That shift is worth more than any amount of outrage.

---

## The evidence base

This is not a matter of anecdote. In 2019, a team of researchers at Princeton crawled **11,000 shopping websites** and found **1,818 instances of dark patterns across 1,254 of them**, which they sorted into 15 types. That's roughly one in nine of the sites they looked at. {{< cite "mathur-dark-patterns-2019" >}}

Two things about that study matter for how you read this page.

First, it measured *prevalence*, not intent. Some of those 1,818 instances were probably incompetence rather than strategy. But at that scale, the distinction stops being interesting: whatever the intent, the result is an ecosystem where deception is common enough to be a design norm.

Second, and more important, the patterns clustered on the pages where money changes hands. Cart and checkout pages. That's where the effort is concentrated, because that's where the return is.

---

## Why they work

The mechanism is an asymmetry, and it isn't about intelligence.

Every dark pattern trades on the gap between the **effort the designer has invested** and the **attention the visitor has available**. The designer has months, a design system, user research, and A/B testing infrastructure. You have six seconds and a mild intention to buy a train ticket. The pattern doesn't need to fool you in principle: it needs to work on you *once*, in that state, at that moment.

Three consequences follow, and they're the reason this page exists.

**Knowing about them doesn't immunise you.** Experts get caught by these too. Recognising a pattern after the fact is much easier than perceiving it while you're trying to complete a task, which is exactly the state the design is built for.

**They're iterated.** Patterns that work get kept, and patterns that don't get removed and replaced. What you encounter is the survivor of a selection process run at enormous scale: the current best version of the technique.

**They're cheap and lawful by default.** A pre-ticked box costs nothing to implement and, until someone objects, nothing to ship. The default is not neutral; it's whatever the person optimising for revenue last found worked.

---

## The field guide

Organised by what the pattern does to you. The full taxonomy is larger: eighteen types are catalogued at *deceptive.design*, which is the canonical reference and worth bookmarking. {{< cite "deceptive-design-types" >}}

### Sneaking: you agreed to something you weren't told about

**Hidden costs.** The price you were shown is not the price you pay. Fees, service charges and delivery costs appear at the final step, after you've invested enough effort that abandoning feels wasteful.
*The tell:* the total changes between the page where you chose and the page where you pay.
*Where:* ticketing, airlines, food delivery, event booking.

**Hidden subscription.** You believed you were making a one-off purchase and have instead started a recurring charge.
*The tell:* the button said "continue" or "get started" rather than naming a subscription.
*Where:* apps, "free trials," anything with a 14-day window.

**Sneak into basket.** Something you didn't choose is already in your order: insurance, a donation, a warranty, a premium tier.
*The tell:* your total doesn't match what you remember selecting. Check the line items before paying; this pattern depends on you not doing that.

**Disguised ads.** Advertising formatted to look like content, navigation, or a download button. The canonical version is the large green "Download" button that is an advert, sitting above the real, small download link.
*The tell:* ask what the element would look like if it were honest. If the answer is "much less prominent," it's a disguise.

**Currency confusion.** Prices presented in a way that obscures what you're actually committing to: multiple currencies, points instead of money, or a "per week" figure when everything else on the page is monthly.
*The tell:* you have to do arithmetic to know the cost. That arithmetic is the product.

### Obstruction: you decided, and the interface disagrees

**Hard to cancel**, the roach motel. Signing up takes one click; cancelling requires a phone call during business hours, or an account you can't find, or a retention agent with a script. The name comes from the design literature and it's accurate: easy to enter, hard to leave.
*The tell:* time the two actions. If they differ by more than a minute's effort, it's deliberate.

**Obstruction.** Actively impeding a task you've already decided to complete: blocking account deletion, making data export impossible, requiring you to contact support to do something the interface could do.
*The tell:* you're asked to explain yourself. No legitimate service needs a reason for you to leave.

**Nagging.** Repeated interruptions designed to get you to do something: repeated permission requests, repeated prompts to enable notifications, a modal that returns every visit.
*The tell:* the request reappears after a clear refusal. Once is a request; twice is a campaign.

### Forced action: your refusal was pre-empted

**Preselection.** The option that benefits them is already chosen, and you must notice it in order to undo it. This is the pattern with the clearest legal answer in Europe: the Court of Justice ruled in 2019 that a pre-ticked checkbox does not constitute valid consent, because consent requires an active act by the user. {{< cite "cjeu-planet49" >}}
*The tell:* any checkbox, toggle, or radio button that arrives already set, especially in a signup form or a consent banner.

**Forced enrolment.** You cannot complete the thing you came to do without also agreeing to something unrelated, creating an account to read, joining a programme to check out, accepting marketing to use a service.
*The tell:* the exit is blocked by something that has nothing to do with your goal.

**Privacy zuckering.** Being manoeuvred into sharing more than you intended, usually through defaults, ambiguous wording, or a settings flow that makes the private option hardest to find.
*The tell:* the most permissive setting is the one described most warmly.

### Misdirection: the design draws your eye away

**Visual interference.** The option you want is styled to be nearly invisible (grey text, low contrast, small type, positioned away from the main flow) while the option they want is a large filled button. Nothing is hidden. Your attention is simply directed.
*The tell:* squint at the screen. Whatever remains legible is what you're being steered toward.

**Trick wording.** Double negatives, ambiguous buttons ("Unsubscribe" meaning "change preferences"), and labels designed to be misread once.
*The tell:* read the button as if it were a sentence about what will happen next. If you can't tell, that's the finding.

**Comparison prevention.** Making it structurally difficult to compare options: obfuscated pricing units, plans that differ on incomparable axes, a comparison table that omits the cheap option.
*The tell:* the difficulty of the comparison is not a consequence of the products being complex.

**Confirmshaming.** The decline option is written to insult you. "No thanks, I don't want to save money." "I prefer to pay full price." "I don't care about my health."
*The tell:* the refusal is phrased as a character flaw. It's cheap to spot and it remains remarkably effective, which is why it persists.

### Fake: the pressure is manufactured

**Fake urgency.** A countdown timer that resets when you reload. "Offer ends tonight" appearing every night.
*The tell:* reload the page. A real deadline doesn't move.

**Fake scarcity.** "Only 3 left in stock" displayed continuously, regardless of how many are actually left.
*The tell:* the number doesn't change as people buy, and it's rarely more than 5.

**Fake social proof.** Invented activity notifications ("Sarah from Leeds just booked this") generated by a script rather than by Sarah.
*The tell:* the claims are unverifiable by design, which is the point.

### Beyond the checkout

**Addictive design.** Infinite scroll, autoplay, streaks, and variable-reward loops that keep a session going past the point of intention. This is the pattern most often defended as engagement, and the defence is worth examining: engagement measured in time-on-site is not the same as value delivered.
*The tell:* you stopped wanting to continue before you stopped.

## The legal picture, and what it's actually worth

Dark patterns are no longer a gap in the law, which is a genuinely recent change.

The **Digital Services Act** addresses them directly: online platforms are prohibited from designing, organising or operating their interfaces in ways that deceive or manipulate users, or that materially distort or impair their ability to make free and informed decisions. {{< cite "dsa-regulation" >}} The **GDPR** supplies the consent standard (freely given, specific, informed, unambiguous) which is what makes preselection and most consent banners unlawful in Europe to begin with. And in the United States, the FTC pursues these practices under its general authority against unfair and deceptive acts, with the **ROSCA** statute covering negative-option subscriptions specifically.

That last point needs a correction, because a lot of commentary gets it wrong. The FTC's 2024 "click-to-cancel" rule was **struck down by a federal appeals court in 2025**. But the widely repeated conclusion that this left subscription traps legal is false: enforcement continued under ROSCA and the FTC Act, and the agency has kept bringing cases. {{< cite "ftc-click-to-cancel-rosca" >}} A vacated rule is not a repeal of the underlying law, and reporting that treats it as one is its own kind of misdirection.

## Enforcement, in three examples

**X, December 2025: €120 million.** The European Commission's first non-compliance decision under the DSA, concerning dark patterns and transparency failures. Whatever you think of the company, the significance is procedural: the DSA is no longer theoretical. {{< cite "ec-x-fine-120m" >}}

**Amazon, September 2025: $2.5 billion.** A US settlement over allegations that the company had duped millions of customers into enrolling in Prime and made cancellation difficult. Note the mechanism: the harm alleged was the *design of the cancellation flow*, not the product. {{< cite "ftc-amazon-25b" >}}

**An Amsterdam court, 2025.** A Dutch court applied the DSA to find that non-persistent settings, a refusal that doesn't stick, amounted to a dark pattern. {{< cite "amsterdam-court-dsa-2025" >}} This is the most instructive of the three, because it targets the thing users actually experience as madness: you decline, and the next visit asks again as though you hadn't.

---

## Why this page won't tell you it's fixed

The honest conclusion is that recognition has improved faster than the practice has declined.

Regulation is arriving, and it is real: there is now a regulator who will fine a large platform eight figures for interface design. But enforcement is slow, selective, and aimed at the largest platforms, because that's where the resources are. The pattern library on a mid-sized e-commerce site is unlikely to attract a decision from Brussels, and everybody involved knows it.

Meanwhile the techniques are cheap, easily deniable ("a test we were running"), and instantly removable if questioned, which makes them low-risk. The rational move for a company optimising revenue has not changed as much as the law has.

Which is why the useful skill here is not outrage but recognition. Outrage is exhausting and doesn't scale. A checklist does.

---

## What to do

**Take the CNIL's quiz.** The French data protection authority built an interactive exercise in recognising these patterns, and it's a better use of five minutes than reading another article about them. {{< cite "cnil-dark-patterns-quiz" >}}

**Squint test.** On any page asking you to decide something, squint until the text blurs. Whatever is still legible is what the design wants you to click. This sounds like a joke and it works.

**Time your exit.** Before signing up for anything recurring, find the cancellation route. If you can't find it in a minute, that is information about the service, and it's cheaper to learn now than in eleven months.

**Complain where it counts.** In the EU, national consumer authorities and data protection authorities both take these reports. A single complaint rarely changes a design; a pattern of complaints about the same company is how enforcement cases start. It is slow, unglamorous, and one of the few things that actually moves the number.

**And build better.** If you make websites, and some readers of a page like this do, this is the section that matters most. Most dark patterns aren't chosen, they're *defaulted into*: the checkbox that ships pre-ticked because that's how the component was built, the modal that can't be dismissed because nobody wrote the dismissal. Read the field guide above as a code review checklist. It costs you nothing to not do these things, and the cost of doing them is eventually a regulator.

{{< source-list >}}
