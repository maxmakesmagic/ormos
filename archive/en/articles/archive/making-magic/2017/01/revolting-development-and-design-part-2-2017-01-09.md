
---
[Link to Wayback Machine](https://web.archive.org/web/20170109173249/http://magic.wizards.com/en/articles/archive/making-magic/revolting-development-and-design-part-2-2017-01-09)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark wraps up his behind-the-scenes look at the development (and design) of Aether Revolt."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1109136"
[_metadata_:publish_date]:- "2017-01-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "A Revolting Development (and Design), Part 2"
[_metadata_:wayback_capture_timestamp]:- "2017-01-09 17:32:49"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170109173249id_/http://magic.wizards.com/en/articles/archive/making-magic/revolting-development-and-design-part-2-2017-01-09"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/revolting-development-and-design-part-2-2017-01-09"
---


A Revolting Development (and Design), Part 2
============================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on January 9, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Last week I began my look behind the scenes at the design of *Aether Revolt*, and this week I'm back with the second part. If you haven't read [last week's column](http://magic.wizards.com/en/articles/archive/making-magic/revolting-development-and-design-part-1-2017-01-02), I suggest you do as this week's column assumes you have. (If I had the time and materials, I'd have a "Previously in Making *Magic*" video on all Part 2s.) That said, let's continue our story.


Aether Ore
==========


As I explained last week, the challenge of *Aether Revolt* was to retain as much as possible of what defined *Kaladesh* while also capturing the feel of a revolt. The *Kaladesh* design team was aware that the revolt was coming in the expansion, so we actually did something to try to help them. One of the things I like to do when designing the large set is to look at the small set and get a sense of what separates the big set from the small set such that we can save something for the small set to do. (One of these days I'll do a column about the evolution of how the large set has looked out for the small set. The short version is with time, we keep doing more and more to figure out what the small set is up to.)


When we looked at *Kaladesh* and *Aether Revolt*, the distinction we drew was that *Kaladesh* was constructive and *Aether Revolt* was destructive. Both were about building inventions, but the former was more about doing so to create things that built other things up, while the latter built things that broke other things down. How could we mechanically make this distinction?


First, we could be careful with what top-down stuff we made. Things like miraculous, showy inventions were for *Kaladesh*, while weapons needed to be saved for *Aether Revolt*. *Kaladesh* artifacts helped you build yourself up when in play. *Aether Revolt* artifacts would, in contrast, be more about bringing the opponent down. Also, we could be extra careful about things that sacrificed other things, especially artifacts, and we could lean more on enters-the-battlefield triggers in *Kaladesh* and less on death triggers. This whole philosophy was spelled out in the *Kaladesh* design vision document, and it was something that the *Kaladesh* development team worked hard to maintain.


The Mechanic That Wasn't
========================


The *Aether Revolt* design team started with the following objective: find a mechanic that conveyed a sense of revolt. The more the design team talked about it, the more we kept circling around to the idea of caring about destruction in some way. As I explained above, the *Kaladesh* design team had left sacrificing artifacts as a cost for *Aether Revolt*. Was there a way to interact with this?


What about artifacts that did damage to an opponent when they went to the graveyard? We could include that on a bunch of cards, but it didn't really feel like a mechanic. Usually when looking for a new mechanic, you need to find something that not only can be used on enough cards and that has the proper feel for the mood and tone of the set, but also something that feels weighty enough to be a named mechanic.


Mark Gottlieb liked the general feel we were playing around with, but wanted to attack it in a more novel way. That's when Gottlieb took the idea of a death trigger that damaged an opponent and applied it to a counter. What if we made a counter with an innate ability? What if there was a counter you could put on a permanent that did damage to an opponent when that permanent went to the graveyard? We called them "volatile counters."


Here's how it worked: Different cards created volatile counters. Some put them on themselves and some put them on other permanents. Whenever a permanent with a volatile counter on it went to the graveyard from the battlefield, the volatile counter did 2 damage to target opponent. Remember it was the counters that did the damage, and whoever generated the counter controlled it, so that meant that you could put volatile counters on an opponent's permanent and when it went to the graveyard, it would damage them.


Volatile counters proved to be very interesting. You could put them on your own things to either discourage your opponent from destroying them or to sacrifice them and get in extra damage, or you could put them on your opponent's permanents to either discourage their use or create an extra bonus when you destroyed something. Around this time in design, we were also toying with possibly having some cards with proliferate—and the volatile counters worked nicely in the ecosystem. (Design did also toy around with dropping fabricate, which is why we had two mechanics for a while during design.)


But volatile counters ending up having three big problems. The first two were complexity issues. Normally, we try to limit counters on any card type to one type of counter. If I see a 2/2 with a counter on it, I should be able to know how big that creature is for any Limited environment. But volatile counters really needed to be able to go on creatures. A lot of the best gameplay was players making choices about attacking and blocking based on how many volatile counters were on creatures. Even if we removed fabricate from *Aether Revolt*, the mechanic was still in *Kaladesh*, and Limited would still create moments where players didn't know if the counter on the 2/2 was a +1/+1 counter or a volatile counter. (As an answer to this problem, we toyed around with making a volatile counter card that you could use to make it clear that it had a volatile counter on it.)


Second, volatile counters often worked best when you spread them around. Keeping track of all the different counters and the damage they represented proved to be a bit more taxing than we liked. And they weren't often something you could ignore because they represented changes in life total, something that's very important to track.


And then there was the third problem. *Magic* is obviously a game about conflict, but we try to stay within the realm of fantasy and steer clear of making things that feel too "real-world violent." No matter how we tried to spin the flavor, volatile never quite felt fantasy enough.


In the end, the complexity issues along with the flavor issue just did the mechanic in, and during design we found ourselves in need of a new mechanic.


It's Revolting
==============


The solution to this problem came from Ben Hayes, *Aether* *Revolt*'s lead developer. Ben agreed with the design team that caring about destruction seemed to be the right area to explore. The mechanic that Ben came to while trying to solve this problem was morbid.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=230777)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=230777)
Morbid is a mechanic from original *Innistrad* where cards get better if a creature had previously died this turn. I'd created morbid during *Innistrad* design because I was trying to find a way to make death matter. I wanted to create a sense of dread in the gameplay, and I liked the idea that any time a creature died, there was something to worry about. It also allowed players to make suboptimal attacks and bluff. (This was important because the creatures in *Innistrad* were designed to be a little more fragile than normal to enable a number of other things going on in the set.)


Ben felt that morbid did a lot of the things he was looking for, but it wasn't quite right. What if they tried artifact morbid—just like morbid except it was checking to see if an artifact had been put in the graveyard rather than a creature? That was still a bit too restrictive. While *Kaladesh* block had a significant artifact component, we had worked hard to differentiate *Kaladesh* from *Mirrodin* and, as such, purposely chose to represent the technology on normal cards in addition to artifacts.


Also, Ben found that restricting the trigger to only things that went to the graveyard was missing a bunch of interactions in the block. By changing it to "leaves the battlefield," the mechanic could also hit things like the self-bounce in *Kaladesh*. Finally, Ben wanted the mechanic to feel vengeful or retributive, so triggering off of the opponent's stuff felt wrong. It was also another way to distant the mechanic a little more from morbid.


![](https://media.wizards.com/2016/c1lRLirbrl_AER/en_qr5oflSmPS.png)


Design-wise, revolt worked on the same type of cards morbid did. It could go on both spells and permanents. For spells, it strengthened the effect of the spell, basically upgrading it. For most permanents, revolt adds an enters-the-battlefield effect, either creating a spell-like ability or adding +1/+1 counters. On a small handful of cards of higher rarity, it adds an at-beginning-of-end-step trigger to create an effect that happens each turn.


Revolt is in green and white with a little in black. Improvise, which I introduced last week, is mainly in blue but also a touch in black and red.


What's New
==========


In addition to the two new mechanics, improvise and revolt, there are a number of other new things in *Aether Revolt*. Let's talk about a few of them.


**The Legend Cycle**


For starters, each color gets a new rare legendary creature. Between the popularity of Commander and the rise in interest in the *Magic* story, legendary creatures are at an all-time high. The *Aether Revolt* development team decided to add five through a cycle. (Legendary creatures are sometimes finalized later in the process, meaning that they're often designed in development rather than design.)


![](https://media.wizards.com/2016/images/daily/4E0MXAONfN.png)


The two most high-profile of the legendary creatures are Baral, the officer that caused Chandra so much hardship in her backstory (the one who would have killed her if she hadn't sparked) and Yahenni, who has been the narrator of two of the [*Kaladesh*](http://magic.wizards.com/en/articles/archive/magic-story/born-aether-2016-09-21) and [*Aether Revolt*](http://magic.wizards.com/en/articles/archive/magic-story/dead-night-2016-11-30) stories. Each of these cards was designed to accomplish two things. One, we wanted designs that captured the top-down flavor of the character. Two, we made sure that these cards were fun build-around cards.


The legendary goodies don't just stop at the creatures, though. The set has six more legendary cards: one enchantment (which I'll talk about below) and five artifacts, including one Vehicle.


**The Expertise Cycle**


![](https://media.wizards.com/2016/images/daily/sAOgs8K4nx.png)


The five legendary creatures also inspired a second rare cycle, all titled "[Legendary Creature's] Expertise." Each of the cards in this cycle is a sorcery. Each one creates a worthwhile effect, then allows the player to cast a card in their hand with a converted mana cost less than the converted mana cost of the Expertise spell without paying any mana. Conveniently, the legendary creature for whom the Expertise spell is named is always less mana than the Expertise spell, allowing you to cast that legendary creature if it's in your hand.


**Ajani and Tezzeret**


![](https://media.wizards.com/2016/c1lRLirbrl_AER/en_SDQw1NFdZl.png)![](https://media.wizards.com/2016/c1lRLirbrl_AER/en_Pm9YNrJbht.png)![](https://media.wizards.com/2016/c1lRLirbrl_AER/en_j2IYia8PtD.png)


The two planeswalkers in *Aether Revolt* are two characters who play a major role in the story. First is Ajani, who we saw meet and befriend the Gatewatch in *Kaladesh*. Ajani returns as a green-white planeswalker. When we first introduced the Gatewatch, I said that others would be joining. Obviously, Liliana joined in *Eldritch Moon*, but that was just the beginning. Ajani joins the Gatewatch as the first multicolored planeswalker. This means, of course, that *Aether Revolt* has another Oath card, this time for Ajani. And yes, the Oath card is the same color as the character taking the oath.


Tezzeret is the second planeswalker, also showing up in the same color combination we last saw him: blue-black. Many players assumed he was going to show up in *Kaladesh*, but we decided to hold him back for *Aether Revolt*. Like his previous incarnations, Tezzeret has a strong artifact theme in his loyalty abilities.


**More Energy**


Energy played a big role in *Kaladesh*, and it was clear to everyone that we needed to continue it in *Aether Revolt*. (Not doing so would cause a real aether revolt.) As I explained last week, energy has a lot of design space, so there were plenty of areas left to explore. (For instance, there are some new triggers to get energy and some new effects to spend energy on.) The *Aether Revolt* design and development teams created new energy cards to go into existing decks but also wanted to explore different spaces for energy. In particular, there was a big push to give a little more attention to white and black energy cards.


**More Vehicles**


Likewise, the design and development teams were eager to find new design space for Vehicles. *Kaladesh* had purposely held back in a few areas to allow *Aether Revolt* room to play. In the set, you'll find Vehicles that interact with energy, one that can be crewed in a new way, and a few more Vehicles that can auto-crew without always needing creatures. We also have new cards that interact with Vehicles in different ways.


**More Johnny Goodness**


Another very important part of the *Kaladesh* block was the inventor feel. *Kaladesh* had a lot of quirky individual card designs that led to interesting deck building and higher synergies in gameplay. The *Aether Revolt* design and development teams were eager to maintain this in the new set. There are plenty of cards with a similar feel to *Kaladesh*, as well as some cards that explore the rebellious and destructive nature of *Aether Revolt*.


All in all, I think that *Aether Revolt* does a wonderful job of finding the space close enough to *Kaladesh* to feel like part of the same block and to play well in Limited formats, but different enough to have its own identity that will line up with the story we're telling.


Explosive Fun
=============


That's all the time I have for today. Hopefully, I've given you a little glimpse into the design of *Aether Revolt*. If you have a chance, I heartily encourage you to check out the Prerelease this weekend. This is definitely a set that has to be played to be properly absorbed.


As always, I am eager to hear your feedback on both this column and the new set. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249), and [Instagram](https://www.instagram.com/mtgmaro/)).


Join me next week when I start telling card-by-card design stories.


Until then, may you find time to join our little revolt.




---

**"[Drive to Work #394—R&D Vocabulary, Part 1](http://media.wizards.com/2016/podcasts/magic/drivetowork394_rdvocabularypart1.mp3)"**


**"[Drive to Work #395—R&D Vocabulary, Part 2](http://media.wizards.com/2016/podcasts/magic/drivetowork395_rdvocabularypart2.mp3)"**


In November, I wrote a column called "[A Few More Words with R&D](http://magic.wizards.com/en/articles/archive/making-magic/few-more-words-rd-2016-11-07)" where I talked about slang used by R&D. In these two podcasts I go over all that vocabulary and more in detail.


* [**Episode 393**](http://media.wizards.com/2016/podcasts/magic/drivetowork393_evergreencreature.mp3) Top 10: Evergreen Creature Keywords" (22.9 MB)
* [**Episode 392**](http://media.wizards.com/2016/podcasts/magic/drivetowork392_designinguncommons.mp3) Designing Uncommons (27.9 MB)
* [**Episode 391**](http://media.wizards.com/2016/podcasts/magic/drivetowork391_cohesion.mp3) Cohesion (20.5 MB)






