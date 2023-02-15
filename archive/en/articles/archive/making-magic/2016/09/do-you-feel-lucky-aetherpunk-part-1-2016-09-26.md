
---
[Link to Wayback Machine](https://web.archive.org/web/20160929104705/http://magic.wizards.com/en/articles/archive/making-magic/do-you-feel-lucky-aetherpunk-part-1-2016-09-26)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark covers the first part of card-by-card design stories from Kaladesh."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1080326"
[_metadata_:publish_date]:- "2016-09-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "`Do You Feel Lucky, Aetherpunk?` Part 1"
[_metadata_:wayback_capture_timestamp]:- "2016-09-29 10:47:05"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160929104705id_/http://magic.wizards.com/en/articles/archive/making-magic/do-you-feel-lucky-aetherpunk-part-1-2016-09-26"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/do-you-feel-lucky-aetherpunk-part-1-2016-09-26"
---


"Do You Feel Lucky, Aetherpunk?" Part 1
=======================================



 Posted in [Making Magic](/en/articles/columns/making-magic-archive)
 on September 26, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






The preview weeks are over, which means it's time for my card-by-card design stories. And I have a lot of good stories to share, so let's jump right in and get started.


Animation Module/Decoction Module/Fabrication Module
====================================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Animation+Module)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Animation+Module)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Decoction+Module)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decoction+Module)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=FABRICATION+MODULE)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fabrication+Module)
During original *Mirrodin* block in the last set, *Fifth Dawn*, I made this cycle of cards:


![](https://media.wizards.com/2016/images/daily/MM20160926_Stations.png)


The cycle was called the Stations. Each of them is what is known as an engine card in that it allows you to trade one resource for another. For example, [Blasting Station](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasting+Station) allowed you to turn a creature into direct damage. *Fifth Dawn* was an artifact set and as part of its identity, I wanted to make it a bit more build-around. You see, earlier, *Mirrodin* had kind of broken things so I was trying to find something fun to do that wouldn't cause further problems in Standard. I figured a wacky build-around theme would do the trick.


The Stations were designed so that each one was a "build around me" card. If you could generate enough creatures, for instance, [Blasting Station](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasting+Station) could kill the opponent. But I didn't stop there. The Stations were each designed such that the output of one card was the input of another. For example, [Summoning Station](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summoning+Station) has an effect that puts a 2/2 creature token onto the battlefield. That both untaps [Blasting Station](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasting+Station) and gives you a creature you could sacrifice to it. If you put all four Stations together, you got a loop that could win you the game. (Technically you also needed a noncreature artifact that costs 1 or less.)


When thinking about fun things we could do for *Kaladesh*, my brain went back to the Stations. Artifact engine cards that click together? What's more inventor-y than that? So, I set out to make a new Station cycle.


My goal was to capture the essence of the Stations but try a different spin on them. Instead of the untap gimmick that the Stations had, I decided to just have a triggered effect that generated some resource and an activated ability that would help you trigger other cards in this cycle. The trick to this cycle was that I wanted the activated ability on the card to be relevant to the triggered ability so that the card could function just fine on its own.


I was also very interested to make use of resources that *Kaladesh* cared about. After some thought, I decided those resources were artifacts, +1/+1 counters, and energy—the two outputs of fabricate and the output of energy. I had started trying to make four cards, like the Stations, but decided that three worked better so I switched to three.


So, one of the cards gave you an artifact and one cared that an artifact entered the battlefield, one card put a +1/+1 counter on a creature and another card cared that a +1/+1 counter was put on a creature, and one card produced energy and another card cared that energy had been produced. The output could come as either the result of the trigger or as a result of the activated ability. I just had to pick an order for the cards to loop in.


I started by piecing together the inputs and outputs. I liked having an artifact that gave you an energy counter each time another artifact entered the battlefield. It had a nice flavor in that you could siphon some energy off each new artifact you got. It then needed an ability that could help you trigger the card unto itself. Because so many cards in the set have "enters the battlefield" triggers (more on that when I get to [Panharmonicon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Panharmonicon)), I liked the idea that you could activate this card to return an artifact to its owner's hand. This way if you had mana, the card allowed you to turn it into energy, plus you could reap the benefits of an "enters the battlefield" trigger on the artifact.


I'm sure, by this point, a bunch of you are, "But Maro, [Decoction Module](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decoction+Module) cares about a creature entering the battlefield not an artifact." To which I reply, "Yeah, it does now." For all of design and much of development, the trigger was an artifact entering the battlefield, but that proved problematic, so development changed it from artifact to creature. As the trigger was an artifact creature token, it was good either way.


If the first artifact produced energy, that meant the next one had to trigger off you getting energy. It also meant the output of the trigger had to be a +1/+1 counter. I believe the original version gave you a +1/+1 counter for each energy counter you got, but it ended up being changed to only trigger each time you got a packet of energy regardless of how many individual energy counters it was. The activated ability didn't have a lot of room as it had to produce energy. We ended up just letting it straight up create energy. As it will always trigger, you essentially get both an energy and a +1/+1 counter for the 4 mana activation.


The final artifact had to trigger off a +1/+1 counter being put on a permanent, and had to generate a artifact creature token. We messed around with it making a Thopter, but that ended up being too good. In the end it was a Servo, and even then we had to make you pay 1 for it. There was much talk, as it added mana into the loop. But, developmentally, we needed it so it stayed. The big question was what would the effect be. We could just have it put a +1/+1 counter on a permanent, but we wanted to do something a little fancier, so we used proliferate.


What?! Yes, for a chunk of design, proliferate was in *Kaladesh*. It was our initial plan for it to be the returning mechanic in the block. It worked with both fabricate and energy, plus artifact blocks tend to have lots of counters. In the end, it worked a little too well with +1/+1 counters and not well enough with energy. It started warping the set in a way that was making it play worse, so it had to go. I do like proliferate and plan one day to bring it back, but this block, unfortunately, just wasn't the time. When proliferate left the set, we opted to scale down the effect to a written out proliferate-like effect that only added one counter to one permanent.


The creative team then ran with the ball, having one artist, Aaron Miller, draw all three pieces and have them create a visual loop if put side by side. The artifacts then were all named the same and given a similar flavor text treatment.


I'm very happy with how they turned out. They share the quality that I like with the Stations in that they are fun to play both by themselves and with each other.


Armorcraft Judge/ Ovyla Pashiri, Sage Lifecrafter
=================================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Armorcraft+Judge)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armorcraft+Judge)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oviya+Pashiri%2C+Sage+Lifecrafter)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oviya+Pashiri%2C+Sage+Lifecrafter)
The key to designing fabricate cards was twofold. First, we wanted to make sure that each card was, unto itself, an interesting decision. If you always picked the same output, be it +1/+1 counters on Servo creature tokens, the mechanic was failing. Making the players feel like an inventor was about creating interesting choices.


