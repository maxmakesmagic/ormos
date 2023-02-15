
---
[Link to Wayback Machine](https://web.archive.org/web/20191007172413/https://magic.wizards.com/en/articles/archive/making-magic/eldraine-check-part-3-2019-10-07)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark finishes telling his card-by-card design stories from behind the scenes of Throne of Eldraine."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1491191"
[_metadata_:publish_date]:- "2019-10-07"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Eldraine Check, Part 3"
[_metadata_:wayback_capture_timestamp]:- "2019-10-07 17:24:13"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20191007172413id_/https://magic.wizards.com/en/articles/archive/making-magic/eldraine-check-part-3-2019-10-07"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/eldraine-check-part-3-2019-10-07"
---


Eldraine Check, Part 3
======================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on October 7, 2019 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






I've spent the last two weeks ([last week](https://magic.wizards.com/en/articles/archive/making-magic/eldraine-check-part-2-2019-09-30) and [the week before that](https://magic.wizards.com/en/articles/archive/making-magic/eldraine-check-part-1-2019-09-23)) sharing card-by-card design stories from *Throne of Eldraine*. I had a lot of stories to tell, but I think one more article should cover it.


Once Upon a Time
================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Once+Upon+A+Time)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Once+Upon+a+Time)
This was another card that was top-down designed from its name. We made it green because the title felt green. Green's all about destiny and fulfilling your role in the world. The earliest version acted like a Leyline that had an effect if you drew it in your opening hand. It was then changed to be free if it was the first spell you cast, which is similar, but felt like a slightly different mechanical space. We wanted it to do something you'd want to do first, and something green, so we made it an "impulse" spell (R&D slang for a spell that only looks at a limited number of cards from the top of your library and lets you take one—in our quest to lessen shuffling, it's how we do a lot of "[tutoring](http://magic.wizards.com/en/articles/archive/play-design/m-files-hour-devastation-part-1-2017-07-14#tutor)" these days) that got you a creature or land.


Piper of the Swarm
==================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Piper+of+the+Swarm)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Piper+of+the+Swarm)
Another creature on our long list of fairy-tale tropes was the Pied Piper of Hamelin. He was a character who had the ability to summon rats by playing his pipe. As the story goes, he comes to the town to clear away all the rats by luring them out of town with his magical pipe, but when he gets stiffed by the town for the payment of the job, he ends up luring all the children in the town with his pipe. It's a meaty trope to work with. Here's our earliest design:


Pied Piper (rare)  

3B  

Creature — Human  

At the beginning of your upkeep, create a 1/1 black Rat creature token.  

Sacrifice three Rats: Gain control of target creature.  

2/3


The basic design was twofold. We wanted to demonstrate that he could summon Rats and that he could also lure Humans. We started by giving him an ability to create 1/1 black Rat creature tokens. We felt an upkeep effect would create them at the right rate but also be impressive enough for a rare. The second ability played into something we don't do often in black, creature stealing. Black is tertiary in creature stealing, and it's something we get to do on occasion. This felt like a great place to use it. To limit how often he could use the ability, we tied it to the sacrifice of three Rats.


Set Design kept the basic framework but tweaked a lot. First, instead of getting the Rats for free every turn, you now have to pay 1B for them. To limit the ability to one Rat per turn, they gave it a tap cost. The bigger change, though, was adding a bunch of mana to the creature-stealing effect. It turns out *Magic* has a lot of other Rats, and it proved a little too easy in playtesting to steal creatures. The ability was also given a tap cost to limit you to only stealing one creature per turn. Then, as this card was clearly encouraging you to play Rats, they gave the creature a static ability that helped Rats, granting them menace. This allowed you to have a second route to victory other than stealing creatures. You could just make a lot of Rats and swarm the opponent. Finally, they changed the creature from a 2/3 for three and a black mana to a 1/3 for one and a black. This allows you to get it out a bit earlier and start making Rats.


The one last thing to note about this creature is its creature type. We decided for *Throne of Eldraine* that we wanted to add a new spellcasting creature type, one that represented the darker side of spell casting. This ended up being Warlock, and the Piper seemed like a good fit.


