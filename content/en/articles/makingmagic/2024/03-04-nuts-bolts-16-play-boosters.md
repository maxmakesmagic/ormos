---
id: db40vhcx
kind: article
lang: en
path: /en/articles/makingmagic/2024/03-04-nuts-bolts-16-play-boosters
title: 'Nuts & Bolts #16: Play Boosters'
published: '2024-03-04'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    lang_detected: en
    capture_id: 373334
    url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    captured_at: '2024-07-03 02:10:21+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    lang_detected: en
    capture_id: 373334
    url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    captured_at: '2024-07-03 02:10:21+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    lang_detected: en
    capture_id: 373334
    url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    captured_at: '2024-07-03 02:10:21+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    lang_detected: en
    capture_id: 373334
    url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
    captured_at: '2024-07-03 02:10:21+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: db40vhcx
  url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
  page_key: magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
  lang: en
  template: contentful
  captured_at: '2024-07-03 02:10:21+00'
  capture_id: 373334
  wayback_url: https://web.archive.org/web/20240703021021id_/https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: db40vhcx
  capture_id: 373334
  url: https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
  wayback_url: https://web.archive.org/web/20240703021021id_/https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-16-play-boosters
  captured_at: '2024-07-03 02:10:21+00'
  template: contentful
  sha256: f4f26dcd76c93f4a4cdf305806b7245727f2a7fb44b05da97458bf824663efdf
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
Sometime during the first three months of each year, I write a column from a series I call "Nuts & Bolts" where I talk about the nitty-gritty of how to make a *Magic* set. The series is intended for amateur game designers who want to get better at *Magic* design, but it's also a technical peek behind the curtain at the nitty-gritty aspects of design, which I hope will be interesting to everyone else.

This is my sixteenth year doing a "Nuts & Bolts" column. Here are the previous fifteen (my 2020 column was a two-parter):

"[**Nuts & Bolts #1: Card Codes**](/en/articles/makingmagic/2012/01-13-nuts-bolts-card-codes)"

The first column is the most technical, explaining how we use a system to make sure everyone is always talking about the same card.

"[**Nuts & Bolts #2: Design Skeleton**](/en/articles/makingmagic/2010/02-15-nuts-amp-bolts-2-design-skeleton)"

The second column introduces the most important tool in designing a set, something called a design skeleton. (It makes use of card codes, which is why that article came first.)

"[**Nuts & Bolts #3: Filling in the Design Skeleton**](/en/articles/makingmagic/2011/02-28-nuts-bolts-3-filling-in-the-design-skeleton)"

The third column talks about how you begin filling in your design skeleton, starting with the common cards.

"[**Nuts & Bolts #4: Higher Rarities**](/en/articles/makingmagic/2012/02-27-nuts-and-bolts-higher-rarities)"

The fourth column talks about filling in all the other rarities.

"[**Nuts & Bolts #5: Initial Playtesting**](/en/articles/makingmagic/2013/02-12-nuts-bolts-initial-playtesting)"

The fifth column discusses how best to use playtesting to gather feedback and make improvements on your set.

"[**Nuts & Bolts #6: Iteration**](/en/articles/makingmagic/2014/03-04-nuts-bolts-iteration)"

The sixth column talks about the concept of iteration and how you can incrementally improve your set.

"[**Nuts & Bolts #7: The Three Stages of Design**](/en/articles/makingmagic/2015/03-30-nuts-bolts-the-three-stages-of-design)"

The seventh column explains the three different stages of design, walking you through how your priorities shift as the set evolves.

"[**Nuts & Bolts #8: Troubleshooting**](/en/articles/makingmagic/2016/02-16-nuts-bolts-troubleshooting)"

The eighth column answers several questions about common problems that can happen in the early to mid-design stages.

"[**Nuts & Bolts #9: Evaluation**](/en/articles/makingmagic/2017/02-21-nuts-bolts-evaluation)"

The ninth column talks about how you can look at your set as a whole and figure out what fine-tuning it still needs.

