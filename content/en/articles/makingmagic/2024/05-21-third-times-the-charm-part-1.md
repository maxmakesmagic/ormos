---
id: fm1qm4tf
kind: article
lang: en
path: /en/articles/makingmagic/2024/05-21-third-times-the-charm-part-1
title: Third Time's the Charm, Part 1
published: '2024-05-21'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    lang_detected: en
    capture_id: 230993
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    captured_at: '2024-07-13 00:11:19+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    lang_detected: en
    capture_id: 230993
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    captured_at: '2024-07-13 00:11:19+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    lang_detected: en
    capture_id: 230993
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    captured_at: '2024-07-13 00:11:19+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    lang_detected: en
    capture_id: 230993
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
    captured_at: '2024-07-13 00:11:19+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: fm1qm4tf
  url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
  page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
  lang: en
  template: contentful
  captured_at: '2024-07-13 00:11:19+00'
  capture_id: 230993
  wayback_url: https://web.archive.org/web/20240713001119id_/https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: fm1qm4tf
  capture_id: 230993
  url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
  wayback_url: https://web.archive.org/web/20240713001119id_/https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-1
  captured_at: '2024-07-13 00:11:19+00'
  template: contentful
  sha256: b6253ed11cc6f6664d592e01146150d07b7499c42765d68a763611a09e4f807d
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
Welcome to the first week of *Modern Horizons 3* previews. I'm going to share the story of the set's design, introduce you to the Vision Design team, and show off a cool preview card. If that sounds fun, keep reading.

## The *Modern* Family

