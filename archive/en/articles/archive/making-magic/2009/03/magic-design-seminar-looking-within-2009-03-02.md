
---
[Link to Wayback Machine](https://web.archive.org/web/20170624225030/http://magic.wizards.com/en/articles/archive/making-magic/magic-design-seminar-looking-within-2009-03-02)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Last November, I explained that I had begun teaching Magic design seminars to all interested parties in R&D. I wrote a column (Magic Design Seminar: The 10 Mental Locks) about one of the seminars and asked if you wanted me to write about any more. The feedback I received boiled down to: `Yes. This is a design column. We really like when you talk about Magic design.`"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "656946"
[_metadata_:publish_date]:- "2009-03-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Design Seminar: Looking Within"
[_metadata_:wayback_capture_timestamp]:- "2017-06-24 22:50:30"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170624225030id_/http://magic.wizards.com/en/articles/archive/making-magic/magic-design-seminar-looking-within-2009-03-02"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/magic-design-seminar-looking-within-2009-03-02"
---


Magic Design Seminar: Looking Within
====================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on March 2, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Last November, I explained that I had begun teaching **Magic** design seminars to all interested parties in R&D. I wrote a column ([**Magic** Design Seminar: The 10 Mental Locks](/en/articles/archive/design-seminar-10-mental-locks-2008-11-10)) about one of the seminars and asked if you wanted me to write about any more. The feedback I received boiled down to: "Yes. This is a design column. We really like when you talk about **Magic** design."


So without further ado, I present another in my **Magic** Design Seminar series. Today's column, interestingly enough, is the very first seminar I held. Many of my other seminars are built upon this one so in retrospect I'm not sure why I didn't start with it in my column as well. 


### Building Blocks


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_relearn.jpg)If you want to become a doctor, one of the first things they teach you is about the body. Not how to fix the body, that comes later, but just how the body works. Likewise, if you want to become a mechanic, you have to learn how a car works. If you want to become a writer of fiction, you have to understand how a story works. The key to learning anything always starts with understand the essence of what you are working with. **Magic** design is no difference. You want to learn about **Magic** design, you have to start by learning about **Magic: the Gathering** specifically and more generally the trading card game genre.


I'm not talking about the cards. Yes, you eventually do have to learn about the history of the game and part of that is learning what's been done before. But for today, I'm going even more basic. Today I'm going to examine what makes **Magic** itself tick. How did Richard Garfield create it? What were the challenges? What were his solutions? Today is about going to the essence of the game and gleaning an understanding of how it works. 


