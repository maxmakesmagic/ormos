
---
[Link to Wayback Machine](https://web.archive.org/web/20200922022701/https://magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "656816"
[_metadata_:publish_date]:- "2013-07-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Working Your Core"
[_metadata_:wayback_capture_timestamp]:- "2020-09-22 02:27:01"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200922022701id_/https://magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08"
---


Working Your Core
=================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on July 8, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







Often, when a set comes out, I walk through the card set and tell stories about individual cards. But as I just told stories a few weeks ago ("Modern Stories, [Part 1](/en/articles/archive/making-magic/modern-tales-part-1-2013-06-17)" and "[Part 2](/en/articles/archive/making-magic/modern-tales-part-2-2013-06-24)"), I thought I'd do something a little different with my card walkthrough today. I'm going to choose a handful of cards and examine why they're designed the way they are. For each card I examine, I am going to talk about why a certain design decision was made. Hopefully, this will be an insight into how we design.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/2pGfcG5CXG_EN.jpg)
 
### "Why is this a sorcery?"



For starters, if you never read my article on why sorceries exist at all ("Can't all the spells just be instants?"), you might want to take a peek at  [my article from Sorcery Week](/en/articles/archive/making-magic/slow-and-steady-2004-04-19)  back in 2004. For those who don't want to read it, it boils down to "Sorceries are an important game-design tool." This card is a good example.


Originally, this mechanic was in blue. The most famous example was a card called [Ray of Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command).



![2528](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=2528)

 


Stealing was firmly in blue's part of the color pie from the beginning, with cards like Control **Magic** and [Steal Artifact](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steal+Artifact) showing up in Alpha. [Ray of Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) came about as a means to steal a creature temporarily. It was made an instant to allow blue to use it as a defensive trick, where it would steal an attacker to use as a blocker. This allowed one spell to remove two threats (if you did it correctly, you could have the two creatures destroy one another in combat). Interestingly, though, this ability didn't first show up in blue, but rather in red, with this card in *Legends*:


 



![1568](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=1568)

 


In fact, if you look back at early **Magic**, red was clearly number two when it came to stealing things. While blue was flavored as manipulation, red was flavored more as trickery. This all came to a head numerous years later when R&D was attempting to balance the color pie. Red was at the low end while blue was at the high end. I brought up that red had a history of stealing things and that perhaps we should consider moving [Ray of Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) into red. That way, we would separate permanent stealing from temporary stealing. Blue the manipulator was better at permanently stealing something while red, with its ability to manipulate emotions, could control creatures for a shorter duration of time.


 


There was just one problem. [Ray of Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) was much more valuable on defense than offense. Yes, sometimes you would use it to attack, but more often you would sit back and use it to wreck the opponent during an attack. Red is the least defensive color (in the fact that it doesn't focus on being defensive—its direct damage can serve as defense in a pinch) so there was some debate about letting red have [Ray of Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command). The solution, I argued, was easy. If we want red to use it offensively we just had to make it a sorcery. Then that would be the only way to use it.


And that is why [Act of Treason](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Act+of+Treason) is a sorcery.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/9kzcek5tPp_EN.jpg)
 
 



### "Why can't Blood Bairn sacrifice itself to itself?"


Once upon a time, all creatures capable of sacrificing a creature were able to sacrifice themselves. It's just the way we did things. Then, one day, developer [Erik Lauer](http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer) asked the following question: "Is it confusing that creatures could sacrifice themselves for an effect that could never happen?"


We'll take Blood Bairn as an example. The creature sacrifice gives Blood Bairn +2/+2. But that effect will never happen if the creature sacrificed itself. What then is the advantage of allowing it? Well, it allows the creature to destroy itself if somehow that is beneficial (for example, someone is trying to steal it). We decided the minimal upside in corner cases wasn't worth the confusion.


Why is this confusion a problem? Because focus testing has shown us that if a card does something that players don't understand, they start to question if they understand what the card actually does. "Why can I sacrifice a creature if doing so would keep it from being able to get the bonus? Okay, I must have read it wrong."


So R&D drew a line. If the creature can sacrifice itself and generate an effect, then it gets the ability to sacrifice itself, but if that ability is negated by the creature no longer being there (which most often means a bonus to the creature), it now says "sacrifice another creature."



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/i7NoPDb13Y_EN.jpg)
 
 



### "Is that middle ability red?"


The short answer is "it is now."


