+++
title = "Seven Things That Aren't True"
subtitle = "Misconceptions about how the web works, each with a way to check it yourself"
description = "Privacy advice is full of comforting half-truths. Here are seven, with what's actually the case and a way to verify it in a browser rather than taking my word for it."
status_as_of = 2026-10-13
weight = 5
nav = "Myths"
sources = [
  "eckersley-fingerprinting",
  "eff-cover-your-tracks",
  "themarkup-blacklight",
  "ecc-encrypted-client-hello",
  "google-incognito-settlement",
  "sweeney-demographics",
  "netflix-prize",
  "aol-4417749",
  "ccpa-sale-definition",
  "cjeu-planet49",
  "edpb-consent-or-pay",
  "pohlmann-first-party-cookies"
]
+++

<!-- STRUCTURE NOTE (remove before publishing):
     Each myth below is a repeating record: claim / reality / check. When the Hugo
     layouts are built, these units move to data/myths.yaml and this page renders them,
     so the same data can also drive the filter on /dark-patterns/. The prose in the
     intro and closing sections stays in this file. -->

Privacy advice is full of sentences that are almost true, which is worse than being false, because almost-true things survive scrutiny long enough to become habits. Each myth below comes with a way to check it in a browser rather than taking my word for it. Where a check needs more than a minute, I've said so.

---

## "HTTPS means the site can't see what I do."

**What's actually true.** TLS encrypts the connection *between* you and the site you're visiting. It stops the person on the café wi-fi, your network operator, and anyone else on the path from reading or altering what passes along it. That is a genuine and enormous improvement over the web of fifteen years ago.

It does nothing whatsoever about the destination. The site is at the other end of the encrypted pipe. That is the entire point of connecting to it. Everything you do on a page is visible to that page: what you read, what you hover over, how far you scroll, how long you linger, what you type before deleting it. HTTPS protects the journey. It says nothing about the arrival.

One genuine wrinkle used to be that the *hostname* you were visiting leaked even over HTTPS. Encrypted Client Hello is the fix, though recent research argues the fix is partial, because it depends on an ecosystem centralised enough to reintroduce the leak in other ways. {{< cite "ecc-encrypted-client-hello" >}}

**Check it yourself (60 seconds).** Open the Network panel in developer tools on any HTTPS site you're signed into, and reload. Every request is now encrypted, and look how many of them are going somewhere other than the domain in the address bar. Better connections did not reduce the number of destinations.

---

## "Incognito mode makes me anonymous."

**What's actually true.** A private window does three specific things: it doesn't save your history locally, it starts without the cookies from your normal session, and it discards everything when you close the window. All three are useful, and none of them is anonymity.

It does not change your IP address. It does not hide your traffic from your employer, your school, or your internet provider. From their side, a private window and a normal one are indistinguishable. And it does nothing about fingerprinting, which was designed precisely to work without stored state. {{< cite "eckersley-fingerprinting" >}}

The gap between what private browsing does and what people believe it does is large enough that it became a lawsuit: in 2024 Google settled a case over how it described incognito mode and agreed to delete billions of records collected from private sessions. {{< cite "google-incognito-settlement" >}}

**Check it yourself (60 seconds).** Run *Cover Your Tracks* twice, once in a normal window and once in a private one. Compare the fingerprints. This is the most instructive minute on this page, because it shows you directly what survives the thing you were told to do. {{< cite "eff-cover-your-tracks" >}}

---

## "They anonymise the data, so it doesn't matter."

**What's actually true.** Anonymisation describes a property of a dataset at a moment in time. It is not a guarantee, and it does not survive contact with other datasets.

In 2000, Latanya Sweeney showed that three ordinary fields (five-digit ZIP code, date of birth, and sex) were enough to single out an estimated 87% of the US population. {{< cite "sweeney-demographics" >}} In 2006, AOL published a research dataset it believed was anonymous: roughly 20 million search queries from about 658,000 users, each replaced by a number. Reporters identified one of those users within days, from the content of her searches alone. {{< cite "aol-4417749" >}} In 2006 Netflix released 100 million "anonymised" ratings for a public competition; two years later researchers re-identified substantial numbers of people in it by cross-referencing public reviews on another site entirely. {{< cite "netflix-prize" >}}

The pattern is consistent. Anonymity is broken not by attacking the dataset but by *joining* it to something else: often something that didn't exist, or wasn't public, when the promise was made.

