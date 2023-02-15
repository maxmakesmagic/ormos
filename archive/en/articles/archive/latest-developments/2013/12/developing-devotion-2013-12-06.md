
---
[Link to Wayback Machine](https://web.archive.org/web/20210429042815/https://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06)

[_metadata_:author]:- "Adam Prosak"
[_metadata_:description]:- "Greetings Everyone! My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make Magic: The Gathering the best game it can be. However, one of the things I've missed during my time here is writing. I harassed Sam Stoddard enough, and he agreed to loan me his digital space for a week. Thanks Sam! The Devotion Mechanic Devotion"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646181"
[_metadata_:publish_date]:- "2013-12-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Devotion"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 04:28:15"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429042815id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06"
---


Developing Devotion
===================



 Posted in **Latest Developments**
 on December 6, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_adamprosak.jpg)
By Adam Prosak




From Friday Night Magic to the Pro Tour, Adam Prosak loves all types of tournament Magic. Currently, Adam is working in R&D as a developer. 







Greetings Everyone!


 My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make **Magic: The Gathering** the best game it can be. However, one of the things I've missed during my time here is writing. I harassed [Sam Stoddard](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard) enough, and he agreed to loan me his digital space for a week. Thanks Sam! 


### The Devotion Mechanic


 Devotion is a mechanic that scales endlessly. Nearly any X spell (such as [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball)) is a good example of a scaling spell. The amount of damage [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) deals is only limited by the amount of mana you are willing to spend. Scaling cards are interesting because they allow you to play different-powered effect depending on the state of the game. Like other scaling cards, cards with devotion are similarly unlimited. Instead of available mana, a card with devotion counts the mana symbols on your permanents. Devotion is different than most scaling mechanics because many of your cards can count multiple times toward your scaling mechanic. A creature that costs ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) counts for two devotion, so it is difficult to plan on a certain amount of devotion. This makes developing devotion cards very tricky, as we want cards to be fun in the most amount of situations possible. 




|  |  |
| --- | --- |
| Fireball | Agent of the Fates |

 Imagine for a second that [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) made 1/1 Elemental tokens rather than 1/0 tokens. If you have a large amount of devotion, [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) is incredibly difficult to beat. We decided to allow players to get around huge [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) by simply killing the [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) itself. Now, [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) is incredible with some highly devoted friends, but only if your opponent can't remove it. That is more fun than your opponent simply sitting there helpless regardless of whether or not he or she can remove the [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves). 


 On the other side of things, it is also important to make sure that cards with devotion are reasonable plays even if you don't have much (or any) devotion when you play them. [Fanatic of Mogis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis) is capable of dealing a large amount of damage, but only if you have heavy devotion. If you don't have that much devotion, playing a 4/2 for ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) isn't the worst thing in the world. We tried to make cards that were appealing enough to play even without optimal devotion. Sitting with a card in your hand all game because you can't get devotion going doesn't provide great game play, so we work to avoid those things. 




|  |  |
| --- | --- |
| Master of Waves | Fanatic of Mogis |

### Making a Card Weaker?


 When developing a card, generally we play around with a mana cost if we want to narrow the range of decks a particular card is played in. For example, if we find that a certain card that costs ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) is played in too many decks, we might change its casting cost to ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) to force it into more heavily green decks. 


 However, with devotion, a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) casting cost is often a benefit rather than a drawback compared to a card that costs ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). In a world of devotion, we have to balance the casting costs on cards differently. [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) itself had a mana cost of 2UU at one point. We actually weakened the card by making it easier to cast. 


