
---
[Link to Wayback Machine](https://web.archive.org/web/20150730015309/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/original-intent-2015-07-27)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Hey everyone! Alli Medwin here, the editor for this here Magic Online game. As ever, with the release of a new set, I'm going to share the scoop on what's going on behind the scenes. I'll be reviewing some of the more interesting cards from a digital implementation perspective, some of the challenges that we've come across with this set, and a few of the improvements that you've seen with this build. More than usual, this time I'll be going over some of the areas where we've made technical improvements to the client—some obvious and some mostly invisible."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "426851"
[_metadata_:publish_date]:- "2015-07-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Original Intent"
[_metadata_:wayback_capture_timestamp]:- "2015-07-30 01:53:09"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150730015309id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/original-intent-2015-07-27"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/magic-online/original-intent-2015-07-27"
---


Original Intent
===============



 Posted in **Magic Online**
 on July 27, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin










Hey everyone! Alli Medwin here, the editor for this here *Magic Online* game. As ever, with the release of a new set, I'm going to share the scoop on what's going on behind the scenes. I'll be reviewing some of the more interesting cards from a digital implementation perspective, some of the challenges that we've come across with this set, and a few of the improvements that you've seen with this build. More than usual, this time I'll be going over some of the areas where we've made technical improvements to the client—some obvious and some mostly invisible.




---

Show, Don’t Tell
================


So let's start with information. There's a lot of it. *Magic*'s a very complicated game, and it's a difficult balancing act to find the right amount to show you. Too little information and you lose the ability to make informed strategic and tactical decisions. Too much and you start losing the ability to process everything you see. We don't want to overload you in the middle of your game with so much that it becomes arduous to read and understand, but we also need to give you enough (and in the right places!) to make the best decisions possible.


Historically, our philosophy has been that when you zoom in or right-click on a card, you get information about the current state of that object. After all, when you're mid-game, you generally accept that characteristics of objects change. It's more important that your opponent's [Ugin, the Spirit Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ugin%2C+the+Spirit+Dragon) is now at 11 loyalty than it is that it entered the battlefield with seven. Except that there are times when it matters—every time you have a line of play that involves bouncing or flickering, for example—and when it matters, you want that information handy. Before Origins, you needed to go to the Collection Scene to take a look at how much loyalty [Ugin](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=394086) enters with. Or maybe load up a web browser, go to [Gatherer](http://gatherer.wizards.com/Pages/Default.aspx), and search for the card.


Balancing the quantity of information the game displays is important, but this is actively hiding important information. So starting with *Origins*, we're showing the original loyalty count for planeswalkers when you right-click on one. After using [Nissa](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398432)'s +1 ability, right-clicking on the card shows me, among other things, this:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img1.png)


[Umezawa's Jitte](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte) has caused some frustration lately. When it's equipped to an untapped creature, the creature card covers the counter icon. In order to find out how many counters are on it, and thus what the [Jitte](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=81979)'s controller can do, you've needed to zoom in on the card. There are several ways to zoom in—mouseover the card, then middle-click, hold Z, or right-and-left-clicking—but even when you know how zooming works, the need to zoom in to get that information just isn't consistent with the way you gather information elsewhere. Now, instead of needing to zoom (although zooming still works!), you'll get the information you're looking for using the more intuitive right-click method.


Here’s what that looks like:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img2.png)


And one last thing about displaying information: Zooming in on a card typically shows everything you see in the standard view—except for marked damage. And that’s a weird exception.


If I see this:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img3.png)


I should also see this:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img4.png)


And starting with *Magic Origins*, you will. Showing information is important, being consistent is important, and that’s why we’ve taken these steps to reduce the difficulty of accessing information.




---

Single Card Stories: Alhammarret, High Arbiter
==============================================


[Meddling Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage), the original “Name a card” card, asks players to do just that: “Name a card.”


[Alhammarret, High Arbiter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alhammarret%2C+High+Arbiter) asks players to “choose the name of a nonland card revealed this way.”


These are *almost* the same. If I’m playing these cards at Friday Night *Magic*, then here’s how they’re each going to work:


I cast [Meddling Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage). I think about what my opponent is playing, then I tank for thirty seconds. What outs might my opponent have? What’s her plan? What am I going to lose to? Eventually I make my decision, name a card, and make my next decision.


