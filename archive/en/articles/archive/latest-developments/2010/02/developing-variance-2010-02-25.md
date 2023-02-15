
---
[Link to Wayback Machine](https://web.archive.org/web/20201111214144/https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Worldwake contains five common creatures with multikicker.This is Multikicker Week, and today I will tell you the story of these five cards. However, like any good development story, it is not short, involves lots of playtesting and spirited debate, and requires a little background. If you're ready, let's hop in the time machine and go back to the middle of Zendikar development ...."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "189616"
[_metadata_:path_date]:- "2010-02-25"
[_metadata_:publish_date]:- "2010-02-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing for Variance"
[_metadata_:wayback_capture_timestamp]:- "2020-11-11 21:41:44"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201111214144id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25"
---


Developing for Variance
=======================



 Posted in **Latest Developments**
 on February 26, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






W*orldwake* contains five common creatures with multikicker.

  
![](https://web.archive.org/web/20130607120246im_/http://wizards.com/mtg/images/daily/ld/ld79_5Cards1.jpg)  
This is Multikicker Week, and today I will tell you the story of these five cards. However, like any good development story, it is not short, involves lots of playtesting and spirited debate, and requires a little background. If you're ready, let's hop in the time machine and go back to the middle of *Zendikar* development ....

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld79_time.jpg) While we were working on *Zendikar*, **Magic** developers discovered two quirks about the *Zendikar* Limited format. The first, and this is an observation that many players have made since the set released, is that it is extremely fast. The set is full of creatures with landfall triggered abilities. Unless you're doing something special, you can only put a land onto the battlefield on your own turn, so all these creatures are stronger on attack than on defense. The set is also full of Allies, and just like lands, in most situations you are playing Allies on your own turn. Once again, Allies encourage you to attack, not defend, as so many of their triggers are only active on your turn.

As we got used to how many of *Zendikar*'s creatures were stronger on the attack than on defense, we adjusted our drafting to match. Our decks kept getting more and more aggressive. We eschewed six-mana fatties for two-mana 2/1s, and after discovering how strong two-mana creatures were in this world, we started picking them higher and higher. We were self-aware about this, of course, and often wondered to ourselves whether this was a good thing or not. Eventually, however, we decided to embrace it. The Limited format immediately preceding *Zendikar* was ***Magic** 2010*, which was on the slower end of the range of speeds we like Limited formats to be. We know that change is what keeps **Magic** fresh. The change of speed from ***Magic** 2010* to *Zendikar* was jarring, but it would certainly keep you on your toes.

Although a Limited format being fast isn't automatically a problem, we discovered a second quirk of *Zendikar* Limited that we did consider to be problematic. That quirk was that it was very difficult to come back from behind. Often, a Limited game progresses to a point where neither player has cards in hand, and both are playing off the top of their libraries. Usually, when this happens one player is in a worse position than the other. In other Limited formats, one of the most important ways such a player could come back was for the other player to draw a string of "blanks," or cards that didn't do anything in the situation. If the opponent draws blanks for a few turns while you draw "live" cards, or cards that do relevant things, you'll be back in the game in no time.

Although a few nonland cards can be blanks, like [Runeclaw Bear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runeclaw+Bear) on a board full of huge creatures, the largest category of midgame blanks in most formats is lands. *Zendikar*, however, is not most formats. It's not uncommon in a midgame stall to want to draw a land in exactly those situations where in any other format you'd be hoping for a spell. Perhaps a land would let you pump your [Baloth Woodcrasher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baloth+Woodcrasher), use your [Turntimber Basilisk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turntimber+Basilisk) to take out your opponent's second-best creature, and use your [Roil Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Roil+Elemental) to steal the best one. Most situations aren't this dramatic, but merely giving a [Hagra Crocodile](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hagra+Crocodile) +2/+2 can be the difference between doing nothing and making a strong attack. Of course, the alternative to drawing a land is drawing a spell, which is also a fine thing to draw on a stalled board—such a strong alternative, in fact, that it's exactly what you hope for in any other Limited format!

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld79_landfall.jpg)  
We've just established that in *Zendikar*, both spells and lands are live draws in midgame stalls. You will note, of course, that every card in your deck is either a spell or a land, so nearly any card drawn in the midgame contributes to a player's board position. How delicious, then, to be the player who is ahead on board. When there are few blanks to draw in either library, the variance in power of draws is very low, and that's exactly what the player who is ahead on board wants. If the game continues in the way it has gone so far, that player will win, and because of the lowered variance that the landfall mechanic provides, a player who pulls ahead is much more likely to stay in the lead.

