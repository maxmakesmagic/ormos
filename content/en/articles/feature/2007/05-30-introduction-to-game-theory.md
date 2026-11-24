---
id: qb9vhmpe
kind: article
lang: en
path: /en/articles/feature/2007/05-30-introduction-to-game-theory
title: Introduction to Game Theory
published: '2007-05-30'
column_slug: feature
column: Feature
authors:
- slug: frankkarsten
  name: Frank Karsten
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    lang_detected: en
    capture_id: 186504
    url: https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    captured_at: '2024-05-18 04:12:38+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    lang_detected: en
    capture_id: 186504
    url: https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    captured_at: '2024-05-18 04:12:38+00'
    rule: jsonld.date_published
  column:
    page_key: magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    lang_detected: en
    capture_id: 186504
    url: https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
    captured_at: '2024-05-18 04:12:38+00'
    rule: url.article_section
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/introduction-game-theory-2007-05-30
    lang_detected: en
    capture_id: 714546
    url: https://magic.wizards.com/en/articles/archive/introduction-game-theory-2007-05-30
    captured_at: '2022-08-07 23:23:01+00'
    rule: drupal.div_author
sources:
- document_id: qb9vhmpe
  url: https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
  page_key: magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:12:38+00'
  capture_id: 186504
  wayback_url: https://web.archive.org/web/20240518041238id_/https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
- document_id: qb9vhmpe
  url: https://magic.wizards.com/en/articles/archive/introduction-game-theory-2007-05-30
  page_key: magic.wizards.com/en/articles/archive/introduction-game-theory-2007-05-30
  lang: en
  template: drupal
  captured_at: '2022-08-07 23:23:01+00'
  capture_id: 714546
  wayback_url: https://web.archive.org/web/20220807232301id_/https://magic.wizards.com/en/articles/archive/introduction-game-theory-2007-05-30
- document_id: qb9vhmpe
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/fk41
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/fk41
  lang: en
  template: aspx
  captured_at: '2014-03-17 18:41:38+00'
  capture_id: 791740
  wayback_url: https://web.archive.org/web/20140317184138id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/fk41
- document_id: qb9vhmpe
  url: http://wizards.com/default.asp?x=mtgcom/daily/fk41
  page_key: wizards.com/default.asp?x=mtgcom/daily/fk41
  lang: en
  template: classic_asp
  captured_at: '2007-10-18 17:54:18+00'
  capture_id: 1950926
  wayback_url: https://web.archive.org/web/20071018175418id_/http://wizards.com/default.asp?x=mtgcom/daily/fk41
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: qb9vhmpe
  capture_id: 186504
  url: https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
  wayback_url: https://web.archive.org/web/20240518041238id_/https://magic.wizards.com/en/news/feature/introduction-game-theory-2007-05-30
  captured_at: '2024-05-18 04:12:38+00'
  template: contentful
  sha256: 1c388dd9e34df35201c42a5502a5d59918ae0dfed20741cf3bc21504a9579bce
render_recovery: []
---
Welcometo Theme Week Week here at Online Tech! This week, I was supposed to come up with a special novel theme for my column that could conceivably be used as a theme week in the future. I came up with a serious theme about a topic that I find quite captivating: Game Theory Week. As a gamer, I appreciate the solution concepts and problem formulations that game theory offers, especially when applied to the game of Magic.

### Game Theory Introduction

