
---
[Link to Wayback Machine](https://web.archive.org/web/20211018085912/https://magic.wizards.com/en/articles/archive/latest-developments/four-resolutions-oh-six-2006-01-06)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "I just got through watching the University of Texas pull off a startling upset of USC in the Rose Bowl to win the college football national championship. The cool part was seeing Todd Harris on the sidelines of the game reporting for ABC. I met Todd several years ago when he was working for ESPN2 covering, of all things, the Magic World Championships. I was playing in that"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "289716"
[_metadata_:path_date]:- "2006-01-06"
[_metadata_:publish_date]:- "2006-06-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Four Resolutions for Oh-Six"
[_metadata_:wayback_capture_timestamp]:- "2021-10-18 08:59:12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211018085912id_/https://magic.wizards.com/en/articles/archive/latest-developments/four-resolutions-oh-six-2006-01-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/four-resolutions-oh-six-2006-01-06"
---


Four Resolutions for Oh-Six
===========================



 Posted in **Latest Developments**
 on June 1, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe











I just got through watching the University of Texas pull off a startling upset of USC in the Rose Bowl to win the college football national championship. The cool part was seeing Todd Harris on the sidelines of the game reporting for ABC. I met Todd several years ago when he was working for ESPN2 covering, of all things, the *Magic* World Championships. I was playing in that event. My how far we've all come through the years.


Speaking of years, we've just started a new one—one that will include four fantabulous new *Magic* releases: *Guildpact* and *Dissension* round out the lovely *Ravnica* block, *Coldsnap* will take us all back to Kjeldor and Balduvia for a quick visit, and then this year's big set (“Snap”) will show up and blow everyone away. *Guildpact* previews start in earnest next week, so this week I'm going to reflect on some decisions I made while working on *last* year's four sets and try to make some resolutions on how I can get better at my own job this year.


### Set 1: *Betrayers of Kamigawa*


**Resolution**: Do not stop paying attention to a set after it is out of my realm of responsibility.



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Umezawa's%20Jitte)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa's%20Jitte)
I wasn't on any of the design or development teams for the *Kamigawa* sets; instead, I was mainly just a playtester. *Betrayers*, for all the good that is in it, will always be remembered for this mistake that is [Umezawa's Jitte](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte).



If you've been playing close attention to how we make cards and where we've run into trouble before, it should have been obvious that Jitte had issues. It was in a theme deck, for crying out loud, where it didn't belong for several reasons, the least of which being that it could easily overpower every other card in every other theme deck in the block. What happened?


Playtesting of the card was virtually nil—after all, it had different text on it when testing *Betrayers* was a priority. It couldn't use its counters to kill creatures and instead had a different, far less powerful, ability that just didn't fit when it came to typeset the card. So some remnants of the development team made the change that gave it the devastating -1/-1 ability, and playtesting of that card didn't occur.


It would be easy to say, “Well, I did my job and then someone else changed it later,” but the truth is that we should all have each others' backs and always be checking up on what's happening with our cards throughout the entire process. I'm sure all my coworkers agree and have redoubled their own efforts in the months since.


I'd like to think there are no Jittes in *Ravnica* block.


### Set 2: *Saviors of Kamigawa*


**Resolution**: Don't always force the cute answer.



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sasaya,%20Orochi%20Ascendant)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sasaya,%20Orochi%20Ascendant)
This one isn't a big deal, but a nice little lesson for me in any event. While I was reading through the card file for *Saviors* a while back, I came across [Sasaya, Orochi Ascendant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sasaya%2C+Orochi+Ascendant)—one of the rare legendary flip creatures that become enchantments. When flipped, it became a kind of [Coat of Arms](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coat+of+Arms) for lands, and its flip condition (at the time) was, “T: Reveal your hand. If you have seven or more land cards in your hand, CARDNAME.”



I thought it was cool, but that maybe it could be a hair cooler. So I posted, “AF 7/10: Does this guy need 'T' in his activation? Seems neat to just reveal my hand in the middle of combat or whatever...” Other developers agreed with me, and the tap was removed, making “Reveal your hand” the activation cost. Harmless enough.


Of course, after the card had gone to press, either an editor, an online rules guru, or rules manager Mark Gottlieb noticed that this created a problem. You reveal your hand as the cost, then you put your hand back “hidden” once the ability is on the stack. Before the ability resolves, you could theoretically alter the contents of your hand, by cycling, being forced to discard, activating a card like [Scroll Rack](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scroll+Rack), or whatever. Then, when the ability resolves, your hand is hidden but the ability needs to check if you have seven lands in it. Hmmm. The problem was that the card needed to know how many lands were in your hand *on resolution*, at which point your hand was hidden information again. Sounds trivial, but this game needs rock-solid rules to work right.


Had I left well enough alone, the card would have worked just like its predecessors, such as [Scent of Cinder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scent+of+Cinder) and [Nightshade Seer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightshade+Seer). Instead, it either needed errata or the comprehensive rules had to be tweaked. Gottlieb opted for the latter, and it was a very minor tweak indeed. (The most relevant bit is in the glossary under “Reveal”: *“If the cost to play a spell or ability includes revealing a card, the card remains revealed from the time the spell or ability is announced until it leaves the stack.”*)


