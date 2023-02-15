
---
[Link to Wayback Machine](https://web.archive.org/web/20161206225922/http://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "&#13; Cascade is a mechanic that produces free spells, and that is an element of Magic that developers must treat carefully. There were a number of things that could have gone wrong with cascade, but we were able to get the mechanic to a place that was both safe and fun. I'll talk about our journey to understand cascade as a mechanic overall, then discuss one of the questions we had to answer about how we were going to use it."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646566"
[_metadata_:publish_date]:- "2009-05-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Getting to Know Cascade"
[_metadata_:wayback_capture_timestamp]:- "2016-12-06 22:59:22"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20161206225922id_/http://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08"
---


Getting to Know Cascade
=======================



 Posted in **Latest Developments**
 on May 8, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







Cascade is a mechanic that produces free spells, and that is an element of **Magic** that developers must treat carefully. There were a number of things that could have gone wrong with cascade, but we were able to get the mechanic to a place that was both safe and fun. I'll talk about our journey to understand cascade as a mechanic overall, then discuss one of the questions we had to answer about how we were going to use it.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld37_3CardsAcross.jpg)**Magic** cards that skirt the mana system must be balanced very carefully. [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), [Contagion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contagion), and [Unmask](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unmask) ask for cards in your hand rather than mana, and all three of these cards have been Constructed superstars. Cards like [Time Spiral](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Spiral), [Frantic Search](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frantic+Search), and [Priest of Gix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priest+of+Gix) that gave players their mana back after they resolved enabled degenerate decks during Urza block. [Mind's Desire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire) is a great example of a card that uses free spell mechanics in a way that mostly didn't break **Magic** while still being powerful, but achieving this requires careful tuning to not create a monster like [Time Spiral](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Spiral). On the other hand, a card like [Spellweaver Helix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellweaver+Helix) offers lots of fun potential, but is not powerful in ways that tournament **Magic** players are likely to appreciate. Balancing cards that allow free spells so that they are both powerful and fun is a challenge that **Magic** developers have struggled with.


Cascade is a mechanic that produces free spells. It is also an exciting new mechanic that *Alara Reborn* needed to show off. We knew that we needed to be able to make cascade card that were powerful, fun, and balanced, so we spent some time early in *Alara Reborn* development thinking about the mechanic as a whole so that we would be able to cost cards that used the mechanic correctly.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld37_equation.jpg)An interesting exercise when thinking about a mechanic is to think in the abstract about how much mana it costs to add that mechanic to a card. Having a vague but reasonable answer for this question helps us cost simple cards that use that mechanic. For example, one might compare [Magma Jet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magma+Jet) to [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock), Fill With Fright to [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot), and [Tel-Jilad Justice](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tel-Jilad+Justice) to [Oxidize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oxidize), and conclude that "scry 2" costs exactly ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif) to add to a card. However, this gets messier when one is confronted with cards like [Lose Hope](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lose+Hope), [Stand Firm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stand+Firm), or [Serum Visions](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serum+Visions). How much does "Draw a card" cost, and how much does "Scry 2" cost? Honestly, I don't have a good answer for that question, and I'm sure the *Fifth Dawn* developers didn't either.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld37_vanille.jpg)It is even more challenging to think about the mana cost of mechanics that change value depending on the card that they are attached to. One great example of such a mechanic is trample. A French vanilla 1/1 creature with trample does not get much out of the trample ability. On the other hand, a French vanilla 7/7 with trample is a very powerful creature. Cascade, on the other hand, scales with the converted mana cost of a card and not with the power of a creature. That variability makes thinking about its value tricky, but spending time thinking about the question is still useful.


We discovered two different ways to think about the value of cascade. The first is based on variance. When you cast a spell with cascade, you're going to get a randomly produced card from your deck. The cost of the cascade spell determines how many of the cards in your deck you can hit. [Ardent Plea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ardent+Plea)'s cascade trigger may find only a few of the cards in your deck, while [Enigma Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enigma+Sphinx) could easily be the most expensive card you have chosen to play and therefore give you no control over which of the rest of your cards you find. **Magic** players are very smart, and we knew that some players would sculpt their decks to make their inexpensive cascade spells hit exactly what they wanted every time. This made cascade more powerful on low-cost cards.


