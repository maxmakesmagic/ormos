---
id: 91fne5jm
kind: article
lang: en
path: /en/articles/makingmagic/2024/04-29-bringing-the-thunder-part-2
title: Bringing the Thunder, Part 2
published: '2024-04-29'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    lang_detected: en
    capture_id: 212604
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    captured_at: '2024-05-18 00:57:41+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    lang_detected: en
    capture_id: 212604
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    captured_at: '2024-05-18 00:57:41+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    lang_detected: en
    capture_id: 212604
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    captured_at: '2024-05-18 00:57:41+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    lang_detected: en
    capture_id: 212604
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
    captured_at: '2024-05-18 00:57:41+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 91fne5jm
  url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
  page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 00:57:41+00'
  capture_id: 212604
  wayback_url: https://web.archive.org/web/20240518005741id_/https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 91fne5jm
  capture_id: 212604
  url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
  wayback_url: https://web.archive.org/web/20240518005741id_/https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-2
  captured_at: '2024-05-18 00:57:41+00'
  template: contentful
  sha256: 5f8972ce246a5475d1ebea4bf3f0061683f6d83ae58f12495a1f9445e1a3df26
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
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist?color=FFFFFF&background=30343C
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
[Last week](/en/articles/makingmagic/2024/04-22-bringing-the-thunder-part-1), I started telling card-by-card design stories for previously known legendary creatures that received new card designs in *Outlaws of Thunder Junction*. I have more stories to tell, so let's continue.

**The Gitrog, Ravenous Ride**

0206\_MTGOTJ\_Main: The Gitrog, Ravenous Ride 

We knew we wanted to do a mount mechanic. We also knew the set was going to have a lot of famous legendary visitors. Could we make those two goals intersect? The answer was yes, and everyone knew instantly what legendary creature we wanted. (We had already showed it being ridden on a card.)

The Gitrog Monster is a giant frog from Innistrad. He first came to prominence as a Frog Horror from *Shadows over Innistrad* and was mutated by Emrakul in the associated story. He would later team up with Thalia in *March of the Machine*.

