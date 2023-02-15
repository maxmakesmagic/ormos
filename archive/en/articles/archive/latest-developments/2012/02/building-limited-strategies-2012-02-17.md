
---
[Link to Wayback Machine](https://web.archive.org/web/20170323230838/http://magic.wizards.com/en/articles/archive/latest-developments/building-limited-strategies-2012-02-17)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "&#13; I write my articles about a week ahead of time, which means that as I click away on this keyboard I'm lounging away in beautiful Honolulu, Hawaii. I know, I know, the life of a Magic developer is fraught with tribulation, hardship, and peril. They even FORGOT to provide me an umbrella with which to accessorize this here frosted tropical beverage. The horror!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644761"
[_metadata_:publish_date]:- "2012-02-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Building Limited Strategies"
[_metadata_:wayback_capture_timestamp]:- "2017-03-23 23:08:38"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170323230838id_/http://magic.wizards.com/en/articles/archive/latest-developments/building-limited-strategies-2012-02-17"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/building-limited-strategies-2012-02-17"
---


Building Limited Strategies
===========================



 Posted in **Latest Developments**
 on February 17, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 







I write my articles about a week ahead of time, which means that as I click away on this keyboard I'm lounging away in beautiful Honolulu, Hawaii. I know, I know, the life of a **Magic** developer is fraught with tribulation, hardship, and peril. They even FORGOT to provide me an umbrella with which to accessorize this here frosted tropical beverage. The horror!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld182_hi.jpg)I will rue this transgression until the day I die.


One thing I always try to do when I make it out to a Pro Tour is draft a few times with my friends on the PT circuit. Part of why I do this is to reassure myself that my skills haven't withered into nothingness now that I've been "on the inside" for nearly three years. (Spoiler Alert: they have.) ((Other spoiler alert: I am having a shame attack just thinking about it.)) (((*exempli gratia*: I attack my [Riot Devils](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riot+Devils) into a 2/2 [Boneyard Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boneyard+Wurm). He flashes back [Dream Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Twist). I damage my glasses due to the force of the ensuing facepalm.))) But it's also important for us to see if the Limited environment is playing out the way we intended. Are the enablers we seeded into the set actually taking off? Is there something we felt was powerful that actually doesn't cut the mustard? Are there mistakes we printed that we should avoid in the future? We can glean a lot of this data from **Magic Online**, of course, but nothing substitutes for the ability to sit down with some of the best players in the world and engage in good old-fashioned battle.


This whole process has me reflecting a lot on how we design the nuts and bolts of most Limited environments in the first place. We've talked a fair amount on **DailyMTG.com** about what factors lead to good Limited game play, but we haven't delved that far into what processes we undergo to ensure that game play happens.


I am about to use the word "wafting" for the first time in my life in print, which is the verb I'd select to describe what is happening with the ocean breeze, vis-à-vis my face right now. Suddenly I better understand the reactions people are having in shampoo commercials. I feel like my experience is being used as we speak to promote the Oahu tourism industry.


Ahem. I keep getting distracted.


Birdie!


::points::


If [Sanctuary Cat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctuary+Cat) were here, he could keep me focused, entranced by the soothing softness of his silken coat...




|  |
| --- |
|  |
| *"Come on, Man."* |


 

OH YES, LIMITED!


I remember.


Cards in a set, like words in a sentence, all need to serve a purpose. Now, sometimes that purpose is "be a context-independent cool thing," but the fact remains that you have very little wiggle-room in a set to include a card just because you've made up something awesome in your head. One of the most vital skills a developer can cultivate is the discipline to "put a card off"—to realize that even though a card is sweet, it doesn't quite fit in the current environment. Before I got to R&D, I assumed most of the time spent working on a set involved coming up with enough cool cards to populate it. Now I realize that's not really how it works. In fact, it's really easy to come up with 229 neat, appealing spells—almost too easy, in fact. Most of the work of late design/early development is getting rid of the goodie-bag feel a lot of files have.


No, most Limited formats improve when they're given direction—when nearly every card can be slotted into some kind of strategy. These strategies can be linear or open-ended, narrow or robust, but our goal is to ensure that as many pieces of real-estate as possible pull some weight. Because of that, one of the most important stages of a set's development comes very, very early in the process. Most draft environments encourage players to play two-color pairs, so the development team gets together in a room and maps out what each color combination is supposed to do. Usually, we assign a primary and secondary strategy to each pair. These can range from the very general (cast some creatures and attack with them, using combat tricks to push through damage) to the very specific (mill your library, survive with [Gnaw to the Bone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gnaw+to+the+Bone), then end the game with a backbreaking [Spider Spawning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spider+Spawning) or with [Memory's Journey](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory%27s+Journey)/[Runic Repetition](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runic+Repetition) recursion), the very straightforward (resolve [Burning Vengeance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Vengeance), then flashback some spells) to the very involved (survive with cheap tempo effects like [Sensory Deprivation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensory+Deprivation) and [Silent Departure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure) for long enough that your [Ghoulcaller's Bell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghoulcaller%27s+Bell)s chain into [Dream Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Twist)s and your Curses of the Bloody Tome can actually start to race your opponent's damage output). What's important is that they exist in the first place. Once these start to materialize, it becomes possible for us to figure out whether those purposes I just talked about are being addressed.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld182_curse.jpg)[Curse of the Bloody Tome](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Curse+of+the+Bloody+Tome) | Art by [Jaime Jones](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Jaime+Jones%22%5D)


Now, these strategies don't just emerge out of thin air. What often happens is that we play an early version of a set as-is and we look for things that have potential. The key at this stage is to try and ignore, as much as possible, concerns about individual card power or anomalous rarity distribution, and try to dig deeper in order to understand what really works. After all, you can push a "Tim" effect (or whatever) up to uncommon later, but you can't as easily seed an entire play pattern into a color. When we identify something that seems potentially fun, we figure out what *would* have to be true for that fun thing to work. Then we make it happen. When "what would have to be true" involves a contribution from another color, that frequently forms the backbone for a primary or secondary strategy.


It's worth noting that one of the reasons we have toned down the density of creature cards in a booster pack is so it becomes more viable to look for these strategies, as opposed to cramming your deck full of generic 2/2s for 2C and hoping for the best. One of the most frequent comments we hear about *Innistrad* is that such a high percentage of the cards are playable under the correct circumstances. We're happy that worked out—but one of the ways we made it work involves something a lot of players don't like in their gut. We weakened the context-independent power-level of your average card, so you're forced to look for synergies to recoup that power discrepancy. It's asking our players to make a little bit of a cognitive leap, but **Magic**'s audience is very smart and we felt the risks were worth the rewards. Every time I win games by enchanting [Rotting Fensnake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rotting+Fensnake) with [Skeletal Grimace](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Grimace), or blowing out combat with a [Moonmist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonmist), I'm happy we moved in this direction.




|  |  |
| --- | --- |
| 
Rotting Fensnake
 | 
Skeletal Grimace
 |

Once we figure out what each color wants (or should want) to do, we have to ensure that what it wants to do is actually *viable*. We might think it's the sweetest thing in the world to turn all Penguin Advisors blue until end of turn, but if it doesn't at least offer the potential of winning, very few players will want to pursue it.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld182_fire.jpg)A sure sign of a failing strategy is a strategy that lacks a *curve*. Most players are probably familiar with the idea of a mana curve—a weighted distribution of spells at different converted mana costs that helps to make sure you cast a one-drop on the first turn, a two-drop on the second turn, etc. So a sure sign of a failing set is one that doesn't curve its creature base. Put simply, if one color can guarantee a consistent stream of threats and another color can't, the second color is going to have a tough time winning the game. By distributing creatures across the curve and smoothing it out, we can avoid this problem.