The other way is to think about mana production. You always get a free card when you cast a spell that has cascade. Because you get to cast that new card for free, the cascade spell also generates mana, and the amount of mana generated is exactly the converted mana cost of the new spell. Therefore, a great way to think about how much mana the cascade spell is generating is the average mana cost of the card you cascade into. Casting an [Ardent Plea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ardent+Plea) in a deck with few one-mana spells is very likely to find you a two-mana spell, and therefore the cascade trigger has produced two mana for you. That's very different from casting [Enigma Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enigma+Sphinx), which will hit almost all of the rest of the cards in your deck. You might hit a six-mana spell, a four-mana spell, or a one-mana spell, so the expected ratio of the cascade card's converted mana cost to the amount of mana effectively produced by the cascade trigger is much lower. Because of this, cascade represents a large fraction of a cheap cascade spell's power, while a more expensive cascade spell gets a smaller fraction of its power from cascade.




|  |  |
| --- | --- |
| 
Ardent Plea
 | 
Enigma Sphinx
 |

You can see the result of our discussions from looking at the cascade spells organized by mana cost. [Ardent Plea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ardent+Plea), [Demonic Dread](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Dread), and [Violent Outburst](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Outburst) all grant fairly minor effects, but are still very strong cards because they consistently cascade into [Terminate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate)s, [Esper Stormblade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Esper+Stormblade)s, and other powerful two mana cards. On the other hand, [Enlisted Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enlisted+Wurm) and [Enigma Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enigma+Sphinx) get to have sizable bodies because they aren't consistently producing free five- or six-mana cards from cascade.


You might also notice that there are no two-mana cascade spells. This is not an accident. Imagine for a moment that the following card exists.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld37_waterfall.jpg)If this card existed, you could play only one unique card that costs one mana in your deck. This would change the action of cascade from a fun source of crazy randomness into a bizarrely mechanical tutoring effect. You would reveal cards from the top of your library, but you would play the spell that you knew all along you were going to play. The randomness would only come from the different amounts of information you granted your opponents.


We really felt this effect in a Future Future Elder Dragon Highlander game that we played with *Alara Reborn* cards, in which Alexis Janson got a [Maelstrom Nexus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Nexus) in play. A few people were capable of killing it, but we all wanted to see the card in action. Alexis started with a one-mana spell next turn. As it turns out, she had only three zero-mana spells in her deck. We encouraged her to just search her deck for the three cards and pick one of them at random, but she chose to do her duty as a member of the *Alara Reborn* development team and do exactly what the card said. It took her about a minute and a half to produce a [Zuran Orb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zuran+Orb) and do the required shuffling, and that showed us the annoying potential of low-cost cascade cards.



![Maelstrom Nexus](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Maelstrom+Nexus)

  

 Another reason that Waterfall is not a card is that thanks to *Time Spiral*, **Magic** now has some very powerful spells that have converted mana cost of zero. A card like Waterfall would have allowed players to abuse those spells very easily. For example, one could put four copies of [Ancestral Vision](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Vision) into a deck along with four Waterfalls and no spells that cost one mana. This means that Waterfall would always lead to drawing three cards, which is quite a deal for the low cost of ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). Amusingly, that's not the most dangerous of the *Time Spiral* spells without mana costs. [Eureka](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eureka)'s effect allows a player with the right cards in hand to win the game on the spot, and thanks to [Hypergenesis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hypergenesis) a player with access to Waterfall would have a guaranteed [Eureka](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eureka) for only two mana. The combination of the potential craziness with zero-cost spells and the mechanical annoyance kept us from making two-mana cascade spells.




|  |  |
| --- | --- |
| 
Eureka
 | 
Hypergenesis
 |

