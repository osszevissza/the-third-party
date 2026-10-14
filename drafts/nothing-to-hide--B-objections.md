+++
title = "Eight Things People Say"
subtitle = "The standard objections to caring about privacy, taken one at a time"
description = "For each common objection, the best available answer, including the three cases where the objection is simply correct."
status_as_of = 2026-10-13
weight = 4
draft_variant = "B (objections)"
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
  "zuboff-surveillance-capitalism"
]
+++

> **SUPERSEDED, kept as the record of a decision.** On 2026-10-14 the maintainer's
> friend reviewed both drafts and agreed with the both-by-purpose recommendation:
> this shape for pages a reader arrives at with a *doubt*, the essay shape for pages
> they arrive at with a *question*. This draft is therefore the ancestor of the live
> page at `content/nothing-to-hide/index.md`, which keeps this structure, restores the
> AOL opening from Draft A, adds a ninth objection about other people's data, and
> carries a short "where this page is wrong" section. **Edit the live page, not this
> file.** It is kept only so the decision has a visible before.

"I have nothing to hide" is usually said by someone who is winning the argument and hasn't noticed yet.

It's a real position. It's held by serious people, for reasons that make sense from the inside, and it shows up in eight standard forms. Below is each one, followed by the best answer available, and in three cases, the answer is *you're right, and that matters more than you think*.

If you only read one, read the one you'd actually say out loud.

---

## 1. "I have nothing to hide."

You probably do, and the phrase is doing more work than you think. "Something to hide" is being used as a synonym for *evidence of wrongdoing*, and almost nobody has that. But a great many people have a medical condition, a debt, a relationship they haven't announced, a job they're quietly applying for, or an opinion they'd rather not have attributed to them by name at work.

None of those are crimes. All of them are things you'd rather control the disclosure of. That instinct isn't shame. It's ordinary self-respect, and it's the thing privacy actually protects. {{< cite "solove-nothing-to-hide" >}}

The cleanest test isn't philosophical. Hand your unlocked phone to the person nearest you and let them scroll for five minutes. Almost nobody says yes. And the reason is rarely a specific secret. Most of us would struggle to name the incriminating thing. The reason is that *this is not the arrangement I agreed to*. Privacy is the ability to set those terms.

"I have nothing to hide" answers a question, do you have secrets?, that was never being asked.

## 2. "The data about me is boring."

Boring is the raw material. That's the whole trick.

In 2000, Latanya Sweeney showed that **87% of the US population** could likely be uniquely identified from three fields alone: five-digit ZIP code, date of birth, and sex. {{< cite "sweeney-demographics" >}} None of those is interesting. Together they're a name and address.

In August 2006, AOL published what it described as an anonymised research dataset: around 20 million search queries from roughly 658,000 users, each person replaced by a number. Within days, reporters had identified user 4417749, Thelma Arnold, a 62-year-old widow in Lilburn, Georgia, from what she'd searched for. The surnames of people she knew. A landscaper she was considering. A three-digit number she looked up repeatedly. The phrase *numb fingers*, which turned out to describe her own symptoms. {{< cite "aol-4417749" >}}

Every one of those searches was boring. Boredom is not protection; it's the substrate.

Netflix learned the same lesson in 2006, releasing 100 million "anonymised" ratings for a public competition. Two years later, researchers re-identified substantial numbers of people in it by cross-referencing public IMDb reviews, a dataset nobody had thought to consider, because nobody had thought about the *combination*. {{< cite "netflix-prize" >}}

You cannot consent to a join you can't foresee. That's why anonymity by deleting names keeps failing: you can remove a name from a file, but you can't remove the fact that the file is joinable.

## 3. "It's all legal, so it must be fine."

This one is fair, and half right. The practices we're describing are, mostly, lawful. But legality is a floor, and it's set by a negotiation between regulators and the industry being regulated, so it reflects what was arguable at the time, not what's harmless.

The US Federal Trade Commission's recent location-data actions are instructive precisely because they concern practices that were widespread and largely unremarkable until they weren't. In December 2024 the FTC moved against two brokers over selling location data that could reveal visits to sensitive places {{< cite "ftc-gravy-venntel" >}}; in January 2025 it finalised an order banning a third from selling sensitive location data outright. {{< cite "ftc-mobilewalla" >}} The data had been collected for advertising. It was then sold onward, repeatedly, into contexts nobody at the point of collection had in mind.

"Legal" answers the question *will I be punished*. It doesn't answer *is this good for me*. Those are different questions, and only one of them is about you.

## 4. "If I've done nothing wrong, I've got nothing to fear."

In 2016, the legal scholar Jonathon Penney published an empirical study of Wikipedia traffic around the 2013 Snowden disclosures, and found a large, sustained decline in views of the encyclopaedia's terrorism-related articles, concentrated in patterns consistent with surveillance awareness. {{< cite "penney-chilling" >}}

