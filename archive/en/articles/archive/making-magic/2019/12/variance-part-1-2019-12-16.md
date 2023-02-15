
---
[Link to Wayback Machine](https://web.archive.org/web/20200113063800/https://magic.wizards.com/en/articles/archive/making-magic/variance-part-1-2019-12-16)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark talks about the importance of variance in game design and how best to understand it."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1492559"
[_metadata_:publish_date]:- "2019-12-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Variance, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2020-01-13 06:38:00"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200113063800id_/https://magic.wizards.com/en/articles/archive/making-magic/variance-part-1-2019-12-16"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/variance-part-1-2019-12-16"
---


Variance, Part 1
================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on December 16, 2019 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Today (and after *Theros Beyond Death* previews), I'm going to talk about an important element of game design, one I haven't delved into too deeply in the past, something known as variance. I'll explain what variance is, how it impacts game design, and why understanding it is so important to designing *Magic* (or any game, really).


Let me begin by defining it. I should note that I'm defining the term in the context of game design. Variance is "how differently a gameplay element plays out from one play experience to the next." We can think of variance as a scale. If that element has a high variance, it has the potential to play differently each time it's played. If that element has a low variance, it will play similarly each time it's played.


There's a second vector to this issue (so you can think of this scale as being perpendicular to variance—more on this below), so let me bring that up as well. That vector is choice. In games, you can have high choice or low choice. High choice means you, the player, are making decisions about that game element. Your input affects how it functions. Low choice means that you are not making decisions about the gameplay element. You don't have any input into what it's doing.


Many different things can be defined as a "gameplay element," so let me walk through a number of examples using *Magic*. For each, I will explain if it's high choice, low choice, or mixed choice (meaning the element can run the gamut from low to high).



![Demonic Tutor](https://media.wizards.com/2019/images/daily/lB9kkdVwIy.jpg)[Demonic Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor) | Art by: [Zack Stella](https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+%5B%22Zack%20Stella%22%5D)
Variance in Cards
=================


We start by looking at a specific card. Each time I play the card, how different is the effect from other times I played it? There are a number of factors that play into this:


**Targeting** – How many different options do I have when I cast the card for who or what it will affect? The more options, the higher the variance. For example, let's take a direct-damage spell. If it says "deal 3 damage to a player," there's not a lot of options in a two-player game. Yes, technically, you can choose yourself rather than your opponent, but with the exception of very narrow use cases, you're going to choose your opponent, so this has rather low variance. In contrast, "deal 3 damage to a creature" most likely will have more options as there's a significant chance of your opponent having two or more creatures (and, again, you could also target your own creatures in certain circumstances). Therefore, this has a higher variance. A spell that says "deal 3 damage to any target" has the potential for even more options, as you can choose players, creatures, or planeswalkers, and, thus, has the highest variance for a direct-damage spell. Note that this category is considered high choice as you, the caster of the card, almost always get to be the one who chooses the targets.


**Modes** – How many options of effects do you have when you cast this spell. A simple modal spell like [Naturalize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) lets you destroy either an artifact or enchantment. This has some variance, but on the lower end. Charms, which give you three options, have more variance, and commands, which give you four options (of which you get to pick two) have even more. Usually, the higher the number of modes, the greater the variance. An important point here concerns the usefulness of each mode. If a card gives you three choices but you're almost always going to choose the same one, that card has less variance overall. Note that R&D generally tries to make the choice on modal cards matter. This category is considered high choice because, as with targeting, the caster of the spell (usually) gets to choose the modes.


**Selecting a specific card** – Does the card's effect require you to choose a specific card? This can be done in a few ways. Probably the most popular is [tutoring](http://magic.wizards.com/en/articles/archive/play-design/m-files-hour-devastation-part-1-2017-07-14#tutor) or wishing, where you go and get the card of your choice, often within a certain subset (from your library or outside of the game, respectively) and put it into your hand. Sometimes you're putting the chosen card into another zone. Another thing you can do when selecting a card is impact it in gameplay somehow. For example, perhaps you name a card and now it can't be cast or activated. This category is high choice in that you have a lot of options available. Interestingly, it can often be low variance because you're highly encouraged to always name the same card game to game. (More on this next week.)


**Interacting with an unknown zone** – This category is mostly about interacting with a library or another player's hand. "Draw a card," for example, has variance because each time you use the effect, you're interacting with your shuffled library. Similarly, if I had an effect that interacts with my opponent's hand with, say, a discard spell, it's going to play differently because it matters what cards they have in their hand at the moment of me casting the spell. That's going to change game to game because my opponent's hand will usually be different. This category is low choice, because you aren't making any decisions that affect why the card plays out differently.


**Random effects** – This category refers to cards that play out differently because it makes use of a randomizing element. Black-border cards will flip coins, silver-border cards will roll dice. The library can also be used as a randomizing element. These types of spells are very upfront about their variance. This category is low choice as you seldom have any input in what happens (although, things like the library can occasionally be impacted by effects like scry).


**Effects based on other card(s)** – This category deals with effects that require other cards (usually on the battlefield, but potentially in any zone) to dictate what the card does. It might be a scaling effect that counts some subset of things. It might be an effect that uses a creature's power and/or toughness to dictate the size of the effect. It could be a threshold (I mean that in the generic R&D sense) spell that gets better if a certain condition is met. The key to these effects is they have variance because they have to interact with other cards to dictate what they do. This category is a mixed choice as it can vary quite a bit how much input you have on what the effect is.


**Additional costs** – Some cards require you to pay a cost other than mana. Maybe you have to discard a card or sacrifice a creature or return a permanent to your hand. Like the last category, this group of effects requires you to interact with another card or cards, thus shifting how it plays out from game to game. This category can also overlap with the last as sometimes the extra cost impacts the effect. This category is a mixed choice for the same reason as the last.


As you can see, there are many ways to affect how much variance any particular card can have.



![Angel of Invention](https://media.wizards.com/2019/images/daily/aCBdWCDI8f.jpg)[Angel of Invention](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel+of+Invention) | Art by: [Volkan Baga](https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+%5B%22Volkan%20Baga%22%5D)
Variance in Mechanics
=====================


Next, we pull back and look at a specific mechanic. How often when playing cards with this mechanic does it play similarly? With mechanics, whether something is high or low choice depends more on deck building than gameplay. I'll discuss each as I talk about it. As with the cards, there are a number of factors that play into the variance of mechanics:


**Variables** – Does the mechanic have a variable built into it? That is, is there something that changes between cards with the mechanic? There's a number of ways it can:


* **Cost:** Many mechanics require some cost, usually mana, to use. Some mechanics, like cycling, can have that cost vary from card to card. It could cost 1 or 2 or a specific colored mana. Others, like food counters, can have that cost locked in (2, T and sacrifice), so it's always the same.
* **Input:** Some mechanics vary what it is they're looking for. For example, proliferate always has the same output (adding up to one counter to various permanents and players) but can have various inputs (sometimes through a cost and sometimes through a trigger).
* **Output:** In contrast, some mechanics, like landfall, have the same input (a land entering the battlefield under your control) but different outputs.
* **Input and output:** Some mechanics, like devotion, can vary both in their inputs (devotion can have different thresholds to trigger) and outputs (devotion cards have all sorts of effects).
* **Range of effect:** Some mechanics vary in how powerful the effect is that they generate. For instance, Annihilator comes with a number that determines how many permanents the opponent has to sacrifice when the creature attacks.

The more variables built into a mechanic, the higher its variance. As far as choice, you can technically choose to include only cards of a certain mechanic that play similarly to one another, but that's not something gameplay will usually encourage, so I consider this low choice.


**Scalability** – Does the effect of the mechanic vary based on in-game conditions? For example, convoke is stronger the more creatures you have on the battlefield. The variance of this category depends on two factors: 1) how many of the things you're caring about can the game reasonably generate (caring about creatures is higher variance than caring about enchantments), and 2) does the mechanic naturally cap itself? Cost-reduction mechanics, like affinity, for instance, can only lower its portion of the spell to 0. Normally, you have a lot of control about how big your effects will be based on deck building, so I would call this high choice.


**Choices/Modes** – Does the mechanic come with an inherent choice? For instance, fabricate allowed you to choose between getting 1/1 Servo creature tokens and +1/+1 counters. The more choices, usually the higher the variance. This is a high-choice factor and one that happens when casting the spell.


**Opt-in use** – Does the mechanic give you a choice to use it? A good example would be kicker. Any spell with kicker has an additional cost you could choose to pay to upgrade the spell, but you're not required to use the mechanic. You can cast the spell normally without the kicker. The variance on this type of mechanic has to do with how easy it is to opt-in. This is also high choice, as whether to use it is (usually) left up to the player.


**Alternate use** – Does the mechanic allow you to use it after casting the spell normally? Flashback is a good example of this type of mechanic. You can cast the cards normally and then later in the game decide whether you want to flash them back. Like the last category, this type of mechanic's variance scales on how easy it is to use. Also, like the last category, this is a high-choice option.


All of this basically boils down to the consistency of all the cards with the mechanic. The more flexibility in how you use it or what effect it has, the higher the variance.


Variance in Deck Archetype
==========================


Now we pull back again, this time focusing on a whole deck. How much change is there when you play the same deck from game to game? This whole section tends to be high choice, but baked more into deck building than gameplay. Deck archetype variance tends to revolve around a bunch of different things:


**Consistency of mana** – Is your deck adjusted to maximize your ability to get mana? If yes, your variance will drop.


**Mana curve** – Does this deck have a consistent thing to do each turn of the game? The tighter the mana curve, the less variance the deck will have. Also, the lower the converted mana cost average of the cards in the deck, the less variance the deck will usually have. (This is due to the fact that there's less variance on what turn you'll get your early land drops.)


**Mana efficiency** – Does your deck allow you to have something to do each turn with your mana? This isn't just about mana curve but having what R&D refers to as mana sinks, things that allow you spend mana when you need to. A good example of a mana sink is a permanent's activated ability requiring mana.


**Number of copies of cards** – Are you playing with four copies of your cards? If yes, you're lowering the variance. If no, you're raising the variance. The more copies you have of any one particular card, the more consistent your deck will play out. This taps into why we don't do restricted cards in any format other than Vintage. (More on this next week.)


**Repetition of effects** – Do you have multiple cards that have the same function? The more you do, the lower the variance of your deck (aka the more your deck does a singular thing, the more likely your games are to play out the same).


You'll notice an ongoing theme in this section. The things that tend to make your deck more competitive are also the things that lower your variance. The reason for this is low variance leads to consistency, which increases your ability to win. More on this in just a moment.


Why Variance Matters
====================


*Magic* has a lot of opportunities to both increase and lower variance through both high and low choice. Okay, why exactly should a game designer care about that? Let me start by focusing on each of the two scales, talking about the advantages of each side of the scale.


We'll start with the variance scale.


Advantages to Low Variance
--------------------------


**Consistency** – If variance is low, games play out more similarly. The cards, mechanics, and decks tend to do the same thing each time you use them.


**Games hinge on smaller details** – Because low-variance games are more consistent, the players tend to have a better understanding of what to expect. This results in the game hinging more on smaller decisions.


**Rewards experience** – As the game is more likely to hinge on smaller decisions, the advantage goes to the player that has the most practice in that match-up. Knowing where to eke out advantage is key in low-variance games.


**Simplicity** – As the cards, mechanics, and decks work more consistently from game to game, it makes them easier to understand. Note that there is still complexity in these games, but it shifts from comprehension complexity (knowing what cards do) to board complexity and strategic complexity (understanding how the pieces interconnect).


**Skill matters more** – Because low-variance games are more controllable, they tend to end less often with one player having bad luck.


Advantages of High Variance
---------------------------


**Novelty** – High variance means games are much more likely to play out differently. How cards get used, how mechanics get used, and how decks get used all have a much wider realm of possibility. This makes the games more novel as each one is just doing stuff that other games weren't doing.


**Games hinge on larger details** – Because high-variance games play out so differently, the players have less experience knowing how to handle any one moment of gameplay. This tends to lead to bigger moments mattering. The winner is more likely to be the person that figured out the flow of where the game was going, relying more on intuition than knowledge.


**Rewards flexibility** – Having the games vary greatly rewards players who are good at adapting on the fly. If every game is different, winning is more about quickly sizing up and capitalizing on new situations than it is about knowing what to do because you've experienced it before.


**Rewards game comprehension** – When cards, mechanics, and decks work differently from game to game, it makes them more complex and harder to learn. This tends to reward players with a better grasp of the game


**Easier for less-experienced players to win** – High variance increases the chance of one player having larger swings of luck, be it good or bad. This increases the chance that a worse player can defeat a more experienced opponent.


**More exciting moments happen** – Good or bad luck swings tend to create larger moments in gameplay.


Now let's examine the choice scale.


Advantages of Low Choice
------------------------


**Ease of play** – The less decisions there are when playing a card, the easier it is to play.


**Simpler board states** – If each individual card can do less, the overall board state is also easier to follow.


**Players can think further ahead** – Choices lead to many potential future board states, making it harder to predict what will happen on future turns. Lower choice means players can better anticipate what will happen on future turns and thus plan ahead. This tends to be a key ability to winning in low-choice games.


**Faster gameplay** – Choices require thinking, and thinking slows down gameplay.


Advantages of High Choice
-------------------------


**Rewards skill** – There is a high corollary between the number of choices in a game and skillful players doing better.


**More surprise** – The increase of choices makes predicting what is going to happen harder and thus increases things happening that one or more of the players does not anticipate.


**Greater chance of advantage changing sides** – High-choice games tend to have more dynamic board states that increase the opportunity for larger swings in gameplay.


**Games are more fun to watch** – The increase in surprise and advantage changing sides tends to make for more enjoyable games to watch.


Now, let's take these two spectrums and position them together in a single grid.


![Variance/Choice Grid](https://media.wizards.com/2019/images/daily/vOKvTZzZBE.png)


This leads to four quadrants: High Choice, Low Variance; High Choice, High Variance; Low Choice, Low Variance; and Low Choice, High Variance.


Let's examine each quadrant.


**High Choice, Low Variance**


This is the quadrant that experienced competitive players enjoy the most. It gives them the greatest ability to impact the game while lessening things outside their control that can lead to random losses.


**High Choice, High Variance**


This is the quadrant that experienced casual players enjoy the most. It makes for the most exciting games to play in and watch. Things tend to change a lot from game to game, allowing players the ability to feel like they've had an impact.


**Low Choice, Low Variance**


This is the quadrant that newer but competitive players enjoy the most. It's the easiest for them to understand but also rewards them for playing well.


**Low Choice, High Variance**


This is the quadrant that beginners like most. It's the least complicated to understand but allows them the best chance of winning from time to time.


"With All That Said . . ."
==========================


Now that I've explained what variance is and how it shows up in the game, it's time to start talking about the relevance of variance to game design. Unfortunately, I've used up my 3,000-plus words doing the former, meaning I'm going to have to push off the latter to next week.


As always, I'm eager. When I dig down deep into a meaty design topic, I always want to hear what you all think of what I've written. If you have any thoughts on today's column or the subject of variance, please [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Instagram](http://instagram.com/mtgmaro)).


Join me next time for part two after *Theros Beyond Death* previews.


Until then, may *Magic* provide the variance level you enjoy most.




 

##### 
 #697: Planeswalker Evolutions






##### 
 #697: Planeswalker Evolutions




In this podcast, I talk about the many different ways we've evolved the planeswalker card type since its introduction.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork697_planeswalkerevolutions_dU29Iue3.mp3)



  


 

##### 
 #698: Reusing Things






##### 
 #698: Reusing Things




Part of *Magic* design is reusing things you've used before. This podcast talks all about when and how we reuse things in design.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork698_reusingthings_ghD93Ydu.mp3)




* [**Episode 696**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork696_whentochange_jsy63U8W.mp3) When to Change
* [**Episode 695**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork695_coreofplanes_kmY2IldO.mp3) Core of Planes
* [**Episode 694**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork694_triviatop50words_jDhe92y7.mp3) Trivia – Top 50 Words