###  Nykthos, Shrine to Nyx


 As *Theros* was released, one of development's biggest concerns about the cards concerned [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx). It has been quite some time since we've printed a land capable of making more than one mana, let alone a land that is capable of making a scaling amount of mana. [Tolarian Academy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy), [Gaea's Cradle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Cradle), and [Cabal Coffers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Coffers) are lands in a similar space to [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx)—and those lands are among the most powerful cards ever printed and not something we would want to repeat. 




|  |  |
| --- | --- |
| Nykthos, Shrine to Nyx | Gaea's Cradle |

 For most of development, [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) was not legendary. There was still a little bit of tension in the card—only tapping for colorless initially hurts when you want to cast [Boros Reckoner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner) or [Nightveil Specter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightveil+Specter) with [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) and two other lands. However, it was an auto include in many of our decks in spite of this. The legendary supertype was added, and all of the developers found ourselves wondering how many to add to our decks. 


 I am extremely happy with how [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) has played thus far. It is an exciting card, and one that is capable of fueling some truly exciting plays. It is great to make exciting cards that don't overshadow the excitement for other cards. I think that we put enough balances on the card to keep [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) from being excessively powerful. Much like our internal playtesting, deck builders all over the world have struggled with how many copies of [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) to put into their devotion decks. I've seen any number from zero to four do well at tournaments, and I think this is a great thing. 


### The Gods and Their Weapons


 The *Theros* Gods are all designed with a similar goal: they require five devotion to turn into creatures, and they have an effect that isn't really worth it unless you have the necessary devotion. For example, [Think Tank](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Think+Tank) isn't exactly the most impressive card, so much of the power in [Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea) is the potential to turn her into an oversized creature. 


 One of my favorite things about *Theros* is how each God has a weapon that plays well with it. First, each weapon provides two devotion. Counting the God itself as a third devotion symbol, you only need two more of the appropriate color devotion to turn your god into a fearsome creature. The part that I really enjoy is that the weapon's ability plays well with the god's ability. Take a look! 




|  |  |
| --- | --- |
| Heliod, God of the Sun | Spear of Heliod |

 Heliod makes tokens, while the [Spear of Heliod](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spear+of+Heliod) is there to give them all a boost. At one point, Heliod had a cheaper activation and made 1/1s. This conflicted with our goals to make the power in turning the God into a creature, so we changed the card into the ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif): 2/1 token you see today. 




|  |  |
| --- | --- |
| Thassa, God of the Sea | Bident of Thassa |

 Thassa's Bident gives you a reward for each of your creatures that get through for damage. What better ability to pair with the "[Thieving Magpie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thieving+Magpie)" ability than unblockability?! 




|  |  |
| --- | --- |
| Erebos, God of the Dead | Whip of Erebos |

 The whip gives all of your creatures lifelink, which boosts your life total. This allows you to be more aggressive when it comes to drawing cards with Erebos's ability. One of my favorite things about Erebos is that he turns off the lifelink from an opposing [Whip of Erebos](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whip+of+Erebos). Erebos doesn't like his weapons being used against him. 




|  |  |
| --- | --- |
| Purphoros, God of the Forge | Hammer of Purphoros |

 Much like [Heliod, God of the Sun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heliod%2C+God+of+the+Sun) and [Spear of Heliod](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spear+of+Heliod), the red combo provides a benefit for your creatures and a way to make extra creatures. However, this time the weapon makes the creatures while the God makes them stronger. I think it is interesting that both colors care about making lots of creatures, but each does it in its own way. Red sacrifices things (in this case, lands) and deals direct damage, while white is all about building up an overwhelming army of creatures. 




|  |  |
| --- | --- |
| Nylea, God of the Hunt | Bow of Nylea |

This is easily my favorite pair. I love that both of them individually help your creatures, which is something very green. Their combination is the most subtle, and one that is difficult to appreciate until you play with it. The combination of deathtouch and trample is very powerful—likely my favorite keyword interaction. If your opponent blocks your 5/5 with a single creatures, he or she will take 4 trample damage because 1 damage is lethal damage with deathtouch.


### Types of Devotion Decks


One of the most interesting things about Devotion is that it doesn't point you in a direction of how fast your deck wants to be. The only thing it really demands is that your deck has permanents. A faster devotion deck can flood the board with creatures and attempt to overwhelm an opponent. A slower devotion deck can use its permanents to slow down a game and take control. As the game goes longer, there are more likely to be more permanents in play, thus making the devotion card stronger.



[Pro Tour *Theros*](/en/events/coverage/dezani-proclaims-allez-les-bleus-pro-tour) was a perfect example of all of the various types of devotion decks. Devotion decks did incredibly well, and each of them had its own unique style. 


### Jérémy Dezani








#### Jérémy Dezani's Mono-Blue Devotion


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (2)



2
[Jace, Architect of Thought](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BArchitect%5D+%5Bof%5D+%5BThought%5D)



##### Creature (30)



4
[Cloudfin Raptor](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCloudfin%5D+%5BRaptor%5D)


4
[Frostburn Weird](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrostburn%5D+%5BWeird%5D)


