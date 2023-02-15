
---
[Link to Wayback Machine](https://web.archive.org/web/20210429125517/https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03)

[_metadata_:author]:- "Bill Stark"
[_metadata_:description]:- "As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on Magic development. Enjoy! –Kelly Digges, magicthegathering.com editor Autumn. There is perhaps no season that so accurately evokes a feeling of change. The weather is turning, the leaves are falling. The political world is in upheaval, and"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646926"
[_metadata_:publish_date]:- "2008-10-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Shards of Alara"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 12:55:17"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429125517id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03"
---


Developing *Shards of Alara*
============================



 Posted in **Latest Developments**
 on October 3, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_BillStark.jpg)
By Bill Stark












*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on Magic development. Enjoy!  

–Kelly Digges, **magicthegathering.com** editor*


[![Edge_of_Autumn](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/FUT/Edge_of_Autumn.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Edge%2Bof%2BAutumn)
Autumn. There is perhaps no season that so accurately evokes a feeling of change. The weather is turning, the leaves are falling. The political world is in upheaval, and professional sports rotate from baseball to football. And of course, most importantly, there's a brand new **Magic** set!


Today we're going to take a look at some of the stories that came from Development during the process of testing, tweaking, and finishing the set *Shards of Alara*. Before we get to that, however, it's important to re-examine the differences between the design and development teams and the roles they play in creating a **Magic** set. How are they separate?


Consider this scenario: your boss has told you she needs you to brainstorm up some ideas for Project Y. You sit down with pen and paper, uninhibited. No restrictions, no rules, no nothing—just coming up with as many ideas as you possibly can. If some of them aren't perfect? No worries, that will get worked out later. Your responsibility is simply coming up with the starting points for everything. Ideas, ideas, ideas.


Got that mental picture in your head? Great. That's (approximately) design.


Now it's time for the second scenario. It's a week later. The bevy of ideas you came up with have had a chance to brew, and it's time to re-examine them. Project Y now has some parameters. The product has to be a certain size, say, or evoke a specific feel. It has to fit the rules and regulations of the market it's being sold in. It's up to you to re-work the ideas you came up with while completely uninhibited into a final product. Some ideas will be thrown out; some new ones will be added. Some of the brainstorms will be edited to increase their potential; some will be edited to decrease it. Now you're entering the world of **Magic** Development.


We don't just make the game you love; we make the game you love better. How do we do that? So glad you asked...


### Salvage Titan



![Salvage Titan](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Salvage+Titan)

No doubt fans of artifacts have been immediately drawn to [Salvage Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Salvage+Titan), particularly as it applies to Extended versions of Affinity. It's certainly an exciting and powerful card, and it made it through development receiving simultaneous powering up *and* down. Here's where we started:



> 
> Salvage Titan 4BB  
> 
> Artifact Creature  
> 
> Trample.  
> 
> You may sacrifice three artifacts instead of paying Salvage Titan's casting cost.  
> 
> Remove three artifacts in your graveyard from the game: Return Salvage Titan from your graveyard to play.  
> 
> 6/3
> 


Pretty over the top, huh? Not only did the Titan start out with trample, but its return-from-graveyard ability actually put the card straight into play. No need to come up with ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) or three more artifacts to be sacrificed; just a 6/3 coming at 'ya. Oof.


It didn't take long for the developers to wrangle the Titan into decks that merited changing the card's stats. Putting the 6/3 back into play from the graveyard was very powerful, and it hurt the flavor of the card. By making [Salvage Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Salvage+Titan) return to a player's hand, the player gets to fill their graveyard with more artifacts, which they can later use to salvage the card should it wind up getting killed. This took care of power level concerns while simultaneously adding free flavor at no charge.


The final change to reduce power was dropping trample from the Titan's abilities. It was determined that such a large monster able to be played so quickly was a bit over the top when it virtually guaranteed punching some amount of damage through. That said, the powering down merited a small improvement in toughness; [Salvage Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Salvage+Titan) might not be able to get through for as much without trample, but it would also be harder to kill via [Incinerate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) or [Resounding Thunder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Resounding+Thunder) at 6/4.


The end result? A fun, artifact-friendly behemoth that's challenging but not over-the-top broken.


### Rafiq of the Many



![Rafiq of the Many](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rafiq+of+the+Many)

