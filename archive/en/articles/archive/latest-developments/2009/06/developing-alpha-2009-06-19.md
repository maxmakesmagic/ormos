
---
[Link to Wayback Machine](https://web.archive.org/web/20200921134538/https://magic.wizards.com/en/articles/archive/latest-developments/developing-alpha-2009-06-19)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646641"
[_metadata_:publish_date]:- "2009-06-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Alpha"
[_metadata_:wayback_capture_timestamp]:- "2020-09-21 13:45:38"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200921134538id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-alpha-2009-06-19"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-alpha-2009-06-19"
---


Developing Alpha
================



 Posted in **Latest Developments**
 on June 19, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







M**agic** R&D is full of smart people, and we often ask each other questions merely to provoke thought. Some of these questions strike us as so interesting that we end up asking them over and over again. One such question is what the most successful **Magic** set ever is. When we asked **Magic** developer Erik Lauer, he claimed that the answer was clearly Alpha. After all, no other set in **Magic**'s history established an entirely new collectible card game. One of the reasons that Alpha attracted so many players was its focus on top-down design; that is, the cards all represented things that were easily understandable by anyone who had experienced fantasy before.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld43_3Cards1.jpg)Unfortunately, from the perspective of a developer, some of the cards in Alpha are grossly miscosted.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld43_3Cards2.jpg)Others are complicated implementations of ideas that could be made into cards more simply.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld43_3Cards3.jpg)**Magic** developers are humans too, and we fall in love with the same resonant concepts that everyone else does. However, we also like cards that are understandable and are reasonably costed. Over time, we've taken many of the resonant baseline concepts from Alpha and "developed" them by making new versions that are simpler, have more appropriate mana costs, and/or work better within modern rules. Today I'll examine some of those concepts and the journeys they have taken through **Magic**'s history.


### [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt)


**Concept:** A wizard summons a bolt of lightning.



![Lightning Bolt](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)

The lightning bolt spell is one of the most classic expressions of wizardly power in fantasy. The idea of calling lightning down from the sky with one's own personal power to cause destruction is intoxicating. Of course, **Magic**'s [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) is famous not only because it is a simple and resonant expression of a fantasy concept. It also happens to be very powerful. When I started playing **Magic** in 1997, starting the game off with a [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) to my opponent's face just felt awesome. Later, I learned that I could save it to kill my opponent's creatures. [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) was a strong constraint on early tournament **Magic**; creatures needed to be extremely efficient or have 4 toughness to be widely adopted.


We've tried to capture the magic of [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) many times, often in ways that have different gameplay than the original. Cards like Shock, Lightning Blast, Barbed Lightning, Branching Bolt, [Chain Lightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chain+Lightning), and so on are attempts to make lightning spells of a lower power level than [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) that have interesting game play. However, many players still wax reminiscent about the original, including those of us here in **Magic** R&D. We love the name "Lightning Bolt" and we all have fond memories of playing with the card. Creatures have grown some in power level since [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) was last in Standard; however, we've been happy with cards like Shock, Incinerate, and Volcanic Hammer for years. If Lightning Bolt were ever to return, it would be only after careful consideration and extensive playtesting.


### [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade)


**Concept:** An army goes on a righteous crusade.



![Crusade](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crusade)

The top-down concept here is spot on. When someone calls a crusade, every righteous warrior gets a little more excited. Only white creatures get to go on crusades, so the card invites players to build a deck just for it and include only white creatures. The unfortunate thing is that if your opponent has some white creatures around, they get just as excited by the [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade) as your own creatures do. Making your own creatures bigger is fun; making your opponent's creatures bigger is a downer.


We've done many riffs on this concept. [Angelic Voices](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angelic+Voices) an attempt to make only your stuff bigger, but it has clunky and unappealing text that punishes you for playing nonwhite creatures. [Call to Arms](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Call+to+Arms) unfortunately returns to [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade)'s text, but adds even more hoops that must be jumped through to keep in play. [Divine Sacrament](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Sacrament) and Light from Within both use new mechanics to offer the promise of giving white creatures even more than +1/+1, and Light from Within helps only white creatures you control.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld43_4Cards1.jpg)However, *Urza's Saga*'s [Glorious Anthem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glorious+Anthem) is the version of this concept we've put in the core set since Seventh Edition. Giving +1/+1 to all of your own creatures addresses the problem of making your opponent's creatures larger. It is also a much simpler card than the four cards from the previous paragraph. Glorious Anthem's eight-year tenure in the core set shows that we think it is a very good implementation of this concept.


 