### In the Beginning


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_cross1.jpg)  
Let's start with this question. Where did **Magic** come from? What was the idea that spawned it? One answer is that Richard was trying to meet the criteria set out by Peter Adkison. Peter was looking for a quick, portable, flavorful game that could be played between roleplaying sessions. (Before the year is out, I promise you will get a full-blown article about this origin story of **Magic**.) Richard's response was that he already had an idea for a game that he felt could fit the criteria. Thus, it is my belief that it was an earlier idea that spawned **Magic**. 


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_goblinMime.jpg)Talking to and reading pretty much everything Richard has written about the origin of the game, I think the kernel that first intrigued Richard was the concept of a "game bigger than the box" (this is an expression I've heard Richard use numerous times). The idea was that the game was something larger than what any one person had. Normally, when you sit down to play a game, everything you need is included. When you play that game elsewhere, even with other people's copies, the game experience is almost identical. True, many popular games come with expansions, but if you and your friend have the same expansions, you had the same basic game experience.


There are a few exceptions, though. The two biggest: roleplaying and miniatures. In each case, the game comes with so many possible components that players in practicality do not all play the exact same game. In the case of roleplaying, an extra wrinkle is added in that the game encourages the players to make up much of their own material thus insuring a uniqueness to each play experience. Miniatures, on the other hand, encourage the players to focus on some subcategory. Players are building an army (most often). Each piece they buy makes other pieces more or less attractive to acquire based on how it interacts with the army they already have. 


The other big exception, in my mind, is games that use a high variance within the game to make each iteration separate from the last. The example I'll use for this category is Cosmic Encounter, both because it is one of the best executions of my point and because it is one of the games with the most influence on **Magic**'s design. Cosmic Encounter is a conquest game where the goal is to take control of a certain number of planets, but it's not really about that. Layered over the conquest game is a system that allows players to break certain rules. Players play the role of alien races that each come with their own ability to break some rule of the game. Traditionally, each player has their own unique alien and thus are allowed to do things differently than every other player. Games of Cosmic Encounter seldom play the same because the interaction of the different aliens is very distinct and with enough aliens to choose from, repetition is kept to a minimum.


Richard recognized that there was space in between each of these games for something new. The idea that I believe Richard latched onto was the concept of a metagame—that is, the idea each player of the game added a their contribution which combined together to make a game in which no one player was in control of what happened. The idea was that there was a game above the game. 


In addition, I think Richard took the pieces of each game that he liked. A trading card game would allow the customization of roleplaying, the synergy of miniatures, and the rule breaking of games like Cosmic Encounter. Trading cards were a perfect medium for several reasons. First, cards lend themselves well to games. Second, cards have space for art which would give the game a look and feel. Third, the model of trading cards makes a good system for randomizing who gets what card. And fourth, trading cards have a sound economic model. 


### "Houston, We Have a Problem"


So Richard comes up with the concept of a trading card game. Each booster will have randomized cards. These cards can be used to construct a deck to play the game. I'm also pretty certain that Richard started with the idea that the flavor of the game was wizards dueling with magic. While the initial idea is exceedingly cool in concept it comes with a barrel of design problems. Let's walk through the major ones:


**#1) The Degeneracy Problem**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_oonaQueen.jpg)Most games have stronger and weaker cards. Boardwalk is better than Baltic Avenue. The queen is stronger than a pawn. An ace has a higher value than a three. But in each of these cases, the game forces you to play with a certain mix of cards. A trading card game doesn't do that. What keeps a player from building his deck full of "queens"?


**#2) The Control Problem**


Every game being the same has a few advantages. For starters, the designer knows what the player is going to see. This allows him or her to balance things accordingly. If a certain element is unfun in large numbers , the designer can simply choose to put less of it in the game. How does the designer of a trading card game put the things he needs into the players hands while holding back the things that aren't supposed to be there in great number?


**#3) The Communication Problem**


Not only can't the designer control what the players get to use, they can't even control what the players see. The designers cannot rely on any one card doing anything because there is no insurance that a particular player will ever see the card in question. How can the designer communicate when he or she can't even control what the player will see?


Much of what you know of **Magic** (or any trading card game) today came from Richard finding solutions to these problems. 


**#1) The Degeneracy Solution**


To solve the degeneracy problem, Richard realized that he needed a way to make as many cards matter as possible. Power level wasn't a viable answer because there was no way to make the volume of cards needed for a trading card game and not have some stronger than others (in other words, trading card games inherently have to have a subset of more powerful cards). First, Richard realized that he needed to find a way to make different cards matter at different times. If the game had some progression during which the value of the cards could change then the game would encourage playing with a larger variety of cards. Second, the game needed some system by which every card couldn't go in every deck. If certain decks excluded certain cards then the game would force the metagame to build different decks rather than find the one optimal build. Third, there had to be a way to make some cards easier to get than others. This way, the more degenerate cards could be kept at a lower number in people's collections.


The first solution led to the creation of **Magic**'s **mana system**. Why not just put the largest, most powerful spells in your deck? Because they are not good for you until later in the game. If your deck is full of them, you will lose to the player who has the leaner, quicker deck. If your deck has none of them, then you will find yourself outclassed later in the game when the opponent's giant monsters start hitting the table.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_manaSymbols.jpg)  
The second solution led to the **color wheel**. Why can't you use all the good spells? Because your deck isn't able to play all of them. Note, by the way, that the color wheel doesn't just add mechanical separation but flavor as well. For some players, the fact that a certain card represents something flavorfully is itself the reason why it rather than another card might go into a certain deck.


The second solution also lead to the concept of **archetypes and synergy**. Certain cards might get played in some decks and not others because they worked better in conjunction with certain cards or certain categories of cards. The other concepts I'm talking about are built into the essence of the game. This one depends a lot more on execution. As such, archetypes and synergy require constant vigilance in design and development.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_4Mox.jpg)  
The third solution led to **rarity**. Maybe "led to" is incorrect, because the concept of a trading card game already had rarity built into it as it was layered on top of an existing trading card model. Nonetheless, the third solution turned to rarity as an answer. Interestingly, too much so. When you ask Richard about cards like the "Power Nine" ([Black Lotus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus), the five Moxes, [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall), [Time Walk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk), and [Timetwister](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Timetwister)), he admits that they knew the power of the cards. They falsely believed at the time that the game would exist at a level much lower than it ended up. Richard assumed people's collections would stop in the range of what players would spend on an average hobby game. Sure, someone might have one Mox but one Mox unto itself is not terribly degenerate.


