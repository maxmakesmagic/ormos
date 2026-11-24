---
id: 4b91msat
kind: article
lang: en
path: /en/articles/makingmagic/2024/04-22-bringing-the-thunder-part-1
title: Bringing the Thunder, Part 1
published: '2024-04-22'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    lang_detected: en
    capture_id: 212575
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    captured_at: '2024-05-18 00:57:20+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    lang_detected: en
    capture_id: 212575
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    captured_at: '2024-05-18 00:57:20+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    lang_detected: en
    capture_id: 212575
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    captured_at: '2024-05-18 00:57:20+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    lang_detected: en
    capture_id: 212575
    url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
    captured_at: '2024-05-18 00:57:20+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 4b91msat
  url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
  page_key: magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 00:57:20+00'
  capture_id: 212575
  wayback_url: https://web.archive.org/web/20240518005720id_/https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 4b91msat
  capture_id: 212575
  url: https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
  wayback_url: https://web.archive.org/web/20240518005720id_/https://magic.wizards.com/en/news/making-magic/bringing-the-thunder-part-1
  captured_at: '2024-05-18 00:57:20+00'
  template: contentful
  sha256: 12fcddb94559499a07bfbe061e5b8fa5f3a167b6da05a3930246547bbfe6cde6
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
The last two weeks ([Part 1](/en/articles/makingmagic/2024/04-08-outlaws-of-thunder-junction-vision-design-handoff-document-part-1) and [Part 2](/en/articles/makingmagic/2024/04-15-outlaws-of-thunder-junction-vision-design-handoff-document-part-2)), I showed you the vision design handoff for *Outlaws of Thunder Junction*. Today and next week, I'll be telling card-by-card design stories from the set. For some focus, I'll talk about new cards for previously known characters and how best to adapt a character to a new card.

**Breeches, the Blastmaker and Malcolm, the Eyes**

0197\_MTGOTJ\_Main: Breeches, the Blastmaker 0219\_MTGOTJ\_Main: Malcolm, the Eyes 

Breeches and Malcolm are both members of the Brazen Coalition (i.e., pirates from Ixalan) who served on the ship *Belligerent* captained by Vraska. Both appeared in the stories for original *Ixalan* but didn't have cards in the block (as the stories are usually written after the card set is locked down). Both first had cards in *Commander Legends*.

Breeches, Brazen PlundererMalcolm, Keen-Eyed Navigator 

The two cards both had partner and were designed to be partnered together, as they work together in the story. Both were Pirate typal and fetched resources. Breeches fetched cards, and Malcolm fetched Treasure to help cast those cards. Both characters got a second card when we returned to Ixalan in *The Lost Caverns of Ixalan*.

0137\_MTGLCI\_Main: Breeches, Eager Pillager 0063\_MTGLCI\_Main: Malcolm, Alluring Scoundrel 

When we redo a character, we want the new card and the old card to feel as if they're representing the same character. They don't have to be mechanically identical, but there's a certain feel that we like. The two cards usually want to feel at home in the same deck.

The new versions of Breeches and Malcolm used different techniques. Breeches kept Pirate typal and interacted with combat, although now with an attack trigger rather than a saboteur trigger (R&D speak for a trigger that happens when you deal combat damage to an opponent). Malcolm kept a saboteur trigger and a way to help you cast cards. Again, Breeches and Malcolm were made to be synergistic with one another, although this time, Breeches could get you the mana and Malcolm could get you the cards.

I believe Breeches and Malcolm weren't in the early version of the file because Pirates weren't part of the outlaw batch. Set Design decided that because *The Lost Caverns of Ixalan* added so many Pirates to Standard and Pirates felt like a good match for the flavor of outlaws, they should add it to the batch. [As I said in my first *Outlaws of Thunder Junction* preview column](/en/articles/makingmagic/2024/03-26-outlaws-of-the-land-part-1), Vision Design handed off just four creature types for the outlaws batch, leaving one slot in case Set Design wanted to add another.

