
---
[Link to Wayback Machine](https://web.archive.org/web/20221001112808/https://magic.wizards.com/en/articles/archive/latest-developments/mixed-bag-part-1-2012-05-04)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Hey, y'all. I hope everybody enjoyed your Avacyn Restored Prerelease and managed to escape with some cool goodies courtesy of the Helvault. It was the first time in a long time I didn't find myself spellslinging anywhere outside of Seattle, but I did make sure to draft plenty of Joint Assaults later on in the day to ensure maximum soulbond blowout potential."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644966"
[_metadata_:publish_date]:- "2012-05-04"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Mixed Bag, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2022-10-01 11:28:08"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20221001112808id_/https://magic.wizards.com/en/articles/archive/latest-developments/mixed-bag-part-1-2012-05-04"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/mixed-bag-part-1-2012-05-04"
---


Mixed Bag, Part 1
=================



 Posted in **Latest Developments**
 on May 4, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 







Hey, y'all.


I hope everybody enjoyed your *Avacyn Restored* Prerelease and managed to escape with some cool goodies courtesy of the [Helvault](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Helvault). It was the first time in a long time I didn't find myself spellslinging anywhere outside of Seattle, but I did make sure to draft plenty of [Joint Assault](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joint+Assault)s later on in the day to ensure maximum soulbond blowout potential. Almost everyone in R&D (myself foremost among them) gets way worse at **Magic** the longer we've been "inside," so I kind of have to take my victories where I can get them nowadays, e.g.:


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_joi.jpg)[Joint Assault](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joint+Assault) | Art by [Raymond Swanland](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Raymond+Swanland%22%5D)


Haven't seen this combat trick before and therefore have zero reason to play around it yet?



![Joint Assault](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Joint+Assault)

 

*Ziiiiiiiiiiing.*


It's the little things in life.


My last couple of columns have been very technical and "developer-y," what with all the conversations about game play environments, draft landscapes, and everything else. It's easy to forget, if you get too embroiled in all of that, that a huge part of what's awesome about **Magic** is simply that it contains a bunch of totally sweet cards. So I want to take a step back today and just talk about some of the stars of *Avacyn Restored:* the cards themselves. [Mark Rosewater](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater) has been doing his card-by-card from a design perspective for years now, so I decided I'd lend a development bent to things.


I don't have any sort of grand agenda, so I'll just parse the file in WUBRG order and think about what comes to me. Every set is full of stories, and the cards catalyze those stories like photographs of childhood memories. Bear in mind: I wasn't actually on the *Avacyn Restored* development team, even though I was involved in dozens of playtests and conversations. So I'm coming at this from an angle of anecdotes and observations. I wasn't in the room when many of these cards were created, so you'll be getting a developer's opinion on the process, not necessarily the product. Hopefully, this'll provide you a little bit of insight into the kinds of things we think about during development, and how we design cards to address those issues.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card01a.jpg)The first time I saw this card in one of our playtests—in our *uncommon* slot—my eyes bulged. Which was exactly the intended effect, I'm sure. One of the challenges of designing *Avacyn Restored* was that you had to convey it was an Angel set at all rarities and for all players, not just those reading the spoiler list on our website. That means you've got to put Angels at lower rarities so they integrate themselves into the game play environment more frequently than just the times you bust a Limited bomb. Moreover, you can't just print a couple 3/3s and skin them as Angels; you have to show what makes Angels cool, too, or you're missing the point.


This card accomplished that task brilliantly, and "demoting" it from rare was a great choice made by the *Avacyn Restored* team.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card02a.jpg)[Tom LaPille](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Tom%20Lapille) created [Zombie Apocalypse](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombie+Apocalypse) by merging two separate cards, and in doing so created one of the most iconic spells in *Dark Ascension*. It represented the ultimate triumph over Avacyn's waning legacy and the abject destruction of humanity on Innistrad.


So what better way to signal a change in the fundamental order of things than to turn that spell on its head?


We've done this a few times, and frequently it's controversial. [Blightsteel Colossus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightsteel+Colossus), for example, was and is a very polarizing card—but it does for sure convey the "turning" of one of Mirrodin's most iconic forces. A similar motivation drove the design of this card, too.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card03a.jpg)Oh, the miracle mechanic. More development time and energy was spent trying to get miracle right than any other mechanic I've seen in my three years at Wizards—and with good reason! It's a high-variance, high-risk, high-reward mechanic. Executed sloppily, it turns every game into a topdecking contest. Executed too conservatively, it fails to do what it's supposed to do, which is make the draw step more exciting. So we had to devote a lot of time to getting the balance right, while ensuring that the "feel" of the cards still delivered the expected emotional payoff.


