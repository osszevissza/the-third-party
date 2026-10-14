+++
title = "Nine Things People Say"
subtitle = "The standard objections to caring about privacy, taken one at a time"
description = "For each common objection, the best available answer, including the three cases where the objection is simply correct."
status_as_of = 2026-10-14
weight = 4
sources = [
  "aol-4417749",
  "sweeney-demographics",
  "netflix-prize",
  "ftc-surveillance-pricing",
  "ali-ad-delivery",
  "ftc-gravy-venntel",
  "ftc-mobilewalla",
  "penney-chilling",
  "solove-nothing-to-hide",
  "solove-taxonomy",
  "zuboff-surveillance-capitalism",
  "verizon-dbir",
  "garcia-shadow-profiles",
  "phone-number-recycling",
  "ftc-data-brokers-2014",
  "google-build-profiles"
]
+++

In August 2006, AOL published a file it believed was anonymous.

It held around 20 million search queries from roughly 658,000 users, each person replaced by a number. No names, no addresses, nothing that identified anybody: by the standards of the day, a model release.

Within days, two reporters had identified user 4417749 as Thelma Arnold, a 62-year-old widow in Lilburn, Georgia. They worked it out from her searches: the surnames of people she knew, a landscaper she was considering, a three-digit number she looked up again and again, and the phrase *numb fingers*, which described her own symptoms. *"We all have our moments of weakness,"* she said, when they called. {{< cite "aol-4417749" >}}

Nobody leaked anything. Nobody hacked anything. The file was withdrawn within days. The identification happened because the data was sufficient, and it was sufficient because it was *many*.

This page is about the argument that says none of that matters. It arrives in nine standard forms, and each one gets the best answer available. Three of the nine are correct, and saying so is the point.

---

## 1. "I have nothing to hide."

You probably do, and the phrase is doing more work than you think. "Something to hide" is being used as a synonym for *evidence of wrongdoing*, and almost nobody has that. But a great many people have a medical condition, a debt, a relationship they haven't announced, a job they're quietly applying for, or an opinion they'd rather not have attributed to them by name at work.

None of those are crimes, and all of them are things you'd rather control the disclosure of. That instinct isn't shame. It's ordinary self-respect, and it's what privacy protects. Daniel Solove's correction is the useful one: privacy isn't a single thing, and it isn't a synonym for secrecy. It's a family of separate concerns about how information about you moves: what gets collected, what gets done with it, who it gets passed to, and what gets intruded on. {{< cite "solove-taxonomy" >}} His short essay on this exact argument is the best thing written about it. {{< cite "solove-nothing-to-hide" >}}

The cleanest test isn't philosophical. Hand your unlocked phone to the person nearest you and let them scroll for five minutes. Almost nobody says yes, and the reason is rarely a specific secret; most of us would struggle to name one. The reason is that *this is not the arrangement I agreed to*. Privacy is the ability to set those terms, and "I have nothing to hide" answers a question about secrets that nobody was asking.

## 2. "The data about me is boring."

Boring is the raw material. That's the whole trick.

In 2000, Latanya Sweeney showed that **87% of the US population** could likely be singled out from three fields alone: five-digit ZIP code, date of birth, and sex. {{< cite "sweeney-demographics" >}} None of those is interesting on its own. Together they're a name and an address.

Thelma Arnold's searches were boring too, and that is why the identification worked. What makes a dataset dangerous is never the sensitivity of one field. It's how many fields can be lined up against each other, and how many *other* datasets they can be lined up against, including ones that don't exist yet. Netflix learned the same lesson in 2006, releasing 100 million "anonymised" ratings for a public competition. Two years later, researchers re-identified substantial numbers of people in it by cross-referencing public reviews on IMDb, a dataset nobody had thought to consider, because nobody had thought about the *combination*. {{< cite "netflix-prize" >}}

