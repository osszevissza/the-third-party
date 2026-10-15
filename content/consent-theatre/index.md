+++
title = "Consent Theatre"
subtitle = "The banner is not there to protect you from tracking. It is there to get your name on it."
description = "Why cookie banners exist, why they fail in ways regulators have already documented, and why the button you are looking for is missing on purpose."
status_as_of = 2026-10-14
weight = 7
nav = "Consent theatre"
sources = [
  "edpb-cookie-banner-taskforce",
  "cjeu-iab-europe-tcf",
  "conseil-etat-yahoo-cookies",
  "cnil-google-san-2025-004",
  "edpb-consent-or-pay",
  "cjeu-planet49"
]
+++

<!-- STRUCTURE NOTE (remove before publishing):
     Register is A: an explanatory essay that builds, strongest argument held back
     until "What the framework is for". The voice decision is closed (drafts/README.md);
     do not restructure this into objection units.

     The /consent-theatre/ interactive promised in SITE_PLAN.md §5 is not built here.
     It has to render its full content as readable HTML with JS off, which means the
     click sequence must be real before any script is written around it. Building the
     counter over an invented sequence would be the exact false precision this project
     forbids. When the sequence is measured on real banners, it belongs in an <ol> in
     this page and the counter becomes an enhancement. 4 hours of work remains. -->

There is a specific kind of tired you only get from a cookie banner.

You wanted one paragraph of a news article. You are being asked to make a decision about hundreds of companies, in a panel that covers the paragraph, with two buttons that are the same shade of blue, one of which is a link inside a sentence you stopped reading three seconds ago. You press the one that makes it go away. You always press the one that makes it go away.

Now notice what is missing. Europe's data protection authorities spent thirteen meetings comparing the banners their citizens were complaining about, and the single most common defect they recorded was a banner with a button to accept and **no way to reject at all** on the layer that carried it. Not a hidden reject button. Not a low-contrast one. No reject option. {{< cite "edpb-cookie-banner-taskforce" >}}

The button you could not find was not there. The banner did not fail. It worked exactly as designed, and the design was never yours.

## Why the banner exists at all

The rule is older and narrower than most people assume. In the EU, it comes from the ePrivacy Directive of 2002, which says that storing information on your device or reading information from it requires you to be informed and to have consented, with a narrow exception for what is strictly necessary to provide a service you asked for. {{< cite "cjeu-planet49" >}}

That is the whole idea. It is about your device, not about your data. It covers a cookie that contains no personal data at all.

The GDPR then does two things on top. It supplies the standard for what consent has to mean, since ePrivacy does not define it, and it governs whatever processing happens afterwards. Supervisory authorities confirmed both halves of that arrangement in the report that matters most on this page. {{< cite "edpb-cookie-banner-taskforce" >}}

So the standard is not vague. Consent has to be **freely given**, **specific**, **informed** and **unambiguous**. A pre-ticked box fails it, which the Court of Justice settled in 2019. {{< cite "cjeu-planet49" >}}

Do not read that as a rule about banners alone. French regulators opened a verification mission into tracers read and placed on the devices of people who were signed in to an account, which is the opposite of what most people assume, that being logged in means you agreed to whatever happens next. {{< cite "cnil-google-san-2025-004" >}}

Read those four words again and then picture the banner you closed this morning. Every one of them is a design constraint. Every one of them is a constraint a banner can be built to defeat while remaining, on its face, a banner.

## What regulators actually found

This is the part that usually gets asserted rather than sourced, so here is the source. Complaints about cookie banners from one complainant were coordinated across European supervisory authorities over thirteen meetings, and the resulting report names the practices and records what the authorities concluded. {{< cite "edpb-cookie-banner-taskforce" >}}

- **No reject button.** Where a banner offers a button to accept and no way to reject on any layer that has a consent button, a vast majority of authorities held that this breaches the consent standard. A few did not, on the narrow ground that the directive does not name a reject option in so many words. The majority position is the one to plan against.
- **Pre-ticked boxes.** Ticking the categories for the user does not produce valid consent, at either layer.
- **Reject as a link.** If the only alternative to accepting is a link inside a paragraph of text, or a link outside the banner frame, with nothing visually pulling your eye to it, that does not produce valid consent.
- **Unreadable buttons.** A reject button whose text is nearly the same colour as its own background was treated as manifestly misleading. Colour and contrast are otherwise left to case-by-case review, which is deliberate: the report declines to impose a blanket standard.
- **Legitimate interests.** A controller cannot fall back on legitimate interests as the basis for placing or reading cookies. And confusion is a finding in itself: asking a user to refuse once for cookies and again for the processing sold as a legitimate interest leads people to think they must refuse twice.
- **"Essential" that is not.** Cookies and processing classified as essential or strictly necessary, when they are neither, is a recognised problem, and the report notes that website owners are expected to be able to document why each one qualifies.
- **No way back.** The absence of a route to withdraw consent is treated alongside the rest. {{< cite "edpb-cookie-banner-taskforce" >}}

