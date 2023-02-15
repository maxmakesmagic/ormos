
---
[Link to Wayback Machine](https://web.archive.org/web/20170607055033/http://magic.wizards.com/en/articles/archive/latest-developments/what-developers-do-2011-12-09)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Today I want to cover something that has been given surprisingly little attention over the ten-or-so-year lifespan of Latest Developments: What is it that Magic developers actually do?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644601"
[_metadata_:publish_date]:- "2011-12-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "What Developers Do"
[_metadata_:wayback_capture_timestamp]:- "2017-06-07 05:50:33"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170607055033id_/http://magic.wizards.com/en/articles/archive/latest-developments/what-developers-do-2011-12-09"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/what-developers-do-2011-12-09"
---


What Developers Do
==================



 Posted in **Latest Developments**
 on December 9, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






Today I want to cover something that has been given surprisingly little attention over the ten-or-so-year lifespan of Latest Developments: What is it that **Magic** developers actually *do?*

Before I got to R&D, I didn't really understand how developers spent their time on, you know, a given Tuesday. I didn't understand which responsibilities fell to design and which fell to development, and to what extent the composition a given set was shaped by the different personalities involved. Now that I've been around a while, and have actually led development of a set, I have a better idea of how that process works. And it's a little different from how I had imagined it to be.

We developers have all sorts of responsibilities, from assigning art waves to physically putting playtest stickers onto **Magic** cards, but I'd say there are five principal activities that occupy most of our time.

Well, six if you count karaoke covers of "Black Horse and a Cherry Tree" at no fewer than twenty late-night Seattle venues.

Or maybe that's just me.

Did I just say that in public?

### Ahem

Headings are powerful.

### Activity Number One: Making Magic Cards

I'd say the most important skill of a **Magic** developer is knowing how to design cool **Magic** cards.

*WHAT!??!!!##111* **DESIGN** *a **Magic** card??? Aren't there* **DESIGNERS** *who do that??*

In my mind, I had always pictured the Design team creating card-files, filling up each slot in a set with the coolest possible spells and mechanics, and the Development team playtesting constantly to ensure that those cards were costed properly, that nothing was imbalanced, that the colors were well-represented and evenly distributed, etc.

That's not really how it works.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld172_control.jpg)  
What happens is that midway through a set's creation, Design hands over a card-file to Development. That's not the only thing they hand over, though. Usually Development receives a detailed vision document containing Design's vision for the set's most important themes, mechanics, individual cards, and essential emotional responses it ought to evoke. Frequently there will be twenty or so "Design Favorites" that the set ought to be developed around—that is, should be preserved if at all possible, and not removed for the set for game-play reasons. Occasionally there will be slots whose game-play purpose is clear, but whose implementation in the form of actual cards hasn't been figured out yet.

It's Development's job to take this handoff and make a set out of it. It's not very different from someone coming to you with a blueprint and a set of materials—some concrete, some bricks, some mortar, the occasional fluted Corinthian column—and asking you to erect a building. The important thing to understand is that Design is actively not supposed to turn over, in the handoff, a set that approximates the final product as closely as possible. Instead, their job is to ensure the correct tools exist for that product to be built.

What this means is that the overwhelming majority of cards in a given handoff get killed for one reason or another. Part of this is because changes to cards—particularly to commons—have a "ripple effect" across the entire set. If I realize that a certain ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 3/2 needs to cost ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) because it has some sick ability, I can't just keep the three other ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) creatures in the file as-is. But when one of those cards changes, it's probably bumping into something like it as well. By the time we've finished this little song-and-dance, we've altered seven cards—and if (say) the green common vanilla was statted at 4/3 to deliberately avoid the common red burn spell, which dealt 2 damage, but which now deals 3 damage because it needed to cost another two mana and not be a totally awful card—well, you can see how this can spiral out of hand very quickly.

The point is that you can't expect for everything about your set to work out correctly if you just twist enough knobs. A lot of the time you have to spawn new cards from your brain onto the page. This can happen with commons, as I just described, or it can happen with rares for a number of different reasons. Maybe a reprint is too powerful in the current environment, even if it was reasonable last time. Maybe a card doesn't properly function within the rules. Maybe the latest riff on a riddle-telling Sphinx is too similar to the last set's riff on a riddle-telling Sphinx. Or maybe you, as a developer, have simply thought of something awesome that really should be in the set. In all of these cases, you've got to be proficient at designing printable **Magic** cards. The trick is figuring out how to do this while ensuring that Design's vision remains intact—indeed, not only remains intact, but becomes fully realized through effective game development.

### Activity Number Two: Playtest Limited