You cannot consent to a join you can't foresee. That's why anonymity by deleting names keeps failing: you can remove a name from a file, but you can't remove the fact that the file is joinable.

## 3. "It's all legal, so it must be fine."

This one is fair, and half right. The practices described here are mostly lawful. But legality is a floor, set by a negotiation between regulators and the industry being regulated, so it reflects what was arguable at the time, not what is harmless.

The Federal Trade Commission's recent location-data actions are instructive because they concern practices that were widespread and largely unremarkable until they weren't. In December 2024 the FTC moved against two brokers over selling location data that could reveal visits to sensitive places {{< cite "ftc-gravy-venntel" >}}; in January 2025 it finalised an order banning a third from selling sensitive location data outright. {{< cite "ftc-mobilewalla" >}} That data had been collected for advertising, then sold onward into contexts nobody at the point of collection had in mind.

"Legal" answers the question *will I be punished*. It doesn't answer *is this good for me*. Those are different questions, and only one of them is about you.

## 4. "If I've done nothing wrong, I've got nothing to fear."

In 2016, the legal scholar Jonathon Penney published an empirical study of Wikipedia traffic around the 2013 Snowden disclosures, and found a large, sustained decline in views of the encyclopaedia's terrorism-related articles, concentrated in patterns consistent with surveillance awareness. {{< cite "penney-chilling" >}}

Read what that means. Nobody was accused of anything. Nobody was punished. The people who stopped reading simply changed their behaviour in advance, because a possibility had become visible to them.

That's a chilling effect, and its defining property is that it works without enforcement: the mere existence of collection is sufficient. So the argument fails on its own terms. The harm lands on the innocent, it lands first, and it is self-administered.

A society whose citizens pre-emptively self-censor is not one that has caught its wrongdoers. It's one that has taught everybody to behave as though they might be.

## 5. "It's just advertising. They can't do anything with it."

Advertising is how the data gets paid for. It isn't the limit of what it's used for.

In January 2025 the FTC published findings from a study of what it calls surveillance pricing, reporting that firms were drawing on a wide range of personal data, including data with no connection to the transaction, to set individualised prices. {{< cite "ftc-surveillance-pricing" >}} The same trail that sells you a jacket is available to decide what the jacket costs you.

And what gets used isn't the data you gave. It's the conclusion drawn from it. Nobody needs your search history; they need the answer to a question they never asked, which is whether you are in debt, pregnant, looking for work, or about to move. That product has three properties which make it worse than collection: it can't be deleted, it can be wrong with no way to correct it, and it can be made about you without your having done anything.

There's a second-order problem too. In 2019, researchers bought Facebook ads with deliberately *neutral* targeting and found that delivery still skewed heavily by race and gender, because the system optimises for who it predicts will engage. {{< cite "ali-ad-delivery" >}} Identical inputs, systematically different outputs.

So the honest answer to "they can't do anything with it" is this: they can help decide what you're charged, and they can help decide how you're treated. Neither decision is one you get to inspect.

## 6. "It's my data. If I don't mind, that's the end of it."

It isn't only your data, and that's the part most people miss.

When an app asks for access to your contacts and you tap allow, you hand over the names and phone numbers of everyone you know, including people who never installed it. A 2017 study tested that on the abandoned data of an old social network: the contact lists users had uploaded contained non-members, and what those users disclosed predicted personal details about people who had no account at all. The finding has a name, the shadow profile hypothesis, and a conclusion worth carrying around: "individual privacy decisions do not happen in isolation." {{< cite "garcia-shadow-profiles" >}}

What travels is not a harmless string. A 2021 study looked at 259 phone numbers available to new subscribers at two US carriers. Of those, 171 were still tied to accounts at popular websites and 100 were linked to leaked login credentials, so the next person to hold a number can often reach accounts belonging to whoever held it before. Most of the numbers also produced hits on people-search services, which publish names, addresses and relatives. {{< cite "phone-number-recycling" >}}

