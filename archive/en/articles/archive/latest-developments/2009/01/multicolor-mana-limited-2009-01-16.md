
---
[Link to Wayback Machine](https://web.archive.org/web/20200818201710/https://magic.wizards.com/en/articles/archive/latest-developments/multicolor-mana-limited-2009-01-16)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645391"
[_metadata_:publish_date]:- "2009-01-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Multicolor Mana in Limited"
[_metadata_:wayback_capture_timestamp]:- "2020-08-18 20:17:10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200818201710id_/https://magic.wizards.com/en/articles/archive/latest-developments/multicolor-mana-limited-2009-01-16"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/multicolor-mana-limited-2009-01-16"
---


Multicolor Mana in Limited
==========================



 Posted in **Latest Developments**
 on January 16, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_cardfan.jpg)Here in **Magic** R&D, we often find ourselves trying to reconcile conflicting goals. For example, last week I talked about how game play and flavor considerations can find themselves at odds. Another example of this kind of situation is that **Magic** players love drafting, and they also love multicolor-themed blocks. We love both of those things too, but making a multicolor-heavy block fun to draft is tricky. Gold cards are exciting, fun, and often powerful. However, they are also much harder to play than monocolored cards, and that puts a strain on Limited mana bases.


I haven't been a **Magic** developer for very long. However, I have been a very active tournament **Magic** player since *Invasion*, which conveniently was the first multicolor-themed set developed with Limited in mind. Come with me as I take a walk down memory lane and look at *Invasion* block and *Ravnica* block with a developer's eye, and we'll see how those sets compare to *Shards of Alara*.


 


### *Invasion* Block


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_likeinvasion.jpg)*Invasion* was **Magic**'s first set since *Legends* with a major multicolor theme, and the first set we consider to be a product of "modern" design and development. It was also extremely popular, and many players remember it quite fondly.


The Limited mana fixing in *Invasion* block, however, looks very strange to my modern sensibilities. One would expect that in a multicolor-themed set there would be plenty of mana-fixing help at common, but instead the mana fixing is incredibly weak outside of green. The only common lands in the block were in *Invasion*, and they only provided multiple colors of mana when they were sacrificed. *Invasion* and *Planeshift* each have a cycle of true multilands, but only at uncommon. Green gets some spectacular mana fixing thanks to its preferred status, and cards like [Harrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Harrow), [Lay of the Land](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lay+of+the+Land), [Nomadic Elf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nomadic+Elf), [Quirion Elves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quirion+Elves), and [Urborg Elf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg+Elf) fuelled many green-based five color decks. On the other hand, the other colors get almost nothing powerful, and instead must live with cards like [Dream Thrush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Thrush), [Helionaut](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Helionaut), and [Morgue Toad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morgue+Toad) if they are to play decks that are solidly in three colors.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_threecards3.jpg)Another quirk of *Invasion* block is that many of the multicolored cards and kicker cards read a lot like "Effect from one color; effect from another color." These cards are the low-hanging fruit of multicolor card design since they are elegant, easy to read, and exciting. However, they also often become two-for ones since many iconic abilities take a card with them. Green gets +X/+X effects and black gets -X/-X effects? Great, combine those into one gold card. Black can kill creatures? Let's use that as a kicker "comes into play" trigger on a blue creature.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_threecards1.jpg)The block was also liberally sprinkled with cantrips. I assume that intent of this was to help players move through their decks to find the mana they needed, but in terms of game play it provides even more opportunities for card advantage. [Repulse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Repulse) and [Exclude](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exclude) were two of the very best commons in *Invasion*, but [Aggressive Urge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aggressive+Urge), [Kavu Climber](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Climber), and even the lowly [Zap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zap) also were easy to two-for-one your opponent with.


The low level of mana fixing encouraged players to play more lands than they needed in terms of pure quantity so that they could get their colors often enough, and it also forced them to play low-quality cards like [Helionaut](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Helionaut) and [Morgue Toad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morgue+Toad) to attempt to fix their mana. A draw full of those kinds of cards could have been a serious problem. However, thanks to all the card advantage–producing gold cards and cantrips, most draws had ways to either trade one card for two opposing cards or cantrips that found more useful spells. This made mana-fixers like [Reef Shaman](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reef+Shaman) and [Sea Snidd](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sea+Snidd) much more attractive to players in that era than they would be to a modern eye.


