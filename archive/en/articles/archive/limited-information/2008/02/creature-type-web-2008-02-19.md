
---
[Link to Wayback Machine](https://web.archive.org/web/20160619191256/http://magic.wizards.com/en/articles/archive/limited-information/creature-type-web-2008-02-19)

[_metadata_:author]:- "Dave Guskin"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "620156"
[_metadata_:publish_date]:- "2008-02-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Creature Type Web"
[_metadata_:wayback_capture_timestamp]:- "2016-06-19 19:12:56"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160619191256id_/http://magic.wizards.com/en/articles/archive/limited-information/creature-type-web-2008-02-19"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/limited-information/creature-type-web-2008-02-19"
---


The Creature Type Web
=====================



 Posted in **Limited Information**
 on February 19, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DaveGuskin.jpg)
By Dave Guskin











Hello! You're probably asking yourself who the heck this Guskin guy is, but fear not, reader: I'm your first guest writer. Known as "Guuuuuskiiiiiin!" to many here at Wizards, I'm pretty much a draft-a-holic and avid fan of all sorts of Limited formats. Back when I was out in the world, I was a competitive PTQ player about once monthly and a casual drafter with college and work friends most evenings and weekends. Now that I work for Wizards, I tend to draft about three times a week on average (it used to be once a week, but now we have the technology of Cubes and Winston to get one-on-one drafts going all the time.) You might be interested to know that I also have two degrees in physics. Currently, I work as a web developer here at Wizards, but whenever the word "draft" reaches my ears, I still perk up and start salivating. So when I was asked to write an article on Limited, I happily accepted. This is my bread and butter!


### Oh What a Tangled Web We Draft


I'm hijacking Noah's column today to discuss a concept I've been knocking around I call the Creature Type Web. Learn it, love it and use it to thwart your enemies! It can even be extended past the new-hotness creature types of today's *Lorwyn-Morningtide* format back to old-and-busted mechanics of **Magic**'s murky history. I'll get to those further on down.


Your Creature Type Web is how tribally connected your deck is. The most tribal deck possible has the appropriate creature type on all non-land cards in it. The least tribal deck possible has no matching tribes among any of its number. (I doubt this is even possible outside of drafting specifically to avoid shared creature types. Man, would your draft have had to go wrong for that to happen in *Lorwyn* / Lorwyn / Morningtidedraft...) Usually, your deck is going to fall in between those two extremes.


Back in Lorwyn, it was easy to figure out how good your deck was at utilizing tribal effects: just count up the number of cards with that type you have. The intersection of two "races", such as Goblins and Faeries, was facilitated by only one kind of card – changelings – and so it was straightforward for each possible draft pick or deck choice how to go about evaluating tribal effects. The big shakeup comes in with *Morningtide*: now there are effects that care about multiple possible matches and which let you choose the kind of match you care about at the spur of the moment, and class types make it extremely easy for most limited decks to have that intersection of tribes even without changelings.


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/limited/nw51_oldraces_venn.jpg)*Good luck finding non-gelatinous Goblin Faeries in Lorwyn!*


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/limited/nw51_newraces_venn.jpg)*Visualizing three-set intersection is tricksy – maybe I can patent this crazy triangle method...*


So, how do we use this crazy Creature Type Web to further our Limited games?


### Matty Lab and the Monte Carlos


I tried to solve this problem using statistics and equations. I ran into what fancy analysts call the "multivariate problem": trying to reconcile a million different factors that impact a game all at once. I simplified to just worrying about kinship, since that's an effect that's interesting and new, but clearly informs use of other tribally-interested cards. But it turns out, I quickly found the math even for this is more complex than I could solve analytically. Heck, people have been trying to solve problems involving drawing with replacement from a random deck for years, so this didn't surprise me overmuch. What it did inspire me to do is what scientists always do when the math gets too hard: run an experiment!


With the help of my science buddies Todd and Sam, I created a little trial program to figure out how many kinship triggers one could expect over the course of a game, given some number of tribally connected cards. It's a grossly simplified model from cardslinging as we know it, with a number of finicky assumptions, but it's illustrative. I ran this simulation one MILLION times and recorded the results. An interesting answer emerged: sure, as you increase the total number of tribal cards in your deck, you get better kinship results as one would expect... but!


