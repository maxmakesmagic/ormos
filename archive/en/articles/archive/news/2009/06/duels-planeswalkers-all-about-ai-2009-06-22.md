
---
[Link to Wayback Machine](https://web.archive.org/web/20211128221255/https://magic.wizards.com/en/articles/archive/news/duels-planeswalkers-all-about-ai-2009-06-22)

[_metadata_:author]:- "Patrick Buckland"
[_metadata_:description]:- "Hi! Patrick Buckland here, CEO and owner of Stainless Games, the developer of Duels of the Planeswalkers. Last Wednesday, I wrote about the engine that drives Duels. In that article, I explained that the Magic engine is self-contained (separate from the user interface or any other code) and instance-based (you can have more than one of them at once).This separation has many"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "683771"
[_metadata_:publish_date]:- "2009-06-22"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duels of the Planeswalkers: All about AI"
[_metadata_:wayback_capture_timestamp]:- "2021-11-28 22:12:55"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211128221255id_/https://magic.wizards.com/en/articles/archive/news/duels-planeswalkers-all-about-ai-2009-06-22"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/news/duels-planeswalkers-all-about-ai-2009-06-22"
---


Duels of the Planeswalkers: All about AI
========================================



 Posted in **News**
 on June 22, 2009 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Patrick Buckland











Hi! Patrick Buckland here, CEO and owner of [Stainless Games](http://www.stainlessgames.com/home/go/), the developer of **Duels of the Planeswalkers**. Last Wednesday, I wrote about [the engine](/en/articles/archive/news/duels-planeswalkers-magic-engine-2009-06-17) that drives **Duels**. In that article, I explained that the **Magic** engine is self-contained (separate from the user interface or any other code) and instance-based (you can have more than one of them at once).

This separation has many advantages, some of which I talked about, but the stand-alone nature of the **Magic** engine is vital in another respect: the AI.




### Basic Concept


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_strategicPlanning.jpg)  
The basic approach to the AI for **Duels** was a simple look-ahead system. In a nutshell, the game would look ahead and experiment with a "tree" of possible futures from the current position. It would say, in essence, "If I played *this* card, then what happens when my opponent then plays *that* card and then attacks me with *those* creatures?" etc. It tries all reasonable combinations, then chooses the action which it predicts will end in the best result from its perspective. Note that it always includes the pseudo-decision "do nothing" in its choices. What this actually means depends on context—it might mean "Skip this phase," "Declare no attackers," "Allow the top item of the stack to resolve," etc.

The AI needs a method of comparing the results of its comparisons. It does this by scoring the world in a static-state fashion. In other words, it doesn't care how it got there—it just looks at the current state and comes up with a number that reflects how beneficial the world is from its perspective. So, for instance, it scores positive points for its life total and negative points for its opponents' life totals. Its permanents score positive (more points for power cards), and its opponents' permanents score negative.

As it back-tracks from looking into the future, the score of a future world-state influences the scores of the states that came before it. So from point A in time, the score is modulated according to what else might happen after point A. Importantly, this doesn't just include what the AI player might do, but also what its opponents might do.

![Bottle Gnomes](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bottle+Gnomes)Let's take an example: You're the **Duels** AI. You're on 1 life, and you have one creature in play, [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes). It's your opponent's first main phase. You have no hand. So your options are to do nothing, or to sacrifice [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes) and get 3 life. However your opponent has a 5/5 creature in play. As you look into the future you see that if you sacrifice [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes), yes, the score is better right now, because you have 4 life rather then 1. However, your opponent then attacks with the 5/5 and you die. Death obviously scores very negatively, which ripples back through and heavily weights the action of sacrificing [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes).

The alternative future path of not sacrificing the Gnomes then also experiments with the your opponent attacking with the 5/5, and you see that you have the option of blocking it with the Gnomes *and* sacrificing them. You still end up on 4 life, but you're not dead! This also ripples back and of course is much more preferable to the plan of sacrificing the Gnomes during your first main phase. You choose to do nothing on your turn, because that scenario has the highest score.




### Reality Check


That's the basic logic. However if you approached the implementation of this system in a simple brute-force fashion, you'd need an orbiting spaceship filled with a multi-dimensional array of massively parallel processors built from alien technology sent through a worm-hole from The Future™. We did try to persuade Microsoft to supply such a vessel with each copy of the game, but sadly they declined.

So the following approaches were taken to make this scheme workable:

**Optimisation** – The **Magic** engine was optimised again and again until it is able to run thousands of possible forward scenarios every second. Examples of optimisation were in static abilities, which original hit the processor hard because every card was checking whether it was affecting every other card. By clever use of scanning techniques during card reading in order to predetermine what might affect what, this core part of the code was sped up a thousand-fold during development.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_parraleThoughts.jpg)  
**Parallelism** – The AI runs on a separate "thread," which runs in parallel to the main game. Thus the thinking happens in the background, without affecting anything on screen. In order to make the most of the Xbox 360's power, this process was moved to another processor in order to operate in a truly parallel manner. We then extended this further by adding three more "sub-contractors." The AI then split its possible actions up and gave work out to these cores, allowing each one to experiment individually on a sub-set of the futures. The principle AI core then compared the results of its sub-contractors with its own result before returning the decision to the main core. 

