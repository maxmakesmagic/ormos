
---
[Link to Wayback Machine](https://web.archive.org/web/20210211162931/https://magic.wizards.com/en/articles/archive/theory-games-2007-09-12)

[_metadata_:author]:- "Frank Karsten"
[_metadata_:description]:- "Today I’m not going to do an overview of last week’s metagame and the latest deck tech, as I was too busy slinging spells and sight-seeing in Florence last weekend to find enough time or an internet connection to report on the Premier Events. Instead, I wrote a discussion of the game of Magic from several theoretic frameworks. A couple months ago, I wrote an article on game"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "624711"
[_metadata_:publish_date]:- "2007-09-12"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Theory Games"
[_metadata_:wayback_capture_timestamp]:- "2021-02-11 16:29:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210211162931id_/https://magic.wizards.com/en/articles/archive/theory-games-2007-09-12"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/theory-games-2007-09-12"
---


Theory Games
============



 Posted in **Feature**
 on September 12, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_FrankKarsten.jpg)
By Frank Karsten












Today I’m not going to do an overview of last week’s metagame and the latest deck tech, as I was too busy slinging spells and sight-seeing in Florence last weekend to find enough time or an internet connection to report on the Premier Events. Instead, I wrote a discussion of the game of **Magic** from several theoretic frameworks.



![Gifts Ungiven](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gifts+Ungiven)

A couple months ago, I wrote [an article on game theory](/en/articles/archive/introduction-game-theory-2007-05-30) where I covered the issue of metagaming. When I need to choose a Constructed deck for an upcoming tournament, I usually take the deck that I consider to have the highest overall win probability against an estimated metagame (which, for any deck, can be computed as my chance to beat a certain opposing deck multiplied by what percentage of the opponents in that tournament I expect to play that deck, summed over all opposing decks). Usually, I end up with a stable control deck that stands a good chance against everything, with the tools to beat any strategy. I like well-balanced decks that are not particularly good against anything, but that don’t have auto-losses either. A [Gifts Ungiven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven) control deck with a consistent game plan and “silver bullet” one-ofs comes to mind as an example.

Now, I am a pretty consistent player myself. I often post decent finishes, like Top 32s or Top 16s at Pro Tours and Grand Prix, which is nothing to complain about. And my Pro Tour median finish is quite good. But I rarely finish in the spotlights. Compare my eight (if I recall correctly) Pro Tour Top 20s to my two Pro Tour Top 8s and you see a skewed distribution. And last season it seemed like I was doomed to finish in the Top 32 of almost every single Grand Prix I went to (and in all three Block Constructed Grand Prix I played this year I made Top 16 or Top 32). These consistent good finishes may sound appealing, and frankly I am happy with them. But you can also view them in another way; there is a downside to consistent decent finishes: you distribute the total amount of match wins and match losses over multiple tournaments, in such a way to minimize your winnings. For example, if you knew in advance that you would get 20 wins and 8 losses in the next two Grand Prix tournaments you would, how would distribute them? Well, the best way is to put all wins in one tournament and all losses in another. This way, you win one Grand Prix and you scrub out in another, and you win a first place prize. The absolute worst way to do it is to go 10-4 in both tournaments, ending up with, let’s say, two Top 32s. Even by simply turning that into one 11-3 (likely Top 8) and one 9-5 (probably Top 64), you would improve your total winnings, as one Top 8 is worth more than two Top 32s in terms of prize money (not to mention eternal fame). See my point?


But I’m not here to whine. It’s no use; whining won’t improve my winnings in the future, just like whining about mana screw or mana flood after losing—no matter how frustrating that game may have been—will not make you into a better player. Instead, you should always look at the plays you made and the deck you played in order to learn and to get better. Should you have attacked that turn? Should you have taken a mulligan after all? And... did you pick the correct deck?