"[**Nuts & Bolts #10: Creative Elements**](/en/articles/makingmagic/2018/03-26-nuts-bolts-10-creative-elements)"

The tenth column discusses how you interweave your mechanical and creative elements into a cohesive set. It discusses both top-down (starting with the flavor) and bottom-up (starting with the mechanics) design. I then go into detail about how to handle names, creature types, and flavor text.

"[**Nuts & Bolts #11: Art**](/en/articles/makingmagic/2019/02-12-nuts-bolts-11-art)"

The eleventh column talks about the importance of using art in later playtests and how to incorporate it into your set.

"[**Nuts & Bolts #12, Part 1: Limited (Mechanics)**](/en/articles/makingmagic/2020/03-09-nuts-bolts-12-part-1-limited-mechanics)"

I broke the twelfth column into two parts. Both talk about how to ensure your set is working properly in Limited. The first article focuses on making sure your mechanics work for Limited play.

"[**Nuts & Bolts #12, Part 2: Limited (Themes)**](/en/articles/makingmagic/2020/03-16-nuts-bolts-12-part-2-limited-themes)"

The second part focuses on building out themes for Limited play.

"[**Nuts & Bolts #13: Design Skeleton Revisited**](/en/articles/makingmagic/2021/03-22-nuts-bolts-13-design-skeleton-revisited)"

R&D revamped its default design skeleton, so I went through it talking about what elements are in every *Magic* set.

"[**Nuts & Bolts #14: Initial Ideation**](/en/articles/makingmagic/2022/03-07-nuts-bolts-14-initial-ideation)"

My fourteenth column covered how to flesh out an idea to create a new set.

"[**Nuts & Bolts #15: Structural Support**](/en/articles/makingmagic/2023/03-06-nuts-bolts-15-structural-support)"

Last year, I talked about what we call "structural support," a design step where we make sure sets have all the elements they need to work properly, especially in Limited.

* * *

This brings me to my sixteenth "Nuts & Bolts" column. In 2021, I walked you all through our default set skeleton. For those unfamiliar with what that is, it's a structural tool R&D uses to see what elements need to be in every *Magic* set and to help us build it in such a way that it functions properly. If you want more information on the basics of what a design skeleton is, [you can read my original article on the topic](/en/articles/makingmagic/2021/03-22-nuts-bolts-13-design-skeleton-revisited).

Part of my reason for showing off the latest design skeleton was to better demonstrate how things were changing. *Murders at Karlov Manor* introduced the Play Booster, a combination of the Draft Booster and the Set Booster that *Magic* used to sell. Today, I'm going to walk you through the default set skeleton for Play Boosters. In doing so, I will explain what the differences are in how we build sets based on the change.

The set skeleton is usually focused on the common slots. The old default set structure broke down the uncommon slots in a little more detail than the current one. The current set skeleton just lists how many slots at uncommon are for creatures and how many are for noncreatures. It's important to remind you that set skeletons are a starting-off point when making a set. Sets will change as they evolve, and slots can move to accommodate the needs of the particulars of that set. This set skeleton is just a jumping-off point.

## "The Play's the Thing"

Before we get into the particulars, let me go over the two biggest changes to set structure in the Play Booster world:

First, the number of cards per rarity has shifted, although just for common and uncommon.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Rarity</strong></td>&#10;			<td><strong>Play Boosters</strong></td>&#10;			<td><strong>Draft Boosters</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td><strong>Common</strong></td>&#10;			<td>81</td>&#10;			<td>101</td>&#10;		</tr>&#10;		<tr>&#10;			<td><strong>Uncommon </strong></td>&#10;			<td>100</td>&#10;			<td>80</td>&#10;		</tr>&#10;		<tr>&#10;			<td><strong>Rare </strong></td>&#10;			<td>60</td>&#10;			<td>60</td>&#10;		</tr>&#10;		<tr>&#10;			<td><strong>Mythic Rare </strong></td>&#10;			<td>20</td>&#10;			<td>20</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

