
---
[Link to Wayback Machine](https://web.archive.org/web/20220121125136/https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "It's Gruul Week, and where would we be if that didn't mean talking about one of the most basic interactions in Magic: attacking and blocking. I briefly considered writing a long string of incoherent words and drawing crude diagrams, but the guild letter hit that note hard, and like all good writers, I fear retribution from my up-to-now benevolent editors for attempting to"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "197721"
[_metadata_:path_date]:- "2013-03-05"
[_metadata_:publish_date]:- "2013-03-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing the Attack Step"
[_metadata_:wayback_capture_timestamp]:- "2022-01-21 12:51:36"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220121125136id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05"
---


Developing the Attack Step
==========================



 Posted in **Latest Developments**
 on March 8, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






It's Gruul Week, and where would we be if that didn't mean talking about one of the most basic interactions in **Magic**: attacking and blocking. I briefly considered writing a long string of incoherent words and drawing crude diagrams, but the guild letter hit that note hard, and like all good writers, I fear retribution from my up-to-now benevolent editors for attempting to shirk my duties. So, instead, I'll be discussing some of the intricacies of the attack step, with a special eye on how it impacted the development of Gruul. 

![](https://media.wizards.com/images/magic/daily/ld/ld237_ruination_wurm.jpg)  
**Magic** developers are probably most closely associated with the kind of player who enjoys long control games or tight tempo races, but there are more than a few of us who like to let the beast out every once in a while and get a good smashing on. For the last several years, we have worked to move the major action of the game more onto the battlefield and out of players' hands, and that means making the interactions on the battlefield more meaningful. Planeswalkers being attackable, for one example, have created a greater necessity for most decks to have some kind of creature offense available to them, and that pushes more interaction on the battlefield. 

 I believe that moving the action to the battlefield shouldn't be associated with dumbing down the game, however. It is the task of development to create a fun and dynamic and robust game where players are able to interact meaningfully with not just their hands, but on the battlefield as well. I think it is important to note the disassociation of the concepts of simplicity and strategically deep game play. One of the things [New World Order](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/172) strives for is to make the game more simple at the most basic level, but to also increase the overall strategic depth of the game. I believe we have done this by harnessing many of the tools **Magic** already had available to it, but doing so in a more thoughtful way than we once did. 

![](https://media.wizards.com/images/magic/daily/ld/ld237_clan_defiance.jpg)  
A Beautiful Asymmetry
 One of the most fruitful things [Richard Garfield](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Richard%20Garfield) built into the original version of **Magic** was different values for power and toughness (and not just power when attacking and power when defending). While it seems obvious now, it certainly wasn't a guarantee to be in the game. Plenty of games pre- and post- **Magic** used one stat for combat. The direction **Magic** went certainly adds some complexity but also a lot of interesting game play. It also lets development make a lot of small tweaks to get cards to the right power levels and to make playing the game more interesting. 

To give an example, let's say we are just playing with creatures with square stats. You have out two 2/2 vanillas, and I have out a 4/4 vanilla. You can't attack me, and I am able to attack and trade my creature for both of your creatures (if you want to make the trade). Now let's look at options for making these creatures non-square. Moving even one of the 2/2s into a 2/3 all of a sudden turns the trade unprofitable for me—my much-larger creature now only trades for one of yours. If my creature was a 3/5, however, I can now freely attack through both of your creatures, assuming there are no combat tricks. Turning my creature into a 4/3 doesn't change its power in the first example, but now it will trade with a 3/1, if you have it. Development makes sure to populate a set with a fruitful number of different power and toughness combinations to ensure that even without a single instant, we can create a good deal of variation, and decisions, in game play. It also lets us tweak the individual strength of creatures by increasing or reducing their stats to trend toward them dying more often from combat, surviving more often from combat, or being better at trading with other creatures in combat.

 When a **Magic** set is turned over from design to development, design generally has the common creatures pretty well balanced on an individual scale for Limited, but it tends to bias away from the simple interactions I discussed above and focus more on whatever the main theme of the set is. That's good, though. Design sets out to create a bold and new vision of what Limited and Constructed should play like, and it is up to development to both make that vision a reality and to figure out how to make that line up with what is expected out of a finished **Magic** set. 



|  |  |
| --- | --- |
|  |  |

  
 Development's first job is to really put the set through its paces in Limited and create an environment full of dynamic interaction, and a lot of that work goes into the seemingly unexciting work of spreading out power and toughness in a way that gives as much game play as possible. If all of the powerful creatures in a set were simply [Grizzly Bears](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) or [Hill Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hill+Giant)s with abilities, **Magic** would become stale very quickly. Making sure the powerful creatures appear at various sizes and various spots on the mana curve alone helps to make a more dynamic environment, with more interesting combat decisions. One of the things, at least for Limited, that development does is figure out ways to reduce the word count in the set and add interaction with important power-and-toughness-combination creatures. Design files are rarely full of vanilla cards like [Pillarfield Ox](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox), [Catacomb Slug](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Catacomb+Slug), or [Horned Turtle](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horned+Turtle), but they are part of the glue that really holds Limited together. Development tries to figure out when and where these are needed and adds them to the set, generally filling in much-needed gaps in a color's curve. 

![](https://media.wizards.com/images/magic/daily/ld/ld237_combo01.jpg)  
 The Tricks of the Trade 
*Gatecrash* is a study in power/toughness asymmetry in **Magic**. Two of the mechanics in the set—bloodrush and evolve—rely heavily on the game play that asymmetrical stats bring up. It was interesting to watch people come around to how powerful [Elusive Krasis](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elusive+Krasis) was in the evolve deck, not just because it was unblockable, but because at 0/4 it is both likely to evolve all of your other creatures and to be evolved by almost all of your future creatures. The evolve deck also pushes you away from playing a lot of the same creatures and toward a greater variety of power and toughness so evolve happens more frequently. 

 This isn't Simic Week, though, so let's get back to the guild at hand—Gruul. And what does Gruul like to do? Gruul smash! 

![](https://media.wizards.com/images/magic/daily/ld/ld237_hulk.jpg)  
Gruul wants its creatures to ABA. A—always. B—be. A—attacking. Always be attacking. If you aren't attacking, you are losing. If you aren't attacking, your opponent is getting a foothold. If you aren't attacking, you can't crush your opponents underneath your feet. You attack, or you hit the bricks. But, uh, anyway, getting back to the subject at hand, one of the keys to making Gruul work was to make sure that attacking with Gruul was the easier decision and blocking was the harder one. It's what bloodrush excels at doing.

![](https://media.wizards.com/images/magic/daily/ld/ld237_combo02.jpg)  
 Bloodrush creatures on the whole have different power and toughness to make blocking decisions more difficult and to better tweak their usefulness as creatures on the battlefield or combat tricks in the hand. If your opponent knew he or she was always playing around +2/+2 or +3/+3, he or she could more easily make optimal decisions on how to block, but Bloodrush was developed to not make those decisions easy. [Scorchwalker](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scorchwalker) is perhaps the poster child for this duality. It is rare that a 5/1 for four has much usefulness on the battlefield, or that a +5/+1 combat trick for three would be a particularly high pick, but the combination of the two on the same card really gets things going. Because all of the bloodrush creatures are playable in either form, your opponent has to at least respect all of them when you attack with your [Slaughterhorn](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slaughterhorn) and [Ember Beast](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ember+Beast). Some are intended to more heavily punish blocking with multiple creatures, some are better at punishing you for blocking with one large creature, and others punish for not blocking at all. The mechanic highlights Gruul as the guild of straightforwardness in attacking, while at the same time creating interesting game-play interactions with the other guilds. 

Dynamic Defense
 Gruul is all about attacking, but we've put in more than a few ways to prevent it from dominating the format—after all, that wouldn't be very interesting. The impulsivity and aggressiveness of Gruul is it greatest strength, but is also what gives its opponents the best opening to defeat it. While the Gruul may be able to dodge counterspells, any removal in response to a creature being bloodrushed is devastating, and we made sure to place a few pieces that are more specifically geared toward the Gruul menace. The first, and most obvious in Limited, is [Smite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite). You could almost say it is perfectly placed to counter bloodrush (interesting, that). While [Smite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite) is a generally powerful Limited card in a vacuum, it is the density of combat tricks in *Gatecrash* and their importance to the Gruul strategy that really pushes it over the edge here. The key weakness of Gruul is that it will rely on combat tricks, not just larger creatures, to win in combat, so removal in response to bloodrush will get you a two-for-one. Without any strong card-drawing or evasion to make up for the loss in tempo, Gruul will have a harder time than other colors coming back from that. 

![](https://media.wizards.com/images/magic/daily/ld/ld237_combo03.jpg)  
 The second card is [Ætherize](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therize). Although it is an uncommon, and won't show up as much as [Smite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite), it has the benefit of not only negating blocked attackers, but unblocked creatures as well. Whenever a blue player presents the Gruul player with the perfect opportunity for a [Scorchwalker](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scorchwalker) or [Zhur-Taa Swine](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zhur-Taa+Swine) to end the game, the Gruul player will have to weigh taking his or her shot at it, and how far behind an [Ætherize](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therize) will put the player. 

 In Constructed, Bloodrush cards like [Ghor-Clan Rampager](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghor-Clan+Rampager) excel at giving decks super-efficient answers to powerful blockers like [Thragtusk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thragtusk), [Boros Reckoner](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner), and [Restoration Angel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Restoration+Angel), but it is similarly weak to cards like [Azorius Charm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Charm) or, often, just [Searing Spear](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear). One thing we enjoy is creating cards that both are trumps and have trumps to different strategies and cards. It is one of the things that keeps Standard moving as a format and, hopefully, keeps it new and interesting for players week after week. 

Looking Forward


|  |  |
| --- | --- |
|  |  |

  
 Bloodrush works wonderfully in the confines of *Gatecrash* Limited, but it is destined for larger things than just that. When *Dragon's Maze* comes out, we hope you will find even more fun interactions with bloodrush in Limited, combining it with familiar cards in *Return to Ravnica*. It could be bloodrushing a [Fencing Ace](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fencing+Ace) on turn three with [Scorchwalker](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scorchwalker) to take a more-than-healthy chunk out of your opponent's life total, or using Faerie Imposter to return a [Slaughterhorn](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slaughterhorn) that has outlived his usefulness on the battlefield and is ready to assist in combat from your hand. And all of that is without even touching the goodies that *Dragon's Maze* adds to the mix. As much as I am enjoying *Gatecrash* Limited, I'm looking forward to everyone being able to enjoy the full block as well. 

![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Top.jpg)![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_leftOfButton.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Button_Static.jpg)](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/league-facts)![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_RightOfButton.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Bottom_Static.jpg)](http://archive.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/gatecrash)  
  
  
  
![](https://media.wizards.com/images/magic/daily/footers/slice1.jpg)![](https://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)![Sam Stoddard](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg) **Sam Stoddard**[@SamStod](https://twitter.com/SamStod)[Email Sam](/company/emailtoauthor.asp?author=Sam%20Stoddardamp;amp;headline=%5BDeveloping%20the%20Attack%20Step%5D "Click to send email to the author.") | [Author Archive](http://staging.wizards.com/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard)[Latest Developments Archive](/Magic/Magazine/Archive.aspx?tag=Latest%20Developmentsamp;description=Latest%20Developments) |  
 Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 