Seven Dwarves
=============


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seven+Dwarves)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seven+Dwarves)
My original plan for *Throne of Eldraine* was that we'd have exactly seven Dwarves in the set. The first time I mentioned this to the Creative team, they stressed it was a bad idea. Cards are going in and out of files constantly, and our ability to tightly control exactly how many of a certain type of card are in a set is harder than you might imagine. Also, seven creature slots takes up a lot of space. Was there a way to make a nod to the seven Dwarves with just one card?


I tried attacking the problem from a different vantage point. What exactly did I want out of the card? I wanted seven Dwarves. How could one card do that? It could be a sorcery that makes seven 1/1 red Dwarf creature tokens, but we were already doing that gag with the three bears. What if I helped you get seven Dwarf cards on the table? I couldn't do that with one card, though, as deck-construction limits would keep you to four. But wait, they didn't have to. What if we made a Dwarf card that let you have seven—not any number, but specifically seven in your deck? That seemed like an interesting space to explore. Here's our first attempt at the design:


Dwarf Miner (common)  

2R  

Creature — Dwarf  

A deck can have up to seven cards named CARDNAME. When CARDNAME enters the battlefield, you may search your library for any number of cards named CARDNAME, reveal them, put them into your hand, then shuffle your library.  

2/2


The first design was heavily influenced by cards like [Squadron Hawk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk) that let you get extra copies of itself. Because you had seven cards in your deck and a seven-card hand limit, the way this tended to play out is that you didn't get all the Dwarves at once, which led to a lot of deck searching and shuffling. In the end, we liked the seven-card limit, but decided to go a different way.


One of the avenues that got explored was trying something in the vein of [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) where they get more powerful as you get more of them. This seemed exciting and would encourage playing all seven copies in your deck as the power of the cards scale with how many you have on the battlefield. After trying various tweaks on [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats), we ended up basically just using the [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) text, but shifted to red. I think the first version made them cost one and a red mana instead of two and a red, as we knew [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats) were a little on the weak side. Set Design would later make then 2/2s. I'm hoping to hear some classic tales of a seven-Dwarf victory.


Spinning Wheel
==============


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Spinning+Wheel)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spinning+Wheel)
You might remember my preview article where I talked about discovering how fairy tales tend to be composed of components that are shared across various stories. Well, it was the design of this card that led me to this realization. Early on, we'd made a giant list of tropes so that we had stuff to top-down design from. One of the cards on the list was the spinning wheel from Sleeping Beauty. It's the item she pricks her finger on that leads to her falling victim to the sleep spell. That design was pretty simple. It could be an artifact that taps creatures (as sleeping in the set was being represented by being tapped—see, for example, [Charmed Sleep](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charmed+Sleep)).


I then realized that there was a completely different spinning wheel from a fairy tale—the one from Rumpelstiltskin. That's the device he uses to spin straw into gold. Oh, that's also a simple design. We could make an artifact that creates Gold tokens (as we did with the early Golden Goose). But which should we do? Both were such classic fairy-tale tropes. The obvious answer didn't take long, why not do both? How do we make this card different from other cards? Use the overlapping flavor to create a card that does both things. You can use this spinning wheel to put someone to sleep or make Gold. I always talk about how I'm excited to find designs that we couldn't make in another set. The flavor allows us to combine things that might normal feel disconnected. Using the overlapping trope space allowed us to make some interesting card designs.


Here's the earliest version of the design:


[Spinning Wheel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spinning+Wheel) (uncommon)  

4  

Artifact  

3, T: Create a colorless artifact token named Gold. It has "Sacrifice this artifact: Add one mana of any color to your mana pool."  

1, T: Tap target creature.


Gold would later leave the set, and the gold making turned into the more straightforward mana production of any color.


Trapped in the Tower
====================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trapped+in+the+Tower)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trapped+in+the+Tower)
This is another top-down card that was designed very early in vision design. Common white needs a [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism)/[Arrest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arrest) variant, and this seemed like it was a good flavor fit. It just needed one small tweak. One of the things that makes top-down designs very charming is that they have a little bit of extra text that's flavorful even if it doesn't come up all that often. Here's the first design:


Locked in the Tall Tower (common)  

2W  

Enchantment — Aura  

Enchant Creature  

Enchanted creature can't attack, has reach, and can only block creatures with flying.


