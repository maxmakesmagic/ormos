
---
[Link to Wayback Machine](https://web.archive.org/web/20170502220221/http://magic.wizards.com/en/articles/archive/making-magic/maze-ing-grace-part-1-2013-04-08)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "656746"
[_metadata_:publish_date]:- "2013-04-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "A Maze-ing Grace, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2017-05-02 22:02:21"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170502220221id_/http://magic.wizards.com/en/articles/archive/making-magic/maze-ing-grace-part-1-2013-04-08"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/maze-ing-grace-part-1-2013-04-08"
---


A Maze-ing Grace, Part 1
========================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on April 8, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







Welcome to the first week of *Dragon's Maze* previews. Today we get to start talking about the third and final set of the *Return to Ravnica* block. There was a lot to pack in a tiny space, so today I'm going to walk you through some of the major challenges that faced the *Dragon's Maze* design team and then walk you through many of our solutions. Sound good? Then let's get started.


### The *Maze* Runner (and Her Team)


Before I jump into the design itself, I always like to start by first introducing the design team.


**Alexis Janson (lead)**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_1_jui89765tg.jpg)


 


In the beginning, **Magic** was designed by outside freelancers, mostly because there wasn't an R&D yet. Starting with *Weatherlight* and *Tempest* (the former was released first but the latter was designed first), design moved in-house. From those sets forward, the design of every set has been led by someone in R&D. Most of the time, that person worked full-time on **Magic** but occasionally R&D members from other teams were asked to lead sets. For example, [Brian Tinsman](http://www.wizards.com/magic/magazine/archive.aspx?author=brian%20tinsman), who led many sets, was in charge of new business design. I bring this all up because Alexis did something that no one has done since *Weatherlight*: she led the design of a **Magic** set without being in R&D.


 


For those who don't know Alexis's history, she first joined Wizards of the Coast as a design intern after winning the first [Great Designer Search](/en/articles/archive/great-designer-search-2006-10-31). That internship led to her getting a job doing prototyping for digital projects. That then led to her getting hired as a developer on **Magic Online**. She began doing the coding for new cards and this eventually led to her being the lead developer of **Magic Online**'s [new client](/en/articles/archive/2011-10-17).


All the while, Alexis worked on numerous **Magic** design teams. She was on *Eventide*, *Shards of Alara*, *Alara Reborn*, *Scars of Mirrodin*, and *Return to Ravnica*, which led to her finally getting the opportunity to lead her own set, *Dragon's Maze*. As you will see, it proved to be the most challenging design of the block, but [Alexis was up to the challenge](http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/242b).


**Dan Emmons**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_2_l8wnq10al6_1.jpg)


 


Dan is the newest member of the **Magic** design team—and by that I mean the collected group of people who work on **Magic** design (Dan, [Ethan Fleischer](http://www.wizards.com/magic/magazine/archive.aspx?author=ethan%20fleischer), [Mark Gottlieb](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Gottlieb), [Ken Nagle](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Nagle), [Shawn Main](http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main), and myself). At the time of *Dragon's Maze* design, this wasn't yet true. You see, Dan was heavily involved in [Great Designer Search 2](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/133). He wasn't one of the final contestants (although he did make the cut to 101) but rather one of the handful of designers who worked diligently making cards for all the contestants.


 


Dan got a job in game support (what was formerly known as customer service) and he came to me his first week saying his long-term goal was to work on **Magic** design. I had heard good things about him from Ethan and Shawn, who had worked with him during GDS2, so I told him we'd stick him on what we call the "hole-filling team"—an internal group we go to when there are cards to make to fill holes created by development.


Dan did a great job on the hole-filling team and this led to us putting him on the *Dragon's Maze* design team. The fact that Dan has since graduated to a full-time **Magic** designer might hint that he did a good job on *Dragon's Maze*.


**Aaron Forsythe**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_3_l28cto6rua.jpg)


 


There are lots of good things about being the director of **Magic** R&D. One of the downsides, though, is there isn't a lot of time to be on design and development teams. [Aaron](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Aaron%20Forsythe) does make sure to carve out a little time each year, and *Dragon's Maze* was the set he chose to work on.


 


There's not much new to say about Aaron. The fact that I've done his bio so many times speaks volumes about his contributions to design (and that's not even getting to his work on development or managing the whole process). As always, Aaron did excellent work.


**Erik Lauer**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_4_3xo3h5ntu3.jpg)


 


We always have a core developer on the design team. [Erik](http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer) filled this role for *Dragon's Maze*. Erik is a valuable addition as he always comes at a design (or a development) with a unique perspective. He asks questions no one else does and he finds solutions no one else thought of. As *Dragon's Maze* was a set with a lot of puzzles to solve, Erik was a great addition.


 


**Shawn Main**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_5_txo3h5npu3.jpg)


 