The longer answer has to do with something known as [Blogatog](http://markrosewater.tumblr.com/). For those who might never visit Tumblr, Blogatog is my daily blog where I answer questions from players. One of the common occurrences on my blog is that players will raise issues which I will then turn back on my audience. One such issue was a concern that red's share of the color pie wasn't as big as the other colors. So I asked if there were things not in red that they felt should be in red.


The players (I call them Question Marks) responded in great volume. One of the ideas that got tossed around was giving red access to more abilities but restricting the duration of how long they could use it. In other words, red could generate effects but only ones that could be used here and now. Red was always in the moment.


I liked this idea because it would allow us to stretch red colorpiewise (I swear that's a word—at least it is now) without having red step on the toes of other colors. Red would get its own take on these effects. The one that came to me first was card drawing. Old timers might remember the card [Elkin Bottle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle).



![2403](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=2403)

 


I was always a huge fan of [Elkin Bottle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) and as I was walking through the idea of short term effects, [Elkin Bottle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) sprung up in my head. Meanwhile, as fates would have it, elsewhere it the pit some R&D folk were trying to figure out how to make Chandra better in **Magic** 2014. This was Chandra's fourth version and they really wanted to make her better than her previous attempts. Chandra has never had a top-tier planeswalker card and she was the face of **Magic** 2014, after all.


 


I made a suggestion of the "use it or lose it" card-drawing ability. I explained how I was trying to help red and everyone liked the suggestion, so in it went.


Is this the last we're going to see of this effect in red? Nope.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/QTdxo5Lqx6_EN.jpg)
 
 



### "Why doesn't this target players?"


If you want the long version, I would go read [this](/en/node/654896) and [this](/en/node/644866). The short version is this: Whenever we design a card for the core set we try to figure out what the simplest, easiest-to-[grok](http://www.merriam-webster.com/dictionary/grok) version of the card is. Note that when we design for expert expansions, how the card fits into the larger environment of the set takes precedence.


A big part of doing this is questioning every single word on the card and asking what value that word adds. So, of course, when this card was being design for **Magic** 2010, the words "Target player" was put under a microscope.


There was much debate as to whether the words added complexity. The anti-"Target player" contingent argued that "Draw two cards" is just simpler and easier to understand than "Target player draws two cards." The pro-"Target player" contingent argued that just as players got that "CARDNAME deals 3 damage to target creature or player" made sense so too did the card draw. The player, they argued (if you didn't read the linked article, I'm on this side) would assume the card did what you would want it to do—direct damage to the opponent and card draw for you.


In the end, the simplicity argument won and the card was made with three words of rules text rather than five.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/wXxy3qT07L_EN.jpg)
 
 



### "Why can you only activate this once?"


[Rootwalla](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla) first showed up in *Tempest* design. It was created by [Mike Elliott](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mike%20Elliott) and was called Chuckwalla—which, by the way, happens to be [an actual type of lizard](http://en.wikipedia.org/wiki/Chuckwalla). Interesting side note—the card was supposed to be called Chuckwalla but the artist assumed it was a made-up creature and thus didn't draw a chuckwalla. The name was then changed to [Rootwalla](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla).


Mike was playing around with the idea of a creature with a built-in [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). He restricted it to one use because the creature wasn't supposed to be a shade or a firebreather (i.e., something that could be used repeatedly) but rather as something that was meant as a one-shot ability. The card did a nice job of giving green an ability that made use of mana to change size in a way that didn't step on the toes of any other color. It worked so well that the "[Rootwalla](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla) ability" became an evergreen, although unnamed, ability.


One of the most important roles of the color pie is to help the colors each have a delineated feel. That means that R&D spends a lot of time splitting hairs and making subtle divisions between the colors. White can pump its toughness (although it doesn't to it often these days), blue can get +N/-N or -N/+N, black can pump its shades (pumping power and toughness), red can have firebreathing, and green gets the rootwalla ability.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/rGjI23bveW_EN.jpg)
 
 



### "Why does this card specify 'non-Demon?'"


The whole "non-Demon" thing started in *Dissension* on a card called [Rakdos the Defiler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+the+Defiler).



![107438](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=107438)

 


Rakdos originally sacrificed half of your permanents when he attacked and made your opponent sacrifice half of his or her permanents when he dealt combat damage to him or her. The problem was that you were always behind because you always had to sacrifice your half of the permanents before your opponent—and that only happened if you managed to deal combat damage to him or her (well, it was a 7/6 flier with trample, so it did happen most of the time).


 


My solution to tip the scales was to have you sacrifice half of your "non-Demon" permanents. I felt it was flavorful, encouraged you to have other Demons in your deck, and solved the problem by only having to add one word to the rules text. The rest of the design team liked it and the change was made.



![Reaper from the Abyss](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reaper+from+the+Abyss)

 


Flash forward to *Innistrad*. During a playtest, I play a [Reaper from the Abyss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+from+the+Abyss). I attacked each turn, my opponent chump blocked (he had a lot of fliers), and then I killed a second creature. This happens until he had only one creature left. I attack, he blocked, and then the following dialogue occurred:


 



> 
> **Him:** Kill your demon.  
> **Me:** What?  
> **Him:** My guy died so you have to kill a creature.  
> **Me:** Yeah, but why would a demon kill himself?  
> **Him:** I don't know. He's depressed there's no one left to kill.  
> **Me:** That doesn't make any sense.  
> **Him:** I don't care. It's what the card says.
> 
> 
> 


I then take out my pen, remembering Rakdos, and wrote "non-Demon" on it.



> 
> **Him:** You can't do that.  
> **Me:** I redesigned him while the effect was on the stack.
> 
> 
> 


Which brings us to Shadowborn Demon. Once we in R&D learn a trick, we tend to repeat it, and the "non-Demon" rider has been well received and has played well, so once again it got used.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/YFDYStzhGw_EN.jpg)
 
 



### "Why aren't the three abilities closer in power?"


The easiest way to think about the power level of activated abilities is to figure out what each would cost if you simply cast it. A 3/3 token can be done for ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Putting three +1/+1 counters on a creature costs somewhere between ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) and ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Gaining 3 life is worth ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Why the discrepancy?


The answer is twofold. First, one of the thing that makes cards with some randomness fun is that there is some variance. With Primeval Bounty in play, each draw becomes a moment of focus. Having a range of what you can expect heightens this suspense. Note that all the effects are good, so you are seeing how much goodness you get rather than fearing something bad happening. (I talk about this concept a lot more in my article on randomness ("[Kind Acts of Randomness](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/37)").


Second is the importance of aesthetics. For those who have never heard of aesthetics, it is a scientific study of how the brain perceives things. I've heard it also called the "science of beauty." (For more on it, I talk about aesthetics in my article "[Zen and the Art of Cycle Maintenance](/en/articles/archive/making-magic/zen-and-art-cycle-maintenance-2002-07-08).") The human brain finds certain patterns pleasing and, using aesthetics, a designer can make a card more pleasing to the players in ways they might not even be conscious of. A common technique is to reuse the same number multiple times.


The three abilities of Primeval Bounty all use the number three. They might not match in power but the fact that each ability (and it helps that there are exactly three) uses three in some way makes the card more pleasing, subconsciously. Note that a lack of aesthetics will have the opposite effect. This card is the perfect example:



![Griselbrand](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Griselbrand)

 


The fact that [Griselbrand](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Griselbrand) has a converted mana cost of eight despite all the 7s in his rules text upset a lot of players.


 



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/xlW1texjFv_EN.jpg)
 
 



### Why does Ratchet Bomb say "equal to" rather than "equal to or less?"


[Ratchet Bomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ratchet+Bomb) is a redone version of a card called [Powder Keg](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) from *Urza's Destiny*.



![Powder Keg](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Powder+Keg)

 


This means the real question is why did [Powder Keg](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) say "equal to" rather than "equal to or less?" The answer is the "equal to" creates better game play. Let's examine each version to see what happens. We'll start with the "equal to or less" text.


 


What do you do each turn? You add a counter. Why? Because adding a counter is strictly superior to not adding one. It merely allows you to destroy yet another subset of cards. This means there's never any decision to whether or not to add a counter.


Now let's look at the "equal to" text. What do you do each turn? Well, that depends on how many counters are on the [Powder Keg](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) and what other permanents are in play. With this version, there's no automatic answer. It also allows your opponent some play as well, because if he or she can goad you into adding a counter, he or she can then play any item with a permanent with a lower converted mana cost.


It's interesting to note when I designed [Powder Keg](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) in *Urza's Destiny*, I had this exact fight with another designer, Mike Elliott. Luckily, the development team agreed that my version led to more interesting game play.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/l5lB2T0CQv_EN.jpg)
 
 



### Why doesn't this Sliver grant abilities to other Slivers?


This card is a tweak of the card [Metallic Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metallic+Sliver) from *Tempest*.



![4617](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=4617)

 


That card, by the way, was supposed to be called Silver Sliver, but the art came back and the creature was more of a bronze color than silver, so we had to change the name.


 


Anyway, the reason neither [Metallic Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metallic+Sliver) nor Sliver Construct grant abilities to other Slivers is that they are not actually Slivers. Rather, they are both constructs built to resemble Slivers. (The one in *Tempest* was built by Volrath, for those who remember their **Magic** villains of days gone by.) This allows them to fool the Slivers and take abilities, but they are incapable of sharing with the Sliver hive mind.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/T7nzQkbcaA_EN.jpg)
 
 



