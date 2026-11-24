---
id: zps4rz94
kind: article
lang: en
path: /en/articles/makingmagic/2024/06-03-expanding-your-horizons-eldrazi
title: 'Expanding Your Horizons: Eldrazi'
published: '2024-06-03'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    lang_detected: en
    capture_id: 220336
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    captured_at: '2024-06-19 10:30:31+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    lang_detected: en
    capture_id: 220336
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    captured_at: '2024-06-19 10:30:31+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    lang_detected: en
    capture_id: 220336
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    captured_at: '2024-06-19 10:30:31+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    lang_detected: en
    capture_id: 220336
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
    captured_at: '2024-06-19 10:30:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: zps4rz94
  url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
  page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
  lang: en
  template: contentful
  captured_at: '2024-06-19 10:30:31+00'
  capture_id: 220336
  wayback_url: https://web.archive.org/web/20240619103031id_/https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zps4rz94
  capture_id: 220336
  url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
  wayback_url: https://web.archive.org/web/20240619103031id_/https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-eldrazi
  captured_at: '2024-06-19 10:30:31+00'
  template: contentful
  sha256: c543457410623ad446a468b1bf6b7c62be927699d9e620f9f1984e37dea08893
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
With my two *Modern Horizons 3* card preview articles out of the way ([Part 1](/en/articles/makingmagic/2024/05-21-third-times-the-charm-part-1) and [Part 2](/en/articles/makingmagic/2024/05-27-third-times-the-charm-part-2)), it's time for some card-by-card design stories. I'm going to do it a bit differently today. First, I'll cover notable Eldrazi cards, then I'll cover energy cards next week. Second, I'm choosing cards that were based off a previous card or cards. Then for each card, I will tell the story of the original design and then the *Modern Horizons 3* card inspired by it.

**Nulldrifter**

0013\_MTGMH3\_Main: Nulldrifter 

Nulldrifter's design story starts with the design of the *Lorwyn* block, which began back in 2005. The set had a typal theme, and I was exploring different ways to tap into it. It needed a spell mechanic, so I was brainstorming ways for cards to be spells *and* tap into typal themes. (The tribal card type, now kindred, would be one of the ways we did this in the final set.) First, I asked myself, "What if we had spells that could turn into creatures?" Imagine a direct-damage spell that could become a Goblin.

My initial take on the mechanic was for it to be an instant or sorcery, but you could pay mana to turn it into a creature. Interestingly, the very first spell I thought up to turn into a creature was Counsel of the Soratami (what would later become Divination in *Magic 2010*)—a 2U sorcery that drew two cards. Here was my first stab at it:

