
---
[Link to Wayback Machine](https://web.archive.org/web/20170403202656/http://magic.wizards.com/en/articles/archive/latest-developments/collisions-multiverse-part-1-2009-05-01)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "&#13;"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646556"
[_metadata_:publish_date]:- "2009-05-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Collisions in Multiverse, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2017-04-03 20:26:56"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170403202656id_/http://magic.wizards.com/en/articles/archive/latest-developments/collisions-multiverse-part-1-2009-05-01"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/collisions-multiverse-part-1-2009-05-01"
---


Collisions in Multiverse, Part 1
================================



 Posted in **Latest Developments**
 on May 1, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







A*lara Reborn* tells the story of Alara's five shards colliding and the disastrous things that happened to their inhabitants. This was a momentous occurrence in the **Magic** multiverse. However, behind the scenes, the many minds that make up **Magic** R&D were crashing against each other in a different Multiverse. When we talk about Multiverse among ourselves, we're usually talking about the internal database that we use to help us both build Magic sets and communicate among ourselves while we do so. Today, we'll take a walk together through the *Alara Reborn* Multiverse file and I'll share with you some of the comments that we made while we were developing **Magic**'s first all-multicolor set.


### [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_boonArt.jpg)As we go along, I'll introduce everyone in the comments to you. Here, "AJ" is Great Designer Search winner and *Alara Reborn* developer Alexis Janson, "MP" is *Alara Reborn* lead developer Matt Place, "Del" is **Magic** editor Del Laugel, and I am "TML." "Spin" is the playtest name for cascade.



> 
> AJ 8/11: We should finish our spin discussion from e-mail re: trigger vs. resolution.  
> 
> TML 8/15: I prefer Spin to be the last thing that happens when resolving a spell, so that there is only one spell on the stack at any given time. This is more natural and simple to explain and play with.  
> 
> MP 9/11: Spin is going to trigger when played so that it is like other magic mechanics.  
> 
> Del 9/26: Was an Aura with enchant creature, "Enchanted creature has flying."
> 
> 
> 


The first version of [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon) that I played with was an aura that cost {2WU}, gave its enchanted creature flying, and had cascade. This read as a very appealing card, but caused frustrating things to happen when I played it. For example, one might cast that version of [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon) targeting a small creature, get a [Woolly Thoctar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar) off of the cascade, then want to put the [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon) on the Thoctar instead. This is not legal because the spell's target was already announced before the Thoctar arrived. It also felt weird that the cascade effect is very capable of producing a creature, but that version of [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon) cannot be played while there are no creatures in play! I often wished when I had no creatures that I could just play it and have nothing happen if the cascade effect didn't find a creature, but the rules of **Magic** do not allow this.


The version of cascade that I constructed to solve this problem was to have cascade be the last thing that happens during the resolution of a non-creature spell that has cascade, and to have the cascade effect happen right before a creature with cascade enters play. The game had never used this timing window on creatures before, and because of that we chose not to explore that option. However, we had already eliminated the possibility of using cascade as a comes into play trigger because it did uncomfortable things with cards like [Recurring Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare). Similar problems sunk every alternative version of cascade that we came up with, so we had to figure out how to make each cascade card feel natural without changing the mechanic.



![Stormcaller's Boon](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stormcaller%27s+Boon)

 

In the end, we decided to change the individual cascade cards to make them feel natural with the cascade mechanic as it was. In the case of [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon), it was decided that the card should not be an Aura. However, we had already commissioned the art so we still had to make the card grant flying in some way. The final version of the card was designed to allow a player to live the dream of cascading up a creature, then using [Stormcaller's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormcaller%27s+Boon) to enhance it. It also serves as a powerful game-ending effect in Limited. We are happy that the cascade cards that are in the set are all reasonably simple to execute, and we think that they allow the fundamentally fun cascade mechanic to shine. Based on the many stories I heard from the Prerelease, it did plenty of shining last weekend!


### [Talon Trooper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talon+Trooper)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_talonArt.jpg)
![Talon Trooper](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Talon+Trooper)

Multiverse is a powerful tool that is very important to **Magic** R&D's ability to produce cards. However, the picture of Multiverse that we paint for you in articles is not entirely accurate. We often show you comments that are deep discussions of important issues. However, comment fields are often not interesting; for example, the Multiverse record for [Goblin Sky Raider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Sky+Raider) in *Tenth Edition* is completely devoid of comments. Another possibility is that the only interesting comments in a card record have to do with templating or editing. Sometimes, however, we fill the development comments fields for otherwise uncontroversial cards with goofy comments. [Talon Trooper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talon+Trooper) is one card that received this treatment. In the following exchange, "MR" is **Magic** head designer Mark Rosewater and "DAL" is Shards of Alara lead developer Devin Low, who is no longer at Wizards of the Coast.



> 
> MP 2/18: Nice.  
> 
> MR (3/27/08): What Matt said.  
> 
> MP 4/9: Agree with Mark.  
> 
> DAL 4/24: Agree with Matt.
> 
> 
> 


Exchanges like this make me love working here a little bit more every time I read them.


### [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_willArt.jpg)[Sage Owl](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) is a card that we debate endlessly in the Pit. Is it for Timmy or Spike? Is it a casual card? What does casual even mean in that question? We know definitively that new players enjoy casting [Sage Owl](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl), and we also know that rearranging the top cards of an opponent's library is something that griefers love to do. [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will) is fascinating to me in that it can do both of those things, and its comment field is very interesting to me in hindsight. Here, "BR" is Wizards of the Coast Vice President of R&D Bill Rose, and "AF" is Director of **Magic** R&D Aaron Forsythe.



> 
> BR 2/26: When Johnny comes into play, Timmy feels bad.  
> 
> AF 3/6: No way. Timmy is the ultimate griefer. Anyway, changed from "opponent" to "player."  
> 
> DAL 4/24: This isn't too mean - they get to draw the cards pretty soon, and it's one-and-done.
> 
> 
> 


The playtest name for this card was Johnny Scrambles, which explains Bill's first comment. The second comment reveals that the first version of this card did not allow the caster of [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will) to rearrange his own top three cards; instead, the card went after the opponent. Aaron responded to that comment with the reaffirmation that griefers are indeed Timmies, which is something I [wrote half an article about](/en/articles/archive/latest-developments/yang-timmy-2009-03-13) a few weeks ago. However, Aaron also changed the card to allow players to rearrange their own top three cards as well.



![Architects of Will](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Architects+of+Will)

 

After plenty of playtest drafts with [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will), I agree with Devin that the griefer side of the card is not too mean even though it does often end a game in which the caster of the [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will) is already ahead. However, it's fascinating that the comments are all about the griefer half of the effect. I watched a lot of people play with [Architects of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Architects+of+Will) at the Prerelease, and I did not see any players use it to rearrange the top cards of their opponents' libraries. It would appear that rearranging the top cards of one's own library is just so much fun that the griefer half has comparatively little appeal. The other fascinating thing was that my opponents were surprised every time I used this card's trigger on them instead of me. It appeared as though the idea of doing that had never crossed their minds, and that made me very happy. I believe that adding the [Sage Owl](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) mode to this card made the world a better place.


### [Singe-Mind Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Singe-Mind+Ogre)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_singeArt.jpg)The Tuesday **Magic** meeting that happens right after lunch is usually the one time each week when all of **Magic** R&D comes together. We often use it to talk about big picture issues like I talked about in [this article](/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-27). A few times a year, we use that Tuesday meeting for what we call "The Slideshow." At this event, we go card-by-card through a set that we are about to hand off to production. The slideshow often feels like a big party because we are celebrating the results of months of hard work. However, it also allows us to make a final check on the cards. Each slideshow usually results in a few cards changing in small ways, and [Singe-Mind Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Singe-Mind+Ogre) was one such card.


Singe-Mind Ogre existed in the file exactly as printed for many months, except for one small difference: it was only a 2/1. When that card came up in the slideshow, many people asked why it was that small when the art was so imposing. No one had a good answer. Creative said that it would be happy with a 3/2, and Matt Place said that he would consider that.



![Singe-Mind Ogre](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Singe-Mind+Ogre)

 

When the slideshow was complete, the developers convened in the Pit. We had already finished developing *Alara Reborn* for Limited so no one was thrilled about the idea of changing a common card, but we recognized how goofy it was that the card that matched that art was only a 2/1. We also came to the conclusion that kicking it to a 3/2 would not make the card too powerful in any arenas, so we went ahead and changed it to match the art. That led to this thrilling Multiverse comment:



> 
> Del 11/12: Changed from 2/1 to 3/2 after the slide show to be a better Ogre.
> 
> 
> 


### [Rhox Brute](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Brute)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_bruteArt.jpg)This card was called "Square" in playtesting, and I drew a single square in the empty art box of each playtest copy I ever played with. I am sad that my collection of amusing playtest cards does not contain a Square with my own original art.



![Rhox Brute](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rhox+Brute)

 

### [Leonin Armorguard](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Armorguard)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_armorguardArt.jpg)Developers care first and foremost that a card set is fun to play with. However, we also try to make sure that each card's concept, which includes the art and tentative name, matches its mechanic. We do our very best to avoid last-minute creative problems like what happened with [Singe-Mind Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Singe-Mind+Ogre). Sometimes we're not sure if a card concept makes sense with a mechanic, so we ask creative to let us know if a card's mechanic and concept match. Thanks to Multiverse, many of these discussions are recorded for posterity. For example, here are the development comments from [Leonin Armorguard](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Armorguard). The card was playtesting wonderfully, but a sketch of the card's art prompted me to question our mechanic.



> 
> TML 8/15: Is it wierd that the concept is a creature that is getting helped, but the mechanic is that it helps your other dudes?  
> 
> DB 8/15/08: Wouldn't you feel more confident with that guy around? :D  
> 
> TML 8/15: I'm not saying it doesn't work, it's just weird. :)  
> 
> MP 8/21: "Prrrrr, the health potion is in there, keep searching..." - Leonin Champion  
> 
> DB 8/28/08: Putting MP on the next flavor text team.
> 
> 
> 



![Leonin Armorguard](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leonin+Armorguard)

 

Savor the Flavor columnist Doug Beyer's amused comments here made it clear that he didn't see a creative problem with the card, so we printed it as it was.


### [Arsenal Thresher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arsenal+Thresher)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_thresherArt.jpg)One part of the developers' job is to identify things that make games unfun because they are too powerful. However, another important part of our job is to protect things that are both fun and powerful at a reasonable level. We often use Multiverse to let each other know about cards that are especially fun so that they can be protected.


[Arsenal Thresher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arsenal+Thresher) was changed to its current form in late June of this year, and from then until late August no one made a single comment. This scared me because of how much fun I was having with it, so the following exchange ensued.



> 
> TML 8/20: No comments on this card is sad. He is super fun and an awesome artifact reward card.  
> 
> MP 8/21: Yeah this guy has done great things.
> 
> 
> 



![Arsenal Thresher](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arsenal+Thresher)

 

Lead developers of sets are always happy to hear positive feedback about their cards, and playtesters are always happy to know that their feedback was heard. Both Matt and I were happy after this, and the card was printed exactly as is. I foresee many Esper drafters picking these guys up in the third pack and cackling with glee.


### [Zealous Persecution](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zealous+Persecution)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld36_zt.jpg)Unfortunately, I'm out of time, and I only got through the commons. I'll do another column going through fun comments from the rest of the cards sometime soon. I'm proud of the work that everyone in **Magic** R&D did on *Alara Reborn*. This weekend local stores all around the world are holding *Alara Reborn* Launch Parties, which are your first chance to buy *Alara Reborn* cards. (Usually these start on Friday, but this time they started on Thursday due to the May Day holiday.) Find one near you [here](http://archive.wizards.com/magic/magazine/article.aspx?x=mtgcom/events/releases)!


### Last Week's Poll




| **Are you going to an *Alara Reborn* Prerelease?** |
| --- |
| Yes, I am attending a local store prerelease. | 4385 | 49.9% |
| No. | 3092 | 35.2% |
| Yes, I am attending a regional prerelease. | 980 | 11.2% |
| Yes, I am attending both a regional prerelease and a local store prerelease. | 330 | 3.8% |
| **Total** | **8787** | **100.0%** |

[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/ARB_ArticleBanner_Launch2.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/releases)





