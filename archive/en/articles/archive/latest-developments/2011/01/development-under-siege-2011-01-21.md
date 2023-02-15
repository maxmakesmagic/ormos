
---
[Link to Wayback Machine](https://web.archive.org/web/20211017184527/https://magic.wizards.com/en/articles/archive/latest-developments/development-under-siege-2011-01-21)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Hello, and welcome back to the first week of Mirrodin Besieged previews. First, I'll introduce you to the development team. Erik Lauer I seem to be getting tons of opportunities to talk about Erik these days, as just two weeks ago I told you that he was the lead designer of Masters Edition IV. Erik is a busy man, though, as he spends lots of time developing paper sets too."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "687006"
[_metadata_:publish_date]:- "2011-01-21"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Development Under Siege"
[_metadata_:wayback_capture_timestamp]:- "2021-10-17 18:45:27"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211017184527id_/https://magic.wizards.com/en/articles/archive/latest-developments/development-under-siege-2011-01-21"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/development-under-siege-2011-01-21"
---


Development Under Siege
=======================



 Posted in **Latest Developments**
 on January 21, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







Hello, and welcome back to the first week of *Mirrodin Besieged* previews. First, I'll introduce you to the development team.


### Erik Lauer


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)I seem to be getting tons of opportunities to talk about Erik these days, as [just two weeks ago](/en/articles/archive/latest-developments/time-traveling-2011-01-07) I told you that he was the lead designer of *Masters Edition IV*. Erik is a busy man, though, as he spends lots of time developing paper sets too. Erik led the development of *Mirrodin Besieged*, which is the eleventh major set in a row that he has been part of the development team for. That's one hell of a run, and represents an enormous collected bank of **Magic** knowledge. He put that knowledge to good use while working on this set.


Erik has since taken over responsibility for the Future Future League, which tests the Standard environment as it will exist when sets leave Wizards and enter the real world. I've been enjoying his vision for Standard more and more internally, and you'll begin to see that vision with *Mirrodin Besieged*.


### Tom LaPille


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_tom.jpg)You've seen Tom's work on **Magic** a few times before, as he was on the development teams for ***Magic** 2010*, *Worldwake*, and ***Magic** 2011*, and he was the lead developer of *Masters Edition III*, *Archenemy*, and *Masters Edition IV*. You will continue to see his work in the near future, as he was on both *Mirrodin Besieged* and "Action" on the path to his first set lead on ***Magic** 2012*. He is also very handsome. Finally, he writes this column, and likely should move on before further embarrassing himself. If you wish to learn more about him, you have only to read the [archives](http://www.wizards.com/magic/magazine/Archive.aspx?tag=Latest%20Developments&description=Latest%20Developments) of this column.


### Mike Turian


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_miketurian.jpg)Pro Tour Hall of Famer Mike Turian has led four **Magic** sets: *Future Sight*, *Morningtide*, *Conflux*, and *Scars of Mirrodin*. We like to have an experienced developer on each **Magic** team who isn't the set's lead, as the combination of experience and increased distance from the product can allow that person to see things that the lead can't. From my experience leading *Archenemy* and ***Magic** 2012*, I know that Mike does an excellent job in this role. His perspective on **Magic** is quite different from other developers', and the combination of experience and idea diversity that he brings is invaluable.


Mike has since moved from R&D to Organized Play, where he is putting his several years of experience playing in **Magic** tournaments to just as good use as he did in R&D.


### Ryan Dhuse


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_ryan.jpg)Ryan is a software architect for **Magic Online**, and has worked on **Magic Online** in various capacities for quite a while. He is also one of the more avid drafters I know who has no lifetime Pro points, and that's what earned him his spot on this development team. The *Mirrodin Besieged* team was Ryan's first, and although **Magic Online** occupied much of his time during our development cycle, we were glad to have the guidance we got from his love of Limited play.


### Joe Huber


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_joe.jpg)Joe Huber is a digital game designer. At the time he was a contractor, but he has since been hired full-time to work on digital products and new business. He was with us for a few weeks as we began. Eventually, though, his time became too crunched, and something had to give. He was removed from the *Mirrodin Besieged* team. His replacement was ...


