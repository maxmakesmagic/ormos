
---
[Link to Wayback Machine](https://web.archive.org/web/20151112173212/http://magic.wizards.com/en/articles/archive/feature/worthy-legend-2015-11-10)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "With the Legendary Cube right around the corner, Alli explains some of the obstacles the team overcame to perfect the experience."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "825521"
[_metadata_:publish_date]:- "2015-11-10"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Worthy of Legend"
[_metadata_:wayback_capture_timestamp]:- "2015-11-12 17:32:12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20151112173212id_/http://magic.wizards.com/en/articles/archive/feature/worthy-legend-2015-11-10"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/worthy-legend-2015-11-10"
---


Worthy of Legend
================



 Posted in **Feature**
 on November 10, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











[![](https://media.wizards.com/2015/images/daily/Download_MTGO-Button_WOL.png)](http://magic.wizards.com/node/823031)


...dary! *Legendary Cube*!


Whew! Been waiting a while to [pay that one off](http://magic.wizards.com/en/MTGO/articles/archive/magic-online/original-intent-2015-07-27#Legen). In the intervening time, we've announced the *Legendary Cube*, and next week you'll finally get to play it! There was a lot of work that went into creating this experience (and implementing the *Commander (2015 Edition)* cards online!), and as usual for each *Magic Online* release, I'll be your hostess, walking you through some of what went on behind the scenes.


I'm Alli Medwin, the editor for *Magic Online*, which means that I'm also on the Digital Design team here in *Magic* R&D and am part of the team responsible for designing the way in which sets function online. One of my regular responsibilities and privileges is to show off to all of you some of the changes, tweaks, upgrades, and enhancements we make to *Magic Online* for each release.


In a normal card set release, we have a handful of new mechanics for a whole bunch of new cards. In this release, we had relatively few new cards, but those we had were pretty complex. In addition to getting those in place, we solved a distribution problem, implemented the "tuck rule," updated some older cards, expanded the way counters can be associated with players, added experience counters, created unique UI for the Confluence cycle, and improved the UI for a few older cards that show up in the *Legendary Cube*.


A Symbolic Request
==================


Before we get into any of that, I want to show you all a little something that our graphic designers cooked up:


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Legendary.png)


This, my friends, is the symbol unique to *Legendary Cube* prize boosters. We don't often get a chance to create expansion symbols just for *Magic Online*, but I'm always excited when we do. This symbol is a stylized cube, perfect for prizes that you get from playing in a Cube format.


A Most Popular Shape
====================


Buying a preconstructed *Commander* deck is a great way to get into the format. It's also a great way to try out new experiences with new decks, and pick up the new cards along the way. We design the decks from each *Commander* release to play well with each other, so it's no surprise that a lot of people do just that: open up a preconstructed *Commander* deck, sleeve it up, and sit down with friends right away.


Trouble is, there are differences in behavior between *Magic Online* and paper *Magic* play, and we can't replicate the same experience online. It's also pretty easy to trade for most cards and build a deck from a list, so getting a new *Commander* product is often just about getting the handful of new cards. It's a simple transaction, sure, but that's not what *Magic* is about. *Magic* is about fun gameplay.


It's also important to make sure that the new cards are available, not only for Commander players but also for our Legacy and Vintage communities. Parity with paper *Magic* is important; Vintage without [Containment Priest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Containment+Priest) wouldn't be the same, nor would Legacy without [True-Name Nemesis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True-Name+Nemesis).


So how do we thread that needle? In paper, the play experience R&D designs is to have people play with different preconstructed decks together. Since we don't support that experience on *Magic Online*, we wanted to switch to an experience we do offer. And we knew that whatever fun gameplay experience we decided on had to reward players with the new cards.


On *Magic Online*, historically, many of the most beloved events are Cube events. That led us to create the *Legendary Cube*: a cube that not only features many of the new cards, but also awards prize packs so players can add those cards to their collections.


If you haven't read it yet, you should read [Adam Prosak's article](http://magic.wizards.com/en/articles/archive/feature/legendary-cube-2015-11-09) from yesterday. He discusses the design and development of the *Legendary Cube* and goes into what it's like to actually play this unique and fun *Magic* format.


Replacing Commander Replacements, or Having a Solution Tucked Away
==================================================================


In a game of Commander, you can return your commander to the command zone any time it would go to your hand, library, graveyard, or exile. Whether it's being tucked on the bottom of the library or returned to your hand (or anything else!), if someone else tries to get rid of your commander, you can choose on the spot to just put it away in the command zone, where it's ready to be cast again for just a little more mana.


In paper, it looks something like this: Someone at the table says "[Overload](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overload) my [Cyclonic Rift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift)" and holds out the card for a moment so everyone can see, then everyone else scoops up their nonland permanents. While they're picking up their permanents, they'll probably pick up their commander as well. Some people (possibly the Oloro player) will put the card aside and adjust the die they're using to mark how many times they've cast their commander from the command zone. The whole process takes a few seconds, maybe more if there are triggers to resolve.


And here's a way we can make the interface better to speed things up in *Magic Online* Commander play while updating the rules to match [the "tuck rule" change](http://mtgcommander.net/Forum/viewtopic.php?f=1&t=17560).


Let's take the same [Cyclonic Rift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift) scenario. On *Magic Online*, returning each permanent is generally fairly simple. When commanders are involved, though, each player whose commander would change zones needs to get prompted, so the player can choose whether it should go back to the hand or to the command zone. In a complicated game, it might need to ask each player! Even if that player had yielded priority for the turn (probably using either the F6 or the F8 keyboard shortcut), a decision needs to be made in turn order for the game to proceed.


We've upgraded this experience now. In addition to implementing the expansion of the commander zone-change replacement rule (the "Commander tuck rule"), we're saving our Commander players some time. Instead of being asked each and every time your commander would go somewhere weird, you'll get to "pre-choose," similar to setting stops. Just like setting stops, you can change them whenever you want. Clicking on your commander in any zone opens the menu, which both tells you what's going to happen and lets you change your choices. This makes for fewer opportunities to misclick by having fewer clicks to make.


So let's look at the menu:


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Menu-1.png)


If it's in your hand or command zone (or if it's somewhere else and you can cast it from there), you'll see the usual casting options. In other zones, you'll just see these controls.


The first line is a header that you can't interact with. Each of the other lines, though, has two functions: one, to describe the current behavior of a particular zone change, and two, to change that behavior with a click.


What's going on in the picture above is me saying that it's okay for Isamaru to be returned to my hand, but if he'd die, be put into my library, or get exiled, I'd rather he be put into the command zone.


If I click on the second bullet point (the graveyard line) and open up the menu again, then I see...


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Menu-2.png)