Because games often started out slowly due to the awkward mana, they sometimes turned into long grinding affairs where each player was topdecking by the end. Those kinds of games are the ones in which card advantage is king, since if your opponent runs out of things to do and you don't, you are probably in great shape. Cantrips and two-for ones are great ways to make sure that you don't run out of cards first.


*Invasion* block was well received, so another multicolor-themed set came along five years later. What happened that time?


### *Ravnica* Block


*Ravnica* block took an entirely different view on common mana fixing, including ten-card cycles of common lands and common artifacts that were extremely strong mana fixers. Green got a few extra mana fixing cards to maintain its status as the color that is best at mana fixing, but realistically any three-color combination could have a reasonable mana base in Limited.


 




|  |  |
| --- | --- |
| 
Boros Signet
 | 
Rakdos Carnarium
 |

An average *Ravnica* block draft contained around eleven "bouncelands" and eleven signets to support eight decks, and that was basically enough. Because each of them produces two different colors, one each of an appropriate bounceland and signet was plenty for a player to have a non-disastrous mana base. A player who prioritized the mana fixing could expect to even have an actively good mana base, even in a solidly three color deck. This was a radical change from *Invasion* block, where one had to depend partially on luck to get reasonable mana draws. I see this as a huge improvement; it's just more fun when the set doesn't punish you for trying to use all of its fun new multicolored cards.


On the other hand, *Ravnica* block continued the tradition of powerful card advantage-granting commons. *Ravnica* and *Guildpact* contain tons of cards built on the "X + Y" model of multicolor card design, as well as many monocolored but powerful card advantage creatures. For example, [Steamcore Weird](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steamcore+Weird), [Vedalken Dismisser](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vedalken+Dismisser), [Civic Wayfinder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Civic+Wayfinder), [Consult the Necrosages](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Consult+the+Necrosages), [Compulsive Research](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), and [Izzet Chronarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Izzet+Chronarch) all encouraged players to try to grind their opponent out with attrition over long games. *Dissension* managed to avoid this, but instead included a cycle of creatures that returned from the graveyard whenever their owner played a gold spell, giving players even more attrition tools.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_threecards2.jpg)Once again, the presence of these kinds of effects pushed players to build for long, grinding games defined by attrition and card advantage. It also made it easy and painless for players to spend spell slots in their decks on signets, since so many of their cards give them more things to do. Is this the inevitable fate of all multicolor-themed sets? Let's see what happened in *Shards*.


### *Shards of Alara*


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_obelisks.jpg)Unlike previous multicolor sets, *Shards of Alara* is built around groupings of three adjacent colors. Many of the set's strongest uncommons and rares have costs that include what we call "CDE"—that is, ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif), ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), and so on. These are significantly harder to play than cards that cost merely "CD," so the burden placed on the mana-fixing is quite high. On the other hand, the flavor of the set is one of five separate worlds, and including so much mana-fixing that it is correct to just play all five colors all the time to have access to the most powerful gold cards in every shard would have seriously detracted from this flavor. The cycles of Panoramas and Obelisks, along with support from the uncommon triple tap-lands, were intended to give players the help they needed to play their "CDE" cards consistently in Limited without pushing decks to include all five colors all the time.


Allow me to put my developer hat on one more time. There are 101 commons and 60 uncommons in *Shards of Alara*. The math says that on average, an eight-player draft will contain almost exactly 12 Panoramas, 12 Obelisks, and Six triple tap-lands. Those thirty mana fixers need to do the heavy lifting for eight players' worth of three-color decks in each draft. Is that enough?


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_ripclan.jpg)I never drafted triple *Shards* during the set's development as part of my job, but I have drafted it many times with printed cards because I like to play **Magic**. My experience is that players who are willing to play Obelisks tend to not have too much trouble playing their three-color spells, and those who choose not to play them experience inconsistency. However, many good players try very hard to play as few Obelisks as possible, are happy to have a slightly unreliable mana base in exchange for not playing Obelisks, and consider it a minor disaster when they have to play one and a major disaster if they have to play more. In fact, I do all three of those things. That leaves me with only 12 Panoramas and 6 triple tap-lands as mana-fixers I am happy to play. Why would I and others feel this way?