As I had said before, for a tournament I tend to choose the deck with the highest overall win probability against an estimated metagame. Furthermore, I enjoy playing stable control decks that do well against everything. I’ll illustrate this with a simplified example. Imagine I was expecting a metagame consisting of only three decks, all with equal popularity: one-third “Control,” one-third “Aggro,” and one-third “Combo.” I would have a choice between two decks myself: “Stable Control,” which has approximately 50% against every deck, or “Meta Owling Mine,” which has a lot of variance in its matchup stats.




|  |  |  |  |
| --- | --- | --- | --- |
|  | vs. Control | vs. Aggro | vs. Combo |
| "Stable Control" | 55% | 55% | 45 |
| "Meta Owling Mine" | 85% | 15% | 50 |

I would calculate the overall win expectancy against the expected field for each deck. For “Stable Control,” this would be 55/3 + 55/3 + 45/3 = 51.7%. For “Meta Owling Mine,” this would be 85/3 + 15/3 + 50/3 = 50.0%. Clearly, I would pick “Stable Control.” It has the highest chance of winning, and therefore it is the deck with the highest chance of winning the tournament.


Or is it?


Well, wait a minute. What exactly are we trying to optimize here? By making the causal connection between a deck that has the best expected match win percentage against the field and a deck that has the best chance of winning a tournament, I’m making a grievous mistake, the impact of which has only recently begun to hit me. Maximizing win expectancy against the field does not equal maximizing the odds of winning the tournament! If I were just trying to maximize the expected value of my number of match wins, or if I were just trying to maximize the amount of rating points I pick up, then “Stable Control” is undeniably the best choice. But usually, that is not what I truly want to maximize. Rather, I want to maximize my prize winnings in a tournament (well, at a Pro Tour at least.... At a local FNM tournament my goal would be to have fun and enjoy my games, but stick with me). And here’s where I went wrong: maximizing my expected number of match wins will lead to the stable consistent finishes that I usually post, but it does not always maximize my prize winnings!


This is because of two things: uncertainty and payoff distribution. The latter refers to the top-heavy payouts of tournaments, which I already touched upon. If you go 12-4 at a Pro Tour and finish in the Top 8, you win at least $10,000. If you had lost one more match for an 11-5 record, you would finish around 30th place or so, which pays $1,500. This type of effect is also visible in online Premier Events; if you go 4-2 twice, then you may finish in 10th place twice and win nothing. But if you go 5-1 once and 2-4 the other time, then you could make a Top 8 and win booster prizes. So consistent finishes don’t really get you anywhere. Rather, variable finishes are rewarded. The payoff distribution at **Magic** tournaments favors the big finishes.



![Ebony Owl Netsuke](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ebony+Owl+Netsuke)

But how to aim for variable finishes? Sometimes I hear people talk about choosing a “5-1 deck” or “a hit-or-miss build,” but how does that work? I mean, we had a “Stable Control” deck with 51.7% against the field and a “Meta Owling Mine” deck with 50.0% against the field. How can picking one or the other lead to a better shot on Top 8? Shouldn’t we still just choose “Stable Control” since it has the better chance of winning a match overall? Well, here is where uncertainty comes in. That 51.7 match win percentage against the field is not a deterministic fixed number. It is the best estimate of the true value based on the information available, but it is still a stochastic random value. It is based on a couple assumptions: that the metagame is exactly as expected and that the matchup stats you got in your playtest games are correct. Those assumptions will not hold completely in real life situations, so there is some variability. I will take tackle one aspect; the one of a variable metagame. The analysis of the situation with variable matchup stats is done in similar way.


Okay, first I gave you the estimation that the metagame consisted of only three decks, all with equal popularity: one-third “Control,” one-third “Aggro,” and one-third “Combo.” It is, however, more accurate to model the metagame with a probability distribution. After all, you are never sure how exactly the metagame will shape up in the end. Let’s say that there is a 25% chance of each of the following:




|  |  |
| --- | --- |
| A. | two-thirds “Control,” one-sixth “Aggro,” one-sixth “Combo” |
| B. | one-sixth “Control,” two-thirds “Aggro,” one-sixth “Combo” |
| C. | one-sixth “Control,” one-sixth “Aggro,” two-thirds “Combo” |
| D. | one-third “Control,” one-third “Aggro,” one-third “Combo” |

