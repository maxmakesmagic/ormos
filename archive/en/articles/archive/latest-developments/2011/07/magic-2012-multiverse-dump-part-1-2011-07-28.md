
---
[Link to Wayback Machine](https://web.archive.org/web/20220629192039/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "It's been a while since I've done a Multiverse article. Conveniently, it's also been a while since I knew a Multiverse file as well as I know the file for Magic 2012, as I was the set's lead developer. Let's do this.For those of you who haven't been around for a while, Multiverse is the database we use to build Magic sets. While much of it is administrative and used to handle"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "192746"
[_metadata_:path_date]:- "2011-07-28"
[_metadata_:publish_date]:- "2011-07-29"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Magic 2012 Multiverse Dump, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2022-06-29 19:20:39"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220629192039id_/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28"
---


The Magic 2012 Multiverse Dump, Part 1
======================================



 Posted in **Latest Developments**
 on July 29, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






It's been a while since I've done a Multiverse article. Conveniently, it's also been a while since I knew a Multiverse file as well as I know the file for ***Magic** 2012*, as I was the set's lead developer. Let's do this.

For those of you who haven't been around for a while, Multiverse is the database we use to build **Magic** sets. While much of it is administrative and used to handle things like art credits, collector numbers, and so on, we also use it to control card texts, and it has space for us to use to communicate with each other. Everything you see in monospace in this article came directly from internal communications that took place during ***Magic** 2012* design and development.

Here's your cast of characters for today.


> AF: Aaron Forsythe, Director of **Magic** Ramp;D and ***Magic** 2012* design team member  
>  DB: Doug Beyer, ***Magic** 2012* design team member  
>  Del: Del Laugel, **Magic** senior editor  
>  DH: Dave Humpherys, ***Magic** 2012* development team member  
>  KD: Kelly Digges, ***Magic** 2012* development team member  
>  KEN: Ken Nagle, ***Magic** 2012* design team member  
>  MJ: Mons Johnson, **Magic** playtester  
>  MR: Mark Rosewater, **Magic** head designer  
>  MT: Mike Turian, ***Magic** 2012* development team member  
>  PAS: Peter Schaefer, ***Magic** 201*2 development team member  
>  Tabak: Matt Tabak, **Magic** editor  
>  TML: Tom LaPille, ***Magic** 2012* lead developer
> 
> 

![](https://media.wizards.com/images/magic/daily/ld/ld153_card01a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld153_card01b.jpg)***Magic** 2012* lead designer Mark Globus created an aura subtheme in ***Magic** 2012*. He was also bored with [Holy Strength](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) and [Unholy Strength](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength), and his design handoff included a more powerful and splashy pair of cards to replace them. The design handoff version of this card, though, gained you only 1 life when it entered the battlefield, to mirror [Dark Favor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor)'s 1 life loss, and gave a bonus of +1/+4 to mirror [Dark Favor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor)'s +4/+1. Power is stronger than toughness, so I thought this card needed a little more juice.


> TML 4/14/2010: We want these cards to be better. Four life instead of one!  
>  KD 4/23: Much more appealing, both power-wise and aesthetically.  
>  MR 7/06/10: If you care about aesthetics, the life should be the combination of the power and toughness.  
>  AF 7/19: I didn't realize aesthetics had such well-defined answers.  
>  KEN 8/2/2010: This card is 3.4 milliHelens beautiful.  
>  TML 8/3/2010: Excellent choice of unit. Also, now less good.
> 
> 

[Dark Favor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor) proved too good at +4/+1, so I moved it to +3/+1 instead. [Divine Favor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Favor) had to change to match it, so it went back down to +1/+3 and 3 life, where we printed it.

![](https://media.wizards.com/images/magic/daily/ld/ld153_darkFavor.jpg)  
![](https://media.wizards.com/images/magic/daily/ld/ld153_card02a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld153_card02b.jpg)[Grand Abolisher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grand+Abolisher)'s intent was never in question. However, its actual words changed quite a bit. Here's where it started:


> During your turn, your opponents can't cast spells or activate abilities.
> 
> 

This is pretty weird for **Magic**, though, as it would keep you from even tapping your lands for mana. We normally get around this by excluding "mana abilities," which according to the rules means "nontargeted abilities that add mana to your mana pool." To match up with precedent, I changed it to this:


> During your turn, your opponents can't cast spells or activate abilities that aren't mana abilities.
> 
> 

Then, I found myself wondering something.


> TML 6/16/2010: Is there any good reason to exclude mana abilities from this? Is someone casting [Fade Away](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fade+Away) or something? Some people think "mana abilities" are any abilities that cost mana, which makes this card read worse to them.
> 
> 

I'm not a big fan of forcing people to look up the comprehensive rules, nor am I a fan of questions with bizarre answers. For example, have a look at these two cards:



|  |  |
| --- | --- |
|  |  |

One of these two cards has a mana ability. Do you know which one? I ran a straw poll among less-experienced **Magic** players in the building, and many of them either got it wrong or told me they had no idea.

Del Laugel, our crack senior editor, was ready with an astute and terrifying answer.


> Del 9/3: Shutting off mana abilities means that we'll need to consider this card when templating all future cards with buyout clauses ([Shrouded Serpent](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shrouded+Serpent)), triggered abilities that have mana stuck in for dev reasons ([Azorius Æthermage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+%C3%86thermage)), and triggered abilities that behave like do-this-once activated abilities ([Electropotence](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Electropotence)). I'm not saying the card can't stay as it is; I'm just saying that it will receive a lot of attention during templating if it's handed off like this.
> 
> 

Attention from the templating team is a little scary, as it means that your cards are liable to change under your feet. In classic **Magic** developer tradition, I just changed my card to dodge the issue instead. It now turns off mana artifacts, but leaves lands—the most likely source of mana—alone.

![](https://media.wizards.com/images/magic/daily/ld/ld153_card03a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld153_card03b.jpg)[Phantasmal Bear](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Bear) started out life the same way it was printed.


> DB 3/8/2010: Don't poke the bear!  
>  KD 4/6: In the old days this would've cost 1U. The old days sucked.  
>  PAS 4/12: Love this theme.
> 
> 

While the Bear was cute, I was interested in doing a little more color pie pushing. Each Illusion creature in the file was designed to match a non-Illusion creature elsewhere in the file; what if one of the illusions was a version of a card that blue didn't normally get? I saw [Youthful Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) in white and got an interesting idea.

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld153_mortallity2.jpg)  

> TML 4/14/2010: Was U 2/2. Trying crazier U 2/1 first strike for more color bleeding.
> 
> 

This caused some consternation. What was I doing with a blue first-striker? Why did it win in combat against everything? What is going on here? There was some amount of unhappiness about this, but a larger amount of bewilderment.

Eventually, though, [Youthful Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) made its way out of the set on its own, which made this particular Illusion Knight look particularly out of place. I changed it back to the Bear, and everyone was happy.


> TML 5/14/2010: Back to bear. No one cared that it was a knight, and [Youthful Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) is gone.
> 
> 

Well, almost everyone. Some people still had issues, but I just pretended to not know what they were talking about.


> MJ 6/10: strange that blue gets a 2 power 1 drop, but green doesn't.  
>  TML 6/16/2010: What two power one drop? I don't see anything... :)
> 
> 

![](https://media.wizards.com/images/magic/daily/ld/ld153_card04a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld153_card04b.jpg)[Chasm Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chasm+Drake), to you, likely looks like just another **Magic** card. When I look at it, I groan a little inside, as it was the common in the set that I struggled the most with.

***Magic** 2012* lead designer Mark Globus was interested in including fantasy tropes that took more than one card into the set. You can see that theme in cards like the Empires artifacts and the pairing of [Arachnus Spinner](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arachnus+Spinner) and [Arachnus Web](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arachnus+Web). One card that didn't make it was an artifact, flavored to be a magic lamp, that interacted with Djinn creatures. I fell in love with this idea, and made a common Djinn, a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) 3/3 flier, to support it. I was rather proud of the mechanic I came up with, which despite being reasonable for common still did a reasonable job of getting Djinn flavor across. Then, I discovered that we don't make common Djinns.


> TML 4/14/2010: Knight is already a bloodthirst enabler, and we need a real flying creature. Was [Zephyr Sprite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zephyr+Sprite). Made a good flyer and a djinn for the Lamp.  
>  TML 4/14/2010: Note that creative is not in love with djinns. We should figure out how much we like the lamp.  
>  EVL 5/2: Fun  
>  TML 5/3/2010: This won't be a djinn, but it can maybe stay this. I like this!  
>  Del 6/1: Should this card wait for the Djinn set to come rather than become "smart pudgy bird" or "baby sphinx"?
> 
> 

I decided that the answer to Del's question was yes—this mechanic worked well enough on a common Djinn that it could wait for a time when it could be one—and looked for a new card. I struggled for a few weeks to find an ability for a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) 3/3 flier until Erik suggested that I look for underplayed color combinations in Limited. This showed me that green-blue was not being played as much as the others. We engineered [Chasm Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chasm+Drake) to be good friends with [Vastwood Gorger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vastwood+Gorger), the lamp became [Quicksilver Amulet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quicksilver+Amulet), and the rest is history.


> TML 6/4/2010: This ability will change. I don't know what to.  
>  TML 6/11/2010: New line of text. Would like a drake here.
> 
> 

Dave Humpherys later pointed out that this card could swoop onto an opponent's side of the board and take out an illusion, which is an unfortunate interaction.


> DH 8/13: Add 'you control' to save the bears (illusions).  
>  TML 8/17/2010: Bears saved.
> 
> 

This being **Magic** Ramp;D, though, we couldn't stop without one final snarky comment.


> Tabak 11/30: I just want to go on record as hating the Bears, but I'll let this go.
> 
> 

![](https://media.wizards.com/images/magic/daily/ld/ld153_card05a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld153_card05b.jpg)Three Ramp;D members disagree.


> MT 3/8: Still think this guy could be busted.  
>  KEN 3/9/2010: I didn't enjoy this card the first time.  
>  DB 3/10/2010: The perfect top-down Skeleton.
> 
> 

Three Ramp;D members disagree.

![](https://media.wizards.com/images/magic/daily/stf/stf153_footer.jpg)  
Okay, I'm out of time. There's more where this came from, though, so I'll be back to it later this summer.

Last Week's Polls


|  |
| --- |
|  **Are you happy that the Titans are in *Magic 2012*?**  |
| Yes | 631 | 54.6% |
| No | 381 | 33.0% |
| I have no opinion. | 144 | 12.5% |
| **Total** | **1156** | **100.0%** |

  


|  |
| --- |
|  **Are you happy that [Glacial Fortress](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Fortress) and friends are in ***Magic** 2012*?** |
| Yes | 851 | 68.2% |
| No | 280 | 22.4% |
| I have no opinion. | 117 | 9.4% |
| **Total** | **1248** | **100.0%** |

  
This Week's Poll
**Which Ramp;D member do you agree with most about [Reassembling Skeleton](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reassembling+Skeleton)?**Mike Turian: Still think this guy could be busted.Ken Nagle: I didn't enjoy this card the first time.Doug Beyer: The perfect top-down Skeleton.  


---

![](https://media.wizards.com/legacy//mtg/images/daily/features/M12_ArticleFooter_MTGO_top_ver1.jpg)[![](https://media.wizards.com/legacy//mtg/images/daily/features/M12_ArticleFooter_MTGO_button_Static.jpg)](http://archive.wizards.com/magic/Digital/MagicOnline.aspx)![](https://media.wizards.com/legacy//mtg/images/daily/features/M12_ArticleFooter_MTGO_BottomRight_ver1.jpg)





