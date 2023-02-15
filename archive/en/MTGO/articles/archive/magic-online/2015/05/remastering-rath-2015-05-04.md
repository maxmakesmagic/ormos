
---
[Link to Wayback Machine](https://web.archive.org/web/20150505171852/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/remastering-rath-2015-05-04)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Hey everyone! It’s time for another in my series of articles where I walk through the issues and design concerns that came up with the implementation of a new set. This time, we’re going to go through Tempest Remastered."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "381791"
[_metadata_:publish_date]:- "2015-05-04"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Remastering Rath"
[_metadata_:wayback_capture_timestamp]:- "2015-05-05 17:18:52"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150505171852id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/remastering-rath-2015-05-04"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/magic-online/remastering-rath-2015-05-04"
---


Remastering Rath
================



 Posted in **Magic Online**
 on May 4, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











Hey everyone! It’s time for another in my series of articles where I walk through the issues and design concerns that came up with the implementation of a new set. This time, we’re going to go through *Tempest Remastered*.


This set is a celebration of a time long ago, when [Slivers](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397585) and [Kor](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397638) roamed the shadow realm, when oversized [Rathi Dragons](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397602) dotted the walls of local game stores and [only the fittest survived](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397535). The set is also a fantastic new draft environment that recontextualizes many beloved cards, giving many of them new opportunities to shine, both in gameplay and in new and improved visuals.


It was also a pretty big opportunity for the digital design team. Since all of the cards already existed in *Magic Online*, we were able to focus exclusively on polish and improvements both to the client itself and to the look, feel, and flow of the cards in this set.


Some of these polish improvements you guys have already seen in *Dragons of Tarkir*, and I talked about them in [my article for that set](http://magic.wizards.com/en/articles/archive/magic-online/tark-here-there-be-dragons-2015-04-06): the new appearance of abilities on the stack, targeting comments, etc. So I’m going to try something a little different this time: rather than bring you guys up to speed on new things in *Magic Online* that you’ve seen anyway, let’s talk about things more specific to this set: a few highlights, then a few specific cards.




---

Symbolism
=========


We’ve never made a set quite like *Tempest Remastered* before. The *Masters Edition* sets were similar in that they were also entirely made up of reprints, but those weren’t trying to feel like a specific individual block, so their expansion symbols highlighted the fact that they were a new series. With *Tempest Remastered*, we’re creating something both new and classic at the same time.


The goal for this expansion symbol was to combine the three *Tempest* block expansion symbols into one, while still calling to mind each of the original three. After a number of different designs and iterations, we settled on something that accomplished that goal. By combining the lightning bolt from *Tempest*, the keystone of *Stronghold*'s portcullis, and the arc shapes of *Exodus*'s bridge, a new symbol came together, which is both unique and an homage to what’s come before.


This image that I got from R&D’s art team might help you see it. And once you see it…


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img1.jpg)


…you’ll never un-see it. Them. It. You know what I mean.




---

Art in Frame
============


During the testing phases—we have weekly internal tournaments both to catch bugs and enjoy the set—one comment we heard internally was that the new art in this set was great.


Except there *is* no new art in this set.


Part of the process in getting cards ready for print is to have our Imaging department prepare an intermediate step called an “art in frame,” where the frame is intact, the art is in place, and there’s no text or expansion symbol anywhere on the card. It’s pretty breathtaking, honestly, to contrast these cards with the original printed cards. The new frames are clean and let the art stand on its own in a way that most of these pieces have never had the opportunity to do before. Take a look through [the set in Visual Spoiler mode on Gatherer sometime](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&page=0&set=%5b%22Tempest+Remastered%22%5d) and look for yourself.


I’ll just leave a few of them here:


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397621)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397621) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397492)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397492) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397559)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397559) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397602)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397602) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397435)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397435) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397482)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397482)




---

Single Card Stories: Cataclysm
==============================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397399)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397399)