In real life these distributions will be less awkward and more continuous, but I am just illustrating a point here with a simplified analysis. Now, let’s say that this tournament will be a six-round PTQ or online Premier Event and that 5-1 or better is likely to make the Top 8. Maximizing the probability of making the Top 8 is the sole goal.


Now, “Stable Control” doesn’t care all that much about which metagame it faces. It had 55% vs “Control,” 55% vs “Aggro,” and 45% vs “Combo.” It likes to see a “Control” or “Aggro” heavy metagame (A and B, in which case it can be shown to have a 14.4% shot to make Top 8), and it doesn’t like a “Combo” heavy metagame (C, where basic statistics yield a 9.5% chance to make Top 8). But the differences in outcome are relatively small.


The performance of “Meta Owling Mine,” on the other hand, is heavily sensitive to the metagame. It had 85% vs “Control,” 15% vs “Aggro,” and 50% vs “Combo.” Clearly, it will do very well in a metagame packed with “Control” (meta A, 37.5% to make Top 8). However, it will lose out in a metagame packed with “Aggro” (meta B, 1.6% to make Top 8).


And there is the big difference; put “Stable Control” once against metagame A and once against metagame B, and you will rack up 0.288 Top 8s on average. Put “Meta Owling Mine” once against metagame A and once against metagame B, and it will rack up 0.391 Top 8s on average. So trying to go for the big record by taking a volatile deck with extreme matchup percentages does work! Overall, against the given metagame probability distribution “Stable Control” has a 12.7% chance to make Top 8, whereas “Meta Owling Mine” has a 15.5% chance to make Top 8, and it will therefore rack up more winnings—even though “Stable Control” had a higher win percentage (51.7%) than “Meta Owling Mine” (50.0%) against the expected field! But that is easily compensated by how well “Meta Owling Mine” does against control-heavy metagames.



![Dampen Thought](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dampen+Thought)

This knowledge can also be applied to 8-man draft situations. Let’s say you can either decide between:

* A safe draft strategy that favors solid spells and card advantage and has a deterministic 55% chance to win a match in the draft pod.
* A risky draft strategy (like Dampen Thought or Slivers), where you can end up with an amazing deck if you get passed the goods, but if you don’t get any of the key cards then your deck will horrendous. Let’s say, for the sake of argument, that half of the time you will end up with amazing deck that has an 80% chance to win a match in the draft pod, and the other half of the time you will end up with a horrendous deck that has a 10% chance to win a match in the draft pod.

It is not hard to show that the expected amount of wins (which is still relevant for things like rating) is higher for the safe draft strategy. But if you assume that you play three rounds, and that the prize payout is five boosters for the 3-0 player and one booster for all 2-1 players (draws are not allowed in this scenario), then you can calculate the expected amount of boosters winnings for the both strategy to see that the safe strategy wins 1.24 boosters on average, and the risky strategy wins 1.49 boosters on average. So it is possible to work with “0-3 or 3-0, c’mon” strategies and to increase your winnings with them, given top-heavy payouts. The next question would be how much of your expected match win percentage against the field you can sacrifice for high variance decks, but that relation is beyond the scope of this article. I merely wanted to illustrate this effect and how it can matter.


### Next Up: Should You Expect Optimal Play or Mistakes from Opponents?


Imagine the following situation. You are playing a Gruul aggro mirror match. Your opponent led out with a [Stomping Ground](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stomping+Ground) and a [Mogg Fanatic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Fanatic). You made a [Forest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) and a [Llanowar Elves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) on your first turn. On his second turn, your opponent attacks with his [Mogg Fanatic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Fanatic). Should you block?


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/online/fk56_moggelves.jpg)If you decide to block with your Elf, he will stack damage and fling the Mogg for 1 final point of damage to your head (End result: no creatures in play, you are at 19).


