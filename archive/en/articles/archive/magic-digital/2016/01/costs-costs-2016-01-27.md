
---
[Link to Wayback Machine](https://web.archive.org/web/20160129104610/http://magic.wizards.com/en/articles/archive/magic-digital/costs-costs-2016-01-27)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Alli has behind-the-scenes technical details of the hard work that went into bringing Oath of the Gatewatch to Magic Online."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "978906"
[_metadata_:publish_date]:- "2016-01-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Costs of Costs"
[_metadata_:wayback_capture_timestamp]:- "2016-01-29 10:46:10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160129104610id_/http://magic.wizards.com/en/articles/archive/magic-digital/costs-costs-2016-01-27"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/magic-digital/costs-costs-2016-01-27"
---


The Costs of Costs
==================



 Posted in **Magic Digital**
 on January 27, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











It took a lot of work by a lot of people to bring *Oath of the Gatewatch* to *Magic Online* effectively. That's a statement that's true of most sets, but *Oath* took more than most. As usual, we've made a host of small changes, bug fixes, and improvements to the game—but, unusually for a *Magic Online* set, we have a singular focus with this set. *Oath of the Gatewatch*, for *Magic Online*, is fundamentally about mana costs and the technical details of how they're implemented.


Keeping Watch
=============


Ever since we first previewed Kozilek, the Great Distortion and Wastes, there's been a lot of discussion about what it means to have a colorless mana cost. What does this new symbol mean, and what does it mean to make a new basic land for the first time since *Limited Edition (Alpha)*? (We're not counting snow lands here.)


Here's the short rundown of what it means to *Magic*:


* Colorless mana, the same kind that's been made by cards throughout the history of the game—from Sol Ring to Blighted Fen—matters in a brand-new way.
* The distinction between colorless mana and generic mana is much more noticeable. A pithy way to understand the new template is "symbols match symbols, but everything matches a number."
* There's a new basic land for the first time since 1993, but it doesn't have a land type and only taps for colorless.

Here's the short rundown of what it means to *Magic Online*:


* The entire system of costs, payments, and mana needed to be rewritten from the ground up.
* Seriously. From the ground up.

This took a significant amount of our card set development team's focus for most of the last year to make work. We had dedicated resources to tackling this problem going as far back as the development of *Dragons of Tarkir*, so before the public was meeting Deathmist Raptor for the first time, we were allocating our development time to make what we came to affectionately call "ninja stars" work properly. We got a lot of ancillary wins in the process, and I'll go through them, but I can't stress enough that this really was a tremendous amount of work and there are still some known bugs that we're working through.


Oracle's Insight
================


One of the consequences to *Magic* of introducing a colorless mana symbol is the change to over 300 cards in Oracle, the central database of official card wordings. Oracle feeds both Gatherer and *Magic Online*, and this is important to know because a lot of cards in a lot of players' collections are going to look a little different.


We can't rearrange the ink on all the physical cards that Magic has ever produced, much as I may wish otherwise. In *Magic Online*, however, we *can*. Cards are automatically updated to use the latest correct wording, and with this set that means adding colorless mana symbols all over. Here's what two classic cards look like now: a *Vintage Cube* staple and the notorious original card that caused us to start using the generic mana symbol to represent colorless mana production.


