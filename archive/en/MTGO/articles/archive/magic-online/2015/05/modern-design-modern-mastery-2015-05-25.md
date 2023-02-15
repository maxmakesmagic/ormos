
---
[Link to Wayback Machine](https://web.archive.org/web/20150528214559/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/modern-design-modern-mastery-2015-05-25)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "This is the very model of a Modern Masters article"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "383076"
[_metadata_:publish_date]:- "2015-05-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Modern Design, Modern Mastery"
[_metadata_:wayback_capture_timestamp]:- "2015-05-28 21:45:59"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150528214559id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/modern-design-modern-mastery-2015-05-25"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/magic-online/modern-design-modern-mastery-2015-05-25"
---


Modern Design, Modern Mastery
=============================



 Posted in **Magic Online**
 on May 25, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











*This is the very model of a* Modern Masters *article*


*With [Elementals](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397680), [Groodion](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397818), [Hierarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397709), and [Dragonsoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397859),*


*I know the [clique Vendilion](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397824), and quote the game historical From [affinity](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397893) to [metalcraft](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397719), in order categorical.*


*I'm very well acquainted, too, with keywords like [proliferate](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397860),*


*I understand the oddball cards like [Guile](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397696) and [Karn Liberate](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397828).*


*‘Bout [Incandescent Soulstoke](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397752) I'm just teeming with a lot of news,*


*With many cheerful facts about the interface that you will use.*


Hey gang! Alli Medwin again. I’m the editor for *Magic Online*, which puts me on the design team and in the thick of the design work that goes into implementing every set. Every set, as we’re wrapping things up, I take some time to walk through some of the design issues that came up over the course of designing and implementing it. So without further ado, let’s talk about *Modern Masters 2015 Edition*!




---

Grafting Improvements to Graft
==============================


The graft mechanic was the Simic mechanic from the original Ravnica block’s *Dissension* set, and it’s awesome and complex at the same time. Creatures with graft enter the battlefield with some number of +1/+1 counters on them, and that’s all they get; they’re 0/0 otherwise. Whenever another creature enters the battlefield—under any player’s control—each creature with graft offers it one of its +1/+1 counters. In paper, this is pretty straightforward: either you move a counter or you don’t, and there’s not much fiddling around with triggers. In the context of *Modern Masters 2015 Edition*, where there are proliferate cards running around the Limited environment too, it’s a lot of fun to move and grow your counter collection across a large number of creatures.


In *Magic Online*, the fact that the graft ability triggers so often is equal parts an opportunity to be tricky and an opportunity to be very complex. There’s unfortunately no way around that. One of the strengths of *Magic Online* is that it’s completely faithful to the rules of the game, so we translate that complexity as well. Despite that, there’s room to streamline the interface, and for *Modern Masters 2015* we’ve made a simple but powerful change to the way that graft works. None of the complexity is gone, but the mechanic is much more convenient now.


Let me back up a step here and walk through this.


When you’re presented with an optional ability in *Magic Online*, you often see a prompt that looks like this:


![](https://media.wizards.com/2015/mtgo/5-25-2015_img1.png)


You don’t have to use the ability. You don’t even always want to. If you have no cards in your library, for example, you *probably* don’t want to use [Abomination of Gudul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Abomination+of+Gudul)’s ability. You can answer the question by clicking the appropriate button in the prompt box.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img2.png)


But sometimes, like here, you always want to. If you put the [Soul’s Attendant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%E2%80%99s+Attendant) in your deck, after all, it probably wasn’t because you wanted a 1/1 for one mana. You probably want the ability every time.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img3.png)


In situations when I always want to answer that question the same way, I can right click on the ability while it’s on the stack and select the “always yes” option. That way, when the trigger begins to resolve, I don’t even need to think about it and it’ll just happen. If you select “always yield” as well, you won’t even need to worry about your triggers except to put them onto the stack.


You’re not locked in to these choices if you do that. You can remove this automated choice with the F3 keyboard shortcut. Alternatively, you can right-click on the battlefield and choose the “turn off auto-yields” option, which also turns off auto-yes and auto-no choices. So if your opponent resolves a [False Cure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=False+Cure), say, you can F3 and just say no for the [Attendant](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=193499) triggers that turn.


None of that is new, but it’s worth reviewing.


