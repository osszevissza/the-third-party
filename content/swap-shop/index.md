+++
title = "The Swap Shop"
subtitle = "What to replace, and what it costs you"
description = "Eight substitutions worth considering, each with the honest price of switching, plus the swaps that aren't worth making, and why."
status_as_of = 2026-10-14
weight = 11
nav = "Swap shop"
sources = [
  "posteo",
  "mailbox-org",
  "gmail-scanning-2017",
  "mullvad",
  "mullvad-audit-cure53",
  "ublock-origin",
  "ublock-origin-chrome",
  "signal-usernames",
  "search-index-concentration",
  "codeberg",
  "peertube",
  "mullvad-public-dns",
  "mullvad-dns-shutdown"
]
+++

Every page like this one turns into an advertisement, because the natural way to write it is a list of better products. So this page has a rule:

**Every swap states what you give up.** Not as a formality, as the most useful field on the page. A recommendation that doesn't tell you its cost isn't a recommendation, it's marketing, and you have no way to decide whether it applies to you.

Two more things before the list.

**You are not expected to do all of these.** Most people will find one or two that matter for reasons specific to them. This page is deliberately honest about a few swaps being bad ideas for most readers, because telling you where *not* to bother is the only way the rest of it means anything.

**None of this is a purity test.** Adopting two of the eight and ignoring the rest is a good outcome. The failure mode isn't partial adoption; it's deciding the whole thing is a lifestyle and opting out of all of it.

---

## 1. Email: from Gmail to Posteo or mailbox.org

**What Gmail does to you.** It's worth being precise here, because the usual criticism is out of date and the accurate version is more interesting.

Google stopped scanning consumer Gmail content for advertising purposes in 2017. {{< cite "gmail-scanning-2017" >}} So the lazy claim, "they read your email to sell you things", is wrong, and repeating it undermines everything else you say. The real costs are structural: your correspondence sits inside an advertising company's infrastructure and under its terms; it becomes the recovery address and identity anchor for every other account you own; and it is reachable by legal process directed at a single jurisdiction and a single company. That last point is the one that matters most, and it's the one that has nothing to do with advertising at all.

**The swap.** Two good European options with different philosophies.

**Posteo** is the purist's choice: paid, ad-free, run on green electricity, with no free tier and no growth-at-any-cost model. {{< cite "posteo" >}} **mailbox.org** is the pragmatist's: at the time of writing, €4 a month gets 20 GB of mail storage, calendar and address book, 10 GB of drive storage, and support for custom domain names. {{< cite "mailbox-org" >}}

**What it costs.** An afternoon, mostly spent changing the address on accounts you'd forgotten you had. Budget longer than you think: the migration is easy, and the notification cascade is not.

**What you give up.** This is where the two options genuinely differ, and it's the clearest example on this page of a trade-off being a matter of principle rather than a defect.

**Posteo does not support custom domains at all.** Not as an oversight, as policy, and the reasoning is unusually good. Using your own domain means the domain must be registered to a named person, which would require Posteo to start storing customer identity information and to hand it over to a regulator on request. They'd rather not offer the feature than build the database. {{< cite "posteo" >}}

**mailbox.org supports them**, which is why it costs more. If having your own domain on your email matters to you, that difference decides the choice before anything else does.

Beyond that, both: you lose Gmail's spam filtering, which is genuinely excellent and the thing most people miss first. You lose the Drive/Docs/Calendar integration, so that's a second swap. And you lose the convenience of an address everybody already has.

---

## 2. Search: from Google to something that isn't Google

**What Google does to you.** Search is where your intentions are most legible. Not your browsing, your *questions*, phrased in your own words, before you've decided anything. Query logs are also the input to the profile that determines what you're shown next, which means search feeds the rest of the web you see.

**The swap.** The honest picture has a wrinkle. **DuckDuckGo** doesn't track you, but it licenses its results from Bing, so switching changes who collects your queries without changing whose index answers them. Genuinely independent indexes are rare: a US court filing in the antitrust litigation observed that only Google, Bing and Brave operate independent general search indices with proprietary technology in that market. {{< cite "search-index-concentration" >}}