If you decide not to block with your Elf, your opponent has two choices. He can either decide to keep the Mogg in play (end result: Mogg and Elf still in play, you are at 19), or he can ping your Elf (end result: no creatures in play, you are at 19; that’s the same as if you had blocked).


So if you block, you make the choice for your opponent. If you do not block, your opponent makes the choice for you. It would seem that blocking is the smart choice. Giving your opponent extra options for free does not make a lot of sense; you want to constrain him as much as possible... if everyone behaves like optimal, rational beings, that is. But humans are fallible. It may be advantageous to give your opponent bad options in order to induce a mistake. If you do not block, your opponent may make the mistake of not pinging your Elf, and then you can start casting your [Troll Ascetic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Troll+Ascetic)s one turn earlier (your opponent does not know you have it of course, but if he is smart then he can guess you have something like that, because you don’t block). If you expect him to make that mistake, it is probably correct to not block there. But this comes at a cost. By responding to potential weaknesses in your opponent’s strategy, you leave exploitable holes in your own strategy. It’s just like in poker; the strategy that the other players at the table cannot improve against is not the one that has the best success (as it doesn’t try to exploit opponent’s mistakes). Perhaps your opponent was really hoping you would not block, so that he could keep his [Mogg Fanatic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Fanatic) in play. He may have multiple [Moldervine Cloak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moldervine+Cloak)s in hand and no other creatures. And then not blocking will have grave consequences.


Another example that illustrates the same idea of giving your opponent choices that you do not have to give him is when you have a [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) in hand and your opponent has a [Burr Grafter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burr+Grafter) and a [Meddling Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage). You should be able to figure out the correct creature to [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock).


In situations like these, the question comes up of whether to assume your opponent plays optimally so that you anticipate that and play accordingly (just block, don’t give him additional options) or whether to assume your opponent may make mistakes so that you can potentially take advantage of those (don’t block, and hope he fails to ping your Elf, even though this can backfire if he has multiple Cloaks in hand).


A related (but slightly different) concept is bluffing. I’ll give an example. You are playing your Block Constructed Blue-Black Teachings Control deck against your buddy’s White-Green [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf) Aggro deck. You lost the die roll and had to mulligan down to a five-card hand of 2 [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island), [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth), [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens), and [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation). Your opponent started out okay, with a [Riftsweeper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) and a [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf) (1/2 due to a [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)) on his first three turns. Now, on your third turn, your board is 2 [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)s and [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens). You have only drawn [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears) so far—three in a row!—so your hand is Urborg, 3 [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears), and [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation).


The first question in this situation would be “play [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) or no?” I am fairly sure that the answer is “not yet” in this case. Your draw this game has consisted of lands and only one business spell, so you have to get the fullest potential out of it. You need some heavy card advantage to get back in this game. Since you are not under a lot of pressure yet, I would wait at least one turn, hoping that your opponent will add another creature to the board—at which point it’s probably time to play [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation), potentially taking out another threat is well worth the couple points of damage in this situation.


[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Urborg%252C%2BTomb%2Bof%2BYawgmoth)But an even more interesting question might be, “Should you play a land or not?” I think everyone’s initial response—including mine—would be, “Of course, you are holding four!” However... if you play a land (be it [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears) or Urborg), you effectively signal to your opponent that you can easily play [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) next turn if you have it, which may make him more cautious and less likely to overextend. On the other hand, if you don’t play a land and pass, then you effectively signal to your opponent that you are mana-screwed, stuck on two [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)s and a Lens, with probably lots of expensive big cards in hand. That may certainly incline him to overextend—perhaps playing two creatures on his next turn—in the hope of killing you quickly before you draw your land and you can start casting your big spells (I mean, he may anticipate that the Teachings player has [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) in hand, but he can only topdeck Urborg to play it next turn...he will view those odds are very slim). And then you can say “ding!” and play Urborg and [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) on your next turn. Let’s assume, for the sake of the argument, that your opponent will never play two additional creatures if you make your land, but he may do it if you pass without playing a land.