4
[Judge's Familiar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJudge%5D+%5BFamiliar%5D)


4
[Master of Waves](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BWaves%5D)


4
[Nightveil Specter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightveil%5D+%5BSpecter%5D)


2
[Omenspeaker](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOmenspeaker%5D)


4
[Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThassa,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D)


4
[Tidebinder Mage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidebinder%5D+%5BMage%5D)



##### Instant (3)



2
[Cyclonic Rift](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)


1
[Disperse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisperse%5D)



##### Artifact (1)



1
[Bident of Thassa](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBident%5D+%5Bof%5D+%5BThassa%5D)



##### Land (24)



21
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


3
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


60 Cards 


##### Sideboard (15)



1
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


2
[Jace, Architect of Thought](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BArchitect%5D+%5Bof%5D+%5BThought%5D)


2
[Ætherling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86therling%5D)


3
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


2
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)


1
[Triton Tactics](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriton%5D+%5BTactics%5D)


3
[Wall of Frost](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BFrost%5D)




##### Blue (35)



4
[Cloudfin Raptor](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCloudfin%5D+%5BRaptor%5D)


4
[Master of Waves](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BWaves%5D)


2
[Omenspeaker](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOmenspeaker%5D)


4
[Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThassa,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D)


4
[Tidebinder Mage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidebinder%5D+%5BMage%5D)


1
[Bident of Thassa](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBident%5D+%5Bof%5D+%5BThassa%5D)


2
[Cyclonic Rift](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)


1
[Disperse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisperse%5D)


4
[Jace, Architect of Thought](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BArchitect%5D+%5Bof%5D+%5BThought%5D)


2
[Ætherling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86therling%5D)


3
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
[Triton Tactics](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriton%5D+%5BTactics%5D)


3
[Wall of Frost](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BFrost%5D)



##### Multi colored (12)



4
[Frostburn Weird](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrostburn%5D+%5BWeird%5D)


4
[Judge's Familiar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJudge%5D+%5BFamiliar%5D)


4
[Nightveil Specter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightveil%5D+%5BSpecter%5D)



##### Colorless (28)



21
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


2
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)


75 Cards 



##### 1 (10)



4
[Cloudfin Raptor](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCloudfin%5D+%5BRaptor%5D)


4
[Judge's Familiar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJudge%5D+%5BFamiliar%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


1
[Triton Tactics](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriton%5D+%5BTactics%5D)



##### 2 (18)



4
[Frostburn Weird](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrostburn%5D+%5BWeird%5D)


2
[Omenspeaker](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOmenspeaker%5D)


4
[Tidebinder Mage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidebinder%5D+%5BMage%5D)


2
[Cyclonic Rift](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)


1
[Disperse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisperse%5D)


3
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


2
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)



##### 3 (11)



4
[Nightveil Specter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightveil%5D+%5BSpecter%5D)


4
[Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThassa,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D)


3
[Wall of Frost](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BFrost%5D)



##### 4 (9)



4
[Master of Waves](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BWaves%5D)


1
[Bident of Thassa](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBident%5D+%5Bof%5D+%5BThassa%5D)


4
[Jace, Architect of Thought](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BArchitect%5D+%5Bof%5D+%5BThought%5D)



##### 6 (2)



2
[Ætherling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86therling%5D)


50 Cards 



##### Common (32)



21
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


4
[Cloudfin Raptor](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCloudfin%5D+%5BRaptor%5D)


4
[Frostburn Weird](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrostburn%5D+%5BWeird%5D)


2
[Omenspeaker](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOmenspeaker%5D)


1
[Disperse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisperse%5D)



##### Uncommon (11)