That leaves three real options. **Brave Search** has its own index. **Mojeek** is an independent UK engine with its own crawler. **SearXNG** is self-hostable metasearch that queries others on your behalf: the most private, and the one that requires you to run something.

**What it costs.** Five minutes for the easy option, an afternoon if you self-host.

**What you give up.** Result quality on obscure technical queries, which is where Google's index advantage is real and noticeable. Local and shopping results get worse across the board. And you may find yourself keeping Google as a fallback for a while, which is fine and honest.

---

## 3. Ad blocking: from nothing to uBlock Origin

**What nothing does to you.** Every ad, tracker and third-party script on every page you visit, executed on your machine, at your bandwidth cost, feeding a profile you never see.

**The swap.** uBlock Origin, and this one is nearly free. {{< cite "ublock-origin" >}}

**What it costs.** Two minutes.

**What you give up, and this is now a browser decision.** As of late 2026, full uBlock Origin **no longer works in current Chrome**. Chrome's extension platform changes removed the capabilities it depends on. Raymond Hill, the same developer, ships a separate Manifest V3 extension called uBlock Origin Lite, which handles everyday ad and tracker blocking but is not equivalent: the project itself notes results differ, particularly on sites that actively resist blocking. {{< cite "ublock-origin-chrome" >}}

So the practical answer is: install the Lite version if you're staying on Chrome, and understand you're getting a reduced tool. Full blocking now means Firefox, where the unrestricted version still runs. That's a real cost, and it's the clearest case on this page of a platform decision having a privacy consequence you can't engineer around.

---

## 4. Chat: from WhatsApp to Signal, with a caveat

**What WhatsApp does to you.** Message content is end-to-end encrypted, and that part is real. The metadata (who talks to whom, when, how often) belongs to a company whose business is advertising, and the account is anchored to a phone number and a contact graph that gets uploaded.

**The swap.** Signal: a nonprofit, end-to-end encrypted, with no advertising business and a much smaller set of things it can be asked for. Roughly a decade of criticism centred on its requirement that you register with a phone number, which is a genuine metadata exposure. Signal has since added usernames, so you can now contact people without handing over your number. {{< cite "signal-usernames" >}}

**What it costs.** Ten minutes to install. Months to convince anyone else.

**What you give up.** This is the swap with the highest real cost on the page, and it has nothing to do with software: **everybody you know is on WhatsApp.** Signal is only useful if the people you talk to will move, and for most people the honest answer is that they won't. Keeping both is a completely reasonable outcome: use Signal where you can, and don't perform a dramatic exit from the group chat your friends actually use.

If you want something that isn't tied to a phone number at all, Matrix is the answer, and it comes with real complexity and a smaller network. That's a project, not a swap.

---

## 5. Documents: from Google Docs to CryptPad or Nextcloud

**What Google Docs does to you.** Everything you write lives on someone else's infrastructure, under their terms, indexed by their systems, and reachable by legal process. The collaboration features are genuinely excellent, which is why the product won.

**The swap.** **CryptPad** for encrypted, browser-based collaboration with real-time editing. **Nextcloud** if you want to self-host files, documents, calendar and contacts as one thing; considerably more work, considerably more control.

**What it costs.** An hour to try, a weekend to migrate a shared drive.

**What you give up.** Polish. Google Docs is a mature product with years of edge-case work behind it, and the alternatives have sharp edges: less reliable real-time collaboration, fewer exotic features, and (the one that actually blocks migration) **other people don't have accounts.** Sharing a document with someone who has never heard of CryptPad is a friction cost you pay every time.

---

## 6. Code hosting: from GitHub to Codeberg

**What Codeberg does differently.** It's a non-profit, running Forgejo, funded by donations rather than by an enterprise sales motion. {{< cite "codeberg" >}} For anyone uneasy about a single company owning the infrastructure that most open-source software is built and distributed through, it's the obvious alternative.

**What it costs.** An afternoon per repository, plus updating every CI config and deployment hook.

**What you give up.** The network effect, which is the whole reason GitHub won. Your issues, your stars, your discoverability, and every integration that assumes GitHub. If your project has contributors, moving means asking them to move too. For a personal repository this is a mild inconvenience; for a project with an active community it's a genuinely hard call, and staying is defensible.

---

## 7. Video: from YouTube to PeerTube

