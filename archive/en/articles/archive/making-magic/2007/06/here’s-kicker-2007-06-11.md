
---
[Link to Wayback Machine](https://web.archive.org/web/20170601043921/http://magic.wizards.com/en/articles/archive/making-magic/here%E2%80%99s-kicker-2007-06-11)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Welcome to Kicker Week! This week we'll be examining the popular Invasion mechanic that dropped by for a spell or two (or ten) during Time Spiral block. I'm going to talk about how kicker was created, explain the rules design and development use when creating kicker cards, share some stories about kicker design, and explain my major gripe with kicker. Yes, today is everything you wanted to know about kicker... but were afraid to ask."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "617196"
[_metadata_:publish_date]:- "2007-06-11"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Here’s the Kicker"
[_metadata_:wayback_capture_timestamp]:- "2017-06-01 04:39:21"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170601043921id_/http://magic.wizards.com/en/articles/archive/making-magic/here%E2%80%99s-kicker-2007-06-11"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/here%E2%80%99s-kicker-2007-06-11"
---


Here’s the Kicker
=================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on June 11, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to Kicker Week! This week we'll be examining the popular *Invasion* mechanic that dropped by for a spell or two (or ten) during *Time Spiral* block. I'm going to talk about how kicker was created, explain the rules design and development use when creating kicker cards, share some stories about kicker design, and explain my major gripe with kicker. Yes, today is everything you wanted to know about kicker... but were afraid to ask. 

### Kick Start

The seeds of kicker's origin stretch back a long time. In fact, longer than the game has been for sale. Yes, kicker's earliest origins can be traced back to pre-**Magic** (well, at least pre-**Magic** release). When Richard first created **Magic**, he was living in Philadelphia. It was here—through a bridge club, for those that love this kind of minutiae—that Richard met what is now known as the Alpha playtesters. These were a bunch of fellow gamers that helped Richard playtest **Magic** before its release. (A great number, interestingly enough, went on to work at Wizards of the Coast—Bill Rose, Charlie Catino, Skaff Elias, Jim Lin, Joel Mick, Dave Petty, Lily Garfield—then Lily Wu—and, of course, Richard). 

Once it became clear that **Magic** was going to be published, the Alpha playtesters, in separate groups, set out to design their own **Magic** sets. There were three in all, named *Ice Age*, *Menagerie* and *Spectral Chaos*. For any trivia buffs out there, before I tell you, can you identify what each of those sets became? 

[![Snow-Covered_Plains](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/IA/Snow-Covered_Plains.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Snow-Covered%2BPlains)*Ice Age*, surprise, surprise, was released under the name *Ice Age* (this was before we started using wacky playtest names to ensure that playtest names didn't just turn into the actual set names). *Ice Age* was designed by a subset of the Alpha Playtesters referred to as the East Coast Playtesters (which is odd since all of them were from the east). The *Ice Age*, and *Alliances*, designers were Skaff Elias, Jim Lin, Dave Petty and Chris Page. The same design team also designed *Antiquities* (with Joel Mick) and *Fallen Empires*. Skaff Elias would go on to serve as **Magic** Brand Manager and creator of the Pro Tour. Jim Lin would later serve as VP of R&D.

*Menagerie* was published as *Mirage* (although technically, what was *Menagerie* got broken into *Mirage* and *Visions*). The *Menagerie* design team was Bill Rose, Joel Mick, Charlie Catino, Don Felice, Howard Kahlenberg, and Elliott Segal. *Mirage* and *Visions* were the only sets designed by this team, but Bill, Joel and Charlie would go on to be on many other design teams and both Bill and Joel would eventually serve Head Designer. Joel would go on to became **Magic** Brand Manager and Bill became, and still is, the VP of R&D.

*Spectral Chaos* was a one-man design team, Barry "Bit" Reich. Barry was a good friend of Richard's and has the honor of playing the first-ever **Magic** game with Richard. *Spectral Chaos* was a set dedicated to multicolor play, and it was the skeleton used by the *Invasion* design team (which incidentally was Bill Rose, Mike Elliott and myself—I'll be getting back to this team in a moment). While there was a lot of deviation, certain elements, such as the domain mechanic (called the "Barry" mechanic in design after Barry), made it all the way through design and development. 

So which of these three sets had the seeds of kicker's design? Trivia buffs, place your bets. Kicker was in *Invasion*, and *Spectral Chaos* was used in its design. Is it *Spectral Chaos*? No. Before I let you guess again, let me fill you in with another important factoid. Bill Rose, the lead designer of *Invasion*, is the designer of kicker. Thus the answer must be *Menagerie*, the set Bill lead the design of. Wrong again. When I asked Bill to dig down deep and figure out where kicker came from, he acknowledged that early *Ice Age* design messed around with extra effects for extra cost. 

I'm not saying that any version of *Ice Age* design exactly had the kicker mechanic. The design just played around with a few spells that could make themselves something more than what they normally were. Remember that early *Ice Age* design was before **Magic** was released (in the summer of 1993). And all of the playtesters shared info with one another to help get feedback. Anyway, the earliest seeds of kicker first showed up in *Ice Age* design. A year or two before the public even knew of **Magic**'s existence. So how did it get from there to its eventual home in *Invasion*? That, my faithful reader, is a story for another section.

### Just For Kicks

![Bill Rose](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_BillRose.jpg)Before we continue, I need to talk a little more about Bill Rose. Bill started at Wizards of the Coast in October of 1995—interestingly, the exact month I began (although three weeks earlier). In fact, Bill has an employee phone list from the month after he started. As each person on the list has left the company, Bill has crossed them off. Eleven names remain on the list, making Bill the twelfth oldest employee and myself the thirteenth (this, by the way, only counts time at Wizards and not people who spent a long time at TSR before it was bought by Wizards). Bill started as a **Magic** developer. He worked his way up to Head Designer / Developer, and finally to VP of R&D.

As I said earlier, Bill got involved in **Magic** by being one of the first playtesters. Bill is a die-hard gamer. He loves board games, he loves computer games, but most of all Bill loves card games. Bill is a shark at trick-taking games, and this is in a group of high-caliber game players. Whether playing after work or squeezing in a game during lunch, Bill is clearly a gamer through and through.

Psychographically speaking, when it comes to **Magic**, Bill is a Timmy / Spike. Bill is definitely in the game for the thrill of the experience. Bill loves playing the big creature or the humongous spell. But Bill also likes to win, so he's always trying to figure out what he can get away with without giving up any advantage. For example, Bill is always on the lookout for a deck that allows him to play a dragon *and* win. What does this have to do with Kicker? A lot.

You see, kicker started because Bill was trying to figure out a way to get big creatures into his deck. The problem was that his big creature deck was getting beaten by people playing hordes of small creatures. Thus to keep up, Bill had to play with the smaller, faster creatures. If only, Bill thought, there was a way to play with small creatures that could turn into big creatures. This thought led him back to the discussions during *Ice Age* design. And thus, the first kicker cards were born—all creatures; little guys that you could turn into bigger guys in the mid to late game. Now all Bill needed was a set to put them in.

### Kicking Things Around

One of the roles of the Head Designer is to put together design teams. Such was the task Bill had in the fall of 1999. **Magic** was going through a few rocky years. *Urza's Saga* block was crazily overpowered and *Mercadian Masques* was forced in the opposite direction to help balance the power level. The next set needed to be strong without being overpowered. Understanding this, Bill pulled out all the stops. The team would be the three strongest designers working on **Magic** at the time (Richard worked at Wizards at the time, by not actively on **Magic**)—himself, Mike Elliott and myself. And we would be working on a theme that we all knew in our hearts was going to be popular with the players—multicolor.

[![Probe](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/IN/Probe.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Probe)So in the middle of winter at my dad's house in Lake Tahoe (back in the day, R&D had numerous offsite / skiing visits to my dad's house), the three of us sat down to flesh out what exactly *Invasion* was going to do. On the very first day, Bill pitched the kicker mechanic. Bill was obviously very eager to use it, and Mike and I took to it immediately. I remember that I really liked how its mana requirements would allow us to make monocolored cards that functioned partially as multicolor cards. 

A lot of times I talk about all the deliberation that goes into picking mechanics. I talk about how at times we can spend months going back and forth over what should and should not be included. Kicker was almost the exact opposite. Bill showed it to us and it was basically in the set the moment he finished talking about it (unlike split cards, but go read my column [Split Decisions](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr7) for that story).

The interesting thing about that week was how much flexibility we found with the mechanic. What had started as a means to make small creatures into big creatures quickly expanded to fill all different card types. It was during this time that we also started crystallizing another aspect for the kicker mechanic. Because kicker mana could be in or out of color, we decided that we should differentiate how they were used. Here's how we did it. If a spell kicked with mana in color, then the kicked effect was merely a larger version of the effect. If it was a creature, it got bigger. If it was a spell, the effect got bigger. There are a few exceptions in *Invasion* block (and many more in *Time Spiral* block as we explored "alternate reality" and "future" ways to mess with it) but all still followed the flavor that the creature/spell got bigger. 

If you paid an off-color kicker then the spell got an extra effect. The spell didn't get bigger in scope but rather bigger in the fact that it did more things. The extra effect almost always tied in with the original effect, often creating synergy. The funny thing about this design was how subtle it was. Whenever I would point it out I would always get responses from players about how the differentiation between on and off color completely passed over their heads. 

### A Kick In The Seat Of The Pants

As there isn't a lot to say about the design of kicker as a mechanic, I thought I'd walk through a few interesting things that happened as we tried to use kicker on various spells. 

**[Rout](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rout)/[Breaking Wave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaking+Wave)/[Twilight's Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twilight%27s+Call)/[Ghitu Fire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Fire)/[Saproling Symbiosis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saproling+Symbiosis)**

![Rout, Breaking Wave, Twilight's Call, Ghitu Fire, and Saproling Symbiosis](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/making/mr283_cardfan.jpg)So have you ever wondered why this rare cycle didn't have kicker? After all, each requires you to pay ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif) to get a bonus to the card (aka turned it into an instant). They sure feel like they have kicker. And you know what, they did. Well, up until templating, that is. Then we ran into a little snag. Kicker costs aren't played until you play the spell. This means that the spell has to already be played before the kicker can alter it. See the problem here? 

If these spells had kicker then you would have to play the spell before you could use the kicker. And as the kicker was the thing letting you play the card as an instant, the timing really didn't work out; there was no way to play them an instant speed. (To all the rules gurus out there, yes, I know there's no such thing as "instant speed"; just work with me here. Everyone else knows what I mean.) These cards were created because we were trying to find other cool things we could do with kicker and in the end, to have their functionality they had to lose kicker. Ah, sweet, sweet irony.

**[Verdeloth the Ancient](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Verdeloth+the+Ancient)**




![Verdeloth the Ancient](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Verdeloth+the+Ancient)This card is the exact opposite of the cards above. Verdeloth was designed without kicker. The original version had you pay ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) when Verdeloth came into play. During some development meeting, someone said, "Hey, isn't this just kicker?" and the rest of the team said, "Yeah, you're right," and changed it.

**[Skizzik](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skizzik)**

![Skizzik](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Skizzik)This card caused a bunch of problems because it did something really weird. You see, [Skizzik](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skizzik) is the only kicker card where paying the kicker loses you something. We tried wordings were the card gained something that kept it alive. My favorite was the idea of having it deal damage to itself instead of causing a sacrifice and then making the kicker grant protection from red. In the end, we went with the wording that's on the card because it seemed to be the simplest and most understandable way to say it.

**[Emblazoned Golem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emblazoned+Golem)**

![Emblazoned Golem](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Emblazoned+Golem)It's interesting how many mechanics come about because we do something quirky on a single card and later we realize we can build an entire mechanic around it. Why do I mention this? Because [Emblazoned Golem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emblazoned+Golem) was the precursor to the sunburst mechanic from *Fifth Dawn*.

**Battlemages vs. Volvers**



|  |  |
| --- | --- |
| Nightscape Battlemage | Necravolver |

During *Planeshift* design, both Mike Elliott and I went down the path of making creatures that had two kicker costs, one for each allied color. Mike's cards each had a comes-into-play effect if you paid the kicker. My version added either one or two +1/+1 counters and keyword abilities (my playtest name for them was "lego creatures" because of their "build a creature" feel). The idea was that if you spent all the mana you could create a monstrosity. Mike and I both liked our cycles, and there was a huge debate over which one should go into *Planshift*. The other would be retrofitted to enemy colors and saved for *Apocalypse*. Which one should stay and which one should go? In the end, the Battlemages won out because they had more synergy with the gating mechanic (creatures that when they came into play required you to return a creature that shared a color to your hand) in the set. 

**[Kavu Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Titan)**

![Kavu Titan](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kavu+Titan)This story isn't really about design but it's become such a classic story (and it involves kicker) that I felt obliged to tell it once again. (And yes, I know I told it during my *Invasion* Week article, [Body Snatchers of the Invasion](/en/articles/archive/making-magic/body-snatchers-invasion-2005-08-08).) During *Invasion* development I played frequently in the FFL (the Future Future League, where we play many months ahead to try and figure out what the future environment will be like). Because I wasn't the best of deck builders (at least a Spike deck builder; I could hold my own in a Johnny world), I usually got decks from other developers. Randy Buehler was running the FFL at the time, and he gave me a red-green deck to play. In it were four [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). I didn't think anything of it at the time. I then went on to go 4-0 that week. I was the only person with an undefeated record.

During my last match, Randy watched. At some point late in one of the games, I played my [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). After the match was over, Randy informed me that the [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) weren't actually [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). They were proxies for [Kavu Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Titan). Armed with this information, the next week I went 2-2. Suffice to say that the R&D guys thought this was the funniest thing ever. The lesson I learned was the importance of using the [Kavu Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Titan)s as 2/2s. When I was aggressive with [Kavu Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Titan), my deck performed much better. When I waited to maximize the [Kavu Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Titan)s as 5/5 creatures, I lost much of the aggression of my deck and thus some of its power. Week 3, I went 4-0 again.

### Kicked When You're Down

[![Growth_Spurt](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/UG/Growth_Spurt.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Growth%2BSpurt)Finally, as promised, it's time for me to talk about the thing I don't like about the kicker mechanic as a designer. Ready? It's too big of a mechanic. It covers too much space. It does too much. In short, it's too all-encompassing. What started as a "pay more, get more" mechanic has turned into a "pay extra mana to do anything and everything" mechanic. Almost any mechanic that requires paying extra mana (or extra anything) can get shoehorned into the kicker box.

Why is this a problem? Because **Magic** is all about exploring new space. Whenever we go down the path of a mechanic with an extra cost (and trust me this is a huge vein of design space—R&D jokes that 90% of cards are kicker or split cards) I know I have to listen to a new round of choruses of "that's just kicker." And on some technical level, sure. We often could word things as if they were kicker. But that doesn't accomplish the task set before us. The goal of design is not to make everything look exactly like what has come before. If a mechanic explores new mental space, we want to give it its own keyword. Having half the mechanics be kicker would both make it harder to differentiate between the mechanics and would definitely give each mechanic less of its own feel.

The mistake of kicker was that we made a mechanic that was too flexible. It represented too large a slice of design space. Our fix has basically to restrict what counts as kicker. Kicker is the "pay more to get something bigger" mechanic. This means one of two things. Either it enlarges the effect or it creates a second effect that is synergistic with the first. Anything else gets its own keyword. So next time you see a new mechanic and you're first inclination is, "Hey couldn't that be done with kicker?", the answer most likely is yes, we could, but we don't want to. 

### Kick Off

And that brings us to the end of my ode to kicker. I hope this has given you a few new insights that perhaps you didn't have before. 

Join me next week when I talk about why we added all those new keywords for old effects in *Future Sight* (and beyond).

Until then, may you find a way to give your own life a little kick.

Mark Rosewater