The bulk of the playtesting that goes on inside the current iteration of **Magic** R&D involves Sealed Deck and Booster Draft. That's not to say we don't playtest a lot of competitive Constructed, too—we'll get to that in a minute—but Limited playtesting allows us to kill a comparatively large number of birds with a comparatively small number of stones. For one thing, real-life Booster Drafts (especially on **Magic Online**) are iterated millions of times and need to remain robust across the life-cycle of the format. This means we need to play them enough to ensure that a given environment's strategies and mechanics don't grow stale after just a few sessions. Sealed Deck, meanwhile, functions as the mechanism through which a huge number of players are introduced to a format by virtue of the Prerelease. Because of that, we've got to make sure that players have a good initial impression of the set right out of the gates. We don't like to be in the position to have to say, "Trust us, this is fun!" because the initial Sealed experience is mind-boggling, unbalanced, or awkward. We'd rather show than tell.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld172_battle1.jpg)  
It's not just about the formal Limited environments, though. If you're reading this article, it means you're enfranchised enough in **Magic** to devote time out of your day to consume content relating to the design of (what I hope to be!) your favorite game. That means, in all likelihood, that you're a **Magic** Player with a capital M and P. Chances are you know what Booster Draft and Sealed Deck are, and you can appreciate the nuances of how Limited formats evolve and how certain cards affect the replayability of a given environment and everything else.

You probably have played a lot of **Magic**, and are probably part of what someone could accurately describe as a "**Magic** Community." A lot of players, though, don't experience **Magic** that way. They have a "red deck" or a "blue-black deck" and pick up a few booster packs of a set here and there and by-and-large play **Magic** with the cards they happen to open. They don't necessarily conceptualize themselves as playing "Limited" or "Constructed" or any format at all. They simply experience the cards put in front of them, and judge the quality of a set by how they experience those cards.

Sealed Deck and Booster Draft playtesting allows us to approximate the experience this kind of player will have. It allows us to analyze what the set looks like when you open up five packs and take a look at what's sitting there in front of you. It allows us to create a kind of microcosmos, a world inside which only a very small number of cards exist, and nevertheless analyze whether than environment is fun. And that's very, very important, because if we fail at this level, our players never have a reason to build themselves into the type of person who (for example) knows what Standard is or knows what the concept of a "sideboard" entails.

Succeeding on this level is a *moral imperative* to me as a game designer. I believe we create something that can be beautiful, and because I believe in what we create I want people to experience it fully. But I don't get to enjoy the luxury of sitting atop my high horse all haughtily saying, "Well, if the player doesn't like what they see at first, they just don't *understand* the intricacy of this beautiful thing I've created," or whatever. I don't get to blame the player when it's me who has failed. I believe I've got to guide the player to that point, and that means developing **Magic** at every level it can be played.

### Activity Number Three: Playtest Constructed

I guess the last section kind of killed the suspense leading into this one. Frown.

Most of our players play Standard. I've talked at length about how our Standard playtesting process works [here](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165), but to reiterate: while we actively don't want to create an environment that's so straightforward as to be solved by eight or so people working inside an office building, we do want to have a good idea of what the general game-play experience is going to be like. Part of this is to maintain balance—to ensure that overly powerful cards never see the light of day—and part of it is to ensure that the types of strategies that tend to lead to net overall fun are viable.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld172_battle2.jpg)  
*Aside on the concept of "net overall fun" that is going to cause people to roll their eyes at me and say "whatever" and make scoffy faces:*

We talk a lot on this website about "things that are fun." Inevitably, when I make some kind of statement along the lines of, "[Stasis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis) decks are miserable and make me wonder why I am playing **Magic** instead of watching football, playing Frisbee, catching up with friends, or subjecting myself to sadistic medieval torture," there's always someone who says, "But wait! I just *loooooooove* to play [Stasis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis)."

I definitely don't have the authority to tell people what should and should not be fun to *them*. To proclaim that I know that much about the quality of another person's subjective experience would be exceptionally arrogant, presumptuous, and also just kind of insubstantial. But we *do* possess a lot of relatively objective, quantitative information about what constitutes *net* fun—that is, what constitutes a more fun game-play experience for both parties at the table. And the amount of misery you're experiencing when I'm blowing up all of your lands or countering all your spells is, overall, usually greater than the amount of enjoyment I'm deriving from doing it. We've accrued data about this type of thing for almost twenty years—we ask people what makes them quit, we ask them what makes them play, we go to tournaments and stores and events and conventions and we take these surveys and we have these conversations and we witness these behaviors firsthand. We look at statistics of tournament attendance in the real world and on **Magic Online**, and compare that attendance to the kinds of decks that dominate both casual and competitive environments. Certain trends emerge time and time again.

There are at least two players in every game.

*End entirely-too-long aside.*