### Zac Hill


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_zachill.jpg)I said two weeks ago that "Action" was Zac's first development team. I was wrong; I forgot this one! Zac joined this team not too long after joining Wizards, which happened just after a Top 8 performance at Pro Tour–Honolulu in 2009. Since then, Zac has grown as a developer very quickly, with his expertise especially felt in the Future Future League. I suspect it won't be too much longer before you see an announcement of a **Magic** set that he leads.


### About *Mirrodin Besieged*


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_mbsLogo.jpg)*Scars of Mirrodin* block is an artifact block, and so, of course, *Mirrodin Besieged* contains plenty of artifacts. Some of them are pretty good.


As a developer, it's my job to get nervous when we print a bunch of powerful colorless cards. One of the important ways that we balance the game is color requirements. Let's travel now to a hypothetical world one month from now in which a black-based infect deck is very strong in Standard. Between Inkmoth Nexus, Phyrexian Crusader, and Phyrexian Vatmother (all from the [Visual Spoiler](http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/mirrodinbesieged/spoiler)), such a deck has plenty of new options coming in, but let's pretend that all twelve (4 copies of each of the three previously listed cards) end up being correct in that deck. Because the deck's black requirements are so heavy, it's tricky to sneak other colors into the deck. It may be possible to add blue thanks to [Drowned Catacomb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowned+Catacomb), [Darkslick Shores](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darkslick+Shores), and [Creeping Tar Pit](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Creeping+Tar+Pit), but adding white is going to be tough because the format only has [Marsh Flats](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh+Flats) to offer. This keeps the deck heavily based in black so that it can cast its early-game cards that cost two black mana.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_3Cards1.jpg)If that deck is strong, one way to attack it is to play a bunch of cards that are explicitly good against black. Mirran Crusader, for example, may be frustrating for that deck to deal with unless it splashes red for burn, which awkwardly doesn't help its main plan. One can also play cards that are strategically good against an infect deck. For example, one might decide that creatures with infect have lower power for their cost than creatures without, and therefore play a bunch of planeswalkers against the infect deck. Black doesn't have cards that are great at killing planeswalkers that fit naturally into an Infect strategy, so this is likely to work to some degree.


Imagine instead that Phyrexian Crusader and Phyrexian Vatmother are artifacts. If that were true, an infect deck containing them would have very easy mana requirements and have little trouble going to any color necessary to adjust to metagame problems. That's trouble, because then that deck, if too powerful, will sit monolithically on top of everything else with no chance for something to move it off the top of the mountain.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld126_steel.jpg)As you may have noticed, *Mirrodin Besieged* adds even more strong artifacts to Standard. Between [Etched Champion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Etched+Champion), [Memnite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memnite), Signal Pest, Phyrexian Revoker, [Steel Overseer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+Overseer), [Mox Opal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Opal), and [Tempered Steel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tempered+Steel), there's probably some kind of artifact rush deck out there in Standard now. As it turned out, there wasn't an "artifact deck" in competitive Standard before *Mirrodin Besieged*. However, that doesn't mean that the world has not seen the sort of deck that [Mox Opal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Opal), [Memnite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memnite), and [Steel Overseer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+Overseer) can produce. At last year's World Championships, Jonathan Smithers unleashed this deck on the Extended portion of the event with impressive results for almost everyone who played it.








#### Jonathan Smithers's Steel Artifact


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (27)



4
[Court Homunculus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHomunculus%5D)


2
[Etched Champion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEtched%5D+%5BChampion%5D)


4
[Master of Etherium](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BEtherium%5D)


4
[Memnite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D)


2
[Ornithopter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D)


3
[Ranger of Eos](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRanger%5D+%5Bof%5D+%5BEos%5D)


4
[Steel Overseer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BOverseer%5D)


4
[Tidehollow Sculler](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidehollow%5D+%5BSculler%5D)



##### Sorcery (4)



