
---
[Link to Wayback Machine](https://web.archive.org/web/20220706015526/https://magic.wizards.com/en/articles/archive/duels-planeswalkers-magic-engine-2014-02-13)

[_metadata_:author]:- "Patrick Buckland"
[_metadata_:description]:- "Hi! I'm Patrick Buckland. I'm the CEO and owner of Stainless Games, the developer of Duels of the Planewalkers. We're a games developer from the UK with over 40 staff, but I like to keep hands-on, so I was Lead Programmer and Project Director on Duels. Duels will be available for download via Xbox LIVE Arcade on the Duels of the Planeswalkers page starting sometime Wednesday"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "154546"
[_metadata_:path_date]:- "2014-02-13"
[_metadata_:publish_date]:- "2009-06-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duels of the Planeswalkers: The Magic Engine"
[_metadata_:wayback_capture_timestamp]:- "2022-07-06 01:55:26"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220706015526id_/https://magic.wizards.com/en/articles/archive/duels-planeswalkers-magic-engine-2014-02-13"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/duels-planeswalkers-magic-engine-2014-02-13"
---


Duels of the Planeswalkers: The Magic Engine
============================================



 Posted in [NEWS](/en/articles)
 on June 17, 2009 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Patrick Buckland











![](https://media.wizards.com/legacy/mtg/images/daily/features/feature43c_dotplogo.jpg)Hi! I'm Patrick Buckland. I'm the CEO and owner of  [Stainless Games](http://www.stainlessgames.com/home/go/), the developer of **Duels of the Planewalkers**. We're a games developer from the UK with over 40 staff, but I like to keep hands-on, so I was Lead Programmer and Project Director on **Duels**. **Duels** will be available for download via Xbox LIVE Arcade on the [Duels of the Planeswalkers](http://archive.wizards.com/magic/digital/duelsoftheplaneswalkers.aspx) page starting sometime Wednesday morning.


I've been playing **Magic** for nearly ten years and have 30,000 cards, all catalogued and filed like the obsessive person I am. So when the opportunity to develop a **Magic**-based Xbox 360 Live Arcade game came up, I bit both of Wizards' arms off up to the elbows.


Because I already knew the game of **Magic** very well, I personally took on the task of writing the **Duels** engine. Then I decided that it made sense if the person who wrote this also wrote the AI. Oh dear. When exactly did that seem like a good move? Hang on a minute, it's my company—shouldn't I be giving the brain-melting jobs to some über-brained underling by now? Well ... to be honest, I just couldn't resist the challenge!


That was back in the summer of '07. It's been a long and difficult journey since then, but the final product has come in *above* spec and—shock, horror!—is astoundingly good fun to play. So having a synapse-soup where my brain used to be is worth it in the end.


 


### Challenges and Solutions


 


We needed to simplify the game in a few keys ways without losing its essence. We had to keep in the back of minds that this was an "arcade" game, albeit one with a more cerebral flavour than most.


Thus above all, it needed to be easy to pick up and play—not a straightforward goal with a game as complex as **Magic**. However we all felt that it still needed to be proper **Magic**. Initial discussions regarding "**Magic** lite" were soon dismissed.


 


### Approach


 


So we decided on a basic mantra that we kept falling back to during development: "How do average "casual" players play **Magic**?" We're talking about people who aren't pros, but certainly aren't stupid—just normal guys and girls who have maybe skimmed the Comprehensive Rules and/or dived into them to answer particular questions, but who wouldn't know that "last known information" or continuous effects layers even existed.


 


### Priority, the Stack, and the Mana Pool


 


The first challenge was priority and the stack. When our hypothetical casual players sit and play **Magic**, do they verbally pass priority? Do they put a counterspell on the stack whilst a creature spell is on there? No, they don't. Fred throws his Platinum Angel onto the table, all smug and smiling, but then Bobs shouts, "Hang on just one moment, sunshine! Not so fast!" and casts his Cancel.


![](https://media.wizards.com/legacy/mtg/images/daily/features/feature43c_cancel.jpg)
 


Likewise in combat. Even if players are aware of how priority is passed during combat, they don't formally do so. They just throw in instants and activate abilities *in real time* as they see fit. It all flows nicely and it works. Very rarely does resolution order matter, and when it does—assuming somebody in the group knows about the stack—you retroactively backtrack and work it all out properly.


And as for the mana pool, what mana pool? Many casual players don't know exactly what it is. They tap some lands to play a card—it's as simple as that.


So we set out to try to mimic this playing experience. We wanted a game that flowed in a way that allowed our players to have fun without the rules of the game getting in their way. That's the way that paper **Magic** works, but it's a lot more difficult on a console or a computer—especially because it needs to work properly in the rare cases where it matters.


We came up with the idea of *shared priority*. It's first-come, first-served. If you can get in there quicker than your opponent, then great—you get to play the spell or ability.


And the stack is in there, but we disguise it as the spell or ability taking time to "operate." What's actually happening is that the object is correctly on the stack, so all the correct **Magic** rules apply, but we don't make a song and dance about it. It feels like a video game.


![](https://web.archive.org/web/20150922134500im_/http://archive.wizards.com/mtg/images/daily/features/feature43c_screenShot1.jpg)
 


The ditching of the mana pool is the biggest divergence of Duels of the Planeswalkers from "proper" **Magic**. But it's worth it, as the game plays much faster, and it's very rare that it ever matters. The only drawback was that it prevented us from using nonbasic lands and other unusual sources of mana—a shame, but a price worth paying for a slick core experience.


To resolve issues with two and three colour decks when paying for colourless costs, the game has to work out what land to tap for you. To do this, it looks at your hand and your activated abilities and tries to leave as many things still playable as possible for you—but it can't always get it right. If tapping a Forest would still let you play card A, but tapping a Plains would let you play card B, which does it do? It can't read your mind, but in most situations it will tap your lands as well as you would.


 


### Other Divergences


 


There were a few other short-cuts; things like the order of triggered abilities and replacement effects. We decided that trying to ask the player which order would just get in the way, so we always use timestamp order.


And in Two-Headed Giant, your attacking creatures always deal damage to the player opposite you, whereas in paper **Magic** you get to choose. Once in a blue moon this makes a difference (say, one head has a Pariah in play but not the other), but it's a small price to pay for avoiding being asked who you're damaging *every* single time one of your creatures connects in 2HG!


A rare example of where we actually broke the rules (at the request of Wizards of the Coast, I hasten to add!): In multiplayer games of paper **Magic**, you always get a free mulligan at the start if you wish. Only then do mulligans start diminishing your hand. But in single player games, you don't get a free mulligan. We all felt that this was confusing, so in **Duels** you *always* get a free mulligan, regardless of number of players.




|  |  |  |
| --- | --- | --- |
| 
Pacifism
 | 
Holy Day
 |  |

We also found in testing that certain cards really frustrated players when the AI hit them with them. In particular, Elspeth's habit of playing Pacifism and Holy Day really wound them up, as did armies of fliers that they couldn't protect themselves from. So we implemented a system whereby certain cards are flagged such that some or all of them are removed (well, actually they're shuffled to the bottom of the AI's deck) when a novice plays the game. The difficulty level then ramps up as the player gets more experienced, and these cards start to get introduced. The player can also bias this difficulty in the Options menu, so that either the game remains on easy (with many of these cards tucked away), or starts on hard.


Finally, the most significant way in which we kept the game slick and relatively simple (for **Magic**) was in card choice. We avoided cards with rules and mechanics on them which we felt were not conducive to an arcade game experience.


 


### Technical Approach


 


So, that's a random selection of design challenges. Now onto what's under the hood.


 


### The Magic Engine


 


First of all, we had to implement a solid **Magic** engine. This would need to be data-driven so that we could release content packs in the future. We also envisaged a long and expansive future for this product, so despite deciding to avoid a great many mechanics for this release (e.g. phasing, hybrid mana, type-changing, removing from the game, copying etc), we structured the underlying engine in such a way that none of these features are precluded from its core structure. In fact some of them (such as the phased-out and removed-from-game zones) are implemented but not used.


 


### Card Scripting


 


We then had to settle upon a means of actually scripting the cards. The actual **Magic** engine is written entirely in C++. We decided to use Lua scripts embedded in XML data files in a proprietary syntax developed for this project. We then wrote a Lua - C++ interface that allows the Lua scripts to manipulate C++ objects such as cards.



![Angel of Mercy](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Angel%20of%20Mercy&options=)

 


Let's take Angel of Mercy as an example. Here's the card's script—even if you're not a programmer, you might be surprised by how much of the code is understandable.


![](https://media.wizards.com/legacy/mtg/images/daily/features/feature43c_card1.jpg)


This card uses some Lua functions (Flying, SelfTriggered and YouGainLife) that are defined elsewhere. For a more programmer-friendly version of the card's code, the full code of the relevant Lua functions, and some additional technical information, click [here](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/43c&page=2).


The above simple card hopefully gives you a flavour of how **Duels** works. Of course many cards are much more complicated than this. In fact the cards themselves actually have their own register arrays so that each card is able to act like its own little self-contained microprocessor if needs be. Some cards were horrendously complicated and constitute entire programs in their own right, thanks to **Magic**'s law that "Any rule can be overridden by card text."


Fortunately, Wizards never asked us to implement Shahrazad ....


**Instance-Based and Client-Server Internal Structure**


The **Magic** engine is entirely self-contained and instance-based (that is, you can have more than one of them at once—I'll explain why this is needed when we get onto the AI system on Monday).


It was important that the engine be self-contained for a number of reasons. We wanted to ring-fence the development of the engine as opposed to the rest of the project for a number of reasons. These included future reuse, but also included the difficulty of developing the engine itself in parallel to the user interface. Mainly, though, it came back to the problem of any card overriding the rules. The user-interface (UI) side of the game cannot possibly know what cards are doing what—only the engine can know this—otherwise many cards would be impossible to implement. Therefore, the engine and the UI code were developed as an entirely abstracted client-server system. The UI is a dumb client of the **Magic** engine.


![](https://media.wizards.com/legacy/mtg/images/daily/features/feature43c_screenshot2.jpg)
 


How it works is that the engine provides the UI with a means to do such things as iterate through the players, teams, zones, cards in each zone, abilities on each card, the types of a card, etc., etc. The UI then treats this information with total ignorance.


For instance, the UI finds that a certain card is in the graveyard. It is essential that the UI sub-system does not care why the card is there, or how it got there. It is entirely a dumb client. All it does is say, "Oh, it's in the graveyard, is it? Hang on, it was in play 0.25 seconds ago, therefore I'd better draw it at point X along a line from its old in-play position to the graveyard." An oversimplification, but that's the gist of it.


Additionally, the UI passes a very small set of messages back to the engine. These are things like "Play a card" or "Activate an ability" or "You can move to the next step now."


Let's take some simple examples.


![](https://media.wizards.com/legacy/mtg/images/daily/features/feature43c_banana.jpg)


First, the untap step. The UI knows nothing about this at all. It merely observes that some cards are untapped, but because they were tapped a short time ago, rather than just drawing them untapped this frame, it draws them in an intermediate angle according to how long ago it last saw them in a tapped state. So the cards visually untap.


Let's presume nothing happens in the upkeep. Then it's draw time, but again the UI knows nothing of this. However, the **Magic** engine causes a card draw (having first fired the appropriate triggers and checked that nothing overrode the draw—the engine allows pretty much anything to be overridden by Lua scripts, so that in this instance a card could say, "If a player would draw a card, he or she instead turns into a banana and explodes" or whatever).


A card draw is merely a card changing its zone from library to hand. That's all the engine does. The UI then iterates the hand next frame, comes across the new card, and again performs the animation *implicitly*. There is never a "This player has just drawn a card" message from the engine to the UI layer. It is entirely an observational relationship.


The result is a robust and future-proof system.


 


### Conclusion


 


So, that's the **Duels of the Planeswalkers** engine in a nutshell. On Monday, I'll be back with an in-depth look at how the game's artificial intelligence makes decisions based on this engine. It's no stretch to say that it's the most advanced **Magic** AI ever created, and even advanced **Magic** players will find themselves challenged.


![](https://web.archive.org/web/20150922134521im_/http://archive.wizards.com/mtg/images/daily/features/feature43c_duelsCta.jpg)
 


To try the game for yourself, go to the [Duels of the Planeswalkers](http://archive.wizards.com/magic/digital/duelsoftheplaneswalkers.aspx) page, where it will be available for download to your Xbox via Xbox LIVE Arcade starting sometime Wednesday morning.