Anyway, we playtest Constructed to ensure that when something *is* unfun, we place tools inside the environment that give players a means to respond to it. We care about all our formats because we know our players care about all our formats. When something breaks, we're working hard to try and figure out what the best thing is to do about it.

### Activity Number Four: Talking. A Lot.

As a decisionmaking entity, R&D is pretty data-driven. We have numerous people with advanced degrees in "hard sciences," and as gamers we all sort of twitch and squirm awkwardly when we can't make decisions based on relevant information. I myself am frequently the developer who is urging people to iterate games instead of spouting opinions (although I'm certainly not going to say I don't do my fair share of, er, opinion-spouting) and we all strive to inculcate a culture of good faith whereby we can trust the reasoned judgment of our colleagues.

But sometimes, you just have to stare at a file for an hour. Sometimes, you're stuck. Sometimes, you don't exactly know what you're supposed to do. In those situations, you call—gasp!— a meeting.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld172_meeting.jpg)  
Aah, meetings. Ye olde standard of corporate culture everywhere. Your average large set development team spends four to six hours a week in meetings, and your average small set team will spend three to five. Sometimes you just need to talk through stuff. And when you're as demanding as we are—when you know that each card you create will be played and scrutinized by millions of people—you owe it to the set to generate heated debate over every single card in the file.

In our meetings, we discuss playtest results. We dissect which cards enable which archetypes in Limited. We design specific cards to fit specific needs. Say, for example, we've realized that nobody has drafted black-green in any of the last three **Magic** 20X6 playtests. Is the problem with the individual black and green cards? Do the cards lack inherent synergy? Do the power cards in each color combination compete with each other on the mana curve, so that drafting them together creates diminishing returns? Is there a specific strategy—maybe speed-infect, or graveyard-matters—that the color combination naturally plays into that we could enable more directly with a choice uncommon or two?

When you're dealing with complex systems, sometimes there isn't a better way to attack a problem than to get four or five smart people in a room and talk through it for a couple of hours. We do a lot of that.

### Activity Number Five: Metagame Design

Oftentimes when we talk about "metagames" in **Magic**, we're referring to the specific composition and frequency of viable decks in a given format. But the term has a much larger meaning—the "game outside the game," broadly-speaking.

R&D serves as the general game-design component of Wizards of the Coast, a large Hasbro subsidiary with 400+ employees in the Renton office alone. Most of our time we spend designing actual games—the products you see on the shelves—but we also contribute a fair amount of time to different processes all across the company.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld172_allied.jpg)  
The game mechanics of **Magic** don't spontaneously become incorporated into reality like Athena springing forth from Zeus's forehead. Huge numbers of people do amazing behind-the-scenes work that ensures the game of **Magic** can actually exist and be played. Physical cards have to be produced, manufactured, printed, and distributed. Art must be contracted, assigned, and fitted to the card. Packaging must be designed. Text must be typeset. Inserts must be folded. Tournaments must be run. My own obnoxious and meandering sentence structure must be rendered coherent by a patient, disciplined editor.

Every single one of these processes is an element of "metagame design," because each one of them contributes to how players experience the game of **Magic**. If **Magic** was the most well designed game in the universe, but you could never play it because the cards never made their way into stores, the game would suffer for it. If instead of Prereleases, Friday Night **Magic**, store locators, and professional events, you had to scour the Internet for some UseNet subcommunity of **Magic** players to play with, the game would suffer for it. If instead of genre-defining, standard-setting, paradigm-establishing worldbuilding and illustration, **Magic**'s art boxes were populated by the likes of "my friend's cousin who can draw, like, *really well,* dude," **Magic** would suffer for it.

Wizards as a company realizes this, and that's why **Magic** developers tend to become involved in all aspects of the process in some form or another. We help design Prerelease experiences—like the *Mirrodin Besieged* faction packs—that take the game beyond your normal Saturday Sealed Deck. We contribute to a set's creative identity by submitting names, concepts, and pieces of flavor text. We ensure that marketing campaigns align with a set's overall mechanics and themes. And—as many of us ourselves came from the ranks of **Magic**'s premier event structure—we're constantly and continually striving to ensure that **Magic**'s organized tournament system best meets the needs of all its players.

There's far more to the game of **Magic** than the words printed on its cards. We game-develop those parts, too.

### Developing Development

Part of quality development is recognizing the need, at the end of the day, to best optimize your processes to best meet your needs. As such, the frequency of these (and other) activities waxes and wanes with each successive set. Furthermore, each Lead Developer has a methodology most well-tailored to him or her. In general, though, these five activities comprise the bulk of our time. Through them, we sculpt the handoffs we receive from design into the sets you guys are playing right now.

We hope you likey.

Zac

  






