
---
[Link to Wayback Machine](https://web.archive.org/web/20220816170533/https://magic.wizards.com/en/articles/archive/lorwyn-goblins-and-circle-death-2007-10-05)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "They're ugly. They're nasty. They're rude. They're hoodlums, mobs, exiles, and stinkdrinkers. They forage, caterwaul, chase sprites, make wigs out of spiders, and kidnap goats. They launch fodder, harass with hornets, sling porcupine quills, and vault on each other's faces. They're Lorwyn's Goblins, and today I'll show you how we developed their themes."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "296396"
[_metadata_:publish_date]:- "2007-10-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Lorwyn Goblins and the Circle of Death"
[_metadata_:wayback_capture_timestamp]:- "2022-08-16 17:05:33"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220816170533id_/https://magic.wizards.com/en/articles/archive/lorwyn-goblins-and-circle-death-2007-10-05"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/lorwyn-goblins-and-circle-death-2007-10-05"
---


Lorwyn Goblins and the Circle of Death
======================================



 Posted in [NEWS](/en/articles)
 on October 5, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low













They're ugly. They're nasty. They're rude. They're [hoodlums](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=hoodlums), [mobs](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=mobs), [exiles](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=exiles), and [stinkdrinkers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=stinkdrinkers). They [forage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=forage), [caterwaul](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=caterwaul), [chase sprites](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=chase+sprites), [make wigs out of spiders](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=make+wigs+out+of+spiders), and [kidnap goats](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=kidnap+goats). They [launch fodder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=launch+fodder), [harass with hornets](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=harass+with+hornets), [sling porcupine quills](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=sling+porcupine+quills), and [vault on each other's faces](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=vault+on+each+other%27s+faces). They're *Lorwyn*'s Goblins, and today I'll show you how we developed their themes.


### A Brief History of Goblins


Goblins have been one of *Magic*'s most beloved races ever since Alpha, when [Mons's Goblin Raiders](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mons%27s+Goblin+Raiders) and [Goblin Balloon Brigade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Balloon+Brigade) formed many a red mage's opening plays, backed up by the original tribal gangster, [Goblin King](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King). Over time, Goblins have become the iconic red weenie, and along with Elves, one of *Magic*'s most iconic weenie races.


[![Goblin Warchief](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Goblin%20Warchief&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin%20Warchief)


Goblins have always been famous for being small, low-cost red creatures that are funny, self-destructive, and prone to dying in droves. Some of the best-known Goblin cards involve the Goblins blowing up themselves (or each other) to win the game, including [Goblin Grenade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Grenade), [Mogg Fanatic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Fanatic), [Goblin Legionnaire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Legionnaire), and [Goblin Digging Team](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Digging+Team).


*Onslaught* Block amped up the Goblin tribe in a whole new way, with synergistic tribal interactions that ushered them to the very top of the power-level pyramid. *Onslaught* Block also underlined this sacrifice-for-advantage theme with cards like [Skirk Prospector](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skirk+Prospector) and [Goblin Sledder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Sledder). Those two looked innocuous to some, but they quickly became tournament powerhouses when combined with [Goblin Warchief](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Warchief), [Goblin Piledriver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Piledriver), and [Siege-Gang Commander](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang+Commander).


Goblins had come a long way from their goofy Goblin Artisans and [Goblin Digging Team](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Digging+Team) roots to becoming one of the most powerful decks in Standard, Extended, and Legacy. The power and speed of the *Onslaught* Block Goblins, capable of killing on turn three with a hand of [Skirk Prospector](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skirk+Prospector), [Goblin Warchief](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Warchief), and three [Goblin Piledriver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Piledriver)s, made the pointy-eared little monsters both loved and feared. Getting killed by *Onslaught* Block Goblins on turn five was reasonably fun the first few times it happened, and okay for the next few dozen times, but when they killed you on turn five for the fiftieth time, it started to get a little annoying.


### Goblins 2007


When the *Lorwyn* designers planned out what to do with each of their tribes, the Goblins presented a dilemma. How could they build on all the qualities of Goblins that people loved without recreating the exact same "superfast-Goblins-kill-you" experience that caused some people to groan? It was important to the designers to give Goblins some powerful new angles the little guys didn't have in *Onslaught* Block. If the *Lorwyn* Goblins had a little less raw speed, they had to have additional power in some other way. It was also important to the designers to make *Lorwyn* Goblins in a way that the multitudes of existing Goblin players in the world would love; Goblins that would "feel right" to those players that loved Goblins most, while also offering new abilities and themes. They had two major answers.


First: The designers grew Elves and Merfolk from their mono-color roots into a minor second color (some black for elves and some white for merfolk). However, they moved *Lorwyn* Goblins' *main* color into black, leaving red as the *Lorwyn* Goblins' minor color. This allowed them to have Goblins focus on black abilities like fear more than red abilities like firebreathing. This is the only tribe in *Lorwyn* with a major tribal history whose main color in *Lorwyn* doesn't match its historical major color.


Second: In contrast to *Time Spiral* Block's flavor of cratered armageddon, *Lorwyn* is a warmer, friendlier world. The line started going around the department that in *Lorwyn*, the bad guys don't kidnap and torture your children; instead, they creep to your window sill and steal your pies. In keeping with this world-building philosophy, the designers worked with the creative team to focus Goblins less on "kill you on turn five" and more on being cruel pranksters. This new emphasis matched Goblins' historically wacky side, and made it crueler to match the Goblins' increased emphasis on black mana. In short, the theme was "Goblins mess with you." At the handoff from design to development, the theme featured a lot of cards like these:



> 
> CB05\_PEA  
> 
> Concentration Breaker  
> 
> 2B  
> 
> Creature - Goblin Shaman  
> 
> 1/3  
> 
> You may choose not to untap CARDNAME during your untap step.  
> 
> B, T: As long as CARDNAME remains tapped, target creature loses all abilities.
>  
> 
> CB06\_PEA  
> 
> Trench Goblin  
> 
> B  
> 
> Creature - Goblin Rogue  
> 
> 1/1  
> 
> You may choose not to untap CARDNAME during your untap step.  
> 
> B, T: As long as CARDNAME remains tapped, target land is a Swamp.
> 


In early development playtesting, these cards definitely conveyed the theme of Goblins being cruel pranksters who would mess with your stuff and laugh about it. They got as close to "stealing your pies" as a card really can. The flavor match was a success. The problem was that these pranks didn't synergize with each other very well in gameplay. The guy that made [Swamp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s didn't combine well with the guy who turned off abilities or with the third goblin who denied your opponent's draw steps. All these things could slow your opponent down, but you weren't really accomplishing anything proactive. You pulled a bunch of pranks, but it didn't really end up getting you anywhere.


![?](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/dl5_questionmark.jpg)It reminded us of the *South Park* episode where the Underpants Gnomes draw up their master plan:


Phase 1) Collect underpants.  

Phase 2) ?  