When Mark Rosewater announced the introduction of mythic rares to the world this past summer, the development team had already pushed out the first set of the new breed of cards. The directive for them had been clear: they were to be powerful, important story tellers but not necessarily Constructed auto-includes. In an effort to get the very first class right, a lot of effort went into tinkering with their power levels, shifting some up while others were shifted down. Rafiq was a member of the group who became more powerful.


There's no doubt Rafiq has a commanding on-field presence now. Not only does he provide a 3/3 body, but his abilities function as a pseudo-haste effect, giving a creature already in play +1/+1 and doubling their power. When Rafiq hits the board, the rest of the table sits up and takes note; trouble could soon be headed in their direction.


But what if Rafiq cost ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) instead of the much friendlier ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)? What if the bonus he provided your creatures was different? Or what if, as he was originally presented, he was:



> 
> Rafiq of the Many 2WUG  
> 
> Legendary Creature  
> 
> Heroic – Whenever a creature you control attacks alone, it gets +1/+1 and double strike until end of turn.  
> 
> 3/3
> 


His impact on a game of **Magic** would have been reduced. Testing revealed some of these weaknesses and quickly inspired changes, while also cleaning up the ability that would eventually become exalted. Originally exalted was simply an ability word for any bonus applied to a lone attacking creature. As testing progressed, however, it soon became apparent that constantly having to check all the bonuses applied to your creature from a plethora of different sources was confusing; why not make "heroic" a single bonus that was universal so it was quick to recognize and more enjoyable to play?


That enabled us to make the ability more fun and easier to understand, but dropped Rafiq in power level too much. How could we have a strong heroic (by then called exalted) creature from Bant that stood out from the rest? The fix came by compromise: finding a way to keep the cool extra exalted abilities on some of the cards that had them while still universalizing exalted overall. So Rafiq was keyworded with exalted, then gained the additional bonus of providing double strike to a lone attacker. You can see this work on other cards such as [Battlegrace Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battlegrace+Angel).



![Battlegrace Angel](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Battlegrace+Angel)

How about the final version? After much discussion, [Rafiq of the Many](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many) made it to the masses in his present form. No word yet on how popular he'll be as an [Elder Dragon Highlander / Commander](http://archive.wizards.com/Magic/TCG/Article.aspx?x=magic/rules/edh) general, but it seems safe to bet you'll soon see him during many such games.


### Kresh the Bloodbraided



![Kresh the Bloodbraided](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kresh+the+Bloodbraided)

While Rafiq was one of the mythic rares that saw an increase in power level, some of the mythic rares were so strong they had to be taken down a peg or two during testing. [Kresh the Bloodbraided](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kresh+the+Bloodbraided), one of the representatives from Jund, was just such a card.


As he sits now, Kresh is very flavorful and sufficiently powerful. He plays nice with the Jund mechanic of devour, quickly growing unmanageable by benefiting from what the denizens of Jund do best. His 3/3 body isn't oversized at five mana but can quickly grow disproportionate. And of course he even takes a stab at appealing to Johnnys everywhere; how will *you* build around Kresh? [Altar of Dementia](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Altar+of+Dementia)? [Ooze Garden](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ooze+Garden)? [Goblin Bombardment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Bombardment)? The options are tantalizing.




|  |  |
| --- | --- |
| 
Ooze Garden
 | 
Altar of Dementia
 |

When Development first got hold of Kresh, however, things were a different story. Here's what his first stats looked like:



> 
> [Kresh the Bloodbraided](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kresh+the+Bloodbraided) 2BRG  
> 
> Legendary Creature  
> 
> Carnage – Whenever a creature goes to the graveyard from play, put a +1/+1 counter on each creature you control.  
> 
> 4/4
> 


It didn't take long for Development to do unfair things with *that*. Mons Johnson (of [Mons's Goblin Raiders](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mons%27s+Goblin+Raiders) fame) managed a combo involving Kresh, [Murderous Redcap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), and [Nantuko Husk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk) that could easily "go infinite" and sucked a lot of fun out of games. Persist creatures in general were very good with Kresh, and it soon became apparent that even at five mana, having no activation cost made it much too simple to use Kresh as an engine to do degenerate things; not really what we had in mind when designing the Jund legendary mythic rare.


