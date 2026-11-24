---
id: h6p35kjd
kind: article
lang: en
path: /en/articles/makingmagic/2022/12-06-mastering-dominaria-remastered
title: Mastering Dominaria Remastered
published: '2022-12-06'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    lang_detected: en
    capture_id: 223040
    url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    captured_at: '2024-05-18 01:35:27+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    lang_detected: en
    capture_id: 223040
    url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    captured_at: '2024-05-18 01:35:27+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    lang_detected: en
    capture_id: 223040
    url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    captured_at: '2024-05-18 01:35:27+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    lang_detected: en
    capture_id: 223040
    url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
    captured_at: '2024-05-18 01:35:27+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: h6p35kjd
  url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
  page_key: magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:35:27+00'
  capture_id: 223040
  wayback_url: https://web.archive.org/web/20240518013527id_/https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: h6p35kjd
  capture_id: 223040
  url: https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
  wayback_url: https://web.archive.org/web/20240518013527id_/https://magic.wizards.com/en/news/making-magic/mastering-dominaria-remastered
  captured_at: '2024-05-18 01:35:27+00'
  template: contentful
  sha256: f020abd072f1b3dec80586f5c0cc8f18fccdf24251eebea380d1ef913281e7b7
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
  target: https://share.transistor.fm/e/69e48438
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/b7d607ec
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
*(Editor's Note: The* Weatherlight *set was originally omitted from the list of sets that took place on Dominaria and where cards in* Dominaria Remastered *would be from.)*

Welcome to *Dominaria Remastered* preview week. Today, I'm going to talk a little bit about the history of remastered sets. I'll walk you through the design of *Dominaria Remastered* specifically. Finally, I'll show off a preview card from the set. It's not a new card, as the set is all reprints, but it does have cool new art.

## Everything Old Is New Again

Our story begins back in 2014. *Magic Online* was looking for more content, but they were trying to do so without making new cards. Was there a way to make new content out of existing cards? That's when the idea of a remastered set was first thought up. When *Magic* premiered in 1993, Limited play wasn't something that was thought about when building a set. Yes, there was some Limited play (mostly Sealed in the early days), but it was an afterthought, and the sets weren't designed with Limited in mind. This meant that most Limited play was not the greatest play experience.

Take *Legends* as an example. There was one red common creature in *Legends* capable of attacking for any amount of damage (Raging Bull was a 2/2), and the only way to destroy an opponent's non-world enchantment required you to bounce all your enchantments to your hand. *Ice Age* had a different problem where you could open all your boosters and not have enough creatures to fill out your deck. I had numerous *Ice Age* games where I opened my boosters and said, "I don't think I can make a deck capable of dealing 20 damage to my opponent."

Starting with *Mirage*, R&D began thinking about Limited, but it was a steep learning curve and it took many years to figure out much of the staples of modern-day design in regards to Limited play. This meant there were a lot of early sets that didn't play up to modern standards for Limited. Was there a way to use an old card pool but apply modern design techniques to it? That was the idea behind a remastered set. You would take a pool of cards larger than a normal set and craft from them a draft environment. This was done by handpicking which cards you wanted, sometimes changing rarity. The initial idea was that you would pick a single block because you would get three sets all in the same locale using the same mechanics and themes. With three sets to choose from, you could fine-tune your themes and reconfigure the set to have a more modern approach.

The first set to get a remastered treatment was *Tempest*. (*Tempest* is near and dear to my heart as it was the first set I ever led and the one that helped me become a *Magic* designer.) The design team took all three sets from the *Tempest* block (*Tempest*, *Stronghold*, and *Exodus*) and from them crafted a single set. This was released on *Magic Online* in 2015. The response was quite positive. *Magic: The Gathering Arena* would then do remastered versions of both the *Kaladesh* and *Amonkhet* blocks in 2020. (The cards had already been coded for the beta playtest, so it didn't require any new coding.) Finally, in 2021, the first remastered set was made for tabletop with *Time Spiral Remastered*. *Time Spiral*, as a block, was more adventuresome than most and had access to a *lot* of mechanics. (No seriously, there were more mechanics in the block than had preexisted in all of *Magic* before the block.)

Which brings us to Mark Globus. Mark came in fourth in the first *Great Designer Search*. That led to a job in R&D. Mark would eventually become a producer and ended up overseeing several products, including the development of the first Commander product and co-leading the design and development of the first *Modern Horizons*. For regular readers of this column, you might recognize him as part of the Council of Marks that helped to get *Unstable* made. Today's story begins shortly after Mark left Wizards of the Coast after working for many years in R&D to pursue other interests. On his way out, he expressed a desire to do some freelance design work.

Mark was given the following freelance assignment. R&D wanted to do more remastered sets. Which ones did he think were most viable? Mark went through all of *Magic*'s sets and made a list of all the possible remastered sets he could foresee, from most viable to least viable. Some of these sets took existing blocks like the past remastered sets had done, but he also looked at other themes that might allow us to approach a remastered set in different ways. Three potential remastered sets were chosen from that list (I assume from the top of the list) for Mark to work on. *Dominaria Remastered* is the first of the three to see print. Mark was aided in his design by Ben Lundquist, a play designer in Studio X.

## Remaster of the Universe

The further back you go, the rougher the design of the sets are for Limited play. For example, the idea of Limited archetypes tied to color combinations is a product of the last fifteen years, meaning the first half of *Magic* didn't purposefully build it in. Some sets ended up doing something roughly in that vein but not structured in the way we do them now. This makes using a lot of early sets for remastered sets a bit tricky. Mark came up with an interesting solution for this problem. What if we themed a remastered set around the plane of Dominaria? Most early sets took place there, so the set would have access to a far larger card pool than normal.

Here's the list of every set that takes place on (or primarily takes place on) Dominaria, 27 in all (for all the Vorthoses out there, *Tempest*, *Stronghold*, *Exodus*, and *Nemesis* take place on the plane of Rath, which would later be overlaid onto Dominaria, but we chose not to include them here because they didn't take place on Dominaria at the time and the first three had already been used in *Tempest Remastered*):

*   *Alpha*
*   *Antiquities*
*   *Legends*
*   *The Dark*
*   *Fallen Empires*
*   *Ice Age*
*   *Alliances*
*   *Cold Snap*
*   *Mirage*
*   *Visions*
*   *Weatherlight*
*   *Urza's Saga*
*   *Urza's Legacy*
*   *Urza's Destiny*
*   *Invasion*
*   *Planeshift*
*   *Apocalypse*
*   *Prophecy*
*   *Odyssey*
*   *Torment*
*   *Judgement*
*   *Onslaught*
*   *Legions*
*   *Scourge*
*   *Time Spiral*
*   *Planar Chaos*
*   *Future Sight*
*   *Dominaria*

This list is significantly longer than what we use for most remastered sets, but since its themes were going to be more built from scratch rather than just following what the set did originally, it was going to need access to a lot more cards. Here's how Mark and Ben built the set. They started by looking at all the available sets and choosing what cards were possible inclusions. Here are some reasons a card might not make the cut:

**1) It's too weak.**

