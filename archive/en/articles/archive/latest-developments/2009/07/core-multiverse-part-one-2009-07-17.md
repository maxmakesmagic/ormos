
---
[Link to Wayback Machine](https://web.archive.org/web/20211023155311/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Now that you've had the chance to play Magic 2010 at the Prerelease this past weekend, it's time for me to show you some of what went into its construction. To do that, we'll dive into Multiverse, the internal database we use to collaborate when we make Magic cards. There are too many comments I found interesting to do in one article, so I'll be splitting it across two. Let's"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646696"
[_metadata_:publish_date]:- "2009-07-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Core of the Multiverse, Part One"
[_metadata_:wayback_capture_timestamp]:- "2021-10-23 15:53:11"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211023155311id_/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17"
---


The Core of the Multiverse, Part One
====================================



 Posted in **Latest Developments**
 on July 17, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







Now that you've had the chance to play ***Magic** 2010* at the Prerelease this past weekend, it's time for me to show you some of what went into its construction. To do that, we'll dive into Multiverse, the internal database we use to collaborate when we make **Magic** cards. There are too many comments I found interesting to do in one article, so I'll be splitting it across two. Let's go!


### Siege Mastodon



![Siege Mastodon](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Siege+Mastodon)

Early in ***Magic** 2010* development, we became unhappy with how fast the Limited games were. The speed of the format felt very similar to *Shards of Alara* Limited with *Alara Reborn*, which was on the faster end of the Limited spectrum. We like **Magic** to change over time so it stays fresh and varied, so we tweaked some cards to encourage slower games. In previous core set development, we would have had to dig through previously printed sets to find cards that would accomplish our goal. However, for ***Magic** 2010* we got to just make up a new card. Here are the comments from [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon).



> 
> EVL 9/3: Another card to slow down the game  
> 
> AF 9/23: Quickly becoming my favorite common. If people are to get excited about flying and fear, guys with no evasion have to fail regularly at being able to attack. This guy ensures that.
> 
> 
> 


In hindsight, when I talked about [how awesome making new cards was](/en/articles/archive/latest-developments/solving-core-sets-dilemma-2009-07-10) for the game play of ***Magic** 2010*, I should have talked about a splashier card than this one. [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) is, after all, a vanilla 3/5 for five mana. However, the first Sealed Deck playtest we did that included this card was totally different from any of the previous ones. [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon)s were gumming up the ground and making it so that white and blue flying creatures had time to outrace ground assaults. I was thrilled that such a small change to an innocuous card gave us the results we wanted, and that made me very glad that we were no longer restricted to cards we had already printed. It's quite possible that ***Magic** 2010* was the first **Magic** set that has really wanted to have a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 3/5 vanilla creature, and this time we were not afraid to just make it.


**Magic** developers experience sets very differently from the rest of the world. Despite how mundane [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) appears, I feel a lot of nostalgia when I look at it and remember how excited I was about new cards in the core set when we made it. I would be shocked if I were not among the three people in the world who like [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) the most.


### Illusionary Servant



![Illusionary Servant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Illusionary+Servant)

We have talked a lot on the site recently about how ***Magic** 2010* is a return to resonant fantasy concepts. We also talked a lot about this during ***Magic** 2010* design and development. Some tropes were easy to turn into cards; [Lightning Bolt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt), for example, is pretty much perfect. On the other hand, there were some concepts that we wanted to have in the set that were more difficult to translate into cards. One example of this was the concept of the illusion. Rather than hem and haw about what the correct implementation of an illusion was, Aaron Forsythe simply put an illusion in the set and watched people comment.



> 
> AF 5/19: Trying Skulking in blue.  
> 
> DB 5/20/08: Like. This ability is really flavorful for blue. [Gossamer Phantasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gossamer+Phantasm) &gt; [Skulking Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Knight).  
> 
> AJ 5/20: Don't like how Freeze [now [Ice Cage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ice+Cage)] and Illusion [[Illusionary Servant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Servant)] have two different skulking triggers. This is the sort of thing players tend to shortcut in their memory and will get confused if they work differently.  
> 
> AF 5/20: I guess this could be "destroy."  
> 
> AF 5/20: Is it okay that illusions are represented by both "skulking" and "unblockable"?  
> 
> AJ 5/21: Not just "destroy" vs "sacrifice", but "becomes the target" vs "dealt damage".  
> 
> AF 7/22: Is this right? There was a popular Djinn submission that flickered out when targeted and you had to pay U when it came back. Is that a better Illusion mechanic than this?  
> 
> DB 7/23/08: I like "skulking" better for [Illusion]. When you disbelieve an illusion, it doesn't just go away for a while, it poofs entirely. The flicker mechanic feels more like a ghost -- also insubstantial, but persistent/recurrent.  
> 
> DAL 7/28: Skulking is a great match to Illusion to me.  
> 
> ND 7/28: Love skulking in blue. Very good match to the illusion creature type - feels D&D.  
> 
> TML 8/4: "When an opponent makes a Will save, sacrifice CARDNAME."
> 
> 
> 


You can see that we decided that this mechanic matched illusions. Interesting, S[kulking Ghost](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=kulking+Ghost) was the first high-profile card that used the "sacrifice me when I am targeted" mechanic. Since then, **Magic** players sometimes called creatures that had that mechanic "skulking" creatures, and that led all the way to *Time Spiral*'s [Skulking Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Knight). I learned during the discussions that surrounded some of these Multiverse comments that the original concept of [Skulking Ghost](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Ghost) was chosen because it was a ghost. "Skulking" was just an adjective that described a flighty ghost, but the important part of the concept was the ghost!


Next, Doug Beyer observed a problem with the word "sacrifice."


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld47_servantCloseUp.jpg)
> 
> DB 8/12/08: I know "sacrifice it" is the right template, but "destroy it" is more flavorful on a first read. ("When something touches my illusion, I have to 'sacrifice' it, whatever that means? It doesn't just go poof?")  
> 
> AF 9/23: Destroy could be awesome here.  
> 
> TML 8/12: That would raise problems with something like [Loxodon Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loxodon+Hierarch) regenerating all your guys. You shouldn't be able to regenerate from going poof.
> 
> 
> 