The first version of both of their cards in *Outlaws of Thunder Junction* was a team-up card like we'd done in *March of the Machine*. Teaming up wasn't a theme of the set, but these two were buddies known for working together, so that's where we started.

**Malcolm and Breeches, Up to No Good (version #1a)**  
 2UURR  
 Legendary Creature — Goblin Siren Pirate  
 4/4  
 Flying, menace  
 Whenever you draw a card, create a Treasure.

The card was blue and red originally because Breeches had always been mono-red and Malcolm had always been mono-blue. They were teaming up, so it got both colors. The initial design doesn't play at all into Pirate typal (as that wasn't a thing in *Outlaws of Thunder Junction*), but it does create Treasure tokens and synergizes with card draw. As I said above, this card would play well in a deck with the other Breeches and Malcolms.

After just one iteration, the decision was reached to separate the two into two different cards, but ones that synergized with each other. To allow you to play either as a Commander that could play all copies of Breeches and Malcolm, both cards were made blue-red even though they only featured one of the characters.

**Rootha, Mastermind's Apprentice (version #1b)**  
 2UR  
 Legendary Creature — Orc Warlock  
 2/4  
 Whenever you cast a spell from exile, you may pay {o1}. If you do, copy that spell. You may choose new targets for the copy.

The second blue-red slot was originally going to be Rootha, a student from Strixhaven in the Prismari college. She was one of the five featured students in the set. Here's her card from Strixhaven:

Rootha, Mercurial Artist 

Rootha, as a member of the Prismari college, was all about artistic performance. Her card copies spells because casting giant spells was central to the blue-red faction from *Strixhaven: School of Mages*. Since her focus was copying spells, her new card gave you a new way to do that. Tying into casting from exile worked very well with the plot mechanic.

