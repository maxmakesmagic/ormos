---
id: 3es7q5zh
kind: article
lang: en
path: /en/articles/makingmagic/2023/01-30-mission-compleat-part-1
title: Mission Compleat, Part 1
published: '2023-01-30'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    lang_detected: en
    capture_id: 223235
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    captured_at: '2024-05-18 01:25:50+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    lang_detected: en
    capture_id: 223235
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    captured_at: '2024-05-18 01:25:50+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    lang_detected: en
    capture_id: 223235
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    captured_at: '2024-05-18 01:25:50+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    lang_detected: en
    capture_id: 223235
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
    captured_at: '2024-05-18 01:25:50+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 3es7q5zh
  url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
  page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:25:50+00'
  capture_id: 223235
  wayback_url: https://web.archive.org/web/20240518012550id_/https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3es7q5zh
  capture_id: 223235
  url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
  wayback_url: https://web.archive.org/web/20240518012550id_/https://magic.wizards.com/en/news/making-magic/mission-compleat-part-1
  captured_at: '2024-05-18 01:25:50+00'
  template: contentful
  sha256: bc971822577a4ce65582be03dec549c1639ad2bfb4f1887464fe55113a408c45
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
After I finish my columns on the story of a set's design, I have an article or two where I go over card-by-card design stories from the set. Normally, I focus on cards that have a higher profile, such as planeswalkers and legendary creatures, which means I tend to write more about rares and mythic rares. To change things up today, I'm going to tell stories about some of the commons from *[Phyrexia: All Will Be One](https://web.archive.org/web/20230130000000/https://magic.wizards.com/en/products/phyrexia-all-will-be-one)*.

**Anoint with Affliction**

![](https://media.wizards.com/2023/one/en_02133f7bc6.png)

Let's begin with a very effective common kill spell. All sets need a certain number of destruction spells in black at common, usually a mix of ones that can kill anything (unconditional) and others that are situational (conditional). The default is one of the former and two of the latter, but it can chance set to set. As with any basic effect that we use all the time, we're always up to finding ways to have it interact with a mechanic and/or theme from the set to make it feel organic to the product it's in. This slot went through a lot of change, so I'll walk you through it and explain why it kept changing.

**Deadly Attitude (version #1)**  
 B  
 Instant  
 Target creature gets +1/+0 and gains deathtouch until end of turn.  
 Relentless (p/b) *(When you cast this from your hand, exile it. When you cast another spell, you may cast this card for its relentless cost.)*

The earliest version was what we call a "sideways kill card." It's a card that can help you kill a creature that you normally couldn't. This first design is a creature combat card designed to help you boost a blocker to take out an attacker. Combat cards are usually counted as a different slot than normal creature destruction.

This design made use of relentless, a mechanic we were trying out in vision design. (p/b) is how we write out black Phyrexian mana. All hybrid costs are written this way with Phyrexian mana getting a lowercase p instead of another color. Note that the early version of relentless cared about you playing a spell rather than a land.

**Deadly Attitude (version #2)**  
 1B  
 Sorcery  
 Target opponent loses 2 life. You gain 2 life.  
 Relentless 1(p/b)(p/b) *(If you cast this spell from your hand, exile it as it resolves. You may cast it from exile for its relentless cost if you've cast a spell with a different name that turn.)*

The last effect didn't work well as a relentless card. Normally, we're careful not to have cards that can be replayed easily destroy creatures to keep them from being two-for-ones (especially at common). The next effect we tried was one that drained the opponent. Note that we tweaked relentless so that it required casting a different spell.

**Intermittent Headache (version #3)**  
 1B  
 Sorcery  
 Target opponent discards a card and loses 1 life. Relentless 1(p/b)(p/b) *(If you cast this spell from your hand, exile it as it resolves. You may cast it from exile for its relentless cost if you've played a land that turn.)*

The drain spell wasn't impactful enough, so we decided to try it as a discard spell. This is a good example of how it can be tricky to understand what works best with new mechanics, so the technique is usually to try something and change it for the next playtest if it doesn't play well. This gets complicated by the fact that we'll often tweak the mechanic as well. Note that relentless now cares about you playing a land.

While relentless on its surface feels like a flashback variant, playtesting can help us understand all the ways in which it's different. The two biggest differences included everything being restricted to turns that you've played lands and the ability to use life as a payment.

**Diseased Mind (version #4)**  
 2B  
 Sorcery  
 Target opponent discards two cards. For each card they can't discard, proliferate.

Relentless was pulled at this point (we're in set design), so the card remained a discard spell but was then tied to a different mechanic in the set, proliferate. During vision design, proliferate was in blue, green, and red, but Set Design moved it to blue, green, and black for a combination of balance and color-pie reasons.

**Fade to Black (version #5)**  
 2B  
 Sorcery  
 Destroy target creature with power 3 or less.

We finally allocated a destruction spell to this slot. The card is essentially a repeat (Vanquish the Weak) but with a new name. The fact that it's just a reprint says to me that the Set Design team wasn't quite sure what to do with this slot but decided they wanted it to be creature destruction, so they put in a reprint as a placeholder.

**Reave Soul (version #6)**  
 1B  
 Sorcery  
 Destroy target creature if it has mana value 3 or less.  
 *Corrupted* – Destroy that creature if its controller has 3 or more poison counters.

The Set Design team eventually decided that they wanted this to have corrupted. The low-hanging fruit was to make it a conditional kill spell that becomes an unconditional kill spell when your opponent is corrupted. Two questions remained: what is the conditional limitation, and what should it cost?

The team decided they wanted to be more aggressive with the mana value, dropping it from 2B to 1B. This means the base ability must be a little weaker, so they made the tweak of changing power to mana value. This hits a smaller subset of creatures, and ones that, on average, are of a lower power level. The final version only makes one change from this version in that it becomes an exile effect rather than destruction. This change came about because Play Design asked Set Design to change it, as they wanted more exile effects in Standard. This change also allowed it to be an answer to the mythic rare Domini. You want to have common answers to your bomb mythic rares.

Finally, here's the art description for the card:

**Setting**: "Lacrosse"  
 **Color**: Spell associated with black mana  
 **Location**: Mirrex (see pages 66–79 of the world guide)  
 **Action**: Please show the moment when a Steel Thane priest (page 144a) writes with its claws to inscribe a Phyrexian inscription (page 11, choose your favorite) into the bare back of a male humanoid aspirant (pages 146–148). The inscription is written with green necrogen acid (page 79). Avoid blood and gore.  
 **Focus**: The action of inscribing  
 **Mood**: Horrifying ritual  
 **Notes**: Copy the Phyrexian text exactly from the world guide. Do not attempt to modify it without first consulting us.

**Basilica Shepherd**

![](https://media.wizards.com/2023/one/en_4f99e651ee.png)

I'd like to start this card's design story with a trivia question.

Is Basilica a real word or a made-up word?

## Click here to see the answer

 

It's a real word. It's a type of a building, originally used in ancient Rome, which most often shows up in church designs.

* * *

This Phyrexian Angel went through a lot of changes. Let's take a look.

**Blessbringer (version #1)**  
 3W  
 Creature — Phyrexian Cleric  
 3/4  
 Tainted 2 *(You may choose to have this creature enter the battlefield with N -1/-1 counters.)*  
 When CARDNAME enters the battlefield with two -1/-1 counters on it, you gain 3 life.

The first version of the card used a mechanic we tried in early vision design. This is back when infect was in the set, so it used -1/-1 counters. We were exploring different ways to use -1/-1 counters, and tainted was an attempt to use them in a kicker-like way. You could choose to have the creature enter with some number of -1/-1 counters, and if you did, you would get an effect. Would you rather have a 3/4 flier or a 1/2 flier that gains you 3 life?

It turns out you'd rather have a 3/4 flier just about every time. We found that shrinking creatures for extra effects was not the most lucrative design space, so we got rid of tainted (before we got rid of -1/-1 counters, I believe).

**Phyrexian Angel (version #2)**  
 4W  
 Creature — Phyrexian Angel  
 3/3  
 Flying  
 When CARDNAME enters the battlefield, gain 2 life for each poison counter all opponents have.

The next version turned into an Angel and gained flying. We then tried it as what we called a "poison scaling card," a card that gets stronger the more poison the opponent has. We tried scaling alongside corrupted and found corrupted tended to do a better job, so scaling got scaled back (although there's a little left in the set).

**Oilbringer (version #3)**  
 4W  
 Creature — Phyrexian Angel  
 3/3  
 Flying  
 When CARDNAME enters the battlefield, put an oil counter on target permanent you control.

One thing that's common in design is that you try to connect your cards to different aspects of your set, but when one thing doesn't work, you often try a different theme. Instead of caring about poison, this version interacted with oil counters. Set Design was trying to figure out how often they wanted to have a card that interacted with oil counters without giving you a way to use them. The answer was "just a little."

**Mitebringer (version #4)**  
 4W  
 Creature — Phyrexian Angel  
 3/3  
 Flying  
 When CARDNAME enters the battlefield, create a colorless 1/1 Phyrexian Mite artifact creature token with poisonous 1 and "This creature can't block."

Set Design decided they preferred the Angel interacting with poison, so this time they had it create a Mite token. Mite tokens had been designed in vision design to let white have a swarm poison strategy. This card would eventually get pushed from creating one Mite to creating two. This forced the mana cost from 4W to 3WW. We don't do a lot of doubled-color mana pips at common (and when we do, it tends to be on higher-mana cards like this), so this was a means to make this card core to white.

Here's the art description:

**Setting**: "Lacrosse"  
 **Color**: White creature  
 **Location**: The Monumental Facade (pages 15–24)  
 **Action**: A Phyrexian angel (page 119A) soars through the sky. She holds a small Phyrexian mite swaddled in red cloth. Use the designs on page 115 as inspiration to design your own mites. Maybe the angel has several sets of arms and has a mite "child" swaddled in each one. Maybe we see some of the five colored suns behind her.  
 **Focus**: The angel  
 **Mood**: A holy mother with her children

**Experimental Augury**

![](https://media.wizards.com/2023/one/en_9a364f301c.png) ![](https://media.wizards.com/2023/one/en_21c1b1378f.png)

This card is referred to as "Anticipate Proliferate" in R&D. Let's walk through its evolution.

**Thought Experimentation (version #1)**  
 4U  
 Instant  
 Draw two cards. Proliferate.

From the very beginning, this card was tied to two things, card drawing and proliferating. Often our first stab at something is the simplest version of it. Let's take Inspiration (3U) and add proliferate to it. Inspiration has room to add something to it but not quite enough to get proliferate, so the cost went up to 4U.

**Laboratory Incrementor (version #2)**  
 2U  
 Creature — Phyrexian Wizard  
 2/3  
 At the beginning of your end step, if you cast an instant or sorcery spell this turn, proliferate.

This slot then moved from common to uncommon and turned into a creature. The reason for both changes was to try and create a proliferate build-around, a card you would pick early that would encourage you to draft a deck around it.

**Productive Research (version #3)**  
 U  
 Instant  
 Proliferate.  
 Relentless (1U) *(If you cast this spell from your hand, exile it as it resolves. Whenever you play a land, you may cast this from exile for its relentless cost.)*

The design team decided they wanted to turn this uncommon slot back into a spell slot rather than a creature slot (I assume because of changes made elsewhere in the file). At that time, Erik had been trying to make relentless work. Note that he'd removed Phyrexian mana from the relentless cost. Proliferate is a nice effect to get to do twice, so it made for a good relentless design. It also allowed Erik to make a cheap relentless spell.

**Contentious Plan (version #4)**  
 1U  
 Instant  
 Proliferate. Draw a card.

Relentless was removed from the file, so we had to redesign the card. It was at that time the slot went back to common. Unsure of what to do with the slot, the Set Design team turned it into a simple reprint.

**Augmented Core (version #5)**  
 2U  
 Instant  
 Look at the top four cards of your library. Put one of them into your hand and the rest on the bottom of your library in any order. Proliferate. *(Choose any number of permanents and/or players, then give each another counter of each kind already there.)*

The set needed some card filtering, so they turned the proliferate common into a filtering card. The design changed to "Impulse plus proliferate" but would end up as "Anticipate plus proliferate" to allow them to drop it down to a 1U cost.

Here's the art description:

**Setting**: "Lacrosse"  
 **Color**: Spell associated with blue mana  
 **Location**: A workshop in The Surgical Bay (pages 54–65)  
 **Action**: Show us a shot looking inside a Phyrexian's head as a Phyrexian scientist (page 126d) performs surgery on it.  
 **Focus**: The surgery  
 **Mood**: Science and horror  
 **Notes**: This is not a gory surgery, mostly mechanical with machine and organic matter.

**Planar Disruption**

![](https://media.wizards.com/2023/one/en_e2db3a4c51.png)

In white, we normally have a common slot for an Aura that helps answer creatures. It's usually either (in R&D-speak) a Pacifism that stops attacking and blocking or an Arrest that stops attacking, blocking, and activated abilities. The default casting for a Pacifism is 1W, and the default casting for an Arrest is 2W. This has been true for over 20 years.

**Cenobite's Demerit (version #1)**  
 W  
 Enchantment — Aura  
 Enchant creature  
 Enchanted creature can't block.  
 *Corrupted* – As long as an opponent has 3 or more poison counters, enchanted creature can't attack.

Interestingly, this slot started as a Pacifism variant. The first version was made as a corrupted card where once corrupted it became a Pacifism. This allowed it to cost just a single white mana.

**Cenobite's Demerit (version #2)**  
 W  
 Enchantment — Aura  
 Enchant creature  
 Enchanted creature can't attack or block unless its controller pays {2}.  
 *Corrupted* – As long as an opponent has 3 or more poison counters, enchanted creature can't attack or block.

The first version playtested poorly, so they changed it into a version that would have more functionality in the early game. The taxing mostly means the creature is effectively answered until the mid- to late game.

**Cenobite's Demerit (version #3)**  
 W  
 Enchantment — Aura  
 Enchant creature  
 Enchanted creature can't attack or block.  
 *Corrupted* – At the beginning of your upkeep, if an opponent has 3 or more poison counters, gain 1 life.

Upgrades into Pacifism have always been a bit underwhelming, so they then changed it to a Pacifism that upgrades into a life-gaining spell.

**Cenobite's Demotion (version #4)**  
 2W  
 Enchantment — Aura  
 Enchant creature  
 Enchanted creature can't attack or block.  
 *Corrupted* – 2W: Exile enchanted creature and create a 1/1 colorless Phyrexian Mite artifact creature token with poisonous 1. Activate this ability only if an opponent has three or more poison counters.

This is Vision Design's last attempt at making a corrupted version. The previous versions were a bit weak, so we tried a version that started as a Pacifism for 2W that then upgraded to remove the creature *and* give you a Mite in exchange.

**Dovishness (version #5)**  
 1W  
 Enchantment — Aura  
 Oily 5 *(This enters the battlefield with five oil counters on it. At the beginning of your upkeep, remove an oil counter from it. When the last is removed, sacrifice it.)*  
 Enchant creature  
 Enchanted creature can't attack or block.  
 Remove an oil counter from CARDNAME: Attach CARDNAME to target creature. Activate this only when you could cast a sorcery.

At this point, the file was with Set Design (led initially by Erik Lauer but handed off to Adam Prosak after two months). Erik had taken the oiled mechanic that Vision Design turned in, which was a means to signify that a creature entered with a certain number of oiled counters, and turned it into a mechanic that matched what vanishing does (remove one counter a turn and sacrifice the permanent when you remove the last counter).

**Dovishness (version #6)**  
 1W  
 Enchantment — Aura  
 Oily 6 *(This enters the battlefield with six oil counters on it. At the beginning of your upkeep, remove an oil counter from it. When the last is removed, sacrifice it.)*  
 Enchant creature  
 Enchanted creature can't attack or block, and its activated abilities can't be activated.

Playtesting showed that the previous version was both fiddly and complicated to monitor, especially as players planned turns ahead. This version simplified things, turning Pacifism into Arrest and changing the oil counters from five to six. Note this is the first version to essentially be a 1W Arrest (although one that eventually goes away).

**Bound in Gold (version #7)**  
 2W  
 Enchantment — Aura  
 Enchant permanent  
 Enchanted permanent can't attack, block, or crew Vehicles, and its activated abilities can't be activated unless they're mana abilities.

Oily went away, so Set Design turned this into a reprint, again mostly marking the slot.

**Arrest (version #8)**  
 2W  
 Enchantment — Aura  
 Enchant creature or planeswalker  
 Enchanted permanent can't attack or block, and its activated abilities can't be activated.

The card stayed a reprint but changed to a straight Arrest, I assume because dealing with planeswalkers was more important than dealing with Vehicles. (The set does have ten planeswalkers, more than any set save *War of the Spark*.)

**Norn's Arrest (version #9)**  
 2W  
 Enchantment — Aura  
 Enchant artifact, creature, or planeswalker  
 Enchanted permanent can't attack or block, and its activated abilities can't be activated.

The design then changed to a new version that worked on artifacts. The Phyrexians have a long association with artifacts, so there are a lot in the set. There was one important final change made by Play Design. The cost was dropped from 2W, the cost that Arrest has usually been at, to 1W. Play Design wanted to strengthen it for Limited and felt that it wouldn't have a negative impact on Constructed. (I was told by Play Design that Ossification is a better candidate for Constructed decks.)

Here's the art description for the card:

**Setting**: "Lacrosse"  
 **Color**: White spell  
 **Location**: The Monumental Facade (pages 15–24)  
 **Intent**: This card is part of a set that showcases story moments from this release. The Wanderer and Kaito have just landed on New Phyrexia, but an enemy force field has messed with their powers, and the Wanderer is fading away.  
 **Action**: The Wanderer and Kaito reach out toward each other, but her arms have become transparent and pass through him. See attached references for character designs. Maybe the atmosphere is filled with poisonous dust (see pages 19 and 23). We're open to any solutions you have for a more abstract interpretation.  
 **Focus**: The fading Wanderer  
 **Mood**: "Don't go!" Two close friends being separated by an evil force.  
 **Notes**: Do not include Kaito's tanuki robot.

## Common Ground

I hope you enjoyed my peek at the design of some of *Phyrexia: All Will Be* *One*'s commons. As always, I'm eager for any feedback, be it about the column, the cards I talked about today, or *Phyrexia: All Will Be One*. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I share more card-by-card stories from *Phyrexia: All Will Be One*.

Until then, may you play lots of commons.