* Zero triggers is by far the most common result (the mode), even for decks that are heavily tribal. (This makes sense if you think about the number of lands you have to run.)
* You can see clear "targets" for what number of tribal cards to strive toward if you want to make efficient use of your kinship cards.

**Assumptions I Made**


* You make every land drop.
* The game is 20 cards drawn total.
* You play the kinship card a.s.a.p.
* Your kinship guy never gets killified.
* Two kinship guys are twice as good.
* Tastes great! Less filling!


Interestingly, the "swingier" kinship effects such as [Leaf-Crowned Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaf-Crowned+Elder)'s free spell and Pyroclast Council's [Pyroclasm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm) are effects you're fine with triggering only once or twice and not necessarily every game (since they're respectable cards even without triggering in terms of impact on the board), so you can shoot for the lower targets, but the "solid" kinship effects such as those on [Kithkin Zephyrnaut](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Zephyrnaut) and [Winnower Patrol](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winnower+Patrol) are effects you want to max out on, so the higher targets are the more relevant ones.

 




| **Probability Jumps** |
| --- |
| **Kinship Triggers (1 kinship card)** | **Tribal count** |
| **to hit ~10% of games** | **to hit ~50% of games** |
| 1 | 4+ | 13+ |
| 2 | 7+ | 16+ |
| 3 | 10+ | 20+ |
| 4 | 14+ | lots of luck :) |
| **Kinship Triggers (2 kinship cards)** | **Tribal count** |
| **to hit ~10% of games** | **to hit ~50% of games** |
| 1 | 3+ | 12+ |
| 2 | 4+ | 13+ |
| 3 | 6+ | 14+ |
| 4 | 8+ | 16+ |

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/limited/nw51_1kinship.jpg)


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/limited/nw51_2kinships.jpg)


The dotted lines represent a three-cost kinship card (as opposed to the solid lines, which show a two-cost kinship card)–since three-cost kinship guys can't be played as early as two-cost kinship guys, the odds are slightly reduced that you can hit the mark you're looking for. However, it's a small effect (but gets larger the higher cost the kinship card is), since the cost only matters if you draw it early in the game.


