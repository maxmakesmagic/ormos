
---
[Link to Wayback Machine](https://web.archive.org/web/20200420121356/https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Today I have the privilege of introducing Alara Reborn's new mechanic. It's called cascade, and it's spectacularly fun. You may have already seen it on Bituminous Blast from the Visual Spoiler."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646531"
[_metadata_:publish_date]:- "2009-04-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Information Cascade"
[_metadata_:wayback_capture_timestamp]:- "2020-04-20 12:13:56"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200420121356id_/https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17"
---


Information Cascade
===================



 Posted in **Latest Developments**
 on April 17, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Today I have the privilege of introducing *Alara Reborn*'s new mechanic. It's called cascade, and it's spectacularly fun. You may have already seen it on Bituminous Blast from the [Visual Spoiler](/en/node/641856).


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/tcg/products/alarareborn/sgr1qw8vrg_EN.jpg)  
  

 
As with all **Magic** cards, the shining façade of the final product belies the massive amount of effort that went into producing it. Today I'll share with you the journey of the cascade mechanic, and then show you a card that was built specifically to show it off.


Before that, though, I'll introduce the *Alara Reborn* development team!


![Matt Place](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_mattplace.jpg)**Matt Place** (lead) – Matt is a former Pro Tour winner and full-time **Magic** developer. Matt also led the development of two other multicolor-themed sets, *Dissension* and *Eventide*, and that made him uniquely qualified to solve the problems that an exclusively multicolored set posed. I learned a lot from watching him work within the restrictions that were placed on him to create a fun set.