**Breeches, Demolition Expert (version #2b)**  
 2UR  
 Legendary Creature — Goblin Pirate  
 3/4  
 Whenever you cast a spell from exile, you may sacrifice an artifact. If you do, copy that spell. You may choose new targets for the copy. Do this only once each turn.

When the decision was to give Breeches and Malcolm each their own card, Rootha's slot was given to Breeches. The Set Design team liked the design, so they mostly kept it the same. The story had decided to make Breeches the explosives expert for Oko's crew, so they exchanged paying mana for sacrificing an artifact, which in the Constructed deck would most often be a Treasure. However, they didn't call out Treasure specifically to give the card more open-endedness to work with other things. Playtesting showed the Set Design team that they didn't want this happening a lot, so they restricted it to one time per turn.

**Malcolm, the Spy (version #2a)**  
 3URR  
 Legendary Creature — Siren Pirate  
 4/4  
 Flying, menace  
 Whenever a card would be put into your hand from the battlefield, you may return it to the battlefield instead.

While Breeches was the demolition expert, Malcolm was the lookout. I'm not sure where this mechanic came from. My guess is it was designed for something else, and they were trying it here. While it matched the idea of a lookout, it didn't feel a lot like Malcolm and didn't synergize with Breeches.

**Malcolm, the Spy (version #3a)**  
 2UR  
 Legendary Creature — Siren Pirate  
 3/3  
 Flying, menace  
 Whenever you cast a spell from exile, investigate. *(Create a Clue token. It's an artifact with "{o2}, Sacrifice this artifact: Draw a card.")*

This next version fixed both those two problems. First, it returned to some mechanical space that Malcolm had done on previous cards: producing tokens and drawing cards. Instead of creating Treasure tokens, it created Clue tokens, which tied into his being the lookout. This also synergized better with Breeches, as both cared about cards being cast from exile.

**Breeches, Demolition Expert (version #3b)**  
 1UR  
 Legendary Creature — Goblin Pirate  
 3/3  
 Whenever you cast your second spell each turn, you may sacrifice an artifact. If you do, copy that spell. You may choose new targets for the copy.

At this point, the Set Design team decided they wanted the blue-red archetype to care about casting two spells in a turn. It still played well with plot, instants, and sorceries but interacted better with other strategies. The final version of Breeches kept most of this final design but with a layer of chaos and the flavor of dealing damage to capture Breeches's role as an expert with explosives. As is our modern strategy when designing coin-flip cards, both outcomes are things the player should be happy with. The downside is not getting the effect you preferred, not that what you get isn't of value. Breeches kept the same mana cost and size but with menace.

Malcolm's cost dropped from 2UR to UR so that you could play him before you play Breeches. That required us to change him from a 3/3 to a 2/2. This also made him a different stat than Breeches. Usually when we have two multicolor cards of the same colors, we like to put them at different mana costs. Because we added menace to Breeches, we changed Malcolm's menace to haste.

Here are the art descriptions for the two cards:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: QXX  
 **Plane**: "Quilting"  
 **Color**: Legendary creature associated with blue and red mana  
 **Location**: On the train tracks (pages 167–178) in the desert, inspired by pages 122–132  
 **Action**: BREECHES (see attached references) is a monkey-like goblin pirate who loves destruction. Please design a new outfit for him inspired by pages 45–57 and pages 89–97. Make sure he has a cutlass and feathered pirate hat, which are important visuals in his design. Show Breeches ready to ignite a pile of magical DYNAMITE that he has set on a RAILROAD TRACK (pages 167–178). Maybe we can see other, smaller explosions going off at other points on the track. Maybe in the background we see piles of rubble made of things that he has already blown up.  
 **Focus**: Breeches  
 **Mood**: Unhinged, chaos-loving, destructive  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: QXX  
 **Plane**: "Quilting"  
 **Color**: Legendary creature associated with blue and red mana  
 **Location**: Above a canyon in a desert, inspired by pages 111–117  
 **Intent**: MALCOLM (see attached references) is a winged siren pirate. Please design a new outfit for him inspired by pages 45–57, pages 89–97. Make sure he wears goggles and a long coat, which are important visuals in his design.  
 **Action**: Show Malcolm FLYING high in the air as he spies on a small TRAIN (pages 167–178) in the distance. Maybe in the background, we see an explosion somewhere along the railroad track. Maybe we see a tornado or storm brewing on the horizon.  
 **Focus**: Malcolm  
 **Mood**: Fun, daring, adventurous  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

**Bruse Tarl, Roving Rancher**

0198\_MTGOTJ\_Main: Bruse Tarl, Roving Rancher 

Bruse Tarl is an ox herder from Zendikar. He didn't end up in the set because he's a villain, but how could we not add a famous ox herder to a Western-inspired set?

**Muzzio, Exiled Inventor (version #1)**  
 2UR  
 Legendary Creature — Human Artificer  
 2/3  
 Whenever a nontoken artifact enters the battlefield under your control, you may pay U. If you do, it becomes a 1/1 Thopter creature with flying and mount 1 in addition to its other types.

It took a while to hammer out just what characters wanted to be in the set, so different characters were tried. Muzzio is from Fiora, first seen as a Human Artificer in *Magic: The Gathering—Conspiracy*. This slot was originally assigned to Muzzio. The initial design captured the feel of Muzzio making artifact creatures.

It didn't take long for the Creative team to decide they wanted Bruse Tarl. Here's his one and only previous card from *Commander (2016 Edition)*:

Bruse Tarl, Boorish Herder 

And here's the first attempt at his new card:

**Bruse Tarl, Cattle Barron (version #2)**  
 2RW  
 Legendary Creature — Human Warrior  
 3/3  
 *Landfall* – Whenever a land enters the battlefield under your control, create a 2/2 white Ox creature token.  
 Whenever one or more Ox tokens you control attack, they gain double strike and lifelink until end of turn.

Bruse Tarl's original card granted double strike and lifelink to creatures, so the first stab at his design does exactly that, except only to Ox tokens. To make sure you have Ox tokens to grant the abilities to, it has a landfall trigger to make 2/2 white Ox tokens. (The cows of *Outlaws of Thunder Junction* are white 2/2 Ox tokens.)

It's common with the first stab at a new card for a character to lean in close to their earlier designs. The finished version doesn't have to be as close, but it usually is a good starting point. There's an art to finding a design that feels right for the character while letting it be its own card.

**Bruse Tarl, Cattle Barron (version #3)**  
 3RW  
 Legendary Creature — Human Warrior  
 3/4  
 Ox tokens you control get +1/+1.  
 At the beginning of your upkeep, exile the top three cards of your library. When you do, create a 2/2 white Ox creature token for each land card exiled this way, and you may play up to one land and cast up to one spell from among the exiled cards until end of turn.

Set Design liked the general feel of the card but experimented with several changes. First, rather than granting the creatures double strike and lifelink, it became a static +1/+1. The ability to create the Ox tokens turned into an "beginning of upkeep" trigger and combined Ox creation with impulsive draw. This helped make him play better as a commander.

Playtesting showed that the best thing to do with this card was turtle up. You don't want to risk anything, so just use Bruse Tarl to build resources. For the card to work, it needs some encouragement to attack, so the trigger was changed back to an attack and enters-the-battlefield trigger. The impulsive-draw effect was also extended until the end of the next turn to give you more chances to cast the card, especially on the turn you play Bruse Tarl. The static ability was changed from +1/+1 to double strike to encourage aggression. Plus, it was a callback to the original card. His mana value was dropped to four, and his stats were swapped from 3/4 to 4/3.

Finally, here's Bruse Tarl's art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: OTJ  
 **Plane**: Thunder Junction  
 **Color**: Legendary creature associated with red and white mana  
 **Location**: Arid plateau with desert flowers (pages 130–131) for inspiration  
 **Intent**: BRUSE TARL, a stubborn cattleman from Zendikar, always had a tumultuous relationship with his equally stubborn oxen. But on Thunder Junction, he's become a willing caretaker of adoring oxen (see attached oxen reference) from all over the Multiverse.  
 **Action**: Show Bruse Tarl with his handlebar mustache wearing a Freestrider costume (see attached reference, pages 23–26, for costume) shepherding several very distinct oxen across the plateau. Maybe he's feeding one flowers while the others wait their turn.  
 **Focus**: Bruse Tarl  
 **Mood**: A loyal protector of his animal companions  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

**Eriette, the Beguiler**

0202\_MTGOTJ\_Main: Eriette, the Beguiler 

Eriette is a witch from Eldraine. Ashiok showed up at the end of the *Wilds of Eldraine* story to recruit her, so she had to be in the set.

Looking back at the database, it's fun to see cards in the slot before the character in question shows up.

**Drudge Outlaws (version #1)**  
 1B  
 Creature — Skeleton Outlaw  
 3/1  
 CARDNAME has indestructible if you've committed a crime this turn.

This was one of our first crime designs. It eventually turned into Overzealous Muscle, a 5/4 for 4B.

0097\_MTGOTJ\_Main: Overzealous Muscle 

**Hootenanny Greeters (version #2)**  
 2BB  
 Creature — Skeleton Rogue  
 4/4  
 Menace  
 Whenever you commit a crime, draw a card and you lose 1 life. *(Targeting one or more opponents and/or permanents, spells, abilities, or cards they own in other zones is a crime.)*

This ability ended up on Raven of Fell Omens, a 1/2 flier for 1B that was restricted to once per turn. It turns out there were too many repeatable activated abilities for zero or little cost.

0101\_MTGOTJ\_Main: Raven of Fell Omens 

**Hootenanny Greeters (version #3)**  
 1B  
 Creature — Lizard Rogue  
 1/1  
 Whenever you commit a crime, choose one that hasn't been chosen this turn —  
 • Put a +1/+1 counter on CARDNAME.  
 • CARDNAME gains deathtouch until end of turn.  
 • CARDNAME gains lifelink until end of turn.  
 • CARDNAME gains menace until end of turn.

This card combined crime with a modal effect. I think because of spree, we got rid of most of the other modal effects in the set. I'm pretty sure this design predates spree being in the set (as it was one of the mechanics added later).

**Hootenanny Greeters (version #4)**  
 B  
 Creature — Lizard Rogue  
 1/1  
 Menace  
 Whenever you commit one or more crimes, CARDNAME gets +2/+2 until end of turn. This ability only triggers once per turn. *(Targeting an opponent or anything they own or control is a crime.)*

I don't think this effect made it into the set. (Lazav, Familiar Stranger does get a +1/+1 counter.)

0216\_MTGOTJ\_Main: Lazav, Familiar Stranger 

Now we finally get to Eriette. As a reminder, here's her card from *Wilds of Eldraine*:

0202\_MTGWOE\_Main: Eriette of the Charmed Apple 

**Eriette, the Charmer (version #5)**  
 2WB  
 Legendary Creature — Human Warlock  
 4/4  
 Auras you control have "{oWoB}: Exile enchanted permanent."

Eriette was a white-black Human Warlock and had a mechanic that cared about Auras, so all three were carried across to the new card. The first stab allowed you to use Auras to kill creatures.

**Eriette, the Charmer (version #6)**  
 1WB  
 Legendary Creature — Human Warlock  
 2/4  
 Whenever an Aura you control becomes attached to a nonland permanent an opponent controls, if that Aura's mana value is greater than or equal to the mana value of that permanent, you gain control of that permanent for as long as that Aura enchants it.

Was there something more fun than just using the Auras to kill your opponent's creatures? What if you used them to steal them instead? To keep it from completely dominating the game, a restriction was added so that Eriette could only steal things of a mana value equal to or greater than the Aura she put on the opponent's creature. We also reduced the cost of the creature and moved her from a 4/4 to a 2/4.

Then someone from the Council of Colors saw the card. It looked mono-blue. Neither white nor black is good at stealing creatures. White isn't supposed to do it at all, and black is tertiary in it. (Cards aren't supposed to use tertiary abilities on multicolor cards.) The only thing white about the card was an interest in enchantments. Mono-blue outside a set with a heavy enchantment theme probably wouldn't have this effect.

The Set Design team really liked the design, so they added blue to the card. Also, to make it feel a bit more white and black, they added lifelink, the evergreen keyword ability, in both colors. This made them have to push the card back up to four mana, so it returned to a 4/4.

Here is Eriette's art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\*  
 Set Code**: QXX  
 **Plane**: "Quilting"  
 **Color**: Legendary creature associated with white and black mana  
 **Location**: An expensive hotel in Prosperity, inspired by pages 154–166.  
 **Intent**: ERIETTE (see attached reference) is a seductive, scheming witch. Please design a new outfit for her inspired by pages 58–71 and pages 89–97. Make sure to incorporate her high collar and shattered-mirror motifs into her new clothes, as they are important visuals in her design.  
 **Action**: Show ERIETTE lounging gracefully at a table in a crowded saloon and all the other patrons (inspired by pages 155–156) SERVING her because they are enchanted by her purple DREAM MAGIC. Maybe someone else at her table lies face down in their meal. Maybe we see her crone self-reflected in a mirror in the back of the bar.  
 **Focus**: Eriette  
 **Mood**: Powerful, deadly, sexy  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, (2) and with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio and fill the extended margins with additional fun details as Easter-egg reveals on the cards printed with the extended aspect ratio.

## *Thunder* Out

That's all the time I have for today. I hope you enjoyed my card-by-card design stories. As always, I'm eager to hear any feedback on the cards I talked about today or *Outlaws of Thunder Junction* in general. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two.

Until then, may you enjoy playing with your favorite characters.