Although it's easiest to talk about the Xbox 360 having six cores, that's not quite true. It's got three processors that can "sort of" do two things at once! Putting an AI process on the same processor as the main process caused frame rate problems, so we moved all AI off of that processor. So we now have the first processor (cores 0 and 1) running the game that you actually see; core 2 on the second processor running the AI in parallel, and core 3 on this processor and cores 4 and 5 on the third processor acting as AI sub-contractors.

I hope you followed that, as I'll be coming round your house later with a written exam.

**Dismissal of Pointless Actions** – There are a whole host of potentially legal actions that the AI could make that wouldn't make any sense. So we don't even investigate them. For instance: Healing your opponent; playing [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) on your opponent's creature; damaging yourself; destroying your own artifacts. Now of course, it being **Magic**, there will always be some bizarre combination of cards that *would* make these actions legitimate—in fact, one of the Challenges in **Duels** requires this (but we're not telling you which one). However it's better to help the AI make better decisions 99.9% of the time at the cost of it not spotting an ultra-rare loony combo.

It should be noted that after implementing this we realised that it would also be useful for human players, so that feature is turned on by default for humans too. It can be turned off in the options menu for those hard-core maniacs who enjoy casting [Lava Axe](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) on themselves ....

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_lavaAxeFinger.jpg)  
**Dismissal of Unnecessary Actions** – The futures tree suffers from a particularly bad case of foliage explosion when players have instants and activated abilities that they can play, as these can be played on the stack and thus the number of permutations goes crazy. All we need is to have a couple of creatures with regeneration down on the table, and then if we're not careful, we have a futures forest.

We solve this thanks to the observation that from a rules perspective, there is never any justification for putting anything on the stack if *you* already control the top item. Playing A and then stacking B on top of it is no different from playing B first, letting it resolve, and then playing A—or at least not in terms of their isolated effects. There are complex ramifications of opponents knowing that A is also going to resolve in the first case, but here we come back to the idea that the AI needs to be excellent 99% of the time, even if it's at the cost of being sub-optimal that other 1%.

So if there are one or more items already on the stack, and we control the top item, we consider our possible actions to be nothing other than skipping. This trims the tree down considerably.

**Suppression of Pointless Depth** – Although we want the look-ahead to run well into the future, there's really no point in experimenting with actual decisions after about three possible moves, as the uncertainty of the results increases with depth—particularly if one's opponent is holding cards and has untapped mana. So after three levels of decision experimentation (actually six moves, because each decision needs a "skip" decision to allow it to resolve from the stack) we stop trying actions and just default to "skip," allowing the world to move forward and observe the results. This has a significant tree-pruning effect.

**Pre-Sorting of Actions** – I've left the most important technique of all until last. Even with the optimisations and parallelism, as soon as things get complicated, the chances are we aren't going to have enough power (or time) to try every possible action. Therefore it is imperative that we try to make sure that the most likely best action *is* tried, and it's the choices that are almost certainly bad anyway that we don't waste processor power on.