One caution, and the report is firm about it: these are a common minimum agreed between authorities, not findings against any particular site, and they do not replace the law of each member state. Treat it as a description of what regulators consider worth acting on, not as a checklist that certifies your banner.

That withdrawal point is not theoretical. The CNIL fined Yahoo EMEA ten million euros over advertising cookies placed and read without prior consent and over the means of withdrawing consent, and France's highest administrative court upheld it. The court's language is about an obstacle standing in the way of withdrawal, and it treated the conditions for withdrawing consent as inseparable from the freedom to give it. {{< cite "conseil-etat-yahoo-cookies" >}}

## What the framework is for

Everything above describes bad banners. That framing is too generous to the system, because it implies that a good banner would fix this.

The ad-tech industry did not ignore the consent requirement. It built infrastructure for it, and the infrastructure is the argument. Advertisers needed one thing that consent banners had never provided: a way to carry a user's choices, in a machine-readable form, from the page where the choice was made to the thousands of companies that would act on it. So it invented a format. Your preferences are encoded into a string that gets passed around the advertising system, paired with a cookie, and read by brokers and platforms so that each of them knows what you agreed to. {{< cite "cjeu-iab-europe-tcf" >}}

In 2024 the Court of Justice looked at that arrangement and made two findings that matter here.

The string constitutes personal data. Combined with an identifier such as your IP address, it can be used to build a profile of you and to identify you. And the industry body that maintains the format is a joint controller, for the step where your choices get recorded in it. {{< cite "cjeu-iab-europe-tcf" >}}

The second finding is the important one. The thing you are agreeing to is not a transaction between you and the site you are reading. It is a transaction between you and an industry-wide mechanism, run by an association whose members are the parties that benefit, and the Court has now said that association shares responsibility for it. That is why the banner is designed the way it is. The site does not need your answer for itself. The site needs your answer in a format that travels.

There is a second piece of evidence for this, and it is the existence of the offer itself. Some large platforms began asking users to choose between consenting to behavioural advertising and paying a fee. If consent were being collected in good faith, a price for withholding it would be an odd product. The European Data Protection Board published an opinion on those models and concluded that in most cases a binary choice between consenting to behavioural advertising and paying is not capable of meeting the standard for valid consent, and that platforms should consider offering an equivalent alternative that costs nothing and involves no behavioural advertising. {{< cite "edpb-consent-or-pay" >}}

Two things about that opinion, because it is easy to overread. It is an opinion, not a ruling, and it is explicitly framed around large platforms rather than every site on the web. {{< cite "edpb-consent-or-pay" >}} But the reasoning generalises in an uncomfortable direction. If being charged for declining means your consent was not free, then the same logic applies to a banner that makes declining exhausting rather than expensive. The coin is different. The currency is the same.

## The other side, stated fairly

The site owner is usually not the villain, and this page is worthless if it pretends otherwise.

If you run a shop, a blog, or a course website, you did not ask for a consent banner. You got one because your site loads a font from somewhere, or embeds a video, or runs analytics you were told you needed, and each of those things can set or read something on a visitor's device. Your options were to remove the tool, to pay a lawyer, or to install a plugin that produces a banner. One of those is cheap, one is expensive, and one is what everyone else did.

The vendor then offers you a banner that is "compliant", meaning it exists, records something, and would be difficult to prove non-compliant without a regulator taking an interest in you personally. Compliance-by-plugin is a reasonable response to a legal obligation you did not want and cannot evaluate. Meanwhile the honest reading of the framework is that the banner is a symptom, and the cause is the third-party request on your page. Remove the request and the banner has nothing to ask about, which is the entire reason [this site does not have one](/analytics/).

And there is a genuine counter-argument to the smug version of this page. Consent, done properly, is not theatre. It is the only mechanism in the whole system that requires a company to ask before it acts. Weakening it weakens the one point where you have standing. A world with no consent requirement is not a world with less tracking. It is a world with the same tracking and no grounds to object.

## Where this page is wrong

Fairness requires the concession, so here it is.

Most of the evidence above concerns large platforms or sites that were investigated. Nothing here establishes that the typical banner on a small site is deliberately manipulative. A great many of them are assembled from a template by someone who picked the first plugin in the list, and the missing reject button may be incompetence rather than malice. The distinction does not change your experience of the banner. It does change what should be done about it.

The taskforce report is a coordination record agreed between authorities, expressly not a set of findings, and expressly a floor rather than a ceiling. It also does not address the question a sceptic will ask: what proportion of banners do these things. There is no figure here because no one has published a reliable count for the general web, and inventing one would defeat the purpose of the page.