[Shawn](http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main) first came to R&D as the runner-up in the Great Designer Search 2. While he didn't get the design internship, his interview impressed enough people that he ended up landing a different R&D internship on the digital team (the people responsible for **Magic Online** and **Duels of the Planeswalkers**). *Dragon's Maze* was his first expert expansion design team. (Shawn was credited as being on the design team for *Gatecrash*, having designed battalion and extort, but he was not actually on the team.) I believe that, at the time of *Dragon's Maze*'s design, he was still an intern. Much like Dan, the fact that Shawn is now a full-time designer speaks well of his *Dragon's Maze* contributions.


 


**Mark Rosewater**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_6_5xbdgc1196.jpg)


 


And then there's [me](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater). These days, I'm on all the expert expansions. My major goal on this team was to be a helping hand for Alexis on her first design lead. If we were metaphorically throwing Alexis in the pool, I was the lifeguard.


 


### Building the *Maze*


To understand the task at hand on Day One of *Dragon's Maze* design, let me back up and explain how we got to the set in the first place. For the longer version of the story I'm about to tell, go back and read my [first preview week article](/en/node/656216) for *Return to Ravnica*.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_7_8xj3jnz79y.jpg)


Maze's End | Art by [Cliff Childs](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Cliff%20Childs%22%5D)


Brian Tinsman pitched the idea of doing a 6/4/10 guild split in *Return to Ravnica* block. Remember, at the time, it was scheduled to be a large/small/small block. We tried a few playtests and it was clear that six guilds was just too many to cram into a modern-day large set (the original *Ravnica* was back when we had slightly larger fall sets). I suggested we could turn the second set into a large set and do a 5/5/10 model. Everyone thought that sounded exciting, so we signed off on it.


Here's the part of the story I didn't tell. I was a little skeptical we could even fit five guilds into a modern-day large set, so I was tasked by Aaron to spend a few weeks kicking the tires of the block plan and making sure the basic design could work. I went back to Aaron and told him while it would be tight, I did think it could work. (We would later, by the way, make *Return to Ravnica* and *Gatecrash* just a wee bit bigger to give them a little more breathing room.)


My bigger issue was with the third set. Let me walk you through my larger concerns:


**#1: The Guild Problem**