That's only the first step, though. It's not simply each *color* that must take its mana curve into account—it's each *strategy*. If every card that pushes me into (say) the White-Black Human Sacrifice deck costs six mana, I'm simply not going to opt into that strategy very frequently. It's just less fundamentally sound than the other hypothetical options. So we have to diversify the seeds of each strategy such that they fall into place along these lines.


Mana-curve distributions aren't the only types of distributions that are important, though. Frequently, when we divvy up a color's primary and secondary strategies, one tends to be fast while the other tends to drift toward the slower end of the spectrum. What this means is that each point on the mana curve needs to be served by a variety of both aggressive and controlling cards. You can't just put four two-mana 2-power creatures with different keyword abilities into white at common and call it a day. Some of them need evasion. Some need ratios weighted toward aggression, while some need to give the control deck the time it needs to survive. Additionally, the nuances of a given rarity's power-to-toughness ratios add depth and robustness to a format without adding too many complexity points. We get to add game-play value without adding words. For a long time, it seemed nearly impossible in **Magic** to get a 2/3 creature for three mana. This made it difficult to trade raw resources—most two-drops traded with most three-drops—which in turn decreases the number of constructive interactions per game. That's bad game play. Therefore, we try to diversify the power/toughness curve of our creatures as much as possible, while meeting the demands of a given set's keywords and themed mechanics.


All this talk of curves, of course, only addresses (a) permanents and (b) those permanents' *converted* mana costs. The reality is much more nuanced. While it's true that because the primary value of a mana curve is to ensure a deck's board presence develops at a maximally efficient rate—and, therefore, that spells don't generally fall onto the graph unless they're intended to be reliably cast as soon you hit the appropriate land drop—it's also important that (for example) a color's combat tricks don't all cost the same amount of mana. "Shields up" and "shields down" moments are hugely important for any kind of card game, so when those values are all constant across a color, you render the game state more binary than it needs to be.


Similarly, it's also important to remember your distribution of CC spells (spells whose mana cost is ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif), say, instead of ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)) needs to be chosen deliberately. If a color contains too many, you're going to find that (a) players tend to declare that color later in draft; (b) a given table of eight players tends to possess fewer players drafting that color; and (c) of the decks which *do* choose to play that color, they're more heavily weighted toward it. To a lesser extent, the lower on the mana curve overall your CC cards tend to appear, the more difficult it is to make two-color aggressive decks featuring that color. Conversely, if you over-do the number of single-C spells—particularly single-C removal spells—that color will weaken overall, due to (a) an increasing number of its powerful cards being splashable, which removes them from the pools of players playing color-dedicated decks and (b) the temptation to first-pick cards that are easier to cast, which draws more players into that color early on and dilutes the pool. This means many sets tend to feature CC "reward" creatures at lower mana costs, a CC removal spell to reward dedicated drafters of that color, and a premier C removal spell that serves as a first-pick incentive and a splash option.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld182_fdb.jpg)To summarize: When we're designing a Limited environment, it's important that every color combination has at least one dedicated strategy it can pursue—it's not just trying to announce spells and hope those spells do something. Once those strategies are determined, it's important to render them actionable by seeding and empowering the cards and interactions that make them feasible. Then, the cards that compose those decks must be curved in such a way that it's actually possible to play them together in a functioning deck.


That's just the tip of the iceberg, of course. I haven't even mentioned rares and mythic rares, which play a more prominent role than it might seem at first glance. And I could write volumes about *how* the playtesting process helps us make the strategies we select actually function correctly. But like I said, this is just about the nuts and bolts, and how those parts come together to create something beautiful.


Join me next week when I talk about how we made sure most undying creatures would live, until they died, at which point they'd come back to life.