The sets have the same number of unique cards (261), but 20 cards have shifted from common to uncommon. This 20-card shift will have a big influence on how we treat what goes at common and what goes at uncommon.

Second, Draft Boosters, save premium and foil cards, had a locked number of slots for each booster: one land slot, ten common slots, three uncommon slots, and one rare or mythic rare slot. (I should note that this was the default. Things like double-faced cards could change the number of rares or mythic rares in a booster.) Play Boosters, because they weave in what players enjoyed about Set Boosters (having multiple rares or mythic rares was the highest-rated attribute of Set Boosters), have variance in how many of each rarity appears in a booster.

For example, a Play Booster is guaranteed to have at least one rare or mythic rare but can have as many as four. (The as-fan of rares and/or mythic rares in a *Murders at Karlov Manor* Play Booster is slightly over 1.4; or in other words, you get two or more rares and/or mythic rares 41% of the time.) This change in as-fan of rares and mythic rares has an impact on Limited play. As you will see, these two factors have a big role in how the structure of set design evolves with the introduction of Play Boosters.

For each color, I will look at the common creature slots, including what we call "keyword distribution" (it says roughly how many of each keyword will appear at common), then the common spell slots, and finally the uncommon numbers for creature and noncreature slots.

### ![White mana symbol](https://media.wizards.com/2023/images/daily/w.png) White

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW01: One-mana creature</td>&#10;			<td>CW01: One-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW02: Two-mana creature</td>&#10;			<td>CW02: One or two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW03: Two-mana creature</td>&#10;			<td>CW03: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW04: Two-mana creature</td>&#10;			<td>CW04: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW05: Three-mana creature</td>&#10;			<td>CW05: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW06: Three-mana creature</td>&#10;			<td>CW06: Two- or three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW07: Three-mana creature</td>&#10;			<td>CW07: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW08: Four-mana creature</td>&#10;			<td>CW08: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW09: Four-mana creature</td>&#10;			<td>CW09: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW10: Five- or six-mana creature</td>&#10;			<td>CW10: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW11: Six- or seven-mana creature</td>&#10;			<td>CW11: Five-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CW12: Five- or six-mana creature</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Having less commons means less overall cards, both in creatures and noncreatures. White is still number one in the number of creatures, meaning it gets the most creatures by percentage of any color. While it's gone down one creature slot from Draft Boosters to Play Boosters, it's gone up in percentage. The default for Draft Boosters was 63% (12 out of 19) while the default for Play Boosters is 73% (11 out of 15).

The reason for this is that the drop in common cards means we have no room for "unplayable commons." "Unplayable common" is defined as a card that situationally might be unplayable in a sealed deck. The card is too narrow in what it does. A good example would be what we used to call "sideboard cards," such as Naturalize or Disenchant ("Destroy target artifact or enchantment"). It's the kind of card you usually don't start with because it often is a dead card in your hand, but you might sideboard it in if the opponent is running threats that it answers. The other major reason a card might be unplayable is power level.

We're doing three things to get rid of unplayable commons. One, the average power level will be higher (although set more for Limited play than Constructed). If you're playing a color, most monocolor creatures in that color will at least be playable in your deck. Some creatures may be more synergistic with certain draft themes, but the base creature stats will usually be something you can run. Two, we're moving some effects from common to uncommon. An example is temporary stealing (cards like Threaten) that we normally do at common in red. Three, we'll be making more use of modal effects. We can still do a Naturalize or Disenchant effect at common, but it will be paired with another effect that is generally more useful, allowing it to be standard in your deck.

The result of these changes is that the creature percentages at common are going up a bit. Creatures are just easier to make usable in more decks and inherently have a built-in win condition.

The other major effect you can see on creatures is that the average size is going up, especially in white. In Draft Boosters, white's default average power was 2.95. In Play Boosters, that goes up to 3.28. That's around a third of a power greater. This is being done to ensure that every creature is playable, as lower-powered creatures can become more situational.

