+++
title = "You Don't Need Google Analytics"
subtitle = "You need about four numbers"
description = "Most site owners look at three or four figures a month. Here's what you actually need, what the alternatives cost, and the honest caveat that cookieless does not automatically mean consent-free."
status_as_of = 2026-10-13
weight = 10
nav = "Analytics"
sources = [
  "cnil-analytics-exemption",
  "cnil-analytics-self-assessment",
  "matomo-log-analytics",
  "austrian-dsb-google-analytics",
  "ga4-consent-mode",
  "web-almanac",
  "goatcounter",
  "plausible",
  "matomo",
  "umami",
  "awesome-privacy-analytics"
]
+++

Open your analytics dashboard and try to remember the last time you looked at anything other than the same three or four numbers.

Most site owners can't. And that's not a failure of discipline. It's what the tool is for. The overwhelming majority of what a full-featured analytics platform measures exists to serve the business model of the company that gives it away, not to answer the questions of the person running the site.

This page is for anyone who publishes something on the web: a blog, a portfolio, a small business, a club, a course project. It's here because "what's the alternative?" is the single most reasonable objection to everything else on this site, and it deserves a real answer rather than a list of tools.

## The four numbers

Strip it back and almost every site owner wants to know:

1. **How many people came**, and roughly how that changed
2. **Where they came from**: search, a link, a newsletter, direct
3. **What they read**: which pages, and how far
4. **Whether anyone came back**

That's it. For a personal site, a small business, or a campaign, those four questions cover essentially every decision you'd actually make: what to write more of, which channel is worth the effort, whether the redesign helped. A change to any of those four numbers is a signal. Everything beyond them is either a refinement of the same four, or a report that exists because an advertiser wanted it.

The honest question isn't "which tool measures more." It's "which tool measures these four, and what does it cost me to have the rest on the page."

## What you're paying, if not money

Google Analytics is free, and that is a genuine offer, not a trick. GA4 is a powerful product with a large ecosystem, and for a marketing team the deep integration with Google's advertising platforms *is* the feature. The analytics and the ad buying are one loop, and you cannot easily separate them.

The cost to you is not financial. It's three other things:

**Requests on every page.** A full analytics installation adds third-party requests to every page load, for every visitor, forever. That is weight you are asking your readers to download, and it's measurable: the HTTP Archive's Web Almanac tracks page composition annually and is the right place to check current figures. {{< cite "web-almanac" >}}

**A disclosure you have to make.** You added a company to your readers' experience that they did not ask for and cannot see. In the EU that triggers consent obligations; a full GA4 setup makes the difference between a site that needs a cookie banner and one that might not.

**Legal exposure you didn't choose.** The use of Google Analytics in the EU has been the subject of sustained regulatory attention since the *Schrems II* judgment, including a 2022 decision by the Austrian data protection authority which found the transfers involved unlawful. {{< cite "austrian-dsb-google-analytics" >}} The legal position has shifted with subsequent adequacy arrangements, and it remains contested. This is a page where you should check the current status rather than take a summary's word for it, including mine.

And there's a subtler point about **Consent Mode**, the mechanism that's meant to reconcile analytics with consent. In practice it means that when a visitor declines, a reduced event still travels, carrying a consent state rather than identifying data. {{< cite "ga4-consent-mode" >}} That's a defensible engineering compromise. It is also not what most visitors believe "reject" means, and on a site whose entire argument is about that gap, it's worth knowing.

## What the alternatives actually are

Five options, described by their *model* rather than their current price list. Prices change, and a page that quotes them goes stale. Check each project's own site for what it costs today.

**Server logs.** Every web server already writes down what it served. This is the option almost nobody mentions and it deserves to be first, because it is free, first-party, requires no JavaScript at all, cannot be blocked by a client, and exposes no fingerprint surface whatsoever. {{< cite "matomo-log-analytics" >}} What it gives you is requests: how many, for what, from where, with what result code. For the four questions above, that is remarkably close to sufficient. What it doesn't give you is session reconstruction or beautiful charts, and the files are ugly. Many people open them once, recoil, and buy a product to avoid reading them, which is a legitimate preference, just not a technical necessity.