I cast [Alhammarret](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398436). I look at my opponent’s hand. I think for a few seconds and point to one of the cards. “That one,” I say, and my opponent scowls because that was her plan for the next turn.


*Magic Online* shows the "name a card" dialog whenever you need to name a card. It's important to be able to let you make whatever decisions online that you can in paper, so while you're probably not naming [Camel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Camel) when your Stoneblade deck casts [Meddling Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage), the option's still there for you. [Alhammarret](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398436), however, severely restricts the names you can choose. There's generally no "tank phase" casting him, so there's no need to display the full "name a card" dialog. Really, the only thing you need to do is choose one of the cards the opponent shows you.


Like this:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img5.png)


What we ended up doing was similar to [what we did for Cursed Scroll](http://magic.wizards.com/en/MTGO/articles/archive/magic-online/remastering-rath-2015-05-04), but a step further. Where [Cursed Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cursed+Scroll) gives you the option to name any card you want, in case you want to bluff, [Alhammarret](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398436) doesn't. Since you don't need to have that option, we can dramatically simplify the user experience to a single click.




---

Single Card Stories: Demonic Pact
=================================


If I had a Mox for every time I saw people speculate about the implementation of this card online, my whole family could play Vintage. I'm happy to say that we are, yes, going to have a confirmation click in place for this card. After all, here's the menu that you'll use to put [Demonic Pact](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Pact)'s trigger onto the stack:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img6.png)


Without a confirmation click, I know there’s a pretty good chance that I’d lose to a misclick at some point too. We never want to introduce new risk to cards that isn’t there in paper, and while some degree of that is inevitable, it should be minimized. There are only so many confirmation clicks you should put into a game, and it’s not a large number. So when your Pact’s ability triggers, you’ll click the mode you want to use, and the ability will be put on the stack, showing only the text of the mode chosen. If you choose the "lose the game" mode, perhaps because you're holding a [Stifle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle), control a [Sundial of the Infinite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundial+of+the+Infinite), or just want to see this lovely dialog box, you're presented with this:


![](https://media.wizards.com/2015/mtgo/7-27-2015_img7.png)


If you click "Yes" here, that lethal trigger is put on the stack and you've got one priority pass to do something before the game ends. You'll also get here—without a confirmation click—if you're out of other options to choose. I hope that original bargain was worth it!




---

Single Card Stories: The Great Aurora
=====================================


[The Great Aurora](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora) is a card that's very complicated in paper and almost simple digitally: very operationally complex, but with minimal choices to make along the way. In paper, you need to first count the number of cards in hand, count the number of permanents you control on the battlefield, add them together, scoop them all up together, shuffle, draw a bunch of cards, then put out all of your lands. Or most of your lands. Probably.


Sure, there are reasons to not put out all of your lands. Maybe you have an [Armageddon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armageddon) in hand (you jerk!) and maybe your opponent's just going to kill you with an unearthed [Anathemancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anathemancer) if you put out too many. Or you want to drop three lands to cast your [Seismic Assault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seismic+Assault) so you can discard your lands to just straight-up win. But most of the time, let's be honest, you're going to put them all out.


There's literally no precedent for what we did here. It's not huge either, but it'll certainly save a few clicks.


![](https://media.wizards.com/2015/mtgo/7-27-2015_img8.png)


In the prompt box, you can see that "All Lands" button, and it does what you probably imagine it does: It puts all the lands in your hand onto the battlefield during that step of resolving the spell. I've talked a few times before about balancing the need to keep the complexity of *Magic* intact while making the most common decisions easier, and this is one of the more offbeat ways we're applying that principle in *Magic Origins*.




---

Putting a Premium on Premium Cards
==================================


Back in April, in my [*Dragons of Tarkir* article](http://magic.wizards.com/en/articles/archive/magic-online/tark-here-there-be-dragons-2015-04-06), I mentioned that we had a new premium card treatment coming. I'm happy to announce that, as of the release of *Magic Origins*, it's here! In addition to being much more noticeable and snazzy, this new color-shifting animation is one of several recent performance enhancements that we've been putting out lately. This one is certainly the most dramatic, but it's hardly the only one.


This isn't exactly what you'll see in the client, because the conversion to this image format cost some detail, but it's pretty close.


![](https://media.wizards.com/2015/mtgo/foil-thunderclap-wyvern.gif)


To check it out for yourself, you can always just open up the client. The animation is off by default, but you can also turn it on (or off) by going to the Account Scene and checking the box labeled “Animate Foil Treatment”.


![](https://media.wizards.com/2015/mtgo/animate_foil_treatment.png)




---

An Original Performance
=======================


When we were doing pre-planning for the *Origins* build, our team identified a problem with the way that the frame for the double-faced planeswalkers would have to be built: the way that the client displays frames, we would need to construct an entirely new pair of frames to account for these five cards. It's no small task, and even if we did that, the client would need to load yet another frame type in order to show the cards properly. The more frame types being drawn simultaneously, the more system resources the client needs.


This wasn't technically a problem that needed to be solved, because we could have gone with the original plan, built those frames and released without a hitch. Instead, though, the team came up with a solution that meant that not only did we not build new frames, but we could reduce the number of card frames in the game: while this is complicated, the one-paragraph version is that our technical artist, Jesse, built a template and several modules that can be independently controlled. Now, when we have individual cards with slightly different frame needs (a color indicator, a power/toughness plaque on a land, etc.), those cards can use the same frame plus the required modular components. Ultimately, this meant that we solved not only for the planeswalkers in *Magic Origins* but also were able to give some significant performance increases and even some small visual upgrades to 63 cards, including existing double-faced cards, [Dryad Arbor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dryad+Arbor). Perhaps best of all, it means that we can use this template going forward when there are other things that call for new frames to be created. I think it's fair to say that we like creating new frames [every](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=368967) [so](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=247426) [often](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=380442).


There's one other thing you might have noticed: the Collection Scene loads a lot faster now. This went live before the release of *Magic Origins*, but it's worth touching on, because it was a result of a huge effort to refactor the code that underlies that scene. Because this was a refactor and not a redesign, I don't have a lot to say here, but everything about this scene is smoother and faster now: searching for cards, building decks, maintaining trade binders, and even just sorting large lists. I think everyone who plays *Magic Online* knows that this scene has historically been really slow, and this addresses a significant pain point that every player experienced at least occasionally.




---

Let Me Draw a Picture for You
=============================


On a similar front to the above, we've made some adjustments to the way that animations of cards work. When cards change zones, tap, or even slide up to the "red zone", that movement (however slight) is animated according to specific rules. It's a brief animation, but an animation nonetheless.


We've recently made some upgrades to the way that those animations work for two reasons. First, we found some significant performance gains to make in the code that defined the behavior of that movement, so it fit into our agenda of upgrading the client's overall performance. Second, up until now, the animations were deliberately limited to a handful of frames that gave many people the impression that the client was stuttering or that they didn't exist. (In fact, they can even be turned off and on from the Duel Scene options menu, found in the lower left corner by clicking on the gear icon.)


Implementing these performance upgrades also gave us the opportunity to increase flexibility in a pretty significant way. For each distinct animation (hand to stack, graveyard to battlefield, etc.), we made sure to include a lot of knobs that we can turn for each animation: frame rate, whether it's defined as a set duration or set velocity, the value of the duration/velocity, etc. With these knobs in place, the whole design team sat down and tweaked them until we got them into a spot that we liked. Then we had our internal beta testers play with it—we run a tournament every Wednesday afternoon that lets us test these things—and we tweaked them some more. Once everyone was satisfied, we locked the values in for this release, but one of the virtues of the knobs is that we can now change these things pretty easily.


So I want to make a request of all of you: please let us know how these animations—cards moving around the screen—feel when you're playing. If you like where we landed, great. If you think there's a way we can improve them, we'd love to hear that too. Our goal with this work was for them to be smooth without being slow, fast but visible and not jarring. Again, this loses some detail in the conversion to an image, but the below animation will give you a general idea of how card movement looks in *Magic Online*.


![](https://media.wizards.com/2015/mtgo/cardanimation.gif)


We definitely read feedback on Twitter, Reddit, and other social media, and we definitely want to get this right. You can talk directly to several of the design team on Twitter: *Magic Online* Design Manager Ryan Spain at [@RyanSpain](https://twitter.com/RyanSpain), yours truly at [@trulyaliem](https://twitter.com/trulyaliem), and Game Designer Rob Schuster at [@RobertJSchuster](https://twitter.com/RobertJSchuster).


Until next time, when I’ll have an article for you that’s legen… wait for it…


Alli Medwin  



[DOWNLOAD MAGIC ONLINE](http://magic.wizards.com/en/content/download)