[![Goblin_Game](https://i.ormos.uk/59/ea/59ea39c8832390d51441d65420fd5e8196618f3a2b9d71ca8b51aade490f81d4.jpg)](https://web.archive.org/web/20070530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Goblin%2BGame)[Game theory](http://www.gametheory.net/) is a branch of applied mathematics that deals with the modeling and analysis of interactive strategic behavior among various players. It is applicable to situations where decision making between various individuals can result in conflict or cooperation between them. Today I will focus on noncooperative game theory, which models and analyses conflict situations where each opposing decision maker tries to find the best strategy for himself. Game theory can then define the best strategy or outline the best decision making techniques for each player.

I will try to correlate the conceptual game theory ideas with various elements of **Magic**—for example, to learn which plays and choices game theory tells you to make in order to maximize your chances of winning a game of **Magic**. Most of these will be highly theoretical and mathematical, and not directly useful. Nevertheless, I like to think that an article offering interesting new approaches and perspectives can improve your conceptual understanding of the roots of game. I hope it will be a fun read that broadens your horizons.

### Game Theory, Example 1

**The Famous Prisoner's Dilemma: The Draft Game**

This example will be an application of the classic Prisoner's Dilemma, which illustrates many of the principles of game theory in a nutshell.

Imagine you and your friend (Team A) sit down for a Two-Headed Giant draft. You have two possible draft strategies: draft Slivers or don't draft Slivers. Let's assume that, for the sake of the argument, you have to choose between these two strategies right away during your first pick. The team to your left (Team B) faces the same strategic choice as your team: Slivers or no? There are two other two teams (Team C and Team D) in the draft, but you know that they despise Slivers with a passion, so they won't touch that creature type for sure. Now, Slivers is a tricky archetype in Two-Headed Giant drafts. They get better in multiples and are only good if you get a critical mass of them. If more than one team drafts Slivers, they will divide all the Sliver cards in the draft between them. That would entail mutual obstruction; neither teams will be able to collect enough Slivers to make a synergetic deck, and both will end up with very mediocre decks.

A convenient way to represent the outcome of this draft strategy choice game is by a vector-valued matrix, in which the rows correspond to the strategy of Team A and the columns represent to the strategy of Team B. In each cell, we then write the payoff for Team A followed by the payoff for Team B. In this case, the payoffs will represent the expected amount of match wins a team will get in this draft. The outcome of each choice depends on the choice of the other team, but you have to choose without knowing what the other team will do. Both teams know—somehow—the exact value of these payoffs in this example. Don't pin me down on these numbers; they are not completely accurate representations of what really happens in such a draft, although the underlying structure of the number sequence distribution is defendable with the assumption that Team A will certainly play against Team B in Round 1.

<table><thead><tr><td> </td><td colspan="3"><b>Team B</b></td></tr></thead><tbody><tr><td rowspan="3"><b>Team A</b></td><td> </td><td>Draft Slivers</td><td>Don’t draft Slivers</td></tr><tr><td>Draft Slivers</td><td>1, 1</td><td>1¾, ⅔</td></tr><tr><td>Don’t draft Slivers</td><td>⅔, 1¾</td><td>1¼, 1¼</td></tr></tbody></table>

You should read the matrix like this: If both teams decide to draft Slivers, they can each expect to win 1 match in this draft. If Team A decides to draft Slivers and Team B decides not to draft Slivers, then Team A has an expected value of 1¾ match wins and Team B has an expected value of ⅔ match win. What would your strategy be?

![Might Sliver with a question mark](https://i.ormos.uk/5e/2a/5e2a0b7281fc84d42732a5ec139caa416f94301779ee23323a64563b3522e203.jpg)Now let's take the stance of Team A and see what the optimal rational, self-interested strategic choice would be. If Team B decides to draft Slivers, Team A's best choice would be to draft Slivers (1⅔). If Team B decides not to draft Slivers, Team A's best choice would be to draft Slivers (1¾1¼). So drafting Slivers is a dominant strategy; it is more beneficial to choose, no matter what the other team's strategy is. Team B will reason along similar lines as Team A, and will therefore choose to draft Slivers as well. You don't even have to predict what the other team will do; drafting Slivers is always better for yourself.

Yet, by both drafting Slivers the teams get a lower payoff than they would have gotten by not drafting Slivers. If the teams would cooperate, then they would both choose not to draft Slivers, effectively helping each other to a better record, as 1¼ + 1¼ is the best possible record outcome of all the options. But since the teams only care about their own self-interest, such cooperation is not stable. Any team can improve by stepping out of this cooperation by choosing to draft Slivers, beating the other team with a superior deck when they get paired.

**What do we learn**?

In the end, both teams will screw each other over by picking the Sliver cards, and they will only have an expected value of one match win.

### Game Theory, Example 2

**Dealing with Uncertainty: The Bluffing Game**

**Magic** doesn't offer as many situations where you can bluff than a game of poker, but bluffing opportunities arise once in a while. Consider the following—extremely simplified—game state, where Player A is playing a game of **Magic** against Player B. The board is empty save for a 5/5 creature on Player B's side of the board, and a 3/3 creature on Player A's side of the board (both untapped). Player B has no cards in hand, and Player A has one card in hand, which he just drew this turn. It is Player A's main phase. Both players have perfect knowledge of the opposing decks, thanks to some [Extirpate](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Extirpate)s. Both players know that Player A could have drawn a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) this turn with a probability of 20%, and any other card (an irrelevant land or creature) with a probability of 80%.

![Giant Growth](https://i.ormos.uk/f6/da/f6da29c3e57b352300b61274e635699a5b573ef938146a360fc387f8e6cda112.jpg)

Now, Player A will face the choice between attacking or not attacking, and Player B will face the choice between blocking or not blocking (if Player A decides to attack). Depending on whether Player A has the [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)—which can allow Player A's 3/3 to prevail over Player B's 5/5—and on whether the players decide to attack or block, imagine that both players can compute the probability that Player A will win the game after the attack (which is, of course, equal to 1 minus the probability that player B wins the game). Finding this exact number is pretty tough, but an estimate is what you should always base your plays on, and in this case both players are brilliant geniuses with perfect knowledge of each other's decks, so they happen to both know the values of these chances.

We can represent this game situation in an extensive game tree, where the outcome numbers represent the probability that Player A wins the game after that sequence of plays. Note that Player B does not know the contents of Player A's hand, but he can tell the strategy employed by Player A (for instance, always bluff or always honest). Player A also knows the blocking strategy employed by Player B (for instance, always block or never block). You may wonder how the players know each other's strategy in this situation. Just assume, for the sake of the analysis, that Player B is aware of Player A's reputation in the community; and therefore it is not unreasonable for Player B to make fair approximation of Player A's playing style. Player B may watch Player A's games in-between rounds and observe that he has a conservative, risky, or solid playing style, giving him a good read on Player A's strategies in situations like these (and vice versa). Or perhaps they play each other every week in the local FNM tournament.

![](https://i.ormos.uk/66/ed/66ed8035b1c8a2cf44582345f3de5316b52eb969289fb8b62cd1ebe163e5c85e.jpg)

What is each player's correct strategy in order to maximize the odds of winning?

A first obvious observation is that if Player A has the [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand, then he should always attack. This is a dominant strategy, no matter whether Player B blocks or not. However, if Player A does not have the [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand, then his choice is more difficult. If, in this case, he decides to hold back, then he simply has a 50% match win percentage. But if Player A chooses to attack, then his gains will depend on player B. Player A can gain if Player B does not block (probability of 0.6 to win the game), but he stands to lose a lot if Player B does decide to block (probability of winning lowered down to 0.2). In this situation bluffing comes in.

Let's analyze a basic obvious strategy for Player A: attack if holding the [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth), never attack otherwise. Then, the optimal response strategy of Player B is to never block. If the players play along these lines, then the probability that Player A will win the game (recall that I stated before that Player A had a 20% chance of having this [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand) is (0.7 \* 0.2) + (0.5 \* 0.8) = 0.54.

But let's take this one step further. If Player B is never going to block the attack, then the optimal strategy for Player A is to always attack, regardless of whether he has [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand or not. After all, this increases his probability of winning to (0.7 \* 0.2) + (0.6 \* 0.8) = 0.62. But—and here is where it gets tricky—if Player A always attacks (and thus bluffs), then what is the optimal strategy for Player B? Looking at the above percentages in the game tree, then Player B should always block. In that case, then the probability that Player A will win the game is lowered to 0.34. Needless to say, the strategy of always attacking is not so smart if Player B is aware of this. And hey, if Player B always blocks, then Player A should employ the strategy of always attacking if he has [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth), and never attacking elsewise. In that case, the probability that Player A will win the game is 0.58.

[![Equilibrium](https://i.ormos.uk/8d/df/8ddfd5f21c52bbdbefb457c88b24bb267613ba1661c8973f0acc4903f5d3ca23.jpg)](https://web.archive.org/web/20070530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Equilibrium)Here, there are no dominant strategies or a clear equilibrium like in the previous draft game example. For each strategy there is another ideal counter-strategy. In this situation, Player A will make a choice first, and if Player B always knows the strategy employed by Player A, then Player A should only attack with a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand, and Player B will never block. As expected, this is what happens most often in real-life game situations that are analogous to the one we are analyzing. These strategies and related outcomes are not particularly bad. However, it is not the best possible one. Can you see a better strategy?

The answer lies in mixing up your plays. We now look for mixed strategies: Player A might randomly choose to sometimes bluff (i.e., attack without a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)), and sometimes be honest (i.e., don't attack without a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)). A solution concept for this situation that game theory offers is the mixed strategy where Player A mixes his plays between attacking and not attacking, such that Player B is indifferent between blocking and not blocking. It is proven that this constitutes the optimal bluffing frequency; you don't care how your opponent will respond, you will end up with the same game win percentage on average. So at the optimal bluffing frequency, there is nothing your opponent can do, and he should just guess at random.

We denote the probability that player A will choose "always attack" with **x**, and the probability that player B will choose "always block" with **y**. Then, to keep everyone indifferent, we have the following equations (using the match win percentages as calculated earlier):

0.62**x** \+ 0.42(1 – **x**) = 0.34**x** \+ 0.46(1 – **x**)  
**x**\=0.125

0.38y + 0.66(1 – y) = 0.42y + 0.46(1 – y)  
y=0.25

So, if both players are very solid rational players with perfect reads on the type of strategy that the other player uses, then the optimal strategies against which the opponent cannot defend by picking a preferred strategy are the following: Player A chooses "always attack" in 1 out of 8 cases, and "only attack with [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand" in 7 out of 8 cases. Player B should choose "block" in 1 out of 4 cases, and "don't block" in 3 out of 4 cases. It can be shown that in this situation, Player A has a 55% chance of winning (this is the maximum attainable for Player A, assuming perfect reads on the perfect strategic play by both players). Note that this is more than the 54% in the case where Player A only attacks with a combat a trick in hand and Player B never blocks.

**What do we learn?**

Mixing up your play can pay off, and you should bluff from time to time! If you encounter a situation like this and you don't have [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand, it can be worth it to randomize your plays by rolling an 8-sided die and only attack if you get a 1. Or even better, always roll a die, since otherwise your opponent will catch on to your tell that you only roll a die when you're not holding a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). Furthermore, the puzzled look on your opponent's face when you randomly roll a die in the middle of a game for no apparent reason is priceless. However, note that you have to be in the correct situation for a bluff to be right. In some cases (if the game-win percentage outcomes are distributed in a different way than the above example) bluffing is a strictly bad play. For instance, take the situation where on turn two you have a 1/1 in play (along with a potential [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in hand) and your opponent has a 2/2. Then it is conceivable that—even if you have the combat trick in hand—the chance of winning when your opponent blocks is actually smaller than the chance of winning when you don't attack (since the opponent will happily trade a [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) and a mana against his 2/2, since later in the game that [Giant Growth](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) would be way more of a wrecking). Be wary of those situations; don't bluff if it will be correct for your opponent to play right into a combat trick even if he believes you have it. This actually comes up more often than you think.

### The Metagame, 1

**One Best Deck: The [Savannah Lions](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) Game**

Now I want to move on by applying game theory to another aspect of **Magic**: deck selection and the metagame at Constructed tournaments. First, I want to introduce a problem that I posed (in slightly different form) a long time ago on the Dutch **Magic** forum. Fortunately it was still around in the archives over there. The [Savannah Lions](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) game modeis a simplified **Magic** format. You have to play a 40-card deck, and the only cards allowed are [Plains](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and [Savannah Lions](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) (you thought the Block Constructed format had a small card pool? Think again!). You start the game on 3 life with no sideboard, no mulligans, and no play skill (you should always play a land and Lions whenever you can, and you always have to attack and block whenever possible).

![Plains and Savannah Lions](https://i.ormos.uk/7f/65/7f651c8b2922f2b68f756f445b363591875297b5c8209b770d806ecc662224d7.jpg)In order to win, you have to play as many Lions as quickly as possible. Let me give an illustration of an example game, as that might make this puzzle easier to grasp:

The person playing first (Jim) has 5 lands and 6 Lions in his top 11 cards, so he goes:  
Turn one: Land, Lion  
Turn two: Land, Lion, Lion  
Turn three: Land, Lion, Lion, Lion  
Turn four: Land, –  
Turn five: Land, –

The person playing second (Bob) has 2 lands and 9 Lions in his top 12 cards, so he goes:  
Turn one: Land, Lion  
Turn two: Land, Lion, Lion  
Turn three: –, Lion, Lion  
Turn four: –, Lion, Lion  
Turn five: –, Lion, Lion

Lions would trade equally on the attack phases of Jim's turn two and three. Then on turn four, Jim swings with 3 Lions, while Bob only has two, so Bob goes down to 1 life and Jim is left with 1 Lion. However, in the subsequent turns Bob plays out Lion after Lion, whereas Jim only has lands, and Bob recovers from his "slow" start to out-Lion Jim.

Now the question is: what is the best deck?

At first, we realized that the optimal deck choice would maximize the odds of having 2 lands on turn two while simultaneously minimizing the odds of drawing extra (dead) lands afterwards. The optimal range was determined to lie around 6-12 lands. But would there be one single best deck, or would there be many viable options? The discussion was eventually solved by computer simulation programs written by the forum readers that played millions of simulated games of decks with various land counts against each other, and computed the win percentages of assorted matchups.

<table><thead><tr><td>Cell value is P(Player 1 wins)</td><td colspan="8"><b>Player 2 land</b></td></tr></thead><tbody><tr><td rowspan="8"><b>Player 1 land</b></td><td> </td><td><b>6.000</b></td><td><b>7.000</b></td><td><b>8.000</b></td><td><b>9.000</b></td><td><b>10.000</b></td><td><b>11.000</b></td><td><b>12.000</b></td></tr><tr><td><b>6.000</b></td><td>0.500</td><td>0.474</td><td>0.462</td><td>0.455</td><td>0.447</td><td>0.446</td><td>0.445</td></tr><tr><td><b>7.000</b></td><td>0.526</td><td>0.500</td><td>0.493</td><td>0.495</td><td>0.498</td><td>0.501</td><td>0.512</td></tr><tr><td><b>8.000</b></td><td>0.538</td><td><b>0.507</b></td><td><b>0.500</b></td><td><b>0.504</b></td><td><b>0.521</b></td><td>0.536</td><td>0.553</td></tr><tr><td><b>9.000</b></td><td>0.545</td><td>0.505</td><td>0.496</td><td>0.500</td><td>0.519</td><td><b>0.544</b></td><td><b>0.571</b></td></tr><tr><td><b>10.000</b></td><td>0.553</td><td>0.502</td><td>0.479</td><td>0.481</td><td>0.500</td><td>0.528</td><td>0.564</td></tr><tr><td><b>11.000</b></td><td>0.554</td><td>0.499</td><td>0.464</td><td>0.456</td><td>0.472</td><td>0.500</td><td>0.539</td></tr><tr><td><b>12.000</b></td><td><b>0.555</b></td><td>0.488</td><td>0.447</td><td>0.429</td><td>0.436</td><td>0.461</td><td>0.500</td></tr></tbody></table>

From this table, we can first conclude that 6 lands is simply not enough. You can improve in all matchups by playing a deck with 7 lands, for example. After tossing out the 6-land decks, we can also toss out the 12-land decks. These are strictly dominated by the 11-land decks (12 lands is only better against 6 lands, but since we determined that no one should ever play a 6-land deck, that is irrelevant now). Next, we can eliminate the 11-land and 10-land decks since they are strictly worse than 9-land decks in every single matchup. Then eventually we can exclude the 7-land decks and 9-land decks, as 8 lands is better in every matchup.

At last, only one option remains: 8 lands is ideal. 8 lands vs. 8 lands is even a so-called Nash equilibrium, which means that no one can improve by picking another deck. You can check this in the table. If you are Player 1 and you know that you are up against Player 2's 8-land deck, then your best deck choice is found by the highest value in the column of Player 2's 8 lands. Evidently, your best bet is to play 8 lands as well, providing a 50-50 matchup and a boring metagame.

**What do we learn?**

This example is interesting because it illustrates an extreme metagame: there is only one best deck, and if you do not play it then you are only hurting yourself. A [Savannah Lions](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) format tournament would therefore result in a room of players that all have the identical decklist of 8 lands and 32 Lions. No one can perk up with another deck choice. Or, most probably, if such a tournament was held, then no one would show up, and people would play a **Magic** format where there actually is some deck variety instead.

### The Metagame, 2

**A Mixed Equilibrium: The Rock-Paper-Scissors Game**

I will now consider a simplified form of the Standard metagame. Imagine that you go to a Standard tournament, and every competitor is an ultimate netdecker: everyone plays a fixed decklist of either Dralnu, Dragonstorm, or Gruul. No other decks or variations exist, because everyone takes a tried and tuned decklist from the Internet, as they don't have the time or skills to tweak or innovate a deck themselves. So, this will be a pure three-deck Standard format. Any deck has strengths and weaknesses. Dralnu beats Dragonstorm, which beats Gruul, which beats Dralnu in turn. For the sake of discussion, let the match win percentages in a certain matchup be known. Don't pin me down on the values I will show, although they are fair representations of the true matchup. I chose not to take symmetrical matchup values, in order to create a more interesting case than pure rock-paper-scissors.

<table><tbody><tr><td>Match win %</td><td>Dralnu</td><td>Dragonstorm</td><td>Gruul</td></tr><tr><td>Dralnu</td><td>50,50</td><td>80,20</td><td>45,55</td></tr><tr><td>Dragonstorm</td><td>20,80</td><td>50,50</td><td>60,40</td></tr><tr><td>Gruul</td><td>55,45</td><td>40,60</td><td>50,50</td></tr></tbody></table>

As an example on how to read this table, Dragonstorm only wins 20% of the time when paired against Dralnu. All players in this tournament are equally skilled, and draws are not allowed. What deck would you pick?

The answer to that question depends on the metagame: the distribution of decks that you expect to face. Now let's assume that there are enough players so your deck choice won't influence the deck choice of others. Let's also assume that everyone knows what the metagame will consist of, because everyone is constantly scouting to see what cards people are sleeving up. Furthermore, assume that the dealers have a special promotion today where everyone can trade any of these three decks for any of the other two, so there are no switching costs.

Right now it is one hour before the tournament starts. Imagine that as everyone arrives, every deck is now accounting for 1/3 of the metagame. However, since you know the matchup percentages, you can calculate what the best deck is for this metagame. If you play Dralnu then you have an expected match win percentage of (50 \* 1/3) + (80 \* 1/3) + (45 \* 1/3) = 58.33. If you play Dragonstorm then you have an expected 43.33% match win. If you play Gruul then you have an expected 48.33% match win. Obviously, picking Dralnu is best. This is the first step in metagaming.

[![Scissors_Lizard](https://i.ormos.uk/3a/8c/3a8c8f668e2756ac8690f95661aec42997067ca47be2324442d47d00de8fc1aa.jpg)](https://web.archive.org/web/20070530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Scissors%2BLizard)But wait up—other players are smart as well, and the matchup percentage table and the knowledge that Dralnu is the best deck is disseminating pretty fast. Now everyone is dashing around the room to find [Watery Grave](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Watery+Grave)s. Ten minutes later, you see that 80% of the players have Dralnu cards in front of them, opposed by 10% Dragonstorm and 10% Gruul. Now, in this metagame, Dralnu has 52.5% chance of winning, Dragonstorm has an ugly 27%, and Gruul suddenly nets a 53% chance of winning. Out of the blue, Gruul has become the top deck.

Another ten minutes later, everyone has traded away their [Watery Grave](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Watery+Grave)s for [Scab-Clan Mauler](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scab-Clan+Mauler)s (the dealers are getting headaches already), and surprisingly, 80% of the players plan to play Gruul, 15% still have Dralnu, and just 5% have Dragonstorm. Now, in this metagame, Dralnu has a 47.5% chance of winning, Dragonstorm has a nice 53.5%, and Gruul just nets a 50.25% chance of winning. Suddenly Dragonstorm has become the top deck.

You can understand where this is going. Everyone will pick up Dragonstorm, and then Dralnu becomes the best choice again. This process can go on indefinitely, with players constantly trying to get an edge on the current metagame. In the quest to chalk up as many wins as possible, many players will switch to the deck that they believe to hold an advantage in a particular metagame. Hence, there is no single best deck. What may be a sure winner in one week could be a big failure in the next week. This explains the up-and-down changes and yo-yo effects often seen in my metagame discussions.

Now imagine that a game theorist walks into the flurry of deck swapping at this tournament site, right before the tournament starts. He employs the minimax algorithm, which aims for indifference between strategies just like in the bluffing example. The proposed solution is to choose a deck randomly: Dralnu with 2/9 chance, Gruul with 6/9 chance, and Dragonstorm with 1/9 chance. Everyone employs the same strategy, so the eventual expected metagame will be 22.22% Dralnu, 66.66% Gruul, and 11.11% Dragonstorm. The interesting part of this result is that every deck now has a 50-50 win against the field (this can be checked against the matchup table if you want). You cannot improve; if you know that the metagame will be as just described then your own deck choice doesn't matter. No one will be able to get an edge anymore, and the tournament starts peacefully.

**What do we learn?**

This example illustrates what a metagame in a stable equilibrium would look like if everyone used game theoretical considerations. Interestingly, Dralnu would seem like the best deck at first (a big advantage of 80% over Dragonstorm, and a slightly unfavorable matchup of 45% against Gruul, seems good) but in the metagame equilibrium, it only has 22.22%, and Gruul is the most popular deck.

### The Metagame, 3

**Complexity and Bounded Rationality: The Real World**

There are obvious problems with the analysis done in the above example. First, people are not rational. They will not employ these considerations to find a best deck. People tend to play a deck they like and are familiar with, since that experience gives them an edge over the other options. It is correct to pick whatever deck best suits your style and playtest it a lot. Furthermore, people have limited budgets and cannot switch decks at will. Some people just collect one deck and keep running it for years, even if the metagame is not right for it. Moreover, often the exact matchup percentages are not known, so people do not have perfect information to make a choice.

So you cannot correctly predict the metagame in a real tournament with game theory; you are better served with your own instincts and knowledge of local players. I often (implicitly) employ the following method when trying to select a deck. For each deck, I determine the overall win probability as follows. I estimate *my* chance of beating a certain opposing deck (not the chance of an average player, since I want to incorporate my own playing style preferences) multiplied by the chance of facing that opposing deck, and then summing up all these values for each possible opposing deck. I then pick the deck that has the highest probability of winning, given an estimation of the metagame.

Furthermore, **Magic** formats are way more complex than just three decks. You have to account for more. **Magic** is intriguing in that there are infinite possible deck configurations. You could not get an edge by picking a certain deck in the previous example in the 2/9 Dralnu + 6/9 Gruul + 1/9 Dragonstorm metagame. But in reality you can simply make a new deck that has more than a 50% chance of winning in this field.

**What do we learn?**

In the current Standard you have so many deck options and players who stick with their own pet decks that it becomes way too complex to analyze. Hopefully my weekly articles can still give you some idea of what to expect.

### **Concluding thoughts**

![Fugitive Wizard, Glory Seeker, and Nessian Courser](https://i.ormos.uk/dd/22/dd22e577a3fe2cea8274e4faccff2881d3079632995f7053a76dc20569c398cb.jpg)Metagames can even exist in Draft. Roel van Heeswijk once posed (as an explanation for why he always won practice drafts for Pro Tour–Prague but didn't make Day 2 in the Pro Tour) that a draft deck that is *slightly* slower and slightly more control-minded than the opposing deck has an edge. But a draft deck that is *much* slower will lose to a more beatdown-oriented deck. An illustrative example would be an imaginary format—somewhat similar to the Lions / [Plains](https://web.archive.org/web/20070530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) format—where everyone has to play 20 lands and 20 creatures, and the creatures can be either 20 1/1s for one mana, or 20 2/2s for two mana, or 20 3/3s for three mana, and so on. It seems that a deck with X/X creatures will lose to a deck with X+1/X+1 creatures. But a deck full of 1/1s should beat a deck full of 6/6s on speed, so there is a turning point. I hereby lay out a challenge for you to analyze this format in case you like a time-consuming puzzle.

What I have offered today is just a brief introduction of some of the concepts of game theory as applied to **Magic**. I haven't even touched on multiplayer games or many other game theory–related subjects, so I hope that this theme will return at some point.