**GoatCounter.** Open source, built to count page views without collecting personal data, with no cookies involved. Free for non-commercial use and self-hostable. {{< cite "goatcounter" >}} It is deliberately small, and its smallness is the point: the feature list is short because the data it holds is short.

**Plausible.** Cookieless, EU-based, paid. The most polished of the hosted options, with a business model that is straightforwardly "you pay us, we don't sell anything." {{< cite "plausible" >}} If you want to pay for something and stop thinking about it, this is usually the answer.

**Matomo.** Open source, the oldest and most feature-complete of these, and the closest thing to a drop-in GA4 replacement, deliberately so, because it was built as one. It can be self-hosted or bought as a service, and it operates in a much heavier weight class than the other three. {{< cite "matomo" >}} Choose it when you need the depth, and accept that you're importing complexity along with it.

**Umami.** Open source, lightweight, self-hostable, and the least opinionated about how you run it. {{< cite "umami" >}} Good if you already self-host other things and want this to be one more container rather than another account.

For a wider and more current field, the community-maintained *awesome-privacy-friendly-web-analytics* list is a better starting point than any list frozen into an article, including this one. {{< cite "awesome-privacy-analytics" >}}

## The honest caveat: cookieless is not consent-free

This is the part that tool vendors and advocacy sites both tend to skip, and getting it wrong will get you into exactly the kind of trouble this site complains about.

**Using a privacy-friendly analytics tool does not automatically exempt you from consent requirements.** Whether a given configuration needs consent depends on jurisdiction and on the specific configuration, not on the brand of the software.

The clearest worked example is France, where the CNIL publishes guidance on which audience-measurement solutions it considers exempt, and maintains a list of configurations that qualify. {{< cite "cnil-analytics-exemption" >}} The conditions are substantive rather than decorative: the purpose has to be limited to measurement, the data can't be shared with third parties or used for other processing, visitors have to be informed, retention has to be limited, and the identifier handling has to be constrained. Meet all of it and you may not need a banner. Meet most of it and you do.

The CNIL also publishes a self-assessment tool for exactly this question, which is a far better guide than a blog post claiming that some product "is GDPR compliant" as a property of the product. {{< cite "cnil-analytics-self-assessment" >}}

So the rule is: **no cookies is a necessary condition in some jurisdictions and not a sufficient one anywhere.** Check your configuration against your regulator's actual conditions, and if you're not sure, ask a banner. An unnecessary banner is a much cheaper mistake than an unlawful absence of one.

## What switching actually costs

Also honest: this is not free, and the costs are social as much as technical.

- **Integrations you lose.** If your ad spending, your CRM, or your agency's reporting runs on GA4, replacing it is a project with stakeholders, not a setting.
- **Historical continuity.** Most migrations break year-on-year comparison at the boundary. Accept a step change or export the old data somewhere.
- **Familiarity.** GA4's reports are difficult and widely disliked, which is a real argument *for* replacing it, but it also means your team has already paid the learning cost, and you'd be asking them to pay it again.
- **Agency and contractor expectations.** If someone else runs your site, "we use GoatCounter now" may be an argument you have to have.

None of that means don't switch. It means the decision belongs to whoever owns the site's outcomes, and the correct answer for a personal blog is different from the correct answer for a business with a media buyer.

## What to do

**If you run a small site and just want numbers:** start with your server logs before buying anything. Ten minutes of `grep` will tell you whether your existing logs already answer the four questions. For a lot of sites, they do.

**If you want a tool and minimal thought:** a hosted cookieless service. Pay for it, and understand that you are buying the absence of a business model rather than a feature set.

**If you need depth or already self-host:** Matomo or Umami.

**If you're staying on GA4 for good reasons** (you have ad spend, you have a team, the integration is genuinely load-bearing), then at minimum configure it to collect less. Turn off what you don't use, shorten retention, and check what Consent Mode is actually sending when someone declines. A smaller GA4 is a real improvement even if it isn't a fix.

**And whatever you choose, publish it.** Write one sentence on your site saying what you measure and what you don't. It costs you nothing, it takes a minute, and it's the thing [this site does on its own receipt page](/receipts/). Almost nobody does it. That's the cheapest credibility available on the web.

{{< source-list >}}