The idea was that the creature is trapped in a tower, so it can't attack, but because it's up in the air, it can block fliers. The flavor seemed cute. The problem was that people treated it like a [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) and just assumed it couldn't block, so people were constantly attacking with fliers only to be surprised that Rapunzel was blocking their flier. As I always say, when players keep making the same play mistake, that's usually a sign that there's something wrong with your design.


The new version shifted from a [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) variant to an [Arrest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arrest) variant (stopping activated abilities in addition to attacking and blocking) and communicated the flavor by only being able to enchant non-fliers. You can't lock a flying creature away in a tower. Normally, white has no problem stopping fliers, but the flavor was so strong that we decided to add it to the card. We made it a restriction of the enchantment for two reasons. One, it made it clear who you could and couldn't use the enchantment on, and two, it allowed you to use a [Flight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flight) effect (something that grants a creature flying) to break them free from the enchantment (if the creature gains flying, the aura falls off as it can only enchant a creature without flying).


I also want to point out that originally [Bake into a Pie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bake+into+a+Pie) was a [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism)/[Arrest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arrest) variant. In vision design, especially when we're doing top-down designs, we allow ourselves to overlap executions of a particular effect, so that we can see which one we like better. This was another reason, by the way, that [Bake into a Pie](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bake+into+a+Pie) moved from white to black.


True Love's Kiss
================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=True+Love%27s+Kiss)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Love%27s+Kiss)
Once we made [Charmed Sleep](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charmed+Sleep) a lockdown card, the next step was to make a spell that would free you from it. Obviously, it had to be called [True Love's Kiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Love%27s+Kiss). Here was our first attempt at the design:


[True Love's Kiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Love%27s+Kiss) (common)  

W  

Instant  

Destroy target enchantment. Gain 3 life.


We only had it destroy enchantments because, at the time, that was the only thing you needed [True Love's Kiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Love%27s+Kiss) to free you from. Then we made [Glass Casket](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glass+Casket). [Glass Casket](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glass+Casket) made perfect sense as an artifact, but it felt wrong to us that [True Love's Kiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Love%27s+Kiss) could save Sleeping Beauty, but not Snow White, so we changed this card from just destroying enchantments to destroying artifacts or enchantments.


We liked the life-gain rider as this set uses gaining life mechanically to represent being happy, but Set Design wanted to distance the card converted mana cost–wise from [Return to Nature](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Return+to+Nature) (*Throne of Eldraine*'s [Naturalize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) variant), so the life gain was changed to card draw (white, like all colors, gets cantrips). Also, because we like subverting tropes, we had this card showing a woman freeing a man from the curse rather than vice versa.


Wicked Guardian
===============


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wicked+Guardian)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wicked+Guardian)
This card is a top-down evil stepparent. In fairy tales, if your parent gets remarried, it's always to someone horrible that makes your life miserable. How could I capture this on a *Magic* card? I started with the color. The cruelty, the pettiness, the vanity—it seemed pretty black. The thing I wanted was a creature that harmed other creatures to make itself better. Here's the earliest version:


Evil Stepmother (uncommon)  

2B  

Creature — Human Rogue  

B: Target creature you control gets -1/-1 until end of turn and CARDNAME gets +1/+1 until end of turn.  

2/2


The idea of this design was that it was basically a Shade, but one that required others to suffer for it to get bigger. Its strength would come from hurting others. That felt pretty step parent-y (the fairy-tale trope kind, mind you).


While super flavorful, it made for a complicated board state. To attack, you not only had to track how big the [Wicked Guardian](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wicked+Guardian) could get but also what creatures would have to shrink to allow that to happen. The card was eventually changed to keep the same flavor but in a way that was easier to track. Now, the card damages something as an "[enters the battlefield](http://magic.wizards.com/en/articles/archive/play-design/m-files-hour-devastation-part-1-2017-07-14#enters-the-battlefield-effects)" effect. If it's small enough, it kills it, but if it's bigger, it weakens it for the turn, making it more vulnerable. Instead of getting bigger, the creature now draws you a card.


Wicked Wolf
===========


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wicked+Wolf)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wicked+Wolf)
Back in 2017, I had an article called "[Mechanical Color Pie 2017](https://magic.wizards.com/en/articles/archive/making-magic/mechanical-color-pie-2017-2017-06-05)" where I walked through the mechanical breakdown of the entire color pie. In it, I had the following entry:


Banisher Priest–like effect (When this card enters the battlefield, exile target creature/permanent until this card leaves play.)


