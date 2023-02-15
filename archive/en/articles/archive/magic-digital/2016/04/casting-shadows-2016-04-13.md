
---
[Link to Wayback Machine](https://web.archive.org/web/20160414193541/http://magic.wizards.com/en/articles/archive/magic-digital/casting-shadows-2016-04-13)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Alli is back with behind-the-scenes stories from the implementation of Shadows over Innistrad in Magic Online."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1016666"
[_metadata_:publish_date]:- "2016-04-13"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Casting Shadows"
[_metadata_:wayback_capture_timestamp]:- "2016-04-14 19:35:41"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160414193541id_/http://magic.wizards.com/en/articles/archive/magic-digital/casting-shadows-2016-04-13"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/magic-digital/casting-shadows-2016-04-13"
---


Casting Shadows
===============



 Posted in **Magic Digital**
 on April 13, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











Hey everyone! I'm Alli Medwin from the *Magic Online* design team. My team's job is, in part, to design the digital implementation of each new set as it comes out. One of my favorite parts of my job is that I get to write articles like this every set, sharing some of the behind-the-scenes stories and challenges we faced and introducing new features that you guys will get to use starting with this set's launch.


Read This First
===============


One of the constant constraints that *Magic Online* operates under is the need to mimic the rules and functionality of paper *Magic* as close to perfectly as possible. Accuracy is a virtue for us, and one of the functions of my job is to help ensure rules' accuracy.


One of the challenges we've dealt with—and many of you have dealt with too—is what I think of as the "[Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) problem." Allow me to illustrate by walking through the steps to cast [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling):



![](https://media.wizards.com/2016/images/daily/MD20160413_Fling-in-Hand.png)*Step 1: Right-click on [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) in your hand.*


![](https://media.wizards.com/2016/images/daily/MD20160413_Targeting.png)*Step 2: Choose a target for [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling)'s effect.*


![](https://media.wizards.com/2016/images/daily/MD20160413_Payment.png)*Step 3: Pay the mana cost to cast [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling).*


![](https://media.wizards.com/2016/images/daily/MD20160413_Sacrifice.png)*Step 4: Choose a creature to sacrifice as an additional cost.*

This is entirely rules-accurate, but if you've ever cast [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) in paper, I bet you've pointed to your own creature first. Some people pick up the creature they're sacrificing and use that to point to the creature they're targeting. Others will point to their creature, then the target.


This makes sense; you're not asking your opponent a question about your permanent. In *Shadows* *over Innistrad* Limited events, you're asking of your opponent: "Excuse me, would you mind if my Angels here were to purge your artifact, creature, or enchantment from the face of the game?"


Paper *Magic* takes a lot of shortcuts that digital *Magic* can't. Because of our mandate to match the rules of the game so precisely, we need to ask the player for a target before paying costs per rule 601.2. And there are good reasons to make this the order: effects can change costs based on the target(s) of a spell.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Accursed+Witch)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accursed+Witch)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Infectious+Curse)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Curse)Transform
Accursed Witch! She and her friends [Icefall Regent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Icefall+Regent), [Elderwood Scion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elderwood+Scion), and [the Torch from some dude named Kaervek](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=382982) are why we have things in this order. If the order were reversed, we couldn't have any abilities like those that change the mana costs of spells that target them.


So you understand the problem now. One of the most common issues players experience is the [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) problem, but there's just not a lot we can do.


What we're trying with the latest entry into the [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) family, [Angelic Purge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angelic+Purge), is some extra reminder text. This is text not present on [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) itself, and I suspect that's one of the reasons people get confused: "Choose target creature or player" just isn't descriptive enough.


![](https://media.wizards.com/2016/images/daily/MD20160413_Angelic-Purge-Targeting.png)


This text is pretty clear as to what you're doing when you're clicking. I'll be honest with you all, I don't know that this will solve the [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) problem completely, but I do know that reminder text is often helpful, so I'm all for expanding its use whenever prudent.


Almost Forgot...
================


Appropriately enough, as I write this article, I almost forgot the creation of some extra reminder text we put onto an ability that can use all the disambiguation it can get:


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forgotten+Creation)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forgotten+Creation)
![](https://media.wizards.com/2016/images/daily/MD20160413_Trigger-Prompt-Box.png)


We put "Use [CARDNAME]'s ability?" on a lot of things pretty regularly, but this seemed worth creating a special case for. It's possible that nobody would make the mistake of accidentally discarding their hand with that default text in place, but with these extra words, it's just that much less likely.


Misclick Protection
===================


Stop me if you've heard this one: "What the Jace? I thought I had my stop set, why did it not let me cast my spell?"


For those of you who don't know what I'm talking about, stops are how you indicate to the game that you'd like to get priority during a specific step or phase, letting you cast a spell or activate an ability. There's a stop setting for almost every step and phase, but most of them start the game set to "off."


![](https://media.wizards.com/2016/images/daily/MD20160413_Phase-Ladder.jpg)


The white triangles indicate where the game will ask you to do something, and you'll skip through the steps and phases with black triangles. The top row of stops is for your opponent's turns, and the bottom row of stops is for your own turns. Until the release of *Shadows over Innistrad*, clicking any of the triangles toggled them between the two states.


The problem is that it's really easy to accidentally click on one of them when you don't mean to, not notice it, and have it seriously cost you later in the game. It's not a common occurrence, of course, but when it happens, it's devastating. In order to prevent this from happening further, we've released a new feature that keeps the phase bar locked by default.


Here's how that works. We start with the phase ladder as it exists with the lock.


![](https://media.wizards.com/2016/images/daily/MD20160413_Locked-Phase-Ladder.png)


All the way on the right, you can see the padlock icon, indicating that left-clicking the phase ladder won't do anything. If you try, the lock will softly flash at you, enough to draw the eye but not so much as to be obtrusive. Now, left-clicking the padlock icon itself...


![](https://media.wizards.com/2016/images/daily/MD20160413_Unlocked-Phase-Ladder.png)


...opens the lock, letting you click your stops freely again. The lock will remember whether you had it open or closed, with the setting saved to your computer. It starts off locked, but if you don't like it, you can click the lock to open it and leave it opened. It'll stay open on that computer until you reinstall *Magic Online*.


Even when the phase ladder is locked, you'll be able to right-click a stop to set or remove it. That menu hasn't changed. You'll still see this:


![](https://media.wizards.com/2016/images/daily/MD20160413_Phase%20Ladder%20Context%20Menu.png)


You're never cut off from making the changes to your stops, but our goal with this feature was to make sure that every change to your stop settings is deliberate.


Unmaddening Madness
===================


*Shadows over Innistrad* introduced a few rules changes, but the most exciting one for *Magic Online* is the change to the way that the madness ability works. If you like Vampires, this change simplifies a workflow you're going to be using a lot over the next six months.


But I'm skipping ahead. Let me set the stage for you: This story begins in the second half of 2015, when we began early work on the *SOI* *MTGO* release. We on the *MTGO* R&D team had known madness was returning for quite a while, having played with the set as it worked its way through design and development, and we knew we wanted to do something with it. Something had to change.


Here's how the mechanic worked: When you discarded a card with madness, you could choose to discard it into your graveyard or exile. If you discarded it into exile, you then put a triggered ability onto the stack. When that triggered ability resolved, you could choose to cast the card for its madness cost or put the card into your graveyard.


Madness was long-famous internally for having an onerous workflow, but because it was a semi-reasonable UI that hewed to the Comprehensive Rules, we weren't interested in revisiting it. Besides, it hadn't been printed since *Future Sight* and saw very little high-level play. We're generally not in the habit of devoting resources to mechanics like that. It was only a step or two above sweep or cipher: we'd love to make it better if we had the time, and we expected to never have the time as long as we were devoting almost all our cardset resources to upcoming sets.


But with madness returning, we had an opportunity to address the problem. Two teams from *Magic Online*—the cardset developers who code the new cards and mechanics, and the design team—sat down and brainstormed. Nothing was off the table, and no idea was too crazy. We walked out of that meeting with a lot of ideas, and I was really happy with the prospects for meaningful change.


I took off my *Magic* *Online* hat and put on my rules and templating hat—a lot of us have multiple roles here, and I'm on that team too—and proposed our ideas to the rest of that team. Most were too zany to work (what if madness were a replacement ability that had you cast the spell instead of discarding it?), but that's expected. That's just how brainstorms are: you might draw three cards, but you're putting two back on top of your library. Not everything works.


It was the humble proposal of removing a meaningless choice that caught people's attention. The team discussed it for a while and eventually couldn't come to a good answer to a simple question: why do we even let players choose how to discard cards with madness? It's only a choice if the player's not planning to cast the card, and even then, the frequency of when it mattered was very low. Cutting that choice simplified the rules without simplifying the strategic choices involved in the mechanic, so it didn't take much to get the rest of R&D on board.


A design maxim: If you can't explain why a rule is good to have in your game, it's probably not a good rule.


This let us cut out two clicks from every interaction that a player has with a discarded card with madness, and it removed a step in which players had to make that same meaningless choice every time: "Discard" or "Discard with madness"?


There are *almost* no times when it matters. It's not zero, but it's very limited. The most prominent one involves activating [Jace, Vryn's Prodigy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+Vryn%27s+Prodigy) with four cards in your graveyard, then choosing to discard a card with madness. Since you're not discarding the card into your graveyard, when Jace looks to see whether he needs to walk the path to exile, he'll only see four cards and not five, so he won't transform.


We try to be good partners with the paper teams, working with them regularly to identify ways in which we can satisfy everyone's needs. Here, we were able to simplify the game's rules and the UI for a key set mechanic at the same time by removing a rule that came up very infrequently and just didn't affect the game very much. We have to match the paper rules, of course, but that doesn't mean the paper rules can't be incrementally improved, and I'm proud of the improvements we were able to make here.


Count on Delirium
=================


I was a premier-level judge for quite a few years before I joined Wizards of the Coast. One of my favorite clever things I saw players doing was a mainstay at Legacy events, and later Modern events too: players would bring a custom die to indicate the power and toughness of their [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)s. These "tarmo-dice" are a super useful play aid, because you want to know at a glance how many card types are represented in graveyards.


And then along came delirium, and it practically begged for the same thing. You're only counting the cards in your own graveyard, but it's just as impractical to count up constantly. Instead, it's better to have a clear indicator of just how close you are.


When you start the game with one or more cards that have a delirium ability in your deck, you are treated to this sight:


![](https://media.wizards.com/2016/images/daily/MD20160413_Delirium-Indicator-0.png)


As card types fill your graveyard, the number will automatically update. But it's not just the number that's important. You also need to know *which* card types are present. Right-click those words, and a tooltip appears, telling you in plain English which card types are present.


![](https://media.wizards.com/2016/images/daily/MD20160413_Delirium-Indicator-4.png)


This indicator only appears on your graveyard at the start of the game. Your opponent won't see it. Once one of your delirium cards becomes visible, though, it'll be visible to them for the rest of the game, too.


There are going to be a lot of times when you're given the choice of sacrificing a permanent or discarding a card, and you really want to enable delirium. This indicator and its tooltip should save you time hunting through graveyards.


A Long, Cold *Shadow*
=====================


There are a host of smaller changes and designs, many of them text-related, that we implemented alongside this set: take a look at the game log to tell you what happened after that Creeping Dread. Welcome to the Fold's prompt box text includes some clarifying text that's important to pay attention to. Or take a look at the text around Sin Prodder. And I'm sure you can figure out why there's no Cancel button when Sinister Concoction asks you to discard a card.


It's not just enough to ship out this set, though. It's great to get feedback. Designer Rob Schuster and I are on Twitter—he at [@RobertJSchuster](http://www.twitter.com/RobertJSchuster), and I'm [@trulyaliem](http://www.twitter.com/trulyaliem)—and we'd love to get feedback from you about how the set plays digitally. If you've got a longer question, feel free to ask it on the [*Magic Online* Tumblr](http://wizardsmtgo.tumblr.com/).


Until next time, when I'll have some answers to eternal questions!







