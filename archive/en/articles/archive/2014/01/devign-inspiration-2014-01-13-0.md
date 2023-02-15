
---
[Link to Wayback Machine](https://web.archive.org/web/20210501193131/https://magic.wizards.com/en/articles/archive/devign-inspiration-2014-01-13-0)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "I was the lead developer for Born of the Gods. It feels strange to type that, as it's been a long time since I wrote a development article. Before I started working on Born of the Gods, though, it had been a little while since I worked on a Magic set. I love Magic, though, and it feels good to be home. Before we get into the meat of the article, let's talk about the Born of"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "683211"
[_metadata_:publish_date]:- "2014-01-13"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Devign Inspiration"
[_metadata_:wayback_capture_timestamp]:- "2021-05-01 19:31:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210501193131id_/https://magic.wizards.com/en/articles/archive/devign-inspiration-2014-01-13-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/devign-inspiration-2014-01-13-0"
---


Devign Inspiration
==================



 Posted in **Feature**
 on January 13, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







I was the lead developer for *Born of the Gods*. It feels strange to type that, as it's been a long time since I wrote a development article. Before I started working on *Born of the Gods*, though, it had been a little while since I worked on a **Magic** set. I love **Magic**, though, and it feels good to be home. 


 Before we get into the meat of the article, let's talk about the *Born of the Gods* development team. 


### Tom LaPille


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_lapille.jpg) That's me! *Born of the Gods* is the third major booster release I led the development for, and I also led *Masters Edition III*, *Masters Edition IV*, and *Archenemy*. I've also been a team member on too many development teams to list. I recently took about a year off of working on **Magic** to help build the mathematical underpinnings of D&D Next, but I came back to **Magic** when [Aaron](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Aaron%20Forsythe) needed someone to lead this set. I'm glad to be back, and I'm already leading another set too! 


### Dave Humpherys


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_humpherys.jpg)
[Dave](http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humpherys) manages the development group, and his **Magic** lead development credits include *Avacyn Restored* and *Gatecrash*. He came to us with a great deal of card game design experience from other games, though, and he also happens to be a member of the **Magic** Pro Tour Hall of Fame. The combination of extreme play skill and experience with the process made him a valuable member of the team. 


### Billy Moreno


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_moreno.jpg) Pro Tour Honolulu 2005 finalist [Billy Moreno](http://www.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno) joined us for a while, lending us his idiosyncratic deck-building instincts and Pro Tour **Magic** expertise. During *Born of the Gods* development, he was preparing for his own first set lead. He has since returned to Texas to pursue other opportunities, but you'll see more of his work in the near future. 


### Mark Gottlieb


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_gottlieb.jpg)
[Mark](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Gottlieb) is currently our design group manager, but he has worn many different hats during his time at Wizards. He was the rules manager when I started in 2008. He did a short stint as a developer before shifting into a management role for the design team, which is where he is now. He was the lead designer of *Mirrodin Besieged* and one of the co-lead designers of *Gatecrash*; he also wrote the House of Cards column on this site for a while, and it is there that you can see the true form of his brilliant madness. Mark is a fantastic designer of individual interesting cards, and his fingerprints are all over the set. 


### Chris Dupuis


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_dupuis.jpg) When *Born of the Gods* started, Chris was a board game designer in **D&D** R&D. His credits from that time include the *Scoundrels of Skullport* expansion to *Lords of Waterdeep*, several Adventure System games, and all five Dungeon Command boxes. He was a skilled designer and wanted to learn about trading card games, so we spent our "not-in-**Magic**-R&D" slot on him. It couldn't have worked out any better. He learned **Magic** very quickly, leveraged this gig into working on **Kaijudo** as a side thing, and has since transferred into **Kaijudo** R&D as a designer. Chris is one of the fastest-learning game designers I've ever met, and it was a pleasure to have him on the team. 




---

 We have our schedules built so that the design team has months to work, and then the development team has months to work when the design team is done. However, the time around the overlap between the two teams is probably the most important time in the whole process. We call that period "devign," because clever names are fun. As of *Born of the Gods*, we now have a step in the process a month before devign begins that I like to call the "devign intervention," which is when the development team plays with the design file and gives formal feedback to the designers. 


 For me, the story of *Born of the Gods* begins with the devign intervention. The first thing I always look for in a set is what the new mechanics are. When we had the devign intervention playtest, there was only one new keyword mechanic in the set: tribute, which was already close to its final form. 



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/BXfs2Ih8NH_EN.jpg)
  
 Tribute recalls cards like [Breaking Point](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaking+Point) and [Browbeat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Browbeat), which we often call "punisher" cards. The punisher mechanic reads well, because it seems to offer the opponent an unpleasant choice, but in practice it often doesn't work as well as one wants. The two options on [Breaking Point](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaking+Point) are very different—one is highly offensive, and the other is quite defensive—and so the decision often is not actually difficult. If you are playing against a beatdown deck that is still at a high life total, your opponent will think nothing of taking 6 damage. If you are playing against a control deck that has few creatures but cares more about its life total, your opponent will likely just let one creature go instead of taking 6. [Browbeat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Browbeat) is the standout punisher card because in a straight burn deck, there's not much difference between 5 damage and three cards. 