The enforcement is thin. One ten million euro fine on one company, and a handful of enforcement actions across a market of millions of sites, is not a deterrent. On the evidence so far, the realistic prospect for most sites is that nothing happens. {{< cite "conseil-etat-yahoo-cookies" >}}

And the framework is genuinely difficult to apply. Consent is supposed to be granular, revocable, and specific to a stated purpose, across hundreds of companies, in a panel the reader has thirty seconds for. Some of the harm here comes from a regulator's requirements and a user interface being intrinsically hard to reconcile. That is a harder problem than a bad button colour, and this page does not solve it.

## Eight clicks through one banner

Here is the whole thing in the order you meet it. Every step is a defect that supervisory authorities have already recorded, and each one is quoted from their report rather than invented for effect. {{< cite "edpb-cookie-banner-taskforce" >}}

**This is one banner, not a survey.** It is assembled from the practices in that report, in a plausible order, so the sequence is a composite rather than a measurement of any particular site. Treat it as what you are likely to meet, not as a count.

{{< interactive >}}
**Click 1. You accept.** Not because you decided to, but because this button was the only one in the banner, and reading further costs time you had earmarked for the article. The report records banners offering a button to accept and a route to further options, with no reject at all on the layer carrying the consent button. A vast majority of authorities held that this infringes the consent standard.

**Click 2. You look for a way out.** You find the settings link, tiny, in the corner. This is the second layer, which is where the choices were moved to.

**Click 3. You find the reject option, as a link.** Not a button. It is wording like "refuse" or "continue without accepting" sitting inside a paragraph of the banner, or parked outside the banner frame beneath the accept buttons, with nothing to draw your eye to it. The report says that does not produce valid consent "in the absence of sufficient visual support to draw an average user's attention to this alternative action."

**Click 4. You compare the two buttons.** Accept is filled, saturated, and about forty pixels tall. Reject is an outline in a paler shade of the same colour. The report calls this a misleading "contrast ratio between the accept button and the background," and while it declines to set a blanket standard it treats a case-by-case check as necessary. Authorities also identified a manifestly misleading version: a reject button whose text is so low-contrast against its own background that it is unreadable to virtually anyone.

**Click 5. You hit a wall of switches.** Several hundred vendors, all pre-ticked. Undoing them is the work of an afternoon. Pre-ticked boxes to opt in do not produce valid consent, at either layer, per both the GDPR's recital 32 ("Silence, pre-ticked boxes or inactivity should not therefore constitute consent") and the ePrivacy Directive.

**Click 6. You find the ones labelled essential.** Mostly analytics and advertising tooling, described as necessary for the site to function. The report records cookies and processing classified as essential or strictly necessary when they are neither, and notes that a site owner is expected to be able to evidence why each one qualifies.

**Click 7. You object a second time.** Some of the processing is presented as the site's legitimate interest, so refusing the cookies does not obviously refuse that. The report records that people read this as having to refuse twice, and settles the point: legitimate interests cannot be the legal basis for placing or reading cookies.

**Click 8. It is still there.** The saved preference did not stick, or the "manage" link reappeared, or there is simply no way to withdraw. The report records the absence of a route to withdraw consent alongside the rest of it.

**You are done.** Nothing you refused has been switched off for certain, and the banner will be back next visit.
{{< /interactive >}}

None of that was an accident, and no single person had to be cynical to build it. Each step is a defensible-looking answer to one constraint. That is what a genre looks like.

## What you can do

**If you run a site:** the fastest honest fix is to count the third-party requests you make and delete the ones you do not need. Each one you remove is a purpose you no longer have to ask about. Then, for what is left, make refusal as easy as agreement: same layer, same visual weight, a real button. The report above is unusually specific about what that means, and it is the closest thing to a documented consensus. {{< cite "edpb-cookie-banner-taskforce" >}} Check what your plugin calls essential, and be able to say why each item is. That claim is now something a regulator can ask you to substantiate. {{< cite "edpb-cookie-banner-taskforce" >}}

**If you are reading this as a user:** stop hunting for the reject button in the wrong places. If it is absent from the layer with the accept button, or present only as an unmarked link, that is not a puzzle you are failing. Regulators have described it as a defect. {{< cite "edpb-cookie-banner-taskforce" >}}

The more interesting option is to stop answering banners individually. The law already accepts that consent can be expressed through settings on the device you are using, rather than through a click on each site. {{< cite "conseil-etat-yahoo-cookies" >}} A browser that sends a clear, machine-readable "do not sell or share" on your behalf is therefore not a loophole or a grey area. It is the mechanism the framework always allowed and nobody built properly, and the reason it has not been built is that no business model depends on your answer being no.

Until that exists, do the tedious thing. Decline where you can, in a browser that makes declining cheap. And when you see a banner built to be survived rather than answered, remember what it is for.

{{< source-list >}}
