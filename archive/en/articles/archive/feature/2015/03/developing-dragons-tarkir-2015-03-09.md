
---
[Link to Wayback Machine](https://web.archive.org/web/20150309144954/http://magic.wizards.com/en/articles/archive/feature/developing-dragons-tarkir-2015-03-09)

[_metadata_:author]:- "Dave Humpherys"
[_metadata_:description]:- "Hitting the optimal number of Dragons in Dragons of Tarkir."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "351701"
[_metadata_:publish_date]:- "2015-03-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Dragons of Tarkir"
[_metadata_:wayback_capture_timestamp]:- "2015-03-09 14:49:54"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150309144954id_/http://magic.wizards.com/en/articles/archive/feature/developing-dragons-tarkir-2015-03-09"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/developing-dragons-tarkir-2015-03-09"
---


Developing Dragons of Tarkir
============================



 Posted in **Feature**
 on March 9, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_davehumpherys.jpg)
By Dave Humpherys




Dave Humpherys has been managing the development team for Magic R&D since 2010. He led development for the Avacyn Restored and Gatecrash sets. He was inducted into the Magic Pro Tour Hall of Fame in 2006. 





Let me start by introducing the *Dragons of Tarkir* development team. This was a large team with a rotating cast of characters so I'll be brief.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/w0xdctvupa_lapille.png)


**Tom LaPille (co-lead)**



Tom recently moved onto another game-design job outside of Wizards of the Coast. While he was with us, Tom led the development of a number of sets including *Magic 2012*, *Dark Ascension*, *Born of the Gods*, and the upcoming *Modern Masters 2015 Edition*. Tom was the lead for the first portion of development, which we refer to as structural development, and then handed off the reins to me. He was still a member of the team while I led, helping communicate the lessons he'd learned whenever I encountered any new challenges.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/9mnbxc996p_Humpherys.png)


**Dave Humpherys (co-lead)**



That's me. You heard from me not long ago in the context of [lead developer of *Fate Reforged*](http://magic.wizards.com/en/articles/archive/feature/developing-fate-reforged-2015-01-05). I'm coming up on my fifth year managing the development team in *Magic* R&D. With *Dragons of Tarkir*, I'll have been on eleven of the last twelve "block"-expansion set-development teams, beginning with *Innistrad*, only missing out on *Dragon's Maze*. I led *Dragons of Tarkir* development through the final phase of team meetings, which we refer to as format development, and continued to make changes until we were off to the presses.


