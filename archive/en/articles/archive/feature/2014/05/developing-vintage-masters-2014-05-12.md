
---
[Link to Wayback Machine](https://web.archive.org/web/20220119142601/https://magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220119142601id_/https://magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12"
[_metadata_:wayback_capture_timestamp]:- "2022-01-19 14:26:01+00:00"
[_metadata_:description]:- "Hi all! I'm Ian Duke and I work as a developer in Magic R&D. I've been with Wizards for about two years, and Vintage Masters was my first opportunity to lead the development of a set release. I'm super excited to dive in and tell you all about the process of building this awesome draft format, but since this is a preview article, I'll have to restrain myself a bit! Being a"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2014-05-12"
---


Developing Vintage Masters
==========================



 Posted in **Feature**
 on May 12, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_ianduke.jpg)
By Ian Duke




Ian Duke is a developer in Magic R&D and has been with Wizards of the Coast since 2012. A gift of an Ice Age starter deck in 1995 sparked Ian's lifelong passion for Magic. He also enjoys math, physics, board games, and puzzles. To the surprise of few, his favorite guild is Azorius. 






Hi all! I'm Ian Duke and I work as a developer in **Magic** R&D. I've been with Wizards for about two years, and *Vintage Masters* was my first opportunity to lead the development of a set release. I'm super excited to dive in and tell you all about the process of building this awesome draft format, but since this is a preview article, I'll have to restrain myself a bit!


Being a developer is all about solving problems and overcoming challenges. Today, I'll share with you the story of one of the challenges our team faced in developing *Vintage Masters*, and how we not only met and exceeded that challenge, but also introduced a new draft archetype in the process. But first—just what is *Vintage Masters*?


### That Vintage Feeling


