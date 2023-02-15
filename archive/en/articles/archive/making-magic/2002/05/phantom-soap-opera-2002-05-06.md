
---
[Link to Wayback Machine](https://web.archive.org/web/20210429045415/https://magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "After last week’s anticlimactic story, I thought it only fair to walk you through a Judgment mechanic that had some real evolution. In particular, I thought I would focus on a single card to show how the card went through the design (and development) process. The mechanic is the phantom mechanic and the card is Phantom Nishoba.The phantom mechanic is on a series of white,"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "616076"
[_metadata_:publish_date]:- "2002-05-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Phantom of the Soap Opera"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 04:54:15"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429045415id_/https://magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06"
---


Phantom of the Soap Opera
=========================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on May 6, 2002 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






After last week’s anticlimactic story, I thought it only fair to walk you through a *Judgment* mechanic that had some real evolution. In particular, I thought I would focus on a single card to show how the card went through the design (and development) process. The mechanic is the phantom mechanic and the card is Phantom Nishoba.

The phantom mechanic is on a series of white, green and multi-colored white and green creatures in *Judgment*. Each phantom has a printed toughness of 0 and comes into play with a certain number of +1/+1 counters. In addition, they all have the following line of rules text: “If damage would be dealt to CARDNAME, prevent that damage. Remove a +1/+1 counter from CARDNAME.” 

What this means in short is that each phantom can survive X-1 fights (or other forms of damage) where X is the number of +1/+1 counters it has. That ability makes them very hard to destroy with damage (combat, direct, etc.). To make matters worse (or better if you’re playing a phantom) the replacement effect happens regardless if there’s a +1/+1 counter on the creature. In English, what that means is that if you manage to increase a phantom’s toughness (with, say, a [Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength)), the phantom will never be destroyed by damage. Essentially, when the creature takes damage, the phantom effect prevents the damage, and when it goes looking for a +1/+1 counter to remove, the game just says, “Oh, there’s no +1/+1 counter. Oh well.”

But this is, of course, is the card as you all get to see it. This isn’t always how the card first appeared.

### Zoinks!

The phantom mechanic was designed by R&D member Brian Tinsman. Brain claims his inspiration for this mechanic was trying to come up with something that could simulate a ghost in game terms. He liked the idea of creatures that were extra resilient and would be tougher to destroy than your average creature. To reflect this flavor, the creatures were called ghosts in design.

Here is the earliest version of Phantom Nishoba: 

[Ghostly Earth Wurm]  
 6GG  
 Creature -   
 7/7  
 Whenever damage is dealt to CARDNAME, prevent that damage and put a -1/-1 counter on CARDNAME.

The early version of the card better demonstrates Brian’s flavor. Each packet of damage, regardless of its amount, shrinks the creature by -1/-1. The reason behind the change from this version to the +1/+1 version is rather simple: we don’t do -1/-1 counters anymore. Okay, that’s not exactly true. We do use them occasionally but only in a very specific way. As an example, [Shambling Swarm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Swarm) from *Torment* does in fact use -1/-1 counters, but please notice that they only last until end of turn.

Why do we do that? Because 99% of the time we can mimic the desired effect using +1/+1 counters and the loss of the 1% is worth the clarity that only having one type of power/toughness-altering counters creates. When you look across the table and see a creature with counters on it, you know they are +1/+1 counters. I know this paragraph will prompt a few letters, but please know that I’m currently working on my “why simplicity isn’t evil” column in which I will explain in a much larger context why we do things like that. (As an aside, changing to the +1/+1 counters did add the "[Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) and live forever" trick.)

The second thing you’ll note is that the card was originally green. The reason is simply that Brian didn’t realize we were going to do multi-colored cards when he made the mechanic. (As a quick aside, it’s interesting to note that the plan to use white/green -- and only white/green -- multi-colored cards in *Judgment* wasn’t decided until halfway through the design process.)

### Let’s Give Them a Hand-Off

Here’s the card as it was handed off from the design team to the development team:

[Ghostly Earth Wurm]  
 2GGG  
 Creature - [Spirit]  
 0/0  
 CARDNAME comes into play with five +1/+1 counters on it.  
 If CARDNAME would be dealt damage, prevent that damage and remove a +1/+1 counter from CARDNAME.   
 T: Put a +1/+1 counter on CARDNAME.

Let’s walk through the changes. First, we came up with the idea of allowing one of the ghosts to be able to make itself bigger. Once we attached that ability, we felt we needed to shrink the creature from 7/7 to 5/5, which also allowed us to lower the mana cost.

Next we added some flavor by making the creature a spirit. The design team liked the idea that the phantoms would be ghostly versions of creatures from earlier in the block. We figured that whole herds of white and green creatures were slaughtered during *Torment* and now was the time for payback.

### Let’s See What Develops

Development made a few key changes. First, they decided that they wanted to have a multi-colored phantom (white/green, of course), and they wanted to return it to its former larger size. But they still liked its activated ability. What should they do?

Early on in the development process, a hole opened up in multi-colored. It was then that the development chose to employ a common development technique: they split Ghostly Earth Wurm into two. One half stayed green and kept the activated ability. The other kept the beef and became multi-colored. The former became the card known as Phantom Nantuko, while the latter became [Phantom Nishoba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba).

To jazz the card up a little once it lost its activated ability, the development team added two basic creature abilities. To keep in the flavor of multi-color, the team decided to make one ability white and the other one green. Trample was obvious, since a creature that big needs some way to break through to deal damage. The "[Spirit Link](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+Link)" ability was added as a cool way to use the creature to aid in your defense. As you beat down you are also building up a life buffer, which is particularly important in multi-player games. (See, we really do keep things like that in mind.)

Meanwhile the creative text guys looked back at all the old white/green creatures to see what cool creature they could “kill” to make the phantom. With slim pickings in white/green in *Odyssey* (they didn't want a Phantom [Mystic Enforcer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Enforcer)), the team looked back to *Invasion*. Once they saw [Sabertooth Nishoba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sabertooth+Nishoba) they knew that had their creature.

And thus, [Phantom Nishoba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba) was born.

Join me next week when we explore the Jedi. (And yes, I’m talking about **Magic**).

Until then, may you have a [Dark Banishing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) in your hand when your opponent plays his [Phantom Nishoba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba).

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*