[Cataclysm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cataclysm) is one of the most devastating sweepers in the history of *Magic*, and arguably the most complex we’ve made to date. As a high school student playing shortly after the release of *Exodus* in the mid-90s, I cast this more than then-Standard all-star [Wrath of God](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=4166). I loved that it gave everyone the opportunity to make mistakes, even if it gave me those same chances. Like many Spikes—and I definitely have a good amount of Spike in me—I love the opportunity to win by making better strategic and tactical decisions than my opponent.


Previously on *Magic Online*, [Cataclysm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cataclysm) gave players those opportunities, yes, but also opportunities to make other kinds of mistakes. All the strategic depth was there, but instead of testing just the player’s strategy, it tested the player’s ability to work through the interface. It was a long multi-step process, with a distinct prompt for each card type: you’d click your artifact, your land, your creature, etc. Clicking gave no indication that a given permanent had been selected, but it advanced the process to the next step. There was a Cancel button that let you start all over again, but if you kept going, the spell just resolved once the last click had been made. To solve these problems, we turned to our friend [Sundering Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundering+Titan).


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=212631)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=212631)


[Sundering Titan’s](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=212631) logic was unique: it allowed players to make a complex selection in a single step, where they’re choosing one each of a number of different subsets of cards. And more importantly, it does so optimally. We borrowed extensively from that logic when we were designing the new [Cataclysm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cataclysm) interface, and it ended up in a place that minimizes both time and potential for misclicks.


So let’s walk through it. I’ll be using a testing tool called “Avatar of Congress,” which allows me to set up board states both to test interactions and interfaces as well as to create illustrative walkthroughs like this one.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img2.png)


A reasonable board state for a test game.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img3.png)


Note the prompt box text: “Choose from among permanents you control an artifact, a creature, an enchantment, and a land. *(Click Done to sacrifice the rest.)*” That Done button text informs you that the spell won’t be automatically resolving and gives you a hint at what’s coming. I know that I want to save my [Sundering Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundering+Titan) and [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault), so I’ll click those.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img4.png)


The red glow on the cards indicates that I’ve chosen them. And the Done button appears now, because this is a legal set of permanents to choose: the [Sundering Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundering+Titan) is my artifact, the [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault) is my land, either can be chosen as the creature, and there’s no enchantment to choose.


Still, there are permanents on the battlefield I can click. What if I click my [Dragon Bell Monk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Bell+Monk)?


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img5.png)


The current choices are still highlighted in red, but the Swamps are now dimmed. After all, I can’t choose them now. If the [Dragon Bell Monk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Bell+Monk) is chosen as my creature, then the [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault) has to be my land, and the [Sundering Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundering+Titan) has to be my artifact. Clicking Done now will let [Cataclysm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cataclysm) resolve, and I’ll sacrifice those Swamps. Except I’m not quite done yet.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img6.png)


I clicked on the [Dragon Bell Monk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Bell+Monk). I really don’t care about it. I clicked on a Swamp, and now the other Swamps and the Monk are all dimmed. Here, the Swamp is my land, the [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault) is my creature, and the [Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=212631) is my artifact. 


I click Done now, and the spell resolves.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img7.png)


Now I’ve sacrificed everything that wasn’t part of that selection process.


At each step along the way, all the decisions I had made and could still make were explicitly presented to me, even the bad ones. Nothing was hidden, and the consequence of each button press is very clear.


One of our goals is to allow players to interact with cards in a way that is not only accurate per the rules of *Magic*, but also has an interface that makes it easier, not harder, to make decisions. Ultimately, [Cataclysm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cataclysm) now asks you to think more about making good strategic decisions, not the interface.




---

Single Card Stories: Rolling Thunder
====================================


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397419)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397419)


Spoiler alert: this card is very good in Draft. There are a lot of one and two toughness creatures in this format, and [Rolling Thunder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rolling+Thunder) can provide some significant card advantage by killing a lot of them for only one card.


