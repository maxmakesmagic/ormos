
---
[Link to Wayback Machine](https://web.archive.org/web/20151014154517/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-zendikarticle-2015-10-12)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Good morning! I’m Alli Medwin, the editor for Magic Online, and each set I make time to go over some of the Magic Online-specific challenges and advances we’re delivering to you with the new card set. Normally I’ve got some really visible stuff to show off, but this time around it’s a little more subtle. I have some user flow improvements to share, of course, and I think you’ll agree that they make gameplay a good bit smoother. And, for a change, I’m going to tell you about about a time where things went more wrong than right. (Not in the title of this article."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "731566"
[_metadata_:publish_date]:- "2015-10-12"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Magic Online Zendikarticle"
[_metadata_:wayback_capture_timestamp]:- "2015-10-14 15:45:17"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20151014154517id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-zendikarticle-2015-10-12"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-zendikarticle-2015-10-12"
---


The Magic Online Zendikarticle
==============================



 Posted in **Magic Online**
 on October 12, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin










Good morning! I’m Alli Medwin, the editor for *Magic Online*, and each set I make time to go over some of the *Magic Online*-specific challenges and advances we’re delivering to you with the new card set. Normally I’ve got some really visible stuff to show off, but this time around it’s a little more subtle. I have some user flow improvements to share, of course, and I think you’ll agree that they make gameplay a good bit smoother. And, for a change, I’m going to tell you about about a time where things went more wrong than right. (Not in the title of this article. I don’t apologize for that at all.)


[Download *Magic Online*](/node/153681)




---

Processing, Zone Controls, and You
==================================


It’s not every game that you need to interact with the graveyard. It’s an even more rare game that you need to interact with exiled cards. Unless, of course, you’re playing with *Battle for Zendikar* Eldrazi, who frequently ingest and process cards through their opponent’s exile zone. So in order to make playing with them easier, we’ve tweaked the behavior of the zones.


Starting from the beginning: On *Magic Online*, the exile zone display is controlled from a series of buttons just under the player avatar.


![](https://media.wizards.com/2015/mtgo/10-6-2015_img1.png)


From left to right, these buttons control the graveyard, the exile zone (it’s the X!), the revealed cards area, and the effects area. Clicking these buttons toggles the display of each of those zones or areas, and they can be closed or opened at will.


So here’s a few images: the left is the start of this test game, the center is after a few turns have gone by, and after a lot of cards have moved around, I ended up with the situation on the right.


![](https://media.wizards.com/2015/mtgo/10-6-2015_img2.png)![](https://media.wizards.com/2015/mtgo/10-6-2015_img3.png)![](https://media.wizards.com/2015/mtgo/10-6-2015_img4.png)


I know from the numbers on the buttons how many cards are in each zone: in the last, the player at the top has sixteen cards in her graveyard and twenty-one in exile, while the one on the bottom has three in her graveyard and two in exile.


Now let’s use one of the Processor cards—I pulled up an [Oracle of Dust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oracle+of+Dust), but it’ll work with any of them—to use up one of those exiled cards.


![](https://media.wizards.com/2015/mtgo/10-6-2015_img5.png)


Two not-new things here: One, the opponent’s exile zone opened up automatically, the same as if I clicked on the X under her avatar. Two, the prompt box clearly says what I’m doing here, and how to do it.


For some time now, these zones have opened up on their own when an interaction is called for. My graveyard, for example, opened a lot last year during *Khans of Tarkir* drafts when I was casting delve spells. And we got a lot of feedback about that. It was mostly helpful, but it made customizing the battlefield layout difficult and manually closing them each time was annoying.


But now, when I click a Plains to process it…


![](https://media.wizards.com/2015/mtgo/10-6-2015_img6.png)


…the exile zone closes back up. And that’s a new change based on a lot of your feedback. It’s a relatively small but substantial change in the way that the zones operate: when a card is done prompting you to do something in one of those zones, if you didn’t have it open already, it’ll close back up. If you had it open, it’ll stay open. If you didn’t care about seeing the graveyard or exile zone before, the game will respect that decision and close right back up as soon as it’s not needed.


After playtesting with this, I’m amazed how much smoother the gameplay feels. I’ve played a few ingest/process decks in our internal testing drafts, and even after working on this change it feels so natural and invisible that I don’t always notice it. That’s a central principle of good interface design: it works exactly as you expect it to in the moment, getting out of your way to let you play the game.




---

Resetting Blockers
==================


Every so often, games of *Magic* get complicated. Combat math can get out of hand really fast. Especially in today’s Standard and in *Battle for Zendikar* draft, there can be a lot of Eldrazi Scions skittering around. With that in mind, we took a look at some of the implications of having large numbers of creatures on the board.


The most serious issue, and the one that came to mind the soonest, was about declaring blockers. This can be a time-consuming and click-heavy process, especially when you’re dealing with cards that create requirements or restrictions, and especially when you have large numbers of creatures.


Previously, choosing blockers in complex board states involved two clicks per blocker and the need to pay careful attention to the entire board. If the blocking declaration was illegal, everything was reset and you had to go through the whole process again. That can be …laborious. I know that sometimes I’ve stared at a complex board state and clicked a bunch only to realize that my opponent’s [Breaker of Armies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaker+of+Armies) (“All creatures able to block [Breaker of Armies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaker+of+Armies) do so.”) was attacking and my set of choices was actually much, much smaller.


In a world populated by large numbers of small creatures, we decided that was an unacceptably poor consequence of trying something illegal. It’ll happen to everyone at some point, and that means something has to change.


So, starting with *Battle for Zendikar*—and previewed on the Community Cup—you’ll see the following while you’re choosing your blockers:


![](https://media.wizards.com/2015/mtgo/10-6-2015_img7.png)


Trying to block illegally, like blocking each attacking Warrior with a single creature after a [Blood-Chin Rager](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood-Chin+Rager)’s trigger resolves, no longer automatically resets the blocking decisions you’ve made. You can reset them if you want with that button, but it’s up to you. The default behavior now is to show you a helpful error message indicating which of those blocking decisions weren’t legal, so you can change them manually. If it’s an easy change, you can make it yourself without having to redo all the rest of the perfectly legal blocks. If it’s a complicated change, on the other hand, go ahead and Reset Blockers if that’s easier for you.


And if you only have seven power of creatures and no tricks when your opponent swings with her [Breaker of Armies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaker+of+Armies), I’m so sorry.




---

Contrast, Clarity, and Comments
===============================


As both an editor and a designer, my favorite word is “iterate”. I’m always interested in looking for ways to make the game better. Even if it’s small, I’ll take it. Given the increased use of targeting comments (both that you guys have already seen and in upcoming sets!), it’s important to make them as readable as possible. We made a color swap for this text that brings it not only in line with the rest of the client, but is much more readable than the old white-on-transparent-gray text.


![](https://media.wizards.com/2015/mtgo/10-6-2015_img8.png)




---

Single Card Stories: [Oblivion Sower](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Sower)
==============================================================================================================


“Didn’t we *just* do something like this?”


I don’t even remember who said that, but it was in a design team meeting and it was the truth: we had just done something similar. And by “similar," of course, I mean "almost exactly the same thing." For the second time in two sets, we part of a spell or ability’s resolution had a player choose a bunch of lands from a zone and put any number of them onto the battlefield. And just like the last time, putting all of the available lands onto the battlefield is almost always the right play.


For those of you who read my [article on *Magic Origins*](http://magic.wizards.com/en/MTGO/articles/archive/magic-online/original-intent-2015-07-27), I went over, briefly, the idea that led us to the “All Lands” button available when resolving [The Great Aurora](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora): streamline the process for the usually-correct scenario. At the time, I said it was new and a little wacky, but a one-button solution saves a lot of clicks and time for the player.


Nothing’s ever new and wacky twice, and a one-button solution still saves clicks and time. Plus, once a card’s flow is built and functions properly, that flow becomes a tool in the toolbox to pull out whenever it’s appropriate. Part of good design is knowing when your existing tools will get the job done. There are other ways this card could have been implemented, of course, but there’s no virtue in reinventing the wheel.


So much like [The Great Aurora](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora), resolving [Oblivion Sower](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Sower)’s ability lets you get all the land at once if you’re so inclined. If you need fuel for your processors, though, you can always click the lands individually and leave some of them in exile.


![](https://media.wizards.com/2015/mtgo/10-6-2015_img9.png)




---

Single Card Stories: [March from the Tomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=March+from+the+Tomb)
========================================================================================================================


This shouldn’t surprise anyone, but the Digital Design team (including me) regularly checks in with the Cardset software development team. These check-ins include previews of upcoming sets so the team is aware of what they'll be working on soon. It’s also important to work with analog R&D to avoid creating cards that would be difficult to program. While the rules engine for *Magic Online* covers a lot of things, it can’t handle everything that the Comprehensive Rules can. The Comprehensive Rules, after all, can handle [Falling Star](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Falling+Star). *Magic* is a complex game and the analog teams are always pushing the envelope and creating new cool things. Our job isn’t to stop cool things from happening at all. On the contrary, we’re looking for ways to keep the essence of the New Cool Thing intact and make it work in digital *Magic*. Huge problems with a card or mechanic can often become trivial challenges with small tweaks that don’t change that essence at all.


This process generally works well, but I’m going to tell you a story of a time it went backwards and a simple card turned into a giant world-eating space monster. And not the cool kind like the Eldrazi.


Once upon a time, [March from the Tomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=March+from+the+Tomb) returned all your Ally creature cards from your graveyard. It also cost more, and it just wasn't doing what the developers wanted it to do. It was very late in development and the card hadn't changed in a while. Through all our check-ins, it just wasn’t a problem. Now, one thing to understand is that most late changes are trivial for *Magic Online*: a mana cost here or a power/toughness shift there, adding or removing existing keywords, these are expected and simple for us. [March from the Tomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=March+from+the+Tomb), however, in order to be fun, exciting, and good for the Standard environment, had to become the card you've all seen with a cap on the number of Ally creatures it could return.


This is, for *Magic Online*, an Ulamog-size problem.


Red flags were raised once the set began coding, but too late to change the card. The trouble is this: the assumptions made when *Magic Online* was first developed didn't foresee that we would, down the road, want to use this specific kind of targeting restriction. As a result, making this card function how we would like—clicking a legal target in your graveyard changing what else is clickable—was next to impossible. Instead, we worked with Cardset and came up with the best rules-accurate way to let players interact with the card: the set of targets chosen is evaluated for legality, and if you choose an illegal set, the game rewinds to just before you began casting the spell. (In case you’re curious, this is thanks to rule 717.1.)


This isn't the ideal interface, but it does work correctly in all cases. More importantly, most times this card will be cast, you'll know what cards you’re planning to choose as targets. In those cases, selecting Ally cards with total converted mana cost 8 or less results in the spell getting cast properly and this issue won't matter. We're looking to improve this further and get an indication in the prompt box to show the total converted mana cost of Allies that you can still select, modeled somewhat after the recent update to [Protean Hulk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk), but that improvement wasn't ready for release.


Software development is hard, and our team works with a lot of inflexible constraints. Part of my job with these articles is to give you that behind-the-scenes look. Sometimes that means taking a hard look at a suboptimal interface that resulted from a technical limitation hitting an imperfect process in just the right way.




---

But Wait, There’s More
======================


I hope you enjoy these regular behind-the-scenes looks as much as I enjoy sharing them, both the successes and the compromises. I think it’s important that you guys know a good amount of what’s going on here. And it seems like you guys agree, because we frequently get feedback asking for more transparency and communication. Read the full *Battle for Zendikar* build notes [here](http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-announcements-october-6-2015#buildnotes).


A few months ago, *Magic Online* Game Designer Rob Schuster and *Magic Online* Events Manager Lee Sharpe started [answering questions from the community on Tumblr](http://wizardsmtgo.tumblr.com/). If you have a burning question for us, or even a lukewarm curiosity, those two fine gentlemen spend hours each week keeping up with and answering questions [on that page](http://wizardsmtgo.tumblr.com/). Sometimes it’s fun and light-hearted—Baby Gideon is *definitely* worth looking for—and sometimes it’s more challenging questions, like why a specific type of event doesn’t happen.


Beyond that, you can always reach the *Magic Online* design team on Twitter: the Design Manager Ryan Spain is [@RyanSpain](https://twitter.com/RyanSpain), Rob Schuster is [@RobertJSchuster](https://twitter.com/RobertJSchuster), and I’m [@trulyaliem](https://twitter.com/trulyaliem).


Until next time, may your blocking decisions never need to be reset.


Alli Medwin  








