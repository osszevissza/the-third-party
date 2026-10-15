+++
title = "One Page Load"
subtitle = "Follow a single page view from your browser into the ad auction"
description = "A timed reconstruction of what leaves a browser during one ordinary page load, built from the ad industry's own documentation, and ending with the same page done differently."
status_as_of = 2026-10-13
weight = 3
nav = "One page load"
sources = [
  "google-openrtb-guide",
  "google-cookie-matching",
  "google-build-profiles",
  "prebid-bidder-count",
  "website-wiretap-litigation",
  "web-almanac",
  "eff-cover-your-tracks",
  "pohlmann-first-party-cookies",
  "ftc-surveillance-pricing"
]
+++

You opened a page. You didn't type anything, log in, click anything, or agree to anything. You just arrived, and the page loaded.

What follows is a reconstruction of what happens next on a typical commercial site, the kind with advertising, analytics, and a social embed or two. It is not a capture of your session; this page has no idea who you are and collects nothing. It's assembled from the published documentation of the systems involved, which is the useful part: none of this is secret, and most of it is described by the companies doing it, in their own developer guides, to the people they're selling to.

Timings are illustrative. The order and the mechanics are not.

---

## The ledger

### `t+0 ms`: you press enter

The browser resolves the domain name and opens an encrypted connection. Your internet provider can see which hostname you're connecting to, even though the content itself is encrypted. If you're on someone else's network, so can they.

### `t+40 ms`: the request leaves

The first HTTP request carries, at minimum:

- **your IP address**: the connection cannot be completed without it, and it's usually stable for months and linked to a physical household
- **a User-Agent string** identifying your browser, version, and operating system
- **Accept-Language**, telling the server which languages you read
- **a Referer header**, naming the page that sent you here

None of that requires a cookie, an account, or your permission. It's the baseline cost of loading a web page.

### `t+120 ms`: the page starts arriving, and you get a name

The server responds with HTML, and sets a **first-party cookie**: an identifier for you. Not you personally. A number that is now yours for as long as the cookie survives, and which the site can attach things to.

This part is ordinary and, in isolation, not sinister. The problem starts when the number can be matched to a number held by somebody else, which is the rest of this page.

### `t+150 ms`: a third party is contacted before you've seen anything

The page asks for its fonts. If they're served from a third-party CDN, then before a single word renders, your IP address and User-Agent have been sent to a company you never chose to do business with and cannot see listed anywhere on the page.

This is the cheapest fix on the whole web: it takes about fifteen minutes to self-host a font file, and every one of those requests stops. Almost nobody does it.

### `t+180 ms`: the measurement layer

An analytics script loads and runs. It reads its own cookie, checks your viewport size and screen resolution, and beacons the result back. If the site uses Google Analytics with Consent Mode, some form of this fires even when a visitor has declined (a reduced event carrying a consent state rather than identifying data).

### `t+210 ms`: the consent layer, which is also a third party

A consent management script loads to ask whether you agree to the other scripts. It is frequently provided by a third party as well, and it runs before you have answered anything (necessarily, since it has to exist in order to ask).

Check who loads on a site you use and you will often find that the mechanism for obtaining your consent is itself an addition to the list of companies receiving your data.

### `t+240 ms`: the ad slot calls home

This is the pivot. An element on the page asks an ad server for something to display. What comes back is not usually an advertisement. It's a **tag**, a small piece of code that instructs the browser to go and ask several other companies for an advertisement instead.

Those companies each return their own tags. The chain is known in the industry as a daisy chain, and it's the reason a single ad slot can produce dozens of requests to companies that appear nowhere on the site's privacy policy.

### `t+300 ms`: the IDs are reconciled

Before anyone bids, the participants need to agree on who you are. Your identifier from one system is matched to the identifier from another through a process called cookie syncing, or cookie matching.

Google documents this plainly for its own ad system: cookie matching "allows you to link your user ID to a corresponding Google User ID for more effective bidding and user list construction," using match tables that "map IDs between domains." {{< cite "google-cookie-matching" >}}

Read that twice. It is an official developer guide describing how to reconcile two separate identities belonging to the same person across two separate companies. That matching is what turns a pile of unconnected cookies into a profile.

### `t+320 ms`: the bid request goes out

Now the page's advertising slot is auctioned, and the auction happens by broadcast. A **bid request** is sent simultaneously to everyone who might want to buy your attention.

Publishers typically work with around ten bidders per auction. The number is an industry rule of thumb, and Prebid, the main open-source header-bidding library, has published A/B testing on the revenue-versus-latency trade-off of adding more. {{< cite "prebid-bidder-count" >}} Ten bidders per slot, several slots per page, on every page you visit.

### `t+340 ms`: what the bid request contains

This is the part worth reading slowly, because it's where the word *broadcast* stops being a metaphor.

Google's own OpenRTB integration guide describes the structure of a bid request: a `BidRequest` object containing `Device`, `User`, and `Geo` objects "with their attributes and Google-specific extensions." The `Geo` object is described as coarse device location **approximated from your IP address**. {{< cite "google-openrtb-guide" >}}

