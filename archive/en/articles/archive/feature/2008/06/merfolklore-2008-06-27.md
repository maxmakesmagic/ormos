
---
[Link to Wayback Machine](https://web.archive.org/web/20160706154343/http://magic.wizards.com/en/articles/archive/feature/merfolklore-2008-06-27)

[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/merfolklore-2008-06-27"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160706154343id_/http://magic.wizards.com/en/articles/archive/feature/merfolklore-2008-06-27"
[_metadata_:wayback_capture_timestamp]:- "2016-07-06 15:43:43+00:00"
[_metadata_:publish_date]:- "2008-06-27"
[_metadata_:description]:- "*/ Last week, I zoomed in on the detailed development of a single card. This week, I’m going to run through the development stories of five different cards. In honor of Merfolk Week, I’ll swim on down to my undersea friends."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


MerFolklore
===========



 Posted in **Feature**
 on June 27, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low











Last week, I zoomed in on [the detailed development](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl42) of a single card. This week, I’m going to run through the development stories of five different cards. In honor of Merfolk Week, I’ll swim on down to my undersea friends.


### Puresight Merrow


This white-blue Merfolk is a gift from the creative team, for which the developers are very grateful. Because Merfolk were white-blue in *Lorwyn* / *Morningtide* and Goblins were black-red, the developers were eager to have at least one hybrid Merfolk and one hybrid Goblin in *Shadowmoor* that fit those colors, even in the context of the overall *Shadowmoor* color scheme, in which Merfolk are blue-black and Goblins red-green.


The creative team thought carefully and came up with stories for one particularly evil [Murderous Redcap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) and one particularly untainted [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow). Designers put together a white-blue Merfolk that combined powerfully with the white [Judge of Currents](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Judge+of+Currents) and the blue [Drowner of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowner+of+Secrets). And [Murderous Redcap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) allowed *Shadowmoor* to add more cards for the mono-black and black-red Goblin decks many players put together. Thanks, creative team—we owe you another one.


The original [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow) was just slightly different. Can you spot the relevance of the change?




> 
> UW03\_JEL  
> 
> [Hoary Lanelord]  
> 
> (w/u)(w/u)  
> 
> Creature - Merfolk Wizard  
> 
> 2/2  
> 
> (w/u), Q: Look at the top card of your library. You may put it on the bottom of your library.
> 



![Puresight Merrow](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Puresight%20Merrow&options=) It didn’t take long for *Magic* developer Mons Johnson to break this card in half. He enchanted it with [Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow), tapped it for U, then untapped it to put the top card of his library on the bottom, tapped it for U, then untapped it to put the top card of his library on the bottom, allowing him to cycle through his entire deck and find a [Judge of Currents](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Judge+of+Currents). This allowed him to tap his Hoary Lanelord a billion times to gain a billion life in a turn. He also played other UNTAP creatures like the old version of [Knacksaw Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knacksaw+Clique) that cost U, UNTAP to activate. With [Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow) on the old [Knacksaw Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knacksaw+Clique), Mons could mill his opponent’s entire deck in one turn, and often did.


A two-card Standard combo that kills in one turn or sets up gaining a billion life almost always spurs us to make some changes, and did in this case. Furthermore, this combo "forced" you to keep filtering your deck until you had the perfect card on top and the most perfect run of cards following it.


Although these combos were abusive, if you look at them another way, they are pretty awesome! They needed some changes, but we didn't want to cut tem down to nothing. So we used a light hand, keeping just one mana to activate on [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow), but changing it to remove the unwanted cards from the game instead of putting them on the bottom of your library. [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow) / [Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow) / [Judge of Currents](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Judge+of+Currents) can still provide a quick 30 billion life—it just doesn't let you set up your library quite as perfectly.. And [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow) / [Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow) / [Drowner of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowner+of+Secrets) still gives you X: Mill your opponent for X. [Knacksaw Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knacksaw+Clique) / [Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow) can still mill your opponent out in one turn—you just need [Mana Reflection](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Reflection) in the mix as well.



### Inkfathom Witch


![Inkfathom Witch](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Inkfathom%20Witch&options=) Due to their shared ability to quickly pump a swarm of weenies to lethal levels, I often refer to this Merfolk Wizard as “the blue-black [Mirror Entity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror+Entity).” It’s the evasion that’s so common on so many blue and black creatures, including [Inkfathom Witch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkfathom+Witch) himself, that make this guy play a little differently. In a deck with twenty blue and black evasive one-drops, including [Prickly Boggart](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prickly+Boggart), [Nightshade Stinger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightshade+Stinger), [Cloud Sprite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Sprite), and [Flying Men](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flying+Men), [Inkfathom Witch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkfathom+Witch) can inflict a turn-four kill with 24 damage.


Here’s the plan:


Turn 1: Evasion one-drop.  

Turn 2: Two evasion one-drops, attack for 1.  

Turn 3: [Inkfathom Witch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkfathom+Witch), evasion one-drop, attack for 3. 4 damage dealt total.  

Turn 4: Attack with five evasion creatures, activate [Inkfathom Witch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkfathom+Witch), deal another 20 damage. Win.


### Hollowsage


There’s a long history of discard effects in *Magic* being sorceries or being playable only as sorceries. There’s good reason: If your opponents could play all the discard effects as instants, they could make you discard all your cards before you ever got to play them. If that happens to people with great consistency, it’s not fun at all.


![Hollowsage](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Hollowsage&options=) We sometimes intentionally break this guideline and allow discard effects to go off at instant speed, partially because it has the allure of forbidden fruit, and the promise of possibly discarding someone’s cards before they can play them. Recent cards that broke this guideline include [Haunting Hymn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Hymn), [Funeral Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Funeral+Charm), and [Piracy Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Piracy+Charm).


But all of those are one-and-done effects. It’s very infrequent that we let people have an opportunity to “draw-step lock” their opponents by recurrently forcing their opponents to discard freshly drawn cards during the opponent’s draw steps, before those cards can be played. But with [Hollowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollowsage), we decided to open the door to exactly that.


[Stonybrook Angler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonybrook+Angler) + [Hollowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollowsage) is just one of the many possible [Hollowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollowsage) combos that allow you to draw-step lock your opponent. We kept an eye on this, but we liked the mirror of [Hollowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollowsage) to *Lorwyn*‘s [Fallowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fallowsage), and our dark sides liked the deliciousness of the prospect of draw-step locking your opponent enough that we decided that this draw-step lock would not go off so consistently as to be excessively annoying. And creature removal instants could still break up the combo.


Like many things in *Magic*, when you see a [Hollowsage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollowsage) draw-step lock happen once or twice, it’s really cool. It’s when it happens for the fortieth time that it gets really, really annoying.


### Deepchannel Mentor


*Lorwyn*, *Morningtide*, and *Shadowmoor* have a *lot* of race and color “lords” between them, and we tested a ton of different designs for them. (When I say “lord,” I mean creatures that pump up all the creatures of a certain type or color, like [Lord of Atlantis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis) or [Goblin King](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King), even though we no longer give such creatures the now-defunct Lord creature type.) During our testing of all these lord designs, one thing in particular stood out. A classic design for lords is for them to grant +1/+1 and a keyword to all their followers. But having too many lords granting evasion as that keyword doesn’t play very well.


![Deepchannel Mentor](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Deepchannel%20Mentor&options=) Coming into *Lorwyn*, we already had a certain number of lords that gave evasion in Standard, including [Lord of Atlantis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis), [Elvish Champion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Champion), and [Goblin King](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King). On top of this, at one point [Mad Auntie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mad+Auntie) gave your other Goblins +1/+1 and fear, and [Wizened Cenn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wizened+Cenn) cost 2W and gave your other Kithkin +1/+1 and “Can’t be blocked by creatures with power 3 or greater.”


There’s a moment of excitement when the Kithkin swarm, Goblin swarm, Elf swarm, or Merfolk swarm has been fiercely pressing the attack in the early turns and getting in lots of early damage, and then the opponent suddenly drops a huge [Chameleon Colossus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chameleon+Colossus) or a [Spectral Force](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Force). Do the weenies have a way to kill the fatty and keep attacking? If not, should the weenies keep attacking, and lose some guys in order to deal more damage? Both players become very invested in how this situation is going to play out.


But when almost all the creature lords gave evasion, this moment lost a lot of its excitement. The weenie player would have the old evasion-granting [Wizened Cenn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wizened+Cenn) or the old evasion-granting [Mad Auntie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mad+Auntie) or [Elvish Champion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Champion) on the board, and the opponent would be holding a 4/4 thinking “I could play this now....but it wouldn’t be able to block any of the non-lords, so I’d just block nothing and take 6 damage...I guess my fatties just can’t affect the swarm.” There was no mystery of “Does she have a removal spell or not? Is she going to keep attacking or not?” The evasion lord was right there on the board making it very clear that the fatty could not block.


Since we already have so many evasion lords, and [Merrow Reejerey](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merrow+Reejerey) was also great at tapping would-be blockers, we changed [Wizened Cenn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wizened+Cenn) and [Mad Auntie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mad+Auntie) to their modern forms, and kept a close eye on how many other lords would grant evasion. Those lessons were still on our minds when developing *Shadowmoor*‘s Mentors, and [Deepchannel Mentor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deepchannel+Mentor) is the only one that grants true evasion. At 5U the [Deepchannel Mentor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deepchannel+Mentor) can be lethal when he shows up, but he takes a little more time to do so.


### Cursecatcher


This Merfolk’s origin is an unusual one. One day, before a *Shadowmoor* development meeting, I said to *Shadowmoor* lead developer Aaron Forsythe:



> “Aaron, let’s make a one-mana 1/1 Merfolk that sacs to [Force Spike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike).”


Aaron’s response is still remembered by the [Merfolk Seer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Seer)s:




> “Sounds powerful. Okay.”


![Cursecatcher](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Cursecatcher&options=) The real story goes back to *Lorwyn* block planning. Block planning is like a boxing match or a pop song or a movie: You gotta pace yourself. If you exhaust everything you have up front, you don’t have anything left for the middle and end. So in *Lorwyn* block planning, we designed an arc for each of the *Lorwyn* tribes planning how their power level would evolve over time. If we pushed every tribe to absolutely as high a power level as it could go with just the *Lorwyn* set, we wouldn’t be able to safely add any power to those tribes for the rest of the year. And it’s more fun to have decks keep getting more powerful as the block evolves than to have every deck just sit at the same place.


So we primed some tribes to come out strong right out of the gates in the *Lorwyn* set, while others emerged at medium-strength in *Lorwyn*, allowing them room to accelerate and grow throughout *Morningtide*, *Shadowmoor*, and *Eventide* with particular cards. Likewise, the *Morningtide* class tribes emerged in *Morningtide* at particular power levels, with more Shamans, Warriors, and so on emerging in *Shadowmoor* and *Eventide*.


Merfolk was one tribe where we intentionally left room for the tribe to grow in power throughout the block. One of the big ways we did this was intentionally holding back on Merfolk one-drops in *Time Spiral* and the *Lorwyn* set. Merfolk still had some serious power in *Time Spiral* and *Lorwyn* between [Silvergill Adept](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silvergill+Adept), [Merrow Reejerey](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merrow+Reejerey), [Lord of Atlantis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis) and other fishy friends. And [Tideshaper Mystic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tideshaper+Mystic) was a one-cost Merfolk that could enable its friends’ islandwalking ways. But the lack of more powerful one-drop Merfolk in *Time Spiral* and *Lorwyn* left a gap that we knew we could fill in later sets to make Merfolk increasingly powerful.




|  |  |
| --- | --- |
| 
Mothdust Changeling
 | 
Stonybrook Banneret
 |

*Morningtide*‘s [Mothdust Changeling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mothdust+Changeling) provided an upgrade over [Tideshaper Mystic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tideshaper+Mystic) while *Morningtide* also added [Stonybrook Banneret](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonybrook+Banneret) and [Sage’s Dousing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage%E2%80%99s+Dousing) to the Merfolk beatdown arsenal, as well as options for “Tappy Merfolk” decks based around [Judge of Currents](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Judge+of+Currents) and [Drowner of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowner+of+Secrets) including [Mothdust Changeling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mothdust+Changeling), [Stonybrook Banneret](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonybrook+Banneret), [Sage’s Dousing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage%E2%80%99s+Dousing), and perhaps [Sage of Fables](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) or [Stonybrook Schoolmaster](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonybrook+Schoolmaster).


*Shadowmoor* adds [Cursecatcher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursecatcher) as a very powerful Merfolk one-drop for both kinds of decks, as well as [Puresight Merrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow) and perhaps [Drowner Initiate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowner+Initiate) for “Tappy Merfolk” decks, plus as a variety of other Merfolk options. Merfolk power level has largely followed the arc we expected, performing well during *Lorwyn*, even better during *Morningtide*, then winning their way into the Top 8 of Standard [Pro Tour–Hollywood](http://archive.wizards.com/Magic/Magazine/Events.aspx?x=mtgevent/pthol08/welcome) with *Shadowmoor* and [Cursecatcher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursecatcher) in the mix. Holding back a little bit on Merfolk in just the *Lorwyn* set has turned out, in my eyes, as a success.


Certainly it is almost impossible for a handful of *Magic* developers to predict the exact evolution of real-world metagames among an entire planet of *Magic* players playing hundreds of millions of games of *Magic*. But that doesn’t stop us from trying.


The public often surprises us with what they find and with cards that are more powerful than we had thought. And it’s exciting that we can’t predict exactly what the public will end up playing and discovering. Just as the Prerelease is a fun day of discovery for many players, watching a Regional Championships, Nationals, Grand Prix, or Pro Tour becomes a fun day of discovery for *Magic* developers to see what the public has uncovered next.


The most exciting part of our *Lorwyn* / *Shadowmoor* block planning adding bursts of power to race and class decks as different sets come out is that it continues through *Eventide*. Some of *Lorwyn*‘s races and classes have very specific bursts of power in *Eventide* that I’m really excited to see enter Standard and Block Constructed.


### Last Week’s Poll




|  |
| --- |
| **What is your favorite Constructed format to play?** |
| Standard | 3629 | 31.0% |
| Vintage | 3105 | 26.6% |
| Legacy | 1613 | 13.8% |
| Extended | 1415 | 12.1% |
| Block Constructed | 1205 | 10.3% |
| Something else | 724 | 6.2% |
| **Total** | **11691** | **100.0%** |

It’s no surprise that Standard is the winner, though it’s not a landslide. It’s interesting that the word “Vintage” here includes both hardcore “[Mana Crypt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Crypt) / [Black Lotus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus) / [Yawgmoth’s Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%E2%80%99s+Will)” Vintage tournament decks and casual Squirrel decks that want to play [Sol Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sol+Ring) and [Demonic Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor) just so they can get more [Deranged Hermit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deranged+Hermit)s and [Squirrel Wrangler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squirrel+Wrangler)s into play. It definitely makes me curious what proportion of the voters who picked “Vintage” are in each of those two categories