Primary: white  

Secondary: blue and green


This is one of white's most efficient answers, especially in Limited. It is usually used on creatures but sometimes hits other permanents. The effect is always on a permanent, usually a creature or enchantment. We've used this effect in blue and green as an enters-the-battlefield trigger with the flavor that it's "eaten" the creature.


This entry raised a lot of eyebrows as green has never done this effect. When I was asked about it on my blog, I said it was something I was trying out in an upcoming set. This was the card I was trying it out on. Here's the original card design:


Big, Bad Wolf  

3GG  

Creature — Wolf  

When CARDNAME enters the battlefield, exile target creature an opponent controls with a power less than CARDNAME until CARDNAME leaves the battlefield.  

3/3


The flavor was simple. The Big, Bad Wolf shows up and eats one of the opponent's creatures, although, something smaller than himself (defined by having a smaller power—note that you could [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in response to the enters-the-battlefield effect to allow the Big, Bad Wolf to eat bigger creatures). The Big, Bad Wolf then "spit the creature back up" when it died. I was playing into one of the versions of Little Red Riding Hood where Red and her grandma get eaten but are later found alive in the wolf when the huntsman kills the wolf and cuts it open.


I thought it was pretty flavorful, but too many others felt it was too much of a departure for green, so the card got changed. The new version played up the danger of the wolf by having it fight when it "enters the battlefield" and allowing it to beef itself up with Food tokens. Since the Big Bad Wolf is most famous from the stories of Little Red Riding Hood and the Three Pigs, the flavor of him always being after food felt right. I also like how this card essentially grants a second ability to your Food tokens.


Wishful Merfolk
===============


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wishful+Merfolk)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wishful+Merfolk)
This was another card that got designed pretty early and didn't change all that much. Here's the original version:


Lovestruck Mermaid (common)  

1U  

Creature — Merfolk  

Defender  

U: Until end of turn, CARDNAME becomes a Human creature in addition to its other types and can attack as though it doesn't have defender.  

2/3


Really, all that changed was numbers being adjusted. She went from a 2/3 to a 3/2, and her activation went from one blue mana to one and a blue. I enjoyed how the defender mechanic communicates that she's a merfolk and thus can't attack, but when she turns into a Human and loses the tail (gaining legs), she can. This card predated the non-Human tribal component of the set, but turned out to play nicely with it as the card has the ability to be either Human or non-Human.


Witch's Oven
============


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Witch%27s+Oven)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Witch%27s+Oven)
The earliest version of this card was a kill card. It was flavored as something you pushed creatures into (ala Hansel and Gretel's handling of the witch that captures them). This was deemed a little too gruesome, and it was later changed to a means to turn creatures into Food tokens (and thus, life). Still a little gruesome, but hey, Grimms' fairy tales were kind of dark.


And They All Lived Happily Ever After
=====================================


And that wraps up my card-by-card design stories of *Throne of Eldraine*. As always, I'm eager to hear your thoughts on today's column or *Throne of Eldraine* in general. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Instagram](http://instagram.com/mtgmaro)).


Join me next week when I start answering all your questions about *Throne of Eldraine*.


Until then, may your games of *Throne of Eldraine* be charmed.




---




 

##### 
 #677: Other People's Lessons – Lessons Learned






##### 
 #677: Other People's Lessons – Lessons Learned




This podcast is another in my "Other People's Lessons" series where I talk top ten lists of lessons for something else and apply them to *Magic* design. Today is life lessons.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork677_lifelessons_MDdwUDs2.mp3)



  


 

##### 
 #678: Small Talk with Sarah






##### 
 #678: Small Talk with Sarah




This is another of my mailbag podcasts where I answer all your questions. I do these with a carpool guest. Instead of "Mailbag with Matt" or "Replies with Rachel," we get the first-ever "Small Talk with Sarah" where my guest is my youngest...

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork678_smalltalkwithsarah_MDeow39D.mp3)





* [**Episode 676**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork676_lessonslearnedwar_gjDeh93U.mp3) Lessons Learned – *War of the Spark*
* [**Episode 675**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork675_bolasarc_DenYr8Ll.mp3) Bolas Arc
* [**Episode 674**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2019/podcasts/magic/drivetowork674_sdcc2019_jYie03eD.mp3) SDCC 2019






