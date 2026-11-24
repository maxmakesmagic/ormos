---
id: vspjk1v8
kind: article
lang: en
path: /en/articles/makingmagic/2023/06-26-stepping-into-the-ring-part-2
title: Stepping Into the Ring, Part 2
published: '2023-06-26'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    lang_detected: en
    capture_id: 230483
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    captured_at: '2024-05-18 01:18:17+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    lang_detected: en
    capture_id: 230483
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    captured_at: '2024-05-18 01:18:17+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    lang_detected: en
    capture_id: 230483
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    captured_at: '2024-05-18 01:18:17+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    lang_detected: en
    capture_id: 230483
    url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
    captured_at: '2024-05-18 01:18:17+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: vspjk1v8
  url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
  page_key: magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:18:17+00'
  capture_id: 230483
  wayback_url: https://web.archive.org/web/20240518011817id_/https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vspjk1v8
  capture_id: 230483
  url: https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
  wayback_url: https://web.archive.org/web/20240518011817id_/https://magic.wizards.com/en/news/making-magic/stepping-into-the-ring-part-2
  captured_at: '2024-05-18 01:18:17+00'
  template: contentful
  sha256: 60c21a6aaffd1441fbadd8effc0bbe536ebad622f245c16a626efe00fb262465
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
[Last week](/en/articles/makingmagic/2023/06-12-stepping-into-the-ring-part-1), I started sharing some card-by-card design stories from [*The Lord of the Rings: Tales of Middle-earth™*](https://web.archive.org/web/20230626000000/https://magic.wizards.com/en/products/the-lord-of-the-rings-tales-of-middle-earth) (LTR). Today's column is part two of three, where I continue these stories.

**Elven Chorus**

![](https://media.wizards.com/2023/ltr/en_1c506d9430.png)

I often have fun tracing a recurring mechanic back to its roots and watching how it evolves over time. Elven Chorus has an interesting design pedigree, so I've chosen it as my historical look back. It's an ability we often use these days, but that wasn't always the case.

Once upon a time, this ability was a single card design, something that, if you'd asked when it was made, we thought we'd be doing once. To explain this card's design, I wanted to go through the history of cards like it. I should also note that I am separating casting cards off the top of your library from spells that exile the top card(s) of your library and let you cast them. They are similar in nature, but I'm exploring what I call "the Future Sight" variant (you can look at the top of your library and cast a certain subtype). I'm fully aware what counts and doesn't count is a little subjective, so I'm using my best judgment.

Our story begins in *Onslaught*. We were trying to capture an element of the story. Ixidor, the antagonist of the set, has the power to make real anything he can dream of. We had just done the wishes in *Judgment*, so getting things from outside the game was off the table. How could we capture the feel of casting something that wasn't there? We then realized the perfect answer. What if you could cast cards off the top of your library? The card we made was called Future Sight.

![Future Sight](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=39628&type=card)

Future Sight is a great example of how creating a single card can sometimes tap into a whole vein of design space. Not that we always know it at the time. You'll see there's a pretty big gap between the making of Future Sight and it becoming a recurring mechanic.

![Magus of the Future](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=136051&type=card)

The second time the effect showed up, it wasn't really a new card as much as a throwback to the original Future Sight. In the *Time Spiral* block, we made cycles of Maguses that represented powerful noncreature cards (often ones on the Reserved List that we couldn't reprint) with their effects used as abilities on creatures. The third set in the block had a cycle of Maguses based on enchantments. As the set was literally called *Future Sight* and Future Sight was a very popular enchantment, it was basically a shoo-in for inclusion. Note that this was five years after its original printing.

![Galvanoth](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=214053&type=card) ![Garruk's Horde](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=220077&type=card) ![Descendants' Path](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=276498&type=card)

It took four more years, but we finally dipped our toe into this design space. Casting things from the top of the library is a lot of fun, and it seemed like there were other designs we could make. The key, we realized, was that we needed to be a bit narrower to be able to make a lot of different cards with this mechanic, so for each future card designed in this space (well, most of them), we started making restrictions on what you could cast.

Remember, we were nine years past the original design. Galvanoth, originally from *Mirrodin Besieged*, didn't even use the framework that's become the telltale sign of this mechanic (you can look at the top card of your library and cast a certain subset of cards), but as it was our first foray into it past *Future Sight* and it's a Magus, I've included it here.

Galvanoth was a variant, for the first time in red. It's triggered, it only lets you cast one card per turn, it pays the mana cost, but you can see we were dipping our toes into another card that lets you repeatedly cast cards from the top of your library. Galvanoth was also the first time this effect appeared on a creature.

Garruk's Horde in *Magic 2012* was the first card that just repeated the Future Sight formula. It did it for the first time in green, and its restriction was creature cards, what would go on to be the most popular subset for this mechanic.

Descendants' Path from *Avacyn Restored* is next in line, and like Galvanoth, it's not quite the structure we ended up using. It's essentially a green Galvanoth, except it cares about creatures rather than instants and sorceries and is an enchantment instead of a creature. I decided to list it here because it shows R&D was trying to figure out the best way to execute on this mechanic.

Galvanoth and Descendants' Path go one direction while Future Sight and Garruk's Horde go a different direction. The Future Sight path would win out. From here on out, I'm just listing cards that do it strictly the Future Sight way. You can see the top card of your library, and/or it's revealed, and you can cast a subset of cards from it.

![Melek Izzet Paragon](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=369062&type=card) ![Rashmi, Vizier of the Menagerie](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=417757&type=card) ![Precognition Field](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=442949&type=card)

Melek, Izzet Paragon was the first card to do this in multicolor in blue-red and allowed you to cast instants and sorceries. This was the first card to have an additional ability, one that triggers if you cast the proper spell off the top of your library.

Vizier of the Menagerie from *Amonkhet* was another card that let you cast creatures off the top of the library. This was the first card that doesn't cast it for free and grants you an ability to make the spells easier to cast (allowing you to use any color of mana in this case).

Precognition Field from *Dominaria* is similar to Future Sight, even being an enchantment, but restricts you to casting instants and sorceries. The innovation on this card was that it lets you get rid of cards off the top of your library to help you find the subset you can cast.

![Experimental Frenzy](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=452849&type=card) ![Bolas's Citadel](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=461006&type=card) ![Mystic Forge](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=466987&type=card)

Experimental Frenzy from *Guilds of Ravnica* was the first card since Future Sight to let you cast any card from the top of your library, but it comes with a restriction that you can't play cards from your hand. It's also the first one that lets you destroy it. Bolas's Citadel from *War of the Spark* was the first time this ability appeared in black. It also lets you cast any spell, but like Experimental Frenzy, comes with a drawback (you lose life equal to the mana cost of the spell). Mystic Forge from *Core Set 2020* was the first artifact with this ability and the first card to make artifacts the subset you can cast.

![Elsha of the Infinite](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=470586&type=card) ![Vivien, Monsters' Advocate](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=479695&type=card)

![Conspicuous Snoop](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=485462&type=card) ![Realmwalker](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=503804&type=card)

Elsha of the Infinite from *Commander (2019 Edition)* was the first three-color card with this effect and the first in white. It restricts you to noncreature, nonland spells but grants them an extra ability: to cast them at "instant speed." Vivien, Monsters' Advocate from *Ikoria: Lair of Behemoths* was the first planeswalker with this ability and the third to specifically let you cast creatures.

It's interesting to see that, as we design a mechanic, when we get enough volume, we start designing subthemes to it. Conspicuous Snoop from *Commander (2021 Edition)* was the first to restrict you to a creature subtype, in this case Goblins. This theme would become a popular one down the line. It can also grant the creature an ability based on what card is on top of your library. Realmwalker from *Kaldheim* allows you to pick which creature type you want to cast from the top of your library.

![Ranger Class](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=527489&type=card) ![Xanathar, Guild Kingpin](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=527526) ![Galea, Kindler of Hope](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=531830)

Ranger Class from *Dungeons & Dragons: Adventures in the Forgotten Realms* (AFR) further cemented green's ability to cast creatures off the top of the library as the main offshoot of this ability. Xanathar, Guild Kingpin, also from AFR, was the first card to let you cast spells off the top of an opponent's library. Galea, Kindler of Hopes from the AFR Commander decks was the first card to let you cast Aura and Equipment cards. This was the first time the ability showed up on more than one card in the same product release.

![Augur of Autumn](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=531830) ![Cemetery Illuminator](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=540888) ![The Reality Chip](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=548372)

Augur of Autumn from *Innistrad: Midnight Hunt* was the first to let you cast just lands and is yet another green card that, under certain conditions, lets you cast creature cards. Cemetery Illuminator from *Innistrad: Crimson Vow* gives you ways to exile cards and then lets you cast cards off the top of your library that share a card type. It was the first in this group that created a condition where there's variance in what you can cast and changes game to game. The Reality Chip from *Kamigawa: Neon Dynasty* was the first to let you play lands and cast spells.

![Falco Spara, Pactweaver](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=555387) ![Korlessa, Scale Singer](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=563163&type=card)

![Nalia de'Arnise](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=567106) ![Emperor Mihail Ii](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=580489)

Falco Spara, Pactweaver from *Streets of New Capenna* lets you cast any spell, but it adds in an additional cost (removing a counter from a permanent you control). Korlessa, Scale Singer from *Commander Legends: Battle for Baldur's Gate* lets you cast Dragons; and Nalia de'Arnise, from a related Commander deck with a party theme, lets you play Clerics, Rogues, Warriors, and Wizards. Emperor Mihail II is from a *Dominaria United* Commander deck and lets you play Merfolk.

![Lila, Hospitality Hostess](https://media.wizards.com/2022/unf/en_ITXZbTR071.png) ![One with the Multiverse](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=583644&type=card) ![Isu The Abominable](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=589566&type=card)

![Errant and Giada](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=607282&type=card) ![Sigarda, Font of Blessing](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=615440)

Lila, Hospitality Hostess from *Unfinity* was the first *Un-* card to play in this space. It allows you to cast commons (normal *Magic* rules don't allow for caring about rarity mechanically). Usually when a mechanic shows up with an *Un-* variant, it's the sign that it's reached a certain popularity. One with the Multiverse from *The Brothers' War* was the first one to let you play lands and cast any spell while allowing some of them, one per turn, to be cast for free. Isu the Abominable from *Jumpstart 2022* lets you play snow lands and cast snow spells, for the first time involving supertypes in the subset. Errant and Giada from *March of the Machine* lets you cast spells with flash or flying. Sigarda, Font of Blessings from *March of the Machine: The Aftermath* lets you cast Angels and Humans.

Which brings us to Elven Chorus. The card was trying to capture Elves singing. As is often the case in *Universes Beyond* designs (or any top-down design), the designers look for mechanics that already exist that capture the feel we want. Future Sight for creatures has become a go-to mechanic in green and felt like a great fit here. There was one tweak to allow your creatures to tap for mana, which felt very Elf-like (thanks to *Magic*'s long history of Elves producing mana) and was nicely synergistic with a card that requires mana to use efficiently.

**Frodo, Sauron's Bane** 

![](https://media.wizards.com/2023/ltr/en_e1bbe34ee3.png)

Frodo is the protagonist of *The Lord of the Rings*, so there was no doubt he was going to get a card. In the end, he would get two cards (and that's just in the main set). The one I want to talk about today is his rare card. It went through a lot of changes and shows how tricky it can be to make a top-down card of a popular character.

**Frodo, the Storyteller (version #1)**  
 1W  
 Legendary Creature — Hobbit  
 2/2  
 When CARDNAME enters the battlefield, it becomes your Ring-bearer. (*It's legendary and has ward {2}.*)  
 At the beginning of your end step, if you don't control a Ring-bearer, you may exile CARDNAME. If you do, search your library for a Saga card, reveal it, put it onto the battlefield, then shuffle.

The first version of this slot was designed during early set design. During vision design, we just made one version of every character, but Set Design decided they wanted multiple versions of the more popular characters (more on this next week). This slot was the second Frodo. They ended up moving the existing one to uncommon (although it also went through many changes) and this slot to rare.

This was when the Ring tempts you mechanic was called Ring-bearer and acted like a status (granting you legendary and ward 2). Because they were making a second version, they realized they had to come up with a way to differentiate them. The obvious choice was to

represent them at different points in the story, so you could show how the character changes through the story. This first stab at this card represented Frodo at the end of the tale, telling stories about his adventure.

The card is small, 1W for a 2/2, because Frodo is small. His "enters the battlefield" trigger involves becoming a Ring-bearer because that's key to his character. The second ability was trying to capture the idea that, after his time of being a Ring-bearer, he would have grand stories to tell. Mechanically, we use Sagas to represent stories, so you can trade Frodo for a story (i.e., Saga). Note that he is exiled rather than sacrificed to imply that he doesn't die.

**Frodo, the Storyteller (version #2)**  
 1W  
 Legendary Creature — Hobbit  
 2/2  
 When CARDNAME enters the battlefield, it becomes your Ring-bearer. (It's legendary and has ward {2}.)  
 At the beginning of your upkeep, if you don't control a Ring-bearer or a Saga, you may return a Saga card from your graveyard to your hand.

The joke of the first version was, "Some storyteller. He can only tell one story." Making you trade Frodo for the Saga seemed a little harsh, so this version tried a different approach, one where you can keep Frodo around to repeatedly, but slowly, bring back Sagas, slowly because you can only have one at a time.

**Frodo, Shire Storyteller (version #3)**  
 1W  
 Legendary Creature — Hobbit  
 1/3  
 When CARDNAME enters the battlefield, exile the top X cards of your library face down, where X is the number of legendary creatures you control. For as long as those cards remain exiled, you may look at those cards and play one of them each turn.

The Saga version ended up being a little too niche. If you opened the rare Frodo in a draft, we wanted you to be able to play him, and the last version was just too narrow. By this point, Set Design had added the "legendary matters" theme to the set, so they tried incorporating it into Frodo's design. Why was he such a good storyteller? Because he had met so many interesting characters. The effect was an attempt to do a white version of impulsive draw, one where you draw cards, but only one a turn. It's more of a long-game take on the mechanic than red usually gets, and it played into how we've tried to shape white card-drawing, to be stretched out over many turns.

**Frodo, Sauron's Bane (version #4)**  
 2W  
 Legendary Creature — Halfling  
 2/2  
 CARDNAME can't be blocked by creatures with power 3 or greater.  
 Whenever CARDNAME deals combat damage to a player, you may have CARDNAME stop being your Ring-bearer. When you do, exile target nonland permanent that player controls.

Being a card-draw engine didn't feel Frodo-y enough, and it didn't mention the Ring at all, which felt odd for a Frodo card, so they went in a different direction. Rather than show Frodo at the very end, they decided to back up a tiny bit and show him on Mount Doom. The saboteur ability (when a creature generates an effect when it deals combat damage to an opponent) represents him destroying the Ring. You would get a payoff for destroying something of the opponent's that you hit. The evasion ability, not being blocked by larger creatures, played up his size and sneakiness as a Hobbit.

**Frodo, Sauron's Bane (version #5)**  
 1W  
 Legendary Creature — Halfling  
 1/2  
 When CARDNAME enters the battlefield, target creature you control becomes your Ring-bearer. (It's legendary and can't be blocked by creatures with greater power.)  
 At the beginning of each combat, your Ring-bearer gains first strike until end of turn if you control a creature with first strike. The same is true for flying, double strike, deathtouch, haste, hexproof, indestructible, lifelink, menace, reach, trample, and vigilance.

The last version didn't give Frodo the Ring but made you acquire it through other cards. This version went back to Frodo getting it as an "enters the battlefield" effect. Note that the effect of the Ring has changed from ward 2 to skulk. This version gave a bunch of rewards to your Ring-bearer based on what evergreen keywords your other creatures had. This list went through a bunch of changes but ended up being all evergreen keywords save for ward and defender (ward because hexproof was there, and defender because it's just downside).

**Frodo, Sauron's Bane (version #6)**  
 W  
 Legendary Creature — Halfling  
 1/1  
 When CARDNAME enters the battlefield, claim The One Ring. (Add its next ability, then a creature you control becomes your legendary Ring-bearer.)  
 Your Ring-bearer has "This creature gets +0/+1 for each other legendary creature you control and assigns combat damage equal to its toughness rather than its power."

The last version was a fine *Magic* card but not a great Frodo. It involved the Ring, which was good, but having your Ring-bearer fly because Frodo and another flying creature were there just didn't feel like it made sense with the character. This version granted one specific ability to the Ring-bearer, the ability to deal damage equal to its toughness, aided by the +0/+1 boost.

**Frodo, Unlikely Savior (version #7)**  
 W  
 Legendary Creature — Halfling Peasant  
 1/1  
 {oW}: CARDNAME becomes a Halfling Scout with base power and toughness 2/3.  
 {oWoWoW}: If CARDNAME is a Scout, it becomes a Halfling Rogue with "Whenever CARDNAME attacks, claim The One Ring."  
 As long as CARDNAME is a Rogue and you've claimed The One Ring four times this game, your life total can't change.

Again, this effect just didn't feel Frodo enough. Also, it encouraged you to put the Ring on your biggest creature, which felt a bit odd. The Set Design team decided to try a completely different take, one inspired by a popular design from many years ago.

![Figure of Destiny](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=158106&type=card)

This gem of a design was created by Brian Tinsman as an attempt to top-down design a creature leveling up over time. Figure of Destiny was so beloved that it's been the springboard for many cards, as well as the level and class mechanics from AFR.

What if the Frodo card represented Frodo changing over time? As with Figure of Destiny, they used creature types as a way to unlock other activations. Frodo would start as a 1/1 Peasant, upgrade to a 2/3 Scout, then become a Rogue and pick up the Ring. The last upgrade didn't happen via mana but through the Ring. The Set Design team wanted to come up with an exciting final ability, as you must jump through a lot of hoops, so they came up with "your life total can't change."

**Frodo, Unlikely Hero (version #8)**  
 W  
 Legendary Creature — Halfling Peasant  
 1/2  
 As long as you've claimed The One Ring four or more times this game, you don't lose the game for having 0 or less life.  
 {oW}: Frodo, Unlikely Hero becomes a Halfling Scout with lifelink and base power and toughness 2/3.  
 {oWoWoW}: If Frodo is a Scout, it becomes a Halfling Rogue with "Whenever you gain life, claim The One Ring."

This version added lifelink to the first upgrade and the second ability changed the Ring trigger to gaining life rather than attacking. This allowed attacking—mostly to do it because of the lifelink—but also allowed the deck to be built around it in other ways. The final ability was moved, I assume for a templating reason, to the front of the card and changed "can't lose life" to "can't lose for having 0 life."

**Frodo, Unlikely Hero (version #9)**  
 W  
 Legendary Creature — Halfling Peasant  
 1/2  
 {oW}: Frodo, the Hero becomes a Halfling Scout with lifelink and base power and toughness 2/3.  
 {oBoBoB}: If Frodo is a Scout, it becomes a Halfling Rogue. Whenever you gain life, if CARDNAME is a Rogue, claim The One Ring. Then each opponent loses that much life.

The final abilities of versions seven and eight ended up being more frustrating than fun. Opponents playing against it felt hopeless. They most often couldn't win, yet Frodo's controller still had to go through all the steps to finish the game. This version made us realize that we weren't using the upgrades as efficiently as we could to tell the story. How do you show Frodo being tempted? Change the activations from white to black. The finished version would take this a step further, having the mana cost be white, the first activation be white-black hybrid, and the last activation black.

The final effect for this version became life loss, which would often lead to a win but didn't feel exciting enough. If you jump through a lot of hoops, you want an exciting finish. In the end, the Set Design team decided to make this the alternative-win condition. If you can level Frodo all the way up and then tempt him with the Ring, then have him "finish his mission of getting rid of the Ring," well, then you win the game. That felt grand enough.

And that is how Frodo went from telling stories to winning the game.

## It Has a Nice *Ring*

That wraps up part two of my stories. As always, I'm eager to hear your feedback on today's column, any of the cards I've talked about, or *The Lord of the Rings: Tales of Middle-earth*. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part three.

Until then, may you create your own Fellowship to play *The Lord of the Rings: Tales of Middle-earth*.