Naturally, stats started morphing. The 4/4 was dropped to 3/3, but that didn't really address the fact Kresh's abilities were being abused. His "carnage" ability (which eventually lost its status as an ability word) changed from giving *all* of your creatures +1/+1 to giving Kresh himself the bonus. A mere +1/+1 from a creature dying wasn't quite strong enough, however, so things went back the other way. Now Kresh himself gets large fast based on what happens on the board, but without being unfun. And, like Rafiq, you can count on Kresh showing up at the EDH table in the near future!


### Cradle of Vitality



![Cradle of Vitality](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cradle+of+Vitality)

For our last example in this installment, we're going to look at an excellent example of an unassuming card at print that started at much more powerful than it was intended to be. We know it today as a neat way to improve decks focused on lifegain, and possibly a way of interacting with persist creatures (did someone say [Kitchen Finks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks)?). Things weren't always this way, and here's how it looked when it was brought to development:



> 
> Cradle of Vitality 2W  
> 
> Enchantment  
> 
> Whenever you gain life, you may pay X, where X is less than or equal to the amount of life you gained. If you do, put X 1/1 white Spirit creature tokens with flying into play.
> 


This, as many developers noted, was a cool combo with cards like [Soul Warden](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Soul%2BWarden) or [Essence Warden](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Warden). It didn't fit the flavor we were looking for, though, and the 1/1 Spirits soon became +1/+1 counters:



> 
> Cradle of Vitality 2W  
> 
> Enchantment  
> 
> Whenever you gain life, you may put that many +1/+1 counters on target creature.
> 


Aaron Forsythe quickly pointed out that not having an activation cost for this version was problematic. What happened when someone resolved Cradle in addition to [Spike Feeder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spike+Feeder)? A two card combo that left you with an arbitrarily large amount of life and an arbitrarily large [Spike Feeder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spike+Feeder)? Something that powerful shouldn't be so easily accomplished for so little effort, and that's before considering the implications of an easily achieved "impervious" [Kitchen Finks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks).


Upping the initial cost from ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) to ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) made the card a bit more balanced, but Greg Marques demonstrated the card still wasn't where it needed to be one afternoon during Future Future League testing. The deck he used for the deed? It revolved around efficient life-gain creatures like [Kitchen Finks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks), [Knight of Meadowgrain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+Meadowgrain), and...[Goldenglow Moth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goldenglow+Moth). It may not sound like much, but it's a rough world when [Goldenglow Moth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goldenglow+Moth) morphs from an innocuous 0/1 into a 4/5 flier that just netted your opponent 4 life before munching your biggest attacker—and did all of it for free.




|  |  |
| --- | --- |
| 
Goldenglow Moth
 | 
Kitchen Finks
 |

Ultimately the card was revised to the version we see today, ready for fun and the ingenuity of the public's deck builders, but safe from the shenanigans that might have been wrought had the crafty minds of the development team not caught it before seeing print.


### Conclusions


That's a look at some of the interesting stories from Development during the process that brought you *Shards of Alara*. Just like the second stage of the Project Y example, we added some ideas, cut some, increased the power of a few, and decreased the power of a few others. Between the two of us (design and development) we're very excited the world finally gets to see what we've been working so hard on. Here's to enjoying *Shards of Alara*!


### Last Week's Poll




|  |  |  |
| --- | --- | --- |
| **Which set will you miss most when Standard rotates?** |  |  |
| *Time Spiral* | 3023 | 32.4% |
| *Planar Chaos* | 1550 | 16.6% |
| *Future Sight* | 1479 | 15.8% |
| I don't play Standard | 1448 | 15.5% |
| *Coldsnap* | 981 | 10.5% |
| None of the above | 539 | 5.8% |
| What is Standard? | 320 | 3.4% |
| **Total** | **9340** | **100.0%** |

With *Time Spiral*—including its 121 "timeshifted" cards—making up close to half the cards rotating out of Standard, it's not surprising to see it at the top of the list.


*Shards of Alara* Launch Parties are this weekend, October 3-5, at stores worldwide, and you won’t want to miss them. Get your chance to buy *Shards of Alara* cards as soon as they go on sale, play the new set with your friends, and get a foil, alternate-art [Ajani Vengeant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Vengeant) promo card!