Before I explain how the set was made, I want to first introduce you to the Vision Design team. (*Modern Horizons 3* didn't have an Exploratory Design team.) Normally, I have the lead vision designer write the bios and introduce their team, but because Erik Lauer has left Wizards, I wrote them this time.

## Click here to meet the *Modern Horizons 3* Vision Design team

**Erik Lauer (Lead)**

Erik Lauer has led more development and Set Design teams than anyone else. (He led or co-led the following sets: *Magic 2010*, *Magic 2011*, *Mirrodin Besieged*, *Innistrad*, *Return to Ravnica*, *Theros*, *Khans of Tarkir*, *Battle for Zendikar*, *Kaladesh*, *Ixalan*, *Dominaria*, *Guilds of Ravnica*, *Throne of Eldraine*, *Zendikar Rising*, *Innistrad: Midnight Hunt*, *Innistrad: Crimson Vow*, *Dominaria United*, *Phyrexia: All Will Be One*, and *The Lost Caverns of Ixalan*.) Erik has led a few Vision Design teams, but always ones that were primarily or all-reprint sets (*Magic 2011*, *Modern Masters 2015*, and *Iconic Masters*). He was interested in spreading his wings and trying to lead a vision design for a set that was primarily new card designs. *Modern Horizons 3* was his first foray into doing this. Next year, you all will get to see his second foray, the return to Tarkir, codenamed "Ultimate." Erik is a huge fan of the game's past and was excited to lead the third *Modern Horizons* set.

**Aaron Forsythe**

Aaron is the vice president of *Magic* design and my boss. He led the set design for the first *Modern Horizons*, and, like Erik, is a huge fan of *Magic*'s history. Aaron doesn't get to work on a lot of design teams in his job, so he's very picky about what design teams he works on. I always refer to *Modern Horizons* sets as "decadent design," as you have access to all the mechanics and a high complexity level to work with. This type of set plays into Aaron's strengths as a designer. (Aaron worked with me on *Time Spiral*.)

**Ethan Fleischer**

Ethan and I were the two people who pitched the idea for *Modern Horizons* during the R&D hackathon where it was created. Ethan led that hackathon design team and the Vision Design teams for *Modern Horizons* and *Modern Horizons 2*, so he was an ideal choice to work on the third incarnation. Ethan loves *Magic* Story and enjoys the freedom *Modern Horizons* allows to access any creative element in the history of the game.

**Michael Majors**

Michael was the set lead for *Modern Horizons 3*, so he wanted to be on the Vision Design team to understand the thought process behind the set's structure and philosophy. Michael is one of the best people in R&D for understanding how best to craft a Limited environment. Michael spent much of vision design absorbing as much as he could to make sure that Set Design was following the previous team's vision.

## A *Modern* Story

Let me start by refreshing everyone on what exactly a *Modern Horizons* set entails. When we made the *Time Spiral* block many years ago, we stumbled into a phenomenon we'd never seen before. The *Time Spiral* block did well in organized play but poorly in sales. Up until that point, sanctioned play and sales were locked together. When one did well, so did the other. The *Time Spiral* block demonstrated that there were groups of players, one of which we dubbed the "invisibles," players who didn't show up in the main market research, were less enfranchised, and were more wary of complexity. They individually spent far less money than the enfranchised players but, in volume, made up a significant portion of the player base. That lesson, in conjunction with some mistakes made during the *Lorwyn* block, led us to create what we called the [New World Order](/en/articles/makingmagic/2011/12-05-new-world-order), a move to simplify premier sets.

Flash forward years later to our first hackathon. An R&D hackathon is where many members of R&D take a week off from their other projects to do some brainstorming on new ideas. The first hackathon involved looking for new supplemental products. Ethan and I had both realized that there was an audience for more complex draft environments. All the people that played in the *Time Spiral* block events enjoyed them. Could we use a supplemental set to deliver something for that audience?

The philosophy we set up in that hackathon was that a *Modern Horizons* set wasn't about making new mechanics but harnessing all the mechanics from the past, making use of the heightened complexity to create designs that we couldn't normally make, including mixing and matching old mechanics and doing tweaks on old cards and themes. This led us to lean heavily into nostalgia, allowing us to make cards that would excite the more enfranchised players. During vision design, we would later decide to make the set legal in Modern.

When Erik was first assigned as the vision lead for *Modern Horizons 3*, he sat down with Aaron and basically questioned everything I'd just established.

**Did the set have to limit itself to existing mechanics?** One of the things a higher-complexity set could allow is the creation of higher-complexity mechanics. There isn't anywhere else we can do them. Should we take advantage of the opportunity here? This was rejected as it would require the rest of the set being simpler to keep the overall complexity at the right spot. That felt to Aaron as if it would conflict too much with player expectation.

**Did the set have to lean into nostalgia?** One could build a design that used old mechanics but felt more like a cohesive new plane rather than a hodgepodge of things from across the Multiverse. Would it make sense to explore new things that we could do with old mechanics and build a world around them? Aaron felt like new planes made more sense for premier sets and that the hodgepodge nature of the creative maximized the designs the team could make. Aaron wanted to stick with nostalgia.

**Did the set have to be legal in Modern?** *Modern Horizons* was added to Modern because we were trying to find a place that the cards could be played in a tournament setting, and Modern had a high enough power level that it could handle the types of designs we wanted to make. Did a new set want to go in a different direction? Maybe be legal in a different format, say Pioneer? Aaron wanted to keep things the same as the first two sets. Also, the product is called *Modern Horizons*, so that alone created the expectation of inclusion in Modern.

In the end, after exploring deviations from the default structure, Erik and Aaron decided to keep the status quo. *Modern Horizons 2* being the bestselling set at the time (*The Lord of the Rings: Tales of Middle-earth™* has since surpassed it) also factored into that decision. If it ain't broke …

Erik's first stab at creating cards for the file was to take every mechanic ever made and make a new card for it. Not all the mechanics would make it to print, but this exercise helped Erik understand the potential of the different mechanics. It would also help Erik reorient himself with the design space for each one.

In conjunction with this, Erik looked at what decks were being played in Modern, using data from various sources, including *Magic Online*. His focus was not on the top-tier decks but the ones a tier or two lower. What decks were close to being top tier? Rather than make the best decks better, Erik hoped the set could boost secondary and tertiary themes. The goal was to make Modern a more fun format, not just add power creep.

The result of the exploration led Erik to realize that there was a mechanical tool (double-faced cards) and other mechanical themes (energy, colorless, and Eldrazi) that seemed ripe to play a larger role in the set.

## Double-Faced Cards

Double-faced cards (DFCs) first appeared in another trading card game Wizards makes called *Duel Masters*. We designed *Duel Masters* many years ago as a means to introduce a game into the Japanese market (trading card games are huge there) that we could eventually bring to the United States. We only expected the game to last three to five years, but *Duel Masters* celebrated its twentieth anniversary in 2022. We twice tried to bring the game to the United States, but neither time with much success.

Double-faced cards in *Duel Masters* don't start in your deck but rather in a place called the uber-dimensional zone. Up to eight cards can start in that zone. Those cards can be cast from that zone under certain circumstances. Many of the cards you can cast from either side, each having its own mana cost. If you cast the front side, you often can essentially transform under various conditions. *Duel Masters* has done a lot of different things with double-faced cards over the years, including a mechanic that's similar to meld.

When we were working on original *Innistrad* design (back then, design was broken into design and development), I had the team brainstorm ideas for representing the Werewolves. Up to that time, there were only three, none of which were either powerful or flavorfully evocative, so I felt mechanically capturing Werewolves was key to the set's success. Tom LaPille, a member of the design team, had recently worked on *Duel Masters*, so he was aware of the double-faced cards. We had talked about wanting to represent two states, Human and Werewolf, so Tom pitched the idea to use a double-faced card to give each state its own card face.

Deviating a bit from how *Duel Masters* used them, our initial design for DFCs played the front face first that could then transform into the back face. On some cards, such as the Werewolves, you could also transform back. We would later refer to this incarnation of DFCs as transforming double-faced cards (TDFCs). To help unify the Werewolves, we came up with a system where all of them transformed from Human to Werewolf using the same condition (no spell getting played—it's night and things are quieter) and Werewolf to Human using a different condition (two spells played on the same turn by the same player—it's day and there's more activity).

I'll admit I was a bit skeptical at first, but in early design we always try things because sometimes, as was the case with DFCs, what seems dubious ends up playing well. The design team soon decided we wanted to use double-faced cards, but there was a journey getting the rest of R&D aboard. First, we had to make sure we could print them. *Duel Masters* had, but *Magic* exists on a much larger scope, so we had to make sure we could do them in the volume *Magic* would need.

The next big thing to handle was how they would work. They had two faces, so could they even go in a deck? *Duel Masters* had opted not to have them in the deck, having them exist in a different zone. Our initial solution was to have a single-faced card that went into your deck that when you cast it, you went and got the double-faced permanent. While not exactly a token, the double-faced card would act similarly in some ways. That plan got foiled when we found out the printers could only guarantee the two cards showed up in boosters together 90% of the time, and certain printers at the time couldn't even do it. We then got data that said most players used sleeves, so we just put the double-faced cards in the deck, and then made checklist cards for the people not playing in (opaque) sleeves.

The biggest hurdle, interestingly, was internal pushback against doing double-faced cards at all. There was a contingent of R&D who strongly felt that not having a *Magic* back was a step too far. Luckily, I got the support of upper R&D management, and double-faced cards made it all the way to print. Interestingly, because there was so much internal concern, we chose to use them only in *Innistrad* and *Dark Ascension*, excluding them from *Avacyn Restored*, the last set in the *Innistrad* block. While it mostly had new mechanics, we purposely carried something over based on feedback from the *Zendikar* block where we didn't. One of the largest complaints about *Avacyn Restored* was that it didn't have any DFCs.

Mayor of Avabruck Bloodline Keeper 

We debuted them at a party connected to PAX West (then just PAX). We opened the curtains to show a giant card. We then had the card rotate to show that it transformed, but it was such a bold idea that people didn't get it. They thought we were just showing a second, separate card. I literally brought a copy of the card in my pocket to show people and explain. ("See. There are cards on both faces.") DFCs create a lot of controversy when we first announced them, but once the product came out, they were quite popular. So much so, that we looked for other places to use them.

Jace, Vryn's Prodigy Liliana, Heretical Healer 

The first opportunity was *Magic Origins*. We were telling the origin stories of the first five members of the Gatewatch (Gideon, Jace, Liliana, Chandra, and Nissa), and the design team came up with a cool idea, showing legendary creature versions of the characters that turned into planeswalkers, representing the moment of their first spark. Technically, these double-faced cards don't transform but are exiled and returned to play as the back face. This would be the first time a set used DFCs in a limited capacity and only at a higher rarity, meaning most boosters of the product didn't come with a DFC. The original *Innistrad* block, in comparison, had a DFC slot, so every booster had one.

0237a\_MTGMH3\_MainDFC: Ajani, Nacatl Pariah 

The DFC planeswalkers were so popular that we've gotten constant requests ever since then to do them again. Aaron, being aware of this player desire, asked Erik to put in a new cycle of planeswalker DFCs into *Modern Horizons 3*.

Archangel Avacyn Gisela, the Broken Blade 

Bruna, the Fading Light Brisela, Voice of Nightmares 

DFCs would return in the *Shadows over Innistrad* block, again using TDFCs. *Eldritch Moon* would introduce meld, which made use of double-faced cards to accomplish something I had first done in *Unglued* with a card called B.F.M., where one permanent consisted of the combination of two cards. DFC technology proved to be key in making such a thing viable in the normal rules.

Growing Rites of Itlimoc Nicol Bolas, the Ravager 

DFCs' next use would come with the *Ixalan* block. The two sets had a theme of exploration, and we liked cards that transformed into powerful lands. It was at this point we realized that DFCs wanted to be deciduous, meaning it should be a tool available to any set that wanted it. DFCs do come with several costs in production and logistics, so we want to be careful not to use them too much, but they had so much design space and were so popular that there was a big draw to use them. *Core Set 2019* would push this boundary by having a single DFC in it, Nicol Bolas as a DFC planeswalker.

*Zendikar Rising* would introduce a whole new way to use DFCs. Aware of how *Duel Masters* used DFCs, we saw that there was a different mechanical model. Rather than letting you cast one side of the card and transform it, there was a different version where you had the ability to cast or play either side, but without the ability to transform it. We called this version modal double-faced cards (MDFCs). These are basically split cards, but ones that could have permanents and allowed for more rules text and two pieces of artwork.

Bala Ged Recovery Toralf, God of Fury Rowan, Scholar of Sparks 

There was so much design space here that I decided to have each of the three main sets of the year have its own version of them. *Zendikar Rising* had MDFCs with lands on the back fitting into the land theme of Zendikar sets. *Kaldheim* used MDFCs to represent the gods of the plane. Each card was a legendary creature with subtype God on the front and a different related permanent on the back. *Strixhaven: School of Mages* had a few executions. It had some permanents with a permanent on one side and an instant or sorcery on the back to fit into the set's "instants and sorceries matter" theme. It also had cards representing the two deans of each school, one on each side, and an MDFC representing Rowan and Will, who were attending the school, each a planeswalker card on their own face.

The MDFC lands were the biggest hit, and Erik's personal favorite designs, so when he was making cards with every mechanic, he made some land MDFC designs. *Modern Horizons* and *Modern Horizons 2* didn't have access to DFCs, so this ended up being something *Modern Horizons 3* could do for the first time. Other than the cycle of DFC planeswalkers, the rest of the DFC designs are all land MDFCs, including my preview card for today:

## Click here to see Disciple of Freyalise // Garden of Freyalise

0250a\_MTGMH3\_MainDFC: Disciple of Freyalise 

Poppet Stitcher Fable of the Mirror-Breaker Starscream, Power Hungry 

*Innistrad: Midnight Hunt* and *Innistrad: Crimson Vow* made use of TDFCs, as is the custom of sets visiting Innistrad. *Kamigawa: Neon Dynasty* combined Sagas with DFCs so that each story ended with you getting a related creature. The Transformers cards that came inside *The Brothers' War* boosters were DFCs that made use of a new mechanic called More Than Meets the Eye, which for the first time combined TDFC technology with MDFC technology. You could cast either side, and they had the means to transform both directions on the battlefield to capture the flavor of Transformers.

Invasion of Ikoria Tithing Blade 0189a\_MTGLCI\_Main: Huatli, Poet of Unity 

*March of the Machine*, in addition to using TDFCs to represent the Phyrexianization of creatures in the war, introduced a new card type, battles with a subtype called Siege that were all double faced, and incubate, a new mechanic that generated a DFC token, the first of its kind. *The Lost Caverns of Ixalan* would bring back TDFCs that turned into lands and introduced a new mechanic called craft that made use of TDFCs to show using one material to create something new. It also had the first creature, Huatli, Poet of Unity, that transformed into a Saga.

I'm happy that *Modern Horizons 3* has been able to use DFCs (it's not something most supplemental sets have access to), and I hope it will bring some new twists to the *Modern Horizons* formula.

That's all the time I have for today. Next week, I'll get into the energy, colorless, and Eldrazi themes and talk through the ten draft archetypes. As always, I'm eager for any feedback on today's column or on *Modern Horizons 3*. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [*Blogatog*](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two.

Until then, may you use both sides of your *Magic* cards (when able).