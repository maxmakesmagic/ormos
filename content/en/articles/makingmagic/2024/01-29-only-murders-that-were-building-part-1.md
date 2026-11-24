---
id: xgpk07my
kind: article
lang: en
path: /en/articles/makingmagic/2024/01-29-only-murders-that-were-building-part-1
title: Only Murders That We're Building, Part 1
published: '2024-01-29'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    lang_detected: en
    capture_id: 225255
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    captured_at: '2024-05-18 01:00:14+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    lang_detected: en
    capture_id: 225255
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    captured_at: '2024-05-18 01:00:14+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    lang_detected: en
    capture_id: 225255
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    captured_at: '2024-05-18 01:00:14+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    lang_detected: en
    capture_id: 225255
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
    captured_at: '2024-05-18 01:00:14+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: xgpk07my
  url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
  page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:00:14+00'
  capture_id: 225255
  wayback_url: https://web.archive.org/web/20240518010014id_/https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: xgpk07my
  capture_id: 225255
  url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
  wayback_url: https://web.archive.org/web/20240518010014id_/https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-1
  captured_at: '2024-05-18 01:00:14+00'
  template: contentful
  sha256: bfb72f77edcd416d24f9b0e1b27f583dec8c1189a94b04c9ee1ce4c333b3e59b
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
Over the last two weeks ([Part 1](/en/articles/makingmagic/2024/01-16-getting-away-with-murders-at-karlov-manor-part-1) and [Part 2](/en/articles/makingmagic/2024/01-22-getting-away-with-murders-at-karlov-manor-part-2)), I told design stories from *Murders at Karlov Manor*. Today, I'll start telling my card-by-card design stories from the set. This time, I decided to try something a little different. I went to [Blogatog](https://markrosewater.tumblr.com/), my blog, and asked the community which *Murders at Karlov Manor* card design stories they wanted to see. This week and next, I'll cover some of those cards.

**Archdruid's Charm**

![Archdruid's Charm](https://media.wizards.com/2024/mkm/en_2330345e1f.png)

Before I was a designer for *Magic*, I was a developer. In my early days, R&D was small, so I (along with Bill Rose, Mike Elliott, William Jockusch, and eventually Henry Stern) were on every development team. Note that this is before the shift to the vision, set, and play design model we use today. One day, during a *Mirage* development meeting, I made an important discovery. There was a green creature in the file that let you sacrifice untapped forests to get +2/+2 until end of turn. I realized that "sacrifice an untapped forest" was basically the same as "G, sacrifice a forest." That meant the card I was looking at was an Atog!

![Atog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=1058&type=card)

The original Atog was a red creature from *Antiquities*, *Magic*'s second expansion. When the set came out, there was a huge backlash against the card, but I thought it was pretty good, so I made an artifact deck built around it, and I was right. It was quite good, especially for the power level of creatures back in the day. I championed it wherever I could. It became my first favorite card.

So, when I realized that *Mirage* had a card that was essentially an Atog mechanically (i.e., it ate a resource to get a boost until end of turn), I insisted that we make it an Atog. Once that happened, I had a quest. I was going to keep putting Atogs in sets until we had one of every color.

![Foratog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3386&type=card) ![Chronatog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3635&type=card) ![Necratog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=4464&type=card)

![Auratog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=4862&type=card) ![Atogatog](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=31834&type=card)

So, each of the next three sets had one. I even made a five-color Atog that ate Atogs to go into *Unglued 2*. That product was cancelled, so I put it in *Odyssey* after we added five ally-color Atogs to that set.

Skip ahead to *Stronghold* design, the second set in the *Tempest* block. The story took place in Volrath's Stronghold (it's why the set was called *Stronghold*), and I really wanted to make a legendary land for it. I'd remembered that in *Mirage*, we made Teferi's Isle as a single legendary land that created blue mana. Inspired by my success with the Atogs but thinking bigger, I came up with an idea that I called the "mega-mega cycle." We would print a card from a cycle once each block for five years.