Because of this, the development team was a little unhappy with the variance-reducing effect landfall had on *Zendikar* Limited games. Just like you, we want **Magic** to be a game of skill, but there is already plenty of skill in **Magic** already. (If you don't believe this, try playing against a player who is much, much weaker or much, much stronger than the players you normally play against. The difference in your win rate should be jarring.) We love dramatic come-from-behind victories, and we value that **Magic** allows them to happen. Mechanics that reduce variance in game play risk keeping them from happening often enough.

![](https://web.archive.org/web/20130607101353im_/http://wizards.com/mtg/images/daily/ld/ld79_wwkBreak.jpg)  
We had these two quirks in mind when we started working on *Worldwake*. As I said before, we saw *Zendikar*'s speed not as a problem, but as a natural part of the evolution of **Magic** over time. However, going by the same logic that led us to believe *Zendikar* could be that fast, *Worldwake* had to change the speed some. Because *Zendikar* was near the fastest we are willing to make a format, the natural thing to do with *Worldwake* was to pull the speed back a little bit. Because drafts use two packs of *Zendikar* and one pack of *Worldwake*, we couldn't change the speed too much, but we wanted to slow it down a little bit.

Because we were less happy with the other quirk, we decided to try to change it. This being the second set in the *Zendikar* block, we didn't have the option of rejecting landfall and Allies as mechanics. However, we could choose to be more careful about how we used them in order to build more comeback potential into Limited games, and that's exactly what we did.



|  |  |
| --- | --- |
|  |  |

These conclusions affected everything we did in *Worldwake* development. One place you can see the results of these decisions is in the common landfall creatures that *Worldwake* has to offer. While five commons in *Zendikar* have landfall triggers that give them +2/+2, only [Hedron Rover](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hedron+Rover) in *Worldwake* receives that bonus on landfall. [Calcite Snapper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Calcite+Snapper) is the only other creature in *Worldwake* whose power and toughness change upon landfall; I don't think anyone would call that card a poor blocker, as a 1/4 with shroud is no jokes. The other landfall creatures gain things like vigilance and flying, which encourage you to attack but give you plenty of power and toughness to use on defense.

I don't have time to talk about all of the ways we addressed this, but I wanted to give you a glimpse of how those goals changed our thinking. This is, however, an article about the five common multikicker creatures, so let's move on to them.

Mark Rosewater invented multikicker during *Zendikar* design, but it was decided that it would be put off to *Worldwake*. As we got closer to the beginning of *Worldwake*'s development, we had those two quirks of *Zendikar* Limited in mind. Once again, we liked multikicker as a mechanic, but we made the unhappy discovery that it also reduced the variance in draws. 

![](https://web.archive.org/web/20130607101221im_/http://wizards.com/mtg/images/daily/ld/ld79_packTwice.jpg)  
Take [Gnarlid Pack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gnarlid+Pack), for example. Because of how fast *Zendikar* Limited is even after *Worldwake*, we thought it was usually correct to just play it on turn two as a 2/2 if it was our only two-mana creature. However, if it were a [Runeclaw Bear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runeclaw+Bear), we might end up drawing it on turn twelve when a 2/2 creature wasn't a big deal. Thanks to multikicker, [Gnarlid Pack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gnarlid+Pack) doesn't have that problem. If you draw it on turn twelve, you can just play it as a 5/5 or 6/6. No matter when in the game you draw it, it's quite good for you. This reduces variance in exactly the way that landfall does. With fewer ways for cards to come up in the wrong order, it's hard for someone to come back from a poor position.

Except for [Enclave Elite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enclave+Elite), each of the common multikicker creatures left design exactly as they are, with only one difference: the multikicker cost was ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif). Fellow developer Erik Lauer was the first to point out how potentially dangerous their variance-reducing qualities were, and when I realized how strong they were, I started agitating for change. I liked [Skitter of Lizards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skitter+of+Lizards) and [Quag Vampires](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quag+Vampires) as they were, but [Apex Hawks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Apex+Hawks) and [Gnarlid Pack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gnarlid+Pack) grated on me; they were both cards that were rather strong in the *Zendikar* / *Worldwake* format before any abilities were added to them, and the multikicker ability just put them way over the top.

I talked so much about this that *Worldwake* lead designer Ken Nagle, in his infinite griefing powers, chose to make each of their playtest names friendly pokes at me. We have physical copies of two of them:

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld79_playtest.jpg)  
The other three were Tom Foolery, Ginger Folk, and White Board Menace, the last a reference to the whiteboard I joke about having used to order my job at Wizards from the universe—a great story that could perhaps be an article one day.

My annoyance at these creatures never really went away. Although my fellow developers agreed with my statements about them, they weren't sure what to do about it, and *Worldwake* lead developer Mike Turian was wary of my proposals because many of them would have made that cycle much less appealing as a whole. I eventually chose to fight for making the green one start at ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) 3/3. Mark Rosewater, however, hated that idea; he thought players would feel better about casting a ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) 3/3 if they had gotten to pay the multikicker cost, which is clearly what you were supposed to do with the card in the first place. 

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld79_1c.jpg)  
The story has a happy ending, however, as Mike offhandedly suggested during one meeting that we change the multikicker cost on these cards from ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif) to "1C"—Ramp;D slang for one generic mana and one colored mana of the appropriate color. As soon as he suggested it, I knew we had found what we were looking for. The cards would read almost as excitingly, but they would be less consistently powerful in the late game because you might have drawn the wrong mix of lands to kick them with all of your mana. It was clear after one playtest that this change returned a significant amount of comeback potential to *Zendikar*-*Worldwake* Limited, and we settled on 1C for the multikicker costs of those creatures.