I agree with Doug Beyer here. "Sacrifice" is the wrong word for what happens to an illusion, but the actual rules behind sacrificing perfectly match what happens when an illusion goes poof. An illusion is destroyed, but a destroyed illusion in **Magic** would be able to regenerate. Despite our best efforts, sometimes words and flavor don't quite match. Here, we went with the flavor of the rules rather than picking the right word for the situation.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld47_timeMachine.jpg)Note that Aaron's comment on 9/23 came before my comment on 8/12. We have two theories about how this could have happened. One is that he can time travel. The other is that his hand was positioned one key to the right on the keypad from 8/12. Given that he's the director, I'll stick with the time traveling explanation.


There's a small amount of story yet to tell. Here it is:



> 
> AF 7/25: To common to give blue sufficient damage-dealing capability in limited.  
> 
> EVL 9/11: Moved to 1UU to improve blue.
> 
> 
> 


### Weakness



![Weakness](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Weakness)

Before a set is printed, the only way that we can interact with the cards is by reading Multiverse records or playing with low-quality playtest cards that have no art. Despite that, sometimes we catch glimpses of the majesty that will be when the cards are actually printed. In our internal database, [Unholy Strength](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength) comes directly before [Weakness](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weakness). That prompted this comment from Ken Nagle after ***Magic** 2010* was handed off.



> 
> KEN 1/5/2009: [Unholy Strength](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength) and [Weakness](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weakness) form most beautiful contiguous pair of Multiverse records I've ever seen.
> 
> 
> 


I'm looking at it now, and it is indeed beautiful.


### Sign in Blood


[Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) is cut from the same cloth as many black card-drawing spells. However, the card's grisly concept is an upgrade over more abstract concepts like [Night's Whisper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night%27s+Whisper) or [Skeletal Scrying](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Scrying). Early on, Aaron Forsythe asked us whether we thought it should be targeted, and we responded with a resounding yes.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld47_signCloseUp.jpg)
> 
> AF 6/9: This would be a more fun card if it was targeted: true or false?  
> 
> AJ 6/09: I thought you didn't want to do drawback cards at black common. And true.  
> 
> LS 6/9: This is also a good "learn about the choices!" card, and to teach about Magic (new players valuing 2 life more than 2 cards until they learn better).  
> 
> KEN 6/25: RAWR target player !!  
> 
> AF 7/14: Trying it.  
> 
> TML 7/25: I would be very interested in finding out how often this gets pointed at the opponent if it gets out the door as is.
> 
> 
> 


After we decided that [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) should target, former head developer Devin Low prompted us to try to figure out how good the card was.