![](https://media.wizards.com/2016/images/daily/MD20160127_Basalt.png)![](https://media.wizards.com/2016/images/daily/MD20160127_Elder.png)


Rapid Hybridization
===================


Paying a cost involving hybrid mana used to be a fairly arduous process. Figure of Destiny, for example, has an ability that costs {R/W}{R/W}{R/W}. Under the old mana system, you couldn't just tap two Plains and a Mountain to activate it. From the menu, you needed to choose the {R}{W}{W} option while being careful not to select the {W}{W}{W} option, or the {R}{R}{W} option, or the {R}{R}{R} option. Activating the third ability had even more options. Now it's easier:


![](https://media.wizards.com/2016/images/daily/medwin_1.jpg)


When you're actually paying the cost, the game will now ask for the hybrid cost like this:


![](https://media.wizards.com/2016/images/daily/medwin_2.jpg)


From here, you can tap those Plains and the Mountain. Or you can tap them first, if you like. Or you can change your mind in the middle and tap three Mountains instead. Hybrid costs finally work in a clear, intuitive fashion, and that's a big win for the new mana system.


Generating Success
==================


With the release of *Magic 2015*, the holes in the automatic payment component of the game's mana system caused a lot of problems for players. Consider Generator Servant:


![](https://media.wizards.com/2016/images/daily/MD20160127_Servant.png)


In that set's Limited format, it was a pretty good play to use Generator Servant to help cast two creatures in the same turn, granting each of them haste. Lots of people did this in paper. Few did it online.


The problem was that the game didn't recognize the colorless mana generated by the Servant as distinct from any other colorless mana for the purposes of automatic payments. If you were casting a Borderland Marauder, or another creature that had only one generic mana in its mana cost, you could manage. Even then, you needed to cast the Borderland Marauder first so the automatic payment would consume one of the Generator Servant mana without consuming the other, then you could cast the other creature and end up with two haste creatures. It was...obtuse.


This wasn't a new problem with *Magic 2015*, though it was pretty recent and notable. Consider also Firespout:


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Firespout)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout)
Let's say you've got two colorless, one red, and one green mana in your pool, and you wanted to cast a Firespout in your hand with {C}{R}{G}. There was literally no way to accomplish what you wanted to do. The menu on the Firespout card had a "Cast for {2}{R}" option and a "Cast for {2}{G}" option, but no "Cast for {1}{R}{G}" option.


With the new, refactored mana system, players have significantly more control over the way they spend mana. You can sacrifice the Generator Servant, have that mana in your pool, and cast two creatures how you want to. You can tap a Sol Ring and Gruul Turf, then cast Firespout with both red and green.


While we're very proud of the gains that we've been able to make with the mana system so far, we're not finished yet. The F8 function (yield when no plays exist) doesn't work correctly at the moment. Additionally, the new system currently has almost no automatic consumption of mana. These are both areas where we're looking to restore and expand functionality in the near future. The current plan we're working on—and this is not a promise of what the future will hold—is that ultimately we'd like to end up with a system that automatically consumes mana intelligently. It's not ideal if you're asked to click mana in your pool when the converted mana cost of the spell you're casting is the same as the amount of mana in your mana pool, or if there's no choice in the types of mana you could use to cast a spell (perhaps if you have {W}{U}{U} in your pool when paying a {1}{W} cost).


Single Card Stories: Bonds of Mortality
=======================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bonds+of+Mortality)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bonds+of+Mortality)
Every set has key cards and important mechanics. *Oath of the Gatewatch* wouldn't be the same thing without colorless mana costs and Kozilek, the Great Distortion. *Battle for Zendikar* needs to work with the exile zone. These things are easy to prioritize: the most important things to the set are the most important things to the digital implementation of the set. And when things are worth that work, like colorless mana costs, we're happy to invest the necessary resources to implement them.


Some things, though, aren't important to the set but still take a lot of work to code properly. The classic example is *Born of the Gods*'s Whims of the Fates, which taught us a [hard lesson in cross-department communication](http://magic.wizards.com/en/articles/archive/daily-deck/born-digital-gods-2014-02-12).


Also from that set was the [Archetype cycle](http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&name=+%5b%22Archetype%22%5d&set=+%5b%22Born%20of%20the%20Gods%22%5d). These cards seemed fairly innocuous, but had an exciting new template doing a new cool thing: keeping objects from gaining abilities. Previously, for example, if we wanted to get around the opponent's creatures' hexproof ability, we'd use words like on Glaring Spotlight. Archetype of Endurance went one step further, and kept your opponents' creatures from even having the ability, removing it and preventing the gain. That's neat in paper, but it turned out to be challenging in digital. There's no one way to have a game object gain an ability, you see, so each card that granted hexproof (or flying, or first strike, etc.) had to have a hard-coded interaction with the appropriate Archetype preventing that ability from being gained. It was a time-consuming process, and it was spent on a cycle that wasn't even all that important to the set.


Two years later, as we're wrapping up work on the paper *Oath of the Gatewatch* set, I noticed the following line of text on the card that ended up becoming Bonds of Mortality:


"Creatures your opponents control lose hexproof and indestructible and can't have hexproof or indestructible."


After learning the lesson from the Archetypes, we had a series of conversations with Lead Developer of *Oath* Ian Duke to figure out how we could tweak this to be easier to code. At first, he pointed out that we'd already used this exact template, but as we explained the nature of the problem, he agreed that changing the card was the best option we had. The card couldn't change too much, though, because it was designed to show the crucial moment in the story when Jace and Nissa render the previously invincible Eldrazi titans mortal. After discussing several alternative designs, we eventually arrived at what you can see in packs, and all was well.


I don't know how many hours of work we saved, not exactly. That's hard to gauge, but it was a nontrivial amount. I've talked several times about prioritization, and one of the ways that we can accomplish more with the same resources is to identify these points where a little collaboration is a highly efficient use of time, letting us spend developer hours elsewhere. On this of all sets, saving even a small number of those precious developer hours was a worthwhile and notable success.


Deck Clarity
============


One of the most important things a user interface must be is *clear*, especially when the user is being asked to give up or trade resources. In a game of *Magic Online*, this might mean making sure the player can't mistake which creature an ability is targeting. Outside of a duel, that can mean making sure the store interface is grokkable, or asking a player to confirm a trade after submitting it.


One place that we've added clarity is in the Event Details screen. It used to be possible to have a deck selected in the Play Lobby unintentionally, then have no way to identify the selected deck after opening up an Event Details screen to start playing. This could lead to entering an event with the wrong deck—and if you've ever done that, you know how unfortunate it is. Giving up your entry option and not getting to play the game you were intending to play is a pretty lousy feeling, especially when you feel like you're doing everything right.


So we made a small change. It's designed to be unobtrusive but useful: now you can confirm the deck that you're using directly above the entry option buttons on the Event or Game Details screens for Constructed play. Here's a screenshot of what that looks like in the internal environment we're using:


![](https://media.wizards.com/2016/images/daily/medwin_3.jpg)


Single Card Stories: Deceiver of Form
=====================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Deceiver+of+Form)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deceiver+of+Form)
So let's say you're playing Standard, and you have a face-down Den Protector on the battlefield next to your Deceiver of Form. You reveal a Deathmist Raptor and decide that, why yes, you would like to have your creatures become copies of everyone's favorite deathtouching Lizard Beast. What would you expect to happen?