**Keyword Distribution (At Common)**

*   3 Flying (different powers)
*   2 Vigilance
*   1 Lifelink (low power)
*   0.25 First strike
*   0.20 Double strike

This set skeleton is set up a bit differently than the last one. Rather than call out slots for certain keyword abilities at common, the set skeleton lays out roughly how often it should appear. If an ability appears at a number below one, that means it might not always appear in every set but will average that number over multiple sets. However, first strike in white has fallen out of favor with R&D. The ability causes ground stalls, which is why we often only make it work offensively.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Spells (Play Booster)</strong></td>&#10;			<td><strong>Common Spells (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW12: Combat-related removal</td>&#10;			<td>CW13: 6–7 Small removal (usually damage to attacker/blocker)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW13: Banishing Light</td>&#10;			<td>CW14: Can't attack or block Aura (sometimes stops abilities)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW14: Combat trick</td>&#10;			<td>CW15: Destroy large/tapped creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CW15: Disenchant/removal spell</td>&#10;			<td>CW16: Combat trick</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CW17: Positive Aura/Equipment</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CW18: Go-wide team-pump effect</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CW19: Destroy artifact/enchantment</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Common spells must be a bit more practical. For white, which has the least spells by percentage, that means focusing mostly on removal cards. Combat tricks want to prioritize designs that save the creature (meaning you use them to functionally get rid of the opponent's creature without going down on creatures). Pacifism-style effects (Auras that keep you from attacking, blocking, and sometimes activating) are being replaced by Banishing Light-style effects (cards that exile something while they're on the battlefield). Effects that neutralize a creature without killing it need to have more "text wiping" because many rares have powerful noncombat abilities, often static or triggered, and the common cards need to be able to answer them. The Disenchant slot will most often be modal and will sometimes be an answer to creatures in addition to artifacts and enchantments.

I also want to point out that this change forces certain effects out of spells and onto creatures. I'll use the go-wide team-pump effect ("Creatures you control get +N/+N until end of turn."). Uncommon can clearly do larger pumps that help win games, but the simple +1/+1 granting will probably exist more on a creature as an "enters the battlefield" effect or an activated ability.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>10 Creatures</td>&#10;			<td>8 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>4 Noncreatures</td>&#10;			<td>5 Noncreatures</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

While uncommon goes up 20 cards, only five are seen in monocolor, one per color. Like common in white, there is a shift upward in creature percentages. For example, creatures in white go from 61% (8 of 13) to 72% (10 of 14) at uncommon. This is due to the same larger factors. We just want more Limited-playable cards at common and uncommon.

Uncommon cards are also being raised in power level because they must compete more directly with rares and mythic rares.

Another change to uncommon is a shifting away from "sideways build-arounds." More of those designs can be done at rare, as rares show up more frequently than they did in the Draft Booster world.

### ![Blue mana symbol](https://media.wizards.com/2023/images/daily/u.png) Blue

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU01: Two-mana creature</td>&#10;			<td>CU01: One-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU02: Two-mana creature</td>&#10;			<td>CU02: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU03: Three-mana creature</td>&#10;			<td>CU03: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU04: Three-mana creature</td>&#10;			<td>CU04: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU05: Three-mana creature</td>&#10;			<td>CU05: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU06: Four-mana creature</td>&#10;			<td>CU06: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU07: Five- or six-mana creature</td>&#10;			<td>CU07: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU08: Six- or seven-mana creature</td>&#10;			<td>CU08: Five-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CU09: Six-mana creature or higher</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Blue creature percentages have gone up, but not as much as white, from 47% (9 out of 19) to 53% (8 out of 15). The average power has gone up from 3.39 to 3.62. For instance, there's no longer a default one-drop in blue at common and potentially multiple six-drops.

**Keyword Distribution (At Common)**

*   3 Flying (different powers)
*   1.5 Vigilance
*   0.5 Ward N
*   0.5 Defender
*   0.5 Flash