4
[Thoughtseize](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### Artifact (8)



3
[Mox Opal](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BOpal%5D)


3
[Springleaf Drum](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpringleaf%5D+%5BDrum%5D)


2
[Thopter Foundry](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThopter%5D+%5BFoundry%5D)



##### Enchantment (4)



4
[Tempered Steel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTempered%5D+%5BSteel%5D)



##### Land (17)



4
[Darkslick Shores](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDarkslick%5D+%5BShores%5D)


1
[Fetid Heath](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFetid%5D+%5BHeath%5D)


4
[Marsh Flats](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D)


3
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


4
[Seachrome Coast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeachrome%5D+%5BCoast%5D)


1
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


60 Cards 


##### Sideboard (15)



1
[Ranger of Eos](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRanger%5D+%5Bof%5D+%5BEos%5D)


2
[Burrenton Forge-Tender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurrenton%5D+%5BForge-Tender%5D)


3
[Celestial Purge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D)


2
[Disfigure](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D)


1
[Duress](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)


3
[Ethersworn Canonist](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthersworn%5D+%5BCanonist%5D)


3
[Leonin Arbiter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BArbiter%5D)




##### White (23)



4
[Court Homunculus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHomunculus%5D)


4
[Ranger of Eos](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRanger%5D+%5Bof%5D+%5BEos%5D)


4
[Tempered Steel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTempered%5D+%5BSteel%5D)


2
[Burrenton Forge-Tender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurrenton%5D+%5BForge-Tender%5D)


3
[Celestial Purge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D)


3
[Ethersworn Canonist](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthersworn%5D+%5BCanonist%5D)


3
[Leonin Arbiter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BArbiter%5D)



##### Blue (4)



4
[Master of Etherium](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BEtherium%5D)



##### Black (7)



4
[Thoughtseize](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


2
[Disfigure](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D)


1
[Duress](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)



##### Multi colored (6)



4
[Tidehollow Sculler](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidehollow%5D+%5BSculler%5D)


2
[Thopter Foundry](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThopter%5D+%5BFoundry%5D)



##### Colorless (35)



4
[Darkslick Shores](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDarkslick%5D+%5BShores%5D)


1
[Fetid Heath](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFetid%5D+%5BHeath%5D)


4
[Marsh Flats](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D)


3
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


4
[Seachrome Coast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeachrome%5D+%5BCoast%5D)


1
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


2
[Etched Champion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEtched%5D+%5BChampion%5D)


4
[Memnite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D)


2
[Ornithopter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D)


4
[Steel Overseer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BOverseer%5D)


3
[Mox Opal](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BOpal%5D)


3
[Springleaf Drum](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpringleaf%5D+%5BDrum%5D)


75 Cards 



##### 1 (16)



4
[Court Homunculus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHomunculus%5D)


3
[Springleaf Drum](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpringleaf%5D+%5BDrum%5D)


4
[Thoughtseize](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


2
[Burrenton Forge-Tender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurrenton%5D+%5BForge-Tender%5D)


2
[Disfigure](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D)


1
[Duress](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)



##### 2 (19)



4
[Steel Overseer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BOverseer%5D)


4
[Tidehollow Sculler](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidehollow%5D+%5BSculler%5D)


2
[Thopter Foundry](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThopter%5D+%5BFoundry%5D)


3
[Celestial Purge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D)


3
[Ethersworn Canonist](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthersworn%5D+%5BCanonist%5D)


3
[Leonin Arbiter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BArbiter%5D)



##### 3 (10)



2
[Etched Champion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEtched%5D+%5BChampion%5D)


4
[Master of Etherium](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BEtherium%5D)


4
[Tempered Steel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTempered%5D+%5BSteel%5D)



##### 4 (4)



4
[Ranger of Eos](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRanger%5D+%5Bof%5D+%5BEos%5D)


49 Cards 



##### Common (17)



3
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Court Homunculus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHomunculus%5D)


4
[Tidehollow Sculler](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidehollow%5D+%5BSculler%5D)


4
[Thoughtseize](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


1
[Duress](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)



##### Uncommon (18)



4
[Memnite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D)


2
[Ornithopter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D)


3
[Springleaf Drum](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpringleaf%5D+%5BDrum%5D)


2
[Thopter Foundry](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThopter%5D+%5BFoundry%5D)


2
[Burrenton Forge-Tender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurrenton%5D+%5BForge-Tender%5D)


3
[Celestial Purge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D)


2
[Disfigure](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D)



##### Rare (29)



1
[Fetid Heath](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFetid%5D+%5BHeath%5D)


4
[Marsh Flats](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D)


2
[Etched Champion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEtched%5D+%5BChampion%5D)


4
[Master of Etherium](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BEtherium%5D)


4
[Ranger of Eos](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRanger%5D+%5Bof%5D+%5BEos%5D)


4
[Steel Overseer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BOverseer%5D)


4
[Tempered Steel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTempered%5D+%5BSteel%5D)


3
[Ethersworn Canonist](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthersworn%5D+%5BCanonist%5D)


3
[Leonin Arbiter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BArbiter%5D)



##### Mythic (11)



4
[Darkslick Shores](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDarkslick%5D+%5BShores%5D)


4
[Seachrome Coast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeachrome%5D+%5BCoast%5D)


3
[Mox Opal](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BOpal%5D)


75 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Darkslick+Shores)


















 

As more and more artifacts enter Standard from *Mirrodin Besieged* and "Action," I expect decks like this to start showing up in Standard more often. When they do, we want there to be answers. In "[Twitstorm Part 2: Scars of Twitstorm](/en/articles/archive/latest-developments/twitstorm-part-2-scars-twitstorm-2010-10-01)", I talked about the need for answers of this sort, but said that we didn't want to give out the nuclear codes quite yet, as we wanted there to be some amount of time during which playing out a bunch of artifacts was safe.


That time has passed. Here are the codes.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/mbs/eg6kcq43u0_en.jpg)I don't have any particularly awesome development stories about this card. We realized that we needed a mass artifact destruction effect, decided that it should go in green instead of red because it makes more sense for Phryexians to be going after Mirran artifacts than for red Mirrans to be sabotaging themselves, and typed the card into Multiverse. Erik's playtest names are known for their directness; for this card, he chose the name "Crush." Unfortunately, he chose a name so well that that name ended up on a different *Mirrodin Besieged* card. This caused no end of problems for us within R&D during FFL meetings, when no one was certain which "Crush" anyone was talking about. It was even worse that the cards had similar purposes!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/iuyftryghsfgf.jpg)Before I go, I would like to touch on this card's rarity. Creeping Corrosion is rare because the world in which this is an uncommon is not a happy one. Conditional mass removal like [Pyroclasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm) or [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout) can be uncommon, but we don't want Limited players living in fear of unconditional sweepers all the time. In an artifact set, Creeping Corrosion is much more like [Day of Judgment](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) than [Pyroclasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm) or [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout). Therefore, it needs to be a rare.


 [![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/MBS_Pre_ArticleBaner.jpg)](http://www.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prerelease-facts)
Next weekend is the *Mirrodin Besieged* prerelease. We're trying something new this time; as you may have read elsewhere, you'll choose "Mirran" or "Phyrexian" at the beginning of the tournament, and all your *Mirrodin Besieged* cards will come from the faction you choose. That has several non-obvious effects. One of them is that because more of the cards in your pool will be playable in a deck built around the faction you choose, the average deck quality in the Prerelease will be somewhat higher than you've seen at a Prerelease before. There are several other impacts, but I leave those for you to discover yourself. I think this will be an interesting experiment, and I look forward to learning about how it goes for everyone else.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/boab/boab126_booster.jpg)### Last Week's Poll




| **Which of last year's draft formats was your favorite?** |
| --- |
| *Rise-Rise-Rise* | 2192 | 34.5% |
| M11-M11-M11 | 1544 | 24.3% |
| *Zendikar-Zendikar-Worldwake* | 981 | 15.5% |
| I don't have an opinion. | 950 | 15.0% |
| *Zendikar-Zendikar-Zendikar* | 679 | 10.7% |
| **Total** | **6346** | **100.0%** |

  

 