Phase 3) Profit!


The Gnomes were implementing step 1 of their plan, and step 3 sounded pretty great. They just hadn't figured out step 2 yet.


The *Lorwyn* Goblins' plan was basically:


Phase 1) Pull some pranks.  

Phase 2) ?  

Phase 3) Profit!


Developers talked about what phase 2 could possibly be, but there just wasn't enough of a way to connect phase 1 to phase 3.


### Filling the Void


It was time for a new Goblin theme. The development team agreed with the designers' reasons for wanting to move away from "Kill you on turn five" goblins, we agreed with their reasons for basing *Lorwyn* goblins in black, and we agreed that we needed to give the goblins some other powerful angles if we weren't going to make them quite as fast. So the question became "What can black mana add to the classic Goblin recipe that players already love?"


We asked that same question for all the *Lorwyn* tribes who had deep roots in *Magic* history. For Elves, one big answer was that moving into black mana could give them Elf-themed creature kill that mono-green Elf decks have always desired and never had. Unlike Elves, Goblins certainly didn't need black mana to get creature kill. Red had that covered. What goes well with lots of little creatures with sacrifice effects that black mana can add to a red mana tribe? The development team bounced ideas off of the design team, getting their feedback and refining the angles until we had found our answer.


The answer we found is an open-ended, round and round, Goblin Circle of Death:


Cards with "Sacrifice any Goblin: get an effect."  

Cards with "Sacrifice **this** Goblin: get an effect."  

Cards with "When any Goblin dies, get a reward."  

Cards with "When **this** Goblin dies, get a reward."  

Cards with "Make Goblin tokens."  

Cards with "[Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) your Goblins to start the whole circle over again."


### Circle Segments


Let's take a closer look at each of the segments of this circle. For almost every segment, the *Lorwyn* design team had made some cards, the *Lorwyn* development team added some cards, and some cards were already lurking in *Tenth Edition* and *Time Spiral* Block.


Seeing how many different options are available in each category also makes it clear how truly vast and open-ended the variety of different Circle of Death combinations really is. It's not just three cards that always go together: it's a vast smorgasbord of combo potential, and you pick your own plate.


**"Sacrifice any goblin: get an effect."**




|  |  |  |
| --- | --- | --- |
| 
[Facevaulter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter)
 | 
[Tar Pitcher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tar%20Pitcher)
 | 
Lowland Oaf
 |
| 
[Marsh Flitter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh%20Flitter)
 | 
[Fodder Launch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fodder%20Launch)
 | 
[Siege-Gang Commander](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang%20Commander)
 |

