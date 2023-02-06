
---
[Link to Wayback Machine](https://web.archive.org/web/20201112030700/https://magic.wizards.com/en/articles/archive/feature/developing-return-2012-09-10)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/developing-return-2012-09-10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201112030700id_/https://magic.wizards.com/en/articles/archive/feature/developing-return-2012-09-10"
[_metadata_:wayback_capture_timestamp]:- "2020-11-12 03:07:00+00:00"
[_metadata_:description]:- "Hello! I'm Erik Lauer. I was the lead developer on Return to Ravnica. This is my fifth development lead, following Magic 2010, Magic 2011, Mirrodin Besieged, and Innistrad. I was very excited to lead development for our return to Ravnica.Billy Moreno, Tom LaPille, Zac Hill, Erik Lauer, Dave Humpherys, Shawn Main, Adam Lee"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2012-09-10"
---


Developing the Return
=====================



 Posted in **Feature**
 on September 10, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_eriklauer.jpg)
By Erik Lauer




Erik Lauer is a senior game designer who works on final game design and development. Recently, he has led the Return to Ravnica, Modern Masters, and Theros development teams. 






Hello! I'm Erik Lauer. I was the lead developer on *Return to Ravnica*. This is my fifth development lead, following ***Magic** 2010*, ***Magic** 2011*, *Mirrodin Besieged*, and *Innistrad*. I was very excited to lead development for our return to Ravnica.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_rollcall_mfb7wsfc39_1.jpg)*Billy Moreno, Tom LaPille, Zac Hill, Erik Lauer, Dave Humpherys, Shawn Main, Adam Lee*

### Roll Call

First, let's meet my team for this set's development:

**Zac Hill:**
[He](http://www.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill) led development on ***Magic** 2013*, as well as being the lead developer on "Sinker." Up until a few weeks ago he wrote the [Latest Developments](http://www.wizards.com/Magic/Magazine/Archive.aspx?tag=Latest%20Developments&description=Latest%20Developments) column here on DailyMTG.

**Dave Humpherys:**
[He](http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humpherys)'s the senior development manager and was the lead developer on *Avacyn Restored.*

**Tom LaPille:** A past and now-current author for Latest Developments, [Tom](http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille) is also an experienced developer, having led development on ***Magic** 2012* and *Dark Ascension*.

**Adam Lee:** Keeping the development of the first set in line with the creative world view is a tricky task. [Adam](http://www.wizards.com/magic/magazine/archive.aspx?author=Adam%20Lee) is a veteran, having done this with *Innistrad*.

**Shawn Main:** Large sets usually have a designer on the team. [Shawn](http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main) came to R&D via the *Great Designer Search II*.

**Billy Moreno:**
[Billy](http://www.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno) is one of the newer members of R&D, having been hired as a full-time member last year after interning with us. He's worked on *Avacyn Restored* as well as a few other projects, so I was eager to have him on the *Return to Ravnica* team.

Those six and myself round out the team that developed *Return to Ravnica*. As I said, this set and block were super exciting to work on, but also a bit harrowing, as we had to live up to the original *Ravnica* while successfully differentiating it from that set (but not making it feel alien).

So I came into the set with some goals that I wanted to see. As the lead developer, I'm tasked with both preserving Ken's design vision and looking at the new set from a nuts-and-bolts perspective:




1. Each guild has common elements. [Ken Nagle](http://www.wizards.com/magic/magazine/archive.aspx?author=kenneth%20nagle) decided the set should have guild leaders, guild mages, and charms. Charms were last seen in *Alara* block, but Ken knew they would be a great fit for Ravnica. Since they have three abilities each, and a fixed mana cost, I knew they would be challenging to develop.
2. Each guild must feel unique, with its own style of game play. This needed to hold in all types of play, from kitchen-table **Magic** to FNM to the most competitive **Magic**. Whether you're playing in the Top 8 of the Pro Tour or in the basement at a friend's house with just some booster packs and an intro deck, each guild should play and feel unique.
3. Finally, some players want to go their own way, so it is important to look at the set from a variety of perspectives, and not only guilds. Guilds are a fun way to play, but they aren't the only way to play

With those goals as my sort of guiding lights, I set off to remake Ravnica.

Brian Schneider led *Ravnica: City of Guilds* and it's one of the best sets and blocks of all time. It was home to many cards that players regard as their favorites—the hits that live on years later in all formats. The Limited format, despite juggling the ten guilds, played excellently and is very well remembered by players of all levels.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_f29q94m5vk.jpg)Art by [Daarken](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Daarken%22%5D)

### Splitting the Guilds

In the original *Ravnica* block, the guilds were split 4/3/3, and this time we knew we didn't want to do it the same way. The main concern with guild balance is, of course, the impact it has on Draft. For *Ravnica-Guildpact-Dissension*, the 4/3/3 split worked out for one of the most popular Limited formats ever. In our goal of wanting to differentiate from the original *Ravnica*, [Brian Tinsman](http://www.wizards.com/magic/magazine/archive.aspx?author=brian%20tinsman) came up with the idea of splitting the guilds in two large sets and then making the third set a small set of all ten guilds.

By having *Return to Ravnica* and *Gatecrash* both be large sets, we opened up a lot of space in terms of how to do it. We wanted there to be "circles" defined by the guilds—that is, one guild leads to the next.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_Guilds.gif)  
There are a bunch of variations that could be used to determine these sort of guild paths, so in our exploration we had a handful of additional qualifications.

For example, you'll notice that neither *Return to Ravnica* nor *Gatecrash* contain all the guilds of any of *Ravnica-Guildpact-Dissension*'s sets.

***Ravnica*'s four guilds:** Selesnya and Golgari are in *Return to Ravnica*, Dimir and Boros are in *Gatecrash*.   
***Guildpact*'s three guilds:** Izzet is in *Return to Ravnica*, while Orzhov and Gruul are in *Gatecrash*.   
***Dissension*'s three guilds:** Azorius and Rakdos are in *Return to Ravnica*, while Simic is in *Gatecrash*.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_sjwll75d0s.jpg)Art by [Daniel Ljunggren](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Daniel%20Ljunggren%22%5D)

### Keywords

Beyond just the physical placement of these guilds, development also took a keen eye on how each of these guilds' mechanics played in comparison to old *Ravnica*'s guild mechanics. None of original *Ravnica*'s mechanics were reused in *Return to Ravnica*, but we wanted to make sure that the mechanics felt similar and had good interplay.

Selesnya's mechanic, convoke, relied on the use of creatures to help with casting spells, but their *Return to Ravnica* keyword of populate allows you to create more creature tokens and thus support convoking spells.

Golgari's mechanic, dredge, might be the most popular and dominant mechanic from the original *Ravnica*. Where dredge put cards in your graveyard, our new mechanic of scavenge makes use of the cards in the 'yard.

The same will be true for all of the guilds in the block. We didn't want to sacrifice game play in the name of tying back to the original like this, so when the two came to a head we chose game play.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_0r96vaw0ci.jpg)Art by [Eytan Zana](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Eytan%20Zana%22%5D)

### A Long-Term Goal

I have a game I play with two dice and **Magic**'s history of vanilla creatures. Roll one die for power, and another for toughness. Try to name a matching vanilla creature. Sometimes you can't think of one, because we never made such a creature, so I set out to complete the six-by-six matrix. I thought I had finished it in *Innistrad* with [Fortress Crab](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fortress+Crab), the vanilla 1/6. 

Shawn Main pointed out an incredible fact: **Magic** used to have a vanilla 2/6 and a vanilla 5/2. But no longer! I caught on to his game: [Wall of Heat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Heat) and [Blistering Barrier](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blistering+Barrier) used to be vanilla creatures, but gained the defender keyword. So I finished my project with a couple of creatures you'll see in *Return to Ravnica*.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat212_vqjbsmvgbi.jpg)Art by [Karl Kopinski](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Karl%20Kopinski%22%5D)

### My Card

Now we come to the favorite part of any article in any preview week: the exclusive new card!

We went through a few iterations of guildmages and settled down on gold, two-mana 2/2 creatures with two activated abilities. We knew the Rakdos guildmage should be cruel. After playing around with different abilities, I liked the idea of offering your opponent a cruel choice.

The unleashed mechanic means you are often attacking and putting your opponent in a position of choosing between blocking or taking a lot of damage. That is the perfect time for your guildmage to torment your opponent. With Rix Maadi Guildmage, even a substantial blocker might lose in combat, but if your opponent doesn't block, the consequence can be very painful!

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/rtr/s15reg2t2t_en.jpg)  
  