**Inspiring Essence (version #1)**  
 1UU  
 Tribal Sorcery — Elemental  
 2/2  
 Draw two cards. Manifest 3 *(You may pay 3 as this spell resolves. If you do, put it into play as a creature.)*  
 -------------------------------- Flying

I assumed I couldn't make it 2U as that was just strictly better than Counsel of the Soratami, so I made it 1UU. I was trying to make a simple card, so for the body, I turned to another creature that we often used—Wind Drake, a 2/2 flyer. Wind Drake costs 2U, but you'd already paid a second blue for the initial cost, so I charged 3. I used the term manifest, which we would reuse years later when designing *Fate Reforged*.

I took this design to the rules manager (Mark Gottlieb at the time). Here is a fictionalized version of our conversation (in modern terms):

**Me**: What do you think?  
 **Gottlieb**: So, if I "kick" it, it's a sorcery and a creature?  
 **Me**: Yes.  
 **Gottlieb**: Okay, you cast it, pay the extra three. What happens?  
 **Me**: I have a 2/2 blue flyer and I draw two cards.  
 **Gottlieb**: For starters, state-based actions will kill it as soon as it hits the battlefield because that's what it does to sorceries on the battlefield.  
 **Me**: Couldn't we change the rules so that sorceries aren't killed when they end up on the battlefield?  
 **Gottlieb**: The rule exists for a reason. What happens when a sorcery ends up on the battlefield that has nothing to do with this mechanic?  
 **Me**: Okay, what if it turns from a sorcery into a creature?  
 **Gottlieb**: And when does that happen?  
 **Me**: I don't know. On the stack?  
 **Gottlieb**: Does it have to be a sorcery when you cast it?  
 **Me**: I want you to have a choice between Counsel of the Soratami or Counsel of the Soratami and a Wind Drake.  
 **Gottlieb**: We can do that, just not how you envisioned it.

Which brings us to my second attempt:

**Inspiring Essence (version #2)**  
 4UU  
 Creature — Elemental  
 2/2  
 Flying  
 When CARDNAME comes into play, draw two cards.  
 Discount 3 *(You may play this creature for o3 less. If you do, sacrifice it when it comes into play.)*

The solution was to make the card a creature the whole time. If you didn't pay the mana cost, sacrifice it. This bypassed how the rules interact with sorceries on the battlefield. As the only person I talked to was Gottlieb, the costs remained the same, although expressed differently. This version worked in the rules. Next, I showed it to some developers:

**Notion Glider (version #3)**  
 5U  
 Creature — Elemental  
 2/2  
 Flying  
 When CARDNAME comes into play, draw two cards.  
 Expedite 2U *(You may play this creature for o2oU. If you do, sacrifice it when it comes into play.)*

First, I learned that Counsel of the Soratami had some wiggle room (meaning the effect didn't cost a full 2U (although more than 1U), which meant we could cost the "spell" ability at 2U. The mana cost was knocked from 4UU to 5U. The other big advancement is that we'd decided the kicker style way of doing things, which is to have you add or subtract to the original cost, was harder than just writing out what you had to pay. So instead of telling you to subtract 3, it changed to tell you the cost for the ability is 2U. Here's what we printed:

Mulldrifter 

The development team would eventually knock the mana cost down to 4U, and creative would rename the mechanic evoke. Mulldrifter ended up being one of the best cards in the set, and the best evoke creature, and saw lots of play, becoming a fan favorite.

Now, let's get into the design of its *Modern Horizons 3*–inspired design.

**Determine (version #1)**  
 1U  
 Instant  
 Scry 2, then draw a card. You get EE.

The Nulldrifter slot started as a spell instead of a creature. Not even an Eldrazi spell, but one tied to energy. (Blue has both Eldrazi and energy themes.) It smoothed your draw, drew you a card, and provided energy, the kind of thing useful in a lot of blue decks.

**Fated Visions (version #2)**  
 U  
 Instant  
 Draw a card. Surveil 1. Dredge 1.

Design removed energy from the card and went looking for another old mechanic. I'm not quite sure how they ended up on dredge. I know *Modern Horizons* sets like to use guild mechanics in colors that they didn't appear in originally. Surprise, surprise; playtesting shows dredge isn't a great idea on this card.

**Logical Argument (version #3)**  
 1U  
 Instant  
 Counter target spell unless its controller pays 1. If they do, investigate.

So, design tried a different approach, making a card-drawing spell that's also a counterspell. This time, it made use of the investigate mechanic originally from *Shadows over Innistrad*.

**Blue Legend (version #4)**  
 7U  
 Legendary Creature — Eldrazi  
 7/7  
 When CARDNAME enters the battlefield, draw three cards.  
 Annihilator 2  
 Evoke CCCC

Here, they tried something a bit more radical. What if this card-drawing spell was a rare rather than a common? (I assume they ended up needing a common slot for something else, so they swapped that card's slot with this. That's often why card slots change rarity.) Also, what if it was an Eldrazi? This is the point where the card got evoke for the first time. To give it an Eldrazi flavor, it also got annihilator.

**Disciple of Kozilek (version #5)**  
 5CU  
 Legendary Creature — Eldrazi  
 4/4  
 Devoid *(This card has no color.)*  
 When you cast this spell, scry 3, then draw a card.  
 Annihilator 1 *(Whenever this creature attacks, defending player sacrifices a permanent.)*  
 Evoke {oCoC} *(You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)*

Design liked the Eldrazi approach, so they lean into it. Now the spell has colorless as a cost, mixed with blue, something we hadn't done before. It received devoid (which it probably should have technically had on the last iteration). The "draw three" was dialed down to a "scry 3 and draw a card," and the evoke cost went down as the spell is weaker. Annihilation 2 became annihilation 1, I assume because they playtested the card and remembered how soul-crushing annihilation is. (The set has two cards with annihilator 2 and one with annihilator X, but none are easy to access.)

**Nulldrifter (version #6)**  
 6C  
 Legendary Creature — Eldrazi Elemental  
 4/4  
 Devoid *(This card has no color.)*  
 When you cast this spell, draw two cards.  
 Flying  
 Annihilator 1 *(Whenever this creature attacks, defending player sacrifices a permanent.)*  
 Evoke {o2oU} *(You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)*

It wasn't until version six that they decided to turn this into a Mulldrifter reference. The "spell" ability turned into draw two, the evoke cost became 2U, and it became an Elemental to match Mulldrifter. They tried having a colorless mana in the cost, but that changed to generic mana in the printed version.

Finally, here's Nulldrifter's art description:

**\*\*\*COLORLESS FRAME\*\*\*  
 Plane**: Non-specific  
 **Color**: Creature associated with colorless mana  
 **Location**: Over an ocean  
 **Intention**: We'd like you to design a brand-new creature that combines elements from the Mulldrifter (see reference) and Eldrazi (see *Battle for Zendikar*, pages 226–228). Start with the image on page 228A, and then show it zooming over the surface of the ocean. Please incorporate wings like the Mulldrifter or maybe the reddish coloration along its back.  
 **Focus**: The flying Eldrazi elemental  
 **Mood**: Hallucinatory, wondrous

**Spawn-Gang Commander**

0140\_MTGMH3\_Main: Spawn-Gang Commander 

Spawn-Gang Commander's story begins during the design for *Scourge* (design started in 2002). This was the third set in the *Onslaught* block, the first block to have a larger typal theme. Our story begins in The Pit, the area where R&D all has desks. This was back in our old, old building, the one across the street from our last building. I was working on something when Worth Wollpert, an R&D member from back in the day, called my name.

Worth sat next to me in The Pit at the time. He was working on some designs for *Scourge* (he and Lead Designer Brian Tinsman were the whole design team), and he wanted my input. He was making a Goblin that made a bunch of Goblin tokens, but it seemed a little lackluster and didn't feel super red. I suggested he add a "sacrifice Goblin" ability to it. That was something more in red's part of the color pie, and it gave a secondary purpose to all the tokens you made. Plus, Goblins famously tend to be fodder. His attention went to Fodder Cannon, a card I'd made in *Urza's Destiny*, which is probably most famous for its flavor text.

Fodder Cannon 

What if the sacrifice ability allowed you to deal damage to any target? That also felt super red. The result was this card:

Siege-Gang Commander 

Siege-Gang Commander, much like Mulldrifter, was one of the most powerful and popular cards from its set and went on to see a lot of tournament play.

Now jump to Spawn-Gang Commander's design:

**Rocket Goblin (version #1)**  
 1R  
 Creature — Goblin Berserker  
 2/2  
 Whenever CARDNAME or another creature enters the battlefield under your control, clash with an opponent. If you win, that creature gains haste until end of turn.

The slot was always for a Goblin, but not yet an Eldrazi one. The first attempt at a card made use of the clash mechanic first seen in *Lorwyn*. I believe this card was made by Erik Lauer early in vision design when he tried designing a card for each existing mechanic. Clash is famous in R&D for being a mechanic that we were excited about but was strongly disliked by most players. (And yes, much of that is due to execution on our part.)

**Rocket Goblin (version #2)**  
 1R  
 Creature — Goblin Berserker  
 2/2  
 At the beginning of combat, if at least two lands entered the battlefield under your control this turn, creatures you control gain haste and trample until end of turn.

The next iteration didn't use a named mechanic, so it most likely was tying into one of the deck archetypes at the time. It filled the same slot in the mana curve, with a similar function, but wasn't memorable and didn't have any strong nostalgic tie to it.

**Rocket Goblin (version #3)**  
 1R  
 Artifact Creature — Goblin  
 2/2  
 C: Creatures you control gain haste and trample until end of turn.

This was the first attempt at adding some colorlessness to it. Interestingly, it was still just a Goblin and not an Eldrazi, which leads me to believe that the team was testing the waters for using colorless mana costs outside of things flavored as the Eldrazi. The card still granted haste and trample.

**Battleroar Eldrazi (version #4)**  
 2CCR  
 Creature — Eldrazi  
 6/6  
 Whenever CARDNAME attacks, other attacking creatures get +2/+0 until end of turn.

Here's where the design team started going all in on this being an Eldrazi. The card changed from a Goblin to an Eldrazi and got colorless mana in its mana cost (as with Nulldrifter; the design team was testing what they wanted to do with colorless mana). Finally, they made the creature much bigger and more expensive. Its ability shifted from being something you want early to something you want late.

**Battlespawn Eldrazi (version #5)**  
 3CR  
 Creature — Eldrazi  
 6/2  
 When CARDNAME dies, create four 0/1 colorless Eldrazi Spawn creature tokens. They have "Sacrifice this creature: Add {C}."

Instead of this interacting with your team, what if it was more of a threat to itself? Giving it a death trigger made you more willing to attack with it. It changed from a 6/6 to a 6/2 to up the number of times it could die and create tokens. The colorless 0/1 Eldrazi Spawn is one of the major tokens in the set.

**Battlespawn Thrinax (version #6)**  
 3RR  
 Creature — Eldrazi Lizard  
 6/2  
 Devoid *(This card has no color.)*  
 When CARDNAME dies, create three 0/1 colorless Eldrazi Spawn creature tokens. They have "Sacrifice this creature: Add {oC}."

The creature lost its colorless mana in its mana cost and gained devoid to tie it to the Eldrazi. It gained the Lizard creature type to give it a little flavor. Some of the Eldrazi cards play into the Emrakul mutations that we saw in *Shadows over Innistrad* and *Eldritch Moon* (although not all the mutations are specifically from Innistrad). Lastly, the tokens it creates decreased from four to three.

It was at this point that a member of the design team pitched the idea of making this an Eldrazi Siege-Gang Commander. The creature tokens went from a death trigger to an enters-the-battlefield trigger, and the sacrifice activation was added. The mana cost, activation cost (although with colorless rather than red), activation effect, and power and toughness were all made to line up with Siege-Gang Commander. This worked well with the many other cards in the set that make Eldrazi Spawn tokens.

Here's the art description for Spawn-Gang Commander:

**\*\*\*ELDRAZI FRAME\*\*\***  
 **Setting**: Non-specific  
 **Color**: A colorless creature  
 **Location**: Rocky terrain  
 **Action**: Design an ELDRAZI GOBLIN that is part of EMRAKUL'S BROOD LINEAGE. See goblin redesign document for goblin design and apply Emrakul mutations to it based on the attached references. The Eldrazi Goblin has TENTACLES protruding from its back that FLINGS a smaller Eldrazi Goblin, like a catapult. We see two other smaller Eldrazi Goblins in the scene, waiting, excited and eager for their turn to be flung.  
 **Focus**: The larger Eldrazi Goblin  
 **Mood**: Living ammunition

**Wastescape Battlemage**

0017\_MTGMH3\_Main: Wastescape Battlemage 

The next story goes back to 1998 and the start of the design of *Invasion*. [In a recent article about my father](/en/articles/makingmagic/2024/05-06-like-father-like-son), I wrote about how this was the set where we started design at his house in Lake Tahoe, Nevada. Bill Rose led the design team, which included me and Mike Elliott. During the first week, Bill told us about a new mechanic he'd made called kicker.

Aside from being very versatile, kicker lent itself to a multicolor block because the kicker cost could be of a color other than the base spell. Both Mike and I took that idea and expanded upon it. The *Invasion* block had a "play as many colors as you can" theme, with things like domain, so Mike and I came up with the idea of cards with multiple kickers, each with a cost of its own color.

Thornscape Battlemage Anavolver 

Mike created the Battlemages, which were monocolor creatures with two off-color kicker costs, each with its own enters-the-battlefield effect. I created the -volvers, which were monocolor creatures with two off-color kicker costs, each granting an ability to the creature and adding a different number of +1/+1 counters so you could tell which abilities the creature had.

Mike and I both pitched these ideas for *Invasion*, but Bill thought they worked better as twists on kicker that showed up later in the block. Because the two were too similar, we chose to put one in *Planeshift* and one in *Apocalypse*. The Battlemages were simpler, as they were "virtual vanillas," meaning they had effects when you played them but were just 2/2 creatures for the remaining turns, so they went into *Planeshift*. *Planeshift* was about ally colors, like *Invasion*, and *Apocalypse* was about enemy colors, so that helped distance themselves from one another. The Battlemages went on to be well received by the audience.

Which brings us to the design of Wastescape Battlemage:

**Lightning Eldrazi (version #1)**  
 3C  
 Creature — Eldrazi  
 4/2  
 Haste  
 *Revolt* — At the beginning of combat on your turn, if a permanent you controlled left the battlefield this turn, CARDNAME gains annihilator 1 until end of turn.

The slot was an Eldrazi creature with a colorless cost from the beginning. The initial version leaned a little more red. It made use of the revolt mechanic from *Aether Revolt* and annihilator from *Rise of the Eldrazi*. The two in combination were too "snowball-y," that is, it helped the person winning win even more, which made it super hard to come back from when you were behind.

**Lightning Eldrazi (version #2)**  
 3C  
 Creature — Eldrazi  
 4/2  
 Haste  
 When CARDNAME dies, each opponent sacrifices a permanent.

The next iteration tried a death trigger that acted like a one-shot annihilation. It played okay but wasn't particularly exciting or evocative. It lasted in the file for a while, but everyone knew it was destined to be replaced. Eventually, Set Design figured out that they wanted a green-blue Eldrazi ramp archetype, so they needed some cards that would allow you to spend a lot of mana on them. Ideally, those would be cards with opt-in costs so that you could cast the card at various times during the game and make it stronger as you gained access to more mana.

The task at hand was simple. Was there an old mechanic that allowed the creature to power up as you got extra mana? As is often with the case when working on a *Modern Horizons* set, you look through the database for answers. This search took them to *Planeshift* and the Battlemages. Obviously, the effects were green and blue as that was the archetype this was being built for, and it's the reason there's only one Battlemage in the set (*Modern Horizons* sets often create single cards inspired by cycles). As the archetype was slow, it wanted answers that could help stall as it was building its board, so the very first design attempt was basically what saw print:

**Eldrazi Battlemage (version #3)**  
 1C  
 Creature — Eldrazi Wizard  
 2/2  
 Kicker {oG} and/or {o1oU}  
 When you cast this spell, if it was kicked with its {oG} kicker, exile target artifact or enchantment an opponent controls.  
 When you cast this spell, if it was kicked with its {o1oU} kicker, return target creature an opponent controls to its owner's hand.

The green ability helped you answer artifacts and enchantments, while the blue ability helped you deal with creatures. I'm sure they talked about making the creature have a mana cost of 2C to match the original Battlemages, but they felt that being a 2/2 with two off-color abilities captured enough of the feel of a Battlemage and the cheaper mana value made it play better.

Here's the art description for the card:

**\*\*\*COLORLESS FRAME\*\*\***  
 **Plane**: Zendikar/BFZ for World Guide references  
 **Color**: Creature associated with colorless mana  
 **Location**: Tazeem (pages 29–35)  
 **Action**: We'd like you to design an Eldrazi knight who mirrors the composition of the original Battlemage image (see attached). Start with the Eldrazi reference on page 221 but imagine crossing it with a horse. Show it reared back on its hind legs in a dramatic stance like the original image. There's no rider in this image, but maybe the Eldrazi has two heads.  
 **Focus**: The Eldrazi "knight"  
 **Mood**: A twisted version of a knight

## Color*less* Is More

That's all the stories I have for today. As always, I'm eager to hear any feedback on the article, any of the cards I discussed, or *Modern Horizons 3* itself. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [*Blogatog*](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for more card-by-card design stories, this time about energy.

Until then, may you tap into your inner Eldrazi as you play *Modern Horizons 3*.