
---
[Link to Wayback Machine](https://web.archive.org/web/20150509113740/http://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09)

[_metadata_:description]:- "I think Mark was right when he cut straight to the chase on Monday … here’s your preview card: I want to spend the rest of this week’s column talking about the new indestructible ability from a developer’s point of view."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "288361"
[_metadata_:publish_date]:- "2004-01-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Indestructibility"
[_metadata_:wayback_capture_timestamp]:- "2015-05-09 11:37:40"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150509113740id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09"
---


Developing Indestructibility
============================



 Posted in [Latest Developments](/en/articles/columns/latest-developments-archive)
 on January 9, 2004 










I think Mark was right when he cut straight to the chase on Monday … here’s your preview card:


![](http://www.wizards.com/magic/images/mtgcom/fcpics/features/DS_eater_of_days.jpg)
I want to spend the rest of this week’s column talking about the new indestructible ability from a developer’s point of view.


All the developers agreed early on that indestructible was quite a cool ability, but none of us were sure exactly how good it was. First we had to figure out exactly what it would mean, of course. It’s all well and good to say “they’re indestructible,” but we spent several months arguing about what precisely that should mean. Everyone knew we wanted indestructible artifacts to survive a [Naturalize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize), and indestructible artifact creatures should never be killed by combat damage, but that still left a bunch of questions: Should indestructible legends die when there are two in play? Does an indestructible creature die when you use a -x/-x spell to lower its toughness to zero? What if your opponent plays [Wrath of God](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God)? What if they play [Diabolic Edict](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diabolic+Edict)? What if you feed your indestructible artifact to your [Atog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog)?


![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/105_atog.jpg)These questions were made even more difficult by the fact that we weren’t tied to any specific reminder text or card wordings. We knew we really liked the word “indestructible,” but that’s really all we had to go on. For quite a while we assumed that “Indestructible” would be a keyword ability, but that led to some really awkward wordings like “CARDNAME gains indestructible until end of turn.” *Gains* indestructible?! We wanted to say things like CARDNAME *is* indestructible. The templating team saved us here by figuring out that we could treat “indestructible” as an English-language word rather than a keyword ability.


Of course, none of that answered the question of how exactly indestructible should work in the non-obvious cases. One early version of indestructible said that whenever the artifact went to the graveyard that it would come back into play, and another version said that whenever it would get put into the graveyard you instead left it in play. Both of these versions were broken in the same way. Imagine sacrificing an artifact to something like an [Atog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog). Well, it would still be there to sacrifice again and again and again. Clearly, indestructible artifacts had to be vulnerable to sacrifice effects. Once we had that figured out, we knew that there were going to be some ways to cause them to go from play into the graveyard. They were just indestructible, not immortal. Rule Manager Paul Barclay really wanted all zero-toughness creatures to die anyway, otherwise he would have to rewrite the rules of the game so that state-based effects wouldn’t keep getting checked and trying to kill them over and over again. He also wanted them to die to the legend rule for similar reasons. From there it was a matter of figuring out what we could easily and clearly explain in reminder text. Drawing the line at destruction effects made sense anyway since the word we were trying to explicate was “indestructible” after all. We knew that most players would not realize that death from combat damage is technically a destruction effect so we went ahead and decided to spell that out in the reminder text and voila – a mechanic was born.


Once we knew exactly what our cool new mechanic would do, it was time to figure out how good it was (and how much mana to charge for it). The indestructible creatures were the hardest ones to balance. The set only has three of them, but they are potentially very powerful and they can go into every deck (regardless of color) so we knew we had to make sure they weren’t broken.


The more we played with them, the more powerful they seemed. We kind of wanted to have at least one creature that was relatively cheap, but even a 1/1 for 3 was too strong and the 2/2 for 5 that we had in the file was quite annoying to play against, especially in Limited where there weren’t a lot of ways to good to get rid of it. Because of the stalemates that can be generated by an indestructible creature in Limited play, we decided not to put any of them at common. Meanwhile, we didn’t want them all to cost an arm and a leg and that’s when somebody suggested that we go the “[Jade Statue](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jade+Statue)” route. Huzzah – problem solved! Of course, I’m only allowed to preview one card this week so you’ll have to wait and see how that creature actually turned out, but I can tell you that we’re pretty happy with the way it’s good without being too good …


### Last Week’s Poll Results:


Well, these are actually results from 3 weeks ago, but here’s what you guys thought of the Type 1 restrictions …





|  |
| --- |
| **What do you think of these bannings?**  |
| Thumbs Up | 2649 | 47.1% |
| I don’t care about Type 1 | 1420 | 25.3% |
| Thumbs sideways | 1048 | 18.6% |
| Thumbs Down | 506 | 9.0% |
| **Total** | **5623** | **100.0%** |




---

*Randy may be reached at latestdevelopments@wizards.com.*







