
---
[Link to Wayback Machine](https://web.archive.org/web/20160709084731/http://magic.wizards.com/en/articles/archive/latest-developments/we-all-pay-our-debts-end-2006-09-01)

[_metadata_:author]:- "Mike Turian"
[_metadata_:description]:- "Hi. I'm Mike Turian. Your usual developer Aaron Forsythe has the week off, so Scott brought me in to entertain you with some harrowing “End of Turn” stories.&#13; &#13; Let me introduce myself. I've been playing Magic since The Dark. I started playing the summer before my sophomore year of high school in 1994. I haven't been playing Magic for half of my life, but it is pretty close."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "290001"
[_metadata_:publish_date]:- "2006-09-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "We All Pay Our Debts in the End"
[_metadata_:wayback_capture_timestamp]:- "2016-07-09 08:47:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160709084731id_/http://magic.wizards.com/en/articles/archive/latest-developments/we-all-pay-our-debts-end-2006-09-01"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/we-all-pay-our-debts-end-2006-09-01"
---


We All Pay Our Debts in the End
===============================



 Posted in **Latest Developments**
 on September 1, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_MikeTurian.jpg)
By Mike Turian




Before joining Magic Online as its digital product manager, Mike worked as a producer for Wizards's technology department, a product manager for organized play, and as an R&D lead developer. He has played Magic Online since it came out in 2002 and Magic since The Dark. 






Hi. I'm Mike Turian. Your usual developer Aaron Forsythe has the week off, so Scott brought me in to entertain you with some harrowing “End of Turn” stories.


Let me introduce myself. I've been playing *Magic* since *The Dark*. I started playing the summer before my sophomore year of high school in 1994. I haven't been playing *Magic* for half of my life, but it is pretty close.


I joined Wizards of the Coast two years ago as an intern, and about six months later I became a full-fledged developer. During that time I have been on the development team for *Guildpact*, *Coldsnap*, and led the development team for *Future Sight*. On top of that I have been a playtester and built theme decks (and run the Future Future League) for every set since *Ravnica: City of Guilds*. I take care of collation, market research projects, and fought hard for more slugs, squirrels, Merfolk, cows and dinosaurs in *Magic*.


### Debtors' Knell


In *Magic* when we want something to happen at a regular interval, we usually use one of two phrases, “At end of turn” or “At beginning of upkeep”. Normally the decision to use one or the other is simple. For example, [Lightning Serpent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Serpent) clearly should die at the end of your turn instead of at the beginning of your upkeep. What fun would it be if you cast that guy as a blocker? *Magic* is full of cards that want their effects to last until the end of the turn, with [Astral Slide](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide), [Ignorant Bliss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ignorant+Bliss), and [Berserk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserk) providing fine examples.


