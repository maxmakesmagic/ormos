---
id: aqf9d7m9
kind: article
lang: en
path: /en/articles/mtg-arena/2023/07-31-on-whiteboards-naps-and-living-breakthrough
title: On Whiteboards, Naps, and Living Breakthrough
published: '2023-07-31'
column_slug: mtg-arena
column: MTG Arena
authors:
- slug: alex-werner-e48db04f
  name: Alex Werner
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    lang_detected: en
    capture_id: 243399
    url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    captured_at: '2024-05-20 07:04:44+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    lang_detected: en
    capture_id: 243399
    url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    captured_at: '2024-05-20 07:04:44+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    lang_detected: en
    capture_id: 243399
    url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    captured_at: '2024-05-20 07:04:44+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    lang_detected: en
    capture_id: 243399
    url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
    captured_at: '2024-05-20 07:04:44+00'
    rule: url.article_section
sources:
- document_id: aqf9d7m9
  url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
  page_key: magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
  lang: en
  template: contentful
  captured_at: '2024-05-20 07:04:44+00'
  capture_id: 243399
  wayback_url: https://web.archive.org/web/20240520070444id_/https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: aqf9d7m9
  capture_id: 243399
  url: https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
  wayback_url: https://web.archive.org/web/20240520070444id_/https://magic.wizards.com/en/news/mtg-arena/on-whiteboards-naps-and-living-breakthrough
  captured_at: '2024-05-20 07:04:44+00'
  template: contentful
  sha256: 8aa0bb75ad395c27322a600a41c56ad2f840b34d7b23826bbb22aa967db77707
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: https://youtube.com/embed/WtEbGCYClmg
  reason: The preview omitted the iframe that loads this separate page.
  labels:
  - Whiteboards and Naps (1 of 2)
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://youtube.com/embed/jXDB1R_n_sA
  reason: The preview omitted the iframe that loads this separate page.
  labels:
  - Whiteboards and Naps (1 of 2)
  occurrences: 1
---
Hello, internet! My name is Alex Werner, and I've been a developer on the rule team of *Magic: The Gathering Arena* since September of 2021. I thought you all might enjoy a peek into the *MTG Arena* rules engine and into the job of those of us who make sure that hundreds of new *Magic* cards added each year work with the thousands of cards that already exist.

## *MTG Arena* Is Just GRE-at!

So first, a quick summary of how the rules engine works. When a game of *Magic* is in progress on *MTG Arena*, the program that is tracking the state of the game and enforcing all the rules-correct card interactions is called the Game Rules Engine (GRE). It's one of the two main programs that we work on. It's written in a combination of C++ and a language called CLIPS, which is a variant of LISP.

What does the GRE do? Well, for the most part, it just knows the basic rules of *Magic*:

*   It knows which player gets priority and when.
*   It knows that creatures die when they have lethal damage.
*   It knows how to move between the phases of a turn.
*   It knows the steps of casting a spell.

What it does not know is what any of the thousands of individual *Magic* cards do.

You can imagine writing a rules engine for *Magic* that actually knows about all the cards … and how it would get out of control quickly. Imagine a function determining whether a player can play a particular land. So that one function would have to have code for Fastbond. And code for Explore. And code for Solfatara. And code for Crucible of Worlds. All those bits of code would have to interact with each other properly. Every new card printed that had anything to do with what lands are or are not allowed to be played with would make that function even more complicated. It would be a nightmare.

Instead, *MTG Arena*'s model is what I like to think of as "naps and whiteboards." I envision the GRE as a very industrious little worker who takes frequent naps. For instance, let's say that Day of Judgment starts resolving. The GRE goes to their whiteboard and writes:

### TO DO

*   Destroy Darksteel Colossus.
*   Destroy Cityscape Leveler (that was unearthed).
*   Destroy Grizzly Bears.
*   Destroy Sanctuary Warden.

Then, the GRE goes off and takes a nap.

While they're napping, the "CLIPS rules" leap into action. These are the little bits of code that make all the specific abilities of individual *Magic* cards work. They are in the CLIPS language, because this sort of flexibility is precisely what CLIPS is designed for.

So first, the CLIPS rule for indestructible comes in and erases "Destroy Darksteel Colossus" off the whiteboard entirely. Then, the CLIPS rule for unearth comes in and replaces "Destroy Cityscape Leveler" with "Exile Cityscape Leveler." Then the CLIPS rule for shield counters comes in and replaces "Destroy Sanctuary Warden" with "Remove a shield counter from Sanctuary Warden."