Those services are the retail end of an industry the FTC studied in 2014. It found brokers holding files on almost every US consumer, assembled from sources those consumers had never dealt with, and found that the files feed decisions about credit, employment, insurance and housing. {{< cite "ftc-data-brokers-2014" >}} Its own example: a customer refused a mobile phone contract by a risk-scoring product, and never told why. Credit is on that list, so a refusal can rest on a file the applicant has never seen.

Every copy you help create is also a copy that can leave: breach reporting is a permanent annual industry because compromise is routine rather than exceptional {{< cite "verizon-dbir" >}}, and the person a leaked file is about is rarely the one who uploaded the contact list.

So "I don't mind" is a real answer to a narrower question. It answers whether you mind. It says nothing about the person whose number you just handed over, and nobody asked them.

## 7. "Everyone uses these things. What's the alternative?"

You're right. This objection is correct, and this is the point where most privacy writing loses its audience by pretending otherwise.

Opting out has genuine costs. Services stop working properly. You lose conveniences your friends have. You become the person who won't join the group chat, which is a real social tax and not a moral failing to acknowledge. A site that demands total abstinence is a site nobody follows.

So this site doesn't demand it. [The swap shop](/swap-shop/) lists what to replace *and what each replacement costs you*, including the parts that are worse. Most of the wins are available for less than you'd expect, and none of them require you to become an enthusiast.

The claim being made here is not "leave the internet." It's narrower and harder to dismiss: the defaults were chosen for somebody's benefit, and they can be changed.

## 8. "I don't have time to care about this."

Entirely legitimate, and this site is built around that answer rather than against it.

Here's the thing worth knowing, though: the reason it takes time is not an accident. Making privacy settings hard to find, opt-outs exhausting to complete, and unsubscribe flows require a phone call is a design discipline with a budget and a job title. It's called dark patterns, and the friction you're describing is the product, not the byproduct.

The correct response to "I don't have time" is not a longer article. It's one small change, and then permission to stop. [Start here](/start-here/) is arranged so you can take one step, in any order, and be done.

## 9. "Isn't caring about privacy a bit paranoid?"

Sometimes, yes, and it's worth saying so, because a lot of privacy culture *is* performative. Distrust as identity. Threat models borrowed from people with genuinely different jobs.

But look at what's actually being claimed here, which is much more modest than paranoia. Not that anyone is watching *you* personally. Not that a conspiracy exists. Only that the relationship is one-directional in a way that has no precedent: they can measure your behaviour comprehensively, and you cannot see the file, contest the conclusion, or discover who bought it.

Shoshana Zuboff's term for that is **instrumentarian power**, power exercised not by coercion but by instrumentation, at a resolution that simply didn't exist before. {{< cite "zuboff-surveillance-capitalism" >}}

The point of naming it is that it holds even if every specific fear is unfounded. Suppose nothing bad ever happens with your data: no breach, no skewed price, no wrong inference. One party still holds comprehensive knowledge of another, and the second cannot reciprocate, inspect, or leave at a cost that isn't punitive.

That's not paranoia. It's asymmetry, described accurately.

---

## Where this page is wrong

**Counting visits is not surveillance.** A site owner who wants to know how many people read a page, and which pages get read, does not need to identify anyone. A tool that counts without profiling is benign, and it would be absurd to treat a visit counter as the moral equivalent of a cross-site tracker. For what that looks like in practice, see [analytics without surveillance](/analytics/).

**Most of these harms are probabilistic.** Most people, most of the time, will not be visibly harmed by any of the mechanisms above. That's true, and it's also an odd basis for a system with no meaningful opt-out: "usually fine" is not a guarantee, and the people for whom it isn't fine have no way to know in advance.

## The one question

Forget the question "do you care about privacy." It has no useful answer and it invites a defensive one.

Ask instead: **name the inference about you that would actually cost you something.**