...this!


Now I'm saying that it's okay to have Isamaru be put into my hand, and he should be put into the command zone instead of into the library or exile, but if he'd die, I'm fine with that. (For the record, I'm never fine with killing puppies.)


Generally, you'll want to keep the defaults—as shown in the first screenshot—but there are always times you don't. Maybe your commander's just getting hit with an [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) trigger, and you can destroy the Ring next turn, so you're okay with the commander going to exile. Maybe you're playing a [Child of Alara](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Child+of+Alara) deck, so you need your commander to go to the graveyard to get your trigger. Whatever your reasons, you can change your mind whenever you want, even if that [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) trigger is on the stack.


Single Card Stories: Sensei Golden-Tail
=======================================


Are you ashamed to be a samurai? I wouldn't be. This is a story about vindication and prioritization, and it's pretty personal for me.


This story starts eleven years ago, when I was in college. I was a "serious casual" *Magic Online* player, and *Champions of Kamigawa* had just been released a few weeks prior. As a college student, I couldn't afford to take the time to draft nearly as much as I'd have liked, but I was usually able to set aside my textbooks and other responsibilities long enough to draft a few times a month, plus special occasions. My birthday was a few days after the Release Events ended, and my then-girlfriend even surprised me with an extra draft set! I was excited about the multiple drafts I was going to play, and pored over spoiler lists until I felt I was ready. I picked [Sensei Golden-Tail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei+Golden-Tail) early, dreaming of stacking bushido triggers to win every creature combat. I even picked up a [Nagao, Bound by Honor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nagao%2C+Bound+by+Honor) and two [Kabuto Moth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kabuto+Moth)s. My deck was sweet.


But when I used my [Sensei Golden-Tail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei+Golden-Tail)'s ability, I didn't get any blue text on the card. None! The trigger worked, and there was a training counter on the creature, but it was a real letdown looking at the now-trained creature. There wasn't much indication that anything had changed.


Yes, I was the geek who cared about blue text *long* before I had this job.


An aside: A lot of work on *Magic Online* is about prioritization. Where can we get the best customer experience with the resources that we have available for card sets? It's a tricky balance to strike, for sure, and it's not always pretty. If a card is in a new set or cube, or if a bug is format-warping, we're going to prioritize it highly. If it's a nonfunctional display issue, it drops down the list. And *Magic Online* is a complex game, so we apply our resources carefully.


Fixing [Sensei Golden-Tail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei+Golden-Tail) under normal circumstances wouldn't make sense. It's just not a relevant card to (most) anyone (other than me). But with it showing up in the *Legendary Cube*, it bumped up a lot higher in priority.


So I present to you the image that I wanted to see all those years ago:


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Kabuto.png)


This moth, my friends, is proud to be a Samurai.


Count on Me
===========


*Magic* has had several types of counters on permanents since the very beginning. [Sengir Vampire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sengir+Vampire) (among others) used the now-omnipresent +1/+1 counter, [Clockwork Beast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clockwork+Beast) had +1/+0 counters, and [Living Artifact](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Living+Artifact) had counters that would eventually be named vitality counters. Every expansion has had one or more types of counters. Some of them showed up again and again (charge counters), and others are unique (do you know what single card makes [manifestation counters](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arbiter+of+the+Ideal)?).


Counters that players get (or as some of us say, "counters on players") are almost as old: *Legends* introduced the poison counter. Until *Commander (2015 Edition)*, though, there was only one kind of counter that could go onto a player, and even then it wasn't a significant mechanic outside of *Scars of Mirrodin* block.