[Debtors' Knell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Debtors%27+Knell) currently triggers at the beginning of your upkeep. It wasn't always that way; [Debtors' Knell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Debtors%27+Knell) went through a number of changes during its development life. Design handed off:



> 
> **Unliving Death**  
> 
> 7 (W/B) (W/B)  
> 
> Sorcery  
> 
> Return each creature card in your graveyard to play under your control.
> 
> 
> 


From a development perspective this card had two problems. First, it was too much of an “I win.” card. *Magic* has room for some small amount of the type of card where you cast it and win. Occasionally we will pull out a card like [Dregs of Sorrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dregs+of+Sorrow) or [Plague Wind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Wind) where, when you cast it, you win some huge percentage of the time. In general though, these cards are few and far between. The set already had [Storm Herd](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Storm+Herd), and having more than one “I win” card in a small set wasn't seen as desirable.


The second strike against the card was that we were worried about [Sins of the Past](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sins+of+the+Past). Aaron Forsythe noted how strong of a combo this could be with [Grozoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grozoth). [Zombify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) effects have proven time and again to be deceptively powerful and worse than that, restrictive. Effectively the best fatty in a format is restricted by the best reanimation spell. When players are running around reanimating too cheaply it handicaps what Timmy cards are possible. At the time we received Unliving Death, [Sins of the Past](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sins+of+the+Past) cost five mana and was a more powerful spell than it has proven to be at six mana.


For both of these reasons Henry Stern, lead developer of *Guildpact*, changed Unliving Death into…



> 
> **Back to Business**  
> 
> 5 (W/B) (W/B) (W/B)  
> 
> Enchantment  
> 
> At the beginning of your upkeep, return a creature card in any graveyard to play under your control.
> 
> 
> 


Back to Business solved both the concern about reanimation and the concern about being too much of an “I win” card. Perfect! Or not.


Back to Business had a new problem. It was a pretty terrible card. You cast it for eight mana and get nothing that turn. The following turn, you get to reanimate a creature (if there is one in a graveyard) and then that creature has summoning sickness. Blech. This is an eight mana spell, it had to be able to do something better than that.



> 
> **Debtors' Knell**  
> 
> 5 (W/B) (W/B) (W/B)  
> 
> Enchantment  
> 
> At the end of your turn, put target creature card in a graveyard into play under your control.
> 
> 
> 




![Debtors' Knell](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Debtors%27%20Knell&options=)

Our first solution to these problems was to make it so you reanimated the creature at the end of each of your turns. The summoning sickness problem goes away, but a new problem arose. Now it wasn't a very interactive card - if your opponent was tapped out you were guaranteed to bring back a creature on the first turn.



Next thing you knew, it was showing up in decks all over the place. Even if people were playing with enchantment removal, they would still lose to the reanimated creature. And if you didn't have an answer... well the game wouldn't last more than a few turns.


The development team liked the new power level of the card, but not how little interaction it offered. Magic often has a system of checks and balances. [Rumbling Slum](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rumbling+Slum) is a powerful creature, but there are powerful spells like [Putrefy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy) to answer the Slum. By reanimating so quickly, [Debtors' Knell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Debtors%27+Knell) sidestepped most of the good answers to it.


Our final version came late in development. We reduced the casting cost by one so that it had almost the identical excitement and power level of the “At the end of your turn” version, but went back to “At the beginning of your upkeep, put target creature card in a graveyard into play under your control.”


### The Most Powerful Wizard


When *Magic* came out, it didn't have the same clean rules that the *Sixth Edition* rules update provided. Apparently, having the text, “Until end of turn, creatures get +2/+2” had a different effect than “Creatures get +2/+2 until end of turn.” Of course “At end of turn,” still existed as well. It was a crazy world to be sure.


I play a lot of games besides *Magic*. On Tuesday nights for the past couple of years, I have been lucky enough to go over to Richard Garfield's house to play various board and card games. I figured that since this was my first article on *magicthegathering.com*, I should go to the source and see if he had any “At end of turn,” tidbits to share with you.


Richard related a story about some games he played versus a player at Whitman College. He remembered how his play group was still excited to be playing with real cards, instead of the playtest cards that they were so used to using to make *Magic*.




![Berserk](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Berserk&options=)

Over the course of a number of games Richard realized that he needed to save his [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog)s for when his opponent played his [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)s and [Berserk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserk)s. He would win the games where he was able to hold the [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog)s, but wouldn't be able to compete with the instant speed growths if he wasted his [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog)s.



His opponent played a [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) on the second turn. The next turn, he attacked for two. Not being able to muster any defense of his own, Richard took the two damage from the [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) turn after turn. When Richard would say he was taking the Bears, he noticed how his opponent would pause and think before finally agreeing to deal just 2 damage.


Finally Richard got down to 2 life and the Bears were attacking him again. He decided it was best to just take the damage since he couldn't see any other way out of this situation. If he [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog)ged now he would just lose later anyhow.


Richard: “Ok, I'm dead.”  

Opponent: “Oh, you're dead! Wait!”  

Opponent: “[Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)! [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)! [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)! [Berserk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserk)! [Berserk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserk)! Haha! Take 44!”  

Richard: “Oh, in that case I'll [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog).”


Needless to say, at the end of the turn the [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) died from the [Berserk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserk) and Richard went on to win that game. His opponent discovered who the most powerful wizard really was.


### But what if your turn never ended?


Paul Sottosanti makes all of the Vanguard Avatars for *Magic Online*. The *Magic Online* avatars are designed knowing that they won't ever be needed to work in real life. The crazy fun ability of Momir Vig to generate a token creature of an appropriate casting cost couldn't be done with paper *Magic*. With Momir Vig, Paul did a great job of exploring what abilities work online that wouldn't work with paper cards.


Another tidbit Paul let slip was how *Magic Online* doesn't have any memory issues. Normally, we don't make cards that have huge amounts of memory issues. As with everything, there are rare exceptions to this rule, but for most cards we try to make it significant enough that players will naturally remember, such as the protection color from [Voice of All](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voice+of+All), or we won't do the card.


For *Magic Online*, avatars like Akroma can give out random protection abilities that last all game, without the memory issues kicking in. Who could possibly remember which of your creatures got haste, protection from red, protection from black, vigilance, first strike, vigilance, or trample?


In paper *Magic* a spell effect will almost always last “Until end of turn”, otherwise we would turn that spell into an enchantment. *Magic Online's* superior memory makes it so that you can make all sorts of cool avatars. From talking with Paul, I bet we haven't seen the last of the multi-turn avatar.


### From V to VI –


![Corpse Dance](https://media.wizards.com/legacy/magic/images/cardart/te/corpse_dance.jpg)As I was talking about earlier, the rules of *Magic* have changed a lot since the early days. The End Phase of *Sixth Edition* was once called the Discard step from Fifth Edition. Among the changes that happened with the changeover was the ability to cast spells during the End Phase. According to the original *Magic* rules, cards like [Waylay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waylay) and [Corpse Dance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corpse+Dance) effects would wear off when the turn ended.


*Sixth Edition* rules opened a loophole with this class of cards. From the *Sixth Edition* rules:



> 
> 313. End of Turn Step
> 
> 
> 313.1. As the end of turn step begins, all abilities that trigger “at end of turn” go on the stack. (See rule 410, “Handling Triggered Abilities.”) Then the active player gets priority and players may play spells and abilities.
> 
> 
> 313.2. If “at end of turn”-triggered abilities are created or if cards with “at end of turn”-triggered abilities come into play after preexisting ones have already gone on the stack at the beginning of the end of turn step, those abilities won't go on the stack until the next turn's end phase. In other words, the step doesn't “back up” so new “at end of turn”-triggered abilities can go on the stack. This only applies to triggered abilities that say “at end of turn.” It doesn't apply to continuous effects whose durations say “until end of turn” or “this turn.” (See rule 314, “Cleanup Step.”)
> 
> 
> 


The combination of these two rules meant that cards like [Waylay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waylay) and [Corpse Dance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corpse+Dance) could all of a sudden be used to get creatures at the end of your opponent's turn. Under the original rules, this wasn't possible. One of the ongoing debates in R&D is what to do with this type of card.


For [Waylay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waylay), we issued errata that stated “Play Waylay only during combat.“ This fixed the issue at the time and kept the intent - we always strive to give the cards the best chance to be true to their original printing. If you haven't done so already, check out [Aaron's recent article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af127) about the changes to the *Urza Saga* cards like [Great Whale](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Great+Whale) and [Priest of Gix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priest+of+Gix). That class of cards has gone back to its original wording and shows how we are revisiting some of these issues currently.


### At End of Turn


Today in development we were talking about people's favorite red burn spell. There is no better way to find out than to ask. If you have one that isn't listed, go ahead and let me know about it in the forums.


Until next time,


Mike Turian







