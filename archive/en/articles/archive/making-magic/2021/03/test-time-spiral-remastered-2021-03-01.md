
---
[Link to Wayback Machine](https://web.archive.org/web/20210302124122/https://magic.wizards.com/en/articles/archive/making-magic/test-time-spiral-remastered-2021-03-01?utm_source=dlvr.it&utm_medium=twitter)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Where did Time Spiral Remastered come from? Mark Rosewater shares the story—and a few preview cards—behind a return to Magic from 15 years ago."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1528394"
[_metadata_:publish_date]:- "2021-03-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Test of Time Spiral Remastered"
[_metadata_:wayback_capture_timestamp]:- "2021-03-02 12:41:22"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210302124122id_/https://magic.wizards.com/en/articles/archive/making-magic/test-time-spiral-remastered-2021-03-01?utm_source=dlvr.it&utm_medium=twitter"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/test-time-spiral-remastered-2021-03-01?utm_source=dlvr.it&utm_medium=twitter"
---


The Test of Time Spiral Remastered
==================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on March 1, 2021 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to *Time Spiral Remastered* previews! I'm going to walk you through the story of how this product came to be and then show off a few cards from the set. Hope that sounds fun.


Remaster the Possibilities
==========================


Our story begins back in 2014. *Magic Online* had a problem it was trying to solve. Players tend to run through content faster in digital than tabletop because it's much easier to get in a lot of games digitally. *Magic Online* was therefore looking to create some additional content. This desire came with a lot of parameters, but the biggest one was that it couldn't create any new cards. The new content had to come from using cards already programmed. How exactly could they do that?


The solution they came up with was to take three sets from an old block (this was back when three-set blocks were the norm) and boil them down into a new large set that would do a few things:


1. It would capture the essence of the block.
2. It would be a fun Limited experience.
3. It would let players get access to cards they were interested in having.

After much searching, they decided the block they would use was *Tempest* (aka *Tempest*, *Stronghold*, and *Exodus*). While I wasn't part of the design team for that product, they did come and talk to me because I'd been the lead designer for *Tempest* (my very first design lead) and had been on the design teams for *Stronghold* and *Exodus*. *Tempest Remastered* was released on *Magic Online* in 2015. Years later, *Magic*: *The Gathering Arena* had a similar issue and chose to make *Amonkhet Remastered* and *Kaladesh Remastered*, released in 2020.


A couple of years ago, Gavin Verhey was put in charge of coming up with new ideas for supplemental sets in tabletop. One germ of an idea came from a frequent piece of feedback he got from players. Why don't we reprint old Draft environments in their entirety so that players can draft that environment again? Gavin was trying to figure out how to make this happen.


Meanwhile, we'd started a project, codenamed "Canoe," where a bunch of designers (myself included) would meet once a week for two months to spitball big-picture design ideas for the future. One of the ideas that came out of this project was "redo a set." I think the impetus was to take a set that we felt wasn't as successful as it could have been and take a second attempt at it with all our modern tools.


Gavin ended up combining these two ideas into one (revisit an old set, but update it in some way), at which point he realized that he had stumbled onto what *Tempest Remastered* had done. By taking all the cards of a block and condensing the block down to a single draftable set, you got to revisit highlights of old drafts while reconfiguring in a way that could take advantage of modern design tools. (I should note that this happened before *Amonkhet Remastered* and *Kaladesh Remastered*—the different timelines just resulted in those two products releasing before *Time Spiral Remastered*.) It was time for tabletop to make a *Remastered* set.


The one big question remaining: which block should they use? Ideally, Gavin wanted a three-set block, as that gave the designers the most room to maneuver and build something new. Remember, *Remastered* sets can't create new cards, they can only make use of cards that were already part of the block. They also normally can't add in old cards that weren't part of that block, but as you'll see, the *Time Spiral Remastered* design team figured out a way around that. Gavin came up with a list of five candidates (I'm not allowed to tell you what the runners-up were, as they're the most likely choices for the next *Remastered* product if *Time Spiral Remastered* is successful) and started asking around The Pit for people's preferences. To give you a sense of how that went, here's a conversation Gavin told me about having with product architect Mark Heggen.


**Gavin**: I have one more for you.


**Mark Heggen**: Okay, but it's going to be hard to top the last one—I already gave that a five out of five.


**Gavin**: What about *Time Spiral* block?


**Mark Heggen**: I give that one million out of five. I don't know if it is right or makes sense, but I love it, and it's so wacky to put it all in one place that it sounds amazing.


Of the five sets Gavin asked about, *Time Spiral* block was far and away the first choice. It was a popular Draft environment with the enfranchised player base. It was the most complex Standard-legal Draft environment we'd ever built. *Modern Horizons* had shown us that there was an audience for more supplemental sets with complex Draft environments. (Remember the whole idea was pitched as *Time Spiral 2*.) The denseness of the sets would also give the designers more options of how to refine it. Finally, it had a lot of individual cards played in numerous formats that we knew players would be happy to see reprinted. It was decided. The set would be *Time Spiral Remastered*.


It's About *Time*
=================


The set was codenamed "Project Cupcake" (I'm guessing because it was such a decadent product), and Ben Hayes was made the lead designer. His design team was Reggie Valk, Megan Smith, JC Tao, and Chris Mooney. The first thing they had to do was wrestle the three-set block down to a single large set. Not counting basic lands or timeshifted reprints, the block had 626 cards in it. (*Planar Chaos* and *Future Sight*'s timeshifted cards were counted, as they were all new designs to the block.) *Time Spiral* had 281 cards (121 commons, 80 uncommons, and 80 rares). *Planar Chaos* had 165 cards (60 commons, 55 uncommons, and 50 rares). *Future Sight* had 180 cards (60 commons, 60 uncommons, and 60 rares). Remember, the mythic rare rarity didn't premiere until two years later with *Shards of Alara*.


All of that had to be whittled down to roughly the size of a normal large set, meaning over half the cards would have to be removed. (*Time Spiral* Remastered ended up having 289 cards.) The first thing the design team did was pull out all of the chaff. *Time Spiral* came out fifteen years ago and was designed using a lot of older design technology. That meant there were a bunch of cards that weren't really pulling their weight in both Limited and Constructed. According to Ben, that initial culling got them "a surprising amount of the way there."


Once the chaff had been removed, the next thing to do was record what all the Limited themes were for each color. The team then looked through the themes and figured out which were the most supported and which seemed the most fun. In general, it was clear which themes the team had to work with. Cards that didn't match any of the themes became candidates for elimination. At common and uncommon, unless the card was particularly iconic, it got pulled from the set. Rares were decided more on a case-by-case basis, as rares have less of an impact on Limited environments, so their impact and/or desire for Constructed formats had a larger influence on whether they were removed.


The next big thing to tackle was Slivers. There were 43 new Slivers introduced in *Time Spiral* block. They showed up in all five colors, often in cycles. For early playtests, the design team left in all the Slivers. This created some issues. First, *Time Spiral* block's Slivers were created back when all the Slivers were symmetrical, meaning each Sliver boosted all Slivers on the battlefield, not just your Slivers. This added significant complexity to Limited environments and created a lot of feel-bad moments where Sliver decks were boosting players who ran individual Slivers to fill out their decks. Second, the sheer number of Slivers and their constant presence in every color was making too many games feel similar. Third, their sheer number was forcing a lot of other cool stuff to get forced out. The solution was to cut back significantly on them (there are 25 in the set) and restrict Slivers to the colors that they felt led to the best gameplay in Limited. That ended up being red, green, and white (there are some multicolor Slivers that have blue and/or black in them).


The next issue was to see which cards caused problems for Limited in original *Time Spiral* block. The general philosophy was not to sand off the rough edges too much. Part of the fun of *Time Spiral* block included some of the crazy cards you could get in Limited. One card in particular needed some attention. If you ever drafted full set *Time Spiral* block, you know which card I'm talking about.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sprout+Swarm)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sprout+Swarm)
[Sprout Swarm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sprout+Swarm) was a common creature from *Future Sight*. It was one of our mix-and-match cards that took nonevergreen named keywords that hadn't appeared in the same block and put them together. Convoke and buyback seemed like they would work well together (because buyback is an additional cost you can pay for with convoke), so I put them together on a card. It seemed cute and innocent when I designed it. The card would later go on to be a major problem in Draft, as it was near impossible to beat once it got going. (Once you created enough Saproling creature tokens, they started generating new creatures without any need for mana.)


The design team tried moving the card to uncommon, but it was still causing problems. They then moved the card to rare. It was still causing problems. They considered mythic rare but realized that it was causing more problems than it was worth and chose to pull it from the set.


The design team made two other decisions. First, they chose to put all the cards into the current frame. The timeshifted cards from *Planar Chaos* and *Future Sight* each had their own frame (which I explain below), respectively, but understanding what each frame meant got confusing outside the context of their original sets. This does mean there are some cards appearing in the modern booster frame for the first time. (And yes, we'll be getting to the old booster frame in the next section.)


The other decision related to the color pie. *Time Spiral* block is famous for messing with the color pie. *Time Spiral*, for example, has numerous cards referencing abilities that used to be in certain colors but no longer were. *Planar Chaos* had an alternate-reality theme where the color pie was executed differently. *Future Sight* teased possible future executions of the color pie, some of which never came to pass. The design team talked about whether it was okay to include those cards. In the end, they decided that the color pie craziness was part of the fun of original *Time Spiral* block and left it in. (I'll note that because they're all reprints, no format is getting cards that they didn't previously already have access to, so no further damage to the color pie is happening.)


There were many playtests and lots of tweaking, but they ended up with the 289-card set that you will all have a chance to play. If you never got to experience original *Time Spiral* block, you're in for a treat. And if you have, you're also in for a treat, because we've used modern design technology to make it even better.


But wait, there's more.


Getting a Bonus
===============


There's one other thing the original *Time Spiral* block is known for. It was the first time we ever used a bonus sheet (aka an extra sheet of cards that get dropped into a booster, usually in a single slot, to add variety to the gameplay). For the block, we called it a timeshifted sheet. Here's how it worked:


In *Time Spiral*, there was a timeshifted sheet of 121 cards of old reprints printed in the original *Magic* frame. *Magic*'s frame changed for the first time in *Eighth Edition*, and every card reprinted on the *Time Spiral* sheet was from before that change. The bonus sheet had one slot in each booster and had a purple expansion symbol (instead of black, silver, or gold).


In *Planar Chaos*, there was a timeshifted sheet of 45 cards, all reprints from the past that had been colorshifted into a new color that had never had that card effect before. *Planar Chaos*'s flavor is that it's an alternate-reality present where the color pie had been allocated differently (yet still follows the same philosophies of the colors). The timeshifted cards represent "reprints" from this alternate reality. Because these were new cards, they showed up at a higher rate than Time Spiral's timeshifted cards. Each booster pack had three common timeshifted cards and one uncommon or rare timeshifted card. They each had a new frame that was sort of a what-if of the *Eighth Edition* card frame redesign.


In *Future Sight*, there was a timeshifted sheet of 81 cards, all "pre-prints," that is, cards "reprinted" from possible futures showing off mechanics, themes, and creative elements *Magic* had not yet seen. A bunch of these cards later "premiered" in future sets. (You can read these articles to learn more about these futureshifted cards and which ones have shown up again—[Part 1](https://magic.wizards.com/en/articles/archive/making-magic/back-future-sight-2020-08-03), [Part 2](https://magic.wizards.com/en/articles/archive/making-magic/back-future-sight-part-2-2020-08-10), and [Part 3](https://magic.wizards.com/en/articles/archive/making-magic/back-future-sight-part-3-2020-08-24).) The futureshifted cards were mixed in with the regular cards in the boosters. You could get anywhere from five to ten of them in a single booster. These cards had a futuristic frame.


The design team knew that they had to have a timeshifted sheet because it was so iconic to the block, but the big question was, what do we put on it? Just reprinting any of the previous timeshifted sheets didn't feel right, so they decided to do something a little bolder. What if the timeshifted cards came from the future, but not our future like Future Sight's timeshifted sheet, rather the future of *Time Spiral* block. Fifteen years had gone by, so there were a lot of cards we could reprint.


To add a little extra excitement and play into the alternate-frame flavor of the original timeshifted cards, what if all the cards appeared in the original *Magic* frame as the timeshifted cards did on the *Time Spiral* timeshifted sheet? Because all these cards first appeared between 2006 and 2020, they would be appearing in the old border for the first time.


![Mystic Confluence](https://media.wizards.com/2021/tsr/en_PvvrBM72hV.png)![Restoration Angel](https://media.wizards.com/2021/tsr/en_LYYdzyrByT.png)![Treasure Cruise](https://media.wizards.com/2021/tsr/en_ZoyAL4UFnQ.png)


The big challenge for the design team was considering what would be on the timeshifted sheet. Like *Time Spiral*, they decided to do a full sheet of cards, which meant they got to include 121 different cards. Here are the things they cared about when choosing the cards:


* **Is it from *Time Spiral* block's future?**

Every card has to have be a new card released after *Time Spiral* block.


* **Is it currently played in a format?**

The design team looked at all the most played formats (Commander, Modern, Pioneer, etc.) and picked cards that clearly a lot of players would like to own.


* **Is it a popular commander?**

The design team prioritized popular commanders.


* **Did it play well with the Limited themes?**

Showing up in every booster meant these cards would see some Limited play. When picking out cards for the timeshifted sheet, the design team thought about how the cards interacted with what the colors were doing in Limited. This was a lower priority but helped them pick when narrowing down the card pool.


Ben told me that at one point they had over twice as many candidates for the timeshifted sheet than they had space for. They tried lots of different combinations with the sheet, going through numerous iterations. The main meeting room the design team met in had the *Time Spiral* bonus sheet framed and hung on the wall, and Ben said the team often looked to it for inspiration. One thing they talked about was including humorous (yet weak) cards on the sheet. *Time Spiral*, for example, had [Squire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squire), a 1/2 vanilla creature for 1W. In the end, they decided that it wasn't something they wanted to do. They already had a lot of competition for the 121 slots. Let's make every slot something that would excite some players. In the end, the timeshifted cards appear one per booster and do have the ability to appear in foil.


Back in Black
=============


Before I wrap up for today, I do have three preview cards to show off, all in mono-black. First up is a card from *Time Spiral*. It was a creature destruction card that played into black's love of pushing you to play even more black. It was a common card that saw play in Limited and Constructed. Any guesses?


Click below when you have a guess to what it is (or if you just want to see the card).




Click here to reveal preview card
---------------------------------






![Tendrils of Corruption](https://media.wizards.com/2021/tsr/en_mWW1CvUD1e.png)






Our next preview card took over the *Magic* website one day as a way to introduce *Planar Chaos* to the world. It's a very popular and often played card that is an alternate-reality version of another very popular and often played card.


Click below to see if you've guessed it correctly.




Click here to reveal preview card
---------------------------------






![Damnation](https://media.wizards.com/2021/tsr/en_xOvMhMr7ue.png)






Finally, we have a timeshifted card from *Time Spiral* block's future, but not that far in the future. It's a rare and popular discard spell from *Lorwyn*.


Click below to see if you've guessed it correctly.




Click here to reveal preview card
---------------------------------






![Thoughtseize](https://media.wizards.com/2021/tsr/en_VYCAl9wWUZ.png)






I hope many of you enjoy throwing some, or all, of these cards in a black deck sometime soon.


Out of Time
===========


And with that, it's time to wrap up for today. I hope you enjoyed hearing how *Time Spiral Remastered* came together. As always, I'm eager to hear your thoughts on today's column or on *Time Spiral Remastered*. You can [email](mailto:making.magic@hotmail.com) me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week when I share some design details you might not be aware of about original *Time Spiral* block.


Until then, may you have fun with *Magic*'s past, present, and "future."




 

##### 
 #811: Mark Tedin






##### 
 #811: Mark Tedin


35:31



In this podcast, I interview longtime *Magic* artist Mark Tedin.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork811_marktedin_y38SuD0D.mp3)



  


 

##### 
 #812: Timeshifted Sheets






##### 
 #812: Timeshifted Sheets


31:12



I talk about the creation and design of the timeshifted sheets from *Time Spiral*, *Planar Chaos*, and *Future Sight*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork812_timeshiftedsheets_TsSUsDp3.mp3)




* [**Episode 810**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork810_arabiannightswithrichardpart2_hsye63Ad.mp3) Arabian Nights with Richard, Part 2
* [**Episode 809**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork809_arabiannightswithrichardpart1_sh7stD9w.mp3) Arabian Nights with Richard, Part 1
* [**Episode 808**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork808_evanerwin_ys6tR67s.mp3) Evan Erwin