I am lucky that [Dave Humpherys](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Humpherys) is one patient gentleman, because I spent a *lot* of time whining about the early executions of the miracle mechanic. If I had been in his shoes, I'm at least 50% sure that at some point I would literally have put my fingers in my ears and started screaming "Neener, neener, neener!" We experimented early on with a variety of miracle costs and effects, and I dug up problems with every one of them. Yes, I was definitely being "that guy." Cost a hugely powerful effect at something like ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), and a huge percentage of the time you would "miracle" it you simply aren't able to pay the cost. That's tremendously dissatisfying. "Okay," you might think, "why not make the cost cheaper?" We did exactly that on a number of effects, but if that's all you ever do, miracle stops being exciting around turn seven or eight or so. "Yes, I saved five mana on my [Hallowed Burial](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hallowed+Burial)! Okay, your turn."


An excellent solution on the part of the *Avacyn Restored* development team was to design miracles with variable mana costs. That allowed them to scale depending on the game state, rendering them relevant in the midgame while creating *epic* stories later on. I'm extremely happy with how cards like [Entreat the Angels](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Entreat+the+Angels) turned out.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card04.jpg)I have become somewhat notorious in the Pit for my irrational love of "ponderous activated abilities." You don't want to do too much of this as a developer, but I think you add a lot of depth to Limited by providing a "value option" on otherwise reasonably costed creatures like these two guys. Most of the time, you don't have four spare mana sitting around and so you don't have to devote a lot of time to thinking about the ability. Later on, though, you can generate some incremental advantage if you're a bit mana-flooded, but not so much that you're going to turn the game completely on its head.


Again, you have to be judicious about your proclivity for this, because you risk gumming up the board. You don't want **Magic** to become a game of "background processes," running queries to parse the battlefield for things you have to keep track of. But some amount of this is healthy.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card05.jpg)As I mentioned earlier, if you're going to make an "Angel Set," you have to make sure the Angels are felt at lower rarities. [Seraph of Dawn](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seraph+of+Dawn), in particular, is an extremely dominant common—one we probably wouldn't just drop into a random set. But sometimes it's important to push the limits a little bit to convey the essence of a particular feeling. As long as you're deliberate, every set can have one or two effects that bend the environment around them in order to establish a certain mood.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card06a.jpg)Starting in earnest with *Dark Ascension*, we've tried to spread "looting" out into red in addition to blue. We'll talk about some of those red effects later on, but a question that move brought up is, "Okay—what does *blue* do, then?"


We talked a lot about how to differentiate "blue looting" from "red looting." We agreed that one of the reasons the effect felt red at all was its impulsiveness, its single-mindedness. Red knows what it wants right now, and doesn't mind throwing out something else it doesn't care about.


In that respect, it felt a little strange for blue to be dumping cards in the graveyard. The more we thought about it, the more it felt like blue would be much more inclined to, you know, put the book back on the shelf (or whatever) and save it for later. So we wanted to experiment with putting cards on the bottom of your library rather than directly into your graveyard, where you have to part with them entirely. Well, at least until you've drawn your [Unburial Rites](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unburial+Rites).


That isn't to say we're eliminating traditional looting from blue. The lines are blurry. The one rule we're sticking to consistently is that red discards the card first, whereas blue goes ahead and draws it. Red knows what it doesn't want; blue knows what it's looking for.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card07a.jpg)Something we've become much more diligent about in the era of modern design is ensuring that every color combination has a strategy to pursue, an identity. Part of this is for Limited play, part of this is for casual Constructed, and part of it is simply to ensure that a set feels like more than just a pile of separate cards.


A few playtests in, the *Avacyn Restored* team realized that blue-black felt as though it was lacking an identity. Dave Humpherys brought in the "loner" mechanic to emphasize that while UB in this set might not be putting together a swarm of monsters to overrun you, the creatures it *did* bother to summon would be pretty powerful indeed. At the Prerelease, I managed to lose *twice* to a topdecked [Predator's Gambit](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Predator%27s+Gambit), so I can testify to the power of this mechanic, even on seemingly innocuous cards, to turn the game around.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card08a.jpg)Called "Elusive Strixogriff" in early Development, this card is notable for being the first mythic rare designed by [Pro Tour Los Angeles finalist Billy Moreno](/en/articles/archive/event-coverage/feature-top-8-player-profiles-2005-10-29).


How do you design a top-down half-owl half-griffin that later changed its concept entirely?


Like this, apparently.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card09a.jpg)As far as I can tell, this card came straight brain-to-print from the design file. The only difference?