![Teferi's Isle](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3576&type=card) ![Volrath's Stronghold](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=5263&type=card) ![Yavimaya Hollow](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=15772&type=card)

![Keldon Necropolis](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=25930&type=card) ![Kor Haven](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=21403&type=card)

That opened the floodgates. Once R&D understood that we could do cycles that carried over years, we started doing all sorts of things. I should note that not all mega-mega cycles start as cycles. Sometimes we make a card, or two, and then later get inspired to make more. That brings us to Archmage's Charm from *Modern Horizons*.

![Archmage's Charm](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=463989&type=card)

*Modern Horizons* is filled to the gills with callbacks, so my gut is this card wasn't designed as the start of a new mega-mega cycle, but I'm not sure, as I wasn't on the Set Design team that made it (I was only on the Vision Design team). Anyway, here's how the second card made it into *Murders at Karlov Manor*. We'll begin with the earliest card design in its rare green slot.

**A Bout of Fisticuffs (version 1)**  
 4G  
 Sorcery  
 Target creature you control fights target creature you don't control. If there have been two or fewer fights this turn, you may copy this spell and cast the copy without paying its mana cost.

Yes, when the set began, this wasn't Archdruid's Charm. It was a completely different card, a take on a rare fight card. The intent was to let the player fight exactly three times. This version lets the player fight with the same creature multiple times, provided it survives, and keeps them from copying the spell.

**A Bout of Fisticuffs (version 2)**  
 G  
 Sorcery  
 Target creature you control fights target creature you don't control. If the creature you control deals excess damage this way, you may exile CARDNAME. If you do, you may cast it from exile this turn by paying 1G rather than its mana cost.

I think the triple fight was a little too much, so we tried a card that let the player fight twice, although it made players a bit pickier about their first fight. I assume if we made this card now, it would just have flashback, as it's now deciduous.

**Archdruid's Charm (version 3)**  
 GGG  
 Instant  
 Choose one —  
 • Search your library for a basic land card, put it onto the battlefield tapped, then shuffle.  
 • Target creature you control gets +1/+0 until end of turn. It fights target creature you don't control.  
 • Destroy up to one target artifact and up to one target enchantment.

In set design, they gave up on the fight card and someone had the great idea of starting a new mega-mega cycle. The trick with any cycle is figuring out what carries through the cycle. As this was the second card, it would do a lot to define this throughline. In the end, we decided it just needed to cost three colored mana, three green in this case, and be a powerful rare charm.

You can see that from the very beginning they had a sense of the three things they wanted to do—fetch land, destroy a creature through a green means, and deal with an artifact or enchantment. Let's walk through the evolution of each one.

**Fetch a land** – This started as simply the effect from the card Rampant Growth (tutor a basic land and put it on the battlefield tapped). If this was a normal charm, that would be fine, but this is an Arch\_\_\_\_\_\_'s Charm. We had to kick it up a notch. Instead of just tutoring for a land, the effect could now also tutor for a creature. Because creatures are usually more powerful than lands, the tutored creature would have to go to your hand. Also, the word basic was dropped to let you get any land.

**Destroy a creature through green means** – The effect started as a "fight" spell with a temporary power boost. Again, the team kicked it up a notch. Now it's a +1/+1 counter instead of a temporary boost, and it's a "bite" effect (i.e., it just deals damage) rather than a "fight" effect.

**Deal with an artifact or enchantment** – This is the effect that one could argue was powered down a touch. Yes, it now exiles instead of destroys, which is an upgrade, but the previous version could get rid of an artifact and an enchantment. Now you can only get rid of one or the other.

Does this mean that there are three more Arch\_\_\_\_\_\_'s Charms to come? Yeah. Once we make two cards, we understand the expectation we set up. Mega-mega cycles are just something that's become normal business since the days of the Atog and legendary land cycles. How soon will you see them? I can't say, but my gut says there will be less than a five-year gap between each one.

Finally, here's the art description for the card:

**\*\*\* EXTENDED-ART ASPECT RATIO \*\*\*  
 Setting**: "Polo"  
 **Color**: Spell associated with green mana  
 **Location**: Unimportant/abstract  
 **Intent**: This is part of a cycle of "charm" cards associated with powerful mages. They all depict a magical amulet shown in front of a magical effect rather than a literal background. See attached reference for an example of how this was depicted for a blue-aligned spellcaster's amulet.  
 **Action**: We'd like you to design a magical amulet used by an archdruid, a powerful caster of green magic. In *Magic*, green is all about nature, interdependence, and instinct. The amulet pulses with intense green magic that pushes back a surrounding aura of malevolent purple magic, completely rejecting this other color of magic that is its enemy.  
 **Focus**: The charm  
 **Mood**: All of nature's power and wisdom in this amulet

**Magnetic Snuffler**

![Magnetic Snuffler](https://media.wizards.com/2024/mkm/en_96c595b845.png)

I have fun writing these articles because I get to go into our database and look at the history of the cards. This card's evolution was a short one, so I would usually skip it, but it revealed a card that we didn't make that I wanted the opportunity to show off. Without further ado, here's the first card to be in Magnetic Snuffler's uncommon colorless artifact slot:

**Mystery Machine (version 1)**  
 5  
 Artifact — Vehicle  
 6/6  
 Cloak 3 *(You may cast this card face down as a 3/2 creature for {3}. Turn it face up any time for its cloak cost.)*  
 Crew 3 *(Tap any number of creatures you control with total power 3 or more: This Vehicle becomes an artifact creature until end of turn.)*

When we start exploratory design, one of the things we normally do for any top-down set is make a list of all the pop culture references people would have about it. Well, if you're talking about the mystery genre, there's a certain cartoon that many people grew up with. The set does reference it in the card Meddling Youths.

![Meddling Youths](https://media.wizards.com/2024/mkm/en_f6d4f21052.png)

The show in question also has a famous vehicle, so this slot started as a reference to that. Normally when we put a Vehicle in a set, we look for ways to embody the mechanics or themes of the set. Well, one of the downsides of Vehicles is that they're often not usable early. Well, what if the set had a mechanic that let you do something else with it early? I want to remind everyone that disguise for most of the set's design was called cloak, so this card basically has disguise. This is early in vision design, so it has the disguise where the creature is a 3/2 rather than a 2/2 with ward 2. I assume we gave it crew 3 to match with the cloak number. I'm not sure why the cloak number is written out though. It was always 3.

**Mystery Machine (version 2)**  
 5  
 Artifact — Vehicle  
 6/6  
 As CARDNAME is turned face up, it becomes an artifact creature until end of turn.  
 Cloak — {3}, *(You may cast this card face down for {3} as a 2/2 creature with ward {2}. Turn it face up any time for its cloak cost.)*  
 Crew 3 *(Tap any number of creatures you control with total power 3 or more: This Vehicle becomes an artifact creature until end of turn.)*

So, we playtested this card. Someone played it face down. They then attacked, and mid-attack, turned the card face up. This prompted a question. Is this a creature? The answer was no, but it was unclear to enough people that we changed it so that it was a creature. This is a good example of tweaking cards so that they play as expected.

**Metal Detector (version 3)**  
 Artifact Creature — Construct  
 3/3  
 When CARDNAME enters the battlefield, return target Clue Equipment card from your graveyard to the battlefield and attach it to CARDNAME.  
 Whenever an Equipment card is put into your graveyard from anywhere, create a 1/1 colorless Thopter artifact creature token with flying.

We gave up on the Vehicle. It just wasn't recognizable enough and didn't make sense on Ravnica. Plus, we had the Meddling Youths card. We made the new card to work with a cycle of uncommon Equipment tied to the game *Clue*. We realized that we could use five of the six weapons to make a cycle of Equipment cards that are also Clues (as in Clue, the artifact subtype). The design was made to encourage playing any Equipment but gave you an extra bonus for using the Clue Equipment. The reward of a flying 1/1 Thopter token was useful but an odd flavor choice.

**Metal Detector (version 4)**  
 Artifact Creature — Construct  
 3/3  
 When CARDNAME enters the battlefield, return target Equipment card from your graveyard to the battlefield and, if that Equipment was a Clue, attach it to CARDNAME.  
 Whenever you sacrifice a Clue, put a +1/+1 counter on CARDNAME.

The next version still rewarded you for having a Clue Equipment but made the card generally more useful for any Equipment. While we broadened the first ability, we narrowed the second, now caring specifically about Clues. Playtesting showed both parts were too narrow, so the final card was made a bit more general. Yes, it worked with Clue Equipment and Clues, but also with any Equipment or artifact sacrifice.

Finally, here's Magnetic Snuffler's art description:

**Setting**: "Polo" Ravnica  
 **Color**: Artifact creature not associated with any color of mana  
 **Location**: An exterior city park (See pages 8–11 and 150–151 for general Ravnican environments.)  
 **Action**: Design a fantastical metal anteater who's basically a sentient metal detector. Its snout ends in a flat, wide dish that lets it magically sense metal. It digs in the ground where it just sensed something, unearthing a hastily disposed-of dagger.  
 **Focus**: The anteater  
 **Mood**: Cute and mindless

**Massacre Girl, Known Killer**

![Massacre Girl, Known Killer](https://media.wizards.com/2024/mkm/en_73b3151d78.png)

Normally, exploratory design begins long before all the story beats are figured out. In fact, when we started working on *Murders at Karlov Manor*, the story team hadn't figured out who the victim or culprit was. Then in the middle of vision design, we decided to use Ravnica as the setting instead of a new plane. So, suffice to say, it wasn't quite clear, even during vision design, exactly who was murdered and who was murdering, but we had some fun guessing at what we might do.

Then, we had the funny idea to make Massacre Girl the first suspect. Killing is kind of her thing. We liked the vibe of "yeah, I could have done it, but no, really, this wasn't me."

Massacre Girl first showed up as a character in the novella tied to *Return to Ravnica* ([*In Praise of the Worldsoul, Part 1*](/en/articles/magic-story/2012/09-25-in-praise-of-the-worldsoul-part-1), [*Part 2*](/en/articles/magic-story/2012/10-03-in-praise-of-the-worldsoul-part-2), and [*Part 3*](/en/articles/magic-story/2012/10-09-in-praise-of-the-worldsoul-part-3)). Because the stories are written after the set is designed, she didn't appear anywhere in the *Return to Ravnica* block. Because she was a much beloved character, we got a lot of requests to make a card for her. We were finally able to do it in *War of the Spark*.

![Massacre Girl](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=461026&type=card)

The card proved to be as popular as the character. Once we knew this set was going to be on Ravnica, we knew we had to make a new card for Massacre Girl. How can you make a murder mystery set without Massacre Girl?

But what should her card do? First, it had to feel like Massacre Girl, which meant some killing would be involved. Second, we really wanted something players could build around. Commander is the most played tabletop format, so when we make cards for popular legendary characters, we think about their ability to be built around. Here's our first stab at the design:

**Massacre Girl, with No Alibi (version 1)**  
 3BB  
 Legendary Creature — Human Assassin  
 4/4  
 Each creature you don't control has "*Foul play* — Whenever a creature card or creature token is put into your graveyard from anywhere, this creature gets -1/-1 until end of turn."

Foul play was a morbid variant that we had in the set for a while. The version on the card was one where any creature card going to the graveyard from any zone triggered it (this would include things like milling or discard). Tying Massacre Girl to foul play seemed flavorful, and the output being temporary -1/-1 effects was a nice callback to her first card. I assume we started with 3BB for a 4/4 for the same reason.

**Massacre Girl, Obviously Shady (version 2)**  
 1BB  
 Legendary Creature — Human Assassin  
 3/3  
 Menace  
 Whenever another creature dies, or a creature card is put into a graveyard from anywhere other than the battlefield, another target creature gets -1/-1 until end of turn.

The first version only triggered on an opponent's creature going to the graveyard. This second version triggered off any creature, which increased players' ability to build around it. We also made her a bit cheaper and smaller and gave her menace (her first card had menace). While we want legendary creatures to be roughly the same size, we don't feel it always has to match exactly.

**Massacre Girl, Too-Obvious Suspect (version 3)**  
 1BB  
 Legendary Creature — Human Assassin  
 3/3  
 Menace  
 If a nontoken creature an opponent controls would die, instead exile that card with a torment counter on it. For as long as it remains exiled, it has "At the beginning of your upkeep, you lose 1 life" and "3: Put this card into your graveyard from exile."

The next version tried a very different take. This version basically punished opponents for having creatures die. The opponent was taxed through a combination of mana and life payments. While this isn't the path we ultimately chose, I do admire the design.

**Massacre Girl, Too-Obvious Suspect (version 4)**  
 BB  
 Legendary Creature — Human Assassin  
 2/2  
 Menace  
 If a creature an opponent controls would die or a creature card not on the battlefield would be put into an opponent's graveyard, instead exile it with a torment counter on it. When you do, it gains "At the beginning of your end step, you lose 1 life" and "{o2}: Put this card into your graveyard from exile."

This "punish death" version of Massacre Girl stuck around for a while and made her even cheaper and smaller. I believe "nontoken" was removed because it wasn't necessary. Tokens vanish when they hit another zone. Playtesting showed that the tax was a little too high, so it was lowered from 3 to 2.

**Massacre Girl, Prime Killer (version 5)**  
 3BB  
 Legendary Creature — Human Assassin  
 4/5  
 If a creature you control would deal damage to another creature, that creature gets -X/-X until end of turn instead, where X is the damage that would be dealt. Whenever a creature an opponent controls dies, if it had 0 or less toughness, each player loses 1 life and you draw a card.

What ultimately got the card changed was that it didn't feel enough like Massacre Girl. Massacre Girl is all about killing things. The "punish death" version rewarded killing, but Massacre Girl wasn't responsible for it. This new version turned all your creatures into killers and then rewarded you when they killed creatures. It was at this point someone said, "Aren't we basically giving the creatures wither. Why don't we just say that?"

For those unaware, R&D has a rule that we don't like mixing +1/+1 counters with -1/-1 counters. It makes it hard, especially in Limited, to track the stats of creatures if both coexist. But this was one mythic rare card. We'd started experimenting with something we call "cameo cards" where we bring back an old mechanic on one card at a high rarity. What if we just thought of Massacre Girl as a cameo card? Yeah, it would make counters mix occasionally in Limited, but not often. Could we try it? We decided yes and put it in. We also brought menace back because Massacre Girl just feels like she should have it. For balance, we moved from 3BB 4/5 to 2BB 4/4 (which matched her original stats).

Finally, here's her art description:

**\*\*\* EXTENDED-ART ASPECT RATIO \*\*\*  
 Setting**: "Polo"  
 **Color**: LEGENDARY creature associated with black mana  
 **Location**: Seedy, shadowed environment in Bane Alley (pages 144–147)  
 **Intent**: Massacre Girl is one of the most obviously suspicious figures on Ravnica. We want to emphasize her suspiciousness with hard, layered shadows (see page 16 for examples).  
 **Action**: Show us MASSACRE GIRL, a notorious, gleeful killer (see attached references) jauntily twirling her signature dagger. Her face paint depicts a menacing snarl, but beneath it, her mouth is stretched in a huge grin. Maybe she's streaked with more red color as well, which could be either smears of paint or blood. Layered shadows stretch long behind her, giving a sinister appearance that contrasts sharply with the cheery confetti sprinkling down in the air.  
 **Focus**: Massacre Girl  
 **Mood**: Gleefully murderous. "Of course, I did it. What were you expecting?"  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, and (2) with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter eggs for cards printed with the extended aspect ratio.

## "When They Met, It Was *Murders*"

That's all the time I have for today. As always, I'm eager for any feedback you have on today's column, any of the cards I talked about, or *Murders at Karlov Manor* itself. You can email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two.

Until then, may you make your own stories with the cards of *Murders at Karlov Manor*.