Also note all of these calculations are approximate. I know a MILLION trials sounds like a lot (it better – those capital letters for emphasis don't come cheap!) but in the grand statistical scheme of things, there's still a bit of error involved with limited sample size.


Click [here](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/nw51&page=2) for a more detailed explanation of the math.


### Choose—But Choose Wisely


But numbers aren't the whole story! (In fact, numbers aren't very good at telling a story at all; they're more of the silent, sensitive type.) Another perspective to take is to think around the possible options *Morningtide* brings to your tried-and-true *Lorwyn* experience. You'll find four categories of cards in *Lorwyn* BlockLimited that utilize this Creature Type Web concept and to which we can apply the scalpel of science:


 


* Lords
* Kinship
* Choose a creature type
* "Web" cards

**Lords and "Count-Me" Cards**


 



![Rage Forger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rage+Forger)

There's not much new ground here; *Lorwyn* already inundated us with effects that care specifically about count of a particular creature type. Lead Developer Devin Low outlined these kinds of cards in his article [Count-Me vs. Threshold Zero](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl10). It's worth noting that there's a new twist to this category with the inclusion of *Morningtide*: cards that care about the count of a particular class, such as [Rage Forger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rage+Forger) or [Obsidian Battle-Axe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obsidian+Battle-Axe)... and as I mentioned above, many more decks with be able to assemble something akin to a race/class-powered Voltron using subtype superglue.

Note that there's a smattering of analogous mechanics from **Magic**'s history that also fall into this category and that the model above fits for these too! Affinity has the same elements as a "count-me": the card with affinity plays the role of the lord (it gets better the more cards you control of the specified type, for example) and your tribe is the type it has affinity for.


**Kinship**


Kinship is special because it cares about (at least) two different types. In fact, observing how kinship plays in limited was the whole "Eureka!" moment that motivated me to write about this Creature Type Web construction. With kinship, the connectedness of your deck is the key quality. A mono-tribal deck has no worries, but as soon as you venture into duo-tribal or further (we can't all be as close-knit as Mr. Mono-Thoughtweft and his Weenie Beatdown House of [Pain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pain)) the key becomes the intersection of your tribes along the kinship condition.


You can always cheat, of course. [Amoeboid Changeling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Amoeboid+Changeling), [Runed Stalactite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runed+Stalactite), instants like [Shields of Velis Vel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shields+of+Velis+Vel)—these will all allow you to "boost" your kinship to trigger on any creature. Statistics is going to catch you with your amorphous hand in the cookie jar, though—overall, you have better chances maximizing your web during the draft and deck construction than you would relying on a two-card simultaneous combo that still relies on the top card of your deck.


Hybrid mana from *Ravnica* is the closest analog in Limited formats to the enigma of kinship—when you're building your mana base, you just need to be aware that either color match will allow you to play your hybrids. So you can reverse the numbers I have above to give you a quick and dirty rubric for the construction of your mana base—for a two-cost hybrid spell, you need to "trigger" with the land(s) of the appropriate type twice, meaning you need at least 7+ sources of the appropriate colors in your deck to consider playing it.


**Choose a Creature Type**


I always feel like an Iron Chef when I have any of the "choose a creature type" cards in my pile trying to construct my deck—the "choose" card is like the secret ingredient and you'll trying to see which dish will have the most bang for the judges' buck. These cards are easier to maximize than the lords, but not by much: almost always, you'll have drafted something with a major tribal theme, so these cards let you bank on your secondary or tertiary tribal counts. These are like the proverbial glove to a changeling's hand—an outlet for your biggest tribal effects without regard to their underlying type (as long as it matches).


The "wild" component of this category is partially mirrored in the converted mana cost matters cards from *Scourge*. You clearly get *some* effect from any permanent you control (well, except for your [Ornithopter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter). Nobody likes your style, [Ornithopter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter)!) However, your Torrent of Flame is going to be much more powerful if you have lots of high converted mana cost permanent cards in your deck, just as a "choose a creature type" card is going to go to the Limit if you maximize one tribe.


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/limited/nw51_rockband.jpg)*Maybe get the band—I mean web—back together?*


**"Web" Cards**


There are really only a couple cards in *Morningtide* that illustrate perfectly this connectedness concept, and I have dubbed them "web" cards. [Reins of the Vinesteed](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reins+of+the+Vinesteed) is a clear example of a card that scales with a tightly connected web—if you can walk along connected creature types, from Elf Warrior to Treefolk Warrior to Treefolk Shaman to Elemental Shaman, you can keep this [Rancor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor) analogue in play quite a while.


[Rivals' Duel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rivals%27+Duel) addresses the same problem, but from the opponent's point of view: how vulnerable is your deck to being Rivals' Bait? The stronger your web, the less likely you are to get blown out by this card. Duel actually cares more about web tightness than Reins does, because any long connections (such as the Elf to Elemental path described above) are like chinks in your armor, opening you up to the dreaded two-for-one.


### Assassins Treed


This is a deck I recently drafted here at Wizards, and it's a great illustration of the principles I outlined above. One of my pet goals for each Limited format is to draft some absurd Johnny deck (the turbo-[Horde of Notions](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horde+of+Notions) and the [Mirror Entity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror+Entity) / [Ceaseless Searblades](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ceaseless+Searblades) / [Brion Stoutarm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brion+Stoutarm) combo deck are two recent ones from *Lorwyn*), so when *Morningtide* appeared with five crazy small-class supporting lords, I knew I had to go for each at least once. Finally, Assassins!







#### Assassins


##### 






![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)





[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (16)



1
[Jagged-Scar Archers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJagged-Scar%5D+%5BArchers%5D)


1
[Winnower Patrol](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWinnower%5D+%5BPatrol%5D)


2
[Game-Trail Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGame-Trail%5D+%5BChangeling%5D)


1
[Lys Alana Huntmaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D)


1
[Imperious Perfect](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D)


2
[Woodland Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BChangeling%5D)


1
[Skeletal Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BChangeling%5D)


1
[Scarblade Elite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarblade%5D+%5BElite%5D)


2
[Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BScarblade%5D)


1
[Weed-Pruner Poplar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWeed-Pruner%5D+%5BPoplar%5D)


1
[Offalsnout](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOffalsnout%5D)


2
[Dreamspoiler Witches](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreamspoiler%5D+%5BWitches%5D)



##### Instant (1)



1
[Earthbrawn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarthbrawn%5D)



##### Land (18)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


9
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)



##### Other (4)



1
Nath’s Elite


3
Eyeblight’s Ending



##### Tribal instant (1)



1
[Gilt-Leaf Ambush](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilt-Leaf%5D+%5BAmbush%5D)


40 Cards 


##### Sideboard (23)



1
[Kinsbaile Skirmisher](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinsbaile%5D+%5BSkirmisher%5D)


1
[Deeptread Merrow](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeeptread%5D+%5BMerrow%5D)


1
[Inkfathom Divers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BDivers%5D)


1
[Latchkey Faerie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLatchkey%5D+%5BFaerie%5D)


1
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
Thieves’ Fortune


1
[Waterspout Weavers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BWeavers%5D)


1
[Exiled Boggart](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExiled%5D+%5BBoggart%5D)


1
[Fodder Launch](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFodder%5D+%5BLaunch%5D)


1
[Nightshade Schemers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightshade%5D+%5BSchemers%5D)


1
[Prowess of the Fair](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BProwess%5D+%5Bof%5D+%5Bthe%5D+%5BFair%5D)


1
[Revive the Fallen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevive%5D+%5Bthe%5D+%5BFallen%5D)


1
[Flamekin Brawler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D)


1
[Soulbright Flamekin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D)


1
[Deglamer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeglamer%5D)


2
[Elvish Eulogist](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D)


1
[Heritage Druid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeritage%5D+%5BDruid%5D)


3
[Lammastide Weave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLammastide%5D+%5BWeave%5D)


1
[Warren-Scourge Elf](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarren-Scourge%5D+%5BElf%5D)


1
[Woodland Guidance](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BGuidance%5D)




##### White (1)



1
[Kinsbaile Skirmisher](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinsbaile%5D+%5BSkirmisher%5D)



##### Blue (5)



1
[Deeptread Merrow](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeeptread%5D+%5BMerrow%5D)


1
[Inkfathom Divers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BDivers%5D)


1
[Latchkey Faerie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLatchkey%5D+%5BFaerie%5D)


1
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
[Waterspout Weavers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BWeavers%5D)



##### Black (13)



1
[Skeletal Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BChangeling%5D)


1
[Scarblade Elite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarblade%5D+%5BElite%5D)


2
[Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BScarblade%5D)


1
[Weed-Pruner Poplar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWeed-Pruner%5D+%5BPoplar%5D)


1
[Offalsnout](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOffalsnout%5D)


2
[Dreamspoiler Witches](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreamspoiler%5D+%5BWitches%5D)


1
[Exiled Boggart](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExiled%5D+%5BBoggart%5D)


1
[Fodder Launch](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFodder%5D+%5BLaunch%5D)


1
[Nightshade Schemers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightshade%5D+%5BSchemers%5D)


1
[Prowess of the Fair](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BProwess%5D+%5Bof%5D+%5Bthe%5D+%5BFair%5D)


1
[Revive the Fallen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevive%5D+%5Bthe%5D+%5BFallen%5D)



##### Red (2)



1
[Flamekin Brawler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D)


1
[Soulbright Flamekin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D)



##### Green (19)



1
[Jagged-Scar Archers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJagged-Scar%5D+%5BArchers%5D)


1
[Winnower Patrol](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWinnower%5D+%5BPatrol%5D)


2
[Game-Trail Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGame-Trail%5D+%5BChangeling%5D)


1
[Lys Alana Huntmaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D)


1
[Imperious Perfect](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D)


2
[Woodland Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BChangeling%5D)


1
[Gilt-Leaf Ambush](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilt-Leaf%5D+%5BAmbush%5D)


1
[Earthbrawn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarthbrawn%5D)


1
[Deglamer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeglamer%5D)


2
[Elvish Eulogist](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D)


1
[Heritage Druid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeritage%5D+%5BDruid%5D)


3
[Lammastide Weave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLammastide%5D+%5BWeave%5D)


1
[Warren-Scourge Elf](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarren-Scourge%5D+%5BElf%5D)


1
[Woodland Guidance](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BGuidance%5D)



##### Colorless (23)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


9
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


1
Nath’s Elite


3
Eyeblight’s Ending


1
Thieves’ Fortune


63 Cards 



#####  (5)



1
Nath’s Elite


3
Eyeblight’s Ending


1
Thieves’ Fortune



##### 1 (4)



1
[Flamekin Brawler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D)


2
[Elvish Eulogist](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D)


1
[Heritage Druid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeritage%5D+%5BDruid%5D)



##### 2 (17)



2
[Woodland Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BChangeling%5D)


1
[Skeletal Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BChangeling%5D)


1
[Scarblade Elite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarblade%5D+%5BElite%5D)


1
[Earthbrawn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarthbrawn%5D)


1
[Kinsbaile Skirmisher](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinsbaile%5D+%5BSkirmisher%5D)


1
[Deeptread Merrow](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeeptread%5D+%5BMerrow%5D)


1
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
[Exiled Boggart](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExiled%5D+%5BBoggart%5D)


1
[Prowess of the Fair](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BProwess%5D+%5Bof%5D+%5Bthe%5D+%5BFair%5D)


1
[Revive the Fallen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevive%5D+%5Bthe%5D+%5BFallen%5D)


1
[Soulbright Flamekin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D)


1
[Deglamer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeglamer%5D)


3
[Lammastide Weave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLammastide%5D+%5BWeave%5D)


1
[Warren-Scourge Elf](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarren-Scourge%5D+%5BElf%5D)



##### 3 (7)



1
[Jagged-Scar Archers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJagged-Scar%5D+%5BArchers%5D)


1
[Winnower Patrol](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWinnower%5D+%5BPatrol%5D)


1
[Imperious Perfect](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D)


2
[Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BScarblade%5D)


1
[Offalsnout](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOffalsnout%5D)


1
[Gilt-Leaf Ambush](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilt-Leaf%5D+%5BAmbush%5D)



##### 4 (6)



1
[Lys Alana Huntmaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D)


2
[Dreamspoiler Witches](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreamspoiler%5D+%5BWitches%5D)


1
[Latchkey Faerie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLatchkey%5D+%5BFaerie%5D)


1
[Fodder Launch](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFodder%5D+%5BLaunch%5D)


1
[Woodland Guidance](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BGuidance%5D)



##### 5 (6)



2
[Game-Trail Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGame-Trail%5D+%5BChangeling%5D)


1
[Weed-Pruner Poplar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWeed-Pruner%5D+%5BPoplar%5D)


1
[Inkfathom Divers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BDivers%5D)


1
[Waterspout Weavers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BWeavers%5D)


1
[Nightshade Schemers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightshade%5D+%5BSchemers%5D)


45 Cards 



##### Common (47)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


9
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


1
Nath’s Elite


1
[Winnower Patrol](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWinnower%5D+%5BPatrol%5D)


2
[Game-Trail Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGame-Trail%5D+%5BChangeling%5D)


1
[Lys Alana Huntmaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D)


2
[Woodland Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BChangeling%5D)


1
[Skeletal Changeling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BChangeling%5D)


1
[Weed-Pruner Poplar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWeed-Pruner%5D+%5BPoplar%5D)


2
[Dreamspoiler Witches](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreamspoiler%5D+%5BWitches%5D)


3
Eyeblight’s Ending


1
[Gilt-Leaf Ambush](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilt-Leaf%5D+%5BAmbush%5D)


1
[Earthbrawn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarthbrawn%5D)


1
[Kinsbaile Skirmisher](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinsbaile%5D+%5BSkirmisher%5D)


1
[Deeptread Merrow](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeeptread%5D+%5BMerrow%5D)


1
[Inkfathom Divers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BDivers%5D)


1
[Latchkey Faerie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLatchkey%5D+%5BFaerie%5D)


1
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
Thieves’ Fortune


1
[Exiled Boggart](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExiled%5D+%5BBoggart%5D)


1
[Flamekin Brawler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D)


1
[Soulbright Flamekin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D)


1
[Deglamer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeglamer%5D)


2
[Elvish Eulogist](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D)


1
[Warren-Scourge Elf](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarren-Scourge%5D+%5BElf%5D)



##### Uncommon (15)



1
[Jagged-Scar Archers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJagged-Scar%5D+%5BArchers%5D)


1
[Imperious Perfect](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D)


2
[Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BScarblade%5D)


1
[Offalsnout](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOffalsnout%5D)


1
[Waterspout Weavers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BWeavers%5D)


1
[Fodder Launch](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFodder%5D+%5BLaunch%5D)


1
[Nightshade Schemers](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightshade%5D+%5BSchemers%5D)


1
[Prowess of the Fair](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BProwess%5D+%5Bof%5D+%5Bthe%5D+%5BFair%5D)


1
[Revive the Fallen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevive%5D+%5Bthe%5D+%5BFallen%5D)


1
[Heritage Druid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeritage%5D+%5BDruid%5D)


3
[Lammastide Weave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLammastide%5D+%5BWeave%5D)


1
[Woodland Guidance](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BGuidance%5D)



##### Rare (1)



1
[Scarblade Elite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarblade%5D+%5BElite%5D)


63 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

















  
When I opened the *Morningtide* booster, I saw two definite first-pick possibilities: [Winnower Patrol](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winnower+Patrol) and [Scarblade Elite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scarblade+Elite). Going into the pack, I had a whopping five Assassins already as Elite-food—the two [Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lys+Alana+Scarblade)s that I had successfully long-ranged, and three changelings—but I had thirteen Elves to trigger the Patrol.


If we refer back to the tables I gave above, thirteen Elves puts me at about one trigger in half my games for [Winnower Patrol](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winnower+Patrol). Is a 4/3 for ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) with a relevant creature type as good as the allure of multiple [Dark Banishing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing)s? Although by the end of *Morningtide* I might be able to beef up my Elf and/or Warrior count enough that expected kinship trigger number up to two or higher, I'd rather select a card which has a much greater potential impact if I do indeed only get one use out of it.


I decided at the time that the additional power of the Assassin's effect, especially the one-two punch of discarding a changeling to Lys-Alana Scarblade and then reusing it with the Elite, was worth passing on a chance for insane multiple kinship draws—especially with more Warriors likely on the way in this booster. I kept my eye out for future changelings to power up the Elite and even found another "real" Assassin in the [Weed-Pruner Poplar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weed-Pruner+Poplar).


You can also see two interesting deckbuilding choices I made. One is fairly straightforward: the inclusion of two totally off-tribe [Dreamspoiler Witches](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dreamspoiler+Witches) due to their raw power and great synergy with the instants I had drafted. This brought up a side question of whether I should play [Nightshade Schemers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightshade+Schemers) as another kinship-like effect, due to the large number of changelings, but I quickly dismissed that option due to the huge number of 5 drops I had in my deck.


The second is a follow-on choice to that, a dilemma which I faced in adding in my final card: should I play something more powerful and subtly synergistic with those Witches and/or good on its own merits, or something more conservative and directly synergistic with the Elves I already had? I had four major tribal effects at work in Elves:


 


* [Lys Alana Scarblade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lys+Alana+Scarblade)
* [Jagged-Scar Archers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jagged-Scar+Archers)
* [Winnower Patrol](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winnower+Patrol)
* [Lys Alana Huntmaster](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lys+Alana+Huntmaster)

"Dave, you buffoon!" I can hear you thinking. (That's right, I can hear you thinking. Science!) "You didn't include [Imperious Perfect](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperious+Perfect) in your list of major tribal effects at work!" Checking back against my sideboard, though, the only possible fit for the slot here if I use an Elf is a dorky 1/1 Elf. And you know what you get if you combine a dorky 1/1 Elf with [Imperious Perfect](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperious+Perfect)? A dorky 2/2 Elf.


 



![Offalsnout](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Offalsnout)

The alternative was oft-maligned [Offalsnout](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Offalsnout). That's right: some sort of disturbing pig-monster. It had synergy with my Witches triggers, as a cheap instant (or instant blocker on their turn). However, the main reason I wanted ol' Offal was the fact that I could see his primary effects—being a Grey Ogre and giving me a bit of maindeck graveyard hate—as useful to round out my game plan. Sometimes you have to forgo topping out on synergy, as with the Elves here, and play cards that both stand up on their own merits and which shore up other pieces of your deck's strategy and/or combine to strengthen other paths you might need to take in Limited.

### The More You Know


I hope I've left you with a better understanding of how to assemble a crack strike force of Rogues, Elf Assassins, Spider Goats—whatever kins your tribe—in this brave new world of *Lorwyn* with *Morningtide*. Remember, these aren't rules set in stone (they're more like guidelines, really). Don't blindly follow the numbers, but instead let them factor into your decision making process when you draft and build your deck. If you guys have any questions, comments or thoughts on my writing, feel free to comment in the forums: web development of the forums is one of my primary responsibilities, so I'll be following the discussion. Thanks for reading!


### Math It Up


\*dons math hat\*


It's like a wizard hat, but less stars and more equations. We're about to get into some complex stuff, so hopefully only the most math-y (and least murderous) of you are reading this!


The initial problem question I thought up was:


 



> How is the Creature Type Web affected by a change in tribal count?


Considering my conception of the Creature Type Web is more of a qualitative concept than something that can be put directly into numbers, I backed off of this and considered just the kinship mechanic:


 



> How is the reliability of kinship affected by a change in tribal count? Specifically, are there interesting correlations between tribal count and kinship triggers?


To solve this problem analytically, I looked up [hypergeometic distribution](http://en.wikipedia.org/wiki/Hypergeometric_distribution), which gives an equation for determining various probabilities on drawing without replacement. However, this distribution could not account for the intricacies of when to play the kinship card, and considering the incremental effect of sequential triggers made my head hurt.


At this point, I decided to go with the scientist's mainstay: the [Monte Carlo method](http://en.wikipedia.org/wiki/Monte_Carlo_method), which would allow me to configure the scenario as one would play it in a goldfish-type situation, and then iterate a hojillion times to get a better estimate of the trends.


As I mentioned in my article, I made quite a few assumptions to simplify this scenario and allow these simulated games to complete without complex branching into many possible states. The results I found are still valid when applied to a real-game situation. One just needs to be aware of the differences between your game and the simulated one, and use those differences to estimate the effectiveness of the Monte Carlo results.


For those interested in the algorithm behind the simulated game, here's how it went down:


 


* Create a deck of 40 cards.
* T of them are tribal matches to the kinship in question.
* K of them are kinship cards (which of course match each other in this analysis).
* The rest are neither T or K.
* Randomize this deck and draw twenty times (representing a game of thirteen turns).
* Assume you make every land drop.
* Assume you play the kinship cards you draw at the first opportunity.
* Assume your kinship card remains in play the remainder of the game after you play it.
* Count up the number of triggers you would have before the game ends.

I varied T (the number of tribally relevant cards in the deck) of between 1 and 15, with the assumption that 15 would be close to maxing out your creature count. Your results would be better if you played fewer lands and more matching creatures of the relevant type, and they would be better if you played tribal spells such as [Eyeblight's Ending](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyeblight%27s+Ending) or [Veteran's Armaments](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Veteran%27s+Armaments).


I varied K (the number of kinship cards in the deck) between 1 and 5. To simplify things, and to allow us to visualize the results at all, multiple kinship cards in play are treated as a multiplier to the effect. This is true in most, but not all, of the kinship cards' cases, such as Pyroclast Council (where two triggers would kill both) or [Squeaking Pie Grubfellows](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squeaking+Pie+Grubfellows) (where two triggers might be giving away information for free if they have only one card in hand). At the very least, the option to trigger twice increases value.


There are plenty of library manipulation effects you could use to increase the chances of the top card matching, especially in *Lorwyn* / *Morningtide* Limited, including clash, Harbingers, and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder). So keep those in mind when applying these results to your own Draft and Sealed experience!