### Is this supposed to be a white ability or a blue ability?


White is the color of delay. Putting a creature on top of its owner's library is a nice simple way to remove the creature for the game for a full turn (and sometimes longer). Blue is the color of bounce (i.e., returning something back to its owner's hand). Putting a creature on top of the library is basically a super-[Unsummon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon). Both feel right, but R&D was unhappy with the overlap. It wasn't the kind of ability used often enough to have it occur in two different colors. Thus, the topic was brought to Card Crafting.


Card Crafting is a weekly meeting where core designers, developers, and creative folk gather to talk technical issues. The fate of "put target creature on top of its owner's library" is exactly the type of topic we talk about each week.


The pro-white camp argued that blue already has [Unsummon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon). Why don't we split up the effects (blue gets return to hand while white gets return to top of library) so that we can create more nuance with the effect?


The pro-blue camp said that the ability felt awkward in white and that the delaying flavor was simply less apparent than the super-[Unsummon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon) flavor. The pro-blue camp also argued that white has numerous other ways to delay creatures and didn't need the mechanical space.


We spent Card Crafting working it out and in the end decided that we didn't want to chop up the effects and that "put target creature on top of its owner's library" simply felt more blue than white.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/m14/poi798sjkasd/nLeu1AwWJq_EN.jpg)
 
 