These cards throw away their fellow Goblins' lives for benefits. In a pinch, [Tar Pitcher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tar+Pitcher) can even throw himself. [Lowland Oaf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lowland+Oaf) is a Giant, but his ability to sacrifice your own Goblins, and thus trigger a variety of subsequent Goblin death effects, is definitely an intentional part of the Circle of Death.


[Facevaulter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter) and [Marsh Flitter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh+Flitter) can be especially nasty with their abilities to sacrifice tons of Goblins in one turn, triggering [Boggart Shenanigans](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Shenanigans) or [Knucklebone Witch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knucklebone+Witch) tons of times.


Also remember: This is *Lorwyn* block. When your [Facevaulter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter), [Tar Pitcher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tar+Pitcher), [Marsh Flitter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh+Flitter), [Fodder Launch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fodder+Launch) and [Siege-Gang Commander](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang+Commander) say "Sacrifice a Goblin," there's no reason to restrict yourself to just Goblin *creatures*. Sometimes [Facevaulter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter) needs to eat a tasty Goblin enchantment.


[Goatnapper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goatnapper) doesn't sacrifice Goblins, but he has a lot of synergy with those who do. If you haven't seen it happen yet, [Goatnapper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goatnapper) usually kidnaps himself a delicious [Avian Changeling](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Avian+Changeling) or [Changeling Titan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Changeling+Titan), each of which is conveniently a Goat! For additional convenience, those two (and all other changelings) are also Goblins, which means that after you steal a Changeling and bash with it, you can sacrifice your captive to one of the "Sacrifice a Goblin" cards in this category and never have to give it back.


**"Sacrifice *this* goblin: get an effect."**




|  |  |  |
| --- | --- | --- |
| 
[Boggart Loggers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart%20Loggers)
 | 
[Boggart Forager](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart%20Forager)
 | 
[Mogg Fanatic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg%20Fanatic)
 |
| 
[Emberwilde Augur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emberwilde%20Augur)
 | 
[Mogg War Marshal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg%20War%20Marshal)
 | 
[Stingscourger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stingscourger)
 |

These goblins sacrificing themselves can help you trigger your Goblin death effects at will, and when you return [Boggart Loggers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Loggers), [Mogg Fanatic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Fanatic), [Stingscourger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stingscourger), or [Mogg War Marshal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+War+Marshal) again and again, it can get downright nasty.


**"When any goblin dies, get a reward."**




|  |  |
| --- | --- |
| 
[Knucklebone Witch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knucklebone%20Witch)
 | 
[Boggart Shenanigans](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart%20Shenanigans)
 |

Here's where the combos start popping. You get pretty happy about all your Goblins sacrificing each other when each Goblin death pumps up your one mana Khabal Ghoul or pings your opponent. For a one-mana creature, [Knucklebone Witch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knucklebone+Witch) sure hits 4/4 in a hurry. The ability to trigger these whenever you want with sacrifice abilities can quickly back your opponents into a corner.


**"When this goblin dies, get a reward."**




|  |  |  |
| --- | --- | --- |
| 
[Hornet Harasser](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hornet%20Harasser)
 | 
[Mudbutton Torchrunner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mudbutton%20Torchrunner)
 | 
[Festering Goblin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Festering%20Goblin)
 |

Hornet Harrasser and [Mudbutton Torchrunner](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mudbutton+Torchrunner) are both good examples of goblins who are worth more dead than alive. Hornet Harrasser is a subtle Goblin reprint of *Urza's Destiny*'s [Disease Carriers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disease+Carriers). It's here in *Lorwyn* because the Goblin theme gives the card a new context and thus a new identity. With the original [Disease Carriers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disease+Carriers), you had to maneuver to get him killed at the right time, trying to get him into fights so that you could kill the 2/2 evasion guy that was killing you. But with all the Goblin sacrifice outlets in *Lorwyn*, Goblin decks can often kill their own Hornet Harrasser whenever they want to, triggering him at just the right time. The same goes for Torchrunner and [Uncle Fester](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Uncle+Fester).


**"Make Goblin tokens."**




|  |  |  |
| --- | --- | --- |
| 
[Marsh Flitter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh%20Flitter)
 | 
[Boggart Mob](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart%20Mob)
 | 
[Siege-Gang Commander](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang%20Commander)
 |
| 
[Mogg War Marshal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg%20War%20Marshal)
 | 
[Empty the Warrens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empty%20the%20Warrens)
 | 
[Ib Halfheart, Goblin Tactician](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg%20War%20Marshal)
 |

If you want to get a lot of Goblin sacrifice fuel, and you want to get a lot of Goblin death triggers, one of the best ways to do it is to crank out a lot of Goblin creature tokens. [Marsh Flitter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marsh+Flitter) and [Boggart Mob](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Mob) provide a stream of willing recruits, and Standard-legal roommates like [Mogg War Marshal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+War+Marshal), [Empty the Warrens](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empty+the+Warrens), and [Siege-Gang Commander](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang+Commander) are already in decks for their multiple token generation.