**Gitrog Monster, Bronco (version #1)**  
 2BG  
 Legendary Creature — Frog Horror  
 4/4  
 Whenever a land enters the battlefield under your control, CARDNAME and its rider each gain +1/+1 and deathtouch until end of turn.  
 When CARDNAME's rider deals combat damage to an opponent, you may sacrifice it. If you do, draw cards equal to its power and gain life equal to its toughness.  
 Mount {oBoG} *({oBoG}: Attach to target creature you control; or detach from a creature. Mount only as a sorcery. The first time you activate it the turn it entered the battlefield, this ability costs {o0})*

Every version of The Gitrog Monster was made during set design. The mutate mount variant we handed off to the Set Design team (as I spelled out in [my preview column](/en/articles/makingmagic/2024/04-01-outlaws-of-the-land-part-2)) had gone away before the first Gitrog Monster was ever made. As you will see, the Set Design team tried a lot of different versions of a mount mechanic.

To be a mount, it needed a way for another creature to ride it, and then it needed some benefit for being ridden. This earliest version allowed the rider to attach to the creature with mount, much like how reconfigure worked in *Kamigawa: Neon Dynasty*. What impact that had was mostly spelled out on the card, not by the mechanic. This first version did make it free to use the mount ability the turn the creature entered the battlefield.

The Gitrog Monster was black and green, as those are the two colors from its two previous cards. (Thalia adds the white in the team-up.) This first version is trying to be as similar mechanically to its last two cards as possible: it references lands, it can gain deathtouch, and it has a sacrifice tied to card drawing. The first ability gives the bonus to the rider and the card with mount because the mechanic has a way for you to detach the rider. The second ability allows you to use the rider as a resource to draw cards.

**Gitrog Monster, Bronco (version #2)**  
 2BG  
 Legendary Creature — Frog Horror  
 5/5  
 Whenever a land enters the battlefield under your control, CARDNAME and mounted creature each gain +1/+1 and deathtouch until end of turn.  
 When CARDNAME's rider deals combat damage to an opponent, you may sacrifice it. If you do, draw cards equal to its power and gain life equal to its toughness.  
 Mount {o2oBoG} *(If you cast this card for its mount cost, it enters the battlefield attached to target creature. As a sorcery, you may pay its mount cost to attach it to target creature or detach it.)*

This next version mostly leaves the card the same, other than growing it to a 5/5. The big change is how mount works. In this version, a rider can only get on the creature when it's cast. It can still hop off at any time. It only took one playtest to see that this flavorfully didn't work. A rider should be able to get on and off his mount many times.

**Gitrog Monster, Bronco (version #3)**  
 2BG  
 Legendary Creature — Frog Horror Mount  
 4/4  
 Whenever a land enters the battlefield under your control, CARDNAME and mounted creature each gain +1/+1 and deathtouch until end of turn.  
 Whenever its rider deals combat damage to an opponent, you may sacrifice it. If you do, draw cards equal to its power and gain life equal to its toughness.  
 Mount {o2} *(Choose target creature you control as this creature's rider. It may have only one rider at a time. Tap this creature. It can't untap unless its rider dismounts. Activate only as a sorcery. Activate again to dismount for free.)*

You can see that we constantly fiddled with how big The Gitrog Monster was. This version is kind of mimicking Equipment and includes the subtype Mount in addition to the mount ability. To capture the rider and mount as one creature, this version of the mechanic taps the mounted creature. This time, we made detaching free.

**Gitrog Monster, Bronco (version #4)**  
 2BG  
 Legendary Creature — Frog Horror Mount  
 4/4  
 *Landfall* — Whenever a land enters the battlefield under your control, CARDNAME and its rider each gain +1/+1 and deathtouch until end of turn.  
 Whenever its rider deals combat damage to an opponent, you may sacrifice it. If you do, draw cards equal to its power and gain life equal to its toughness.  
 Mount up {o2} *({o2}: Until end of turn, this creature can't attack and another target creature you control becomes its rider. Activate only as a sorcery and only once each turn.)*

We decided to make landfall deciduous, and this card had landfall, so we chose to label it. The mount ability became mount up. The biggest difference is that being a rider only lasted until the end of the turn, meaning you had to spend mana each turn to use it.

**Gitrog Monster, Bronco (version #5)**  
 2BG  
 Legendary Creature — Frog Horror Steed  
 5/4  
 Whenever CARDNAME attacks, you may sacrifice target creature that crewed it this turn. If you do, draw cards equal to its power and gain life equal to its toughness.  
 Crew Steed 1 *(Tap any number of other creatures you control with total power 1 or more: This Steed becomes crewed until end of turn.)*

The landfall ability went away, and the creature got a little bigger. This is the point where Set Design started using the Vehicle variant version of mount that had been designed by the Vision Design team of a future set. I know that because we (i.e., the other design team) called it crew Steed. In this early version, we were trying to see if we could just make this ability an extension of crew, not a separate yet similar mechanic.

**The Gitrog Monster, Ravenous (version #6)**  
 2BG  
 Legendary Creature — Frog Horror Steed  
 5/4  
 Whenever CARDNAME attacks, if it was saddled this turn, you may play an additional land this turn and you may sacrifice a creature that saddled it this turn. If you do, you draw cards equal to that creature's power and you gain life equal to its toughness.  
 Saddle 1 *(Tap any number of other creatures you control with total power 1 or more: This Steed becomes saddled until end of turn.)*

This version finally gets to saddle, as crew didn't capture the proper flavor and required some choices we didn't want. Now the creature gets a bonus for being saddled. Some flavor of playing lands is added to tie back to the previous Gitrog Monsters.

**The Gitrog Monster, Untamed (version #7)**  
 2BG  
 Legendary Creature — Frog Horror Steed  
 4/5  
 Reach, deathtouch  
 Whenever CARDNAME attacks while saddled, you may play an additional land this turn. You may sacrifice a creature that saddled it this turn. If you do, you draw cards equal to the sacrificed creature's power and you gain life equal to its toughness.  
 Saddle 1 *(Tap any number of other creatures you control with total power 1 or more: This Steed becomes saddled until end of turn. Saddle only as a sorcery.)*

Saddle now gains its sorcery restriction. We didn't want things getting saddled to block. We swapped the Gitrog Monster's stats and gave it reach and deathtouch (the latter being another callback to the original cards). The final version went to five mana, gained a power, and traded reach and deathtouch for haste and trample. While deathtouch is a callback to the original two cards, it just didn't play well. Haste and trample created better play patterns. That's another important lesson when redesigning new versions of a character. You are not beholden to mechanics done earlier if those mechanics do not serve the new card. The new card playing well is more important than it mechanically connecting as much as possible. It simply needs to feel like the same character.

Finally, here is the art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: OTJ  
 **Plane**: Thunder Junction  
 **Color**: Legendary creature associated with black and green mana  
 **Location**: Bog (118) with duck weed (see reference) or other swamp greenery. Intention: The Gitrog Monster (see reference) is a huge, mutated frog. Denizens of Thunder Junction have been trying to wrangle the Gitrog so they can ride it, but so far, their efforts have been futile.  
 **Action**: The Gitrog Monster blasts out of the swamp. Various nets, lassos, and ropes dangle off the monster from failed efforts to capture or contain it. It's got a saddle (page 87A) in his mouth like a dog with a chew toy.  
 **Focus**: The Gitrog Monster  
 **Mood**: YOU CANNOT TAME THE GITROG!  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

**Rakdos, the Muscle**

0226\_MTGOTJ\_Main: Rakdos, the Muscle 

*Outlaws of Thunder Junction* needed to bring in famous troublemakers from across the Multiverse. Who better than an ancient demon, one of the paruns (i.e., founders) of the guilds on Ravnica?

**Brion Stoutarm, Rough-Gang Leader (version #1)**  
 1RW  
 Legendary Creature — Giant Warrior  
 3/3  
 Whenever a source you control deals noncombat damage to one or more opponents, put a +1/+1 counter on each creature you control.  
 {o2oR}, sacrifice a creature: Brion deals damage equal to the sacrificed creature's power to each opponent.

Interestingly, the first thought of the character to be the muscle wasn't Rakdos, but a giant from Lorwyn, Brion Stoutarm. Brion is well known for throwing creatures, so his new card does exactly that (although only to players), except it has a static ability that rewards the rest of your creatures for you tossing one.

Once the Creative team came up with the idea of Rakdos being the muscle for Oko's gang, there was no going back. Rakdos had appeared in four cards before *Outlaws of Thunder Junction*, one even in the set right before.

Not a lot of characters have four cards. When designing characters that have a bunch of card history, you really want to start by getting a sense of what the existing cards have mechanically dictated about the character. When doing a second card, you have some flexibility. Less so on your fifth. If enough dots were made, some lines start getting drawn. Here's what the four versions have in common:

1.  He's black and red.
2.  He costs four to six mana.
3.  He's a Demon.
4.  He has flying and trample.
5.  His power and/or toughness is 6. (Six is thought to be the number of the beast.)
6.  He's kind of destructive.

**Rakdos, Bloodsoaked Enforcer (version #2)**  
 2BBRR  
 Legendary Creature — Demon  
 6/6  
 Flying, trample  
 Once each turn, you may cast a spell by sacrificing three creatures instead of paying its mana cost.

The first stab captures all six of those things. It's playing in dangerous territory, though, as evading mana cost has historically caused problems, but three creatures is a lot, and the flavor is strong.

**Rakdos, the Muscle (version #3)**  
 1BBRR  
 Legendary Creature — Demon Mercenary  
 5/5  
 Flying, trample  
 Once during each of your turns, you may cast a red or black spell by sacrificing three other creatures rather than paying its mana cost.

He becomes a Mercenary to make him an outlaw. We restrict the colors of the cards he can cast to black and red because the previous version was too much of a color pie bend. We also drop his mana cost to 1BBRR and his stats to 5/5 (which means he's now not following one of the items above.)

**Rakdos, the Muscle (version #4)**  
 1BBR  
 Legendary Creature — Demon Mercenary  
 5/5  
 Flying, trample  
 At the beginning of combat on your turn, you may sacrifice three creatures. If you do, put a red or black creature card from your hand onto the battlefield.

We further restrict what Rakdos can play for free to black and red permanents rather than any spell.

The finished version went in another direction. You're still sacrificing creatures, but now for two different abilities. First, it allows you to access cards from the top of any player's library. The ability cares about mana value rather than power or toughness because we don't want you sacrificing creature tokens to it. Second, it allows you, once a turn, to protect Rakdos by making him indestructible. We also tweak his mana cost and put him back up to 6 power.

Here's his art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: QXX  
 **Plane**: "Quilting"  
 **Color**: Legendary creature associated with black and red mana  
 **Location**: A villainous saloon in Tarnation (pages 167–178)  
 **Action**: RAKDOS (page 16) is a destruction-loving demon who can make himself gigantic. Show him, wings outspread, enlarged to 30 feet tall, using his flaming SCYTHES to rip the ROOF off a building and reveling in the chaos. Maybe he is holding screaming humans in his gigantic hands. Maybe we are staring at him from inside the building he has decapitated.  
 **Focus**: Rakdos  
 **Mood**: Powerful and destructive  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

**Riku of Many Paths**

0227\_MTGOTJ\_Main: Riku of Many Paths 

Riku first showed up in *Magic: The Gathering—Commander*.

He was a mage who had two passions, studying magical spells and studying creatures. To accomplish both, he used an ancient spell to split himself into two. That way, one copy of him could study spells and the other copy could study creatures. His card represents both copies of him with one effect copying spells and the other copying creatures. He would later show up in *Duels of the Planeswalkers* as an opponent who would play your own deck against you.

**Stormbreath Dragon (version #1)**  
 3RR  
 Creature - Dragon  
 4/4  
 Flying, haste, protection from white  
 {o5oRoR}: Monstrosity 3. *(If this creature isn't monstrous, put three +1/+1 counters on it and it becomes monstrous.)* When Stormbreath Dragon becomes monstrous, it deals damage to each opponent equal to the number of cards in that player's hand.

The slot, which originally was mythic rare, started as a reprint from *Theros*. I'm not quite sure why. My best guess was it might have been playtest filler.

**Wort, Indecisive Auntie (version #2)**  
 BRG  
 Legendary Creature — Goblin Warlock  
 3/3  
 Whenever you choose one or more modes on a spell or ability, put a number of +1/+1 counters on target creature you control equal to the number of modes chosen.  
 {oT}: Add {oBoRoG}. Spend this mana only to cast spells with one or more modes.

The first version of this card as a legendary creature was built bottom up. To explain what it was up to, we must go back to *Limited Edition (Alpha)* with the following card designed by Richard Garfield:

Richard made a common cycle of cards he called "the boons." Each one was an instant that cost a single colored mana that did three of some effect.

The power level of the spells were kind of all over the board (with the Ancestral Recall eventually moving to rare), with white having the weakest effect. To try and make it a little better, Richard gave Healing Salve two options. You could either gain 3 life or prevent 3 damage. This was the first modal spell (i.e., a spell where you get to choose between different effects). *Urza's Saga* would change the template of Healing Salve to "Choose one," but it wasn't until *Khans of Tarkir* that the bulleted list was created.

Modal spells had been part of the rules for a long time (it wasn't defined yet in *Alpha*), but it wasn't until *Khans of Tarkir* that it was templated in such a way that it was clear in looking at a card what was and wasn't a modal spell (not that many players knew specifically what to look for). R&D has talked about making a card that cared about modal spells for a while, but it didn't find a home until *Outlaws of Thunder Junction*.

The slot was allocated for a "villain," so a name was thrown on it. Not Riku at first, but Wort. Wort is a goblin from the plane of Lorwyn. Playtesting showed two things. One, caring about modes was kind of cool, and two, nothing about this card, other than maybe the colors, was reminiscent of Wort. Wort mechanically was tied to Goblins and getting things back from the graveyard. Nothing about this card evoked Wort, so the Set Design team decided to go and look for a character that made sense.

Caring about modes is an odd flavor, and there wasn't an obvious slam-dunk fit. Riku, with his focus on splitting himself, seemed closer than anything else the team could come up with, so they tried him. This gets into another topic of redoing characters. Sometimes you come up with something cool that captures a vibe, even if it's not mechanically identical. So, Wort became Riku.

**Riku of Many Modes (version #3)**  
 1BRG  
 Legendary Creature — Human Wizard  
 3/3  
 Vigilance, trample  
 Whenever you choose modes for a spell or ability, put a number of +1/+1 counters on target creature you control equal to the number of modes chosen.  
 {oT}: Add {oBoRoG}. Spend this mana only to cast spells with one or more modes.

Now that it was Riku, there were a few issues. One, it was in the wrong colors. Normally when we bring a character back after a length of time, we tend to either put them in the same colors, or a subset of the colors, unless something substantial happened to them in the story that would cause a shift in colors. Riku of Two Reflections was green-blue-red, so we changed him to those colors.

Neither the +1/+1 counter granting nor the mana production felt like a great fit for Riku, so the design team decided to lean into the mode flavor and make this card have a modal element. (I should note, Riku only works with "modal spells," which don't care about permanents that have modal effects.) Now, how many modes you picked on your modal spell dictated how many different modes you get to choose on Riku.

The penultimate change for Riku was moved from mythic rare down to rare. We tend to put quirky build-arounds at rare.

**Riku, Master of Refractions (version #4)**  
 1GUR  
 Legendary Creature — Human Wizard  
 3/3  
 Vigilance, trample  
 Whenever you choose modes for a spell, choose up to that many modes. You may choose the same mode more than once. —  
 • Exile the top card of your library. You may play it this turn.  
 • Create a 1/1 blue Bird creature token with flying.  
 • Put a +1/+1 counter on CARDNAME. It gains trample until end of turn.

This final version got closer to the printed version. All the three modes stayed, although the templating for them changed a little. The "impulsive draw" mode was the only one that mechanically changed in that the effect went from "this turn" to "until the end of your next turn." The fact that you had to play a modal spell made it hard to be able to cast that spell on the same turn. Riku lost his vigilance and trample (the latter of which he didn't need, as the +1/+1 counter mode granted it) and went down in cost to three mana.

Here's his art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\***  
 **Set Code**: OTJ  
 **Plane**: Thunder Junction  
 **Color**: Legendary creature associated with green, blue, and red mana  
 **Location**: Abstract version of a red-rock desert with floating stones (pages 124–131)  
 **Intent**: RIKU (see reference) is a master wizard who has come to Thunder Junction to hone his magical skills. Riku is wearing a duster inspired by page 94, but please include aspects of his original costume, such as a burst of blue, green, and orange energy or coloration.  
 **Action**: We'd like you to design an abstract scene that depicts Riku magically deconstructing his environment. One possibility is to show Riku hovering off the ground near a natural stone arch (page 124) that he has magically shattered. The arch has cracks, like shattered glass, which are beginning to float apart, but we can still see its original shape. Several RAVENS fly away from the shattered arch as if they've been disturbed by this strange occurrence. Or you can go more abstract. Maybe Riku is surrounded by a beautiful pattern of red stone shards, ravens, and magical bursts of blue, green, and orange energy.  
 **Focus**: Riku  
 **Mood**: A beautiful and magical deconstruction of the desert  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

## *Thunder* Past

That wraps up my card-by-card design stories from *Outlaws of Thunder Junction*. As always, I'm eager to hear any feedback you have on any of the cards I talked about today or *Outlaws of Thunder Junction* in general. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for a *Making Magic* tribute to my father who very recently passed.

Until then, may you commit crimes (in *Magic*) with a smile on your face.