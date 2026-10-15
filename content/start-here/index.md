+++
title = "Start Here"
subtitle = "One step, in any order, and then permission to stop"
description = "How to read this site if you have ten minutes, an hour, or an afternoon, plus two ladders of concrete actions, with honest cost estimates for each rung."
status_as_of = 2026-10-13
weight = 2
nav = "Start here"
sources = [
  "eff-cover-your-tracks",
  "ublock-origin",
  "themarkup-blacklight"
]
+++

This site argues that the web you use is not quite the web you think you're using, and that the difference is measurable rather than a matter of opinion. It is not a demand that you change your life. It's a set of explanations, each of which ends with something you could do about it, and none of which requires you to do anything.

If you take one thing from this page, take this: **the honest answer to "should I care about all of this?" is no, not all of it.** Pick one thing. That's the design.

## How to read this site

<div class="panel">
**If you have ten minutes.** Read [Seven Things That Aren't True](/myths/). It's the fastest route to the point, because each item ends with something you can check in a browser rather than something you have to believe. If you only have sixty seconds, run EFF's *Cover Your Tracks* in your normal window and then in a private one, and compare. {{< cite "eff-cover-your-tracks" >}}

**If you have an hour.** Read [What Leaves Your Browser](/what-leaves-your-browser/) and then [I Have Nothing to Hide](/nothing-to-hide/). The first explains what the machinery does, the second deals with the argument that it doesn't matter. They're written to be read in that order.

**If you run a website.** Go straight to [You Don't Need Google Analytics](/analytics/). It's the most immediately useful page here for anyone who publishes, and it's where the argument turns into something you can act on this week.
</div>

## Ladder one: if you just use the web

<div class="actions">
Rungs are roughly ordered by effort. Stop wherever you like, but the first one is worth doing even if you do nothing else.

**1. Install an ad blocker.** *Two minutes. Free.* uBlock Origin is the standard choice, open source and independently maintained. {{< cite "ublock-origin" >}} This is the single largest reduction in what leaves your browser available in a single action, and it is not close. It will also break a small number of sites, which is the price.

**2. Look at your own fingerprint.** *One minute.* Run *Cover Your Tracks* twice, private window and normal. You're not looking for a good or bad score; you're looking at what remains when cookies are gone.

**3. Change your default search engine.** *Five minutes.* Try one that isn't funded by advertising against your query. This is the highest-leverage habit change on the list, because search is where your intentions are most legible.

**4. Audit which accounts you actually use.** *An hour, and then some deleting.* Not a privacy measure so much as a reduction in surface area. Every account is a copy of you that can leak.

**5. Move one thing you care about off an ad-funded service.** *An afternoon.* Email is the conventional suggestion and the biggest lever, but it's also the most disruptive. A calendar, a drive, a photo backup. Any of them counts.

**6. Learn what a VPN does and doesn't do.** *Reading time, no purchase.* A VPN changes who can see your traffic. It does not make you anonymous, and it does nothing about the account you're signed into. Anyone selling you the second thing is selling you the first one.

**If you only do one rung:** the first. It costs two minutes, it's reversible, and every page you load afterwards is measurably lighter.
</div>

## Ladder two: if you run a website

<div class="actions">
This ladder is shorter and, honestly, has more effect per hour spent, because a site owner affects every reader rather than only themselves.

**1. Count your own third-party requests.** *Five minutes.* Open the Network panel on your own site and count how many domains you're loading from other than your own. Almost nobody has done this on their own site. The number is usually a surprise. {{< cite "themarkup-blacklight" >}}

**2. Decide whether you need your analytics tool.** *An hour.* [This page](/analytics/) walks through it, including the case for just reading your server logs. If you're staying on GA4, configure it to collect less. That's a real improvement even if it isn't a fix.

**3. Self-host your fonts.** *Fifteen minutes.* A third party loaded for typography is a third party with a record of every one of your readers. A system font stack costs nothing at all; a self-hosted font file costs one request to your own domain.

**4. Replace embeds with click-to-load.** *An hour.* A YouTube embed phones home before a visitor has decided to watch anything. A placeholder image with a play button defers that until they ask for it.

**5. Say what you collect.** *Ten minutes.* One sentence, on the page or in the footer. "This site counts visits without identifying anyone" is sufficient, provided it's true.

**6. Publish your numbers.** *An afternoon.* Request count, page weight, tracker count, carbon estimate. It's the highest-credibility, lowest-cost thing a website can publish, precisely because nobody else does.

**If you only do one rung:** the third. It's a quarter of an hour, it removes a third party from every page load permanently, and it's the change most likely to make you notice the others.
</div>

## What this site won't ask you to do

<div class="callout">
**Delete your accounts.** Your social accounts are how you know people. The correct response to a harmful structure is not to exile yourself from it.

**Stop using the web, or use it "properly."** There is no properly. There are defaults, and there are choices, and the defaults were chosen by someone with an interest.

**Be consistent.** Use the private search engine and keep the group chat. Nobody is scoring you, and pretending otherwise is how this subject acquires the reputation it has.

**Care about all of it.** Pick a page, take one step, and be done. The material here will still be here if you come back in a year.

**Become an expert.** You should not have to understand TLS, or the difference between a first-party and third-party cookie, or how a fingerprint is assembled, in order to use the web without being profiled. The fact that you currently do is a design failure on the part of the industry, not a gap in your education. This site exists to shorten the distance, not to certify you at the end.

**Feel guilty.** Guilt is the least useful output of this subject, and it's the one most often produced. Nothing here is your fault, and the changes available to you are worth making because they're cheap, not because you owe anyone penance.
</div>

## A note on pace

The strongest predictor of whether someone keeps any of this up is whether their first attempt was small enough to survive a busy fortnight.

So: pick the rung that costs two minutes. Do it. Notice that nothing got worse. Come back to the next one whenever, or don't, and read the site purely for interest, which is also a completely respectable way to use it.

{{< source-list >}}
