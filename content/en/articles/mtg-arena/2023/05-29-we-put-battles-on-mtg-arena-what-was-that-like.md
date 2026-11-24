---
id: p54apxna
kind: article
lang: en
path: /en/articles/mtg-arena/2023/05-29-we-put-battles-on-mtg-arena-what-was-that-like
title: 'We Put Battles on MTG Arena: What Was That Like?'
published: '2023-05-29'
column_slug: mtg-arena
column: MTG Arena
authors:
- slug: ian-adams-1d137168
  name: Ian Adams
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    lang_detected: en
    capture_id: 243713
    url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    captured_at: '2024-05-20 19:52:38+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    lang_detected: en
    capture_id: 243713
    url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    captured_at: '2024-05-20 19:52:38+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    lang_detected: en
    capture_id: 243713
    url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    captured_at: '2024-05-20 19:52:38+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    lang_detected: en
    capture_id: 243713
    url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
    captured_at: '2024-05-20 19:52:38+00'
    rule: url.article_section
sources:
- document_id: p54apxna
  url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
  page_key: magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
  lang: en
  template: contentful
  captured_at: '2024-05-20 19:52:38+00'
  capture_id: 243713
  wayback_url: https://web.archive.org/web/20240520195238id_/https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: p54apxna
  capture_id: 243713
  url: https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
  wayback_url: https://web.archive.org/web/20240520195238id_/https://magic.wizards.com/en/news/mtg-arena/we-put-battles-on-mtg-arena-what-was-that-like
  captured_at: '2024-05-20 19:52:38+00'
  template: contentful
  sha256: 895c77f86b28a6d8b6e852b8bbea9d8e07217886ea47c6559fd8742dc74eaa02
render_recovery: []
---
A new card type! This is the kind of thing we only do roughly every fifteen years (give or take), so it seems like a good time to talk about what that requires. The short answer is, "a lot of work," but given that you've clicked on this article, I would assume you're looking for a more robust level of detail. That's what the rest of the paragraphs are for.

## What Exactly Is a Battle?

