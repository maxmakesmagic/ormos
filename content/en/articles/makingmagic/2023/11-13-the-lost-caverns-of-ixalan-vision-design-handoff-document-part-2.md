---
id: e1t14te1
kind: article
lang: en
path: /en/articles/makingmagic/2023/11-13-the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
title: The Lost Caverns of Ixalan Vision Design Handoff Document, Part 2
published: '2023-11-13'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 230896
    url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:06:14+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 230896
    url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:06:14+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 230896
    url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:06:14+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 230896
    url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:06:14+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: e1t14te1
  url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
  page_key: magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:06:14+00'
  capture_id: 230896
  wayback_url: https://web.archive.org/web/20240518010614id_/https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: e1t14te1
  capture_id: 230896
  url: https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
  wayback_url: https://web.archive.org/web/20240518010614id_/https://magic.wizards.com/en/news/making-magic/the-lost-caverns-of-ixalan-vision-design-handoff-document-part-2
  captured_at: '2024-05-18 01:06:14+00'
  template: contentful
  sha256: 3de075e96ebd3b2453d06fb1e04573b80cf20c2789bae06eaf876eceb863db20
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
[Last week](/en/articles/makingmagic/2023/11-06-the-lost-caverns-of-ixalan-vision-design-handoff-document-part-1), I began showing you the vision design handoff document for *The Lost Caverns of Ixalan*. It was long enough for two articles, so today's is part two. As with last week, most of what you'll be reading is the actual document I handed off at the end of vision design. Anything in a blue box is my commentary explaining things in the document. With that said, let's get back to it.

With the above tools at hand, the design cares about color in two different zones—the battlefield and the graveyard. As the latter ties directly into our resource acquisition, I'll start there.

## Caring About Color in the Graveyard

We wanted the set to have an element of resource acquisition, and we needed it to tie into the flavor of the underground. Tapping into the source material, we liked the idea of mining gems. These are things found underground that have an inherent sense of value to them. After much playtesting, we ended up with five precious gems, one for each color—pearl, sapphire, jet, ruby, and emerald. We think this will be a nice nod for the enfranchised players, and the gems do a good job of communicating their color.

One of the dangers of early design is that you can get really stuck on a cool idea. We wanted to do crafting. We liked tying crafting to precious gems, as it matches the trope space. *Magic* has five famous precious gems as part of the most powerful cycles in the game, the Moxen. This just seemed like an amazing moment of everything falling together, of doing our take on a famous trope. There are a bunch of reasons this mechanic suite didn't work out (and I talk about that later), and one of those reasons might have been our desire to match the Moxen. It encouraged us to make the set more complex than we should have.

How does one get gems? Well, the main way to do that is through mining, a brand-new mechanic:

### Mining and Crafting

**Pearlescent Healer**  
 3W  
 Creature — Human Cleric  
 3/4  
 \<pearl>: Pearlescent Healer has lifelink.  
 Activate this ability only as a sorcery.  
 2, T: Mine. Activate this ability only as a sorcery. *(Exile a card from your graveyard to mine the associated gem.)*

**Mine-a-lith**  
 2G  
 Artifact  
 \<emerald>: Whenever Mine-a-lith becomes tapped, you gain 1 life.  
 T: Add one mana of any color.  
 2,T: Mine. Activate only as a sorcery. *(Exile a card from your graveyard to mine the associated gem.)*

**Gold Elemental**  
 3W  
 Creature — Elemental  
 3/3  
 \<sapphire>: Gold Elemental has flying.  
 \<emerald>: Gold Elemental has vigilance.  
 2,T: Mine. Activate only as a sorcery. *(Exile a card from your graveyard to mine the associated gem.)*

**Monstrous Mole**  
 5R  
 Creature — Mole  
 5/5  
 Trample  
 \<jet>\<ruby>\<emerald>: Monstrous Mole has "whenever this creature deals combat damage to another player, destroy target artifact, creature or land."  
 2,T: Mine. Activate only as a sorcery. *(Exile a card from your graveyard to mine the associated gem.)*

Another idea I latched onto early and held tightly all the way through vision design was the idea that the recipes on the cards would make use of the symbols of the gems from the Moxen. An important part of vision design is creating cool elements, and I thought visual recipes went a long way in making this feel both flavorful and novel.