**#2 The Control Solution**


Some of the above items also help with this problem, rarity being the biggest one. How can you force certain cards into people's hands while restricting others? Simple—just print more of the former and less of the latter. A cycle of five commons, for example, really does help communicate a set's theme. One mythic rare does not. The key to solving this problem rests a lot on statistics. Make sure that you give the player the best chances of seeing what you need him to see, by lowering the rarity and spreading it out over multiple cards. 


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_funMeter.jpg)The other important key to solving this problem is power. If you make the more fun parts of the game stronger and the less fun parts weaker, you have much better chance of encouraging the play you want. As an example, R&D quickly found that land destruction was very unfun if it could be used to keep the opponent from ever being able to do anything. This has led to R&D making the choice to print the majority of land destruction at a lower power level to keep those kinds of decks generally out of the tournament environment.


In many ways, this area of the game is more under development's watch than design as it relies heavily on volume and power, things that development monitors. 


**#3 The Communication Solution**


As with the last solution, the key to this solution rests a lot with learning how to maximize the volume of your messaging. Another big part of this solution is learning that a trading card game communicates in different ways from traditional games. This is why themes and cycles and keywords and names and card concepts and world building, for instance, play such a crucial role in design and development. Most importantly, a designer has to understand that he or she simply does not have the control that one does in traditional games. Each trading card player will have a unique discovery of the set. As I said above, there are tools (which also includes non-game things such as tip cards and **magcithegathering.com**) to help minimize the variance of the discovery but there is no way to completely erase it. As a TCG designer, I have come to embrace this as one of the things that set TCGs apart. Still, this problem is always on the mind of every designer in every set.


### On the Plus Side


While trading card games come with some inherent trouble areas, they also come with some special bonuses. Let's walk through what they are and how Richard played into their strengths with **Magic**.


**Customizability**


I'm often asked to describe **Magic** to people who have never played it. The most successful technique I found involves comparing it a more famous game: **Monopoly**.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_stitchTogether.jpg)
> 
> Each and every time you sit down to play **Monopoly**, there are forty squares on the board. Those forty squares are the same each and every game. Imagine a game where that wasn't true. Imagine if each time you sat down at the **Monopoly** board the squares were different. Sure, many games would have Boardwalk but not all of them. In some games, it might not even be the most expensive square. The game might have four railroads one game, then eight the next, and then maybe none. There could be colors that require four or five properties to get a monopoly. Each time you played, you didn't know what you were going to get until the game began. That's **Magic**. Every game is unique.
> 
> 
> 

My example only goes part of the way (I've learned the key to explaining something as complex as **Magic** is to not and try to explain it all). Not only does **Magic** keep changing, you the player have a huge impact on what that change is. If you like a certain style of game, you have the control to make it (at least your half) just that. This "make it what you want it to be" aspect of trading card games is very compelling.


Richard played into this in two opposite ways. First, he made most cards generally open-ended, allowing numerous combinations. Second, he added themes that drew cards together. (In Making Magic terminology, he made sure to have modular and linear cards.) The color wheel helps this immensely, as it steers you down certain paths that are inherently flavorful.


**Ego Investment**


There is another huge benefit of making players create their own game: players become more emotionally invested. This isn't just a random game piece you are playing with—it's your deck. *Your* deck. The thing you built and tuned and labored over was successful. The connection is much stronger than the average game and thus creates a stronger emotional response.


I think Richard's choice of the dueling wizards theme did a great job of playing into this strength. As players build their deck, they are compiling their spell arsenal. I feel this metaphor does a lot to make the game approachable and enjoyable and helps players build the emotional attachment.


**Community**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_mactaRioters.jpg)The existence of a metagame forces more interaction between the players. Such interaction leads to stronger community ties. In short, you are more likely to make friends playing **Magic** than other games because the nature of a trading card game forces you to mingle with other players, be it for trading, deck discussion, or playing. The existence of the metagame also gives the community constant material to talk about. What did you think of the newest set or Card A or Deck B? 