|  |  |
| --- | --- |
| Breaking Point | Browbeat |

Tribute solves this problem by reducing the difference between each mode of the card. Because so much of the value of the card is the base creature, it's much less likely that either of the two options will leave you with a blank card after your opponent makes his or her decision. This means that more of the cards are strong enough to play, and so the fun punisher decision gets put to players more often. By the end of the playtest, I knew that tribute was a keeper.


I mentioned before that there was no other keyword mechanic in the set at the time. Instead, there was a loosely connected constellation of cards that played in the space of caring about whether creatures were tapped or untapped. There was no unifying mechanic, however, which I thought was almost certainly a bad idea. Many of the ideas were innovative but a little weird, like creatures with static or activated abilities that only worked while the creature was tapped—things that I wasn't interested in having at common, which is somewhere a main set mechanic must be able to live.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/2014/pjmpjcpiet_featdevigninspirationwk02_pg.jpg) Pharagax Giant | Art by [Ryan Pancoast](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Ryan%20Pancoast%22%5D)




[Ken Nagle](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20nagle) and I were both interested in investigating ways to unify all of these cards into one mechanic. I'm generally a fan of tightening up cards that work similarly so there is less to learn before a player can more quickly start thinking about how cards interact with one another instead of how an individual card works, and Ken was looking for another mechanic that could get a unique word. 


 The first thing we investigated in the wake of the devign intervention was [the untap symbol](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+%5b%22Shadowmoor%22%5d&text=+%5buntap%5d+%5bsymbol%5d) from *Shadowmoor* and *Eventide*. That felt like it was in the right space, as I liked that you could put mana on the activation costs and it was capped at one use per turn unless you did something strange. I didn't like the onboard complexity of it being usable at instant speed, so we tried it with an "activate this ability only any time you could cast a sorcery" restriction. 


The two playtests we did with this version were closer, but still not quite right. It was strange to attack with a guy and then immediately pay mana to untap it, and the untap symbol itself is a bit of a goofy rules object. I suggested we try "When CARDNAME untaps..." as a trigger instead. Ken tried it, and it stuck.


 In development, we often like to imbalance, where we put different quantities of different mechanics in each color in order to make playing different colors feel different. Inspired began in the file in all five colors evenly, but it played more synergistically in blue and black because those were the colors in *Theros* Limited that most wanted to play for the long game. We adjusted for this by putting extra inspired cards in those colors, as well as more cards that help you get your own creatures tapped. 


 That solved inspired for Limited, but not for Constructed. At the time, most of our decks that played black had significant numbers of high-mana-cost cards, and our beatdown decks that included black were pretty weak. I also knew that I wanted to make at least one strong inspired Constructed card. My idea was that a [Dark Confidant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Confidant) variant would help out lower-curve decks, but not replace [Underworld Connections](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Connections) in a deck that wanted to go bigger with its mana costs. 


 With that in mind, here's Pain Seer. 



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/wXHJZFYuK6_EN.jpg)  

  
 I found this to be an interesting ability to put on a [Walking Corpse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse), as I drafted decks during our playtesting that would have preferred a [Walking Corpse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) to a Pain Seer by a good margin. [Walking Corpse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) isn't usually where you want to be in Constructed, so Pain Seer is much stronger there, but it would not be fair to claim that Pain Seer is a straight upgrade. 


 I think very highly of inspired for many reasons. A card with an inspired ability can go in any deck and just work, as attacking is a built-in way to get cards tapped. There is plenty of room to build around it, though, and many people enjoyed the cards in  *Born of the Gods*  that can be used to get your creatures tapped through other means. I also enjoy that inspired helps drive games toward completing, as an inspired ability is a strong incentive to attack. 


 I had a lot of fun making *Born of the Gods*. I received an excellent design handoff from Ken Nagle, and in the end I think it's my best work yet. I look forward to seeing how things play out in the real world, and maybe you'll hear from me again soon. 