![](https://media.wizards.com/2015/dftyuvbd564776rvf/j23zc10k52_Aten.png)  




Tim is a *Magic* R&D editor. We consider Tim to be a particularly strong and talented Limited player so we asked him to join the team to focus attention on improving Sealed and Draft formats for the format development portion of the development team. He replaced the slot for creative on the team as the creative elements became solidified and our focus shifted more toward Limited and Constructed formats. For his first development team, Tim grasped our development philosophies quite well and was eager to design cards.


![](https://media.wizards.com/2015/dftyuvbd564776rvf/mm20150303_devisnger_kawakami.png)



**Colin Kawakami**



Colin is a creative manager managing the team responsible for art direction. Colin's role was to make sure we were hitting the correct creative notes with this set. My time on the team didn't overlap with Colin's but I'm told he was voice for simplicity. Colin isn't shy about speaking his mind so I'm sure his voice was heard.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/ec065zx1bj_Lauer.png)


**Erik Lauer**



Erik is the *Magic* development lead. He heads the technical aspects of our development team, while I focus on the management of the development team. Erik has led development of some of our most critically acclaimed sets and has led the first set of each block's development team since and including *Innistrad*. Erik was invaluable down the stretch of this set, helping me design new cards we expect to evolve the Standard format.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/zy6b7pky4m_Nagle.png)


**Ken Nagle**



Ken is on the *Magic* design team, most recently leading *Fate Reforged* design. Ken also led design for *Born of the Gods* and *Return to Ravnica*. Ken was the lone member from *Magic*'s design team and so one of his main roles was cranking out a lot of card designs for us to choose from when we needed some fresh ideas for cards.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/mm20150303_devisnger_stoddard.png)  




Sam is a *Magic* developer. He is a voice for our development team through his weekly column Latest Developments on this site. Sam was the member of the team also on the design team, so one of his roles was to make sure we were staying true to the design vision of the set. Sam's most notable lead will be released soon in the form of *Magic Origins*.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/ij37g1lm1t_Thompson.png)


**Gerry Thompson**



Gerry was a development intern in *Magic* R&D for six months until last spring. I didn't overlap with him on the *Dragons of Tarkir* team but I did witness a ton of solid decks he built and tuned for us in our Future Future League for Standard during this block. Now that he has returned to the *Magic* community it's not surprising that he's still creating a prolific amount of creative content and decks. I attribute no small percentage of the quality of our current Standard environment to Gerry's hard work here. With *Dragons of Tarkir*, you'll see some of the final influences of his work within R&D.



Dragons, Dragons, and more Dragons
==================================



One of the biggest challenges with *Dragons of Tarkir* was in how to handle Dragons. Everyone agreed that there should be a lot of them, but there was a fair amount of lively discussion on just how many of them were optimal. We knew the set needed to really take it to the next level of draconic compared to *Fate Reforged*. This is *the* Dragon set after all! At the same time, making each of the Dragons feel new and relevant was challenging once we're looking at more than 30 Dragons in the block. This is especially true given that we wanted each Dragon to feel legitimately like an impressive Dragon in its own right. There was a desire to steer clear of the [Dragon Egg](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Egg)s and [Dragon Whelp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp)s space. Each dragon needed to be mighty enough to warrant the Dragon subtype.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/en_GpZCLoKBHh.png)



At the same time, we also wanted to make Dragons meaningful in new ways. There are many, many cards that incentivize playing with Dragons. [Crux of Fate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crux+of+Fate) and more innocuous text on all of the legendary Dragons in *Fate Reforged* was just the tip of the iceberg for what this block will offer for reasons to consider playing Dragons over other similar creatures. Many of the cards in *Dragons of Tarkir* are at lower mana costs to complement the rest of a potential Dragon-themed deck. Scaleguard Sentinels, for example, is part of a cycle of uncommon cards and perhaps more that, while a bit of a mouthful of words, will hopefully make you eager to consider playing more Dragons in your deck. We went through much iteration on the wording of this cycle to eliminate the "feel-bad" of having your Dragon killed in response and giving you the flexibility to reveal a Dragon from your hand instead of having to wait until you controlled one.



See this Dragon in my hand? It's coming for you!



![](https://media.wizards.com/2015/dftyuvbd564776rvf/en_7LRSy258uL.png)



We wanted to play up Dragon tribal not only in Constructed but also in Limited. The trick was how to make all of the Dragons awesome and yet have Dragons get passed around the table to a player or two who wants to play a bunch of Dragons and be rewarded for doing so. And then who's really going to want to play so many cards in a range of five to seven mana?



One of the first ideas I came up with to encourage dedicated "Dragon-drafters" was to create a cycle of Dragons with megamorph. This meant that you could put a Dragon into the three-mana slot in your deck. Because megamorph allows you to turn up creatures and put +1/+1 counters on them, these Dragons could have slightly smaller stats than the typical Dragon, given that a frequent case use would still be to deploy them effectively as 4/4 flying creatures with upside. One thing I love about megamorph is that the mechanic tweak strongly incentivizes you to go through the face-down state. We tuned these Dragon cards to a power level where they are likely to be passed around a bit to drafters who prioritize them higher than others for the Dragonness.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/en_uAUcJILFrv.png)



My preview card for the day is another way in which we could make Dragons more relevant on cards that don't initially require a lot of mana. We can create cards that are impressive in their own right and provide more late-game options that offer you the assistance of Dragons.



Let's take a look at Dragon Whisperer



![](https://media.wizards.com/2015/dftyuvbd564776rvf/en_xo74Fm8vrT.png)



For two mana, you get a 2/2 that you can spend mana to give flying and/or to pump its power. That felt like a good starting point for a card but there's a lot more upside to be found. If you are in a game that starts to develop into a little more complicated board state and you are struggling to get through safely with Dragon Whisperer, you might just control creatures with total power 8 or greater. In that case, instead of making Dragon Whisperer herself more impressive, you can spend mana to start creating an army of Dragons. I generally love the versatility and feel of this card. It's reminiscent of various aspects of [Dragonmaster Outcast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragonmaster+Outcast), [Dragon Roost](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Roost), and [Kargan Dragonlord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kargan+Dragonlord) all rolled into one.



But It's Not Just About the Dragons
===================================



As I write this, I get to see all of the excitement over Dragonlord Silumgar and am happy to have come up with the idea to add the two important words "or Planeswalker" to the card. It's also great to see the excitement over the art, for which I can take no credit. Seeing reaction to preview season is one of the best parts of this job.



Dragons were a huge focus of this set and are certain to receive much of the initial attention. And it would have been easy to get completely lost in making them shine at the cost of the other elements of the set. Aside from finding solutions for a couple of challenges I've used as examples above, much of the focus of my lead was actually in bringing all of the other pieces of the set together. We needed to make sure the other cards in the set matched the story we were telling through the block. We needed to find spaces for the other cards in the set to shine and move them to appropriate mana costs, and we needed to support other deck themes. We wanted to spice up some old decks and to find suitable creatures to enter before the Dragons and race them.



![](https://media.wizards.com/2015/dftyuvbd564776rvf/cardart_159826.jpg)


Dragon Whisperer | Art by [Chris Rallis](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&&method=visual&&action=advanced&&artist=["Chris Rallis"])



In Limited, we needed to make sure there was a sandbox of things to do and you'd be happy even if you didn't open up any Dragons you wanted to play. As part of that, we needed to make sure that Dragons were good and playable, but also that they weren't despair-inducing. We had to ensure there were enough decent cards to answer the Dragons, in ways we had fallen short of in our previous draft environment of big flying creatures, with *Avacyn Restored*.



By the time I was leading the set, the keyword mechanics had all been solidified, so it was a matter of finding the best execution on these cards. It was a matter of interweaving the mechanics as best we could and playing up fun synergies like those between prowess and rebound. Until I started work on *Dragons of Tarkir*, I'd been approaching it from the other end of the system as lead of *Fate Reforged*. And now I'm very excited to see all of the elements of this block come together. We hope you enjoy it too!



As always, thanks for reading,



Dave Humpherys