Not a secret. Not a crime. A conclusion someone could draw, rightly or wrongly, from the ordinary trail you leave. A health condition. A financial situation. A job search. A habit you'd rather not have summarised in a dashboard and priced.

Most people can name one in about ten seconds. If you can, you've already stopped believing you have nothing to hide. You just haven't updated the sentence yet. Then do one small thing and treat it as sufficient for now.

**Start here:** open EFF's *Cover Your Tracks* in your browser. Thirty seconds. It shows what can be deduced about your device from the connection alone, before any account, cookie, or login.

## Two harms that needed arguing

The test below names seven ways this can go wrong. Five of them are argued in the nine answers above. The other two were only named when this page was first written, which is the same shortcut this site complains about when other people take it, so here they are.

**Secondary use.** Everything above assumes the data goes where you were told it would go. The more common arrangement is that it goes somewhere else, later, for a purpose somebody else chose, and nobody tells you.

Google's own developer documentation for its advertising systems is unusually direct about the mechanism. A user profile, it says, is "a mapping of a user identifier [...] to information about the user that you can use for bidding with interest-based ads or remarketing with user lists". {{< cite "google-build-profiles" >}} The request that goes out to fetch one ad, in one slot, on one page, is raw material for a persistent file. The same page spends its length on the conditions under which that is permitted, which tells you how ordinary the practice is.

The FTC's location cases have the same shape with a different kind of data: information gathered for advertising, then sold into contexts that nobody at the point of collection had in mind, including inferences about visits to clinics, places of worship and protests. {{< cite "ftc-gravy-venntel" >}}

The rule meant to prevent this is called purpose limitation: collect for a stated reason, and do not quietly reuse the data for another. Its weakness is arithmetic. The second purpose usually does not exist yet when you agree to the first one, so the only decision you ever get to make is the earliest one, taken with the least information you will ever have about it. You are not consenting to a use. You are consenting to a market.

**Dignity.** This one is different from the six around it, because it does not depend on anything going wrong.

The FTC's 2014 study of data brokers gives the plainest example. A customer was refused a mobile phone contract by a risk-scoring product, and was never told why. {{< cite "ftc-data-brokers-2014" >}} Nothing leaked. No error was proved. A refusal was simply delivered, out of a file the applicant had never seen, by a process with no obligation to explain itself.

That is a different injury from being treated badly by a person. A person can be argued with, complained about, or avoided. A scoring product cannot. What is being described is not a bad outcome but a set of terms: one party holds a comprehensive account of another, and the second cannot inspect it, correct it, or reciprocate, except at a cost that is punitive by design. {{< cite "zuboff-surveillance-capitalism" >}}

**This is the only claim on this page that is normative rather than empirical, and it should be weighed as one.** Reasonable people can disagree about how much it matters. What it does not do is disappear when everything else goes right: a system that sorts people by a judgement they cannot see or answer treats them as cases to be administered, and it does that whether or not it ever gets anything wrong. The name for the thing being damaged is dignity, and no mistake is required for the damage to be real.

**A last test, if the nine answers still feel abstract.** Ask which of these would actually bother you, and notice that every one of them happens to somebody without their knowing.

{{< interactive >}}
### Which would actually bother you?

**Aggregation.** Harmless facts combine into something else. Section 2.

**Exclusion and discrimination.** What gets inferred about you decides what you are offered. Sections 1 and 6.

**Chilling effects.** Being watched changes what you look at. Section 4.

**Insecurity.** Every copy you help create can leave. Section 6.

**Power asymmetry.** One party knows, the other cannot reciprocate. Section 9.

**Secondary use.** Data given for one purpose, used for another. Sections 3 and 5, and argued above.

**Dignity.** Being judged by a process you cannot see, answer, or correct. Argued above.
{{< /interactive >}}

That is the whole argument of this page in seven words. None of them requires you to be hiding anything.

{{< source-list >}}