![Dave Guskin](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_daveguskin.jpg)**Dave Guskin** – Dave is a full-time web developer at Wizards. He is the driving force behind the [new version](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/arcana/169) of the [Gatherer](http://gatherer.wizards.com) card database and he was also instrumental in the creation of the [Totally Normal Draft Viewer](/en/articles/archive/draft-viewer-412009-2009-04-01). Dave spends part of his time in **Magic** R&D helping us with Limited playtests and playing Constructed in the FFL, and he occasionally he serves on set development teams.


![Alexis Janson](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_alexisjanson.jpg)**Alexis Janson** – Alexis was the winner of the Great Designer Search. Her full-time job now has her working on **Magic Online**, but she continues to help out on both design teams and development teams. Her design credits include *Morningtide*, *Eventide*, *Shards of Alara*, and *Alara Reborn*, and she also was a member of the *Shadowmoor* development team.


![Erik Lauer](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**Erik Lauer** – Erik once had a reputation as one of the **Magic** Pro Tour's best deck-builders, and now he uses those same skills to make sure that **Magic** is fun for all players no matter how much effort they put into trying to win. Midway through *Alara Reborn* development, however, Erik began his role as the lead developer of ***Magic** 2010* and became too busy to continue working on *Alara Reborn*. He left the team and was replaced by ....


![Mike Turian](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_miketurian.jpg)**Mike Turian** – Mike is both a member of the **Magic** Pro Tour Hall of Fame and an experienced **Magic** developer. His lead developer credits include *Future Sight*, *Morningtide*, and *Conflux*, and that experience meant that Mike had no trouble seamlessly jumping onto the *Alara Reborn* team.


### Cascade's Journey


Now that you know the team, let's talk about cascade!


The first version of cascade came from Mark Gottlieb. Its playtest name was "spin," and it originally had a number attached to it that was equal to the converted mana cost of the spell it was on. The ability looked like this:



> 
> Spin N (When you play this spell, find the first nonland card in your library that costs N or less. You may play it instead of CARDNAME. Shuffle your library.)
> 
> 
> 


[![Spin_into_Myth](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/FUT/Spin_into_Myth.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Spin%2Binto%2BMyth)
This mechanic created tension for the player by showing what was behind door number two and asked if the player wanted that instead of what they had cast. When you cast a spin spell, you might end up playing it, but you might also take the buyout option.


There were several problems with this mechanic. One was that cards with spin needed to have costs that took into account the increase in power that the spin mechanic gave them. This meant that the effect of a spin card that cost four mana was usually worse than the effect of a four mana card that didn't have spin, so if you hit a four mana card with the spin, you were likely to just play the new card instead. This made the cards feel more like mystery buttons than well-defined spells.


Mike Turian did not enjoy the tension that the mechanic created. He was looking for a fun and variable experience when he cast a spell with spin, and instead was presented with a thought-provoking decision when the mechanic resolved. He suggested that cascade allow you to get both spells instead of just one. That would make the mechanic all-upside, and it would also keep the game from pausing while someone made a decision. The teams decided to try that version, and they liked it.



> 
> Spin N (When you play this, find the first nonland card in your library that costs N or less. **You may play it for free.** Shuffle your library.)
> 
> 
> 


There was now a new problem. If the nonland cards in your deck all had spin and had the same converted mana cost, playing only one of them would eventually result in every spell in your deck being cast. Something less extreme but similar would happen if all the nonland cards in your deck that cost three mana had spin, and no other cards in your deck cost less than four. In that case, you would get all the spells that cost three for free. We didn't like that this felt very deterministic and tutor-like, so the team changed the spin ability to only trigger when a spin card was played from your hand.



> 
> Spin N (When you play this **from your hand**, find the first nonland card in your library that costs N or less. You may play it for free. Shuffle your library.)
> 
> 
> 


[![Fatespinner](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/MRD/Fatespinner.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Fatespinner)
The "play from your hand" clause solves the problem of spinning into another spin card. However, many people argued that this was not a problem at all. In fact, spinning into another spin card sounded like an incredibly fun thing to do. Many ways to enable this were discussed, but the simplest was to allow the mechanic to only see cards that cost less than the cost of the spell. This had various benefits. One was that it allowed for the dream of enormous spell chains. The second is that it made the template much shorter when written rigorously. It allowed us to delete "from your hand," and it also allowed us to simply say "less" rather than "less than or equal to." Finally, it made the mechanic work cleanly without requiring us to attach a number to it. This was the next version.



> 
> Spin (When you play this from your hand, find the first nonland card in your library **that costs less than this card.** You may play that card for free. Shuffle your library.)
> 
> 
> 


Spin now provided big dreams. A lucky player could play a 7-cost spin spell, spin into a 6-cost spin spell, spin into a 5-cost spin spell, and so on, until the process stopped with a two-mana spell. It stopped at two because Alara Reborn's hook kept it from containing any one mana spells, and therefore a two-mana spin spell in a deck full of *Alara Reborn* cards would simply reveal its caster's library to its opponent before forcing it to be shuffled. The cheapest cards in *Alara Reborn* that have cascade cost three mana, but the possible spell chain that went all the way from 7 to 2 was still very exciting.


The mechanic passed through the hands of some editors, and then the designers handed the following templated version off to development.



> 
> Spin (When you play this spell, **reveal cards from your library until you reveal a nonland card with a lesser converted mana cost. You may play it without paying its mana cost. Then** shuffle your library.)
> 
> 
> 


Ken Nagle had fallen in love with the dream of big spell chains and was one of the people who advocated for this version of the mechanic. Once spin had been changed to accommodate the dream of spinning through every possible mana cost, Ken built a deck and tried to live it. I don't know if he ever managed to chain spells all the way from 7 to 2, but I do remember at least one chain of spin cards he produced that was four cards long. His deck produced tons of dramatic and fun moments and was a source of constant amusement for Ken's opponents and all who watched his games.


About this time, the creative team dubbed the mechanic "cascade," and **Magic** editors began to cut words away from its reminder text. The file contained the following version of cascade for a long time.



> 
> **Cascade** (When you play this spell, reveal cards from the top of your library until you reveal a nonland card **that costs less**. You may play it without paying its mana cost. Then, shuffle your library.)
> 
> 
> 


[![Temporal_Cascade](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/MRD/Temporal_Cascade.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Temporal%2BCascade)
Near the end of development, many playtesters complained that cascade forced them to shuffle their library. The physical process of resolving a cascade trigger was extremely fun, but needing to shuffle every time was too annoying. Lead developer Matt Place took sympathy on them. The templating team was unhappy about adding words to an already wordy mechanic, but they solved the problem by removing the cards from the game rather than revealing them, then putting them on the bottom of the library.


The last question to be answered was in what order the removed cards go on the bottom of your library. If the player who resolved the spin was allowed to choose the order, a player who had nothing left in his deck to spin into would end up stacking his entire deck. We didn't like this, so we went with the slightly bizarre option of randomizing only the revealed cards. This is still a little bit of shuffling, but it isn't nearly as bad as randomizing the whole deck.


Here's the final version.



> 
> Cascade *(When you play this spell, remove cards from the top of your library from the game until you remove a nonland card that costs less. You may play it without paying its mana cost. Put the removed cards on the bottom in a random order.)*
> 
> 
> 


Of course, we didn't just design and develop a mechanic. We also created cards to put it on, and we tried to use some of those cards to truly show it off. In some ways, the best part of cascade is the fun of discovering what unknown card you get for free. Because of this, the *Alara Reborn* design team decided to make a creature with cascade that could be cast multiple times. Here's what they came up with.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/tcg/products/alarareborn/t2dzux4tuj_EN.jpg)  
  

 
This card was designed when someone jokingly said that the only thing better than casting a cascade spell was casting a cascade spell multiple times. Someone immediately had the idea to put cascade on a creature that went back to your hand somehow. It seemed too annoying to have the creature immediately go back to a player's hand when it died, so instead they went with the slightly strange "third from the top" clause.


Having cascade on a seven-mana spell creates awesome moments in game play. When you play Engima Sphinx in an Esper deck, you could end up with something as small as an [Etherium Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Etherium+Sculptor), but you might also end up with something as enormously awesome as [Sharuum the Hegemon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sharuum+the+Hegemon). It is a mystery!


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld34_ip8ee7veah.jpg)  
  

 
However, if your deck has cascade cards of all the mana costs from 7 down to 3, you could very well end up with a completely ridiculous chain like this one.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld34_4dlk0b3226.jpg)  
  

 
I have had a blast playing with cascade, and I can't wait for everyone else to be able to share that fun. Your first chance to play with *Alara Reborn* will come at the *Alara Reborn* Prerelease, which is April 25 and 26. Those events will be happening at local stores all over the world, so find one and I promise you'll have tons of fun playing with all the new multicolored cards!


### Last Week's Poll




| **Do you follow @[dailymtg](/en/articles/archive/2012-07-10) on Twitter?** |
| --- |
| No. I know what Twitter is but don't have an account. | 4560 | 60.3% |
| No. I don't know what Twitter is. | 2006 | 26.5% |
| Yes | 552 | 7.3% |
| No. I have a Twitter account and don't follow @dailymtg. | 450 | 5.9% |
| **Total** | **7568** | **100.0%** |

  
Twitter is a social networking site that lets people share what they are up to in real time. Through the @[dailymtg](/en/articles/archive/2012-07-10) Twitter feed, Kelly Digges and Monty Ashley post fun tidbits about day-to-day life inside **Magic** R&D. Sometimes we use it for other things. For example, people who follow the @dailymtg twitter feed received a special bonus preview card last Friday.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/tcg/products/alarareborn/jmuy79o67k_EN.jpg)  
  

 
We promised that we would give another preview card over Twitter if we hit 2000 followers. We did, and then we previewed this.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/tcg/products/alarareborn/fu3s4fawaj_EN.jpg)  
We know that not everyone saw those on Twitter, and some may not have seen them at all before now. You can make sure you don't miss any cards by checking the [Visual Spoiler](/en/node/641856). Every card we preview anywhere—such as the preview card in today's [The Week That Was](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/boab/34)—will find its way there!


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/ARB_ArticleBanner_Pre1.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prereleases)





