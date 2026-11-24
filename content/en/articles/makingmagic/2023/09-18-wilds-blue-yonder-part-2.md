---
id: 74v819jx
kind: article
lang: en
path: /en/articles/makingmagic/2023/09-18-wilds-blue-yonder-part-2
title: Wilds Blue Yonder, Part 2
published: '2023-09-18'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    lang_detected: en
    capture_id: 234528
    url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    captured_at: '2024-05-18 01:11:46+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    lang_detected: en
    capture_id: 234528
    url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    captured_at: '2024-05-18 01:11:46+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    lang_detected: en
    capture_id: 234528
    url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    captured_at: '2024-05-18 01:11:46+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    lang_detected: en
    capture_id: 234528
    url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
    captured_at: '2024-05-18 01:11:46+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 74v819jx
  url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
  page_key: magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:11:46+00'
  capture_id: 234528
  wayback_url: https://web.archive.org/web/20240518011146id_/https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 74v819jx
  capture_id: 234528
  url: https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
  wayback_url: https://web.archive.org/web/20240518011146id_/https://magic.wizards.com/en/news/making-magic/wilds-blue-yonder-part-2
  captured_at: '2024-05-18 01:11:46+00'
  template: contentful
  sha256: cd232908fd5ddff3946051a60a1fbf7049b32f71da7ce13fbc16d3cb235f26bf
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email me
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
[Last week](/en/articles/makingmagic/2023/09-11-wilds-blue-yonder-part-1), I started telling card-by-card design stories from *Wilds of Eldraine*. I had more stories to tell, so today is part two.

**Rowan, Scion of War and Will, Scion of Peace**