The whole point to the 5/5/10 plan was to give every guild one last chance to get some more cards. That means all ten guilds have to be in the set. The set, being a small set, only has 156 cards. And remember that eleven of those cards are lands—ten Guildgates and one mythic rare land. (The "shocklands" are considered pick-ups as they are exactly the *Return to Ravnica*/*Gatecrash* versions, complete with art and expansion symbols.) That means there are 145 cards for ten guilds. That's only 14.5 cards per guild. Not a lot to work with.


**#2: The Number of Mechanics Problem**


Normally, in a large fall set we have four or five mechanics. In the winter small set, we traditionally keep most of them and add in one or two more. In the spring small set, we usually add one or two but we also tend to remove one or two (or relegate them to one or two cards at a high rarity that will come up infrequently). That means the most we ever put in a small set is seven, and that's on the high end.


*Return to Ravnica* block is about the guilds. Every guild has a keyword. The expectation is that all the keywords would show up in the third set. That's ten keywords—numerous keywords above our limit.


**#3: The Newness Issue**


The set has to cram ten guilds with their ten guild keywords into the set. We had issues getting five in a large set. Now we're trying to fit ten in a small set. As if that wasn't challenge enough, we had an additional issue. Players expect new sets to have new things in them, especially mechanics. How were we going to fit it in when we already felt ten mechanics was too many?


**#4: The Identity Problem**


Not only must a new set have new things, it also has to have its own identity. What sets this expansion apart from all other expansions? And how does the set gets its own identity when it's so busy using all the elements from the other two sets in the block?


**#5: The Drafting Issue**


*Return to Ravnica* drafts alone. *Gatecrash* drafts alone. Come *Dragon's Maze*, both return and are now drafted together. *Dragon's Maze* had to be the glue to hold the draft together. (We did work hard to seed some of the cards we needed in *Return to Ravnica* and *Gatecrash*.) So not only did we have to do everything listed above, we also had to make the set have the tools to make the draft work.


**#6: New World Order**


To top it all off, we needed to do it all while still trying staying true to [New World Order](/en/node/654416) (but luckily not [New New World Order](/en/articles/archive/making-magic/new-new-world-order-2013-04-01)—for those who might not have figured it out yet, it was an April Fool's joke).


Was all of the above possible? I really didn't know. I'm optimistic by nature so, as always, I assumed it was, but I stressed to Aaron that *Dragon's Maze* was going to be the trickiest set of the block. Aaron agreed, so we started design extra early. It's also a reason that this was the one set Aaron chose to be on.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_8_gfyx314izu.jpg)


Art by [Mathias Kollros](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Mathias%20Kollros%22%5D)


How did we tackle each of these problems? Let me explain:


**#1: The Guild Problem**


The first thing we did was to ask ourselves, "What are the expectations of the audience?" *Dragon's Maze* was going to give each guild new toys to play with. Our job was to make sure those toys were the toys the players either expected and wanted or didn't expect but would be happy to see.


Things expected:



* **Guild Champions**

Original *Ravnica* block had two legendary creatures for each guild, a guild leader and a guild champion. We knew going into *Return to Ravnica* block that we again wanted two legendary creatures per guild. Since the original *Ravnica* block release, the Commander format has taken off, giving extra significance to legendary creatures. Multicolor ones in particular are sought after, so we didn't want to do less than two. Spacewise, we didn't have room for thirty, so three was out. Why not have an uneven number among the guilds? The guild structure requires a certain amount of equity so all players, no matter what guilds they favor, feel the overall structure is fair.


To save something for *Dragon's Maze*, *Return to Ravnica*—and by default *Gatecrash*—chose to just use the guild leaders. This saved the guild champions for *Dragon's Maze*. While *Dragon's Maze* was happy to have the guild champions, they presented some unique problems. At first, we considered putting them all at mythic rare, where legendary creatures tend to go, but we quickly had a problem.


Ral Zarek, the Izzet Planeswalker who calls Ravnica home, was scheduled to be in *Dragon's Maze*. Every set has at least one Planeswalker and he seemed like a better fit in the third set than the first (*Gatecrash* didn't have the Izzet guild, so it felt odd to put him there). As all Planeswalkers must be mythic rare and there are ten guild champions, having only ten mythic rare slots was a problem. (Maze's End is an eleventh mythic rare but it is on the land sheet.) In the end, we decided to make all the guild champions rare.



* **Mana-Fixing Cycle**

Multicolor blocks need artifacts and lands to help players adjust to the higher color demands. While this is addressed occasionally on single cards, multicolor blocks always have a few cycles to help the mana. *Return to Ravnica*/*Gatecrash* had three such cycles: the common Guildgates, the uncommon Keyrunes, and the rare shocklands.


*Dragon's Maze* was expected to add to this mix with at least one more cycle. We tried a lot of different things but ended up with an uncommon cycle. I'll leave all the decisions that led to the mix of mana fixing for Latest Developments, as that was more development's decision than design's.


The other decision was to use the land slot for the Gates. This allowed us to bring them back both because, symbolically, they matter a lot to the story, and because it was another way to help with mana fixing. We'll get to why this was so important next week. Having the shocklands at rare and Maze's End as a mythic rare land allowed us to make the land slot exciting in a way it's never been before.



* **Guild Completion**

The last expectation was a little vaguer but nonetheless an issue the design and development teams had to address. The 5/5/10 model sets up the expectation that *Dragon's Maze* will help fill in the needs of the guilds. That meant we had to spend time figuring out what each guild was missing. Development would later do the same thing, looking at actual deck builds to figure out what components would be in demand.


The key to solving each of the above was making sure our answers matched expectations.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_9_6yk2dfsfwc.jpg)


[Simic Guildgate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Simic+Guildgate) | Art by [Svetlin Velinov](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Svetlin%20Velinov%22%5D)


**#2: The Number of Mechanics Problem**


This was a tricky problem to solve. For starters, we really didn't have a choice about the ten guild mechanics—they had to be in the set. We questioned whether we had to have all ten but quickly decided that each guild has players dedicated to it. How could we defend giving some guilds more of their keywords but not others?


The next idea we floated was to only use the keywords at uncommon and higher. This would lower how many different keywords would show up in a Limited game. Unfortunately, as we put together the set we realized that part of making each guild shine was maximizing the small space we had for each one. Using the guild keywords was a way to really hit the guild yet make rather simple cards.


In the end, the key was to boil down as many of the keyword cards at low rarities as we could to be as elegant as possible. In a bigger sense, the solution to this problem was to bite the bullet and just hope the players' experiences with *Return to Ravnica* and *Gatecrash* would make the ten mechanics a little less overwhelming. This is definitely one of the solutions where we had to cross our fingers and have a little hope.


**#3: The Newness Issue**


This was such an interesting problem to solve I'm saving it as the major subject matter for next week's column.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_10_moaavgo0rf.jpg)


Art by [Clint Cearly](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Clint%20Cearly%22%5D)


**#4: The Identity Problem**


The solution to this problem was to embrace the 5/5/10 model. What was *Dragon's Maze*'s identity? The revisiting of all the mechanics. While the original *Ravnica* block went well, there was definitely some player frustration that we never went back to revisit any of the guilds. Your guild showed up in one set and then that was it. That was all the goodies you were going to get.