I believe that there are two reasons. One reason is that the Obelisks are very slow. They take up your entire third turn, which is an enormous cost in competitive limited. Strong **Magic** players love to attack their opponents early and often, hoping to win before their opponents' best cards show up. If my opponent and I are both playing Obelisks, then we'll each have a slow start the same amount of the time. Suppose I cut the Obelisks from my deck but my opponent does not. If my opponent has an Obelisk draw but I draw my mana perfectly, I may come out so fast that my opponent will never have the chance to come back. On the other hand, if my opponent has an Obelisk draw and I don't have my mana, I will have a little more time to naturally draw the lands I need to play my spells because my opponent spent a turn playing the Obelisk. If my opponent does not draw the Obelisk, I'm on equal footing. The potential upside for cutting Obelisks is high compared to the potential downside, so that's a tradeoff Spike is happy to make.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_obeliskambush.jpg)The other reason is that the cards in *Shards of Alara* do not protect you from mana flooding. The horde of two-for-one effects in *Invasion* and *Ravnica* that kept giving players action even when they drew few spells and many lands is conspicuously absent in *Shards*. Because of this, changing one card in your deck from a spell to a mana source is more painful since your spells run out faster. Two-for-one effects do exist in the set, but the concentration is much lower and most of them take two cards with them rather than keep giving new cards. Therefore, most of the time mana flooding in [Shards of Alara](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shards+of+Alara) limited is a disaster, and playing an Obelisk in your deck makes it more likely that that will happen. Spike would rather be unable to cast his spells for a while and then come back to win than run out of spells to cast, so his decision is easy.


In an unfortunate twist of fate, the end result of the Obelisks was exactly what the *Shards of Alara* developers hoped wouldn't happen. People who are playing three-color decks deliberately sacrifice their mana consistency for power by avoiding the Obelisks, and a small number of players who are attempting to play the best cards from all five colors eagerly snap them up instead.


My co-workers wrestled with this issue early on in *Conflux* development, and the general plan for the mana fixing in the rest of the block was determined before I got here. You'll see how they chose to address it when you play with *Conflux* and *Alara Reborn*. Of course, it won't be too long before you get your hands on *Conflux*—**magicthegathering.com** previews start next week, and the Prerelease weekend is only two weeks away! We hope you're as excited as we are.


### Poll Results


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld21_chandrawrath.jpg)

| Should we be willing to print "destroy target planeswalker" despite the flavor issues? |
| --- |
| No. The costs to flavor outweigh the game-play benefits. | 6942 | 64.7% |
| Yes. Having explicit answers to planeswalkers is important. | 2680 | 25.0% |
| I don't care. | 1111 | 10.4% |
| **Total** | **10733** | **100.0%** |

Most of the email I got was from players in the "No" camp. The common themes in their emails were that they had already figured out how to deal with planeswalkers, did not want cards that narrow to show up in their packs, and wanted something clever like "remove all counters from target permanent" that they could use in other ways instead. There was another group of players who helpfully suggested ways to get around the flavor problems but still mention planeswalkers on cards. The most common suggestions were "Remove target planeswalker from the game," which has the same "kill target opponent" ring as the destroy wording, and "Remove all loyalty counters from target planeswalker," which still requires some rules knowledge but isn't as bad. I appreciate the helpful suggestions, but neither alternative quite solves the problem.


On the other hand, a fourth of you voted that you did want direct planeswalker destruction. Only a few people from that group emailed me, but those people all reiterated how powerful an unopposed planeswalker is. We will of course continue to print sideways planeswalker answers like [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) and [Pithing Needle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle). Whether we choose to call out planeswalkers explicitly on cards remains to be seen. Thanks for all of your feedback.








