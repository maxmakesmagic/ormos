
---
[Link to Wayback Machine](https://web.archive.org/web/20220627090630/https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Many Magic players have an image of Timmy as an excitable person who loves enormous creatures. While those people fall into the Timmy category, not all Timmies look like that. Timmies want their games to take them on emotional rides, but not all Timmies want the same ride, and some Timmies even want to engineer an unpleasant ride to take their opponents on. `The Yang of Timmy`"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "647116"
[_metadata_:publish_date]:- "2009-12-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Yang of Timmy"
[_metadata_:wayback_capture_timestamp]:- "2022-06-27 09:06:30"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220627090630id_/https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25"
---


The Yang of Timmy
=================



 Posted in **Latest Developments**
 on December 25, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







*Many **Magic** players have an image of Timmy as an excitable person who loves enormous creatures. While those people fall into the Timmy category, not all Timmies look like that. Timmies want their games to take them on emotional rides, but not all Timmies want the same ride, and some Timmies even want to engineer an unpleasant ride to take their opponents on. "The Yang of Timmy" talks about "griefers," which is a word many gaming communities use to describe exactly that kind of player.*


*This article originally ran on March 13, 2009.*


By this point in Timmy Week, Timmy himself needs little introduction. Mark Rosewater talked about [designing for Timmy](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/29) on Monday and Kelly set out [a manifesto for Timmy](/en/articles/archive/serious-fun/timmy-manifesto-2009-03-10) on Tuesday. You might think that now you know everything there is to know about Timmy, but he also has a dark side that no one else this week has been willing to expose. Today I'll talk about how we develop for the four subtypes of Timmies that Kelly talked about on Tuesday, then I'll talk about a different and more sinister kind of Timmy that you might not have thought of as a Timmy before.


### Power Gamers


I don't think I can top Kelly's description of power gamers from his Tuesday article: "Power gamers are all about huge plays and giant monsters. They want the biggest, the dumbest, the craziest, and the coolest. They want dragons. They want Ultimatums. They want three planeswalker ultimates to go off in one turn." **Magic** developers are very good at identifying power level, and we have detailed metrics that we use to evaluate card power both in Limited and Constructed. However, it's much more difficult to measure how much raw excitement cards create.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_awesomePoll.jpg)To get a picture of how exciting cards are, we use a tool that we uncreatively call "the rare poll." Early in each set's development, we send employees from all over the company a poll that asks them to rate all the rares and mythic rares in that set on a scale from 1 to 10. That data gives us a much better picture of what cards tickle people's inner Timmy. When a card that we thought would be exciting does well on the poll, we protect it. When such a card does poorly instead, we tweak it to make it more appealing to that audience.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_partyCard.jpg)One card that benefited from the rare poll is [Progenitus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus). There was a point in *Conflux* development where some people thought that it should not be a 10/10. The card was already insane enough, they argued, because of the line "protection from everything," and did not need to kill in two hits. *Conflux* lead developer Mike Turian knew that the card was a top 10 finisher in the rare poll and knew that the card had very little danger of being a power level problem for tournament **Magic**, so he let it go as a 10/10 to make sure that it read as the most ridiculous possible card.


### Social Gamers


Social gamers are people who use **Magic** mainly as a social outlet. They tend to play multiplayer formats that involve lots of people and their primary goal is for everyone to have fun. It's hard for us to develop for social gamers, largely because they are perfectly willing to develop for themselves by making house rules banning particular things. You might find a group of social gamers who despise time-consuming search effects, mass land destruction, or [Congregate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Congregate), and just outright ban the offending card or cards. Those players do a better job of developing for themselves than we ever could.


The biggest thing that we do as developers for social gamers is to give cards extra functionality in multiplayer when we can do that without making the card more complicated than we would like. For example, [Hit](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Hit) gained the ability to key off of a teammate's creatures, [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) lets you remove one card each from two different graveyards, and [Cryptic Command](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command) taps creatures controlled by all your opponents. Another example of a card that gained from this is Silence from [***Magic** 2010*](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/27a), which stops all your opponents from playing spells.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_silence.jpg)### Diversity Gamers


Diversity gamers are players who want **Magic** to be a new experience every time they play it. They need constant change to stay interested. We serve diversity gamers by making sure that **Magic** offers plenty of different things to do. We try to make each set pull players in different directions, so over time diversity gamers will naturally experience many different things. They will also find that each set's different themes can be taken in different directions. For example, some of the Merfolk in *Lorwyn* and *Morningtide* gave players tools to mill their opponent with, but they also supported a simpler beatdown merfolk deck. This allows players who value diversity to build different kinds of decks within the same block theme.


 




|  |  |
| --- | --- |
| 
Drowner of Secrets
 | 
Streambed Aquitects
 |

### Adrenalin Gamers


Adrenalin gamers are people who enjoy tense situations that have very high variance. It's lots of fun for them to wait in suspense while they find out whether or not something awesome happened. We develop for adrenalin gamers by making sure that we protect exciting cards that produce those kinds of games. One great example of this category of card is Capricious Efreet from ***Magic** 2010*, which Aaron Forsythe previewed when he [announced that set](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/27a). At one point its text box looked like this:



> 
> At the beginning of your upkeep, choose target permanent you control and up to two target permanents you don't control. Destroy one of them at random.
> 
> 
> 


**Magic** designer and ***Magic** 2010* development team member Greg Marques noticed that the obvious use of this card is to target one of your own lands and two of your opponent's nonlands. Most of the time you'll kill one of your opponent's permanents, and some of the time you'll kill your own land. Greg complained that this was hardly a moment of tension at all, and that the card wasn't very fun for this kind of Timmy because there was no real way anything could go wrong. We added "nonland" to the card to increase the tension, and Greg and other adrenalin Timmies like him became much happier.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_efreet.jpg)That's all I have to say about the kinds of Timmies you've met so far this week. Now it's time to introduce you to a kind of Timmy that you may not have thought of as a Timmy before.


### Griefer Timmies


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_bondOfAgony.jpg)Just like other Timmies, "griefers"—a term that comes from online games—are looking to experience something. Unlike other Timmies, however, the experience that the griefers want is the experience of their opponents squirming in misery. They are at their very happiest when their opponents are miserable. Griefers cackle with glee when they hit your best card with a [Millstone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Millstone), and they feel deeply cheated when an opponent who has no permanents concedes even though the griefer has no plans to actually win anytime soon. His goal is to make you sad, and he gets a kick out of your sadness.