*Magic* took a while to get a good sense of power level, especially with creatures, so a lot of cards just weren't up to the power level one would expect for a modern Limited experience. This was the category that led to the most cuts.

**2) It's too strong.**

Part of missing the power level also meant occasionally missing high, especially when it comes to Limited. Past *Magic* sets, especially earlier ones, have cards that warped the Limited environment, and those were often removed from consideration. Changing rarities was a possibility, so some strong commons and uncommons could be upshifted in rarity assuming they weren't too swingy.

**3) It's out of color pie.**

We do allow reprints of cards out of color pie provided the printing doesn't introduce them to a new format (meaning there are a bunch in *Dominaria Remastered*), but when you're playing into familiar themes, you must be careful with color-pie breaks, as they can imply things when drafted that aren't true for the rest of the set.

**4) It's too narrow.**

There are a lot of cards, especially in the early days, that have functions that just don't come up in Limited situations (and often not in Constructed situations either). A bunch of cards were cut because they just didn't contribute to the larger Limited environment and weren't relevant to any Constructed formats.

**5) It's too misleading.**

In Draft, R&D has something we call a "trap," where it hints to the drafter that there's a theme to draft that isn't supported in the set. We allow some of that at high rarities if the card is relevant for Constructed formats, but we are extra careful about it at common and uncommon. When picking cards from the past, the design team had to be conscious of cards that deviated too far from the norm of the rest of the cards in that color.