A year ago, we made a big change to add vigilance to blue. It's now the second-most-used keyword, mainly because making blue creatures want to attack can be difficult. Also, while this is not unique to blue, it's the most notable in blue: we're being more cautious with toughness-statted creatures, as they tend to stall out games.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Spells (Play Booster)</strong></td>&#10;			<td><strong>Common Spells (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU09: Protective instant</td>&#10;			<td>CU10: 0-power creature, defender, or noncreature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU10: Counterspell</td>&#10;			<td>CU11: &quot;Hard&quot; counterspell (counters anything)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU11: Cantrip</td>&#10;			<td>CU12: &quot;Soft&quot; counterspell (conditionally counters things or a subset)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU12: Draw spell (two to three cards)</td>&#10;			<td>CU13: Lockdown Aura</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU13: Witness Protection Aura</td>&#10;			<td>CU14: Card drawing (no more than three)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU14: Top or bottom spell</td>&#10;			<td>CU15: Cantrip/card filtering</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CU15: Modal spell</td>&#10;			<td>CU16: Bounce spell</td>&#10;		</tr>&#10;		<tr>&#10;			<td></td>&#10;			<td>CU17: Positive Aura or combat trick</td>&#10;		</tr>&#10;		<tr>&#10;			<td></td>&#10;			<td>CU18: Disrupt opposing creatures (freezing, tapping, lowering power, etc.)</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CU19: Anything</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Again, we ensure each color has common answers to rare and mythic rare bombs, especially creatures. For blue, this means making counterspells that are good at stopping big spells, trading in its traditional lockdown Aura for one that overwrites the creature ("Enchanted creature is a 1/1 with no abilities") and upping its bounce from hand to top (or bottom if the opponent chooses) of library. Blue also wants to have very efficient card drawing and card filtering.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>6 or 7 Creatures</td>&#10;			<td>7 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>7 or 8 Noncreatures</td>&#10;			<td>6 Noncreatures</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Blue is the one color where creature percentages have gone down at uncommon from 53% (7 out of 13) to 46% (6.5 out of 14).

### ![Black mana symbol](https://media.wizards.com/2023/images/daily/b.png) Black

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB01: One- or two-mana creature</td>&#10;			<td>CB01: One-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB02: Two-mana creature</td>&#10;			<td>CB02: One- or two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB03: Two-mana creature</td>&#10;			<td>CB03: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB04: Three-mana creature</td>&#10;			<td>CB04: Two- or three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB05: Three-mana creature</td>&#10;			<td>CB05: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB06: Four-mana creature</td>&#10;			<td>CB06: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB07: Four- or five-mana creature</td>&#10;			<td>CB07: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB08: Five- or six-mana creature</td>&#10;			<td>CB08: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB09: Six- or seven-mana creature</td>&#10;			<td>CB09: Five-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CB10: Six-mana creature or higher</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Black's creature percentages have jumped from 52% (10 out of 19) to 62% (9 out of 14), and its average power has jumped from 3.25 to 3.56.

**Keyword Distribution (At Common)**

*   2 Flying (different powers)
*   1.5 Menace
*   1.25 Deathtouch
*   1 Lifelink

While black has two common fliers, they're not quite as strong as white's or blue's. That is, they're good enough to include in your deck but are less often the all-star of the common creatures. Menace has been creeping up as it plays so well. Usually, deathtouch is on one of the smaller creatures, whereas lifelink tends to be on something slightly bigger than is seen in white at common.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Spells (Play Booster)</strong></td>&#10;			<td><strong>Common Spells (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB10: Small conditional removal</td>&#10;			<td>CB11: Removal spell (kill anything)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB11: Combat trick</td>&#10;			<td>CB12: Removal spell (kill small things)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB12: Card draw (added cost)</td>&#10;			<td>CB13: Removal spell (forced sacrifice or conditional)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB13: Coercion+</td>&#10;			<td>CB14: Removal spell (conditional, weaker)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB14: Unconditional removal</td>&#10;			<td>CB15: Card draw (added cost)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CB15: Slightly overcosted removal</td>&#10;			<td>CB16: Raise Dead (one or two creatures)</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CB17: Discard (one or two cards)</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CB18: Positive Aura or combat trick</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CB19: Anything</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Again, we focused common spells toward answers to threats. The efficiency of black's creature removal will vary, but all are still worth playing. The discard effect has turned into a Coercion variant (i.e., you get to select what nonland card gets discarded) to help give black more answers to rares and mythic rares. The one other effect we made sure to keep is card drawing. Black must spend a secondary resource, usually life, so the card drawing isn't quite as good as blue but good enough to include in your deck.