One classic griefer strategy is land destruction. The dream there is that the opponent will be stuck staring wistfully at a hand full of cards that he can't play. Another strategy that griefer Timmies I grew up with loved was counterspells. Some Magic players use counterspells to stop threats that they can't deal with otherwise, but griefer Timmy is excited about counterspells because he can use them to stop every card his opopnent ever plays in an entire game. Timmy doesn't play eight counterspells; he plays plays twenty-eight of them. The joy of those strategies isn't that they are powerful or lead to winning the game. It is only that the opponent can't do what he wants to, and a sad opponent makes for a happy griefer.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_counterDeck.jpg)We are not afraid to print individual cards for griefer Timmy. Two classic examples of these cards are [Glimpse the Unthinkable](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glimpse+the+Unthinkable) and [Haunting Echoes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Echoes). Griefer Timmy loves milling because everyone gets to see the fun and exciting cards that his opponent won't play this game, and ten cards milled for only two mana is awesome. [Haunting Echoes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Echoes) is somewhat similar in that it gives griefer Timmy the chance to take away his opponent's cards in a very public way. However, a player whose graveyard is full when they get hit by a [Haunting Echoes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Echoes) must play the rest of the game with a deck largely devoid of action spells, which is demoralizing and annoying. That's exactly what griefer Timmy wants out of a card.


 




|  |  |
| --- | --- |
| 
Glimpse the Unthinkable
 | 
Haunting Echoes
 |

Griefer Timmy doesn't need his cards to be powerful as long as they are sufficiently annoying. One classic combination that griefer Timmy loves is [Noble Benefactor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Benefactor) and [Lobotomy](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lobotomy). Everyone is happy when [Noble Benefactor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Benefactor) lets everyone get their favorite card, but griefer Timmy isn't interested in getting an awesome card of his own. Instead, he wants you to tell him what your favorite card in your deck is, then rip that card out of your deck entirely with [Lobotomy](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lobotomy). This is a lot of work to go through for something that isn't particularly powerful, but griefer Timmy is happy to do it as long as it makes you sad.


 




|  |  |
| --- | --- |
| 
Noble Benefactor
 | 
Lobotomy
 |

In some ways, from our perspective the ideal card for griefer Timmy is one that he thinks annoys his opponents a lot but actually doesn't annoy them too much. Those cards allow griefer Timmy to be happy because he gets to mess with other people, but don't hurt other players' experiences excessively. On the other hand, it is important for griefer Timmy that he feels like his efforts reward him with his opponents' misery, so we have to make sure that he does manage to annoy his opponents some of the time.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_silence2.jpg)Sometimes people who work on **Magic** fight to kill cards that enable griefing. Extremely annoying cards sometimes don't survive, but other times those people's efforts are thwarted because we want to make griefer Timmies happy too. One instance of this from ***Magic** 2010* is Silence, another one of the cards that Aaron Forsythe previewed in his announcement. Former Building on a Budget author and R&D member Nate Heiss argued that the card was a very bad thing to print because it was both miserable and powerful in tournament constructed, and he built tons decks that included it. He would then play them against various people to try to prove his point.