After this pass, they looked at their pool to see if they could find mechanical themes that naturally existed in the different color pairs. *Magic*'s colors have been somewhat mechanically consistent over the years. In addition, they wanted to have multicolor signpost cards at uncommon, so they looked through the multicolor cards to see what themes they encouraged.

Back in the day, we purposefully withheld multicolor from a lot of sets, so the multicolor pool to choose from was smaller than you might assume. They did find themes, but due to the nature of the card pool, they had to be a little lighter in touch than we tend to do in modern sets.

To adjust for this, Mark and Ben found small clusters of cards that worked well together to weave through the set. This meant that sometimes while looking for a certain theme, they might get pulled a little in a different direction by cards that were synergistic with one another. These synergistic clusters are one of the most fun things about the card pool and can create neat deviations in Draft.

The design went through several iterations, using playtests to see which themes were coming through and which were fun to play. When the dust settled, here's where the archetypes ended up:

### White-Blue: Flicker

White and blue have numerous ways to bring a creature onto the battlefield multiple times. They can flicker them (exile and return), they can return them to hand and replay them, they can return them from the graveyard (both to hand and the battlefield), they can copy them, etc. This archetype takes advantage of this by having a lot of enters-the-battlefield effects which it can trigger multiple times. These effects are then used to help you control the game, allowing you to use these same creatures as your win condition.

### Blue-Black: Control

Blue and black have a lot of tools at their disposal (counterspells, discard, bounce, creature kill, stealing, etc.) to gain card advantage and stay ahead of the opponent. This archetype is a bit slower, but it does a good job of giving the player the effects they need to influence the game in their direction, allowing them to slowly eke out a win over time. Blue-black is very good at winning in a way where the opponent doesn't quite understand how they lost.

### Black-Red: Zombies and Goblins

Most of the archetypes are just playing in the mechanical space that the two colors most often use in sets. Black-red does something a little different. It takes a popular creature type theme in black, Zombies, and a popular creature type theme in red, Goblins, and finds ways to mash the two together. It turns out Goblins are good at making lots of Goblins and Zombies have the means to sacrifice creatures for advantage. The archetype also makes use of cards specifically with Zombie and Goblin rewards. Finally, several sets had some mono-black Goblins in them (but no mono-red Zombies, sadly).

### Red-Green: Cycling