4
[Judge's Familiar](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJudge%5D+%5BFamiliar%5D)


3
[Negate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D)


1
[Triton Tactics](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriton%5D+%5BTactics%5D)


3
[Wall of Frost](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BFrost%5D)



##### Rare (20)



4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


4
[Nightveil Specter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNightveil%5D+%5BSpecter%5D)


4
[Tidebinder Mage](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidebinder%5D+%5BMage%5D)


1
[Bident of Thassa](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBident%5D+%5Bof%5D+%5BThassa%5D)


2
[Cyclonic Rift](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)


2
[Ætherling](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86therling%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


2
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)



##### Mythic (12)



4
[Master of Waves](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMaster%5D+%5Bof%5D+%5BWaves%5D)


4
[Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThassa,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D)


4
[Jace, Architect of Thought](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BArchitect%5D+%5Bof%5D+%5BThought%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)


















 Jérémy Dezani's deck is devoted to blue and [Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea). With eight one-drops, Dezani won the Pro Tour with the most aggressive of the devotion decks. Attempting to quickly overwhelm opponents with a quick [Thassa, God of the Sea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea) or a [Master of Waves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves), Dezani used devotion to get 5/5 indestructible creatures for three mana and 10 (or more) power's worth of creatures for four mana. Who said blue is always a control color? 


### Kentarou Yamamoto








#### Kentarou Yamamoto's Mono-Black Devotion


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (15)



4
[Desecration Demon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDesecration%5D+%5BDemon%5D)


1
[Erebos, God of the Dead](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErebos,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BDead%5D)


4
[Gray Merchant of Asphodel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGray%5D+%5BMerchant%5D+%5Bof%5D+%5BAsphodel%5D)


4
[Lifebane Zombie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLifebane%5D+%5BZombie%5D)


2
[Pack Rat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPack%5D+%5BRat%5D)



##### Sorcery (4)



4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)



##### Instant (10)



2
[Devour Flesh](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevour%5D+%5BFlesh%5D)


4
[Doom Blade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D)


4
[Hero's Downfall](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHero%5D+%5BDownfall%5D)



##### Artifact (2)



2
[Whip of Erebos](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhip%5D+%5Bof%5D+%5BErebos%5D)



##### Enchantment (4)



4
[Underworld Connections](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BConnections%5D)



##### Land (25)



4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


1
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


16
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Temple of Silence](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D)


60 Cards 


##### Sideboard (15)



1
[Erebos, God of the Dead](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErebos,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BDead%5D)


1
[Devour Flesh](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevour%5D+%5BFlesh%5D)


4
[Duress](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)