The very essence of a trading card game plays so well into this attribute that there wasn't much extra Richard needed to add. Ironically, the one thing he could have done, publish info about the game including deck lists, was purposely avoided during the game's first few years. (See [my column from two weeks ago](/en/articles/archive/25-random-things-about-magic-2009-02-16) for more on this.)


**Portability**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_annex.jpg)Trading card games tend to be light on pieces. Usually all you need is a deck (and some means to keep score – yes, I use my iPhone) and you're good to go. That is not true of the vast majority of games. This was definitely in Richard's mind when he chose the deck size. (And remember, the game started with an even smaller deck size, 40 cards; once again see my column from two weeks ago for more).


**Responsiveness**


In most games if I have a continued bad experience, I learn to walk away from the game. Trading card games have a much greater ability to respond to environment. Thus, if something is unfun for me, I can choose to modify my deck to defeat that unfun thing and drive it away. (When you can't, that is when development has made a misstep—and even then, the nature of new releases and formats guarantees that all logjams eventually break.) Richard's response to this bonus was to make sure that Alpha had a lot of cards that served as answers to other cards. In particular, the set is filled with color hosers.


### What It All Means


Let's wrap this all back to the topic at hand. What does this mean for card design? It means that all designers have to be aware of the strengths and weaknesses built into the game as every designer has to take advantage f and/or compensate for them. Let's walk through the major concerns. For each one, I'll point out a time in **Magic** where I believe we made a design mistake.


**Rarity**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_cross2.jpg)  
This is one of the most important tools a trading card designer has at their disposal. It is essential that you use your commons to help establish what the set is and make sure that the key things you want explored exist there. As I often tell designers, "if a set's theme isn't in common, it isn't the set's theme." Sets aren't what the designer wants them to be about, they are what the players perceive them to be about. In addition, make sure the things that define the play of the set exist at enough volume in common.


**Mistake of the Past –** *Chamions of Kamigawa* block had a legendary theme. All the rare creatures for the entire block were legendary creatures. The problem was that, you can't possibly pick up on that through a few packs. Even if two of your rares are both legendary creatures, that simply isn't enough to convey that all the rare creatures are legendary. My point here is that one of the set's major focuses was put in a place where the players couldn't see it. 


**Color Wheel**


Sets need definition, both to provide choices for what decks to build and to allow each player to find elements that they will most enjoy. The mana system makes it such that colors have a natural separation in the game. Designers need to take advantage of that. Colors are a natural divide to work in different elements of a set. Designers need to make use of this valuable tool.


**Mistake of the Past –** I believe the lack of strong color wheel influence is one of the major reasons that the Standard environment during *Mirrodin* got so messed up. The "affinity" deck (I put affinity in quotes because there was so much going on over and above the affinity mechanic itself) had the ability to play every good card in the environment because there wasn't a firm color wheel to force the cards into different decks.


**The Mana System**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm28_shardCon.jpg)**Magic** needs different things to be relevant at different parts of the game. This holds true for each set. When creating a design, you have to make sure that the different pieces you are building span the length of a game. In addition, you have to always be aware of what is necessary in your mana to support your themes.


**Mistake of the Past –** *Invasion*, while a fun environment, proved frustrating to many of the tournament players because the pull of the set (play as many colors as you can) forced them to rely on shaky mana bases that were inconsistent.


**Archetypes and Synergy**


Sets have to be about something, several somethings in fact. Some cards have to have value situationally allowing more cards to have relevance in play. When crafting a set, designers have to think about what archetypes they are supporting and what natural synergies are built into the design.


**Mistake of the Past –** One of the biggest problems with *Homelands*, in my opinion, was that the cards did not lead you to anything. There was some creative linkage but mechanically the set didn't work as nicely with itself as a **Magic** set should.


### Wrapping Up


As you can see, to understand the basics of **Magic** design, you have to understand the basics of the trading card game genre. Much of the responsibility of a designer is to make sure that the set you're working on fulfills the basic needs of the game. Yes, the decisions about how to design a particular card are important, but they are minor in the scope of what needs to be done to make each set work within the context of the game. Today's column should give you a little more insight into what that context is..


I hope you enjoyed this second seminar. Assuming I get positive feedback, you'll see more seminar columns in the future.


Join me next week when I seek out experiences.


Until then, may you take a moment to think about how the things you take for granted came to be.