It turns out that three different blocks set on Dominaria (the *Urza's Saga*, *Onslaught*, and *Time Spiral* blocks) all made use of the cycling mechanic. (Interestingly, originally designed by Richard Garfield for use in *Tempest*.) That was more than enough to build a Limited theme out of them. The design team chose red and green, as those are the two best ramping colors. When you draw the cycling cards in the early game, cycle away what you don't need to get the cards to help you ramp, and then when you draw them in the late game, cast them.

### Green-White: Threshold

The threshold mechanic (which rewards you for having seven or more cards in your graveyard) only appeared in the *Odyssey* block (*Odyssey*, *Torment*, and *Judgment*), but it works well with green-white's normal go-wide strategy. Some smaller cards will fill up your graveyard, allowing others still on the battlefield to upgrade and overrun your opponent. This was one of the trickiest themes for them to properly balance.

### White-Black: Life Gain and Life Loss

White and black are both good at gaining life (white through life-gaining spells, black through drain effects, and white and black through creatures with lifelink). This archetype gives you a lot of ways to gain life and other ways to spend it. The archetype is slow and controlling, using your life gain to stall while plinking away at the opponent's life to win the game. This type of deck is often referred to as a "bleeder deck."

### Blue-Red: Storm

Storm is a keyword mechanic introduced in *Scourge* and brought back in the *Time Spiral* block. It plays nicely with blue-red's spell theme (blue and red have the highest percentages of noncreature spells). The archetype uses its spells to gain tempo advantage, often using storm as a finisher. Note that all the storm cards are in red.

### Black-Green: The Rock

"The rock" is an archetype that's appeared numerous times throughout *Magic*. It's a midrange archetype that plays a lot of disruption. It keeps putting out creatures that get larger and larger, using its spells to remove obstacles. Its usual finisher is a giant creature.

### Red-White: Auras

As usual, red-white is an aggro archetype that wins by being aggressive. It makes use of Auras to boost creatures, helping them be as offensive as possible. This is a good example of a theme that was possible because it's something that showed up in almost every set, giving the design team a lot of choices.

### Green-Blue: Ramp

Blue-green ramp is another time-tested staple archetype. Blue uses its control elements to support green's mana growth, which leads to large spells of both colors getting played in the late game. Because this theme is used so often, there were a lot of cards that helped enable it as an option.

Once Mark and Ben had the themes for the archetypes, they spent a lot of time picking monocolor cards that worked in multiple themes. This would allow the draft to be dynamic. In the wiki on the set, there's a long list for each color of what cards in other colors combo well with that color's themes.

Beyond the Limited concerns, Mark and Ben took a lot of time figuring out which cards would be popular reprints that would excite players interested in different formats. One of the fun things about looking through the file is seeing a lot of favorite cards from the past.

## Remaster of One's Own *Destiny*

My preview card for today is one I designed in 1997, or around then. I thought I'd show it off and give you a little story about its design.

## Click here to see it

 

![Urza's Incubator](https://media.wizards.com/2022/dmr/en_0e1fbee9f8.png)

![Borderless Urza's Incubator](https://media.wizards.com/2022/dmr/en_3c965a7665.png)

![Retro Frame Urza's Incubator](https://media.wizards.com/2022/dmr/en_a42e3baf53.png)

My preview card is Urza's Incubator. It has brand-new art for this set. This card was designed for *Urza's Destiny*, a set for which I was the entire design team. There weren't a lot of full-time *Magic* R&D designers back then (just six, I believe), and we were making a lot of stuff (okay, not as much as today, but R&D *is* over eight times the size now), so I was asked if I could handle the design for *Urza's Destiny* by myself. I said I could. Other than *Alpha* and *Arabian Nights* (both done before there was an R&D team), I believe *Urza's Destiny* is the only *Magic* set, with new content, created by a design team of one.

I was a big believer in creature-type themes. Note that this was before I'd pushed hard to make creature types a big part of the *Onslaught* block, so it was more of a niche theme at the time. I wanted to make a card that enabled creature-type decks, but I only had one slot for it. My solution was to make something generally useful and then let the player decide which creature type they wanted to care about. I figured this would allow one slot to meet the needs of a whole swath of different creature-type decks. I weighed a bunch of different effects but in the end went with something that made spells cheaper. It didn't work quite as well with a few weenie creature types, but at the time, those were the ones that were already playing best.

This card, originally rare (although to be fair, that was the highest rarity at the time), was moved to mythic rare, as it's more for Constructed than Limited. It's hard to use in Limited, as the set is not designed with a strong creature-type theme (other than the black-red archetype, and even that is a light touch). I'm excited for a new generation of players to get a chance to play it.

* * *

## The Student Becomes the Remaster

That's all the time I have for today. I hope you enjoyed hearing about the creation of *Dominaria Remastered*. As always, I'm eager to hear your feedback about today's column or *Dominaria Remastered*. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I answer reader questions about *The Brothers' War*.

Until then, may you make something new out of something old.

*   [**Episode 988**](https://cdn.transistor.fm/file/transistor/m/shows/21454/6cdd0a0829349d7573fac5665b4511d2.mp3) Designing for an Eternal World
*   [**Episode 987**](https://cdn.transistor.fm/file/transistor/m/shows/21454/31d53556388b21d1b6958701d0adc1c4.mp3) *Unfinity* Rules with Jess Dunks
*   [**Episode 986**](https://cdn.transistor.fm/file/transistor/m/shows/21454/323fe01e7f7e3a30ca6555110ab32680.mp3) Costing Cards