### Why does this round down instead of up?


I designed this card during *Odyssey*. The block had a strong graveyard theme, which tends to naturally push design to include a milling theme, as it helps get cards into graveyards. I was trying to make a super-milling card but I also wanted to make sure that the spell didn't make it too easy to mill out the opponent.


For those who don't know this, I'm a bit of a puzzle fan. [Traumatize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traumatize) was inspired by a riddle. A scientist invents a radical new invention, a super car. You put in your end destination and in ten second it takes you exactly halfway. Assuming you are trying to travel 3,000 miles, how long will it take you?


I'll let you think about it for a second before giving you the answer.


See the answer


>> Click to Show
The answer is an infinite amount of time because you'll never get there. As you keep going half way, you never complete the journey. This riddle gave me the solution to my problem. If I mill half of your deck, the spell is never going to mill you out. It will keep getting the player closer but by itself it cannot win.


That's why I made it round down—so that this card would never be the one that mills out your opponent. Your opponent will always have to draw the last card him- or herself.



 


### You're My Only Hope


 


Before I sign off for today, I have a personal request to make of all of you. Please watch the video below.





![](https://web.archive.org/web/20220216050541im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/img/interface/video-place-holder.png)[.](http://www.youtube.com/v/x7khnFuv66A&hl=en&fs=1&rel=0)





I appreciate any help you can provide me in my quest. Thanks.


### "Why? Because We Like You"


 That's all the time I have for today. I hope you enjoyed this peek into some of the reasons behind how the cards work the way they do. As always, I'd love to hear your feedback through my email, the thread of this column or any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)). 


 Join me next week for the six-hundredth week of Making **Magic**. 


Until then, may you take the time to think about why your cards work as they do.

   


---

  
###  Drive to Work #41 – *Mirage*, Part 1


 Today I start talking about the design and development (but more the development) of the first set of the very first modern block, *Mirage*. 


  
* [**Episode 41**](http://media.wizards.com/podcasts/magic/drivetowork41mirage1.mp3) : *Mirage, Part 1* (11.1 MB)
* [**Episode 40**](http://media.wizards.com/podcasts/magic/drivetowork40wizardsofthecoast.mp3) : *Wizards of the Coast* (14.9 MB)
* [**Episode 39**](http://media.wizards.com/podcasts/magic/http://media.wizards.com/podcasts/magic/drivetowork39randomness.mp3) : *Randomness* (13.9 MB)
* [**Episode 38**](http://media.wizards.com/podcasts/magic/drivetowork38unglued2.mp3) : *Unglued 2* (10.6 MB)
* [**Episode 37**](http://media.wizards.com/podcasts/magic/drivetowork37lessonslearned3.mp3) : *Lessons I've Learned, Part 3* (10.5 MB)

### So You Want To Work At Wizards


Many years ago I started posting job searches at the end of my column. You all liked the chance to see potential jobs at Wizards. We liked that it proved to be a good way to find qualified candidates, so I've chosen to keep doing them.


 Today, we're looking for a senior coordinator for **Magic: The Gathering**. The requirements are: 


* Bachelors in Graphic Design or other visual communication field (or equivalent experience) highly desired.
* Experience with Word, Excel preferred.
* Experience with InDesign preferred.
* Familiar with Adobe CS5 preferred (minimally Photoshop CS4)
* Familiar with FileMaker Pro preferred.

And asks for the following knowledge, skills, and abilities:


* Must be detail-oriented
* Strong communication skills required
* Print production knowledge highly desired
* Able to adapt to quickly changing environment
* Ability to work effectively with diverse groups of people
* Ability to multitask
* Participate in gaming environments

 If you think that sounds like you, see the full job listing [here](http://company.wizards.com/about/careers/sr-coordinator-art-administration-job-renton-wa-us?careers-view=1). 


   
 