These two cards represent the other part of making the mechanic work. We needed to make cards that externally made both choices relevant. For +1/+1 counters, that meant one of two things. You could make +1/+1 counters relevant, as Armorcraft Judge does, or you could make power and/or toughness relevant. For the Servo artifact creature tokens, you had more options. You could make artifacts relevant. You could make creatures relevant, either as a resource, as a means to deal damage, or as a way to care about the number of creatures you control. Also, because the tokens are external to the creature, it makes things that flicker (exile and then later return to the battlefield) or bounce your creatures have extra value.


The trick here is focusing both on the micro, making the cards in a vacuum relevant, and the macro, making environments where both halves of the mechanic can shine.


Concealed Courtyard/ Spirebluff Canal/Botanical Sanctum/ Inspiring Vantage/Blooming Marsh
=========================================================================================


![](https://media.wizards.com/2016/images/daily/MM20160926_KLD-Fast.png)


Players ask me all the time why design put a particular dual land cycle into the set. The answer is most often the same: we didn't. Access to colored mana is so key in Constructed *Magic* that development figures out what mix of dual lands will work best, and then informs design of their decision. On occasion, we design a dual land that fits perfectly in theme and present it to development, but that is the exception to the rule and was not the case this time around. The players have been asking for the enemy version of the dual lands from *Scars of Mirrodin* for years now, so it was nice to finally get them into a set.


Cataclysmic Gearhulk/Torrential Gearhulk/Noxious Gearhulk/Combustible Gearhulk/Verduous Gearhulk
================================================================================================


![](https://media.wizards.com/2016/images/daily/MM20160926_Gearhulks.png)


The Gearhulk cycle was added in development. They wanted a cycle of mythic rare artifact creatures and nothing design turned in quite fit the bill, so they designed their own cards. They all cost five or six mana with two colored mana required, they all have an evergreen creature keyword of their color and they all have a powerful "enters the battlefield" effect.


There was a little discussion about them being colored artifacts as that's not something found anywhere else on Kaladesh, but development both wanted them to require colored mana (to keep too many from going into the same deck) and wanted them to be artifact creatures for flavor reasons, so the colored artifacts ended up being the best choice.


Chandra, Torch of Defiance
==========================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chandra%2C+Torch+of+Defiance)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%2C+Torch+of+Defiance)
Of all the Planeswalkers that show up on a somewhat regular basis, Chandra has historically proven the hardest to make tournament playable. This was Chandra's home plane and it was going to be her story, so we were determined to give her a good card. I'm not sure who first brought up the idea of making her a four-ability Planeswalker (she's the third after [Jace](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=195297) and [Garruk](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=383251)—not counting the double-faced Planeswalkers) but everyone got on board as soon as the suggestion was pitched.


Her first ability makes use of the "impulsive draw" ability which first showed up on a previous Chandra but which has since become a staple ability of Red. The second ability is something new for Chandra—creating mana, but is something Red can do. Her third ability is standard Chandra dealing direct damage to creatures. Her ultimate was trying to capture her art with the idea that an angry Chandra is an ablaze Chandra hurling fire everywhere.


We'll have to see if this version of Chandra can live up to the hype, but I believe it will.


Chief of the Foundry
====================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chief+of+the+Foundry)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chief+of+the+Foundry)
*Kaladesh* did something we had never done before—we previewed a new plane by having it show up in small quantities in an earlier set. I remember talking with Shawn Main (who was the lead designer for *Magic Origins*) about how we could set up some expectations without committing ourselves too deeply to a set that wouldn't begin design for over a year.