While the benefits of that “land slow-roll” play may be high, there is also a clear downside: you miss a land drop. This may be important if, for example, you draw [Triskelavus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triskelavus) next turn, which will then come down one turn later because you missed a land drop. Deceptively not playing that land may prove especially detrimental if your opponent doesn’t add additional creatures to his board on his next turn (perhaps he reads you like a book, or perhaps he has nothing but lands). [Clear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clear)ly, you are worse off in the worst-case scenario of not playing a land than in the worse-case scenario of playing that land. But should you base your plays on best-case scenarios (where your opponent can make a play that can turn out very bad for him, i.e. overextending in this example) or on worst-case scenarios (where your opponent gives maximal resistance, fictively knowing the contents of your hand and playing accordingly)?


I asked a couple fellow pro players their thoughts on this issue.


**Jelger Wiegersma:** It always depends on the opponent. I usually assume they play close to optimal, unless (like in the second example) he really has to start making mistakes in order to give me a chance to win.


**Wessel Oomens:** I always assume my opponents are good players and that they at least make good decisions. So I would be inclined to block the Fanatic and play the land (you also play Teachings in the last situation, which makes it better). However, you have to think about funny plays like the second example very quickly. If you start thinking whether or not to play a land, your opponent will catch on to you.


**Roel van Heeswijk:** The answer to the first problem is dependent on how good the opponent is. The answer on the second one is the probability to get profit from not playing a land times the value of that profit versus the loss of not playing a land times the value of that loss, which looks negative to me. Especially when playing an Urborg may signal Teachings into Tendrils, which may incline your opponent to play extra creatures after all.


**And lastly, my take:** While I assume my opponents will usually play optimally, I try to look for situations with high reward and low risk and try to pull those. The first situation seems like it has high reward (you have Troll in hand; your opponent probably does not have multiple Cloaks) and low risk (very likely your opponent will ping your Elf anyway). The second situation seems like it has low reward (I think the odds of your opponent overextending in response to not playing a land are relatively low) and high risk (the deck is full of expensive cards, so missing that land drop is huge). So I would try to induce a mistake in the first situation, not in the second one.


### Is Magic a Game of Skill or a Game of Chance?


Often when I explain the game of **Magic** to non-gamers, I am asked whether it is more like a game of skill (such as chess) or a game of chance (such as roulette). When I explain that it is a little of both, with strategic decisions that can positively or negatively influence your position in the game, and with random shuffling of decks that is admittedly a chance element, I am still unable to say exactly how much of **Magic** is skill and how much is chance. Not to mention it’s probably dependant on the matchup.