After plenty of play, we felt comfortable with making three-mana cascade spells. We knew that the potential for the [Hypergenesis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hypergenesis) deck still existed, but we also felt that the cost of including no one- or two-mana spells in one's deck was high enough that nothing would go wrong. On the other hand, that is hardly an insurmountable barrier, and plenty of players seem excited about the possibility of converting [Demonic Dread](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Dread), [Ardent Plea](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ardent+Plea), and [Violent Outburst](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Outburst) into the two-, one-, or zero-mana spell of their choice. We expect that this will turn out to be a fun thing to do, but also that it won't be ruinously powerful.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld37_ambush.jpg)One question we had to answer about how to use cascade was how many instants we wanted to give cascade to. *Alara Reborn* lead developer Matt Place kept a careful eye on how many instants had cascade. He understood how crushing it can be to have cards come out of nowhere and punish you for attacking. If too many instants had cascade, players might be ambushed by cascade cards after they attack one too many times and decide that attacking into open mana is just wrong. It's not very fun when it's never right to attack, so Matt wanted to make sure that this did not become the case due to excessive amounts of instants with cascade. On the other hand, it wouldn't be very interesting if there were no instants with cascade at all, because then you would be safe all the time. Matt's goal was to find a happy medium, and put cascade on instants only where it made sense to do so.


[Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) was one card that Matt had his eyes on. It entered development exactly as printed except that it was an instant and it only gained 3 life. Mike Turian noticed how brutal it was in Limited when someone attacked into a surprise creature from a [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight), and proceeded to build a board control deck that used [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) to cascade into [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring)s and [Kitchen Finks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks). [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) felt like a less powerful [Loxodon Hierarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loxodon+Hierarch), but the surprise factor made for very painful situations. *Alara Reborn* lead developer Matt Place knew that gaining life at instant speed was fun, but he also knew that excessive amounts of unfun surprises might be too painful. He decided that life-gain spells played fine as sorceries, and changed [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) to a sorcery that gained 4 life instead of an instant that gained 3.




|  |  |
| --- | --- |
| 
Captured Sunlight
 | 
Bituminous Blast
 |

This change caused people to wonder a little bit about why [Bituminous Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bituminous+Blast) was an instant. This card was often more painful a surprise than [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) because its main effect was (and is) excellent at instant speed. Why did it get to be an instant when [Captured Sunlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captured+Sunlight) didn't? Matt's answer was that there was a much larger amount of extra fun gained from making a removal spell an instant. Life-gain spells work fine as sorceries; [Bituminous Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bituminous+Blast) would not. Personally, I also found the removal spell to be much less onerous because it costs five mana. When I attack into five open mana and get surprised, it's hard for me to get angry. I'm glad that [Bituminous Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bituminous+Blast) is an instant.



![Violent Outburst](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Violent+Outburst)

  

 The only other instant with cascade is [Violent Outburst](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Outburst). There was a suggestion that this card change to a sorcery and grant creatures haste as well as +1/+0. However, we enjoyed the card as an instant trick enough that this idea never gained momentum, so we left it as it was.


Cascade is an extremely fun mechanic. Its potential frightened us early in *Alara Reborn* development, but we did the work to make it both exciting and balanced. We're proud of the cascade cards we printed, and we hope you are enjoying them!


### Last week's poll




| **Are you attending, or have you attended, an *Alara Reborn* Launch Party this weekend?** |
| --- |
| Yes | 1354 | 40.2% |
| No | 2017 | 59.8% |
| **Total** | **3371** | **100.0%** |

I'm excited by how many respondents attended the Launch Parties. They're a great way to get your hands on the new cards and meet other **Magic** players near you, and I hope everyone who went had fun. [Alara Reborn prerelease events](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/050609a) begin on Friday, May 15, and the set releases on **Magic Online** on May 18. If you didn't attend a Prerelease or Launch Party, or you just didn't get to play enough with *Alara Reborn* at those events, the **Magic Online** release events are your chance to get your fill!


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/ARB_ArticleBanner_Instores1.jpg)](http://archive.wizards.com/magic/tcg/Products.aspx?x=mtg/tcg/products/alarareborn)