Its playtest name was "Business Class."


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card10a.jpg)Speaking of "Miracles that took an unbelievable amount of time to develop..."


Probably ten percent of total *Avacyn Restored* development man-hours were spent on ensuring this card cost what it was supposed to cost. The *Avacyn Restored* team knew it wanted miracles to hit hard, and one way to do that was to offer a look into their potential power level in an obvious, visceral way. The first step was to ensure this card exiled itself, because—well, thank you, [Noxious Revival](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noxious+Revival) and [Snapcaster Mage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage). The second was getting the opportunity cost calculation correct. We wanted, if at all possible, for this card to have a miracle cost equal to [Time Walk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk). That meant we had to make sure that when you drew it on the game's first two turns, you were about as "behind" relative to the value of your average card that you were "ahead" when you hit it and were able to pay the miracle cost.


We hope we hit the spot!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card11a.jpg)I have nothing terribly constructive to say about this guy except that he's my favorite piece of art in the set.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card12a.jpg)This guy is doing a lot of work, actually—and with the current art, I might actually remember to call it "Creeper" rather than "Keeper"!


One thing we realized as early as *Innistrad* was that the Zombie deck was lacking in powerful two-drop creatures. However, given the obvious power level of [Diregraf Ghoul](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diregraf+Ghoul) and the upcoming [Gravecrawler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravecrawler), [Geralf's Messenger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger), and [Diregraf Captain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diregraf+Captain) (coupled with [Phantasmal Image](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Image)), we knew we couldn't just give the Zombie deck all of the gasoline everywhere it wanted it. Instead, we wanted deck builders to have meaningful choices for some of the remaining slots.


Both [Crypt Creeper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crypt+Creeper) and [Butcher Ghoul](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Butcher+Ghoul) are solid role players for the Zombie deck. [Crypt Creeper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crypt+Creeper) can generate some value in concert with opposing undying creatures and [Snapcaster Mage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), and [Butcher Ghoul](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Butcher+Ghoul) can be combined with any of Standard's abundant sacrifice effects ([Birthing Pod](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birthing+Pod) into [Geralf's Messenger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger), anyone? Chaining that into [Phyrexian Metamorph](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Metamorph)??) to add a layer of consistency and iterative advantage to the deck. Are either of these cards format-defining powerhouses? Of course not. But they are capable of performing a role.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card13a.jpg)o\_0


This guy is no joke. I am sure plenty of time will be spent talking about him elsewhere, so I'll save the bigger points for that time, but I *will* answer the one big question I keep receiving:


Yes, I promise you we tested it at seven mana. :)


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card14a.jpg)Called "Homicide" in playtesting, this card was designed by Erik Lauer as a solution to [Champion of the Parish](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Champion+of+the+Parish) and everyone's favorite Human Insect, [Delver of Secrets](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Delver+of+Secrets)/[Insectile Aberration](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Insectile+Aberration). We also wanted some splash hate for [Huntmaster of the Fells](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Huntmaster+of+the+Fells), which had the nice value option of hitting [Avacyn's Pilgrim](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=243212) early. It's comparable to [Tragic Slip](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tragic+Slip) to be sure, but requires less set-up than Slip off the topdeck.


Also, totally sweet art, [Davey P](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5b%22David+Palumbo%22%5d).


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld193_card15a.jpg)For whatever reason, a lot of these black cards are producing far more quips than pieces of design insight.


Nine months or so prior to the release of every set, the **Magic** team gets together for a slideshow where we put the near-finalized version of every single card under scrutiny. Part of this is to catch late-stage errors or mistakes, and part of it is simply for everyone to get a chance to appreciate the product they've worked hard creating for the last ≈18 months.


I mention all of this because the flavor text for [Killing Wave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Killing+Wave) elicited a bigger reaction than any other card I can remember seeing. It's just *awesome*, and is *so* Liliana.


I want a t-shirt that declares, simply, "I hate angels."


 

...whoa.


I'm a little more than halfway through the set and already over my word limit. Guess there's a lot to say about the stuff we make!


I'm going to go ahead and call it a day, but stay tuned for Part 2 of this series, where I cover the red, green, artifact, and gold cards the week after next. What are some of your favorite cards from the set? Anything in particular I haven't covered that you'd like to know the story behind? Let me know, and I'll see if I can tackle it when we come back around!


Thanks for reading, y'all.


Zac