**What PeerTube is.** Federated video hosting: a network of independent servers rather than one platform, so no single company decides what's recommendable. {{< cite "peertube" >}}

**What it costs.** An afternoon, more if you run your own instance.

**What you give up.** Your audience. That's not a minor caveat: for anyone whose work depends on being found, it's close to disqualifying, and pretending otherwise would make this page worthless. PeerTube works for publishing *alongside* an existing audience, for content that isn't discovery-dependent, or for archival. It is not a replacement for a platform whose value *is* its reach.

---

## 8. DNS: from your ISP's resolver to a public one

**What your ISP's resolver does to you.** Every domain you look up passes through it, which builds a near-complete record of the sites you visit, including things HTTPS hides, because the lookup happens before the encrypted connection starts.

**The swap.** A public resolver, or DNS-over-HTTPS to encrypt the lookup itself.

**Which resolver, and why this page puts a date on things.** The reasoning above matters more than the brand, and any public resolver is the same kind of trade. One example, though, because it makes the dating argument better than any sentence could. Mullvad has run public encrypted DNS since 2022, and in September 2026 it announced that it is shutting those servers down on 2 November 2026 and **sponsoring Quad9 instead of running its own** {{< cite "mullvad-public-dns" >}} {{< cite "mullvad-dns-shutdown" >}}. So a resolver this page could have recommended without a date would have expired within weeks. Advice without a date is not advice, it is a guess with a shelf life.

**Notice: the resolver named here changes on 2 November 2026.** Everything above still stands, and the name does not. Mullvad's public resolvers stop that day, and what Mullvad points people at instead is Quad9, which it now funds rather than competes with. That is the switch this page's author is making, so this paragraph will be rewritten once it lands and the "status as of" date at the top of this page will move with it. **The link was going to break, and it is the kind of link that breaks quietly**, which is why the date is in the sentence rather than in a footnote. If you are configuring a resolver today: pick one that is not your ISP, check that it is still running, and expect to do it again in a year or two.

**What you give up, and this is the honest part.** You are not removing the record. You are **moving who holds it**: from your internet provider to a DNS company, which is a different set of incentives rather than no incentives. If that company also runs advertising or security products, you may have swapped a regulated utility for an unregulated one.

This swap is worth making if your ISP is the party you most want out of your traffic. It is not worth making as a general gesture, and it should never be described as anonymity: it changes nothing about your IP address.

---

## Swaps that aren't worth making

A page that recommends everything it can think of is a page that hasn't thought about you.

**Browser to Tor, as a daily driver.** Tor is an anonymity tool, not a privacy browser, and using it for ordinary browsing is slow, breaks sites, and, most importantly, you're not anonymous if you log into anything. Use it where anonymity is genuinely the goal. For everything else, a hardened Firefox and an ad blocker do more, faster.

**VPN for general privacy.** A VPN moves your traffic from your ISP to a VPN company. That's it. It does nothing about the account you're signed into, the fingerprint your browser presents, or the trackers on the page. See the DNS entry above for the same reasoning.

If you *do* have a specific reason to use one (a hostile network, an ISP you don't trust, a jurisdiction you're passing through) then choose on business model rather than on feature list. Mullvad issues account numbers instead of taking your email address and accepts cash, which changes what it is able to tell anyone about you. {{< cite "mullvad" >}} It also publishes third-party audits of its apps and infrastructure. {{< cite "mullvad-audit-cure53" >}} Those two things tell you more about a VPN than any number of server locations.

**Deleting social accounts.** Your social accounts are how you know people. The harm is in the structure, not your presence in it, and leaving the structure doesn't change it: it just removes you from your friends. Use the platform, and don't let it be the only copy of anything you'd miss.

**Replacing every Google service at once.** This is how people end up doing nothing. Migrate one thing, let it settle for a month, and decide about the next one later.

---

## How to choose

Pick by **what you'd lose if it leaked**, not by which company you dislike most. If the answer is your email (the archive of everything you've ever said to anyone, plus the recovery address for every account you own) then the email swap is worth an afternoon and the DNS swap is worth five minutes.

Which is the only test that matters: not how principled the swap is, but whether it costs you less than the thing it protects.

{{< source-list >}}