**Magic** development is a complex puzzle. To do it well, we have to take in and weigh lots of information, including playtest data, past experiences, and opinions from non-developers. Every card has a story, and the story of these five cards should show you just how detailed those stories can be. We put tons of effort into each **Magic** card, though, and we have a blast while we make them. We hope you're having fun with them too!

**Last Week's Poll** 



|  |
| --- |
|  **What is your favorite *Worldwake* mythic rare card?**  |
| Jace, the Mind Sculptor | 2388 | 28.9% |
| Abyssal Persecutor | 1378 | 16.7% |
| Dragonmaster Outcast | 854 | 10.3% |
| Omnath, Locus of Mana | 846 | 10.2% |
| Admonition Angel | 569 | 6.9% |
| Wrexial, the Risen Deep | 551 | 6.7% |
| Novablast Wurm | 521 | 6.3% |
| Eye of Ugin | 482 | 5.8% |
| Comet Storm | 350 | 4.2% |
| Avenger of Zendikar | 319 | 3.9% |
| **Total** | **8258** | **100.0%** |

  
My answer to this poll is [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor). While fiddling around with the top of one's library is not what every **Magic** player loves, there is a subset of players that adores cards like [Sage Owl](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) and [Sensei's Divining Top](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei%27s+Divining+Top). I am one of those players, and I love using Jace to sculpt games over many turns.

**This Week's Poll**



|  |
| --- |
| **What do you think of Standard with *Worldwake*?**It's awesome!It's good.It's okay.It's bad.It's terrible!I haven't played Standard since *Worldwake* released. |

[![](https://media.wizards.com/legacy//mtg/images/daily/ads/wwk_game_article-banner-620-wide-template.jpg)](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/gameday-facts%20)  