|  |
| --- |
| 
Glorious Anthem
 |

Personally, I feel like the transition to Glorious Anthem from [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade) was not without cost. As a player who grew up with [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade), I find it a little jarring every time Glorious Anthem buffs an army of nonwhite creatures. As a developer, I enjoy the deck-building direction provided by [Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade)'s requirement that the creatures be white. If history is any indication, we won't stop making new implementations of this concept. Perhaps one of them will address this issue.


### [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist)


**Concept:** A spell that destroys another wizard's mind.



![Mind Twist](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mind+Twist)

Human beings value their intelligence. The idea of magical effects that alter or destroy someone's mind is classic because of how frightening it is to think of one's ability to think taken away. [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) expresses this idea across by forcing a player to discard their cards. A card that causes you to merely choose and discard cards might feel like it was forcing you to forget something, but [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) precludes that by making the discards random, as though the caster of the [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) is haphazardly tearing bits out of your memory.


[Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) was one of early **Magic**'s hated cards. One reason is that discarding cards at random is emotionally unsatisfying. Choosing and discarding a card is annoying, but you got to choose it. When the opponent looks at your hand and chooses a card for you to discard, you are sad that you lost your best card, but you can see that your opponent was allowed to choose it. Random discard just feels worse than either of the previous two options because it is totally based on luck, not choices made by either player. Another reason the card was hated is that it was very, very powerful. That power earned [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) a spot on the restricted list very early on.


I had not yet joined Wizards of the Coast when *Morningtide* was released, and as soon as I saw Mind Shatter I thought that **Magic** R&D had made a terrible mistake. [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) is very powerful and has a reputation for being quite unfun, and I did not believe that adding a single black mana was enough to balance such a powerful effect. It amuses me in hindsight that it did not even have a negative effect on Standard. Its most common use has been to punish decks that planned to quickly build up mana to cast powerful expensive spells, but aggressive decks are now fast enough that Mind Shatter is not strong against them. [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) earned much of its reputation for ruining tournament games in formats that contained [Dark Ritual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual). In Vintage, [Black Lotus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus), [Sol Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sol+Ring), [Mana Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain), and the Moxes also didn't help. Perhaps if those cards had not existed, [Mind Twist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist) would not have been undercosted after all.


### [Dragon Whelp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp)


**Concept:** A baby dragon.



![Dragon Whelp](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dragon+Whelp)

[Dragon Whelp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) is an adorable **Magic** card, and one of my favorites. When I told **Magic** creative manager Brady Dommermuth this, he accused me of falling victim to nostalgia. However, he was wrong. The first time I ever cast a Dragon Whelp was in *Time Spiral* Block Draft. I found it completely adorable that this little baby dragon couldn't quite control its own fire. It didn't hurt that Dragon Whelp is a very powerful card in Limited, but I still fell in love with its quirky death trigger while I beat people with it.


We've done a few other baby dragons before. The first riff on Dragon Whelp was *Judgment*'s [Fledgling Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fledgling+Dragon), which starts small but becomes a full-grown [Shivan Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Dragon) when its controller reaches threshold. The most recent attempt is [Hellkite Hatchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hellkite+Hatchling), who must be fed to grow to adult size. *Tenth* *Edition*'s designers chose to use *Darksteel*'s simple [Furnace Whelp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Whelp) as their representative baby dragon.