And then there is a page in Google's Authorized Buyers documentation titled **"Use bid requests to build user profiles."** Its first sentence defines the term:

> A user profile is a mapping of a user identifier, such as the Google User ID included in `BidRequest.user.id`, to information about the user that you can use for bidding with interest-based ads or remarketing with user lists.

That is Google, in its own developer documentation, describing the construction of profiles about people out of the contents of bid requests, and naming the identifier field that carries the link. {{< cite "google-build-profiles" >}}

It is not a privacy campaign's characterisation of the ad industry. It is the ad industry's own documentation, telling its customers what bid requests are for.

Put the two facts together. The request carries a location derived from your IP, a device description, and whatever identifiers can be attached, and it is transmitted, in the clear, to every bidder at once. There is no recipient list, because the mechanism has no concept of one. You cannot agree to something sent to an unenumerated set of recipients.

### `t+450 ms`: the auction clears

The whole auction resolves in well under a second, comfortably before you've finished reading the headline. The winner's creative is rendered into the slot, and a set of tracking pixels fires: impression counted, audience segment attached, any prior campaign's conversion credited.

### `t+600 ms`: the session recorder starts

On many commercial sites, a session-replay script now begins capturing what you do: where you move, where you hesitate, how far you scroll, and in some configurations what you type into fields before submitting.

This technique has generated a substantial body of litigation in the United States on its own: claims brought under wiretapping statutes, particularly where tracking technology ran on healthcare websites and captured information that other laws specifically protect. {{< cite "website-wiretap-litigation" >}}

### `t+900 ms`: the embeds wake up

A video player, a social widget, a map, a comment system. Each is a third party with its own cookies, its own scripts, and its own reason to phone home. In each case, the company receives a request from your browser before you have shown any interest in what it provides.

### `t+1200 ms`: you still haven't clicked anything

Everything above happened because you loaded a page. That's the whole input.

---

## The shape of it

{{< diagram "one-page-load" "The request graph of one page load. One request leaves your browser and at least nine companies receive one: the site, the measurement layer, the consent vendor, the ad server, and five bidders. The five-bidder figure is the industry rule of thumb the page cites; the structure is from Google's own ad documentation." >}}

## What the same page looks like done properly

Now the other version, because a page like this has an obligation to show its work.

A site built to avoid this sends **zero third-party requests**. It serves its own fonts. It embeds nothing, or defers embeds behind a click. It measures with a tool that counts page views without identifying anybody, or reads its own server logs, which require no JavaScript at all and cannot be blocked.

The result is a page that is faster, lighter, and cheaper to run, that needs no consent banner because there is nothing to consent to, and that you can verify with your browser's Network panel in about a minute.

{{< diagram "two-page-loads" "The same page in two versions. The left column lists the companies a page contacts when it is built for extraction; the right lists what a self-contained page contacts, which is itself. The left is a composite of the practices this page documents rather than a count taken on any single site." >}}

There is no trade-off being made here except effort. Nobody who visits such a site notices anything missing, because the only things removed are the things that were only ever for someone else's benefit.

You can run the comparison yourself: open the developer tools, switch to the Network panel, and count requests to domains other than the one in the address bar. Then do it on this site. The number is the argument, and it's better than mine.

---

## The honest part

Three qualifications, because a reconstruction presented as fact would be its own kind of deception.

**This is a general picture, not a measurement of you.** Real sites vary enormously. Some run a fraction of the above. Some run considerably more. The HTTP Archive's Web Almanac measures page composition annually and is the place to check current figures rather than trusting a number quoted in an article. {{< cite "web-almanac" >}}

**The order is approximate, and the timings are illustrative.** Network conditions, caching, and implementation differ. The *mechanics* (the header contents, the tag chain, the broadcast, the matching) are documented and stable.

**Several of the mechanisms above exist for defensible reasons.** Geotargeting lets a local business avoid paying to advertise to people four hundred miles away. Fraud detection genuinely needs device signals. Frequency capping protects you from seeing the same advert forty times. The hostile part is not any individual mechanism; it is that they run by default, at scale, without your knowledge, and that the resulting profiles are used for purposes that were never disclosed, including individualised pricing, which the US Federal Trade Commission has documented as drawing on personal data with no connection to the transaction. {{< cite "ftc-surveillance-pricing" >}}

And the fingerprint is still there underneath all of it. If you cleared your cookies and came back, the identifiers above would be reconstructed from your device's configuration, which you carry with you and cannot delete. {{< cite "eff-cover-your-tracks" >}} {{< cite "pohlmann-first-party-cookies" >}}

---

## What to do

**Watch it happen on a real site.** Open the Network panel, filter to third-party domains, and reload something commercial. You will see the tag chain fire in real time, in order, and it is considerably more convincing than reading about it.

**Then look at the clock in the timeline.** Everything in the ledger above completes while you are still deciding whether to read the article.

**And if you run a site:** this ledger is a specification for what not to do. Start with the fonts: one change, fifteen minutes, and it removes a third party from every page load you will ever serve. [Start Here](/start-here/) has a shorter ladder aimed at people who run a site, with the effort priced on every rung, and [the analytics page](/analytics/) covers the measurement question specifically.

{{< source-list >}}