Read what that means. Nobody was accused of anything. Nobody was punished. No consequence was imposed on any of the people who stopped reading. They simply changed their behaviour in advance, because a possibility had become visible to them.

That's a chilling effect, and its defining property is that it works without enforcement. The mere existence of collection is sufficient. So the argument fails on its own terms: the harm lands on the innocent, it lands first, and it is self-administered.

A society whose citizens pre-emptively self-censor is not one that has caught its wrongdoers. It's one that has taught everybody to behave as though they might be.

## 5. "It's just advertising. They can't do anything with it."

Advertising is how the data gets paid for. It isn't the limit of what it's used for.

In January 2025 the FTC published findings from a study of what it calls surveillance pricing, reporting that firms were drawing on a wide range of personal data, including data with no connection to the transaction, to set individualised prices. {{< cite "ftc-surveillance-pricing" >}} The same trail that sells you a jacket is available to decide what the jacket costs you.

And what's used isn't the data you gave. It's the conclusion drawn from it. Nobody needs your search history; they need the answer to a question they never asked: are you in debt, pregnant, looking for work, sleeping badly, about to move. That's the industry's actual product, and it has three properties that make it worse than collection: it can't be deleted, it can be wrong with no mechanism to correct it, and it can be made about you without your having done anything at all.

There's a second-order problem too. In 2019, a team of researchers bought Facebook ads with deliberately *neutral* targeting, the same audience specified for every campaign, and found that delivery skewed heavily by race and gender anyway, because the system optimises for who it predicts will engage. {{< cite "ali-ad-delivery" >}} Identical inputs, systematically different outputs.

So the honest answer to "they can't do anything with it" is this: they can help decide what you're charged, and they can help decide how you're treated. Neither decision is one you get to inspect.

## 6. "Everyone uses these things. What's the alternative?"

You're right. This objection is correct, and this is the point where most privacy writing loses its audience by pretending otherwise.

Opting out has genuine costs. Services stop working properly. You lose conveniences your friends have. You become the person who won't join the group chat, which is a real social tax and not a moral failing to acknowledge. A site that demands total abstinence is a site nobody follows.

So this site doesn't demand it. [The swap shop](/swap-shop/) lists what to replace *and what each replacement costs you*, including the parts that are worse. Most of the wins are available for less than you'd expect, and none of them require you to become an enthusiast.

The claim being made here is not "leave the internet." It's narrower and harder to dismiss: the defaults were chosen for somebody's benefit, and they can be changed.

## 7. "I don't have time to care about this."

Entirely legitimate, and this site is built around that answer rather than against it.

Here's the thing worth knowing, though: the reason it takes time is not an accident. Making privacy settings hard to find, opt-outs exhausting to complete, and unsubscribe flows require a phone call is a design discipline with a budget and a job title. It's called dark patterns, and the friction you're describing is the product, not the byproduct.

The correct response to "I don't have time" is not a longer article. It's one small change, and then permission to stop. [Start here](/start-here/) is arranged so you can take one step, in any order, and be done.

## 8. "Isn't caring about privacy a bit paranoid?"

Sometimes, yes, and it's worth saying so, because a lot of privacy culture *is* performative. Distrust as identity. Threat models borrowed from people with genuinely different jobs.

But look at what's actually being claimed here, which is much more modest than paranoia. Not that anyone is watching *you* personally. Not that a conspiracy exists. Only that the relationship is one-directional in a way that has no precedent: they can measure your behaviour comprehensively, and you cannot see the file, contest the conclusion, or discover who bought it.

Shoshana Zuboff's term for that is **instrumentarian power**, power exercised not by coercion but by instrumentation, at a resolution that simply didn't exist before. {{< cite "zuboff-surveillance-capitalism" >}}

The point of naming it is that it holds even if every specific fear turns out to be unfounded. Suppose nothing bad ever happens with your data. No breach, no skewed price, no wrong inference. The structure is still one in which one party holds comprehensive knowledge of another, and the second cannot reciprocate, inspect, or leave at a cost that isn't punitive.

That's not paranoia. It's just asymmetry, described accurately.

---

## The one question

Forget the question "do you care about privacy." It has no useful answer and it invites a defensive one.

Ask instead: **name the inference about you that would actually cost you something.**

Not a secret. Not a crime. A conclusion someone could draw, rightly or wrongly, from the ordinary trail you leave. A health condition. A financial situation. A job search. A habit you'd rather not have summarised in a dashboard and priced.

Most people can name one in about ten seconds. If you can, you've already stopped believing you have nothing to hide. You just haven't updated the sentence yet.

**One thing to do:** open EFF's *Cover Your Tracks* in your browser. Thirty seconds. It shows what can be deduced about your device from the connection alone, before any account, cookie, or login.

{{< source-list >}}