Then, the GRE wakes up from its nap and looks at the whiteboard, which now reads:

TO DO

*   Exile Cityscape Leveler (that was unearthed).
*   Destroy Grizzly Bears.
*   Remove a shield counter from Sanctuary Warden.

And it does those things. The key here is that the GRE neither knows nor cares how many CLIPS rules came along and modified the contents of the whiteboard while it was napping. If we print a *Magic* card next year which reads, "When this creature would be destroyed, instead you win the game," and the GRE comes back from its nap to see "Player 1 wins the game," it will just do that. It doesn't care.

Let's look at one more example, which will be more relevant to the story I'm telling. In addition to to-do lists while resolving spells or abilities, one of the things the GRE is constantly doing is assembling a list of available actions for a player who has priority.

So, Player 1 has priority. The GRE writes on the whiteboard:

### AVAILABLE ACTIONS FOR PLAYER 1

*   Cast Lightning Bolt (from hand).
*   Play Swamp from hand.
*   Activate Icy Manipulator.

And then the GRE takes a nap. Again, the CLIPS rules go to work. It turns out that Player 1 cast Yawgmoth's Will earlier this turn. So, the CLIPS rule for Yawgmoth's Will shows up and adds "Play Forest (from graveyard)" and "Cast Lightning Bolt (from graveyard)" to the whiteboard. But … Meddling Mage naming Lightning Bolt is in play, so the CLIPS rule for Meddling Mage comes up and erases "Cast Lightning Bolt (from hand)" and "Cast Lightning Bolt (from graveyard)" from the whiteboard.

And then the GRE wakes back up from their nap, sees the finalized list of available actions, and sends it off to Player 1, who sees the Forest in their graveyard highlighted and playable, but neither of their Lightning Bolts are playable.

What's important about this is that the GRE has no idea that either Yawgmoth's Will or Meddling Mage exists, and neither one of them knows anything about the other. There's no special case code to make sure Meddling Mage and Yawgmoth's Will work together. But if each of them generates well-behaved CLIPS rules, they all work together seamlessly.

## The Story of Living Breakthrough

So, let's move on to today's story, which is about the most memorable card I've ever worked on. The card is Living Breakthrough from *Kamigawa: Neon Dynasty*, and it has this ability: **"Whenever you cast a spell, your opponents can't cast spells with the same mana value as that spell until your next turn."** This was one of the very first cards I worked on at least partially on my own, so I remember it well.

Now we come to the other program that we rules engineers spend our time working on, along with the GRE, which is the Game Rules Parser (GRP). This program (written in Python) takes raw English rules text of *Magic* cards and converts them into one or more CLIPS rules. It's what allows 80% or so of newly written *Magic* cards to just work in *MTG Arena* automatically. It's also what we have to update, modify, and improve to get the other 20% to work. Living Breakthrough was in that 20%, because we'd never had a card that forbade specific mana values of spells from being cast.

Fortunately, most of the components were already in place. We already knew how to trigger off cards being cast and how to prevent spells from being cast if they met conditions. So, I added code to the GRP to hook all those bits up, and quickly I had the GRP producing three CLIPS rules for Living Breakthrough.

Using our whiteboard analogy from above, the three rules were something like:

1.  *Whenever a player casts a spell, and they control Living Breakthrough, post a reminder note reading "Living Breakthrough notes that Player 1 cast Lightning Bolt."*
2.  *As a player starts their turn, get rid of any of these notes about spells they cast (this provides the "until your next turn" duration).*
3.  *Most interestingly: when we're calculating available actions for a player, if any of the spells they might cast have the same mana value as a spell mentioned in one of these notes from step 1, and if the player referred to in that note is their opponent, then cross that spell off the list of available actions.*

I'd done it! But, of course, it's important to always check our work. The next step was to write a "regression test," which is a little scripted game of *Magic* that checks that the card is functioning properly. That's where I ran into a very unexpected hurdle.

## Lore Counter I: The Story Keeps Going

I wrote a regression test for Living Breakthrough. It started out like this:

1.  Player 1 puts Living Breakthrough into their hand.
2.  Player 1 casts Living Breakthrough.
3.  Player 1 casts Lightning Bolt.

Now, I was entirely ready for this test to fail down in line 6 or 7, when I would verify that Player 2 was properly allowed (or not allowed) to cast spells based on what Player 1 had done.