In the end, Shawn chose to focus on artifacts. Kaladesh was going to be a steampunk inspired world so it seemed like a safe bet. Part of this was also choosing to focus on artifact creature tokens. Kaladesh of *Magic Origins* played up Thopter tokens but I felt confident that we could broaden out of the theme with more artifact creature tokens in *Kaladesh*, the block.


One of the big questions we had going into *Kaladesh* design was what reprints might we want from *Magic Origins*. It felt like we had to have some and at least one that would be memorable. [Chief of the Foundry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chief+of+the+Foundry) ending up being that card. It was created originally to work with Thopter tokens but it compliments Servo tokens equally well. We kept it at uncommon because we felt it would serve a similar function of being a strong "build around me" card for Limited.


Cogworker's Puzzleknot/Glassblower's Puzzleknot/Metalspinner's Puzzleknot/Fireforger's Puzzleknot/Woodweaver's Puzzleknot
=========================================================================================================================


![](https://media.wizards.com/2016/images/daily/MM20160926_Puzzleknots.png)


This cycle exists to solve two issues with an artifact block. First, an artifact block requires a certain threshold of artifacts. This means you have to make room in the file for additional artifacts, which requires finding ways to free up space elsewhere in the file. One trick to do this in an artifact block is to make artifacts that fill the role filled by instants and sorceries. Usually these are artifacts that either have an "enters the battlefield" trigger and/or have a sacrifice effect. The Puzzleknot artifacts do both.


Second, you have to be careful with artifact blocks because they can disrupt the balance of the color pie. One of the easiest ways to handle this is to make artifacts that have activations (or triggered effects) using colored mana. You just have to make sure that some portion of the artifact is still useful without the colored mana, because we like artifacts to be able to function in any deck. The Puzzleknot artifacts solve this because they get their "enters the battlefield" trigger regardless of your access the right color mana.


Confiscation Coup/Die Young/Harnessed Lightning
===============================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Confiscation+Coup)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confiscation+Coup)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Die+Young)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Die+Young)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Harnessed+Lightning)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Harnessed+Lightning)
Energy cards can be tricky to design. As a rule of thumb, you want to make sure that the card provides enough access to energy that you'll be able to properly use it. Beyond that, you also like to have your energy cards feel as if they can do something even bigger if you get access to additional energy.


Permanents do this easily. You usually get energy counter as an "enters the battlefield" effect. You then have an ability that uses energy in a way that could potentially become larger in scale if you ever get access to other energy. The problem is that it's hard to capture this feel when you're messing around with nonpermanent spells. These three cards were our attempt to answer this issue.


Each of these cards gives you some amount of energy. It then allows you to use as much energy as you like, to create a scaling effect. If you have no other access to energy, these cards are self-sufficient, but are limited in scope as to what they can do. If you do have access to other energy, you can use that energy to boost the effect, making it potentially very powerful.


