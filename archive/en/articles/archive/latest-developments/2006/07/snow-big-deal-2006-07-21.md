
---
[Link to Wayback Machine](https://web.archive.org/web/20210122124608/https://magic.wizards.com/en/articles/archive/latest-developments/snow-big-deal-2006-07-21)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "When I reflect on the development process for Coldsnap, I remember a tumultuous time of change. Two keyword mechanics—ripple and recover—were added. A cycle of gold cards were cut, as was most of the allied-color helping theme. The number of Aurochs cards increased, and the number of cards with the “Panglacial Wurm” mechanic was reduced. Legendary characters like Zur, Lovisa, Arcum Dagsson, and King Darien were given their own cards."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "289781"
[_metadata_:publish_date]:- "2006-07-21"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Snow Big Deal"
[_metadata_:wayback_capture_timestamp]:- "2021-01-22 12:46:08"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210122124608id_/https://magic.wizards.com/en/articles/archive/latest-developments/snow-big-deal-2006-07-21"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/snow-big-deal-2006-07-21"
---


Snow Big Deal
=============



 Posted in **Latest Developments**
 on July 21, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe











When I reflect on the development process for *Coldsnap*, I remember a tumultuous time of change. Two keyword mechanics—ripple and recover—were added. A cycle of gold cards were cut, as was most of the allied-color helping theme. The number of Aurochs cards increased, and the number of cards with the “Panglacial Wurm” mechanic was reduced. Legendary characters like Zur, Lovisa, [Arcum Dagsson](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcum+Dagsson), and King Darien were given their own cards.


In order to write this article, I had to dig up the original design spreadsheet for *Coldsnap*, then codenamed “Splat.” Because I was being trained in our new card database software at the time, the set had to be compiled in an external Excel sheet as opposed to right in the database, which turned out to be handy in retrospect, as I have a wonderfully clean snapshot of the set on the day it was handed off to development.


After looking it over, I realize my recollections of the process were greatly exaggerated. What design turned in is very close to what you see on the cards right now. Randy Buehler and his team of Mike Turian, Devin Low, and Zvi Mowshowitz did a great job coming up with the exact tweaks and missing pieces that were necessary to make the set hum, but it was fun to see just how many of those final pieces were in place from the beginning. As an example, here's a look at the dozen white commons that were submitted:




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CARDID** | **R** | **C** | **N** | **TITLE** | **TYPE** | **SUBTYPE** | **COST** | **P** | **T** | **RULESTEXT** |
| 121188 | C | W | 1 | Kjeldoran Scout | Creature | Human Scout | W | 1 | 1 | Whenever CARDNAME becomes blocked, creatures defending player controls can't attack or block next turn. |
| 121235 | C | W | 2 | Kjeldoran Cleric | Creature | Human Cleric | W | 1 | 2 | Cumulative upkeep 1//T: Prevent the next X damage, divided as you choose, that would be dealt to any number of target creatures or players this turn, where X is the number of Age counters on CARDNAME. |
| 121263 | C | W | 3 | Kelsinko Martyr | Creature | Human Soldier | 1W | 2 | 2 | 1, Reveal any number of cards from your hand, sacrifice CARDNAME: Target creature gets +X/+X, where X is green cards revealed. |
| 121273 | C | W | 4 | Duck Decoy | Creature | Bird | 1W | 1 | 1 | Flying//W, T: Tap target creature. |
| 121244 | C | W | 5 | Frost Griffin | Snow Creature | Griffin | 3W | 2 | 3 | Flying//S: CARDNAME gains first strike until end of turn. |
| 121128 | C | W | 6 | Frost Piker | Snow Creature | Human Knight | 2W | 3 | 2 | S: CARDNAME gains first strike until end of turn. |
| 121237 | C | W | 7 | Arenson's Homeguard | Creature | Human Soldier | 3W | 2 | 4 | Sacrifice CARDNAME: Destroy target enchantment. |
| 121225 | C | W | 8 | Illusionary Wall of Swords | Creature | Wall | 3W | 4 | 6 | Cumulative upkeep 1//Flying, defender |
| 121148 | C | W | 9 | Warrior's Kindle | Instant |  | 1W |  |  | All attacking creatures get +X/+X until end of turn, where X is 1+ the number of cards named CARDNAME in all graveyards. |
| 121255 | C | W | 10 | Turquoise Touch | Instant |  | W |  |  | Prevent the next 4 damage that would be dealt this turn to target green, white, or blue creature. Draw a card. |
| 121213 | C | W | 11 | Snowsuit | Enchantment | Aura | W |  |  | Enchanted creature can't block or use activated abilities.//S: Enchanted creature can't attack you this turn. |
| 121211 | C | W | 12 | Inflatable Armor | Enchantment | Aura | W |  |  | Cumulative upkeep 1//Enchanted creature gets +1/+1 for each age counter on CARDNAME. |

![Kjeldoran Javelineer](https://media.wizards.com/legacy/magic/images/cardart/csp/kjeldoran_javelineer.jpg)Kjeldoran Scout was originally part of a “becomes blocked” cycle that eventually resulted in [Drelnoch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drelnoch) and [Karplusan Wolverine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Wolverine). Kjeldoran Cleric morphed into [Kjeldoran Javelineer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kjeldoran+Javelineer)—you can see the family resemblance. Kelsinko Martyr and his four cycle buddies traded their allied-color reveal abilities for more traditional in-color ones, resulting in [Martyr of Sands](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martyr+of+Sands) and friends. Duck Decoy is obviously [Squall Drifter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squall+Drifter), Frost Griffin evolved into [Boreal Griffin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boreal+Griffin), and Arenson's Homeguard shed some pounds to become the familiar [Ronom Unicorn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ronom+Unicorn). Illusionary Wall of Swords planted the seed for the quirky [Wall of Shards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Shards). Warrior's Kindle improved to become [Kjeldoran War Cry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kjeldoran+War+Cry); the “collect-me” cards existed in design, although not at the quantities they do in the final set. Turquoise Touch was simplified to become [Swift Maneuver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swift+Maneuver); by reducing the allied-color theme, the developers made many cards more open-ended. Snowsuit is [Gelid Shackles](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gelid+Shackles), and Inflatable Armor was beefed up to become [Glacial Plating](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Plating).


Of those twelve cards, only Frost Piker is nowhere to be seen in the final set, and one might even argue that his spirit lives on in the ripple-tastic [Surging Sentinels](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Surging+Sentinels). That is some efficient use of design and development resources right there, folks.


Ironically, Frost Piker is one of the important cards in the rest of today's discussion regarding what development did with the snow mechanic. I'm not going to show you the entirety of the design file (there are a few goodies in there that were shipped off to *Time Spiral* and later sets), but instead will call out specific records that will help illustrate my points on snow.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121244 | C | W | 5 | Frost Griffin | Snow Creature | Griffin | 3W | 2 | 3 | Flying//S: CARDNAME gains first strike until end of turn. |
| 121128 | C | W | 6 | Frost Piker | Snow Creature | Human Knight | 2W | 3 | 2 | S: CARDNAME gains first strike until end of turn. |

These first two snow creatures tell a lot about the design and development of the mechanic. You can see right away that the supertype “Snow” and the “S” mana symbol had already been decided on in design, arrived at through a good deal of discussion with both the creative and rules people.


One thing that design tried to do was give each color two common creatures that had the same exact snow-activated ability, just to give some structure and flavor. Design was also conscious that snow land would be somewhat hard to come by in Limited play, so the abilities would play better if they didn't scale, meaning they'd be about as good if you had one or two snow lands in play as if you had eight or nine snow lands in play.


Development maintained the “non-scaling” part of the snow abilities (for the most part), but gave up trying to maintain the idea of two cards with identical abilities once they added ripple and recover into the set. After all, there is only so much room for everything the set is trying to do, and the second creature with activated first strike is much less interesting than the first.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121273 | C | W | 4 | Duck Decoy | Creature | Bird | 1W | 1 | 1 | Flying//W, T: Tap target creature. |

One thing design did not do was put the snow supertype on cards arbitrarily. If it didn't have an [snow] activation or refer to snow cards in the text somehow, it wasn't snow itself. Over the course of development, however, the team realized that the number of snow cards needed to increase, but not necessarily the number of cards that needed snow lands to be optimized. So some creatures were made into “snow.”




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121213 | C | W | 11 | Snowsuit | Enchantment | Aura | W |  |  | Enchanted creature can't block or use activated abilities.//S: Enchanted creature can't attack you this turn. |

You'll notice that the original version of [Gelid Shackles](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gelid+Shackles) was not snow. The design team didn't want to make snow Auras that would be played on other players' permanents because they felt too many players would miss them when instructed to count the number of snow permanents they had in play. Development wasn't quite so coddling to players—the card makes sense as a snow enchantment, so that's what it is. Surely you can remember what you have in play, even if it isn't right in front of you!




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121132 | C | U | 4 | Snowblind Drake | Snow Creature | Drake | 2U | 2 | 2 | Flying//S: CARDNAME cannot be the target of spell or abilities this turn. |
| 121176 | C | U | 7 | Snowblind Kraken | Snow Creature | Kraken | 5U | 5 | 6 | CARDNAME cannot attack unless defending player controls a Snow land.//S: CARDNAME cannot be the target of spell or abilities this turn. |

Design's idea for a blue snow-activated ability was untargetability. Unfortunately, it proved so frustratingly strong in Limited play that both cards had to be weakened. The Drake ([Frost Raptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frost+Raptor)) had its activation upped from [snow] to [snow][snow], and the Kraken ([Ronom Serpent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ronom+Serpent)) lost the ability altogether.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121239 | C | U | 8 | Minor Freezemage | Creature | Human Wizard | 2U | 1 | 2 | T: Tap or untap target permanent. Play this ability only if you control four or more snow permanents. |
| 121215 | U | U | 3 | Major Freezemage | Creature | Human Wizard | 3U | 2 | 3 | T: Counter target activated ability. Play this ability only if you control four or more snow permanents. |
| 121147 | R | U | 2 | Toby, Legendary Freezemage | Legendary Creature | Human Wizard | 4U | 3 | 4 | T: Return target permanent to its owner's hand. Play this ability only if you control four or more snow permanents. |



![Rimewind Cryomancer](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Rimewind%20Cryomancer&options=)

After a powwow with the creative team, during which the antagonists of the set's backstory were discussed, design made this trio of fellows to represent the Rimewind contingent. As you can see, each of their costs, power, and toughnesses increments by one as you go up in rarity, and they all have tap abilities that can only be played when the world is cold enough (you control four or more snow permanents). Of course, playtesting resulted in the numbers being broken up a bit—some better, some worse—but one thing remained the same throughout—these three cards ([Rimewind Taskmage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rimewind+Taskmage); [Rimewind Cryomancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rimewind+Cryomancer); and [Heidar, Rimewind Master](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heidar%2C+Rimewind+Master)) do *not* have the snow subtype.



Design left off the type for flavor reasons; after all, these were the sect of mages trying to control and use the power of snow, they weren't snow themselves. In fact, none of the snow creatures in the set are human. Development left the supertype off because they liked the tension of wanting to play a deck that used all the Rimewinders' awesome abilities, but needed fuel for those abilities from other cards. In other words, three Rimewind Initiates shouldn't feed one another; instead, they all need critical mass of other snow permanents in play to operate.


There was a great deal of back-and-forth on the topic. I can remember days when we were to playtest them as snow creatures, only to have that decision reversed hours later. In the end, however, we ended up right back where we began.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121228 | C | U | 12 | Frozen Solid | Enchantment | Aura | 1UU |  |  | Enchanted creature doesn't untap during its controller's untap step.//When enchanted creature is dealt damage, destroy it. |

Development loved the idea of the [Frozen Solid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frozen+Solid) “pre-print,” but they really, really wanted it to be a snow card—for flavor reasons if nothing else. “Could we really,” they asked themselves, “give it errata to be a snow card?” The answer was sensibly “no,” mainly because the change would imply that other historically snowy cards should get errata to the snow type as well. Imagine if [Tendo Ice Bridge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tendo+Ice+Bridge) was a snow land!




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121175 | U | U | 2 | Balduvian Ice Sculptor | Snow Creature | Human Wizard | 2U | 1 | 1 | T: Target Snow land becomes a blue 2/2 creature with flying until of turn. |

Above I stated that no snow creatures in the set are human… including this guy. He lost the supertype even though he deals directly with snow cards.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121136 | C | B | 2 | Snow Skeleton | Snow Creature | Skeleton | B | 1 | 1 | S: Regenerate CARDNAME. |
| 121154 | C | B | 5 | High Legion of Lim-Dul | Snow Creature | Zombie | 3B | 2 | 3 | Snow landwalk//S: Regenerate CARDNAME. |

The black common snow activation—regeneration—was a good choice and both cards with the ability stayed intact. Regarding High Legion of Lim-Dul: I was initially disappointed that the creative team took the concept away from a Lim-Dul Zombie; after all, there were two such 2/3's in *Ice Age*. But the idea of a [Zombie Musher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombie+Musher) with his team of undead sled dogs is such a good one that I quickly forgave them.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121194 | U | B | 1 | Frozen Chef | Snow Creature | Zombie Chef | 2B | 2 | 2 | S, Sacrifice a creature: You gain 2 life. |
| 121258 | U | B | 4 | Darkling Snowstalker | Snow Creature | Shade | 2B | 1 | 1 | Flying//S: CARDNAME gets +1/+1 until end of turn. |

These two creatures both started out as uncommons because their snow abilities weren't regeneration. They eventually wound up as commons—[Gutless Ghoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gutless+Ghoul) and [Chilling Shade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chilling+Shade). The Ghoul's activation cost is currently non-snow; it was actually no mana to use it for a while in development. The Shade is one of the few commons that really reward you for having the maximum possible number of snow lands in play. We generally tried to avoid those kinds of effects, but the Shade and [Skred](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skred) are good exceptions that can really reward players that prioritize snow lands in draft.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121219 | C | R | 3 | Goblin Bard | Snow Creature | Goblin Shaman | 2R | 2 | 2 | T: Target creature can't block this turn.//S: CARDNAME gains haste until end of turn. |
| 121173 | C | R | 7 | Gorilla Bob Sledder | Snow Creature | Ape Berserker | 4R | 4 | 3 | S: CARDNAME gains haste until end of turn.//Sacrifice CARDNAME: Add RRR to your mana pool. |

The red common snow activation that design submitted was haste, and it remained on two cards. Goblin Bard was printed as [Goblin Rimerunner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Rimerunner), and Gorilla Bob Sledder evolved into the slugtastic [Thermopod](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thermopod).




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121185 | C | R | 2 | Goblin Sunbather | Creature | Goblin Warrior | 1R | 2 | 2 | Prevent all damage CARDNAME would deal to snow creatures. |
| 121144 | C | R | 6 | Heated Gorilla | Creature | Ape Warrior | 3R | 3 | 3 | G: CARDNAME gains protection from snow until end of turn. |
| 121167 | C | R | 11 | Snow Shock | Instant |  | 2R |  |  | CARDNAME deals 3 damage to target creature or player. CARDNAME deals 6 damage instead if that creature is a snow creature. |
| 121143 | C | R | 12 | Sleetstorm | Sorcery |  | 2RR |  |  | Destroy target artifact or land. If that artifact or land is snow, draw a card. |
| 121135 | R | R | 2 | Blowtorcher | Creature | Human Barbarian | RR | 2 | 2 | Cumulative upkeep R//At the beginning of each player's upkeep, that player sacrifices a snow permanent. |

As this group of commons and rares indicates, design gave red a very “anti-snow” theme, meaning it had cards that were both very weak and very strong against snow. The latter card—[Goblin Furrier](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Furrier) *nee* Sunbather—was kept, but all of the hosers were removed.


Mark Rosewater has been in sporadic email contact with one of the original *Ice Age* designers on and off since we started talking about *Coldsnap* on this site, and that designer has enlightened Mark as to why certain things were done in that large set long ago. There was a real fear among the *Ice Age* designers and developers that snow-covered lands offered such a tangible benefit over normal basic lands that everyone would play the snowy ones. In order to lessen the potential benefits of playing all snow lands, the team made sure that there were identical numbers of cards in *Ice Age* that benefited from snow land and punished it. That's why there are scads of landwalkers, land destruction spells, and other savage hosers for what appears to be an innocuous little mechanic.


The good news is that the *Coldsnap* development team didn't buy into that theory at all, instead believing that the current crop of lands available in Standard offered a strong enough pull away from running all snow lands all the time that a natural tension would arise in lieu of needed a ton of hosers. Time will tell if they were right!




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121152 | C | G | 6 | Aurochs Mk II | Snow Creature | Aurochs | 2G | 3 | 1 | Whenever CARDNAME attacks, it gets +1/+0 until end of turn for each other attacking Aurochs.//S: CARDNAME gains trample until end of turn. |
| 121270 | C | G | 7 | Johtull Behemoth | Creature | Beast | 4G | 5 | 6 | Cumulative upkeep 1//Protection from snow |
| 121260 | C | G | 8 | Crackosaurus | Snow Creature | Dinosaur | 5G | 6 | 4 | S: CARDNAME gains trample until end of turn. |

Here are three green commons from design. The first and last illustrate design's green snow activation—trample. Development ditched that idea when they upped the number of Aurochs in the set and gave them all trample naturally (to match their *Ice Age* predecessor). The only snow-activated creature at common now is [Boreal Centaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boreal+Centaur).


The middle card, Johtull Behemoth, was printed as-is as [Ronom Hulk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ronom+Hulk). If there's any color in *Coldsnap* that is anti-snow, it's green. Not only does green have the only protection from snow creature, but it also has the only real hoser—the uncommon [Freyalise's Radiance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Freyalise%27s+Radiance).




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121193 | C | G | 2 | Snow Elf | Snow Creature | Elf Druid | 1G | 1 | 1 | T: Add R, G, or W to your mana pool. |
| 121199 | U | G | 6 | Snowy Rampant Growth | Sorcery |  | 2G |  |  | Search your library for a basic land and put that land into play, or search your library for a snow land and put that land into play tapped. The shuffle your library. |

Development did these two snowy accelerators (now [Boreal Druid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boreal+Druid) and [Into the North](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Into+the+North)) a huge favor by making them both simpler and cheaper, as well as moving the sorcery from uncommon to common.


Notice that Into the North was at no time a “Snow Sorcery.” While we could have chose to make instants and sorceries have the supertype, design decided against, based on the flavor of the original modifier: “Snow-Covered.” How could something that isn't a physical object be snow-covered? A land, sure. Creature, why not. Artifact, makes sense. Enchantment, maybe. Spell? Not happening.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121201 | U | G | 5 | Rain of Cicadas | Instant |  | 3G |  |  | Target land becomes a 4/4 green Giant Insect creature until end of turn and it's still a land. If you paid S to play CARDNAME, destroy that land instead. |

Here's an interesting card from design. Rain of Cicadas was part of a failed cycle of uncommon spells that were part enhanced and part modal. Borrowing a page from *Ravnica's* enhanced cards, these spells behaved differently based on what mana was spent to play them. But unlike [Ribbons of Night](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ribbons+of+Night) and [Seed Spark](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seed+Spark) which just got better if they were played with the “correct” mana, Rain of Cicadas changed functionality completely if snow was used to play it. If you didn't have snow, you'd want to play it on your own land. If you did have snow, you'd want to use it on an opponent's land.


The goal of these cards was to see if an environment could exist where people wanted to play about *half* snow lands, as opposed to all or none. The problem was that in the early game, when cards like these are at their best, you don't have much choice in how the spell plays out—it's all up to the fate of what lands you drew. Their lack of flexibility proved frustrating, as oftentimes you could only play one half when you really wanted the other. A neat idea, but it just didn't pan out.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121123 | U | A | 1 | Crystal Snowglobe | Snow Artifact |  | 2 |  |  | CARDNAME comes into play tapped.//As CARDNAME comes into play, choose a color.//T: Add one mana of the chosen color to your mana pool. |
| 121142 | U | A | 2 | Snowcrusher | Snow Artifact Creature | Juggernaut | 4 | 5 | 3 | CARDNAME attacks each turn if able.//1S: CARDNAME gets +1/+0 until end of turn. |
| 121120 | U | A | 3 | Dripping Icicle | Snow Artifact |  | 3 |  |  | CARDNAME comes into play with four ice counters on it.//At the beginning of your upkeep, remove an ice counter from CARDNAME.//T: Target creature with power equal to or less than the number of ice counters on CARDNAME can't attack or block this turn.//SSSS: Add an ice counter to CARDNAME. |
| 121127 | U | A | 4 | Ice Golem | Snow Artifact Creature | Golem | 5 | 3 | 5 | CARDNAME doesn't untap during your untap step.//1S: Untap CARDNAME. |

All four of the uncommon artifacts submitted by design were snow artifacts. Three of them saw print in one form or another: Crystal Snowglobe is [Coldsteel Heart](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coldsteel+Heart); Snowcrusher was fattened up but otherwise unchanged and is now [Phyrexian Snowcrusher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Snowcrusher) (and is the first creature card printed with the subtype Juggernaut); and Ice Golem was made less like the *Mirage* [Lead Golem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lead+Golem) and more like the *Alliances* [Phyrexian War Beast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+War+Beast) on its way to becoming [Phyrexian Ironfoot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Ironfoot).


Development ditched the crazily confusing Dripping Icicle in favor of the non-snow and very nostalgic [Mishra's Bauble](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Bauble), heralding the influx of “slowtrips” to the set.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121209 | R | A | 2 | Snow Stone | Snow Artifact |  | 2 |  |  | Snow spells costs 1 less to play. |

Snow Stone was killed in development in favor of the much more exciting [Thrumming Stone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thrumming+Stone), meaning that no snow artifacts were printed at rare.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121234 | U | L | 1 | Precarious Peak | Snow Land |  |  |  |  | T: Add 1 to your mana pool.//4S, T, Sacrifice CARDNAME: CARDNAME deals 4 damage to target creature. |
| 121189 | U | L | 2 | Snowy Tundra | Snow Land |  |  |  |  | CARDNAME comes into play tapped.//T: Add W or U to your mana pool. |
| 121212 | U | L | 3 | Snowy Sea | Snow Land |  |  |  |  | CARDNAME comes into play tapped.//T: Add U or B to your mana pool. |
| 121125 | U | L | 4 | Snowy Springs | Snow Land |  |  |  |  | CARDNAME comes into play tapped.//T: Add B or R to your mana pool. |
| 121259 | U | L | 5 | Snowy Taiga | Snow Land |  |  |  |  | CARDNAME comes into play tapped.//T: Add R or G to your mana pool. |
| 121158 | U | L | 6 | Snowy Brushland | Snow Land |  |  |  |  | CARDNAME comes into play tapped.//T: Add G or W to your mana pool. |

Here are the uncommon lands submitted by design—all snow and all printed as-is.




|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121204 | R | L | 1 | Heart of the Snowdrifts | Snow Land |  |  |  |  | T: Add U to your mana pool.//2U, T: Look at the top card of your library. If that card is a snow card, reveal it and put it into your hand. |
| 121245 | R | L | 2 | Heart of the Frostleaves | Snow Land |  |  |  |  | T: Add G to your mana pool.//Tap an untapped snow creature you control: Untap CARDNAME. |
| 121155 | R | L | 3 | Monster in the Ice | Snow Land |  |  |  |  | CARDNAME comes into play with eight ice counters on it.//3: Add or remove an Ice counter from CARDNAME. Any player may play this ability.//When CARDNAME has no Ice counters on it, sacrifice it and put a 20/20 black Legendary Snow Demon creature token with trample and indestructible into play. |

![](https://media.wizards.com/legacy/magic/images/tournamentcenter/2006/maritlagetoken.jpg)Finally, the rare lands. It is interesting to note that the two “Hearts” were designed as strictly better than basic snow lands, something we usually try to avoid. The problem was solved on Heart of the Snowdrifts by having it produce colorless mana and require snow to activate—you now know it as [Scrying Sheets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrying+Sheets). The Sheets are the hallmark snow card—if anything enables the mechanic in Constructed and makes people consider setting aside their *Ravnica* dual lands, it will be this card. This is the kind of card I feel *Ice Age* (and *Alliances*) was missing—that solid, tempting gem that would enable snow decks of all colors and flavors to compete.


The better-than-basic problem was solved on Heart of the Frostleaves by cutting it from the set in favor of the hilarious [Jester's Scepter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jester%27s+Scepter).


That leaves [Dark Depths](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Depths), a.k.a. Monster in the Ice. I designed this card after hearing from creative point-man Brandon Bozzi that part of the set's story plot involved a race to thaw an ancient monster from a frozen lake. I had no idea that (a) the card would actually survive development making a 20/20 token, and (b) that the token would end up being something as awesome as Marit Lage. Great stuff. Notice that the card didn't tap for mana in design either, as a nod to *Ice Age* lands like [Ice Floe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ice+Floe) and [Halls of Mist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Halls+of+Mist). There was a great deal of debate about the lack of that ability in development, and it did tap for mana for some period of time, but in the end a number of issues, one of which was available space for text, forced the mana ability off.


That's the story of snow, from Day One to the printed cards. I do believe we did a great job giving some respectability to a good idea that was somehow derailed over a decade ago.


Don't forget to play in this weekend's release events, where shiny foil Marit Lage tokens await! Check here to find a store in your area.


### Last Week's Poll:




|  |
| --- |
| **Do you agree with our removal of power-level errata?**  |
| Yes, great job. | 4205 | 56.8% |
| I don't care. | 1785 | 24.1% |
| In theory but not in execution. | 944 | 12.8% |
| No, quit changing things. | 467 | 6.3% |
| **Total** | **7401** | **100.0%** |

I'll take that percentage of support on any controversial decision any day of the week, thank you very much....