That's no longer the world we live in. With experience counters also possible now, we needed to revisit the way we display counters on players.


Previously, we displayed poison counters on players by putting a skull-and-crossbones icon in the same part of the battlefield where the mana pool resides. There are a few problems with that, the first being that icon appears nowhere else in all of *Magic* iconography. It's a clear symbol of death (or pirates!), and it's labeled as "Poison," but it doesn't fit the rest of the game. Second, it's sitting with the primary resource type that players use to cast spells and perform other game actions. While *Magic Online* players generally know how the game works and know that poison isn't actually that kind of resource, it's misleading to put two very different things together in near-identical displays.


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Display-1.png)


So we knew we needed to do better. And while technically speaking the counter isn't "on" the player, it's certainly strongly associated with the player. For poison counters especially, it's effectively an alternate life total. So we're showing it on the player avatar now. There's plenty of room to show off the experience counters now, too. And also, while we're constructing a new way to display these numbers, we might as well give poison counters a new and more appropriate symbol.


So all told, that looks like... (Drumroll, please!)


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Display-2.png)


A Confluence of Events
======================


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Charms.png)


In the beginning, there were Charms, and they were charming. The *Mirage* set had five cards that each had multiple effects on them. The built-in flexibility was appealing, and the concept was revisited several times over the years. When *Magic Online* was introduced, it was a simple matter to offer **three** different casting options, each correlating to a different mode. It was quite clear how to use them, and so all was well.


Eleven years later, that technology was revisited to create a commanding presence in the form of *Lorwyn*'s Command cycle. Instead of three modes asking the player to choose one, they had four modes, asking the player to choose two. Rather than three casting options, then, these cards had upward of **six**, each of them being long enough to not be immediately readable. The same right-click cast menu was used, and while it occasionally caused players to pause, it was not a significant disruption in gameplay. This was our consensus during *Dragons of Tarkir* implementation design: The functionality wasn't problematic.


And then came the Confluences. In design, they were called the "super charms," and while they're really cool, I dreaded the implementation of a card with **ten** different casting options. It's not 27, because the instructions are always performed in the order written on the card regardless of which order they're chosen in, the same way that [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command) always bounces a permanent before drawing a card. Even with "only" ten, though, that menu would likely be larger than most player's screens. This was clearly not a great option.


During design team meetings, we tossed around several alternate ideas. We discussed, we iterated, and we eventually came up with a plan. The plan was implemented, the implementation was reviewed, and we came to this:


![](https://media.wizards.com/2015/images/daily/FEAT20151110_MED_Confluence.png)


When you begin to cast a Confluence, a window appears showing you the available choices. You can use the number spinners—that's the up and down arrows to the left of the modes—to choose how many times you want to use each mode. By default, each mode is chosen once, but you can use the up arrow to increase that number. If you're maxed out on your choices, it'll just drop one of the other numbers by one.


If you can't use a mode (perhaps because there's no legal target), then it'll appear grayed out and you won't be able to use the associated number spinner. If there's only one mode you *could* choose, then it appears immediately with a 3 already chosen. And if you've looked around a bit and dropped some numbers such that you don't have all three choices made, the "Cast" button will deactivate, and the "*(number remaining)*" reminder at the top will indicate how far away you are.


Most of the time, you'll know what you want to do with a spell long before you see this window. Starting each spinner at 1 lets you get to your choice with a minimum of clicks, which should shave off some time while playing with this cycle of cards.


Let us know what you think of this kind of interface! While designing this, a question came up: Should Commands use this type of window? We eventually decided that the cost to players in changing familiar interfaces wasn't worth it, but it's an open question and we'd love to get your thoughts!


Legendary Epilogue
==================


The annual *Commander* release is a particular favorite for a lot of people. As a former *Magic* judge, I of course love Commander, but I want to give particular recognition to one of the only people who enjoys Commander more than I do, the man who probably enjoyed working on this card set release more than any other, my teammate and coworker Rob Schuster. He's the game designer behind the official *Magic Online* Tumblr, which can be [found here](http://wizardsmtgo.tumblr.com/) if you want to keep up with what we're up to more frequently.


We—the Digital Design team—are also on Twitter: Design Manager Ryan Spain is [@RyanSpain](http://www.twitter.com/RyanSpain), Rob is [@RobertJSchuster](http://www.twitter.com/RobertJSchuster), and I'm [@trulyaliem](http://www.twitter.com/trulyaliem). We keep up with [Reddit](http://www.reddit.com/r/mtgo) as well, and feedback is always welcome [at the Tumblr](http://wizardsmtgo.tumblr.com/). Or if you want to send long-form feedback to me and the design team, you can email [MTGOEditor@gmail.com](mailto:MTGOEditor@gmail.com). We can't respond to everything, of course, but we do read it all, and we do want to hear your thoughts and opinions on how we bring *Magic* to the digital realm.


Until next time, may your Moths always be proud Samurai.


Alli Medwin


Digital Editor, *Magic Online*


[@trulyaliem](https://twitter.com/trulyaliem)







