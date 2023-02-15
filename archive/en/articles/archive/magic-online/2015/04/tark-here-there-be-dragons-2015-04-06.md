
---
[Link to Wayback Machine](https://web.archive.org/web/20150409004537/http://magic.wizards.com/en/articles/archive/magic-online/tark-here-there-be-dragons-2015-04-06)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Welcome back to another R&D Dragons! As with previous sets, I’m going to walk through some of the design challenges and decisions that came Dragons with Dragons of Tarkir. These savage behind-the-Dragons looks are ruthlessly important to keep everyone up to speed on what we’re all doing, because waiting to learn about a cunning new set shouldn’t be a matter of endurance. This one in particular was a Dragons fun set for us to work on (because Dragons), and I’m really excited to show you all some of the designs we Dragonsed up for this Dragons. Dragons."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "draft"
[_metadata_:publish_date]:- "2015-04-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Tark-Here There Be Dragons"
[_metadata_:wayback_capture_timestamp]:- "2015-04-09 00:45:37"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150409004537id_/http://magic.wizards.com/en/articles/archive/magic-online/tark-here-there-be-dragons-2015-04-06"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/magic-online/tark-here-there-be-dragons-2015-04-06"
---


Tark-Here There Be Dragons
==========================



 Posted in **magic online**
 on April 6, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin










Welcome back to another R&D Dragons! As with previous sets, I’m going to walk through some of the design challenges and decisions that came Dragons with *Dragons of Tarkir*. These savage behind-the-Dragons looks are ruthlessly important to keep everyone up to speed on what we’re all doing, because waiting to learn about a cunning new set shouldn’t be a matter of endurance. This one in particular was a Dragons fun set for us to work on (because Dragons), and I’m really excited to show you all some of the designs we Dragonsed up for this Dragons.


Dragons.




---

Now Look Here…
==============


Our team is always looking for ways to improve the way *Magic Online* looks and feels. It’s a constant process, and to that end, we’ve designed a new look and feel for abilities on the stack. The old look and feel was created based on the frames created for *Eighth Edition*, and it fit well enough at the time. Just as printed and digital tokens got updated with *Magic 2015*, though, we felt it was time to update the way abilities on the stack here too. We wanted abilities on the stack to look distinct from cards on the stack, yet feel like they’re part of the *Magic 2015* frame set.


We’re also—and this is very exciting to me as an editor-slash-*Magic*-rules-goob—getting rid of the unclear and unhelpful “FX: triggered ability from” text that appeared on the previous abilities.


So without further ado, here’s one of my favorite triggered abilities in all of *Dragons of Tarkir*:


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_1.png)


And here’s what that looks like in a game:


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_2.png)


She’s so hungry!




---

Choose Any Number of Target Creatures
=====================================


While we’re improving the look and feel, we’re also interested in improving the clarity of the information presented to players in game. Previously, casting a spell with multiple targets that affected different targets in different ways could lead to some frustrating moments. Let’s look at the problem and our solution with a scenario involving a *Khans of Tarkir* Limited experience from a few months ago:


I’m playing my boss Ryan, and I cast [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth) targeting three of my creatures. They’re each 1/1, but they’re about to become 2/2, 3/3, and 4/4. He’s got a couple of 4/4s, but he can’t handle me having a creature big enough to trade with one of his. I’m pretty sure I’ve got this locked up… except he has cards in his hand.


One of them is [Winterflame](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winterflame). So he can kill the creature that’s slated to get three +1/+1 counters, keeping me from having a good attack. Just… which one is it? He can check the game log, right?


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_10.png)


Oops. They’re all Goblin tokens. Here’s the problem: the client buried the information he needs. For him to find out, he has to read the game log entry carefully, use the mouse to point to the third instance of the word “Goblin” in the game log entry pictured above, then remember which Goblin it was when he was clicking on it. It’s possible, sure, but it’s harder than it needs to be and there are a lot of ways this could go wrong. Good odds for me, but it’s an unsatisfying way to win a game.


So how do we solve this problem?


The solution came from the same tool we use when we’re identifying the spell to the player casting it during the casting process. We call them Target Comments, and they’ve been a useful tool to help people cast spells. Now they’re also useful to identify the spell as it’s on the stack, so you have full information as you want to respond.


If this were to happen again, here’s what we’d see: My [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth) on the stack, targeting three Goblin tokens.


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_3.png)


With his [Winterflame](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winterflame) on the stack, I know which creature will be shocked and which will be tapped.


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_4.png)


And if you point the cursor to the [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth), even with the [Winterflame](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winterflame) on the stack, you can see what the Growth is doing.


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_5.png)