**"[Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) your goblins to start the whole circle over again"**




|  |  |  |
| --- | --- | --- |
| 
[Boggart Birth Rite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart%20Birth%20Rite)
 | 
[Warren Pilferers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warren%20Pilferers)
 | 
[Wort, Boggart Auntie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wort,%20Boggart%20Auntie)
 |
| 
[Footbottom Feast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Footbottom%20Feast)
 | 
[Tarfire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarfire)
 | 
[Squee, Goblin Nabob](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squee,%20Goblin%20Nabob)
 |

These Goblin sacrifice outlets, Goblin death triggers, and some spell-wielding opponents combine to ensure one thing: tons of Goblins in the graveyard. This is where *Lorwyn*'s black mana influx into Goblins comes in: Now that you've successfully killed a lot of your own goblins, it's time to bring them all back to start again. [Wort, Boggart Auntie](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wort%2C+Boggart+Auntie), [Warren Pilferers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warren+Pilferers), and [Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) are the stars here. [Squee, Goblin Nabob](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squee%2C+Goblin+Nabob) in *Tenth Edition* brings himself back to be sacrificed again and again.


I mention [Footbottom Feast](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Footbottom+Feast) as an "honorary" Goblin card which is in the set both to return sacrificed Goblins and to trick your opponent by suddenly stacking the top of your deck to win a clash. (Did you see that one?)


[Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) and [Wort, Boggart Auntie](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wort%2C+Boggart+Auntie) can both raise "Goblin *cards*," which means you can bring back [Tarfire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarfire) again and again. Or play [Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) for your other [Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) for your first [Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) for your other [Boggart Birth Rite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Birth+Rite) for your own nefarious purposes.


### You Define What You Combine


When you play Goblins in Sealed or Draft, I think you'll quickly find out how much fun it is to use your [Facevaulter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter) to sacrifice [Mudbutton Torchrunner](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mudbutton+Torchrunner), pumping up the [Facevaulter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Facevaulter) while blowing up your opponent's creatures with Torchrunner's death effect, then regrowing the Torchrunner with Wort to do the whole thing again next turn. Or combine any of the other cards in any of these categories. Once you've tried it in Limited, look for ways to pull similar tricks in Constructed.


I really enjoy that the Circle of Death is so open-ended. You can choose to combine almost any two segments of the circle and they will do something cool together. And you choose whatever cards you want to use from each segment, and even which segments to use and which to ignore. It's not one pre-made combo that you have to follow—it's the basic ingredients for a billion potential combos that you concoct yourself.


The [Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) angle that black mana adds to *Lorwyn* Goblin decks also gives them a resiliency that mono-red *Onslaught* Goblin decks sometimes lacked. If [Goblin Sledder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Sledder) wasn't around, a well-timed [Pyroclasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm) could wipe the *Onslaught* Goblin deck out. The *Lorwyn* Goblins are more likely to sac a couple of guys in response to [Pyroclasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm), resolve a couple of death triggers, then regrow the dead Goblins and come right back.


There are also a ton of Goblins in the set that aren't a part of this Circle of Death theme at all. They just fight well, or attack with fear, or do something else. There are also some more subtle Circle of Death synergies in the set and in Standard that I didn't even touch on. You'll have to find them yourself.


### Last Week's Poll




|  |
| --- |
| **How often should we do flash creatures after *Lorwyn*  Block is done?** |
| Sometimes, mostly at uncommon and rare | 6408 | 47.3% |
| Frequently, at all rarities | 4264 | 31.5% |
| Not very often, and not at common | 2272 | 16.8% |
| None of the above | 611 | 4.5% |
| **Total** | **13555** | **100.0%** |

One response that came back very clearly on the boards and in my email was that people wanted more options to express themselves on flash and felt too limited by the options provided. Ironically, my first draft included the wider set of poll response options below. I was worried that these options would bias readers too much with my own predilections for flash in the future (rarity, color, size, etc.), so I decided to scale back the options to reduce any bias and get the most sincere flash feedback possible. As it turns out, I scaled back too much.


I got a lot of very well-reasoned feedback about what people want to see from flash in the future and why, on the boards and in my email. The feedback has helped me form a potential plan on how to use flash going forward. I'm going to run my ideas past the other *Magic* developers and designers, talk it out, then describe the way forward in a future article. Here are the original poll options I was going to give:



> 
> * Often, in white blue or green, at any size and rarity.
> * Only at high rarities.
> * Commons are okay, but only on small creatures.
> * Commons are okay, and any size is ok, but only do flash in white and green, not blue.
> * Any rarity or size is okay, but aim them at Limited, not Constructed.
> * Not very often at all.
> * None of the above.
> 
> 
> 