> 
> DAL 7/28: Targeted seems fun. Is this the best card drawing in the set, better than all the blue card drawing? [Mind Spring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring), [Jace Beleren](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren), 2U Draw 2.  
> 
> TML 8/11: [Mind Spring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) is stronger than this, but this is stronger than Jace and 2U draw 2.  
> 
> ps 8/17: this is better than mind spring imho. night's whisper has seen play in vintage and it doesn't even randomly kill people. i think the power level of this is quite high.  
> 
> TML 8/18: Much of the card's power in vintage is the ability to go land-Mox-Whisper, but after some more play I think you're right about this being better.
> 
> 
> 



![Sign in Blood](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sign+in+Blood)

My statement that [Mind Spring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) is stronger than [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) was wildly misguided. At the time, I was playing a lot of mana ramp decks with [Fertile Ground](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground) and [Garruk Wildspeaker](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker), and in those decks [Mind Spring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) was very powerful for me. However, at ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)[Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) was a [Night's Whisper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night%27s+Whisper) with random upside. Former R&D member Paul Sottosanti's comment brought me back to earth. ***Magic** 2010* lead developer Erik Lauer also noticed how good it was too, and it received a recosting.



> 
> EVL 8/18: Cost changed from 1B to 2B.
> 
> 
> 


At this cost, however, it compared too easily to blue's [Divination](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination). The flavor of black trading cards for life made sense, but we didn't want [Divination](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) and [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) to line up so nicely next to each other. Comparing the two made [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) look unappealing even though it was actually still a good card. There was a point in our Limited tuning of the set where we wanted to make black stronger, so Erik took the opportunity to both make the card better and distance it from [Divination](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination).



> 
> EVL 8/20: Cost changed to BB.
> 
> 
> 


Now, [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) serves as both a powerful reward for playing heavy black in Limited and a potential Constructed card. While it is rare that a [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) is cast targeting its controller's opponent, I have seen more than one copy of the card take a player below zero life. Unfortunately, I have not seen it deck anyone. The holy grail of [Sign in Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood)s, however, is targeting an opponent who has both 2 or less life and only one card in his or her library. I'd love to know if you've seen this happen.


### Berserkers of Blood Ridge



![Berserkers of Blood Ridge](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Berserkers+of+Blood+Ridge)

I talked in the [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) entry about how we did some things to make ***Magic** 2010* Limited slower than *Shards of Alara* block Limited. One of them was to make cards like [Siege Mastodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon), but another was to be cautious about where we put large creatures. [Berserkers of Blood Ridge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserkers+of+Blood+Ridge) was a card that I tried to get changed to help with this. The influence that **Magic** set development team members have means that most decisions go the way they want them to, but one must always be prepared to lose a fight or two. This was one fight that I did not win. In hindsight, I'm glad that I lost!



> 
> TML 9/3: This guy is too big. I would like to make him smaller to have fewer guys that run over 1/4's and 2/4's.  
> 
> TML 9/4: Still enormous. I would like to have this card change as part of our campaign to make slower games.
> 
> 
> 


After the set was handed off from development, Aaron made a comment in this card's Multiverse record that I did not discover until I started building this article.



> 
> AF 1/5: The Berserkers have defeated you.
> 
> 
> 


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld47_defeated.jpg)I'm out of room here, but I'll be back with more ***Magic** 2010* Multiverse comments in a month or so.


### Last Week's Poll




| **Are you going to a Prerelease this weekend, or have you already gone to one?** |
| --- |
| Yes, I will attend or have attended a local store Prerelease. | 4139 | 45.4% |
| No. | 2765 | 30.3% |
| Yes, I will attend or have attended a large regional Prerelease. | 1185 | 13.0% |
| Yes, I will attend or have attended both kinds of Prereleases. | 362 | 4.0% |
| No, but I will play in Magic Online release events. | 356 | 3.9% |
| No, but I will play in Magic Online release events and would have posted angrily in the forums if this option were not here. | 319 | 3.5% |
| **Total** | **9126** | **100.0%** |


 

Many R&D members went to the big regional prerelease in Seattle. Personally, I went to a local Prerelease at Shane's Cards and Comics here in Renton. I saw lots of people having fun, and my colleagues reported seeing the same thing at other locations. We hope you continue to have fun playing with ***Magic** 2010* at this weekend's Launch Parties!


On an unrelated note, I refuse to believe that over three hundred of you would have posted angrily in the forums. With that in mind, I have a follow-up question.


  
[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/m10_launch1.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/releases)