Depala, Pilot Exemplar
======================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Depala%2C+Pilot+Exemplar)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Depala%2C+Pilot+Exemplar)
This card addressed a number of different issues:


1. Dwarves have traditionally been red, but *Kaladesh* introduced them in white. We wanted to promote some Dwarf tribal but we wanted it to be backwards compatible. The key was making a dwarf lord that was red and white.
2. Vehicles were designed so you didn't have to play a lot of them. You can just throw one or two in a deck and be fine. But we knew some players were going to want to put the pedal to the metal, figuratively *and* literally, and play a heavy Vehicle deck. Cards like this help make that possible.
3. On this world, Dwarves are the best pilots. This card allows you to cross the synergy of Dwarves with the synergy of Vehicles and make "Dwarves are the best pilots" true for game play.
4. We like to make sure that Commander players get Commanders that play into the sets themes. Depala plays into *two* of the set's themes.
5. One of the complaints I've been getting lately is that too many red-white commanders play into the same deck archetype—aggro beatdown. Depala is a completely different deck for the Commander Boros players out there.

Dovin Baan
==========


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dovin+Baan)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovin+Baan)
An important job of design is to work with the creative team to make sure that the cards mechanically copy the elements of the story. Sometimes that's easy, and sometimes it can get very difficult. [Dovin Baan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovin+Baan) is an example of the latter. [Dovin Baan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovin+Baan)'s ability is to spot weaknesses in things. It allows him the ability to exploit these weaknesses and makes for a very compelling character. There's only one problem—we have to make a Planeswalker card for him and "can spot the weaknesses in things" is very hard to design.


The trick to doing it was to take a step back and think a little more big picture. Instead of trying to imagine what, exactly, his ability meant as an effect, we tried to think about what it might mean as an archetype. What kind of deck would you imagine he'd be played in. For starters, he's white-blue, which means he would lean toward a more controlling deck.


Okay, he's part of the government and the control aspect thematically makes sense. Also, his power set would be good for restricting an opponent. What if we made a card that helped you in a control deck? His first ability shuts down creatures. He can figure out their weaknesses and use that to slow them down. Makes sense.


His second ability is more defensive. It allows him to both help survive and improve your card selection. What if the flavor is that by seeing weaknesses, he can take better advantage of the system to gain incremental advantage? His ultimate is also something that helps gum up the opponent. If he can sense weakness, perhaps he can manipulate circumstances to increase problems for them.


When you pull back, you have a Planeswalker that's a bit more reactive, one that makes it hard for the opponent to function as well as they normally do. And that does a decent job of capturing the flavor of Dovin Baan.


"Well, do you?"
===============


That's all the time I have for today. As always I'm eager to hear your feedback on both the article and *Kaladesh*. You can write me [an email](mailto:making.magic@hotmail.com) or talk to me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249), [Instagram](https://www.instagram.com/mtgmaro/)).


Join me next week for Part 2.


Until then, may you create some card-by-card stories of your own.




---

**"[Drive to Work #368—20 Lessons—Make It Personal](http://media.wizards.com/2016/podcasts/magic/drivetowork368_lessonsmakeitpersonal.mp3)"**


This is the seventh podcast in my series "20 Lessons, 20 Podcasts" based on [my GDC speech](https://youtu.be/QHHg99hwQGY) from earlier this year about many of the lessons I've learned in my twenty years making *Magic*. This lesson is "Allow the player the ability to make the game personal."


**"[Drive to Work #369—Lessons Learned—*Khans of Tarkir*](http://media.wizards.com/2016/podcasts/magic/drivetowork369_lessonslearnedkhanstarkir.mp3)"**


This is another in my "Lessons Learned" series, where I explain the design lessons I got from sets I've led. Today I talk about a set I learned a lot from, *Khans of Tarkir*.


* [**Episode 367**](http://media.wizards.com/2016/podcasts/magic/drivetowork367_flux.mp3) Urza's Flux (23.4 MB)
* [**Episode 366**](http://media.wizards.com/2016/podcasts/magic/drivetowork366_ravnicashowdown.mp3) Ravnica Showdown (25.9 MB)
* [**Episode 365**](http://media.wizards.com/2016/podcasts/magic/drivetowork365_urzaslegacypart2.mp3)Urza's Legacy, Part 2 (25.5 MB)