And now we come back to the *Modern Masters 2015* change to graft. If you know that you’re always going to make the same decision, it’s worth considering the option to automate that. Normally, you don’t want to hand one of your opponent’s creatures a +1/+1 counter, but you might put them on your own. The problem in the current interface is that while both positions make sense, it’s both yes and no and you can only choose one. The new option lets you choose both:


![](https://media.wizards.com/2015/mtgo/5-25-2015_img4.png)


Now you can automatically say no—selectively—to graft triggers that would move a counter to one of your opponent’s creatures. Combined with auto-yielding to the trigger, this can save you a lot of time on your round clock!


It really is almost tempting here to just make this the default. Almost. After all, if that’s usually the correct answer, it’s probably not an interesting choice. The problem is that removing the option entirely to move counters onto your opponent’s creatures would be a functional change to the way the mechanic works, which we don’t do. But *presenting* the option to save time and clicks allows us to streamline common use while allowing the more rare cases to keep full functionality.




---

Eldrazi Spawn
=============


Five years ago, *Rise of the Eldrazi* introduced a new kind of token creature, produced by fourteen different cards, called “Eldrazi Spawn.” Each token was creatively linked to the brood lineage of one of the three great Eldrazi titans.


Previously on *Magic Online*, when you used any of those fourteen cards, you ended up with one of the three Spawn tokens at random. The goal was to make sure that playing with Spawn-generating cards was fun, and a little bit of randomness in the way that you see these tokens is certainly fun.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img5.png)


From left: Eldrazi Spawn of the Ulamog, Emrakul, and Kozilek lineages.