On top of all that, with the new activation, you sometimes randomly show your opponent your hand on *Magic Online* when you think you're choosing a blocker. Heh. Like I said, not that big a deal, but it goes to show how one little uninformed whim can create extra work and headaches for lots of other people. I now try to do a bit more research into the rules before I propose bizarre solutions.


### Set 3: *Ninth Edition*


**Resolution**: Don't get too caught up in the “rules du juor.”



![](https://media.wizards.com/legacy/global/images/mtgcom_daily_af100_picmain_en.jpg)
The last rerun article of mine that was posted over the holiday break was “[Ninth Time's a Charm: Part 2](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af99),” which went over some of the finer points of the most recent Core Set, including blue's poor showing therein.



I regret some of those choices now, I really do. Not the fact that [Counterspell](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) isn't there, but the fact that some of the decent middle-of-the-road cards like [Spiketail Hatchling](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiketail+Hatchling) and [Curiosity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Curiosity) and [Inspiration](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspiration) are gone. We kind of got caught up in a bit of blue-bashing back then, with a lot of “Blue can't get this,” and “Blue shouldn't have that any more” being bandied about in R&D. We were definitely on the right track with reigning in its tournament power, especially in the control card category, but I think our vicious housecleaning hurt a lot of other more innocuous blue strategies as well. Overall, I don't think *Ninth* is a particularly flattering picture of what blue is capable of, and I honestly expect that to be fixed—at least a little bit—with *Tenth*.


The moral to me is, once we've gone through and implemented all the changes and rules we want to implement, we have to take a step back and say, “Okay, here's what we ended up with. Is this fun? Is this sending the right message?” I think we did a great job of that in *Ravnica* with transmute especially; we knew we had to keep the power level down, but I think we ended up with some neat fun cards that have applications across various formats.


### Set 4: *Ravnica: City of Guilds*


**Resolution**: Don't fall in love with my own ideas.



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mark%20of%20Eviction)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mark%20of%20Eviction)
As a designer *and* a developer, I get put into a few awkward situations from time to time, like, for instance, when a set's lead developer asks me point-blank if I think a card I designed is poorly made. What am I supposed to say? Of course, wearing both hats also puts me in a unique position of being able to defend my own ideas when I think other people aren't seeing the big picture of what my cards are capable of.



The problem arises when I'm passionately defending what turns out to be a bad idea. For instance, I designed [Mark of Eviction](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mark+of+Eviction) really early on in the set's lifespan, before there even was an Aura subtheme introduced. From the very beginning, it cost but a single mana, and I always had a great time winning with the card and coming up with wacky ways to use it. Other developers would always initially undervalue it, and then quickly come around on how potentially powerful it was. Here are some comments from the card in Multiverse:



> 
> bs 7/19: interesting for casual enchantress.  
> 
> MP 7/22: Very neat with/against the CIP enchantments in limited.  
> 
> MT 9/7: Could be powerful. Seems frustrating at the very least.  
> 
> bs 12/2: there have been many calls for an adjustment downward here. should be 1U.  
> 
> MP 12/4: Yep, massively annoying and power level is too high in limited.  
> 
> bs 12/9: should move to uncommon.  
> 
> bs 12/14: now uncommon, should continue testing to make sure this isn't annoying.  
> 
> RB 12/20: I like that this went to UC instead of being downgraded ... it's new, tricky, better than it looks, and best in a good player's hands.  
> 
> bs 12/21: there are still murmurs that this should be downgraded.  
> 
> MJ 12/22: It isn't just this, it is the whole gamut of "don't play creatures" spells. Between this, Fetters, Spawn Broker [which used to exchange creatures based on CMC, not power], Pink Bolt, etc, beatdown doesn't seem to have a chance.  
> 
> Del 1/6: Remember the Auras!  
> 
> bs 1/10: should we downgrade this?  
> 
> bs 1/28: this question stands...
> 
> 
> 


And that's it. Sure, it went from common to uncommon, but it stayed at one mana, almost entirely at my behest and against the better judgment of everyone else involved.


The card is crazy in limited, to the point of being impossibly frustrating to play against. Sure, there are ways to fight it, but it very cheaply and efficiently creates bad redundant game states that sap the enjoyment out of playing (for at least one person). We shouldn't make (many) cards like that, really. It would have done 95% of its job at 1U, and still been relevant to some interesting combos and strategies in both limited and casual play. But because I loved the card too much, it costs one and is creating little pockets of Hell on Earth on a daily basis.


From now on, whenever I'm outnumbered six to one, I'll try to be more objective.


Last year was a busy one, and this year looks to be great (and busy) as well. Let's all hope I can stick to my resolutions! Tune in next week for some saucy *Guildpact* goodies!


### Last Article's Poll:





|  |
| --- |
| **What would you rather get as a gift this holiday season?**  |
| An Unlimited [Mox Emerald](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Emerald) | 3012 | 29.5% |
| A box of *Guildpact* boosters | 2937 | 28.8% |
| Two boxes of *Ravnica* boosters | 2605 | 25.5% |
| An iPod Nano | 1189 | 11.7% |
| Socks and underwear | 463 | 4.5% |
| **Total** | **10206** | **100.0%** |