What I was not expecting was for the test to fail on line 1, "Player 1 puts Living Breakthrough into their hand." But it did! Repeatedly. I double-checked everything. Did I spell the name of the card wrong? Do I need to do a full rebuild? Nothing fixed it. So, I did what every new-to-a-job developer tries to avoid, which is ask a senior developer a potentially really stupid question. Why could I not put Living Breakthrough into Player 1's hand?

The answer, as some of you have probably realized, is that Living Breakthrough isn't a card that can ever be in anyone's hand—it's the back face of the double-faced Saga, Inventive Iteration!

![Inventive Iteration](https://media.wizards.com/2021/neo/en_90nKwZ2M2y.png)

![Living Breakthrough](https://media.wizards.com/2021/neo/en_jFmT5B4Vt2.png)

Inventive Iteration

Which is, when you think about it, kind of wild. I was working on a card, and I didn't even know the most basic thing about the card. It's one of the funny quirks of our job that we work on the tricky bits of a card's ability text, and basic things like how much it costs, power and toughness, instant versus sorcery, usually don't matter at the time. It's always a bit jarring to have worked on a card for days or even weeks, finally get it all done, move on to something else, and then later you see it in action in a playtest and—holy mackerel—that card actually has power! And toughness! And art!

But, back to the story. I changed my regression test to cast Inventive Iteration, wait three turns, verify that Living Breakthrough was on the battlefield, and then start casting spells.

And, to start with, it all looked good. Player 1 cast Lightning Bolt. Player 2 then could not cast Lightning Bolt but could cast Runeclaw Bear. The effect wore off properly at the end of the correct turn. It continued to apply if Living Breakthrough left the battlefield, etc. Victory!

It turns out there was a BIG problem still. Given my description above of the CLIPS rules that I was generating for Living Breakthrough, I'm curious if any of you can figure out what it was. And while you're doing that, to fit the theme of this story, I'll take a nap.

## Lore Counter II: The X Factor

The problem was X spells. My CLIPS rules were saying "there's a spell that you might be able to cast, but it has the same mana value as a mana value I have forbidden, so I'll cross that off the list." But, that meant if Player 1 cast Lightning Bolt and Player 2 had Stream of Life in their hand, the CLIPS rule would look at the mana value of Stream of Life, see that it was 1, and forbid the casting of Stream of Life entirely. Which is clearly wrong.

So, the CLIPS rules had to become more complicated.

We amended rule #3 as follows:

3.  *When we're calculating available actions for a player, if any of the spells they might cast have the same mana value as a spell mentioned in one of these notes from step 1, **and if that spell does not have X in its cost**, and if the player referred to in that note is their opponent, then cross that spell off the list of available actions.*

And added rule #4:

4.  *When a player is about to choose the X value for a spell, if any of those Living Breakthrough notes apply to them, then see if any possible value of X would cause the spell to add up to the disallowed mana value. If so, disallow that value of X.*

Note that this is a bit trickier than it might initially sound, because not all X spells have as simple a mana cost as Stream of Life. For instance, if you are forbidden from casting spells with mana value 7, and you have Empty the Pits in your hand, what value of X is forbidden to you? None! Empty the Pits always has an even mana value. But what if the forbidden value is 2, which is even. Now what value of X is forbidden? Still none, as Empty the Pits always has a mana value of at least 4.

And I had another, more fundamental, problem: the GRE did not support asking a player to choose X with certain values disallowed.

## Lore Counter III: Duel Shot

This meant that I had to get the Duel Scene (DS) team involved. This is another team of programmers who work on the client in tandem with the GRE. Specifically, they work on what we call the "duel scene"—that is, an ongoing game of *Magic* (as opposed to deck building, drafting, etc.).

We work very closely with the DS team because the GRE is constantly coming to points in a *Magic* game in which it needs a player to make a decision. It sends a message asking the client to make a choice, and it's the responsibility of the DS team to display that choice to the user, which they do in a variety of different ways, sometimes highlighting creatures on the battlefield, sometimes popping up a dialog of some sort, sometimes displaying various buttons, etc.

Previously, when the GRE needed a player to choose an X value, we would send them a message saying, "Have the player pick an X value. Here's a maximum and minimum legal value."

Now the message needed to say, "Have the player pick an X value. Here's a maximum and minimum legal value and a list of values that are specifically not allowed." 

This required a fair bit of work on my side and on DS's side. But it was just "normal programming" rather than anything related to the game of *Magic*, so I'll skip the details. 

## Returned to the Battlefield: The Other X Factor

I was feeling QUITE confident. Every spell I was testing worked. X spells worked. So, I wrote a few more tests just to cross the t's and dot the i's, and … I stumbled upon another bug.

It was frankly pure luck that I found it. One of the cards I was using in my little script was Endless One because it's a spell whose entire mana value is X. I was mainly using it on Player 2's side to verify when a player could or could not cast Endless One for various values of X if their opponent had resolved some Living Breakthrough triggers. But, because I had already loaded it into the regression test, and because it's an easy way to cast a spell of any mana value, I was also using it for Player 1.

Something funny happened. Basically, I had a script that looked something like this (Player 1 controls Living Breakthrough):

1.  Player 1 casts Endless One for 5.
2.  Put the Living Breakthrough trigger on the stack.
3.  With the trigger still on the stack, Player 2 can cast spells with a mana value of 5.
4.  Living Breakthrough trigger resolves; Endless One is still on the stack.
5.  Player 2 now cannot cast spells with a mana value of 5.
6.  Endless One resolves.
7.  Player 2 still cannot cast spells with a mana value of 5.

But, the final step started failing. Player 2 was allowed to cast spells with mana value 5 the moment Endless One resolved, even though the effect should have lasted a full turn cycle. What was happening?

Well, let's revisit our very first CLIPS rule, and elaborate on it a bit:

1.  *Whenever a player casts a spell, and they control Living Breakthrough, post a reminder note reading, "Living Breakthrough notes that Player 1 cast Lightning Bolt."*

To be a bit more precise, this rule really read something like:

1.  *Whenever a player casts a spell, and they control Living Breakthrough, post a reminder note reading, "Living Breakthrough notes that Player 1 cast spell #278."*

When any of the other rules were testing whether a spell should be allowed, they "looked up" spell 278 to see what its mana value was. We have a nice system for finding last-known-information about spells that resolved in the past, so it all worked fine.

Except … there's a funny wrinkle in *Magic* rules: as a permanent spell resolves and moves from the stack onto the battlefield, it's still—at least in some ways—"the same object." It's not fully the same object, but it's kinda sorta the same object. We tracked that by having that object keep its ID number. So, when one of the other CLIPS rules was checking whether a player should be allowed to cast a spell, it was looking at the posted reminder, seeing "oh, Player 1 cast spell #278," and then saying "hmm, and what is the mana value of spell #278?" It got back that the current mana value of Endless One on the battlefield was, of course, 0!

(The same thing would have happened if Player 1 had cast Clone, and then cloned a Grizzly Bear; the mana value being forbidden would be 2 instead of 4.)

So, I had to go back in and subtly change the format of the little blob of posted information from "Living Breakthrough wants you to know that Player 1 cast spell # 278" to "Living Breakthrough wants you to know that Player 1 cast a spell with mana value 5." I made that change and, finally, all my tests passed.

## Wait—There's More? QA Gonna QA

Any of you who have worked in software development can guess what happened next: I handed this issue off to our QA team and … they found a bug. Fortunately, it was just a minor one; the interaction with Omniscience and similar effects. If a player is going to cast an X spell via Omniscience, the X value will always be 0. In that case, the "normal" condition should apply.

So, I amended rule #3 even further to:

3.  *When we're calculating available actions for a player, if any of the spells they might cast have the same mana value as a spell mentioned in one of these notes from step 1, and if that spell does not have X in its cost, **or if they are casting it without paying its mana cost**, and if the player referred to in that note is their opponent, then cross that spell off the list of available actions.*

And with that, there were, as far as I know, no more bugs.

## Epilogue

That's pretty much the end of my Living Breakthrough story. But I have two final notes:

First: While this turned out to be an awful lot of work for one card, almost none of the work we ever do is just for one card. Yes, I had to handle a bunch of cases and so forth, but all the work I did (assuming I did it right) was not to make Living Breakthrough, specifically, work. Rather, it was to support cards which forbid a player from casting a spell with a specific mana value. So, if a new card comes out in the next set that says, "Your opponents can't cast spells with mana value equal to the number of creatures you control" or "When this card enters the battlefield, choose a number. Players can't cast spells with mana value equal to that number," it *should* just work straight out of the card file with no effort on our part.

Second: Remember how I mentioned that the Duel Scene team added an interface for a player picking an X value with certain values forbidden? Well, after all the time and effort I put into making Living Breakthrough work, I have yet to see that interface. I have no idea what it looks like. We do all our rules development without a graphical client at all, just little scripted text games. And despite playing a ton of *Kamigawa: Neon Dynasty* Limited, I've never happened to have Spinning Wheel Kick in hand when my opponent has triggered Living Breakthrough. So, it may remain a mystery to me ... perhaps forever.