However, we’ve shifted our attitude towards our creative treatments. As with so many other things in *Magic*, it’s the little things that count. Starting with *Modern Masters 2015 Edition*, cards that make Eldrazi Spawn will make *specific* Spawn. Creative Designer Kelly Digges wrote an Arcana five years ago that detailed which cards make which Spawn tokens (which [has been recently updated](http://magic.wizards.com/en/articles/archive/arcana/know-your-spawn-2015-05-14)) and that’s what you’ll see going forward. Specifically, for this set, you’ll see [Dread Drone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Drone) and [Kozilek’s Predator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kozilek%E2%80%99s+Predator) each making two Kozilek-lineage Spawn, and Nest Invader making one Emrakul-lineage Spawn.


But where’s Ulamog?


[Where, indeed](http://magic.wizards.com/en/articles/archive/uncharted-realms/nissa-worldwaker-2014-06-25).




---

Proliferate
===========


When it comes time to revisit mechanics that are already implemented, the first step is to open up the client and poke at it. How does the mechanic work in normal use cases? How does the mechanic work in edge cases? How would we want to implement it if it were a brand-new mechanic?


When we went through this process for proliferate, it turns out that it was already implemented mostly very well. We’ve gone through some shifts in design philosophy and process in the years since the *Scars of Mirrodin* release, but for the most part, we were happy with the implementation. The verdict was the same as morph got last year: pretty good, but with room for improvement.


To proliferate online, the client puts you into a selection step, where all players and permanents with counters get a highlight and can be clicked. Once you’re done, you click a button and end up with all the extra counters that you asked for. At the core, that’s not changed. We tweaked three things for *Modern Masters 2015 Edition*:


One, counters are now only added when the process is complete and you click the Done button in the prompt box. Previously, counters were added as you clicked a permanent or player, and the selection step ended as soon as you had nothing else you could click. Importantly, this change allows you to click a second time to toggle the selection in case you decide you didn’t want to add the counter after all. It also protects you from accidentally skipping this step with the F2 (“pass priority”) keyboard shortcut. Everyone’s clicked on something accidentally before, and where we can make that easier to avoid, we try.


And not for nothing, it’s also more accurate to the rules of *Magic*, which is a big plus.


Two, the prompt box was updated to match the convention we use today: *Magic* instructions, followed by italic reminder text to describe the interface. Here’s that new prompt box *(this text speaks for itself)*:


![](https://media.wizards.com/2015/mtgo/5-25-2015_img6.png)


Three, and saving the best for last, let me first paint a picture for you: You attack with a [Thrummingbird](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thrummingbird). It’s a common in this set, so it’s probably going to happen once or twice.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img7.png)


There are a number of indicators that it’s attacking, including that characteristic red glow indicating that the creature is attacking. It’s not the only sign, though. The creature also slides forward to partially be in the “red zone,” and an arrow appears on mouseover, indicating what player or planeswalker is being attacked. The client needs to be very clear what’s attacking, because that’s a portion of the game that can least afford ambiguity.


Making a complex selection process like proliferate needs to be just as clear. For the same reason, seeking the same clarity, we’ve used that same red glow to indicate that an object is currently part of the selection.


The problem comes in when we need to do both at once. Like, say, once that [Thrummingbird](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thrummingbird) connects with a player and its trigger starts to resolve.


This isn’t just about proliferate, but it highlights the problem well by highlighting the selection poorly. If I’ve got a handful of attacking creatures with +1/+1 counters on them, for example, and connect with a [Thrummingbird](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thrummingbird), then it’s easy to lose track of what’s part of the current selection. Adding a red glow to a red glow is just not helpful. This wasn’t a problem in the previous iteration of proliferate because it didn’t use this selection workflow. But once we changed the flow, we realized that we needed to also change the glow.


So here’s what that looks like now:


![](https://media.wizards.com/2015/mtgo/5-25-2015_img8.png)


Selection has shifted from a red glow to a green glow. More than that, the intensity of the glow is pretty different, so our red-green colorblind fans will also be able to tell them apart. And that’s the important thing: allowing both states of highlighting to exist. The red carries the message that a creature is attacking through the combat phase, and the green is used only during the specific decision-making process. This applies to all selection steps, from proliferate to delve to resolving an opponent’s [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) and discarding a few cards.


It’s a pretty big change, so what do you all think of this one?




---

Adding Multiple Mana of Any Color
=================================


Here’s a riddle for you: How many abilities in a menu is too many?


I think this is too many:


![](https://media.wizards.com/2015/mtgo/5-25-2015_img9.png)


There’s not a lot to say here about the design of this interface, except that searching large lists is frustrating and it’s hard for me to come up with a lot of scenarios in which it’s worth asking players to go through that process. (It doesn’t help that those aren’t in the right color pair order, but maybe that’s just me.)


Elementals is a sweet deck in Limited, and [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider)’s a key part of enabling it. It would be really, really unfortunate to have people avoid that archetype because they don’t want to negotiate activating [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider).


To get around presenting a huge cluttered menu, we’ve updated the way that [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider) (and friends [Shaman of Forgotten Ways](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shaman+of+Forgotten+Ways) and [Altar of the Lost](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Altar+of+the+Lost)) works. One click and a trip to the prompt box to click some mana symbols, and you can add mana however you like.


And the right-click menu is down to a single item: the same ability as on the card.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img10.png)




---

Incandescent Soulstoke
======================


So “teeming with a lot of news” might be overstating things, but there are two small updates to the interface for [Incandescent Soulstoke](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incandescent+Soulstoke) to bring it in line with modern *Magic Online* design sensibilities: One, the prompt box text now specifies what you’re supposed to do when the ability resolves. You probably already wanted to put an Elemental creature card onto the battlefield, but this makes it explicit.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img11.png)


Assume you say yes and click a [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider) in your hand to put onto the battlefield. Previously, there was no indication which card was put onto the battlefield this way. Now, however, if you look in your Effects area, indicated by the shield icon, you (and your opponent!) might then see this waiting around reminding you which card is going to be sacrificed when that delayed trigger resolves. The blue text “haste” is helpful, but there are a lot of ways to put that word in blue text on a creature.


![](https://media.wizards.com/2015/mtgo/5-25-2015_img12.png)


This delayed trigger is unambiguous and clear about what’s going to happen to this [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider). Poor [Smokebraider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokebraider).




---

Patter Promises
===============


Sometimes you just need to make the rhyme work. Sorry. I don’t have much on [Karn](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397828), [Vendilion Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique), and the others. Happily enough, some things already work pretty well and didn’t need to be revisited.


So I’ll just leave you with a screenshot of a [Groodion](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397818). [Groodions](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397818) are awesome. And look at those shiny targeting comments! It’s super clear what that lil’ guy is doing!


![](https://media.wizards.com/2015/mtgo/5-25-2015_img13.png)


Until next set, may your choices always be clear and your [Groodions](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397818) always be drooling.


Alli Medwin  

Digital Editor, *Magic Online*  
[@trulyaliem](https://twitter.com/trulyaliem)