Nate's decks tended to include a bunch of little creatures, some removal spells, and Silences. He would curve out with some creatures and then Silence his opponent during upkeep when he thought his opponent might cast a spell. He would then try to convince his opponents that they were annoyed, but mostly they would just draw their card, play a land, and then wait a turn to play their spells. Sometimes, his opponents even had the audacity to respond to his Silences with instant removal spells, in which case the Silence didn't hurt them very much at all. Other times, both Nate and his opponent would create a creature stall, and when he drew a Silence in that situation he was effectively down a card.


In the end, Nate's efforts did not stop the card, and ironically convinced the ***Magic** 2010* development team that the card was a great idea to print. He showed us that Silence wasn't going to be too powerful when used merely to grief people and that Silence would make people who enjoyed griefing very excited. Nate never really came around to this view, but the card made it out the door intact.


This story is beautiful to me because even though Nate was griefing us relentlessly, he wasn't doing it because he enjoyed it. Instead, he was doing it because he thought it was his responsibility to keep everyone else from doing it. In the process, however, he became exactly the thing that he hated. When the **Magic** web team heard this story, they dubbed Nate "the Rorschach of griefing," which is hilarious and awesome.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld29_whoWatches.jpg)Even though griefer Timmy's goal is to make you sad, there is an effective way to deal with him. Simply refuse to be sad in the face of his tricks, and you will deny him his fun. Even more devastating, you can beat him while ignoring his efforts to annoy you. A griefer Timmy who neither wins the game nor makes his opponent miserable is a very sad griefer Timmy indeed. However, be very careful when you do this. If you enjoy a griefer Timmy's misery too much, you will become intimately familiar with the fun that a griefer Timmy can have and you might be tempted to become one yourself!


We've come to the end of Timmy week. If you are a Timmy, be proud of the big creatures and swingy moments you love. If not, be respectful of them now that you know what makes Timmy tick, and we'll have weeks devoted to your psychographic later this year.


### Last Week's Polls




|  |  |  |
| --- | --- | --- |
| **How many Pro Tour Qualifier tournaments have you played in?** |  |  |
| 0 | 2446 | 57.6% |
| 1 | 479 | 11.3% |
| 2 or 3 | 471 | 11.1% |
| 4, 5, or 6 | 276 | 6.5% |
| 7, 8, 9, or 10 | 157 | 3.7% |
| 11 or more | 419 | 9.9% |
| **Total** | **4248** | **100.0%** |


 

My intention for this poll was only to learn how many of my readers have actually played in [Pro Tour Qualifier](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/ptq) tournaments. I understand that competitive **Magic** is not for everyone. I also knew that last week I would be talking about the Pro Tour, so it seemed appropriate to ask how much of my audience had tried to qualify for one.


I was glad to see that people who had played in qualifiers seemed to do a good job of figuring out whether the qualifier scene was for them. The majority of players who had played in a qualifier either stopped after three or less or had continued on to play seven or more. We try to have diverse organized play offerings so that every player can find something they enjoy, and these results suggest that players who decided that qualifiers weren't fun for them found other arenas to play in rather than soldiering on in a world they didn't like. We couldn't be happier about that, and all we want for you is that you are having fun with **Magic** however you choose to play it.




|  |  |  |
| --- | --- | --- |
| **Did you follow the coverage of last weekend’s Pro Tour in Kyoto?** |  |  |
| I only read the text coverage. | 1772 | 41.6% |
| I read the text coverage and watched the live webcast. | 1348 | 31.7% |
| I didn't follow the coverage at all. | 925 | 21.7% |
| I only watched the live webcast. | 212 | 5.0% |
| **Total** | **4257** | **100.0%** |

I'm happy to see that many of you did watch at least some of the live webcast of [Pro Tour–Kyoto](/en/events/coverage/nassif-greater-power). I enjoy watching **Magic**, and there were some great games of **Magic** played on camera two weekends ago. In particular, [the Finals match](/en/articles/archive/event-coverage/finals-controlling-giant-2009-02-28) between Luis Scott-Vargas and Gabriel Nassif will go down in history as one of the great Pro Tour Finals matches and I fully expect both of them to one day be in the Pro Tour Hall of Fame. I recently found out that I'll be attending [Pro Tour–Honolulu](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/protour) as part of the coverage team, and I hope to be able to watch some **Magic** that good in person!