![Rowan, Scion of War](https://media.wizards.com/2023/woe/en_4049313685.png) ![Will, Scion of Peace](https://media.wizards.com/2023/woe/en_4e44fe4ae6.png) 

 

Rowan and Will are what is known in design as a mirrored pair. That is, two designs that are usually opposite colors that are similar in some mechanical regard but opposite in another. The classic example from *Alpha* (although there were many, Richard really liked mirrored pairs) was White Knight and Black Knight.

![White Knight from Alpha set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=274&type=card) ![Black Knight from Alpha set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=50&type=card) 

 

The two creatures are both 2/2 for two colored mana and have first strike and protection. They are opposite in color and the protection is from each other.

The first step to creating Rowan and Will was to put them in opposite colors. To add some texture, they were both made multicolor but both pairs of colors were opposites. Rowan and Will traditionally have been red and blue, already enemy colors, so that had to stay. Black and white were the second pair of enemy colors we chose. Black made more sense with Rowan and white with Will given their stances in the stories.

Here was the first stab at their design:

**Rowan, Vengeful Heir**  
 1BR  
 Legendary Creature – Human Wizard  
 3/3  
 First strike  
 Spells you cast cost {oX} less to cast, where X is the amount of life you lost this turn.

**Will, Wise Heir**  
 1WU  
 Legendary Creature – Human Wizard  
 3/3  
 Vigilance  
 Spells you cast cost {oX} less to cast, where X is the amount of life you gained this turn.

Both cost 1MN (M means a color, and N means a second color), are 3/3, have one keyword ability, and have a cost reduction ability. The reflection comes from the different colors, the alternate choice of keywords, and the opposite condition of the cost reduction ability.

The final versions aren't too far from the initial designs. We decided to mirror power/toughness rather than having them match. Rowan, the more aggressive, gets 4/2, and Will the more defensive gets 2/4. Rowan's ability was changed from first strike to menace, as first strike is tertiary in black and it felt better to have the keyword ability be something primary or secondary in both colors. Their cost reduction ability was changed to require a tap, and the spells affected by it were restricted to their two colors. I assume both changes were based on play design concerns.

Finally, here's the art descriptions for the two cards:

\*\*\* EXTENDED ART TEMPLATE\*\*\*  
 **Setting**: ELDRAINE  
 **Color**: Legendary creature associated with red and black mana.  
 **Location**: The ruins of Castle Ardenvale (page 234).  
 **Action**: ROWAN (the woman on p.8) walks down crumbling steps that lead down from a destroyed tower, dragging her sword along the broken wall beside her. She is angry, bitter, and vengeful, having lost her mother, her father, and her home to war. Sparks fly from where her blade scrapes the stone wall, and she charges up a blast of spark magic in her other hand. Mirror shards (p.106) surround her sword and her charged up magic. The mirror shards are leaking purple magical wisps (p.102 for inspiration).  
 **Focus**: Rowan.  
 **Mood**: A traumatized victim of war, hellbent on getting even.  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, and (2) with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio, and fill the extended margins with additional, fun details as Easter egg reveals on the cards printed with the extended, aspect ratio. 

\*\*\* EXTENDED ART TEMPLATE\*\*\*  
 **Setting**: ELDRAINE  
 **Color**: Legendary creature associated with blue and white mana.  
 **Location**: The REALM (see the background on page 20 as well as the basic lands on pages 298-305).  
 **Action**: Show WILL KENRITH, the new king of Eldraine, at the head of an army. Behind him we see standards bearing the heraldry of both ARDENVALE and VANTRESS (see 260 and 267). Maybe he's on horseback. It would be nice to get a clear shot of his PROSTHETIC LEG here. See attached reference for Will.  
 **Focus**: WILL  
 **Mood**: A courageous young king with the country behind him.  
 Note: See attached references for Will. See pages 260-263 and pages 267-269 for Ardenvale and Vantress knights, respectively. Notes: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, and (2) with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio, and fill the extended margins with additional, fun details as Easter egg reveals on the cards printed with the extended, aspect ratio. 

**Syr Ginger, the Meal Ender**

![Syr Ginger, the Meal Ender](https://media.wizards.com/2023/woe/en_887916ded2.png) 

 

Part of leading vision design is getting a good understanding of what about the set will most lead players to want to play it. Our internal lingo for that concept is "key selling points" (KSP). The plane of Eldraine was initially pitched as *Magic*'s version of Arthurian legend. It would be a plane of courts and castles, of knights and quests. Knowing we could only stretch that source material so far, I pitched adding the fairy tale element to it. I'd been trying to make a fairy-tale set for ages and realized that Arthurian legend and fairy tales were a good fit. One could argue Arthurian legend is just England's form of fairy tales.

As I started working on the set, I realized something else. Players generally liked high fantasy courts and knights, but *Magic* had done it so much since *Alpha* that it didn't feel distinct. It just felt like what *Magic* always does. It was a bad KSP because it didn't present something new, but rather something old. When you're selling a set, you want to lean on what's new and exciting about it.

I took this information to our marketing team. I said, "The set has a lot of cool stuff going in it, but the thing that's going to draw player attention is the fairy-tale stuff. It's just the new thing. I strongly urge you to lean into the fairy-tale aspect of the set when selling it." Many months later, the head of marketing that I had talked to asked me to come with her. She had a trailer to show me. All she said was, "We leaned into what you said."

The trailer got a lot of people talking at Wizards. The plane had been sold internally on Arthurian legend and the trailer featured gingerbread people. There was some worry that it wasn't going to do well with the audience. That fear proved completely unfounded though. The audience absolutely adored the trailer. So much so that we had an opposite problem. The set did have a gingerbread person (Gingerbrute) in it, but the main character from the trailer was nowhere to be seen. Where was Syr Ginger? I got a lot of mail about it.

So, when we returned, it was clear that Syr Ginger needed a card. Here was the first stab at the design:

**Syr Ginger the Brave (version #1)**  
 2  
 Legendary Artifact Creature – Food Knight  
 2/1  
 CARDNAME has double strike as long as an opponent controls a planeswalker.  
 Whenever you sacrifice CARDNAME or another food you control, target creature gets +1/+1 until end of turn.  
 {o2}, {oT}: Sacrifice CARDNAME: Gain 3 life. 

We wanted to capture the feel of the character in the trailer, so the first thing we wanted was something that felt anti-planeswalker, as her antagonist was Garruk. Because her name was Syr Ginger, we felt she had to be a Knight. Double strike felt good with that. We wanted her second ability to tie to food, because we liked the idea that she went into a deck with other Food. Her third ability was just to allow her to have the Food subtype.

**Syr Ginger, Last of Her Batch (version #2)**  
 2  
 Legendary Artifact Creature – Food Knight  
 3/1  
 Protection from planeswalkers  
 Whenever an artifact you control is put into a graveyard from the battlefield, put a +1/+1 counter on CARDNAME.  
 {o2}, {oT}: Sacrifice CARDNAME: You gain life equal to CARDNAME's power. 

The next version tried something shorter for her anti-planeswalker portion. We made her Food synergy a little more open-ended so that she worked with other artifacts and not just Food. Her stats changed from 2/1 to 3/1 as she lost the double strike. In the final version we decided to just grant her a handful of abilities when facing a planeswalker. The second ability added scry 1 to make it a bit stronger.

Here was her art description:

\*\*\* EXTENDED ART TEMPLATE\*\*\*  
 **Setting**: Eldraine  
 **Color**: Legendary associated with no colors of mana.  
 **Location**: Inside a house in Edgewall (p.26-30).  
 **Action**: GINGER, a living gingerbread woman, is riding a wildly charging steed made of gingerbread across a tabletop! She is using a large fork as a lance and has a metal coat button shield! Maybe she has candy armor in addition to her original frosting decorations.  
 **Focus**: Ginger.  
 **Mood**: Charge!  
 **Notes**: This art will print with TWO DIFFERENT ASPECT RATIOS: (1) the standard aspect ratio, and (2) with extended margins (please see attached template). Please compose the illustration to fit cropping for the standard aspect ratio, and fill the extended margins with additional fun details as Easter egg reveals on the cards printed with the extended aspect ratio. 

One final piece of trivia. Her horse's name is Cinnamon.

**Totentanz, Swarm Piper**

![Totentanz, Swarm Piper](https://media.wizards.com/2023/woe/en_95954f48b0.png) 

 

[Last week](/en/articles/makingmagic/2023/09-11-wilds-blue-yonder-part-1), I talked a bit about the history of Mice in *Magic*. This week, I'm going to talk about Rats.

![Plague Rats from Alpha set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=77&type=card) 

 

Rats showed up in *Alpha*, although only on one card. It was a pretty high-profile card though. Plague Rats got better the more Plague Rats you had. And in early *Magic*, you weren't limited to just four copies of a card in your deck, so sitting down to play often meant you ran into a deck filled with Plague Rats.

![Bog Rats from The Dark set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=1731&type=card) ![Pestilence Rats from Ice Age set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=2481&type=card) 

 

![Diseased Vermin from Alliances set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3070&type=card) ![Sewer Rats from Mirage set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3308&type=card) 

 

Rats took a year to show up again, but then started to come about one a set. Design-wise they tended to be all over the map. Each card played into some top-down essence of Rats (they were sneaky, they carried disease, they were a bit destructive). A recurring theme was that Rats liked to hang out with other Rats, but that was mostly done by playing a lot of the same card.

![Relentless Rats from Fifth Dawn set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=73573&type=card) 

 

The side effect of all this was Rats never held together well as a typal deck. There were plenty of rats to play because we kept making more, but they didn't tend to encourage playing them together. And whenever we explored typal themes, we choose other creature types to focus on.

![Marrow-Gnawer from Champions of Kamigawa set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=50253&type=card) ![Swarm of Rats from Ninth Edition set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=83292&type=card) ![Pack Rat from Return to Ravnica set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=253624&type=card) 

 

Eventually we started making individual cards designed to lead a Rat deck. The sets that had them tended not to have a huge number of Rats, meaning they were never a draft strategy, but we knew players wanted to construct Rat decks. *Throne of Eldraine* even had one with Piper of the Swarm.

![Piper of the Swarm from Thrones of Eldraine set](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=473062&type=card) 

 

*Wilds of Eldraine* is the first set to have Rat typal as a draft archetype. We built each color pair around a fairy tale, and the Pied Piper of Hamelin seemed too good to pass up. The trick to making it work was realizing we needed our Rat tokens to be unable to block. That allowed us to be more aggressive with creating them, encouraging you to attack with swarms of Rats, basically a desire that players have demonstrated since *Alpha*.

Totentanz is the signpost gold uncommon that's supposed to tell you what to do with black and red. We knew we wanted it to produce lots of Rat creature tokens, and we wanted it to incentivize attacking. We felt tying Rat production to creature death was flavorful. Giving deathtouch to Rats was on the card from the first design, although originally it wasn't activated.

To all the Rat lovers out there: I'm happy we finally got to give you a draft archetype. May your swarm of Rats win many games.

**Virtue of Loyalty, Virtue of Knowledge, Virtue of Persistence, Virtue of Courage, and Virtue of Strength**

![Virtue of Loyalty](https://media.wizards.com/2023/woe/en_bb6ca8e16e.png) ![Virtue of Knowledge](https://media.wizards.com/2023/woe/en_a6f5eb1d37.png) ![Virtue of Persistence](https://media.wizards.com/2023/woe/en_8724e1a72a.png) 

 

![Virtue of Courage](https://media.wizards.com/2023/woe/en_a335f824c6.png) ![Virtue of Strength](https://media.wizards.com/2023/woe/en_85825790cd.png) 

 

When the Creative team builds a plane, one of the things they always do is figure out how to incorporate the color pie into the essence of the plane. This can be done in many ways. Sometimes it's rolled into the factions, sometimes it defines an element of the plane (like *Theros*'s pantheon of Gods), sometimes it's connected to specific themes.

For Eldraine, the Creative team chose to craft the five courts around it. Each court would be connected to a different color and embody the ethos of that color. Part of this exercise involved making a virtue for each court. That is, what positive quality does that court philosophically aspire to?

Flash forward to *Wilds of Eldraine* vision design. We knew that we wanted to bring back Adventures, as they were the highest rated mechanical element of *Throne of Eldraine* in our market research. The big question was, what did we want to do with them?

*Commander Legends: Battle for Baldur's Gate* had used them and expanded their use a little. *Throne of Eldraine* Adventures had always been on creatures. *Battle for Baldur's Gate* extended them to artifacts. With [Roles and bargain](/en/articles/feature/2023/08-15-wilds-of-eldraine-mechanics), *Wilds of Eldraine* had an enchantment theme, so we thought it would be cool to do a cycle of Adventures that went on global enchantments. But what should those enchantments do?

Here's the part in the story when our chocolate meets our peanut butter. While we had decided *Wilds of Eldraine* would focus more on the fairy-tale side of the plane, we still wanted some nods towards the courts, and it turns out that, while the virtues had been part of the world building, they hadn't been as incorporated into the cards as they could have been. What if our five Adventure enchantments represented the five virtues of the courts?

For starters, this meant the cards wanted to be monocolor. We did plan to do off-color Adventures somewhere in the set, but the virtues being tied to monocolor courts made that a bad fit for this cycle. Vision Design made a rare cycle of virtues, but the cycle got pushed to mythic rare when it went to set design.

The key to the design was to make a powerful enchantment that felt like it embodied the virtue, something that the player would want to have access to every turn. The enchantment would constitute most of the card's power. Then we had to find an instant or sorcery to be the Adventure that mechanically connected to the chosen enchantment effect.

Here's a list of the abilities tried for each color before finding the final version:

**Virtue of Loyalty**  
 Creatures you control get +1/+1. //ADV// Ardenvale Aid {o1oW} Sorcery  
 Create two 1/1 white Human creature tokens.  
 At the beginning of each end step, if a creature with power 2 or less entered the battlefield under your control this turn, draw a card. //ADV// Demonstrate Loyalty {o1oW} Sorcery - Adventure Create a 2/2 white Knight creature token with vigilance. (Then exile this card. You may cast the creature later from exile.) 

Loyalty felt like it wanted to be about rewarding your creatures, so all the enchantments the design teams chose either boosted your team or rewarded you for having a large team. In every version, the Adventure created a creature token.

**Virtue of Knowledge**  
 You may look at the top card of your library any time. You may cast noncreature spells from the top of your library. //ADV// Vantress Aid {o1oU} Sorcery — Adventure Scry 2. (Then exile this card. You may cast the enchantment later from exile.) 

The Vision Design team started by using an ability that let you cast more spells, but we go to that well often, and it didn't seem exciting enough. Instead, we decided to make the effect more powerful but more niche. While the white virtue was generally useful, the blue version encourages you to build around it.

**Virtue of Persistence**  
 At the beginning of your upkeep, return target creature card from your graveyard to your hand. Whenever a creature you control dies, exile it. //ADV// Locthwain Aid {oB} Sorcery — Adventure As an additional cost to cast this spell, sacrifice a creature. Destroy target creature. (Then exile this card. You may cast the creature later from exile.) 

Skip your draw step. Pay X life: Exile the top X cards of your library face down. Put them into your hand at the beginning of your next end step. //ADV// Demonstrate Persistence {o1oB} Instant — Adventure CARDNAME deals 2 damage to target creature or planeswalker and you gain 2 life. 

The low hanging fruit of persistence in black is some form of recursion. The Vision Design team started with returning creatures from graveyard to hand. The Set Design team then tried a very different approach, making a spell that felt like Necropotence (historically one of black's most powerful spells). This just didn't feel enough like persistence, so they went back to recursion, but strengthened it by returning the creatures to the battlefield rather than to the hand.

**Virtue of Courage**  
 If an attacking creature you control would deal damage, it deals double that damage instead. //ADV// Embereth Aid {oR} Sorcery — Adventure Target creature gets +1/+0 and gains first strike until end of turn. (Then exile this card. You may cast the creature later from exile.)

If an instant or sorcery spell you control would deal damage to a creature, planeswalker, or player, it deals twice that much damage to that permanent or player instead. //ADV// Demonstrate Courage {oR} Sorcery - Adventure CARDNAME deals 2 damage to any target. 

The Vision Design team liked the idea that the spell encouraged your creatures to attack, as that felt very courageous. The doubling theme spent a little time moving to spells before Set Design realized it feel courageous enough. They ended up with an impulsive draw trigger that again encouraged attacking because that best captured the virtue.

**Virtue of Strength**  
 Creatures you control have trample. At the beginning of your upkeep, if you control a creature with power 4 or greater, draw a card. //ADV// Garenbrig Aid {o1oG} Sorcery — Adventure Put two +1/+1 counters on target creature you control. (Then exile this card. You may cast the creature later from exile.)

If you would put one or more counters on a permanent or player, put those counters plus additional counter of each of those kinds on that permanent or player instead. //ADV// Demonstrate Strength {o1oG} Instant - Adventure Distribute two +1/+1 counters among one or two target creatures. 

The Vision Design team started focusing on encouraging big creatures, as that made the most sense to capture the idea of strength. Set Design then experimented with caring about buffing up your creatures, making them into big creatures.

In the end, none of those designs worked out, and the Set Design team decided to be a little more symbolic in what strength meant, strengthening you the player rather than your creatures. The combination of the Adventure spell along with the enchantment did allow you to get your biggest creature from the graveyard to the battlefield.

## *Wilds* at Heart

Those are all the card-by-card design stories I have time to tell. As always, I'm eager to hear your thoughts on today's article, on any of the cards I talked about, or on *Wilds of Eldraine* as a set. You can email me or contact me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [Tik Tok](https://www.tiktok.com/@markrosewater)).

Join me next week when I explore how we distributed the ten fairy tale archetypes in *Wilds of Eldraine*.

Until then, may your games with *Wilds of Eldraine* end happily ever after.