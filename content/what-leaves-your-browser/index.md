+++
title = "What Leaves Your Browser"
subtitle = "Three kinds of information, and the one that actually matters"
description = "A page load sends far more than you typed. This is what goes, in what order, and why the deductions drawn from it are a bigger problem than the collection itself."
status_as_of = 2026-10-13
weight = 3
nav = "What leaves your browser"
sources = [
  "eckersley-fingerprinting",
  "eff-cover-your-tracks",
  "web-almanac",
  "pohlmann-first-party-cookies",
  "ftc-surveillance-pricing",
  "sweeney-demographics"
]
+++

A page takes about a second to load. In that second (before you type anything, log in, click anything, or agree to anything), a request has already left your device carrying a numeric address that identifies your network, a string describing your browser and operating system, the address of the page that sent you there, and whatever your browser volunteered about its own screen, language, timezone, and capabilities.

That is before any cookie. Before any account. Before you have been asked anything, because you have not been asked yet.

Most explanations of this subject start with cookies, which is a bit like explaining air travel by starting with the peanuts. Cookies are real and they matter, but they're a mechanism. The interesting question is what the information *is*, and what happens to it after it arrives, and for that it helps to separate three things that get discussed as though they were one.

{{< diagram "three-buckets" "The page in one picture: the first two buckets are what a request carries, and what the systems actually use is the conclusion drawn from them, which is bucket three." >}}

## Bucket one: what you hand over

This is the part everyone thinks about, and it is the least interesting.

When you fill in a form, sign in, type into a search box, or upload a file, you have knowingly given something to somebody. It is *deliberate*, it is *legible*, and you have a reasonable intuition about what it contains. Even when the terms are lopsided (you did not read them, and they know you did not read them), the transaction is at least visible to you. You know a transaction happened.

Nothing in this bucket is the problem. It is the thing people picture when they hear "data collection," and because it is the thing they picture, the defences they adopt are aimed here. Use a pseudonym. Don't fill that in. Log out.

## Bucket two: what is observed

This is the bucket that does the actual work, and almost none of it is something you chose.

Some of it is unavoidable. **Your IP address** is the clearest case: the connection cannot be made without it, because the network needs to know where to send the reply. It is also, in most residential cases, stable for long periods and trivially linked to a physical household. You cannot opt out of having one. You can only change who sees it, using something in between.

Some of it is volunteered by your software. Every request carries a **user agent** string naming your browser and operating system, and a **referrer** telling the destination which page sent you. Those exist for legitimate reasons: servers use them to serve the right version of a page, sites use them to understand their traffic. They also narrow you down.

And then there's **the fingerprint surface**, which is the part that surprises people. Your browser will happily report, on request:

- your screen's resolution and colour depth
- your timezone and language settings
- which fonts are installed
- how your graphics hardware renders a specific image, via canvas and WebGL
- how your audio stack processes a tone
- how many processor cores you have, and how much memory
- a list of attached media devices
- and a long tail of smaller signals, from the exact build of your browser to whether your device reports a battery

None of these is unusual. That's precisely the point.

Think of how you'd describe a stranger in a small town: tall, wears glasses, has a dog, drives a blue car. Every one of those details is common. The *combination* describes exactly one person, and it does so without a name.

That is what a browser fingerprint is. And the mechanism is neither new nor sophisticated: in 2000, Latanya Sweeney showed that three ordinary fields (five-digit ZIP code, date of birth, and sex) were enough to single out an estimated 87% of the United States population. {{< cite "sweeney-demographics" >}} A browser fingerprint is the same trick with more fields and no consent form.

Peter Eckersley's 2010 study at the Electronic Frontier Foundation demonstrated it directly in the browser: the large majority of browsers in his sample could be singled out from their configuration alone, with no cookie involved and nothing stored on the machine. {{< cite "eckersley-fingerprinting" >}} You have been carrying an identifier this whole time. It just isn't stored anywhere you can delete it.

## Bucket three: what is deduced

Here is the correction that matters most, and it is the one that most explanations skip.

The observations in bucket two are **raw material**. What gets used is not the raw material. What gets used is the *conclusion*.

Nobody needs your screen resolution, your font list, or the fact that you visited a page about a medical condition. They need the answer to a question they never had to ask you: is this person likely to be in debt? Pregnant? Looking for work? Sleeping badly? About to move house? Recently separated? The industry term is inference, and the commercial value of personal data sits almost entirely here rather than in the observations.

In January 2025, the US Federal Trade Commission published findings from a study of what it calls surveillance pricing, reporting that firms were drawing on a wide range of personal data (including data with no connection to the transaction at hand) to set individualised prices. {{< cite "ftc-surveillance-pricing" >}} Feeding a font list in and getting a price out is not an intuitive relationship. That gap is where "it's only what my browser reports" stops being reassuring.

Three properties of inference make it harder to deal with than collection:

**It cannot be deleted.** You can delete a row. You cannot delete a conclusion someone has drawn from it: the conclusion now lives in a statistical model, not a database, and may be indistinguishable from a general pattern that was never about you specifically. Deleting the input does not un-train the output.

**It can be wrong, and there is no appeal.** A deduction about your health, finances, or intentions can be confidently false. You will usually never learn that it was made, let alone be able to dispute it. An observation can at least be checked against reality; a probability cannot.

**It generalises to people who did nothing.** A model trained on people like you makes claims about you. You do not have to have visited anything, searched anything, or done anything at all for a prediction to be attached to your file, because the prediction is about your *category*.

## Why clearing your cookies doesn't fix this

This is where the practical advice most people have received quietly stops working.

Cookies are a storage mechanism with a well-known limitation: the user can delete them. That limitation is exactly why the industry spent two decades building ways around it. Three are worth knowing:

**Fingerprinting, by design, defeats deletion.** A fingerprint's whole purpose is to recognise a returning visitor without storing anything on their machine. Clear your cookies and you are still, to the server, the same arrangement of screen, fonts, and rendering quirks you were yesterday. A new cookie gets issued and attached to the old profile. The deletion is real; the forgetting is not.

**Tracking has moved inside the first-party domain.** A request to `metrics.example-news.com` looks internal; it sits under the same domain as the page you are reading, so it inherits the trust and, in several browsers, the cookie rules of the site itself. Researchers have documented the widespread use of this technique, known as CNAME cloaking, to make third-party tracking present as first-party. {{< cite "pohlmann-first-party-cookies" >}} Your blocker's blocklist has to work harder to notice it.

**Tracking has moved off the browser entirely.** The most direct answer to ad blockers is not to use the browser. Server-side tracking sends events from the website's own infrastructure straight to the advertising platform, with no script in the page for a blocker to stop. This is now standard, well-documented practice rather than an exotic workaround.

The aggregate picture (how many third-party requests a typical page makes, and how that has changed over time) is measured annually by the HTTP Archive's Web Almanac, which is the best available public dataset for this and worth checking for current figures rather than trusting any number quoted second-hand, including in this sentence. {{< cite "web-almanac" >}}

## The retention asymmetry

One more property, because it explains why the problem feels unfixable even when you're doing everything right.

A cookie has an expiry date. Even a long one. **A profile does not.** The identifier is a handle; the record behind it persists on the collector's side, and it can be rebuilt, merged, or re-matched later. Clearing your browser removes your copy of the handle. It does not remove their copy of the file, and it never did.

This is the structural reason that privacy advice framed as deletion keeps disappointing people. Deletion is a request. Whether it is honoured depends on somebody else's incentives, and on whether the thing being deleted is even the thing that matters. The conclusions were never stored in your browser to begin with.

## Where the sceptics have a point

It would be dishonest to present all of bucket two as hostile, because most of those signals exist for reasons that are entirely legitimate.

A server genuinely needs your IP address to reply to you. Screen size and language exist so that pages lay out correctly and render in a language you read. The user agent exists so servers can serve a compatible version of a page; it is a fossil of the era when browsers disagreed violently about everything. Canvas and WebGL exist to draw things.

The hostility is not in any individual signal. It is in **the combination, the retention, and the join**, in assembling signals that were each collected for a narrow, reasonable purpose into a persistent profile that serves a completely different one.

This distinction matters practically, not just rhetorically, because it's the difference between a defensible position and an absolutist one. "Stop collecting altogether" is a demand nobody will meet, and it makes the whole argument easy to dismiss. "Each of these has a purpose, and the purpose is not this" is much harder to argue with, and it points directly at the interventions that would work: shorter retention, no joining across contexts, and disclosure of what was deduced rather than only what was collected.

## What to do

**Measure your own page load.** This is the single most useful thing on this page, and it takes about a minute. Open any news site, open your browser's developer tools, switch to the Network panel, and reload. Count how many requests went to a domain other than the one in the address bar. Then do the same on this site. The number is the whole argument, and it's yours rather than mine.

**Then find out what you look like without a cookie.** EFF's *Cover Your Tracks* shows you the fingerprint your browser presents and whether it is distinctive enough to single you out. It runs locally, shows you what it found, and requires no account. {{< cite "eff-cover-your-tracks" >}} Run it twice: once in your normal window, once in a private one. The comparison is more instructive than any explanation, because it shows you what survives the thing you were told to do.

**Then stop thinking about it as deletion.** You are not trying to remove a file. You are trying to reduce the number of places where a copy exists, and to make the copies that do exist less joinable. That reframing points at different tools: fewer sites that collect anything, more separation between contexts, and, for the case where you genuinely need to not be recognised, an actual anonymity network rather than a private browser window.

And if you can name the inference about you that would actually cost you something, you already know which of those is worth your afternoon.

{{< source-list >}}