4
[Pharika's Cure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPharika%5D+%5BCure%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


4
[Xathrid Necromancer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXathrid%5D+%5BNecromancer%5D)




##### Black (49)



4
[Desecration Demon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDesecration%5D+%5BDemon%5D)


2
[Erebos, God of the Dead](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErebos,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BDead%5D)


4
[Gray Merchant of Asphodel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGray%5D+%5BMerchant%5D+%5Bof%5D+%5BAsphodel%5D)


4
[Lifebane Zombie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLifebane%5D+%5BZombie%5D)


2
[Pack Rat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPack%5D+%5BRat%5D)


3
[Devour Flesh](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevour%5D+%5BFlesh%5D)


4
[Doom Blade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D)


4
[Hero's Downfall](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHero%5D+%5BDownfall%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


4
[Underworld Connections](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BConnections%5D)


2
[Whip of Erebos](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhip%5D+%5Bof%5D+%5BErebos%5D)


4
[Duress](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)


4
[Pharika's Cure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPharika%5D+%5BCure%5D)


4
[Xathrid Necromancer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXathrid%5D+%5BNecromancer%5D)



##### Colorless (26)



4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


1
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


16
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Temple of Silence](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


75 Cards 



##### 1 (9)



4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


4
[Duress](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)



##### 2 (13)



2
[Pack Rat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPack%5D+%5BRat%5D)


3
[Devour Flesh](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevour%5D+%5BFlesh%5D)


4
[Doom Blade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D)


4
[Pharika's Cure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPharika%5D+%5BCure%5D)



##### 3 (16)



4
[Lifebane Zombie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLifebane%5D+%5BZombie%5D)


4
[Hero's Downfall](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHero%5D+%5BDownfall%5D)


4
[Underworld Connections](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BConnections%5D)


4
[Xathrid Necromancer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXathrid%5D+%5BNecromancer%5D)



##### 4 (8)



4
[Desecration Demon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDesecration%5D+%5BDemon%5D)


2
[Erebos, God of the Dead](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErebos,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BDead%5D)


2
[Whip of Erebos](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhip%5D+%5Bof%5D+%5BErebos%5D)



##### 5 (4)



4
[Gray Merchant of Asphodel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGray%5D+%5BMerchant%5D+%5Bof%5D+%5BAsphodel%5D)


50 Cards 



##### Common (31)



16
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Gray Merchant of Asphodel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGray%5D+%5BMerchant%5D+%5Bof%5D+%5BAsphodel%5D)


3
[Devour Flesh](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevour%5D+%5BFlesh%5D)


4
[Thoughtseize](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D)


4
[Pharika's Cure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPharika%5D+%5BCure%5D)



##### Uncommon (4)



4
[Duress](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D)



##### Rare (38)



4
[Mutavault](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D)


1
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


4
[Temple of Silence](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D)


4
[Desecration Demon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDesecration%5D+%5BDemon%5D)


4
[Lifebane Zombie](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLifebane%5D+%5BZombie%5D)


2
[Pack Rat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPack%5D+%5BRat%5D)


4
[Doom Blade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D)


4
[Hero's Downfall](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHero%5D+%5BDownfall%5D)


4
[Underworld Connections](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BConnections%5D)


2
[Whip of Erebos](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhip%5D+%5Bof%5D+%5BErebos%5D)


1
[Pithing Needle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D)


4
[Xathrid Necromancer](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXathrid%5D+%5BNecromancer%5D)



##### Mythic (2)



2
[Erebos, God of the Dead](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErebos,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BDead%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mutavault)


















 On the other end of the spectrum, Kentarou Yamamoto's mono-black deck was the most controlling of the devotion decks. Using permanents such as [Underworld Connections](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Connections) and [Whip of Erebos](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whip+of+Erebos), Yamamoto's permanents were more reliable in providing devotion. This allowed Yamamoto to play many removal spells without fearing for his devotion count. 


### Makihito Mihara








#### Makihito Mihara's Colossal Gruul


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (9)



3
[Domri Rade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDomri%5D+%5BRade%5D)


4
[Garruk, Caller of Beasts](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BCaller%5D+%5Bof%5D+%5BBeasts%5D)


2
[Xenagos, the Reveler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXenagos,%5D+%5Bthe%5D+%5BReveler%5D)



##### Creature (28)



3
[Arbor Colossus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArbor%5D+%5BColossus%5D)


4
[Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BEmissary%5D)


4
[Elvish Mystic](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D)


2
[Nylea, God of the Hunt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BHunt%5D)


4
[Polukranos, World Eater](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D)


3
[Scavenging Ooze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScavenging%5D+%5BOoze%5D)


4
[Sylvan Caryatid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BCaryatid%5D)


4
[Voyaging Satyr](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoyaging%5D+%5BSatyr%5D)



##### Land (23)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


2
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


4
[Stomping Ground](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D)


4
[Temple of Abandon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BAbandon%5D)


60 Cards 


##### Sideboard (15)



1
[Xenagos, the Reveler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXenagos,%5D+%5Bthe%5D+%5BReveler%5D)


2
[Burning Earth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BEarth%5D)


2
[Chandra, Pyromaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra,%5D+%5BPyromaster%5D)


1
[Destructive Revelry](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDestructive%5D+%5BRevelry%5D)


1
[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistcutter%5D+%5BHydra%5D)


3
[Mizzium Mortars](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMizzium%5D+%5BMortars%5D)


2
[Nylea's Disciple](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea%5D+%5BDisciple%5D)


1
[Sylvan Primordial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BPrimordial%5D)


2
[Wasteland Viper](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWasteland%5D+%5BViper%5D)




##### Red (7)



2
[Burning Earth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BEarth%5D)


2
[Chandra, Pyromaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra,%5D+%5BPyromaster%5D)


3
[Mizzium Mortars](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMizzium%5D+%5BMortars%5D)



##### Green (34)



3
[Arbor Colossus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArbor%5D+%5BColossus%5D)


4
[Elvish Mystic](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D)


2
[Nylea, God of the Hunt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BHunt%5D)


4
[Polukranos, World Eater](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D)


3
[Scavenging Ooze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScavenging%5D+%5BOoze%5D)


4
[Sylvan Caryatid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BCaryatid%5D)


4
[Voyaging Satyr](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoyaging%5D+%5BSatyr%5D)


4
[Garruk, Caller of Beasts](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BCaller%5D+%5Bof%5D+%5BBeasts%5D)


1
[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistcutter%5D+%5BHydra%5D)


2
[Nylea's Disciple](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea%5D+%5BDisciple%5D)


1
[Sylvan Primordial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BPrimordial%5D)


2
[Wasteland Viper](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWasteland%5D+%5BViper%5D)



##### Multi colored (11)



4
[Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BEmissary%5D)


3
[Domri Rade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDomri%5D+%5BRade%5D)


3
[Xenagos, the Reveler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXenagos,%5D+%5Bthe%5D+%5BReveler%5D)


1
[Destructive Revelry](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDestructive%5D+%5BRevelry%5D)



##### Colorless (23)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


2
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


4
[Stomping Ground](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D)


4
[Temple of Abandon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BAbandon%5D)


75 Cards 



##### 1 (7)



4
[Elvish Mystic](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D)


1
[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistcutter%5D+%5BHydra%5D)


2
[Wasteland Viper](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWasteland%5D+%5BViper%5D)



##### 2 (19)



4
[Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BEmissary%5D)


3
[Scavenging Ooze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScavenging%5D+%5BOoze%5D)


4
[Sylvan Caryatid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BCaryatid%5D)


4
[Voyaging Satyr](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoyaging%5D+%5BSatyr%5D)


1
[Destructive Revelry](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDestructive%5D+%5BRevelry%5D)


3
[Mizzium Mortars](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMizzium%5D+%5BMortars%5D)



##### 3 (3)



3
[Domri Rade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDomri%5D+%5BRade%5D)



##### 4 (15)



2
[Nylea, God of the Hunt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BHunt%5D)


4
[Polukranos, World Eater](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D)


3
[Xenagos, the Reveler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXenagos,%5D+%5Bthe%5D+%5BReveler%5D)


2
[Burning Earth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BEarth%5D)


2
[Chandra, Pyromaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra,%5D+%5BPyromaster%5D)


2
[Nylea's Disciple](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea%5D+%5BDisciple%5D)



##### 5 (3)



3
[Arbor Colossus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArbor%5D+%5BColossus%5D)



##### 6 (4)



4
[Garruk, Caller of Beasts](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BCaller%5D+%5Bof%5D+%5BBeasts%5D)



##### 7 (1)



1
[Sylvan Primordial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BPrimordial%5D)


52 Cards 



##### Common (21)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


2
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Elvish Mystic](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D)


4
[Voyaging Satyr](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoyaging%5D+%5BSatyr%5D)


2
[Nylea's Disciple](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea%5D+%5BDisciple%5D)



##### Uncommon (7)



4
[Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BEmissary%5D)


1
[Destructive Revelry](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDestructive%5D+%5BRevelry%5D)


2
[Wasteland Viper](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWasteland%5D+%5BViper%5D)



##### Rare (29)



4
[Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNykthos,%5D+%5BShrine%5D+%5Bto%5D+%5BNyx%5D)


4
[Stomping Ground](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D)


4
[Temple of Abandon](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BAbandon%5D)


3
[Arbor Colossus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArbor%5D+%5BColossus%5D)


3
[Scavenging Ooze](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScavenging%5D+%5BOoze%5D)


4
[Sylvan Caryatid](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BCaryatid%5D)


2
[Burning Earth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BEarth%5D)


1
[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistcutter%5D+%5BHydra%5D)


3
[Mizzium Mortars](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMizzium%5D+%5BMortars%5D)


1
[Sylvan Primordial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BPrimordial%5D)



##### Mythic (18)



2
[Nylea, God of the Hunt](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNylea,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BHunt%5D)


4
[Polukranos, World Eater](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D)


3
[Domri Rade](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDomri%5D+%5BRade%5D)


4
[Garruk, Caller of Beasts](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BCaller%5D+%5Bof%5D+%5BBeasts%5D)


3
[Xenagos, the Reveler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BXenagos,%5D+%5Bthe%5D+%5BReveler%5D)


2
[Chandra, Pyromaster](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra,%5D+%5BPyromaster%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)



















[In his deck tech](/en/articles/archive/event-coverage/video-deck-tech-colossal-gruul-makihito-mihara-2013-10-12), Makihito Mihara made it clear he was playing a combo deck. With 4 [Voyaging Satyr](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voyaging+Satyr) and 4 [Nykthos, Shrine to Nyx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx), Mihara was looking to generate a large amount of mana. [Garruk, Caller of Beasts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Caller+of+Beasts); [Arbor Colossus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arbor+Colossus); and [Polukranos, World Eater](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polukranos%2C+World+Eater) are great things to spend that mana on. 


  


---

  
Standard is shaping up to be a great format, with devotion being an important part of many different decks. It's also important that devotion isn't the only thing that you can do. We like making lots of exciting new things, but we work to make sure that any given thing isn't so powerful that nothing else is worth doing. Given the success of Esper Control, white beatdown and other non-devotion decks, there are plenty of options in Standard.


Thanks for joining me this week,


Adam Prosak