To achieve this we first take our list of possible actions, try each one of them, allow them to resolve, and score the world without any further actions. This can be done very quickly indeed. We then sort this list according to score, and then perform a full tree look-ahead in this order. This way, we are more likely to include the best action in our full look-ahead in the event that we time out before trying everything.

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_hints.jpg)  
This is particularly important in the combat phase. Clearly as soon as each player has a few creatures down, the permutations of attackers and blockers goes through the roof. Even a basic look-ahead on all of these would be impractical, let alone a full-tree look-ahead. So instead we do a super-fast first pass. This takes into account a few basic things such as evasion, trample, and first or double strike, but nothing more sophisticated. It very rapidly tries every combination of attack formations and every combination of block formations for each of these attack formations. (For the propeller-heads out there, it pre-packs first-strike and normal power of both creatures into the 4 bytes of a 32-bit word and the toughnesses of both into another, subtracts the first from the second for each permutation, and inspects the results.)

It then scores the formations according to a simple calculation based on damage dealt (including player death) and creatures destroyed. These results are sorted, and we then have a list of possible attack or block formations in order of probable preference. If the AI is attacking, for each attack permutation, it performs this super-fast block calculation for every blocking possibility, sorts these, then assumes that the opponent will pick the best possible block formation and uses this final score to score the original block formation.

We can then start the full tree look ahead (which sees such things as regeneration, triggered abilities, etc.) on these permutations in an order that is most likely to leave the worst ones untried if we run out of time—which we definitely will do as soon as things get complicated.




### Undoing and Synchronizing


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_unsummon.jpg)  
So, how does the AI actually perform the basic (noncombat) look-ahead, and the full tree look-aheads? Here we come back to the instance-based nature of the **Magic** engine. The game actually contains multiple engines, one for each AI process. These are complete copies of the game in every way bar graphics, sound, etc. They can therefore process events by trying something and instantly skipping forward to see what happens, all without affecting the game that the player can see.

We then need two more pieces to the jigsaw: the AI "worlds" need to be able to synchronise with the player's perspective of the world, and they need to be able to rapidly undo time in order to wander up and down the branches of the futures tree. These two problems end up converging, in the sort of software synergy that happens once in a blue moon. Things normally get *more* complicated the more you think about them in this business, not less!

The need to be able to undo actions required us to incorporate the idea of an "undo buffer" into **Duels**. This is a data buffer into which you pipe a sequence of bespoke commands such that there is sufficient information to interpret the buffer in a reverse direction and completely reverse time. This means that we can fully revert the state of the game to any point in the past in such a way that it is genuinely identical to the state that it was actually in at that point, and can thus re-commence execution from there.

This allows us to rewind after trying something, and then try something else.

Of course, the software engineering hurdles involved in achieving this in such a reliable manner are considerable, and thus beyond the scope of this article. Needless to say, this system is critical to the AI's ability to experiment with multiple possible futures.

However, the free bonus feature that came with the implementation of this system was the ability to synchronise the AI brains with the real world. If we have a system that can define all the actions of the game in a buffer, we can therefore transmit that buffer between versions of the world and thus replicate the state.

How this works is that when something happens in the "real" world—a card or ability is played, something resolves on the stack, a step changes, etc.—the main version of the world pipes this action into its global undo buffer. Through various cunning multi-threaded semaphores and witchcraft, the other AI threads are informed of this.

They then stop whatever it is that they were doing (as whatever it was, it's no longer relevant now that the state of the world has changed). They then collect the data from the global undo buffer from the point that they last knew about, rewind their world to the same point, then apply this data to their own world as a sequence of actions in order to bring themselves to the same state that the main world is in.

This data is extremely small and efficient—it only consists of minimal things such as a certain card being played. The ramifications of this are not piped. Instead these effects are implied because they will occur for themselves in each of the parallel worlds that are used to calculate the AI.




### Strategy


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_strategySchmategy.jpg)  
So how does the AI come up with strategies and cunning combos? It doesn't. What it does is employ a "peep-hole" approach to AI, in that all it ever considers is what it can do (and what other players might do) *right now*. Each time it considers such moves, it no longer has any concept of previous actions, nor any notions of subsequent ones.

