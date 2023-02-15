
---
[Link to Wayback Machine](https://web.archive.org/web/20210429041046/https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03)

[_metadata_:author]:- "Erik Lauer"
[_metadata_:description]:- "Wait a minute (you might find yourself wondering), what’s a new article doing on the site today? Isn't Wizards out of the office for the Independence Day holiday? Indeed we are, but we couldn't take the day completely off—not when there are cards to preview! Below, developer Erik Lauer fills in for Tom LaPille (who was busy writing this week's feature article). Erik has a"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646666"
[_metadata_:publish_date]:- "2009-07-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing an Answer"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 04:10:46"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429041046id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03"
---


Developing an Answer
====================



 Posted in **Latest Developments**
 on July 3, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_eriklauer.jpg)
By Erik Lauer




Erik Lauer is a senior game designer who works on final game design and development. Recently, he has led the Return to Ravnica, Modern Masters, and Theros development teams. 






*Wait a minute (you might find yourself wondering), what’s a new article doing on the site today? Isn't Wizards out of the office for the Independence Day holiday? Indeed we are, but we couldn't take the day completely off—not when there are cards to preview! Below, developer Erik Lauer fills in for Tom LaPille (who was busy writing [this week's feature article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/45)). Erik has a preview card for you, plus a brief look at how that card came to be. Enjoy!*

Kelly Digges  
 Daily MTG Editor, **magicthegathering.com**

The ***Magic** 2010* design team created an excellent set that captured the feel of **Magic**'s first card set, Alpha, and enriched it with years of experience in card design. The set has many cards that each give a translation of a single piece of fantasy into a viable **Magic** card. The development team balanced these cards, and the set as a whole, for a variety of play environments from Limited and casual play up to cutthroat competitive play.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld45_2010.jpg)  
Sometimes the development team changed the sets in other ways. One day we were looking at reducing the wordiness of commons to make a greater contrast with some of the wordy rares. We had ten common vanilla creatures total, roughly two per color, and I asked Randy Buehler what he thought about that. Randy walked over to a framed set of the "Beta" card set we have on the wall, and we counted out: [Pearled Unicorn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pearled+Unicorn), [Merfolk of the Pearl Trident](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+of+the+Pearl+Trident), [Mons's Goblin Raiders](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mons%27s+Goblin+Raiders), [Grey Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grey+Ogre), [Hurloon Minotaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurloon+Minotaur), [Hill Giant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hill+Giant), [Scathe Zombies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scathe+Zombies), [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears), [Ironroot Treefolk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironroot+Treefolk), and [Craw Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craw+Wurm). With a chuckle, Randy approved.

Today's preview card isn't one of those vanilla commons, but for a rare, it isn't very wordy either. Here it is:

![Great Sable Stag](https://media.magic.wizards.com/image_legacy_migration/mtg/images/tcg/products/magic2010/direc18apt_EN.jpg)  
You might wonder why we chose to print such a powerful hoser.

Blue-black decks have been powerful in Standard for years. At Worlds 2006 Guillaume Wafo-Tapa played Dralnu du Louvre with great success. After [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) was printed, lists such as this one from Frank Karsten became very popular.

![Damnation](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Damnation)  






#### Frank Karsten's Dralnu Control


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (6)



1
[Dralnu, Lich Lord](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D)


1
[Skeletal Vampire](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D)


1
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


3
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)



##### Sorcery (3)



3
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)



##### Instant (25)



3
[Mana Leak](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D)


4
[Remand](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D)


2
[Repeal](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D)


4
[Rewind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D)


1
[Seize the Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D)


2
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


3
[Spell Snare](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D)


1
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


1
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)



##### Land (26)



2
[Tolaria West](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D)


2
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Dimir Aqueduct](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D)


9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Watery Grave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


60 Cards 


##### Sideboard (15)



1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


3
[Bottle Gnomes](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D)