Casting this card used to be a misleading experience. You were asked to choose a first target, then a second target, then a third target, and so on, etc. There were little displays with a numeral and up/down arrows on each selected target indicating the amount of damage, but the card didn’t let you unselect a target easily. Rather than just click a creature to remove it from the set of targets while you’re choosing, instead you had to reduce the damage you planned to do to it to zero. This wasn’t clear, and I’ve heard several stories of players thinking that you couldn’t undo a targeting decision with this card.


Now, though, it’s clear. Let’s walk through this one too.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img8.png)


I’ve just cast [Bestial Menace](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bestial+Menace), so I have a few creature tokens on the battlefield to target. This is a complex process, so the prompt box gives me helpful instructions here in the reminder text: *(Click a creature or player to target it, then use the arrow buttons to choose how much damage will be dealt to each target.)*


Great, so I’ll click each of the creatures once.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img9.png)


Next I’ll update the damage I’d like to deal, to be sure to kill them all.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img10.png)


And let’s say that I changed my mind about killing the Wolf token. One click, and I see this.


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img11.png)


And once I click OK, the spell resolves and only the Wolf is left on the battlefield.


And of course, while the [Rolling Thunder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rolling+Thunder) is the top object on the stack or while you’re pointing to the spell with your cursor, you’ll see targeting comments indicating the amount of damage it’s going to do to each creature.




---

Single Card Stories: Cursed Scroll
==================================


[Cursed Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursed+Scroll), when you activate it, asks you to name a card. But this is bigger than that: It’s about how you name a card.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=397653)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397653)


I started ~~playing with~~ losing to this card in high school when I worked at my local game store and my boss built a Standard deck (then called "Type 2") that seemed like pure card advantage. If you can’t beat them, join them, I reasoned, so I traded for a few and learned from my defeats. I’ve played this card in Standard, Block, and Cube. I’ve activated it with one card in hand, and I’ve activated it with six cards in hand. And over all that time, I can count the number of times I’ve named a card that wasn’t in my hand *on* my hand.


Far and away, the most common use for a player to activate a [Cursed Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursed+Scroll) is to name a card in his or her hand to try to get that damage. So we’ve updated the way that [Cursed Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursed+Scroll) works now, and I’ll let the reminder text speak for itself here:


![](http://www.wizards.com/mtg/images/digital/magiconline/R&D_TPR_img12.png)


Now, you’ve always been able to start typing a card name to scroll right to it on lists like that. Anything that has you naming a card, creature type, etc. works like that. It’s one of those features, though, that we didn’t do a great job advertising. Now the prompt box reminds you of this when you’re naming cards, and hopefully it’ll be more clear to people that they can save some time.


But that isn’t the most exciting part of this reminder text: *“…or click a card in your hand to name that card.”* Starting with *Tempest Remastered*, when you activate a [Cursed Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursed+Scroll), you don’t even need to worry about the list unless you’re bluffing. Just click the card in your hand. It’s [stunningly quick.](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397466) 




---

Reminder Text Reminder Text
===========================


I’ve talked before about the importance of this text in helping players make decisions. It’s worth noting that one of the lessons we’ve learned with reminder text in general is this: when you need it, it’s awesome. When you don’t, you ignore it.


That’s why part of the prompt box text here is italicized, because as *Magic* players, we’re all used to seeing text that you want to read the first time and only rarely read later as italics. It’s not strictly necessary to know; the game is asking you to perform the action on the card, and if you know the card, you know roughly what you’re doing. But just as reminder text carries some of the weight of *Magic*’s complexity in paper, *Magic Online* reminder text carries some of the complexities of the interface’s weight.


*Magic* is a complicated game. The more we can make it simple to use while maintaining the depth of its complexity, the better.


Until next set, may every old spell you cast be new again.


Alli Medwin  

Digital Editor, *Magic Online*  
[@trulyaliem](https://twitter.com/trulyaliem)