![Invasion of Tarkir](https://media.wizards.com/2023/mom/en_70513e45dc.png) 

![Defiant Thundermaw](https://media.wizards.com/2023/mom/en_e984275eb1.png) 

**Invasion of Tarkir**

![Invasion of Ikoria](https://media.wizards.com/2023/mom/en_d9fc7b122f.png) 

![Zilortha, Apex of Ikoria](https://media.wizards.com/2023/mom/en_66b182dc81.png) 

**Invasion of Ikoria**

![Invasion of Segovia](https://media.wizards.com/2023/mom/en_c591da8678.png) 

![Caetus, Sea Tyrant of Segovia](https://media.wizards.com/2023/mom/en_bb0efcebb0.png) 

**Invasion of Segovia**

Before we can do anything else with battles, we've got to get to a place where we can ingest the data. Battles have lots of things our parser knows how to handle, like a mana cost, a linked back face, and rules text, but it also has defense counters. Once that's in, we need to introduce a ton of new lexemes into the game rules parser. Basically, we need to teach the software what words like battle, protector, defense counters, and the concept of "defeating" a permanent mean when reading other cards.

At this point, we have a permanent, it has counters, it has effects upon entering the battlefield, it has unique language relevant to it, and it can be cast from exile. Once we update the combat manager to handle you attacking a permanent you control and a designated opponent blocking for that permanent, we're at a point where battles can at least kind of be played with, right?

![Battlefield screenshot showing the mouse hover expanded display of Invasion of Tarkir and it's back face, Defiant Thundermaw](https://media.wizards.com/2023/images/daily/screen_battles_battlefield.png) 

No, of course not! *Magic* always has at least a couple more layers of complexity.

We need to get the ability to damage and target battles directly. We need to create new hot/cold definitions for targeting because, unique among card types on *MTG Arena*, while destroying or exiling your own battle is still generally bad, damaging it is good. We need to ensure battles that have become creatures cannot participate in combat. We need to manage having those creature-battles being forced to transform. And almost all of this must be done twice because everything I'm saying applies to Sieges, the subtype of battles that appear in *March of the Machine*. We also wanted to make sure the non-Siege style of battles was rules-correct and behaved as you'd expect.

Now that we've finished all of this (actually, in parallel with a lot of the edge-case fixing, but for the sake of this article flowing in a coherent way), we get to start on the complicated half of battles.

## How Exactly Is a Battle?

While the rule side of battles is extremely complex, client presentation is where the type of work we must do fundamentally changes. Until now, the work has been complicated and required creative solutions, but the goal was clear: battles needed to function in a rules-complete way and use established *MTG Arena* paradigms around things like targeting.

From here, we have a lot of open questions. Battle cards are played horizontally in tabletop. Should they be horizontal on *MTG Arena*? What about on the battlefield? What about in your hand? In a browser? Battles are protected by your opponent, but you control them. Where should they sit on the battlefield. How does that impact combat clarity? How does that impact clarity when deciding to react to a spell cast by your opponent targeting that permanent?

"How do you even display these things" is something we started asking basically as soon as we saw the direction battles were taking. Fully horizontal all the time is a nonstarter on *MTG Arena*. It's awkward to read in hand, doesn't fit correctly on the stack, breaks a ton of visual effects that already exist, and is simply a case where the paper solution doesn't translate to digital ("just turn it sideways to read it" is fine for a card, but is not acceptable for someone's 49-inch ultrawide monitor, much less a smart phone).

The call here was that while there are a lot of places where the card needed to be modified into a vertical aspect, being horizontal was an important part of the identity of battles, and it helps communicate just how unique this new permanent is. The initial design here was:

*   Battlefield: horizontal
*   In hand: vertical
*   On the stack: vertical
*   Decks scene: vertical
*   Examined: horizontal

But after playtesting, it became clear that in many cases the Examined (that's the pop-up you get when mousing over or long pressing a card) actually needed to be contextual, because having a battle in a scry browser suddenly pop up sideways was distracting and did not help with clarity. So that changed to:

*   Examined
    *   In hand: horizontal
    *   Battlefield: horizontal
    *   Decks scene: horizontal
    *   In a browser: vertical

The good news is that a permanent being horizontal is so unique and distinctive that even being horizontal *pretty* often is enough to make them feel like The Special Horizontal Ones.

![Battlefield screenshot showing the Invasion of Ikoria examined in the player's hand](https://media.wizards.com/2023/images/daily/screen_battles_hand.png) 

Even having sorted that out, we were immediately hit with a lot of complications. Battles all have a back face, which means that we need a hanger with the back-face image so they're not just wide but wide *with an additional card hanging off the side*. Making the hanger look right on a sideways card with a vertical card hanging off of it took iteration, as did making it physically fit on all the different deck-building and drafting scenes.

## Where Exactly Is a Battle?

So, we've got battles (specifically Sieges). They work in the rules, we know what the cards look like in various contexts. We're set right? All we have to do is put it on the battlefield. Sure, but *where*?

In every single conversation we had about these, there were people passionate about the fact that there was a clear, obvious, fundamentally correct solution. Unfortunately, these people consistently disagreed. It was obviously better to have these cards, which are often played purely for their enters-the-battlefield effects, enter on your side as the casting player. It makes it clear who is the source of the ability, and beyond that, makes it obvious who owns this permanent and wants to protect it from removal or other interaction.

It was *also* obviously impossible to have them be on your side, because attacking a permanent on your side of the battlefield not only violates the fundamental paradigm of *Magic* combat as established in 1993 by Doctor Garfield, it also looks very silly.

The only certainty produced from these conversations came when I asked, "How bad would it be if they entered on your side, then moved to the protector's side during combat?" Finally, everyone agreed on something: it would be very confusing and distracting, would potentially shift around planeswalkers you were planning to attack, and I shouldn't have suggested such a thing.

So, we did the reasonable thing: we implemented both. The debug version of the client had a toggle you could flip to change which side of the battlefield the battles appeared on, and we ran a series of tests. The results of the tests were:

*   Sieges felt better when they entered the battlefield on their controller's side.
*   Combat felt better when Sieges were on the protector's side.

Canny readers will note that this is exactly what we knew going into the tests.

Fortunately, additional testing, including some sessions in which people switched halfway through the playtest, a pattern emerged: people were able to get comfortable with either side, but combat feeling right consistently ranked as the priority, and we had our answer.

![Screenshot showing of Invasion of Tarkir placement on the battlefield, in this situation on the opponent's side, in the upper-right area of the battlefield](https://media.wizards.com/2023/images/daily/screen_battles_general.png) 

Now all we had to do was rebuild the planeswalker zone to make sure that putting a battle onto your opponent's side of the battlefield doesn't immediately cause their planeswalkers to page off the screen. (I say that like it was easy, but Autumn and Warren did fantastic work in very short order getting this done, and Jeremy turned the designs around amazingly fast.)

## Why Exactly Is a Battle . . . Not Quite Finished Yet?

At this point, it should be obvious that—you guessed it!—we weren't done yet. Card-side VFX like indestructible and hexproof didn't fit. Many VFX weren't centered correctly because of the new ratio. We had to make sure you could tap this new wide shape (which doesn't generally do anything but is important for being rules-correct in some niche scenarios). Highlights had to be rebuilt for the new shape. We had to handle presentations where the battle gained other types. We had to make sure the token creature Adeline, Resplendent Cathar creates can attack a player or a planeswalker but *not* a battle. We even had to make sure that we had frames for token battles (which don't exist as printed objects in paper but *can* be created).

And then we had to make sure we could do token versions of the back faces. I'm sure the rule-savvy among you are saying, "But did you? When the token battle is exiled, it stops existing, so you can't actually cast the back face." Which is TRUE! But it's also true that people can use Encroaching Mycosynth to make the battle an artifact, then The Blackstaff of Waterdeep to make it a creature, then Arcane Adaptation to make it a Human, then Moonmist to transform it, and because of the changes to DFC token rules introduced for Incubator tokens, that token would then transform.

If any of you are wondering, "But is anyone going to actually play that?" I pose a counter question: Have you met *Magic* players? Yes. Yes, they will.

There's even more that went into getting battles into *MTG Arena*, but I wanted to make this article reasonably brief (I'm not convinced I've hit that target). A new card type, especially with a rules-bearing subtype, is an exceptionally high amount of work, but this is a pretty great example of how additional tasks fall out beyond the obvious work necessary to implement new mechanics. *Magic* is not just *a* complex game, it is *the most* complex game, and accounting for that, while trying to create a clear and consistent visual presentation that facilitates fast, fun digital play, is a huge lift that requires input and effort from a ton of people.

Fortunately, I assume we have fifteen or so years before we have to do quite this much work again.

## Want to Learn More from Behind the Scenes of *MTG Arena*?

Join Ian Adams for a Q&A session on [the *Magic* Discord channel](https://discord.gg/wizards-magic) Tuesday, May 30, from 1 p.m to 2 p.m. PT, where he'll talk about the development of battles on *MTG Arena* and answer your questions!