![](https://web.archive.org/web/20090602072246id_/https://www.wizards.com/mtg/images/daily/features/21_power_nine_fan.jpg)

*Vintage Masters* was conceived as a way of introducing the [Power Nine](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/arcana/432) cards to **Magic Online**. It was to be a special, **Magic Online**–only release that would also rerelease many cards that are important to Constructed Vintage play. The goal was to eventually sync up the online Classic format with the traditional Vintage format. We want both Vintage aficionados and new competitors alike to be able to experience the awesomeness of Vintage through the convenience of **Magic Online**.


When *Modern Masters* debuted we were overwhelmed with positive feedback about how much players enjoyed the Limited play. It was then that we realized we could do a similar thing with *Vintage Masters*. We set out to create a fully draftable, high-powered Limited environment that captures the fun and nostalgia of playing with the strongest and most iconic cards from **Magic**'s early history.


However, we knew we didn't want to simply replicate the *Modern Masters* experience—we wanted to make *Vintage Masters* stand out on its own. Aaron Forsythe, director of **Magic** R&D, came up with the idea of building *Vintage Masters* from only the set of cards that aren't currently Modern legal. This would emphasize the feeling of the Vintage experience and play up the nostalgia of the early days of **Magic**. As any Legacy or Vintage player can tell you, there's no shortage of awesome, iconic cards to draw from in the pre-*Eighth Edition* period.


We ended up with an awesome set.


Whether you've been playing **Magic** since 1993 or have only ever heard of [Black Lotus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus) spoken of in hushed whispers in the back room of your local card shop, I encourage you to check out *Vintage Masters* when it launches June 13. While we certainly pulled no punches in making the set as fun as possible for experienced players, you don't need to have been playing **Magic** for decades in order to jump in and enjoy the set. Many of the archetypes are visible at the surface level, but we also infused the draft environment with enough depth to keep things fresh for ten, fifteen, twenty drafts and beyond.


### Restrictions Breed Creativity


Limiting our focus to the pool of cards that aren't Modern legal was both the biggest challenge and the most fun aspect of working on *Vintage Masters*. This restriction asked the design and development teams to be much more creative in how we built the set, and I firmly believe the draft environment ended up a much more fun, distinct, and nostalgic experience as a result.


![](https://media.wizards.com/images/magic/daily/features/feat217a_inspiration.jpg)
[Inspiration](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspiration) | Art by [Izzy](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Izzy%22%5D)


It turns out that **Magic** has evolved in many ways over the years. For example, the color pie has changed in several subtle and not-so-subtle ways. Black used to be the color of fast mana rituals before that was shifted into red. White used to be better at destroying both artifacts and enchantments than green was. In addition, the relative balance between creatures and spells was much different. Big creatures didn't really exist at common, and in general instants and sorceries were much stronger, relative to creatures.


When design handed off the file to development, many of these imbalances from the early days of **Magic** were showing through. The powerful, iconic spells we knew we wanted to include in the set were outshining many of the interesting synergies design had built in. Certain color combinations were working very well, but others were lagging behind. Of course, that's nothing unusual for a **Magic** set at that stage of the process, so the development team set to work tweaking and tuning and bringing things into balance.


### Homeless Pups


For the most part, our iteration was working well. We largely focused on making strategies stronger, since we wanted to maintain the high power level and splashy plays that make eternal formats so enjoyable. However, we found that we were hitting a ceiling in some areas. Certain color combinations and strategies weren't coming up to par with the rest of the set. In particular, the color red was turning out to be a challenge.




|  |  |
| --- | --- |
| 
4825
 | 
207
 |


*Examples of cards that were cut.*

What we found in testing was that players were snapping up the premium red burn spells and splashing them, but no one was building decks with red as the main color. The problem? The creatures were too weak. We began a massive exploration, poring over every possible red creature from **Magic**'s early days, and even considering dramatic rarity shifts in order to get red's creature curve in line. We were able to make a few changes that helped somewhat, but ultimately the team wasn't satisfied. After all, some of the most efficient creatures red had access to in those days were [Ironclaw Orcs](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironclaw+Orcs) and [Jackal Pup](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jackal+Pup). Not exactly impressive!


Even though we were a ways into the development process at this point, we still kept the design team very much looped in on our progress. When we discussed the difficulty we were having with red, designer Ethan Fleischer came up with a brilliant idea.



![Goblin Warchief](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Goblin%20Warchief&options=)


Goblins!


### Red Goes Green


While red's creatures from this time period were weak on their own, Ethan suggested that we could lean on tribal synergies to bring up the collective power level. I was skeptical. I thought that the Goblins wouldn't play well with the rest of the set and what the other colors were trying to do. I also wasn't sure we'd even be able to get the power level of the Goblins up to par. Design had tried some other tribal strategies earlier in the process and they didn't work well, which left me hesitant to try again.


Luckily, development-team member Adam Prosak stood up for his green-skinned buddies. At the next team meeting, Adam brought a list of all the Goblins we had access to, including his recommendations for which would be the most fun and powerful to play with. Once the team saw his plan laid out, we agreed to give it a try in the next draft playtest.


It worked wonders. What we found was that because the Goblins were individually weaker than many of the cards in the set, they tended to float around the draft table longer. Eventually, someone would figure out that red was open and start collecting a Goblin tribal package. Instead of seeing a bunch of [Ironclaw Orcs](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironclaw+Orcs) and [Jackal Pup](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jackal+Pup)s lap the table indefinitely, we saw the player who was "supposed" to be base red assemble a powerful tribal deck.


![](https://media.wizards.com/images/magic/daily/features/2014/feat_1k19_299_gk.jpg)
[Goblin King](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King) | Art by [Ron Spears](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Ron+Spears%22%5D)


The result? A 3–0 victory for the [Goblin King](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King) of the playtest. We saw the similar things happen in future playtests. While Goblins wasn't always the dominant deck of the draft, it took its place as one of many viable strategies, and one of many things red can do in the set.


### Drafting Constructed


While our job of developing the set was far from done, we had successfully overcome one of the major challenges we'd run in to. We continued polishing the set from there, and I can say I'm very happy with where we ended up. The result is a Cube-like draft experience that captures more of a Constructed feel than traditional Limited formats often do. Beyond the basic two-color combinations, there are plenty of sideways strategies and unique build-around cards at higher rarities. This creates a huge variety of experiences and keeps the format fresh for many, many drafts.


![](https://media.wizards.com/images/magic/daily/features/2014/feat_1k19_299_dc.jpg)
[Delif's Cube](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Delif%27s+Cube) | Art by [Mark Tedin](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Mark+Tedin%22%5D)


I hope you enjoyed this journey through one of the challenges we faced in building *Vintage Masters*. For a more in-depth look at what it's like to work on such a unique and exciting set, join me for my next article in early June, where I'll take us through a development retrospective. Until then, enjoy preview week!