**Check it yourself (2 minutes).** There's no browser test for this one. Instead, read any privacy policy paragraph containing the word "anonymised" and look for a description of *how*. The absence of a method is the informative part: a claim you cannot evaluate is not a reassurance, it's a mood.

---

## "We don't sell your data."

**What's actually true.** This is frequently true in the narrow sense and empty in the useful one. The phrase is doing the work of narrowing "sell" to "exchange for money," which is not how personal data moves.

Under California's privacy law, the definition of a sale is drawn wide enough that *sharing* personal information for cross-context behavioural advertising can be covered even when no money changes hands. {{< cite "ccpa-sale-definition" >}} And in real-time bidding, the details of your visit are broadcast to a large number of companies within milliseconds in order to solicit bids. Whether that is a "sale" is a legal question. That it is a disclosure to strangers is not.

**Check it yourself (30 seconds).** Scroll to the footer of a site that claims not to sell your data. If it carries a link reading "Do Not Sell or Share My Personal Information," that link is legally required in California only of businesses that sell or share personal information. The presence of the opt-out is the admission.

---

## "I clicked 'Accept all', so I had a choice."

**What's actually true.** Having a button is not the same as having a choice, and European law is unusually explicit about this. Valid consent must be freely given, specific, informed, and unambiguous, and the Court of Justice ruled in 2019 that a pre-ticked checkbox does not qualify, because consent requires an active act by the user. {{< cite "cjeu-planet49" >}}

Regulators have since found widespread failures in the design of consent banners, and the harder question (whether "consent, or pay us" constitutes a genuine choice at all) was the subject of a formal opinion from the European Data Protection Board in 2024. {{< cite "edpb-consent-or-pay" >}}

**Check it yourself (60 seconds).** Find a site with a consent banner and don't touch anything. Now locate the option that is not "accept," and time how long it takes you and how many clicks it costs. Then note that the design is not an accident: it was prototyped, A/B tested, and shipped, and the friction was the feature.

---

## "Blocking cookies stops the tracking."

**What's actually true.** Blocking cookies stops *cookie-based* tracking, which is one of at least three mechanisms in current use.

Fingerprinting exists precisely to recognise you without storing anything on your device, so there is nothing for a blocker to delete. {{< cite "eckersley-fingerprinting" >}} CNAME cloaking puts the tracking request on a subdomain of the site's own domain, so it arrives looking first-party and inherits the trust and cookie rules of the first party. {{< cite "pohlmann-first-party-cookies" >}} And server-side tracking moves the reporting off the browser completely, sending events from the site's own infrastructure to the advertising platform, where no extension can observe them.

**Check it yourself (2 minutes).** With your blocker enabled, open the Network panel on a content-heavy site and look for requests to a subdomain of that site's own domain which return almost no content. A first-party request that exists only to report is the signature.

---

## "They say they take privacy seriously."

**What's actually true.** That sentence is not a standard, a certification, or a regulated claim. There is no body that audits it and no consequence for being wrong about it, which is why it appears comfortably on sites carrying hundreds of trackers. Reading a privacy policy is worth doing, but it is a poor use of your first thirty seconds, because the policy is written by the party you are trying to evaluate.

The informative move is to **count instead of read.** Measurement is cheap now, and it does not depend on anyone's self-description.

**Check it yourself (60 seconds).** Run The Markup's *Blacklight* on a site you trust. It reports the specific techniques in use (trackers, session recording, fingerprinting, ad targeting) on the page as it actually is. {{< cite "themarkup-blacklight" >}}

---

## What the seven have in common

Each one is a *mechanism* being mistaken for a *solution*.

Encryption is a mechanism for protecting data in transit. A private window is a mechanism for not saving things locally. A button is a mechanism for recording a decision. A blocklist is a mechanism for matching known patterns. A sentence is a mechanism for persuading you. Every one of them is real, and every one of them solves a narrower problem than the one you're worried about.

That's not an argument against using them. A blocker and a private window are both worth having. It's an argument against treating any of them as *settled*, as the thing you did once, after which the question is closed.

The distinction is worth holding on to, and it generalises: **the reassuring sentence about a mechanism is not evidence the mechanism addresses your problem.** The only way to know what's happening is to look, which is why every item above ends with something you can run rather than something you should believe.

If you've arrived here with an *argument* rather than a misconception ("I have nothing to hide," "it's all legal," "everyone does this"), those are addressed on [a different page](/nothing-to-hide/), because they're claims about what follows from the facts rather than claims about how the facts work. Both kinds of doubt are reasonable. They just need different answers.

{{< source-list >}}