Effects that don't have space on a spell at common, like Raise Dead (returning creature cards from the graveyard to the hand), can either be made at uncommon or can be added to creature spells as an effect.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>7 or 8 Creatures</td>&#10;			<td>7 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>7 or 8 Noncreatures</td>&#10;			<td>6 Noncreatures</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

While creature percentages go up in white uncommon and down in blue uncommon, they stay at mostly the same percentage in black.

### ![Red mana symbol](https://media.wizards.com/2023/images/daily/r.png) Red

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR01: One- or two-mana creature</td>&#10;			<td>CR01: One-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR02: Two-mana creature</td>&#10;			<td>CR02: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR03: Two-mana creature</td>&#10;			<td>CR03: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR04: Three-mana creature</td>&#10;			<td>CR04: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR05: Three-mana creature</td>&#10;			<td>CR05: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR06: Three- or four-mana creature</td>&#10;			<td>CR06: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR07: Four- or five-mana creature</td>&#10;			<td>CR07: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR08: Five-mana creature</td>&#10;			<td>CR08: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR09: Six-mana creature</td>&#10;			<td>CR09: Five-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CR10: Five-mana creature or higher</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Red has the second-largest increase in creature percentages at common, jumping from 53% (10 out of 19) to 64% (9 out of 14). Its power has jumped from an average of 3.15 to 3.39. Red's two biggest changes are that it no longer has a guaranteed one-drop slot and instead has a guaranteed six-drop slot.

**Keyword Distribution (At Common)**

*   1.5 Trample
*   1.5 Menace
*   1.5 Haste
*   1 Reach
*   0.25 First strike
*   0.20 Double strike

Like black, we've been increasing red's menace percentages because we've enjoyed how it plays. It also now has a dedicated slot for reach, as having more rares and mythic rares means more flying threats. Like white, first strike is down.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Spells (Play Booster)</strong></td>&#10;			<td><strong>Common Spells (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR10: Direct damage (deals 2)</td>&#10;			<td>CR11: Direct damage (efficient, usually any target)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR11: Combat trick</td>&#10;			<td>CR12: Direct damage (less effective)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR12: Rummaging/impulsive draw</td>&#10;			<td>CR13: Steal/direct damage (ineffective)</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR13: Modal Shatter</td>&#10;			<td>CR14: Team pump/land destruction</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR14: Direct damage (efficient, usually deals 4)</td>&#10;			<td>CR15: Cantrip/rummaging</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CR15: Direct damage (five mana, 6 damage)</td>&#10;			<td>CR16: Positive Aura/Equipment</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CR17: Combat trick</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CR18: Can't block/destroy artifact/direct damage to player</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CR19: Anything</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Half of red's spells are direct damage because it's red's best answer to creatures. We used to top off red common direct-damage spells at 5 but have moved that to 6 to help answer rares and mythic rares. Its artifact destruction is now usually part of a modal spell (if not on a creature). It also has a dedicated card-flow slot, either rummaging (discard and draw) or impulsive drawing (exiling cards that must be played "soon"). The increase in red's creature percentages have meant it's lost more spell space than any other color. Some of that, like temporary stealing, got moved to uncommon. Others are being incorporated into creature designs.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>7 or 8 Creatures</td>&#10;			<td>7 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>7 or 8 Noncreatures</td>&#10;			<td>6 Noncreatures</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Like black, red's uncommon creature percentages have basically stayed the same.

