
---
[Link to Wayback Machine](https://web.archive.org/web/20220927074259/https://magic.wizards.com/en/articles/archive/duels-planeswalkers-design-2014-07-09)

[_metadata_:author]:- "Nik Davidson"
[_metadata_:description]:- "A behind-the-scenes look at the new features in Magic 2015—Duels of the Planeswalkers."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "231196"
[_metadata_:publish_date]:- "2014-07-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duels of the Planeswalkers Design"
[_metadata_:wayback_capture_timestamp]:- "2022-09-27 07:42:59"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220927074259id_/https://magic.wizards.com/en/articles/archive/duels-planeswalkers-design-2014-07-09"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/duels-planeswalkers-design-2014-07-09"
---


Duels of the Planeswalkers Design
=================================



 Posted in [NEWS](/en/articles)
 on July 9, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_NikDavidson.jpg)
By Nik Davidson




 Nik Davidson makes games, writes stories, solves problems, and plays Magic. He's almost certainly doing one of those things right now. 






Last year, Wizards of the Coast put out a call to a bunch of Seattle-area game developers to see if they'd like to come down to Renton to [play some *Magic* with us](http://archive.wizards.com/Magic/magazine/article.aspx?x=mtg/daily/arcana/1163). More than 100 people showed up from eleven different developers.