A quick trivia aside. The set that came out the summer after Ravnica block was *Coldsnap*, the "missing" set from the *Ice Age* block. We considered a number of ideas for what that set should be. [Brady Dommermuth](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Brady%20Dommermuth), **Magic**'s creative director, fought hard for it to be a fourth Ravnica set with goodies for all ten guilds.


This time, we decided to embrace the idea and play up that *Dragon's Maze* would be the set where every guild gets some more toys.


**#5: The Drafting Issue**


This problem was partially solved by the block planning. In the 5/5/10 model, each Draft environment was unique. *Return to Ravnica* and *Gatecrash* would each be drafted by themselves. Then when *Dragon's Maze* came out, the two would be drafted together for the first time. The trick for the design and development teams was making sure that each played out differently.


As we examined *Dragon's Maze* Draft, we realized that the key difference had to do with color focus. In *Return to Ravnica* and *Gatecrash*, having all three packs support the same five guilds meant players could easily focus on drafting two-color decks. Once you start mixing the packs, two-color decks become harder to draft, but three-color decks start becoming a lot more attractive. The key reason is that any three-color mix involves three different guilds. For example, blue-black-red is a combination of Dimir, Izzet, and Rakdos. One of the neat things about how the block is set up is that any three-color combination splits up the guilds between *Return to Ravnica* and *Gatecrash* two to one. (This was accomplished by making sure each color only appeared in two guilds in each expansion.)


In order to make three colors work better in Draft, we also slowed down the environment. Three-color decks require more setup, which means they take more time to get going. To make sure three-color decks were viable, we had to slow down the environment. Because of the need to make *Dragon's Maze* the slowest of the three Draft environments, the previous two sets were made a little faster for contrast.


The other big thing we needed wasn't done by the *Dragon's Maze* design and development teams, but rather by the *Return to Ravnica* and *Gatecrash* ones. All the teams made sure each of those sets had cards that played nicely with cards from the other set. *Dragon's Maze* then made sure to create new cards that had synergies between different guilds.


**#6: New World Order**


This last issue didn't have an all-encompassing answer. It was more about all the little details to make sure the complexity level didn't rise too much. And, to be clear, cramming ten (I mean, eleven—join me next week) mechanics into a small set meant we were accepting that the complexity was bound to go up a little. We worked hard to make sure it only was a little and not a lot.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/mm242_11_b0xc7nuphp.jpg)


Art by [David Palumba](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22David%20Palumba%22%5D)


### All Together Now


I'm very happy with how *Dragon's Maze* turned out but it definitely was the set we were sweating about the whole block. It had a lot of demands and the least amount of space. I'm happy for previews to begin so you can see all the things we managed to fit in.


Before I leave you for today, I have one last responsibility. I need to show you a preview card. So here's what I'm going to do. I'm going to ask you what card you most want to see. I'm hoping a lot of you said Ral Zarek.


For those unaware of who Ral is, we created a few new Planeswalkers for *Duels of the Planeswalkers* and players have been clamoring for them to finally make it onto cards in the game. I am happy to say Ral is premiering in *Dragon's Maze*. As an Izzet from the plane of Ravnica, how could he not show up in this block?


So, ladies and gentlemen, I am happy to introduce you to Ral Zarek


>> Click to Show![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/dgm/tiwoirwiixix/pwnx7gvean_EN.jpg)
That's all the time I have for today. As always, I'm excited to hear your reactions to the new set. You can email me, respond in the thread, or contact me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)).


Join me next week as I explore how we managed to add in some new stuff while still meeting all of the requirements I laid out today.


Until then, may you find the guild goodies you're looking for.


### Drive to Work #28—*Planar Chaos*


Today, I examine a set that messed with the color pie like no other in **Magic**'s history.


* [**Episode 28**](http://media.wizards.com/podcasts/magic/drivetowork28planarchaos.mp3) : *Planar Chaos* (10.7 MB)
* [**Episode 27**](http://media.wizards.com/podcasts/magic/drivetowork27badcards.mp3) : *Bad Cards* (10.6 MB)
* [**Episode 26**](http://media.wizards.com/podcasts/magic/drivetowork26white.mp3) : *White* (9.8 MB)
* [**Episode 25**](http://media.wizards.com/podcasts/magic/drivetowork25Homelands.mp3) : *Homelands* (10.8 MB)
* [**Episode 24**](http://media.wizards.com/podcasts/magic/drivetowork24Mana_3of3haho5u.mp3) : *The Mana System* (9.92 MB)
* [**Episode 23**](http://media.wizards.com/podcasts/magic/drivetowork23ColorPie_d5z12sxuq8.mp3) : *The Color Wheel* (10.2 MB)