### ![Green mana symbol](https://media.wizards.com/2023/images/daily/g.png) Green

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG01: One- or two-mana creature</td>&#10;			<td>CG01: One-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG02: Two-mana creature</td>&#10;			<td>CG02: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG03: Two-mana creature</td>&#10;			<td>CG03: Two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG04: Three-mana creature</td>&#10;			<td>CG04: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG05: Three-mana creature</td>&#10;			<td>CG05: Three-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG06: Three- or four-mana creature</td>&#10;			<td>CG06: Three- or four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG07: Four- or five-mana creature</td>&#10;			<td>CG07: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG08: Five-mana creature</td>&#10;			<td>CG08: Four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG09: Six-mana creature</td>&#10;			<td>CG09: Five-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG10: Six- or seven-mana creature</td>&#10;			<td>CG10: Five- or six-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CG11: Six-mana creature or higher</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Green has the largest creature percentage increase, going from 58% (11 out of 19) to 71% (10 out of 14). Note that it still has one less creature than white. Its average power rose slightly from 3.59 to 3.7, keeping green the color with the highest average power (i.e., the biggest).

**Keyword Distribution (At Common)**

*   1.5 Vigilance
*   1.5 Trample
*   1.5 Reach
*   1 Deathtouch
*   0.5 Ward N
*   0.20 Haste

Like red, the amount of reach in green has gone up to help accommodate the addition of rare and mythic rare fliers. It also has a smidgen more trample to go with its increased size. Its deathtouch creature is usually one of its smaller creatures, often a one-drop in sets where green has a one-drop. You'll notice haste is listed as 0.20. While green is secondary in haste, it tends to be on larger creatures, usually at higher rarities, and often ones aimed at Constructed.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Spells (Play Booster)</strong></td>&#10;			<td><strong>Common Spells (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG11: Fight spell</td>&#10;			<td>CG12: Fight or bite spell</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG12: Bite spell</td>&#10;			<td>CG13: Power/toughness pumping</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG13: Combat trick (power pump)</td>&#10;			<td>CG14: Another combat trick</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG14: Mana acceleration</td>&#10;			<td>CG15: Cantrip/card filtering</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CG15: Dig for lands and/or creatures</td>&#10;			<td>CG16: Positive Aura or Equipment</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CG17: Anti-flying</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CG18: Mana acceleration</td>&#10;		</tr>&#10;		<tr>&#10;      <td></td>&#10;			<td>CG19: Destroy artifact/enchantment</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Green has gone from having one spell, which is either a fight spell (two creatures do damage to each other) or a bite spell (your creature deals damage equal to its power to another creature) to having one of each. These spells usually also have some buffing to help your creature kill the opponent's larger rare and mythic rare creatures.

Another side effect of Play Boosters is that we have to be extra-careful with how easy we give green access to other colors in Limited, as it's much easier to just play a "good stuff" deck (a deck with all the best spells in each color) with all the powerful rares and mythic rares. This means we are more likely to do land fetching that gets lands off the top cards of your library rather than fetching one out of your deck. We will also be more careful with lower-rarity mana-acceleration spells to have green cards give you access to green mana rather than any color. This will still help you ramp without making it easier to splash other colors.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>9 Creatures</td>&#10;			<td>8 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>5 Noncreatures</td>&#10;			<td>5 Noncreatures</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Green uncommon creature percentage have gone up slightly from 62% (8 out of 13) to 64% (9 out of 14), making it the only color, along with white, to go up in percentage.

### ![White mana symbol](https://media.wizards.com/2023/images/daily/w.png)![Blue mana symbol](https://media.wizards.com/2023/images/daily/u.png)![Black mana symbol](https://media.wizards.com/2023/images/daily/b.png)![Red mana symbol](https://media.wizards.com/2023/images/daily/r.png)![Green mana symbol](https://media.wizards.com/2023/images/daily/g.png)![Colorless mana symbol](https://media.wizards.com/2023/images/daily/c.png) Multicolor

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>20 Slots (the majority are creatures)</td>&#10;			<td>10 Slots (usually creatures)</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