Mining is an ability that goes on artifacts and creatures, all of which have a crafting upgrade (that I'll talk about in a moment). Mining gives the card the ability to tap and exile a card from your graveyard to generate a gem that matches one of the colors of the card. For example, I could exile a blue card to mine a sapphire, or I could exile a red and green card to mine either a ruby or an emerald. Mining a card only gets you one gem, but you get a choice if it is more than one color. Colorless cards can't be mined. The gems are all counters, which go to you, the player. The current plan is for the set to have punch-out counter cards like *Amonkhet* and *Ikoria* that would have the gems on them to help keep track of the board state (and look really cool).

With these documents, I often see problems in looking back that I couldn't see at the time of writing. Having the gems be counters rather than just direct costs (a ruby means exile a red card from a graveyard) made this ecosystem much more complex than needed. As Play Design liked to point out, we made energy but with five variables. I do believe finding a way to visually show off the gems would have made the overall feel of the set cooler, but I would have done that as the cost on the cards and not with counters (hindsight 20/20).

Each card with the mining ability also has a crafting cost. The crafting cost is made up of colored gems (and maybe generic mana, if needed, but for right now they are just gems) and functions much like monstrosity in that it's a one-time permanent upgrade. When you pay the crafting cost, you put the gem counters on the creature to visually signify it's been upgraded. Note, as seen above, we do have some designs where there are two different crafting costs for different upgrades. The costs use different gems, so you can tell which cost has been paid by looking at the gems on the creature. The intent is that the gem costs would have colored gem symbols. The current thought is that the abilities granted by off-color gems would still be something the color could bend to and wouldn't cause any color-pie breaks.

To answer a question that I'm sure some of you are asking, I was trying hard not to make use of double-faced cards because I was using counters. The slot where you would put an aide to help with DFCs fights with the slot where you would put a punch-out card. Both also fight for the same "extra stuff" part of the set's budget. Finally, Ixalan was not yet part of the set, so there was less pressure to use DFCs. Whenever we do two-state cards, Set Design can always opt into them becoming DFCs. The switch to Ixalan as a setting and the desire to have TDFCs with lands on the back made the choice to include TDFC crafting cards more straightforward.

At common, all the crafting cards only have crafting gem costs of their own color (at a variety of costs in number), but at higher rarities, we will have cards with colored gems not found in their mana cost. The assumption is that we would talk with the Commander folks about colored gems adding color identity. A mono-green creature with a gem cost of jet-emerald-emerald, for example, would be considered black and green (as the card can't upgrade without black cards in your deck).

Again, I walked through some execution of our mechanic so that Set Design would understand how we want to use it. You'll note that I'm aware we're stepping in new space as far as color identity is concerned, so I'm noting we'll have to talk with the Commander Rules Committee. (For those unaware, Wizards does not set the rules for Commander.)

**Strike Ore**  
 1R  
 Sorcery  
 Strike Ore deals 2 damage to any target. You get a ruby.

The Vision Design team did create some cards that could produce colored gems as a rider, but Set Design can figure out whether those are necessary.

Once you choose to have the mechanic represented with counters, it becomes a resource you can use on other cards. Again, in retrospect, I wouldn't have used counters.

### Crafting Table

**Crafting Table**  
 Token Artifact  
 2,\<gem>,T: Create a 1/1 Gnome artifact creature of the color of the sacrificed gem.  
 \<gem>\<gem>\<gem>, T: Search your library for an artifact of the color of one of the sacrificed gems, reveal it, put it into your hand, then shuffle.  
 2,T: Mine *(Exile a card from your graveyard to mine the associated gem.)*  
 Activate each ability only as a sorcery.

Some creatures with a crafting cost at a higher rarity (currently, it's legendary creatures) enter with an external game piece (like a dungeon or The Monarch helper card), a token artifact called the Crafting Table. The Crafting Table has three functions: One, it lets you mine gems. Two, it allows you to turn a gem into a 1/1 Gnome artifact creature of the color of the gem spent. Three, it allows you to turn three colored gems into an artifact in your deck of the colors of one or more of the gems spent. All three abilities can only be used as a sorcery. The reason the Crafting Table mostly just shows up at higher rarity is because it's designed to help out the mechanic in Constructed (especially Commander) without causing too much fallout in Limited.

We really wanted a crafting table for resonance. We went back and forth on whether it was supposed to be a card or a token. A lot of commentary on this document is self-reflection, and I wince a bit seeing how much complexity I put into the set. I'm going to talk a bit about what went wrong below, but the excess complexity didn't help.

## Caring About Color on the Battlefield

Because we're using the various tools like twobrid and off-color creature tokens, we realized that we can also care about how many different colors you have on the battlefield. As I mentioned above, we were interested in pushing "color matters" in a different direction, so all the color-matters mechanics only cared if you had one permanent of a particular color rather than rewarding you for having a bunch of the same color. This philosophy pushed us toward several designs, including a domain-like mechanic.

### Illuminate

**Ornery Salamander**  
 2(2/r)  
 Creature — Salamander  
 3/2  
 Illuminated — When Ornery Salamander dies, it deals X damage to each opponent, where X is the number of colors among permanents you control.

**Forked Rainbow**  
 U  
 Instant  
 *Illuminated* — Copy target instant or sorcery spell whose mana value is less than or equal to the number of colors among permanents you control. You may choose new targets for the copy.

Illuminate is an ability word that counts how many different permanents you have on the battlefield to set an ability, which can be scaled. It is possible to create some illuminate cards with a threshold ("if you control three or more colors") rather than a scale if such a thing is needed. Illuminate can show up on any kind of card, and we've used it a bit on spells as mining leans toward permanents.

Illuminate is a cool mechanic, and when we one day do a set with a "color matters" theme (it will eventually happen, as *Magic* is a hungry monster), I'm sure we will take a look at using illuminate. Domain (caring about how many different basic land types you have) is a lot of fun, and illuminate seems to play in similar territory, but in a way that requires less-risky mana bases. I do think the vision design came up with a lot of cool ideas, just many that didn't make sense in this set. Having done this for over 28 years, I know these cool ideas will eventually find a home.

### Threshold-One Effects

**Ancient Idol**  
 4  
 Artifact Creature — Golem  
 4/4  
 If you control a white permanent, Ancient Idol has vigilance. The same is true for blue and flying, black and lifelink, red and haste, and green and trample.

**Cavern Brawl**  
 G  
 Sorcery  
 Target creature you control gains lifelink until end of turn if it's white. Then it fights target creature you don't control.

Often when we make a "color matters" set, we will design cards that grant abilities to cards of a particular color ("all blue creatures you control gain flying"). With "Offroading," we've designed all these types of cards to act as "threshold one," meaning you only need one card of the color to get the benefit. ("If you control a blue permanent, all creatures you control gain flying.") This means that these types of cards need to be on spells or reference another color if used on a permanent.

This was another important discovery as we were playing in "color matters" space. Scaling color effects or effects that affected all cards of one color encouraged you to lessen the number of colors you played as you got giant effects for having a lot of cards of the same color, but "threshold one" effects (i.e., the effect turns on if you have one card of the color) encouraged the kind of splashing we wanted.

## One Final Mechanical Tool

Another aspect that we wanted to incorporate into this set was the idea of digging. One of the popular tropes of an underground world is the sense of discovery, that the world has various treasures that you're trying to find, and digging is the means of that discovery. We wanted a mechanic that let you look for things without you already knowing the outcome of what you're looking for. That led us to the library. While the graveyard has a lot of great flavor related to the underground, it lacks any hidden information. What we ended up with is a mechanic that provides card flow but also combines with mining such that you can find certain gems.

### Dig

**Watchful Guardian**  
 5W  
 Creature Giant  
 3/6  
 Vigilance  
 Dig 1W *(1W, Discard this card: Surveil 1, then draw a card.)*

**Earthly Lullaby**  
 3UU  
 Sorcery  
 Return up to two target creatures to their owner's hands.  
 Dig 1U *(1U, Discard this card: Surveil 1, then draw a card.)*

Dig is a combination of cycling and surveil. You can pay mana to discard the card in your hand with dig, and that lets you look at the top card of your library, choose whether to put it in the graveyard, and then draw a card. Dig has all the utility of cycling with the bonus of having two different ways to get a certain colored card into your graveyard to mine it. We think this mechanic will add needed flavor as well as card flow and synergy to the set.

The flavor desire that led to dig would be met in the final set with discover. Once we decided to make the setting Ixalan, that encouraged us to add explore, and dig and explore are too close to one another. I did think dig was a nice smoothing mechanic and would work well in a set with a "graveyard as resource" theme.

## In Conclusion

I'm quite proud of all the work the Exploratory and Vision Design teams did (along with the Creative team) to craft a set around the underground. I think we found a way to make an evocative world that captures the essence of what makes other games in this genre fun. As always, I can't wait to see what the Set Design team is able to do with the vision we laid out. If you have any questions about anything in (or not in) this document, please come talk to me.

Thanks,

Mark Rosewater

Before we wrap up, it's time for a little self-reflection. Why is the finished product so far away from the vision design handoff? There are two main answers:

**Reason #1: The switch to Ixalan**

Once we chose to change the setting, the set had an obligation to feel Ixalan-ish. Yes, this was a backdrop set and we weren't repeating the core mechanical heart of original *Ixalan* block, but there was still a need for the set to feel like it shared the same plane. This would push for some mechanical inclusions like explore, transforming double-faced cards (TDFCs), and Dinosaur typal. These inclusions would have some ripple effects.

Sometimes it pushed out things because they were too close (we didn't want dig and explore in the same set), other times it forced consolidation (if we have TDFCs to replicate the transformation into legendary lands, the crafting mechanic might as well also use it), and sometimes it caused conflicts. *Ixalan* block was best known for typal themes. Even though we were reducing the number of them, we still wanted Dinosaurs for a draft archetype and the other three at higher rarities for larger Constructed formats. Caring about creature types fights a bit with color mattering structurally as they are similar but on a different vector. It would be odd, for example, to have one card grant Dinosaurs a bonus and another grant red creatures a bonus. It makes tracking board states complicated.

The biggest issue was one of design space. There's just so much room for themes. The primary theme had to be underground, as it was the core of what we were building. Vision Design chose to make color mattering its secondary theme, but once the plane became Ixalan, feeling like Ixalan took over as the secondary theme. There wasn't room for both, and color mattering got squeezed out.

**Reason #2: We were a little too bold without a strong enough fallback plan.**

I led this set because I had cool idea for it. As such, my design team and I took a big swing. That's the kind of thing vision design *should* be doing. But we made a couple mistakes (and by "we," I really mean "I," as I led the team and this was my vision).

**Mistake #1:** **The structure was too complicated.**

Having five different counters (or five different artifact tokens before that) was too much. It required too much processing and would be near impossible for the Play Design team to balance. The color-matters theme, while probably fine in a vacuum, was a lot when added to this system. We don't have extensive experience working with twobrid mana, for example, so that would have required significant set design and play design time. The core ideas we were playing with were good (and the final version of crafting does follow the basic shell of what we were doing), but it was too much.

**Mistake #2: Our components were too interconnected.**

When building a file in set design, if you find you've overshot mechanically, the first step is to remove a portion of the design. We intertwined most of our components in a way that made that difficult. You may see a recurring theme: we built the set such that we made it harder for people downstream of us to be able to adapt it.

**Mistake #3: We didn't build a fallback plan.**

Of the three mistakes, this is the biggest one. It's fine for vision design to be adventurous. In fact, I ask all my Vision Design teams to think big. But our most important responsibility is to make sure we're enabling the teams after us to do their job. Part of being bold is having a plan for what happens if the bold thing doesn't work out. Normally, I do this. Behind the scenes, I was just juggling a little more than I should have and dropped the ball here. I like sharing behind-the-scenes processes to give you an idea of what happens as we make sets. Here's me messing up. As a result of this vision design, we did change things to make the fallback plan a deliverable, meaning the Vision Design teams are now officially on the hook to have one.

I want to applaud Erik Lauer, Jules Robins, and their Set Design team for figuring out how to make this set work, both in adapting Ixalan and capturing our goals in a way that mechanically worked. I hope this vision design handoff helped illuminate how things don't always go to plan and how even after making sets for 30 years, there are hiccups.

## Going Down

That finishes our look at the document. I hope you've enjoyed this peek at *The Lost Caverns of Ixalan* vision design handoff document over these last two weeks. As always, if you have any comments on the document, my articles, or *The Lost Caverns of Ixalan* itself, you can email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I start my card-by-card design stories from *The Lost Caverns of Ixalan*.

Until then, may you have fun exploring *The Lost Caverns of Ixalan*.