The strategies and combos then naturally emerge from this approach.

Let's say it can attack with a 1/1, but you have a 2/2 blocker. However, it has a [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in its hand and an untapped [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest). So it tries two options—attacking with nothing, and attack with the 1/1. For each of these, it then tries all blocking options that its opponent might perform. From this it assumes that when it attacks with the 1/1, it will be blocked by the 2/2, as this provides the best outcome for its opponent.

![Giant Growth](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Giant+Growth)In the blocking priority window it then tries doing nothing, and playing [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). Doing nothing ends up in disaster—its 1/1 dies—but playing the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) is great, as its opponent's 2/2 dies and its 1/1 lives. So this great result ripples back through, because the best possible result for the player in question (which includes the opponent when it's their action—"best" being from *their* perspective) is the one which most influences the scores of what came before it in the tree.

So the result is that attacking with the 1/1 is better than doing nothing, even though it doesn't now "know" that it needs to play the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). The logic is that if it was better to do this when looking ahead, it's still going to be better to do this when it comes to actually making that decision in the future. Or, if it's not, because something else has changed, (e.g. an opponent played an instant that the AI wasn't expecting), it will then re-assess the situation based on the new state.

So the 1/1 attacks. The opponent then probably blocks with the 2/2, and the AI then kicks in again, evaluates doing nothing or playing the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth), and lo and behold the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) is better, so it plays it.

From the player's perspective, the AI has just been wickedly clever, and has lured them into a trap which has killed their 2/2. In fact all that happened was a simple sequence of logic (simple in concept, not in implementation!).

Note that in its first main phase, the AI would have experimented with playing [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) as well, but would have observed that if it had done so, the player wouldn't have blocked and thus wouldn't have lost the 2/2—so it didn't play it (unless it considered the loss of 4 life more valuable that the loss of a creature, which is not the case on 20 life but might be on lower life totals). 




### Limitations


So what problems emerge from this system? Well firstly, we just don't have the horsepower to look that far ahead. Crucially, this means that the AI doesn't understand the concept of holding back blockers to protect against your attack next turn, so sometimes it can be quite dumb in this respect. We do intend to address this in the future with specific code to look for precisely this. Right now, though, it actually rarely damages the AI's chances as it does mean that it plays extremely aggressively, which, interestingly, seems to bring pretty good results.

Secondly, it generally does not do things based on deck-specific knowledge, e.g. not playing an unneeded land so we have a sacrificial discard because the opponent is playing a black deck; teasing out counter-spells by playing inferior cards first; *not* blocking that 1/1 with its 2/2 when it opponent very suspiciously has an untapped [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) and a card in hand, etc. But is this a bad thing? Maybe not .... Rather than trying to second guess what *might* happen like a human does, it plays utterly logically based on nothing but the facts in front of it, which most of the time is probably better than trying to be big and clever.




### Lessons


Interestingly, as an experienced—but decidedly amateur—**Magic** player myself, I've actually learned a few tricks from my own AI! One thing it's particularly good at is damaging its opponent's creatures by direct damage spells and abilities *before* it declares attackers. The opponent is then heavily restricted as to what they can block with, as the blockers will die. Because in the paper game, keeping track of damage on creatures is far from easy, this had simply never occurred to me.

Then there's the time it attacked with a bunch of green creatures, let me block, and only *then* used [Elvish Piper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Piper) to drop a [Roughshod Mentor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Roughshod+Mentor) into play and give everything trample. Aaaah, how I laughed ....



|  |  |  |
| --- | --- | --- |
| Elvish Piper | Roughshod Mentor |  |

Anyway, that's a brief look into the **Duels of the Planeswalkers** AI. It might sound complicated, but actually? It's *much* more complicated that the above makes it sound! I've simplified a lot of things for this article. Hopefully you can get a feel for how it thinks and breathes.

And even if not, go out and play it. Maybe my code will kick your ass once in a while! Or maybe not. Either way, I think you'll enjoy playing it almost as much as I enjoyed writing it.

[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature44_cta.jpg)](http://www.wizards.com/Magic/Digital/Default.aspx)