So now the [Winterflame](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winterflame) has resolved…


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_6.png)


And now the [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth) finally resolves. Much less exciting for my Goblins, but maybe this way Ryan can beat me.


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_7.png)


Ultimately, the goal of any good interface is to help you, the user, understand what’s going on. With these enhanced targeting comments, we’re making a pretty big leap forward in clarity.




---

Single Card Stories: [Archfiend of Depravity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archfiend+of+Depravity)
==============================================================================================================================


Let’s talk about design philosophy for a minute. Over the last year and change, we’ve had a shift in design philosophy: we began to focus a lot more on nuances like order of actions performed, the way we present information, etc. Most of my previous articles are based on that theme: If a card says to perform an action, we ask you to perform an action. (And, increasingly, we then tell you in a parenthetical comment where to click to make that happen, just in case it isn’t clear.)


[Archfiend of Depravity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archfiend+of+Depravity)’s triggered ability reads “At the beginning of each opponent’s end step, that player chooses up to two creatures he or she controls, then sacrifices the rest.” As a result, the client asks you to perform the same action as the card: choose up to two creatures you control.


So you perform the action, you move to the next step, then… whoops, you clicked through too quickly? Sorry, you lose all your creatures. Zero is a perfectly legal number to choose for “up to two” after all, and we have to allow you to make all legal decisions you could make with a card, however unusual. Unfortunately, this happened far too often, and it was almost never deliberate.


If a couple of people misclick trying to resolve a card, that’s an unfortunate part of playing *Magic Online*. When lots of people misclick trying to resolve that card, it’s on Design to improve that experience. After a lot of discussion, we ended up making three changes for [Archfiend of Depravity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archfiend+of+Depravity), each one coming with lessons for the future.


The first change we made was simple: replace the button. Simply by changing the button from “OK” to something else we remove the ability for players to use their keyboard shortcut (F2 by default) to bypass this step. Since a lot of people play *Magic Online* with a finger on that shortcut, this forces those players to stop and pay attention to what they’re doing.


The second change was to add more text to be helpful. The new button is labeled “Sacrifice,” and we’ve also added reminder text that’s explicit in what happens as soon as you press the button. Once you’re playing, this is what you’ll see:


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_8.png)


I did say there was a third thing, and here it is: if you could choose more creatures than you’ve chosen, but you click Sacrifice, the game asks you for a confirmation click. *Magic Online* is typically a complex enough game that confirmation clicks are usually more of an inconvenience than helpful. There are so many decisions to make during a game of *Magic*, digitally or in person, that asking you to verify each action is just impractical.


What we learned from [Archfiend of Depravity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archfiend+of+Depravity) is that for those mistakes that are so wretched and so painful, but so simple to make, we should put in that extra step. It’s not going to show up often. Right now, I’d be surprised if it shows up even a handful of times per set. But it’s a tool in the toolbox when we need it. If we made [Door to Nothingness](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Door+to+Nothingness) today, for example, targeting yourself would probably call for such a confirmation click.


And while I’m talking about confirmation, let’s show you the confirmation step. After all, if you really want to sacrifice all your creatures, you still can.


![](http://www.wizards.com/mtg/images/digital/magiconline/4-6_img_9.png)




---

On the Horizon: New Foil Treatment
==================================


Previously in this space, Jon Loucks would preview things that we were working on with the understanding that such a preview wasn’t a promise or guarantee that things would turn out that way. I’ve spent most of these articles avoiding that, because most of the things that have been going on behind the scenes are pretty unexciting. Leagues is in progress, of course, but aside from that we’ve been focusing our efforts, [like Worth said here](http://magic.wizards.com/en/articles/archive/mtgo/magic-online-2014-executive-summary-2015-02-23), on fixing annoyances and bugs, improving performance and the like.


Every so often, though, while we explore solutions to those problems, we figure out something new and cool that we can implement without detracting from that primary mission. This built on the development we did around *Fate Reforged*’s premium cards’ lenticular watermarks—the ones you can see on premium versions of [Crux of Fate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crux+of+Fate) and the five [Siege](http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&name=+[siege]&set=+[%22Fate%20Reforged%22]) enchantments—and some other optimizations that our programmers are working on. Hopefully someday soon I’ll be able to talk about this again without the “just an exploration, no promises” caveat.


What is this, you ask?


Oh, just a new foil treatment that’s both better-performing and much, much cooler-looking. Stay tuned. We’ll have more on this soon, including (hopefully) some preview images!


Until next set, may your opponent always click Sacrifice to confirm he or she wants to be eaten by a Dragon.


Alli Medwin  