2
[Persecute](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


3
[Tormod's Crypt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


1
[Grim Harvest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


1
[Trickbind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D)




##### Blue (28)



1
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


3
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


3
[Mana Leak](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D)


4
[Remand](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D)


2
[Repeal](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D)


4
[Rewind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D)


2
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


3
[Spell Snare](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D)


1
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


1
[Trickbind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D)



##### Black (13)



1
[Skeletal Vampire](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D)


1
[Seize the Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


1
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Persecute](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


1
[Grim Harvest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)



##### Multi colored (1)



1
[Dralnu, Lich Lord](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D)



##### Colorless (33)



2
[Tolaria West](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D)


3
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Dimir Aqueduct](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D)


9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Watery Grave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


3
[Bottle Gnomes](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D)


3
[Tormod's Crypt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D)


75 Cards 



##### 1 (6)



2
[Repeal](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D)


3
[Spell Snare](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)



##### 2 (10)



3
[Mana Leak](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D)


4
[Remand](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D)


1
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


1
[Grim Harvest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D)


1
[Trickbind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D)



##### 3 (6)



2
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


3
[Bottle Gnomes](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D)



##### 4 (17)



4
[Rewind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D)


1
[Seize the Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D)


1
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


2
[Persecute](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)



##### 5 (5)



1
[Dralnu, Lich Lord](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D)


1
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


3
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)



##### 6 (1)



1
[Skeletal Vampire](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D)


45 Cards 



##### Common (29)



9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


3
[Mana Leak](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D)


4
[Remand](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D)


2
[Repeal](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D)


2
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


3
[Bottle Gnomes](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D)


1
[Grim Harvest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)



##### Uncommon (22)



1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Dimir Aqueduct](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


4
[Rewind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D)


1
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


3
[Spell Snare](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D)


1
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


3
[Tormod's Crypt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D)



##### Rare (17)



2
[Tolaria West](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D)


3
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Watery Grave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D)


1
[Dralnu, Lich Lord](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D)


1
[Skeletal Vampire](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D)


1
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


1
[Seize the Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D)


2
[Persecute](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


1
[Trickbind](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D)



##### Mythic (7)



3
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tolaria+West)

















  
At Worlds 2007, Kotaro Otsuka also has success with a blue-black deck, this time using evoke creatures alongside [Makeshift Mannequin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) and [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command).







#### Kotaro Otsuka's Blue-Black Control


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (23)



4
[Epochrasite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D)


4
[Mulldrifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D)


3
[Phyrexian Ironfoot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D)


4
[Riftwing Cloudskate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D)


4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


4
[Shriekmaw](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D)



##### Sorcery (2)



2
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)



##### Instant (7)



3
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


4
[Makeshift Mannequin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D)



##### Artifact (4)



1
[Loxodon Warhammer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D)


3
[Mind Stone](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D)



##### Land (24)



4
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


2
[Mouth of Ronom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D)


4
[River of Tears](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D)


5
[Snow-Covered Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D)


4
[Snow-Covered Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


60 Cards 


##### Sideboard (15)



2
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


2
[Liliana Vess](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D)


3
[Nameless Inversion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)


2
[Persuasion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D)


2
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)




##### Blue (13)



4
[Mulldrifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D)


4
[Riftwing Cloudskate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D)


3
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


2
[Persuasion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D)



##### Black (21)



4
[Shriekmaw](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


4
[Makeshift Mannequin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D)


2
[Liliana Vess](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D)


3
[Nameless Inversion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### Multi colored (4)



4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)



##### Colorless (37)



4
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


2
[Mouth of Ronom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D)


4
[River of Tears](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D)


5
[Snow-Covered Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D)


4
[Snow-Covered Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Epochrasite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D)


3
[Phyrexian Ironfoot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D)


1
[Loxodon Warhammer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D)


3
[Mind Stone](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D)


2
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


75 Cards 



##### 1 (6)



2
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### 2 (10)



4
[Epochrasite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D)


3
[Mind Stone](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D)


3
[Nameless Inversion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)



##### 3 (8)



3
[Phyrexian Ironfoot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D)


4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


1
[Loxodon Warhammer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D)



##### 4 (11)



3
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


4
[Makeshift Mannequin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D)



##### 5 (16)



4
[Mulldrifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D)


4
[Riftwing Cloudskate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D)


4
[Shriekmaw](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D)


2
[Liliana Vess](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D)


2
[Persuasion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D)


51 Cards 



##### Common (24)



5
[Snow-Covered Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D)


4
[Snow-Covered Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D)


4
[Mulldrifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D)


4
[Shriekmaw](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D)


3
[Nameless Inversion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### Uncommon (26)



4
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


2
[Mouth of Ronom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D)


3
[Phyrexian Ironfoot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D)


4
[Riftwing Cloudskate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D)


4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


4
[Makeshift Mannequin](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D)


3
[Mind Stone](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D)


2
[Persuasion](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D)



##### Rare (19)



4
[River of Tears](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Epochrasite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D)


3
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


1
[Loxodon Warhammer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D)


2
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)



##### Mythic (6)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


2
[Liliana Vess](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Conclave)

















  
At Worlds 2008, yet again blue-black decks were having a great deal of success. Five of the Top 8 players were playing Faeries including Antti Malin, the eventual world champion. 







#### Antti Malin's Blue-Black Faeries


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (12)



4
[Mistbind Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D)


2
[Sower of Temptation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D)


4
[Spellstutter Sprite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D)


2
[Vendilion Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D)



##### Sorcery (4)



4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### Instant (15)



4
[Agony Warp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D)


3
[Broken Ambitions](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D)


4
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


3
[Remove Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D)


1
[Terror](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D)



##### Enchantment (4)



4
[Bitterblossom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D)



##### Land (25)



1
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


6
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


4
[Secluded Glen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D)


4
[Sunken Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


60 Cards 


##### Sideboard (15)



1
[Sower of Temptation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D)


4
[Flashfreeze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D)


2
[Glen Elendra Archmage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D)


4
[Infest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D)


2
[Jace Beleren](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D)


1
[Mind Shatter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D)


1
[Ponder](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D)




##### Blue (32)



4
[Mistbind Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D)


3
[Sower of Temptation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D)


4
[Spellstutter Sprite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D)


2
[Vendilion Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D)


3
[Broken Ambitions](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D)


4
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


3
[Remove Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D)


4
[Flashfreeze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D)


2
[Glen Elendra Archmage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D)


2
[Jace Beleren](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D)


1
[Ponder](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D)



##### Black (14)



4
[Bitterblossom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D)


1
[Terror](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


4
[Infest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D)


1
[Mind Shatter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D)



##### Multi colored (4)



4
[Agony Warp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D)



##### Colorless (25)



1
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


6
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


4
[Secluded Glen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D)


4
[Sunken Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


75 Cards 



##### 1 (8)



3
[Broken Ambitions](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


1
[Ponder](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D)



##### 2 (21)



4
[Spellstutter Sprite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D)


4
[Agony Warp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D)


4
[Bitterblossom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D)


3
[Remove Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D)


1
[Terror](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D)


4
[Flashfreeze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D)


1
[Mind Shatter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D)



##### 3 (8)



2
[Vendilion Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D)


4
[Infest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D)


2
[Jace Beleren](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D)



##### 4 (13)



4
[Mistbind Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D)


3
[Sower of Temptation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D)


4
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


2
[Glen Elendra Archmage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D)


50 Cards 



##### Common (20)



6
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


2
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


3
[Broken Ambitions](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D)


3
[Remove Soul](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D)


1
[Terror](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


1
[Ponder](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D)



##### Uncommon (13)



1
[Faerie Conclave](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D)


4
[Agony Warp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D)


4
[Flashfreeze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D)


4
[Infest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D)



##### Rare (30)



4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


4
[Secluded Glen](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D)


4
[Underground River](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D)


4
[Mistbind Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D)


3
[Sower of Temptation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D)


4
[Spellstutter Sprite](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D)


4
[Cryptic Command](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D)


2
[Glen Elendra Archmage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D)


1
[Mind Shatter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D)



##### Mythic (12)



4
[Sunken Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D)


2
[Vendilion Clique](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D)


4
[Bitterblossom](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D)


2
[Jace Beleren](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Conclave)

















  
Standard currently has cards such as [Deathmark](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathmark) and [Celestial Purge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Celestial+Purge) to keep each allied-color pair from getting out of control. If blue-black decks are too strong, shouldn't green have a card that helps keep things in check? Not only did green have [Karplusan Strider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Strider), but it also got [Marshdrinker Giant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marshdrinker+Giant). While these cards punish blue and black, they just haven't proven strong enough to keep things in check.



|  |  |
| --- | --- |
| Celestial Purge | Karplusan Strider |

Paladin *en*-Vec is a card that has helped white. The card doesn't completely shut down black-red decks, but it is a thorn in their side. The development team set out to make a green card that would do similar things. While many of the cards in ***Magic** 2010* are based on high fantasy, this is more of a nuts-and-bolts type card. The creative team breathed life into once we were done and created a fantasy concept based on a mythical stag, but that's not how we made the card.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld45_mana.jpg)  
We started off with a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) creature with protection from blue and protection from black. We soon realized that if the card could be countered, it would not be particularly hard for the blue-black deck to deal with, so the card should have "can't be countered" as its third ability.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld45_textBox.jpg)  
The next issue was the creature's toughness. We knew Faeries would still be a strong Standard deck, and that this card would need to be useful against them. [Volcanic Fallout](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) is also useful against Faeries, so this card should work well in the same deck with Fallout. That means that the toughness must be at least 3. Since the card is supposed to have answers in other colors, we left the toughness at 3, making it vulnerable to [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt).

Finally we had to decide on the creature's power. We determined that 2 power was not enough to seriously threaten the Faerie deck, while 3 power was sufficient. The result is powerful, but fair, and as a 3/3 for three mana, it's aesthetically pleasing too.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld45_pt.jpg)  
We have Future Future League tournaments were we build decks in formats that will come out in the future. I decided to test the Stag by playing Faeries. It occurred to me that I could add another color, such as red for [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt). However I wanted to see how a blue-black deck would work. I figured [Vendilion Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique) would frequently come out too slowly to take Great Sable Stag from my opponent's hand, so I played [Thoughtseize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize). However, when my opponent was able to cast a Stag, I felt stepped on. I couldn't counter it, and there wasn't much I could do to it was it entered the battlefield. How unfair! Maybe I could race, possibly with a couple [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command)s to tap the Stag. The real hero was [Chameleon Colossus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chameleon+Colossus), who held the fort against the Stag while my [Sower of Temptation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sower+of+Temptation) pecked away!

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld45_stagSplash.jpg)  
After playing against the Stag, I could tell it was powerful, but not too powerful. It was a bit more than a thorn in my side, but it wasn't enough to make any matchup hopeless. The Stag was filling its role, and we look forward to seeing it do the same out in the real world.

[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/m10_Pre1.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prereleases)  