One of the biggest changes from Draft Boosters to Play Boosters was the decision to increase from one multicolor card per two-color combination to two. One will be an enabler, helping make the archetype work. The other will be a strong payoff for doing what the archetype is telling you to do. In the Draft Booster world, we'd have to choose which of these two functions the gold signpost had. In the Play Booster world, we have space to do both. This is where ten of the 20 new cards in uncommon are going.

### ![Colorless mana symbol](https://media.wizards.com/2023/images/daily/c.png) Artifacts

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Creatures (Play Booster)</strong></td>&#10;			<td><strong>Common Creatures (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA01: Two-mana creature (variance buster)</td>&#10;			<td>CA01: One- or two-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA02: Three-mana creature</td>&#10;			<td>CA02: Three- or four-mana creature</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA03: Four-mana creature</td>&#10;			<td>CA03: Five- or six-mana creature</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

In the Play Booster world, we want the colorless cards to be a bit stronger because they help fill out all the decks. They still shouldn't step on the toes of the colors that do what they do best, but we've upped the power level to make them generically stronger. Because many Play Booster sets will have an upgrade in the land slot some percentage of the time, the artifacts don't have to do quite as much color fixing. "Variance buster" means that the card can help you find lands (through things like scrying and filtering) early in the game if you're short on land. Note it's not good at finding you a particular land. In general, we're being a bit stingier on access to extra colors as we don't want to encourage players splashing the bombs they open.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Common Noncreature (Play Booster)</strong></td>&#10;			<td><strong>Common Noncreature (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA04: Removal</td>&#10;			<td>CA04: Equipment</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA05: Manalith+ ability</td>&#10;			<td>CA05: Land fetching/color fixing</td>&#10;		</tr>&#10;		<tr>&#10;			<td>CA06: Land fixing</td>&#10;			<td>CA06: Mana production</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

The removal is usually expensive but generally useful. We want this as yet another answer to rare and mythic rare bombs. The rest of the common artifacts are helping you with your mana.

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td><strong>Uncommon (Play Booster) </strong></td>&#10;			<td><strong>Uncommon (Draft Booster)</strong></td>&#10;		</tr>&#10;		<tr>&#10;			<td>4 Creatures</td>&#10;			<td>3 Creatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>3 or 4 Noncreatures</td>&#10;			<td>3 Noncreatures</td>&#10;		</tr>&#10;		<tr>&#10;			<td>2 or 3 Lands</td>&#10;      <td></td>&#10;		</tr>&#10;	</tbody>&#10;</table>

Play Boosters have added 20 cards to uncommon. By default, five went to monocolor, ten to multicolor, and five to colorless, most often artifacts or lands. The uncommon creatures, like those at common, want to be generically useful. This is often where we'll put cards that have synergy with large set themes, allowing all colors access to it.

Finally, here are some additional tips for us to keep in mind:

*   We want each two-color draft archetype to have at least six support cards: two monocolor commons and two monocolor uncommons, usually one in each color, and two multicolor cards (as I talked about above).
*   With all the extra rares and mythic rares, the synergy of draft themes is more important than ever. We want to encourage you to play the themes rather than just a smattering of bombs.
*   We want to make sure there's enough graveyard hate such that rare and mythic rare threats aren't continually coming back.
*   Rares and mythic rares want to be more liberal in their use of extra pips of colored mana to make them harder to splash.
*   It's important to make sure some portion of your rares and mythic rares play into draft themes.

## "Go Play!"

That brings us to the end of this year's "Nuts & Bolts" column. I hope it gave you a better insight into how Play Boosters differ from Draft Boosters. As always, if you have any feedback on today's column or on Play Boosters in general, you can email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week as I go back into *Magic*'s past to pick the design innovation from each year of the game's 30-year history.

Until then, may you have fun designing your own boosters.