If you answered "my face-down creature is now a face-up 3/3 deathtouch creature!" then you're in good company. That's not correct, but you're in good company. This very bug was incorrectly entered and heavily discussed during implementation of this set. When it came up, as a former veteran *Magic* judge, I was able to dispel the confusion. It's worth talking about more generally, though, because it's not the most intuitive interaction and I'd hate to see anyone get deceived by the form of their own creatures.


So the thing to know is that every permanent has a *status*, which represents its physical, er...digital state. This covers things like whether it's tapped or untapped, face up or face down, or other categories that are only relevant to older mechanics. Any face-down permanent that becomes a copy of another permanent becomes a copy as you'd expect...but *the face-down status wins*. It doesn't matter if it was cast face down or manifested, the face-down status wins.


If you wanted to turn that card from earlier face up, it would be a copy of the Deathmist Raptor, so you'd be turning it face up by paying a megamorph cost of {4}{G}. You wouldn't get the Den Protector trigger. On the other hand, if you turn a face-down creature into a Den Protector, then you can turn it face up for {1}{G} and get a counter and card out of your graveyard for the trouble!


Another interaction that came up: you might have a Deceiver next to an awakened land. That interaction is also little weird; the land ends up as a copy of whatever, but has a base power and toughness of 0/0 like any awakened land, plus however many +1/+1 counters are on it. Creature lands like Shambling Vent work similarly, except they have the base power and toughness from the activated ability, not the copied creature.


If you want to know more, the [Comprehensive Rules](http://magic.wizards.com/en/gameinfo/gameplay/formats/comprehensiverules) can answer your questions. Look for rule 707.10 for information on the interaction between face-down status and copy effects, then 702.36e for the morph cost that you'd need to pay. It's not actually part of the layer system covered in section 613, but if you're familiar with that section, it can be helpful to think about the face-down status as effectively "layer 1.5."


Gatewatch Out
=============


If you'd like to get in contact with the *Magic Online* design team—and you should, we're a friendly bunch—there are several ways you can send us feedback or questions. The best is the [official *Magic Online* Tumblr](http://wizardsmtgo.tumblr.com/). Game Designer Rob Schuster and I are both on Twitter: he's [@RobertJSchuster](http://www.twitter.com/RobertJSchuster) and I'm [@trulyaliem](http://www.twitter.com/trulyaliem). (Get it? I'm "truly Alli M"!)


We can't reply to everything, of course, but we're very interested in reading all of your thoughts and feedback about how *Oath of the Gatewatch* was implemented!


Until next time, for the sake of the internet, may you keep watch.


Alli Medwin


Digital Editor, *Magic Online*


[@trulyaliem](http://www.twitter.com/trulyaliem)







