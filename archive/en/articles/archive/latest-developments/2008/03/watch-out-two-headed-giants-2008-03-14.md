
---
[Link to Wayback Machine](https://web.archive.org/web/20220127100820/https://magic.wizards.com/en/articles/archive/latest-developments/watch-out-two-headed-giants-2008-03-14)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "In a Magic world like Lorwyn or Dominaria, `Watch out for two-headed giants!` is just plain good advice. But in Magic development, the advice is just as sound. It's easy to find yourself focusing on two-player Magic during development, and that is how we test most often. But it's also important for us to make fun cards for Two-Headed Giant (2 vs. 2), Emperor (3 vs. 3),"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "623411"
[_metadata_:publish_date]:- "2008-03-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Watch Out for Two-Headed Giants!"
[_metadata_:wayback_capture_timestamp]:- "2022-01-27 10:08:20"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220127100820id_/https://magic.wizards.com/en/articles/archive/latest-developments/watch-out-two-headed-giants-2008-03-14"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/watch-out-two-headed-giants-2008-03-14"
---


Watch Out for Two-Headed Giants!
================================



 Posted in **Latest Developments**
 on March 14, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low












In a **Magic** world like Lorwyn or Dominaria, "Watch out for two-headed giants!" is just plain good advice. But in **Magic** development, the advice is just as sound. It's easy to find yourself focusing on two-player **Magic** during development, and that is how we test most often. But it's also important for us to make fun cards for Two-Headed Giant (2 vs. 2), [Emperor](/en/articles/archive/serious-fun/emperor-imperatives-2003-11-25) (3 vs. 3), Free-for-All, and other multiplayer **Magic** formats, and we make that a high priority. For more about Two-Headed Giant, see the sidebar below.


One of many times these topics come up is late in a set's development, when developers are working with the set's editor to finalize the last little details of cards' rules text. Up until this point, it's easy to gloss over "Target opponent lose 2 life" and "Each opponent loses 2 life" as if they say the same thing, because in two-player **Magic**, they do mean the same thing. But once you're sitting at a six-person free-for-all table, the words "each opponent" and "target opponent" suddenly mean extremely different things.


We intentionally select which one of those multiplayer-relevant wordings we want on every single card where the opportunity appears. And the reasons to choose one wording over the other can be very subtle from card to card. *Morningtide*, for example, is packed full of cards that could have worked a couple of different ways in multiplayer **Magic**, and where we had certain reasons to select each multiplayer-relevant wording that we chose.


**Two-Headed Giant Rules**


You and your teammates sit next to each other and take your turns together.


You share a life total (which starts at 30), you share phases and turns, and you attack and block together.


You also get to talk over each move together, showing each other your cards in hand.


One of you is the dominant head, which only means that you get final say-so if the two of you refuse to make a decision which is required of the team in order for the game to advance.


The team that goes first skips their first draw step, as in regular **Magic**.


Games tend to take longer than individual duels, so matches are a one-game, winner-take-all affair.


So this week, I'm going to let you be the **Magic** developer. I'm going to give you the chance to decide which multiplayer wording you think is best on a variety of *Morningtide* cards. Then I'll show you which one we actually picked and why.

Just remember, while making the card play well in multiplayer, you don't want to mess up one of your other priorities for the card's word choice:


* You want the card to play well in two-player games.
* You want the card to read naturally.
* You want to keep the card's word count reasonably short.
* You want to note how the card will interact with [Shunt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shunt) and [Ivory Mask](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Mask) effects.
* You want to maximize the card's flavor.

Not an easy task.


Ready to develop *Morningtide*? Then here we go:


### Battletide Alchemist




|  |  |
| --- | --- |
| Battletide Alchemist #1
 3WW
 Creature - Kithkin Cleric
 3/4
 If a source would deal damage **to you**, prevent X of that damage, where X is the number of Clerics you control. | Battletide Alchemist #2
 3WW
 Creature - Kithkin Cleric
 3/4
 If a source would deal damage **to a player**, you may prevent X of that damage, where X is the number of Clerics you control. |

Have you made your choice?


Version #1 would be a fine card to make. But #2 is a better card to make. First of all, version #1 doesn't work at all in Two-Headed Giant (2HG). In 2HG, if I play Version #1, the opposing team can just choose to deal damage my teammate (they attack the whole team, but they choose which player their creatures deal damage to). No damage is prevented, and the Alchemist ends up doing nothing. Version #2 solves that by having the option to protect my teammate as well.


Version #2 is also more fun in free-for-all multiplayer. If you control the [Battletide Alchemist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battletide+Alchemist), you can protect or not protect whichever players you want. If someone is helping you or needs a hand, shields up—you can protect them. But if someone has been beating on you, or you just don't like them, shields down—they get damaged. This makes a lot of people want to stay on your good side! And if someone thinks you're going to shield them, chooses not to block, and then you suddenly drop the shields down and let them die... that's just hilarious.


 



![Battletide Alchemist](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Battletide+Alchemist)

### Nightshade Schemers




|  |  |
| --- | --- |
| Nightshade Schemers #1
 4B
 Creature - Faerie Wizard
 3/2
 Flying*Kinship* - At the beginning of your upkeep, you may look at the top card of your library. If it shares a creature type with Nightshade Schemers, you may reveal it. If you do, **target opponent** loses 2 life. | Nightshade Schemers #2
 4B
 Creature - Faerie Wizard
 3/2
 Flying*Kinship* - At the beginning of your upkeep, you may look at the top card of your library. If it shares a creature type with Nightshade Schemers, you may reveal it. If you do, **each opponent** loses 2 life. |

Have you made your choice?


This choice is a one word difference that means nothing in two-player **Magic**, but means a lot in multiplayer, whether free-for-all, Emperor, or 2HG. Both wordings are the same length, have the same flavor, and read just as naturally. Since it's a tie on every other measure, and the power-level boost in multiplayer is not broken by any means, just a fun little boost, it's a good idea to take the more fun multiplayer path and let it hit each opponent. We made the same choice on *Morningtide*'s [Ink Dissolver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ink+Dissolver) and [Squeaking Pie Grubfellows](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squeaking+Pie+Grubfellows).



![Nightshade Schemers](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nightshade+Schemers)

### Greatbow Doyen




|  |  |
| --- | --- |
| Greatbow Doyen #1
 4G
 Creature - Elf Archer
 Other Archer creatures you control get +1/+1.
 Whenever an Archer you control deals damage to a creature, that Archer deals that much damage to **target player**. | Greatbow Doyen #2
 4G
 Creature - Elf Archer
 Other Archer creatures you control get +1/+1.
 Whenever an Archer you control deals damage to a creature, that Archer deals that much damage to **that creature's controller**. |

Have you made your choice?


Here's another case where the wordings function identically in two-player **Magic**, and they are basically the same length. So should we choose the more powerful-in-multiplayer version (#1) like we did with [Nightshade Schemers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightshade+Schemers)?


In this case, actually, no. Version #1 is more flexible and open-ended. But #2 is the better choice to print here. The reason is flavor. The [Greatbow Doyen](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greatbow+Doyen) teaches his archer followers to shoot their arrows *through* enemy creatures straight into those creatures' controller. That's the cool part. Shooting through John's creatures to hit Paul isn't nearly as satisfying flavor-wise.



![Greatbow Doyen](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Greatbow+Doyen)

### Burrenton Shield-Bearers




|  |  |
| --- | --- |
| Burrenton Shield-Bearers #1
 4W
 Creature - Kithkin Soldier
 3/3
 Whenever Burrenton Shield-Bearers attacks, **target creature** gets +0/+3 until end of turn. | Burrenton Shield-Bearers #2
 4W
 Creature - Kithkin Soldier
 3/3
 Whenever Burrenton Shield-Bearers attacks, **target creature you control** gets +0/+3 until end of turn. |

Have you made your choice?


In two-player games, these are basically the same. #1 plays a little better in Two-Headed Giant, because you can pump up your teammate's creatures while the two of you are attacking simultaneously. Unlike the relevance of the [Battletide Alchemist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battletide+Alchemist) word choice, This is such a tiny tiny gameplay benefit that it wouldn't be worth it if it took any more words to give the improved 2HG gameplay. Fortunately, #1 is actually shorter in words, and reads very naturally, so it is the better choice to print.


 



![Burrenton Shield-Bearers](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Burrenton+Shield-Bearers)

### Sage of Fables




|  |  |
| --- | --- |
| Sage of Fables #1
 2U
 Creature - Merfolk Wizard
 2/2**Each other Wizard creature you control** comes into play with an additional +1/+1 counter on it.
 2, Remove a +1/+1 counter from a creature you control: Draw a card. | Sage of Fables #2
 2U
 Creature - Merfolk Wizard
 2/2**Each other Wizard creature** comes into play with an additional +1/+1 counter on it.
 2, Remove a +1/+1 counter from a creature you control: Draw a card. |

Have you made your choice?


Version #2 would allow your 2HG or Emperor teammate to benefit from your [Sage of Fables](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) with his or her Wizards. And that seems like a positive. But be careful: #2 would play much worse in two-player games, because it adds +1/+1 counters to all your *opponent's* Wizards. In [Ask Wizards on January 15](/en/articles/archive/ask-wizards-january-2008-2008-01-01), I gave our reasons for why we switched from *Invasion*'s [Elvish Champion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Champion) pumping all Elves to *Lorwyn*'s [Imperious Perfect](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperious+Perfect) pumping only your own Elves. Those same reasons apply here, and are well worth staying away from pumping your opponents wizards with #2. Version #1 is the better choice.


 



![Sage of Fables](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sage+of+Fables)

### Cenn's Tactician




|  |  |
| --- | --- |
| Cenn's Tactician #1
 W
 Creature - Kithkin Soldier
 1/1
 W, T: Put a +1/+1 counter on **target Soldier creature you control**.
 Each creature you control with a +1/+1 counter on it can block an additional creature. | Cenn's Tactician #2
 W
 Creature - Kithkin Soldier
 1/1
 W, T: Put a +1/+1 counter on **target Soldier creature**.
 Each creature you control with a +1/+1 counter on it can block an additional creature. |

Have you made your choice?


At first, this seems to be the same category as [Sage of Fables](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables), which would suggest that Version #1's "you control" is important on the counter-adding ability here. [Cenn's Tactician](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cenn%27s+Tactician) is even part of the same loose cycle of uncommon "class lords" that give +1/+1 counters, along with [Sage of Fables](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables), [Bramblewood Paragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon), [Rage Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rage+Forger), and [Oona's Blackguard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard), all of which use "each other [creature type] creature you control" like #1.


For [Cenn's Tactician](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cenn%27s+Tactician) however, Version #2 (without "you control" on the counter-adding ability) is actually the better choice to print. The difference is that [Cenn's Tactician](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cenn%27s+Tactician)'s counter-giving ability is used only when you tap it, not automatic like the other four "class lords," so there is no danger that you will pump up opposing Soldiers. Once you've realized that, you might as well go with the shorter template on the counter-giving ability here, which is the one that omits "you control." Just like [Burrenton Shield-Bearers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burrenton+Shield-Bearers), the counter-giving ability reads very naturally without "you control." And there are a couple of wacky reasons in **Magic** you'd [Hunter of Eyeblights](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Hunter%2Bof%2BEyeblights) to [Cytoplast Manipulator](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Cytoplast%2BManipulator) to [Experiment Kraj](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Experiment%2BKraj).


As for the multiple-blocking ability (which is coincidentally, on-theme, being the ability of the original [Two-Headed Giant of Foriys](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Two-Headed+Giant+of+Foriys)), this one should definitely be "you control" to avoid your lord annoyingly pumping up enemy creatures like [Elvish Champion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Champion) does.


 



![Cenn's Tactician](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cenn%27s+Tactician)

### Notorious Throng




|  |  |
| --- | --- |
| Notorious Throng #1
 3U
 Tribal Sorcery - Rogue
 Prowl 5U *(You may play this for its prowl cost if you dealt combat damage to a player this turn with a Rogue.)*
 Put X 1/1 black Faerie Rogue creature tokens with flying into play, where X is the damage **dealt to target player** this turn. If Notorious Throng's prowl cost was paid, take an extra turn after this one. | Notorious Throng #2
 3U
 Tribal Sorcery - Rogue
 Prowl 5U *(You may play this for its prowl cost if you dealt combat damage to a player this turn with a Rogue.)*
 Put X 1/1 black Faerie Rogue creature tokens with flying into play, where X is the damage **dealt to your opponents** this turn. If Notorious Throng's prowl cost was paid, take an extra turn after this one. |

Have you made your choice?


Here the flavor is the same either way. But the potential combos in multiplayer are way more fun with version #2. [Sizzle](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sizzle) + [Notorious Throng](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Notorious+Throng). [Mind Bomb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Bomb) + [Notorious Throng](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Notorious+Throng)! It's worth enabling people to build those multiplayer decks. Version #2 is the better choice.



![Notorious Throng](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Notorious+Throng)

### Revive the Fallen




|  |  |
| --- | --- |
| Revive the Fallen #1
 1B
 Sorcery
 Return target creature card **from your graveyard to your hand**. Clash with an opponent. If you win, return Revive the Fallen to its owner's hand. *(Each clashing player reveals the top card of his or her library, then puts that card on the top or bottom. A player wins if his or her card had a higher converted mana cost.)* | Revive the Fallen #2
 1B
 Sorcery
 Return target creature card **in a graveyard to its owner's hand**. Clash with an opponent. If you win, return Revive the Fallen to its owner's hand. *(Each clashing player reveals the top card of his or her library, then puts that card on the top or bottom. A player wins if his or her card had a higher converted mana cost.)* |

Have you made your choice?


This choice has its own development story. One of the goals of *Future Sight* was to try out various experiments from hypothetical futures of **Magic**. One such experiment was [Grave Scrabbler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave+Scrabbler). Besides his madness trigger, [Grave Scrabbler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave+Scrabbler) also had the experimental [Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) template of being able to return any player's creature card to its owner's hand, not just your own. It's very easy to miss this weird [Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) version on [Grave Scrabbler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave+Scrabbler), but we got feedback from several Two-Headed Giant and free-for-all players that thought it was cool to be able to help out their teammates or friends.


Since that one worked out, we decided to continue the experiment by bringing a "[Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) for anyone" from *Future Sight* into "present-time" **Magic**. It is admittedly a little clunkier, and we'll see how this one plays out. If people say they like it, we'll do more in the future. If they find it too unnatural or bizarre, we will back down to regular [Raise Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead).



![Revive the Fallen](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Revive+the+Fallen)

### Gilt-Leaf Archdruid




|  |  |
| --- | --- |
| Gilt-Leaf Archdruid #1
 3GG
 Creature - Elf Druid
 3/3
 Whenever you play a Druid spell, you may draw a card.
 Tap seven untapped Druids you control: Gain control of all lands **target player controls**. | Gilt-Leaf Archdruid #2
 3GG
 Creature - Elf Druid
 3/3
 Whenever you play a Druid spell, you may draw a card.
 Tap seven untapped Druids you control: Gain control of all lands **controlled by other players**. |

Have you made your choice?


Combos that kill one person in multiplayer are way more fun than combos that kill all the opponents at once. When a combo suddenly kills one person, it's like, "Holy crap! He's going crazy! Somebody kill that guy before he untaps again!" and you get an exciting struggle to defuse the doomsday device before more players fall. But when the combo is "And now I can do infinite damage to an infinite number of target players, so... I do," then you lose that exciting endgame.


You might give them an awesome surprise the first time, but once other players in multiplayer know you're planning to activate [Gilt-Leaf Archdruid](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilt-Leaf+Archdruid), they have some opportunities to kill your Druids to stop you before you get up to seven Druids. And if it said "Gain control of all lands," then they certainly would stop you. But if it just takes one player's lands, you might be able to convince Jeff to help your Druids stay alive just long enough for you to steal Joey's lands before he wins. And then right when you activate the Archdruid, you hesitate and say, "Maybe I'll steal all of *Jeff's* lands." That mind-game maneuvering gets lost if it takes everyone's lands at once. For these reasons, I strongly prefer #1 here.



![Gilt-Leaf Archdruid](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gilt-Leaf+Archdruid)

### Boldwyr Heavyweights




|  |  |
| --- | --- |
| Boldwyr Heavyweights #1
 2RR
 Creature - Giant Warrior
 Trample
 When Boldwyr Heavyweights comes into play, **each opponent** may search his or her library for a creature card and put it into play. Then each player who searched his or her library this way shuffles it. | Boldwyr Heavyweights #2
 2RR
 Creature - Giant Warrior
 Trample
 When Boldwyr Heavyweights comes into play, **each other player** may search his or her library for a creature card and put it into play. Then each player who searched his or her library this way shuffles it. |

Have you made your choice?


Version #2 would create powerful multiplayer combo, especially in team Constructed multiplayer formats like Emperor or some 2HG games, since your allies would get to tutor for a creature for free too. In general we do like little multiplayer boosts on cards. The problem is that this combo would actually be absurdly powerful, to the point of being stupid. Imagine you are playing casual 2HG Standard Constructed with a friend against another team of two.


On turn four, Enemy A plays [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights). You fetch [Troll Ascetic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Troll+Ascetic), and your ally fetches [Ohran Viper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ohran+Viper). Enemy B fetches and plays for free another [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights). This makes enemy A fetch and play for free another [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights). This makes enemy B fetch and play another [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights). Each team in Two-Headed Giant Constructed is restricted to four copies of a given card, so your team now has four [Troll Ascetic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Troll+Ascetic)s and four [Ohran Viper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ohran+Viper)s, and your opponents have four 8/8 tramplers. Then they cap it off by fetching [Akroma, Angel of Wrath](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%2C+Angel+of+Wrath) and attacking.


Or maybe the enemy who didn't tap out to pay ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) for [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights) this turn plays something like Ashling's Perogative or [Emblem of the Warmind](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emblem+of+the+Warmind) to give haste to all thirty-two trampling power of four [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights), who immediately come over and kill you (or come very close and wipe out your team) on turn four.


Whew! It's a really cool story to think about and talk about. And there are certainly lots of [Shriekmaw](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shriekmaw)s you can imagine having in your own decks that would shut it down. But it would eventually get old that the enemy team was quadruple-tutoring up this ludicrous, bizarre, lethal combo for just ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif). And if you can believe it, having the Emperor play [Boldwyr Heavyweights](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boldwyr+Heavyweights) in "range 1" Emperor **Magic** is even more broken. In any case, version #1 ends up being the better version to make.


And there's an appropriate final spokesgiant for Giant Week.



![Boldwyr Heavyweights](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boldwyr+Heavyweights)

 


Now you know what it means to "Watch out for two-headed giants!" in **Magic** development. I hope you've seen how even the tiniest details of these cards' wordings are actually made very intentionally, for a variety of subtle reasons, including maximizing the fun of Multiplayer **Magic**.


### Last Week's Poll




| **What do you think of the new Extended rotation policy?** |
| Good Idea | 4855 | 60.1% |
| Pretty Reasonable | 2621 | 32.4% |
| Bad Idea | 605 | 7.5% |
| **Total** | **8081** | **100.0%** |

The results are in. With over 8,000 voters chiming in, over 92% percent of respondents called the new Extended rotation policy "Pretty Reasonable" or a "Good Idea." I'm happy to hear it. 


[The survey originally included in this article has been removed.]