In my studies, I lately came across an interesting Ph D. thesis by Dreef [\*](#footnote1), called “Skill and Strategy in Games,” which used a method developed by Borm and Van der Genugten [\*\*](#footnote2) in order to measure the amount of skill relative to the amount of chance in a game. This method can for example be applied to poker, in order to provide a better ground to base government legislation on. I, of course, thought about applying this method to **Magic**. Their measure of skill in games is as follows:


Skill = learning effect / (learning effect + random effect)


The learning effect is defined as the difference in expected result between a beginner—who plays the game in the naïve way of somebody who has merely understood the rules of the game, but has not understood intricate strategies yet—and an optimal player, who always makes the profit maximizing play at every stage, which approximates a player like Kai Budde. The random effect is defined as the difference in expected result between an optimal player and a virtual optimal player—whom we tell in advance the outcome of chance elements. In a game of chess, with no random dealing of cards, there is no difference between an optimal player and a virtual optimal player, so then the skill measure reduces to 1. In a game of “flip a coin,” where the only decision moment is calling “heads” or “tails,” there is no difference between a beginner and an optimal player, so then the skill measure reduces to 0. It looks like this skill measure is appropriate.


[![Gemstone_Caverns](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/TSP/Gemstone_Caverns.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Gemstone%2BCaverns)How can we apply this skill measure to **Magic**? Well, we need to know the expected result of a beginner (in terms of probability to win a match), of an optimal player, and of a virtual optimal player, when they play against an optimal player. An optimal player vs. another optimal player clearly yields a 50-50 matchup. The probability that a beginner defeats an optimal player can be determined with the Elo rating system used by the DCI. Therein, a win probability is defined that is used to determine rating changes, calculated as 1 / { 10 ^ [ ( Opponent’s Rating – Player’s Rating ) / 400 ) ] +1 }. A beginner’s rating is automatically set at 1600. A good estimate for the rating of an optimal player would be a rating of 2150. This gives the beginner a 4.05% chance of winning, and—based on general consensus on where better players can get their edges—let’s split that up into 0.10% chance to win a control mirror match and an 8.00% chance to win an aggro mirror match. The expected result of a virtual optimal player is a little harder to decide, but that’s where the game theory exercise that I posed in my column [two weeks ago](/en/articles/archive/extended-education-2007-08-29) comes in.


I asked you to what extent the availability of hidden information and knowledge of outcomes of random chance elements in advance would help. You could learn the exact order of all cards in player’s libraries, the contents of your opponent’s hand, etcetera. I split this up into two questions: one where this better informed player plays a control mirror match (against another equally good optimal player like Jon Finkel or Kai Budde, who lacks the information) and one where he plays an aggro mirror match. I should have made clearer whether I meant game or match, and taken out sideboard impurities, but I still think I managed to get the point across. Thanks for voting in the poll! The results were:




|  |  |  |
| --- | --- | --- |
| **What is the better-informed control player's chance of winning?**  |  |  |
| 50-55% | 133 | 3.0% |
| 55-60% | 126 | 2.9% |
| 60-65% | 317 | 7.2% |
| 65-70% | 348 | 7.9% |
| 70-75% | 559 | 12.7% |
| 75-80% | 580 | 13.2% |
| 80-85% | 759 | 17.2% |
| 85-90% | 649 | 14.7% |
| 90-95% | 441 | 10.0% |
| 95-100% | 495 | 11.2% |
| **Total** | **4407** | **100.0%** |

Average: 79.8%.




|  |  |  |
| --- | --- | --- |
| **What is the better-informed aggro player's chance of winning?**  |  |  |
| 50-55% | 386 | 10.4% |
| 55-60% | 468 | 12.6% |
| 60-65% | 632 | 17.0% |
| 65-70% | 439 | 11.8% |
| 70-75% | 463 | 12.5% |
| 75-80% | 349 | 9.4% |
| 80-85% | 348 | 9.4% |
| 85-90% | 252 | 6.8% |
| 90-95% | 176 | 4.7% |
| 95-100% | 203 | 5.5% |
| **Total** | **3716** | **100.0%** |

Average: 71.0%.


That is roughly what I expected to see. An aggro mirror often comes down to quickly playing your threats and the better draw will win. The information gained helps mainly in deciding when to mulligan and to decide whether to fling that burn at players or creatures, depending on whether there is more burn on top or no. With perfect information in the control mirror, you can respond to everything correctly, which makes your countermagic much better. Control mirrors tend to take longer than aggro mirrors, with more decision moments, and long-term strategy is more important, so you have more time to put that information to use.


[![Lurking_Informant](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/RAV/Lurking_Informant.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Lurking%2BInformant) I believe—like the outcome of the poll—that the perfect information is more important in the control mirror. But I think the difference is as large as some people may think, because in aggro mirrors that only take a small number of turns, the players see a smaller fraction of their deck than in control mirrors, which increases the random element. And in the control mirror you usually get part of the information anyway. By clever deduction, you can often figure out part of the contents of opponent’s hand (along the lines of: “Hmm, he didn’t play a card draw spell or removal last turn, so he probably does not have those, and these cards are already in his graveyard, which leaves...”). But still, knowing the order of the libraries is beneficial, especially if you play with [Mystical Teachings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings). I would personally have voted for 85-90% in the control mirror and 80-85% in the aggro mirror.


This was an interesting thought experiment that also tells us that about 20% of the games you play you can never win, no matter what plays you make. But coincidentally it also gives us the result of the virtual optimal player from the skill vs. chance measure, as this poll has effectively asked you to give the win probability of a virtual optimal player.


Now, let’s calculate the amount of skill in a game of **Magic**. Recall that skill was defined as learning effect / (learning effect + random effect), in other words (optimal player result – beginner’s result) / { (optimal player result – beginner’s result) + (virtual optimal player result – optimal player result) }. Putting in all the values we have gotten so far (using the average of the poll results), we get the following:


Aggro mirror: skill = 66.7 %.  

Control mirror: skill = 62.6%.


That’s a surprising result ... the aggro mirror is more skill intensive? We can view this outcome in several ways:


1 – The skill measure is inaccurate; it does not measure skill vs. chance well enough.  

2 – The Elo rating system is wrong; it doesn’t determine the chance a beginner can beat an optimal player accurately.  

3 – The poll results were wrong; the true results of a virtual optimal player are different.  

4 – The aggro mirror is truly more skill dependent.


You be the judge. I think the first one is most applicable. I think that a skill measure that would be based on the amount of decision moments in games may be better. In chess you have many decision moments, and when you flip a coin there is only one decision moment. The more decisions, the more skill is introduced. And using such a measure, control mirrors would certainly come out as more skill intensive.


No matter how you look at it, at least in the future you can tell anyone who asks how much of **Magic** is skill and how much is chance that it is roughly two-thirds skill and one-third chance. That much we have learned, using scientific methods.


### On to the Invitational


I am looking forward to playing in the  [**Magic** Invitational](/en/node/580771)  again this year. Trying to break the wacky formats will certainly be a lot of fun, and there is always the honor of making your own card for the first place finisher. Well, at least I can hope. Last year, I designed a card that combined the mechanic on [Gifts Ungiven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven) (my favorite card), mulligans (my favorite part of the game), and hybrid mana cost (my favorite mechanic):



> **Evolution Spawn**  
> 
> Mana cost: {hybrid blue-black} + {hybrid blue-green}  
> 
> Creature — Zombie Minion  
> 
> 1/4  
> 
> When Evolution Spawn comes into play, search your library for exactly three cards with different names. For each mulligan you took this game, an opponent chooses one of those cards. Put the chosen cards into your hand and the rest into your graveyard. Then shuffle your library.


I liked this card, but I wanted to submit something different this year. After all, it would be kind of lame to submit the same card in two consecutive years. And I think I found a cool idea in the virtual optimal player from the last section, who knows the outcome of random chance elements in advance. Information as a resource is an underused design angle, in my opinion. I think I can take a card based on this theme in two directions: either it gives its controller knowledge of hidden information, or it hands it to your opponent in exchange for some effect. What would knowledge of your opponent’s hand (so the card has to have some “reveal” clause) and the top of the libraries (an effect similar to [Sensei’s Divining Top](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei%E2%80%99s+Divining+Top)) be worth?


An email by Jason S. and a forum post by torturedsouls acted as more inspiration, and now I have two basic ideas that I’d like to share.



> **Niflheim**  
> 
> Land  
> 
> T: Add UB or RB to your mana pool.  
> 
> Play with your hand and the top card of your library revealed.  
> 
> XX: Look at the top X cards of target player’s library, then put them back in any order. Only an opponent may play this ability.



> **Wall of the Beholder**  
> 
> 1UU  
> 
> Creature – Eye Wall  
> 
> 1/4  
> 
> Defender  
> 
> Opponents play with their hand and the top card of their library revealed  
> 
> XX: Look at the top X cards of target player’s library, then put them back in any order.


I would love any input and ideas for tweaking are greatly appreciated. Let me know what you think about the power level of these cards and which of the two you like best!


[\*](#footnote1a) M. Dreef (2005), Skill and Strategy in Games. Ph.D. thesis, UvT, ISBN 9056681486  
[\*\*](#footnote2a) P. Borm, and B. van der Genugten (2001). On a Relative Measure of Skill for  

Games with Chance Elements. Trabajos de Investigacion Operativa 9(1), 91–114.