Every baby dragon we've made has been a reasonably powerful Limited card, but my favorite of them is still Dragon Whelp. I have an irrational love for the way it sometimes explodes. In fact, its [new cute-but-deadly art](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=178019) in *From The Vault: Dragons* made it the card in that set that I was the most excited to acquire.




|  |  |  |
| --- | --- | --- |
| 
Fledgling Dragon
 | 
Hellkite Hatchling
 |  |

Dragons are both classic fantasy tropes and classic **Magic** cards, so it's only natural that we'll keep printing them.


### [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats)


**Concept:** A swarm of rats that gets more dangerous as it grows.



![Plague Rats](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plague+Rats)

At the very beginning of **Magic**'s life, there were no deck construction rules that governed the number of copies of the same card that could be played in one deck. A player could put whatever cards he owned in his deck, and that was that. Accordingly, Alpha contains [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats), a card that rewards a player for collecting tons and tons of copies. The idea of a growing swarm of rats is reasonably resonant, but collecting is something that human beings love to do. [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) explicitly encourages this behavior, and had very fun results in play when tons of them appeared in the same deck.


Unfortunately, cards other than [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) were not developed with playing unlimited quantities of them in mind. With cards like [Black Lotus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus), [Timetwister](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Timetwister), [Time Walk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk), and others floating around, with infinite card access it wasn't too hard to build a deck that won on the first turn every time. To fix this, the deck construction rule that allowed players to play no more than four of the same card was instituted. This fixed the game for every card other than [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats), but it made [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) very sad. How was one supposed to get tons of copies of [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) in play when one could only play four of them?


Many **Magic** cards have used this idea. Cards like [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle), [Muscle Burst](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Muscle+Burst), and [Aurochs](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aurochs) encourage players to play many copies of them, but the four-of rule limits their ability to explode. The obvious solution to this problem is to simply write on a card that one could play as many copies of it as one wants. *Darksteel*'s [Relentless Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Relentless+Rats) was the result of this realization, and after some testing, developers decided that it was safe to be more generous with power and toughness to our new swarm of rats than Alpha was with [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats).


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld43_rats.jpg)### [Raging River](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+River)


**Concept:** An uncrossable river divides the battlefield.



![Raging River](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Raging+River)

[Raging River](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+River) does a great job of showing us what a big river cutting across the battlefield would do. Unfortunately, not all top-down concepts are great for **Magic**. Some are very good top-line ideas, but have very messy implementations when reproduced faithfully on a **Magic** card. Other concepts simply aren't resonant. In my mind, [Raging River](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+River) falls into both of these categories. Creating a river in the middle of the battlefield isn't the kind of thing I imagine myself doing as a powerful wizard, and the card itself is a pile of words. **Magic** developers have chosen not to take another shot at this concept.


### Wrapping Up


We've reached the bottom of Top-Down Week. When Aaron Forsythe [introduced ***Magic** 2010*](http://archive.wizards.com/magic/Magazine/Article.aspx?x=mtg/daily/feature/27a), he told you that many aspects of the set were inspired by conversations about top-down **Magic** design. You'll start seeing what came out of those conversations when ***Magic** 2010* previews start on June 29!


We [announced](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/43d) some changes to the Vintage Restricted list today, as well as a banning in **Magic Online** Kaleidoscope. I don't have space to talk about our reasons for these changes in this article. I will cover this topic as part of next week's article.


### Last Week's Poll




| **What’s your favorite format to read about in Magic tournament coverage?** |
| --- |
| Standard | 2144 | 39.1% |
| Booster Draft | 899 | 16.4% |
| Legacy | 543 | 9.9% |
| Extended | 512 | 9.3% |
| Other/None | 398 | 7.3% |
| Vintage | 344 | 6.3% |
| Sealed Deck | 326 | 5.9% |
| Block Constructed | 313 | 5.7% |
| **Total** | **5479** | **100.0%** |


 

It's not surprising to see that Standard is the favorite format for coverage readers. PTQ attendance this season has been spectacular, so it's clear that our Standard format is something that people want to play as well. Thanks for the feedback!