![](https://media.magic.wizards.com/news20140701_dotp15.jpg)

While some people were surprised by the high turnout, I wasn't among them. I've been a game developer for over thirteen years, and I've never worked at or visited a game studio that didn't have a *Magic* league, some lunchtime players, the occasional after-work draft, or an FNM contingent. The depth and strategic opportunities of *Magic* makes it exactly the sort of game that appeals to people who make games for a living.


We divided into groups of eight, and of the seven other players in my pod, four of them told me that they had played *Magic* years ago, and started playing again much more recently via *Duels of the Planeswalkers*. A fifth had only started playing recently, and told me she had learned to play via *Duels of the Planeswalkers*. As the new lead designer for *Duels of the Planeswalkers*, it was music to my ears.


Improving on a New Classic


I came to Wizards of the Coast about a year and a half ago, just as we were finishing up testing on *Magic 2014*—*Duels of the Planeswalkers* and as *Magic 2015—Duels of the Planeswalkers* was just getting underway. It's a great thing to be able to come in fresh to an existing successful franchise. A lot of the nuts and bolts of the system are already decided and polished, and rather than answer the blue-sky question of "What should we do?" you get to ask the much more productive question of "What can we do **better**?"



**![](https://media.wizards.com/images/magic/daily/features/2014/news20140709_en_gameplay.jpg)**

For me, the answer was pretty clear. **Duels of the Planeswalkers** did a great job of teaching people to play **Magic*,* but I wanted to set my sights a little bit higher. My goal was to make a **Duels of the Planeswalkers** that could *make *Magic* players*—to give players all the tools they would need to play **Magic** in any capacity they chose after (or while) playing **Duels of the Planeswalkers*.* The game has always been a good teaching tool and a fun way to build your skills, but there was a big missing component. Naturally, I'm talking about deck building.


Can I Build a Deck?


I've taught lots of people to play *Magic*, and I pretty much always start the same way. I go over the absolute minimum information about parts of a card and creature combat, and then I hand them a deck that I've already built, and we get to it. Depending on how innately competitive my student is, we may or may not play open-handed. We'll play a game or two, talk about cards, sets, and theory, and then some of them will ask a question that is the best indicator of whether or not that person will be playing *Magic* a year later:


"Can I build a deck?"


Deck building is at the heart of *Magic*. It's not just that there are countless possibilities for deck concepts and compositions, it's that when I build a deck, it's *mine*. And in that moment, *Magic* goes from being "a fun game" to being "*my* game." Capturing that feeling for *Magic 2015—Duels of the Planeswalkers* was my number one goal in design.



![](https://media.wizards.com/images/magic/daily/features/2014/news20140709_en_deckbuilder.jpg)

From there, the next challenge was tackling the core-gameplay loop. Any time you have highly open-ended systems in your games, it's valuable to put intelligent constraints on other aspects of play. For *Magic 2015—Duels of the Planeswalkers*, this meant making the most out of the existing campaign systems that we had available to us from previous iterations. We knew we wanted to award cards and boosters for winning games, but we also knew that part of the fun of the game is creating special challenge scenarios that are as much a puzzle as they are a game of *Magic*.


These are great, but, like puzzles, once you've solved them, they lose a lot of their replay appeal. That's why we've introduced Exploration battles. You can explore on any of the five planes in *Magic 2015—Duels of the Planeswalkers*, and you'll get a random battle chosen from several options for that plane. All of these are designed to be challenging and replayable, and winning these battles will earn you booster packs of cards from that plane.


Once you get going, you've got almost a "*Magic* RPG" feel to the gameplay—build a deck, win a battle, get a booster, improve your deck, and challenge a tougher foe.


You Autocomplete Me


Deck building can be intimidating. From the beginning, we knew it wasn't enough to just take the training wheels off and throw people into a deck-building interface, we needed to provide as much or as little guidance as the player needed. Our starting point was the deck-building interface that allowed players to build sealed decks in *Magic 2014*—*Duels of the Planeswalkers*. From there, we enhanced the filtering options to account for the much larger collections that players would have access to, and developed a deck-building AI that would take into account things like mana curve, creature count, and even cross-card synergies. From there, a player has a lot of options.


The easiest way to go about constructing a deck is just to ask the AI to take a stab at building a deck according to a two-color archetype. Each of the color pairs in *Magic 2015—Duels of the Planeswalkers* has a strong mechanical identity—not to say that's the only way to build it, but, for example, the green-blue deck has a concentration of creatures and spells that can exploit enters-the-battlefield effects with ways to return your own creatures to your hand. The deck builder will try to build as thematic a deck as possible toward that archetype, and then you're ready to go. You can edit that deck freely, but the AI will give you a strong starting point.


If you're willing to go one step more freeform, you can just start adding cards and then ask the deck builder for suggestions of cards that will complement the cards you've already chosen. And if you get stuck, or you're not sure which direction to go, there's a handy Autocomplete button that will finish your deck based on the cards you've already added. You can do this with as little as a single card already placed into your deck—if all you know is that you've got a Dragon and you want a deck with your Dragon in it, the AI will accommodate.



![](https://media.wizards.com/images/magic/daily/features/2014/news20140709_en_cardzoom.jpg) >

I've been pretty impressed with the quality of the decks we can build on the players' behalf. A top-notch deck builder will definitely have a serious advantage over an AI-constructed deck, but I've found that the autobuilt decks are more than capable of challenging the *Magic 2015—Duels of the Planeswalkers* campaign.


Hunting Big Game


And speaking of the campaign, this year, we set a new bar for integration with the *Magic* storyline. You'll play as a Planeswalker, initially enlisted by Avacyn, to seek out and aid Garruk, who is faring pretty poorly under the curse of the Chain Veil. Your travels will take you across five planes—Innistrad, Theros, Ravnica, Shandalar and Zendikar—but as you close in on Garruk, the Multiverse's greatest hunter may pick up your trail as well! Some of the events in *Magic 2015—Duels of the Planeswalkers* are already impacting cards in *Magic*—you may have noticed that Ob Nixilis has a new look, for example—and the implications of your actions are potentially far-reaching.



![](https://media.wizards.com/images/magic/daily/features/2014/news20140709_en_campaign.jpg)

Before I Go


While we at Wizards of the Coast are responsible for the content and art direction of *Magic 2015—Duels of the Planeswalkers*, the project would be absolutely impossible without our partners at [Stainless Games](http://www.stainlessgames.com/), located on the scenic [Isle of Wight](http://en.wikipedia.org/wiki/Isle_of_Wight). The team there is comprised of some of the most-talented, hardest-working, and *Magic*-loving developers I've ever had the privilege of working with, and while I get to write the somewhat self-congratulatory website article, those fine men and women deserve a lion's share of the credit. My thanks and admiration to them on another *Duels of the Planeswalkers* well done!


And with that, I'll leave you to the game itself. *Magic 2015—Duels of the Planeswalkers* is available on iPad July 9 and other platforms—including Xbox One, Xbox 360, PC via Steam, Android tablet via Google Play, and Amazon Kindle—starting July 16, and it's free to play the first campaign and start your collection. Whether it's the start of your path as a *Magic* player, or just a way to sneak in a quick duel between rounds at your next PTQ, I hope you enjoy it.







