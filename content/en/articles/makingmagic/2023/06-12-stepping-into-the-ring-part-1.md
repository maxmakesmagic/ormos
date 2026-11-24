---
id: vhh55y4c
kind: article
lang: en
path: /en/articles/makingmagic/2023/06-12-stepping-into-the-ring-part-1
title: Stepping Into the Ring, Part 1
published: '2023-06-12'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    lang_detected: en
    capture_id: 230472
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    captured_at: '2024-05-18 01:15:25+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    lang_detected: en
    capture_id: 230472
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    captured_at: '2024-05-18 01:15:25+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    lang_detected: en
    capture_id: 230472
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    captured_at: '2024-05-18 01:15:25+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    lang_detected: en
    capture_id: 230472
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
    captured_at: '2024-05-18 01:15:25+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: vhh55y4c
  url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
  page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:15:25+00'
  capture_id: 230472
  wayback_url: https://web.archive.org/web/20240518011525id_/https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vhh55y4c
  capture_id: 230472
  url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
  wayback_url: https://web.archive.org/web/20240518011525id_/https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-1
  captured_at: '2024-05-18 01:15:25+00'
  template: contentful
  sha256: 87abd4b3ea7ae58dab127923a1ac499f70e060c375efa80664121f5dbefb042e
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
Over the last two weeks ([Part 1](/en/articles/makingmagic/2023/05-30-crafting-the-ring-part-1) and [Part 2](/en/articles/makingmagic/2023/06-05-crafting-the-ring-part-2)), I talked about the vision design and set design of [*The Lord of the Rings: Tales of Middle-earth™*](https://web.archive.org/web/20230612000000/https://magic.wizards.com/en/products/the-lord-of-the-rings-tales-of-middle-earth) (LTR). Over the next two weeks, I'll be telling some design stories for cards from the set. Let's get to it!

**Aragorn, Company Leader** 

![](https://media.wizards.com/2023/ltr/en_43f565416f.png)

*Amonkhet* introduced punch-out cards that could fit into a booster and had elements, often counters, that players could punch out and use in gameplay. When designing *Amonkhet*, the idea of keyword counters came up for the first time, but the set had enough going on that they decided not to pursue it. I should note that the Chimeras from *Visions* were technically the first cards to put counters on a creature and grant them a keyword ability, although not as cleanly as keyword counters. (If we had the technology at the time, I'm sure they would have used keyword counters.) Then about a year later, we did a Hackathon looking at potential future design space, and I led a small team to design a whole bunch of cards using keyword counters to test them out. They played well.

I ended up using them in the vision design for *Ikoria: Lair of Behemoths*, originally as a core tool to how mutate worked. Mutate would change, but Dave Humpherys, who had been the set lead for *Amonkhet* and *Ikoria*, was a huge fan of them and kept them in. *Ikoria* had a punch-out card to help players track the changes. The set introduced nine keyword counters (deathtouch, first strike, flying, hexproof, lifelink, menace, reach, trample, and vigilance). *Commander (2020 Edition)*, which was released with *Ikoria*, included two more (double strike and indestructible). This covered all the evergreen keywords at the time except three: defender, flash, and haste. The first was a downside mechanic, and the other two don't work particularly well as counters. Ward, which was added late, hasn't gotten a keyword counter yet. [A previewed plane card](/en/articles/announcements/2023/05-05-allons-y-on-october-13-celebrate-60-years-of-doctor-whotm-through-magic) in the upcoming *Magic: The Gathering® – Doctor Who™* Commander decks uses a shadow keyword counter, the first nonevergreen keyword counter.

During *Kaldheim*, Dave Humpherys decided to use them in the set on three cards—one uncommon and two rares. The set didn't have punch-out cards, but Dave felt that at a low as-fan it would be acceptable. This prompted us to move keyword counters to deciduous status, meaning any set had access to them, but the general rule was that the set needed to be at a low as-fan if there aren't punch-out cards. Dave would use them yet again in *Kamigawa: Neon Dynasty*.

The more we use keyword counters, the more we push the boundaries of how we can use them. Aragorn, Company Leader is a good example. While we've made cards before that trigger to put a counter on your creature, and often a choice of numerous counters, we haven't combined them with a separate "counters matter" ability. In this case, it allows you to duplicate a counter put on Aragorn on another creature. Note that this ability isn't limited to just the keyword counters named on the card, allowing it to play with other cards in the set.

Aragorn, Company Leader is one of just four characters (Aragorn, Faramir, Gandalf, and Galadriel) that rewards you for choosing another creature for being your Ring-bearer. Aragorn's effect is the granting of one of four keyword counters. The second ability was chosen to make the card a fun build-around while having synergy with the first ability.

Keyword counters have proven to be useful and flavorful, and I can see us continuing to evolve how we use them. I assume we'll have sets with a punch-out card occasionally, where we can do them in high number and even possibly include them in a mechanic. Outside of that, expect to see the occasional design, mostly at rare and mythic rare, and probably in most sets for which Dave Humpherys is the set design lead.

**Bill Ferny, Bree Swindler** 

![](https://media.wizards.com/2023/ltr/en_6bb7a18ad8.png)

An important part of making a *Universes Beyond* set is designing cards for all the main characters. For many players, these are the cards they're most interested to see. But for die-hard fans, sometimes the most important cards are the deep cuts, the cards that reference minor characters, ones that only they might recognize. Which brings us to the design of Bill Ferny (and Bill the Pony, coming next). If you remember the knowledge pyramid from [my first LTR preview article](/en/articles/makingmagic/2023/05-30-crafting-the-ring-part-1), Bill Ferny and Bill the Pony were on the top of the pyramid (meaning only the most dedicated fans would likely know them).

Bill Ferny is a scoundrel. He's an agent of Saruman and Sauron and is mostly only out for himself. At one point in the story, he sells a pony named Bill to Aragorn. He, of course, charges way too much. We knew from the very beginning that we wanted both characters to have cards in the set. Bill Ferny needed to be in blue or black. Blue is the color more in need of creatures, so Bill Ferny became blue.

The early attempts at his design were mostly different ways to top-down design a scoundrel.

Raid — Whenever CARDNAME or another creature you control enters the battlefield, if you attacked this turn, draw a card, then discard a card.

Whenever a creature enters the battlefield under your control, target player mills one card. If that creature is legendary, they mill two cards instead.

Whenever CARDNAME or another Human enters the battlefield under your control, tap or untap target permanent.

At some point, we decided that it was important to involve treasure, because greed drives Bill Ferny the most.

When CARDNAME enters the battlefield, choose a creature you control to become your Ring-bearer. (It's legendary and has ward {2}.) Whenever one or more legendary creatures become blocked, create a Treasure token. (It's an artifact with "{T}, Sacrifice this artifact: Add one mana of any color.")

Whenever one or more legendary creatures you control deal combat damage to a player, create a Treasure token. (It's an artifact with "{T}, Sacrifice this artifact: Add one mana of any color.")

When CARDNAME enters the battlefield, if you cast it, create a Treasure token for each Human you control. (They're artifacts with "{T}, Sacrifice this artifact: Add one mana of any color.")

Meanwhile, the team was also making a Bill the Pony card (which I'll get to in a second), and it dawned on them that Bill Ferny had to somehow reference Horses.

When CARDNAME enters the battlefield, if you cast it, create a Treasure token for each Horse and Human you control. (They're artifacts with "{T}, Sacrifice this artifact: Add one mana of any color.")

Whenever you cast your second spell each turn, target player mills two cards. Whenever a player mills one or more creature cards, create a Treasure token. If one of those cards was a Horse, create three Treasure tokens instead. (It's an artifact with "{oT}, Sacrifice this artifact: Add one mana of any color.")

Whenever CARDNAME deals combat damage to a player, they mill that many cards. Whenever an opponent mills one or more creature cards, create a Treasure token. If they milled one or more Horse cards, create three Treasure tokens instead. (They're artifacts with "{oT}, Sacrifice this artifact: Add one mana of any color.")

As the design evolved, the Set Design team decided it wasn't enough to just reference Horses. Bill Ferny had to sell Horses.

{o3oU}, {oT}: Target opponent gains control of target non-Treasure permanent you control. Whenever an opponent gains control of a permanent you own, draw a card and create a Treasure token. If that permanent was a Horse, instead draw three cards and create three Treasure tokens. (They're artifacts with "{oT}, Sacrifice this artifact: Add one mana of any color.")

Whenever another permanent enters the battlefield under your control, you may have target opponent gain control of it for as long as you control CARDNAME. If you do, create a Treasure token. If that permanent was a Horse, instead create three Treasure tokens. (They're artifacts with "{oT}, Sacrifice this artifact: Add one mana of any color.")

Whenever CARDNAME deals combat damage to a player, you may choose another permanent you control. If you do, that player gains control of that permanent until the end of your next turn and you create a Treasure token. If a Horse was chosen this way, create three Treasure tokens instead of one. (They're artifacts with "{oT}, Sacrifice this artifact: Add one mana of any color.")

Eventually, the Set Design team decided the card was getting a little too carried away in its attempt to sell the Horse. The solution was to give the card one basic function while making the effect modal so that selling Horses was possible but not the main use of the card. That's how we ended up with Bill Ferny's final design.

**Bill the Pony**

![](https://media.wizards.com/2023/ltr/en_0be114b28c.png)

Everyone knew from early on that we needed a card named Bill the Pony. We knew that it had to be a legendary creature with subtype Horse and have some white in him. What exactly he did and how big he would be went through a lot of changes. In researching his design evolution for this article, I notated fifteen distinct versions before his final printed one.

Bill was a helpful pony, so maybe he had a useful "enters the battlefield" effect. He could fetch you a land, which would represent travel, or maybe pick up a friend (he started in mono-white):

When CARDNAME enters the battlefield, search your library for a Plains card or a legendary creature card, reveal it, put it into your hand, then shuffle.

Forget the travel, he'll just go get your friend:

When CARDNAME enters the battlefield, search your library for a legendary card, reveal it, put it into your hand, then shuffle.

He carries supplies. Maybe we want him to interact with Food. White has aggressive archetypes, so it can be an attack trigger, and he still likes your friends, but now all of them:

Whenever CARDNAME attacks, you may sacrifice a Food token. If you do, choose both. If you don't, choose one.  
 • Legendary creatures you control get +1/+1.  
 • Untap all legendary creatures you control.

We leaned into the historic theme and gave him an ability that synergizes with Food but doesn't reference it specifically:

Other legendary creatures you control get +1/+1. If you would gain life, you gain that much life plus 1 instead.

He could encourage attacking with your friends more directly:

Prevent all combat damage that would be dealt to attacking legendary creatures you control.

Maybe a synergy with Food was the right call. He could use it to save your creatures:

Sacrifice a Food token: Return target creature you control to its owner's hand. Activate only during your turn and only once each turn.

Forget the Food. Focus on saving creatures:

Whenever one or more creatures you control become blocked, you may return one of those creatures to your hand.

No, he was a packhorse. He should interact with Food. Perhaps eating the Food could help Bill get bigger (note, at this point, he became green-white for a while):

When CARDNAME enters the battlefield, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this artifact: You gain 3 life.")  
 Whenever you gain life, put a +1/+1 counter on CARDNAME.

No, Food should help your other creatures, not Bill:

When CARDNAME enters the battlefield, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 Whenever CARDNAME attacks, creatures you control get +1/+1 until end of turn. If you gained life this turn, put a +1/+1 counter on each of those creatures instead.

Maybe Bill should be helping Hobbits (or at least smaller creatures):

At the beginning of each end step, if a creature with 2 or less power entered the battlefield under your control this turn, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")

Forget Hobbits, what if Bill used Food to help you be aggressive:

When CARDNAME enters the battlefield, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 Whenever a Food token enters the battlefield under your control, tap target creature an opponent controls.

Back to eating Food to help your creatures get bigger (Bill went back to being mono-white):

Whenever CARDNAME deals combat damage to a creature, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 Whenever CARDNAME attacks, another target attacking creature gets +X/+X until end of turn, where X is the amount of life you gained this turn.

Maybe we could tie Food to the Hobbits (there is a green-white Hobbit/Food archetype):

Whenever CARDNAME deals combat damage to a creature, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 At the beginning of each end step, if you sacrificed two or more Food tokens this turn, you may search your library for a Halfling card, reveal it, put it into your hand, then shuffle.

Food seemed key to the design. Let's go full circle back to land fetching; traveling was good flavor:

Whenever CARDNAME deals combat damage to a creature, create a Food token. (It's an artifact with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 At the beginning of each end step, if you sacrificed two or more Food tokens this turn, you may search your library for a basic land card, reveal it, put it into your hand, then shuffle.

No, let's keep to the Food and Hobbit theme:

When CARDNAME enters the battlefield, create two Food tokens. (They're artifacts with "{o2}, {oT}, Sacrifice this artifact: You gain 3 life.")  
 Sacrifice a Food token: Target Halfling gains double strike until end of turn. Activate only as a sorcery.

The story of this card's design is a common one. We had a rough shape of what we wanted, but there were a lot of ways to tweak it, so the design kept changing as the set around it changed. Little by little, we picked up themes we liked (Food should matter) and eventually the card coalesced into its final form.

Allowing players to trade Food tokens to allow a creature to deal damage equal to its toughness was the Set Design team trying hard to avoid the mistakes made by *Throne of Eldraine* when it introduced Food tokens. They wanted Food to push toward aggression and ending games rather than defense. Therefore, they put abilities on creatures (especially in white and green) that were, on average, worth more than the 3 life. This would encourage players to use Food to win rather than stall.

Bill the Pony has a lot of flavor but also has an important gameplay function. I hope Bill the Pony fans are happy.

**Dúnedain Blade** 

![](https://media.wizards.com/2023/ltr/en_352ff242df.png)

Equipment was first introduced in *Mirrodin*, our first trip to the plane. It was so well liked internally, and later externally, that we upgraded it to evergreen status the very next set. Early on, we wondered if we should have Equipment cards that can only equip to some subset of creatures. Perhaps there's a blade only Goblins can wield. We decided that was too limiting. Instead, we made Equipment cards that could equip to any creature but give bonuses to certain creature types.

In original *Innistrad*, some Equipment was more potent when equipped to Humans. The flavor captured the strengths of humans, as they were better with weapons and everyday items than the monsters of the plane. At that time, we talked about cheaper equip costs for Humans as one possible advantage. We checked with the rules and were told they could handle it. We liked the flavor that the Equipment got stronger, so we didn't end up using the equip \[SUBSET\] technology at the time.

![Pirate's Cutlass](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=435400&type=card)

The next time we considered using it was during *Ixalan*. Pirate's Cutlass was equip Pirate for a while, but in the end, we chose to have it equip to a Pirate when it entered the battlefield.

![Blackblade Reforged](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=443099&type=card) ![Team Pennant](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=513752&type=card) ![Commander's Plate](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=497825&type=card)

We finally decided to use an alternate equip cost on Blackblade Reforged in *Dominaria*. It was just the cleanest and least wordy way to write it. Testing showed that using it was intuitive. We did make the decision when using equip to (almost) always have a normal equip cost. This allowed the card to act as a normal Equipment but clearly encourages a certain theme. Next came Team Pennant in *Strixhaven: School of Mages*. The set had a strong creature token theme (it allowed "creature" cards to be instants and sorceries), so we used this technology to make it easier to equip token creatures. Next up was Commander's Plate in *Commander Legends*. The product was aimed at the Commander format, so the alternate equip cost was for your commander.

![Ceremonial Groundbreaker](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=555376&type=card) ![Luxior, Giada's Gift](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=555441)

![Robe of the Archmagi](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=562974) ![Veteran's Blade](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=583626&type=card)

*Streets of New Capenna* was the first, and the only set so far, to have two different equip abilities. Ceremonial Groundbreaker had a reduced equip Citizen cost. Luxior, Giada's Gift did something a little more complex and new in this space. It allowed you to equip planeswalkers, something Equipment isn't normally able to do (if it's not also a creature). The equip planeswalker ability grants the ability to do it, meaning it has extra functionality. Robe of the Archmagi from *Commander Legends: Battle for Baldur's Gate* was the first equip cost to include multiple creature types (Shaman, Warlock, and Wizard). Veteran's Powerblade from *The Brothers' War* is the first to equip Soldiers.

Which brings us to Dúnedain Blade. The Dúnedain are a long-lived race of Humans who settled in Middle-earth from Númenor. During the War of the Ring, the Gondorians and the Rangers of the North were Dúnedain. Aragorn, for example, is Dúnedain. The Dúnedain Blade represents one of their weapons. To connect them mechanically to Humans, the Set Design team decided to make use of equip Humans, interestingly going full circle to the beginning of this story. This card is common and was designed to be best in a Human-themed deck (the red-white draft archetype is "go wide" Humans). The card is costed to be playable in Limited formats in non-Human decks but is clearly optimized if you're playing with Humans. This means a player drafting red-white is encouraged to take this card slightly earlier than other drafters. It also means if you draft this card, you're slightly incentivized to prioritize drafting Humans.

I think we're early in the design evolution of equip . I expect us to do a lot more with it, and not just with more creature types, although we'll do plenty of that, but larger experimentation like we did with equip planeswalker. It's a flavorful and clean way to add a bit of flavor to an Equipment card.

## *Ring* Out

That's all the time I have for today. As always, I'm eager to hear your feedback on today's column, on any of the cards I've talked about, or on *The Lord of the Rings: Tales of Middle-earth* itself. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part four in my "Lessons Learned" series, and I'll continue card design stories for *The Lord of the Rings: Tales of Middle-earth* the week following.

Until then, may you enjoy playing with *The Lord of the Rings: Tales of Middle-earth* and making some stories of your own.