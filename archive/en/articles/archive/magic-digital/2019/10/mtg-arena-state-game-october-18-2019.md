
---
[Link to Wayback Machine](https://web.archive.org/web/20191105152645/https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-state-game-october-18-2019)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "With the October update, we're reprioritizing bug fixes and performance improvements to make MTG Arena the best it can be."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1491596"
[_metadata_:publish_date]:- "2019-10-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "MTG Arena: State of the Game – October 2019"
[_metadata_:wayback_capture_timestamp]:- "2019-11-05 15:26:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20191105152645id_/https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-state-game-october-18-2019"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-state-game-october-18-2019"
---


MTG Arena: State of the Game – October 2019
===========================================



 Posted in **Magic Digital**
 on October 18, 2019 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











Normally, this is the time and place we talk about all the fun and exciting things coming soon to *Magic: The Gathering Arena* (which we'll get to), but we wanted to start today's developer update by addressing some of the concerns currently impacting the state of the game before we talk about what's coming on October 24, 2019.


Performance Check-In
====================


Performance improvements and overall client health is our highest priority for the game right now and will be our primary focus for the next few months. This is something that's been on our radar since the release of *Core Set 2020* back in July, however, the improvements and changes we've made have not been enough for many of our players.


We need to do more. So, we're going to do more. And we're going to keep at it until we can provide the experience players expect and deserve.


Since the release of *Throne of Eldraine*, we've increased the number of developer resources dedicated to finding and fixing the underlying problems. Today, we want to give you more insight into what we've discovered so far and what we're doing to solve it.


**Gameplay Crashes** 


Last week, we released a patch to address crashes that players may have experienced when playing on a device with an integrated GPU. We're continuing to keep an eye out for any additional reports.


**Reconnection Issues** 


Since the September game update, we've seen increasing reports of players experiencing a "black screen" when attempting to reconnect to a match (players can hear gameplay sounds, but only see a black screen until their timers run out or they fully restart their client).


A fix for this issue is currently being tested, and we hope to have it resolved with the October game update.


**Gameplay Hitches, FPS Drops, Unresponsiveness** 


Based on player logs and internal reports, this appears to be related to how our asset database handles finding all the things necessary to display a card in *Magic: The Gathering Arena*. This goes beyond card animations or particle effects: textures, shaders, rule hangers, artwork, even the size and shape of cards when they're in your hand, on the stack, on the battlefield, in your graveyard, etc. This is why players may experience these issues outside of matches, such as during sideboarding, drafting, deck building, or opening boosters.


*Magic* is the most content-intensive CCG in existence, and as we grow *MTG Arena*, we need to scale the capacity of our asset system to accommodate this. We've identified the necessary improvements we need to make to our asset system, however, resolving this is going to take some extensive code refactoring and time.


**Memory Allocation and Management** 


Colloquially known as a "memory leak." We have identified certain assets which are not being correctly cleaned up between games, which increasingly bogs down performance the longer you play. This is currently our primary lead, and we are working toward a solution but will continue to investigate as there may be other causes.


**Your Reports Help** 


There are hundreds of factors that can lead to performance issues, further complicated by variations in computer configurations and hardware. This is why player reports are so important. Please continue to submit support tickets with the following information whenever you experience performance issues:


* Gameplay logs,
* DxDiag analysis, and
* Additional details—what were you doing (building a deck, playing a match, sideboarding, etc.), how frequently do you experience issues (first time, after a few games, every time you play, etc.). The more you can provide, the better!

These reports fill in the gaps that sometimes we can't see, and they are vital to this process. Without your help, we would still be trying to find a viable solution to those gameplay crashes that are now fixed.


**In Summary**


* **Game Crashes – Monitoring**: We believe the changes we made on October 10 have solved this for players with integrated GPUs, but we're keeping an eye out for additional reports.
* **Reconnection Issues –** **In Test**: We are currently testing a fix that will prevent "black screens" after a disconnect, and we hope to have this for the October 24 game update.
* **FPS Drops/Gameplay "Hitches" – Identified**: We have a found a few major culprits behind the FPS drops, and our engineers are currently working on a fix.
* **Memory Allocation – Identified**: We also have a few leads on what's causing extensive memory usage during longer gameplay sessions and are working toward a fix. We're continuing to investigate, as there may be additional steps we need to take.

Again, we want to stress that improving our game's performance and overall stability is our highest priority right now and will continue to be our highest priority until we get the needed results. This is on us to solve, and we'll do whatever is necessary to ensure a better experience for our players.


Beyond what we've outlined above, we're also exploring other options (such as IL2CPP) for additional performance improvements. All of this is going to be a lot of work—which is why we're on [the lookout for an additional six software developers](https://company.wizards.com/content/jobs), with more openings coming soon. Think you can help? Apply!


Friends List Update
===================


Though we had previously announced that this feature would be coming with the October game update, we have decided to delay this feature for the time being. As noted above, our priority right now is focusing on performance improvements and client health, and we didn't want to risk adding a new feature until we've made more progress in that area.


We also know that this is one of our most highly anticipated features, and we want to make sure we do it right.


For those of you looking forward to this, we apologize for the delay. Everything we had previously announced for our social features remains on the roadmap (friends messaging, friend deck sharing), with the goal to expand these features beyond that (eight-person drafts, spectating, four-player formats, etc.) when the time comes.


Brawl Launch Event
==================


Okay, so now for the exciting things.


![](https://media.wizards.com/2019/images/daily/BrawlLaunch_Social_horizontal.jpg)


With the October 24 game update, we're officially adding Constructed Brawl to *MTG Arena*. We will be celebrating with a special week-long Brawl event, where you can win a copy of five rare cards and their respective card styles. These cards were previously only available in *MTG Arena* through Wildcard redemption, as these cards were built for brawling and are not found in booster or Limited packs.


These rewards can only be earned once, but don't worry—you can continue playing in the event beyond five wins.


Brew. Build. Brawl.
===================


For those of you who enjoyed our Courtside Brawl event back in September, it's the same format (play a deck built around a specific legendary creature or planeswalker from the Standard card pool), but now *you* get to choose the legendary creature or planeswalker to build your deck around!


![](https://media.wizards.com/2019/images/daily/brawl_deck.png)


When building a Brawl deck, the first thing you should do is decide which card shall be your commander, as their color identity will determine the color identity of the 59 *other* cards in your deck. Once you've chosen your commander, the deck builder will automatically filter based on their color identity—no need to add any additional filters—and enforce the singleton (one copy of any card) deck-building requirement (except basic lands, of course):


![](https://media.wizards.com/2019/images/daily/brawl_done.png)


And for those of you interested in sharing your deck ideas, [here](http://media.wizards.com/2019/downloads/chulune_deck.txt) is an example output of the what a Brawl deck exported from *MTG Arena* will look like.


Wednesday Brawl
===============


Beyond our Brawl launch event, there will be a Brawl play queue every Wednesday, starting on November 6 at 8 a.m. PT (16:00 UTC) and available for 24 hours. Like our other Standard play queues, there will be no entry fee and no additional rewards, but games will grant quest progress and contribute toward any daily or weekly win counts.


If you need more Brawl in your life, it will also be available all the time through direct challenge, and be sure to check out [your participating local game store](https://locator.wizards.com/event-reservations-web/?searchType=magic-events&query=Los%20Angeles,%20CA,%20USA&distance=25&page=1&sort=date&sortDirection=asc) for *Magic* Weekend: Brawl (Psst! Don't forget that if you participate, you'll be sent a code via email with more *MTG Arena* rewards!)


Showing Off
===========


And for those of you who have been wondering when the *Throne of Eldraine* showcase cards will be in *Magic: The Gathering Arena*, the answer is[nbsp] . . .[/nbsp] soon! Starting in November, we'll be hosting the Festival of the Fae event series, where you can earn some of those whimsical card styles for your collection.


![](https://media.wizards.com/2019/images/daily/fest_artisan.png)


Each event will have a 2,500 gold or 500 gem entry fee and will feature the following formats:


* Artisan: Build a Standard deck using commons and uncommons only.
* Oko's Madness: It's like Momir's Madness, but your creatures are also 3/3 Elk.
* Cascade: When you cast your first spell each turn, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost.

To learn more about these formats, you can check out our [event details page](https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-formats). Mark your calendars, because the festivities begin on November 3 with Artisan! For those who've done the math, three events with five card styles leaves more room for Adventures, and you'll find the remaining showcase cards available for purchase through the in-game store.


![](https://media.wizards.com/2019/images/daily/bundle.png)


These Adventure bundles will only be available until our November game update, though, you will be able to buy each showcase card style separately at a later date.


Daily Wins – Now with XP!
=========================


And no, this doesn't involve us removing it from weekly win rewards either. We're adding 25 XP to daily win rewards for the first ten wins of each day as another way to help players catch up with their leveling if they missed out on a few quests or didn't always finish their weekly wins throughout the first month of the *Eldraine* Mastery Pass.


Clean-Up Phase
==============


Brawl, *Throne of Eldraine* showcase cards, and new events will be arriving on October 24, alongside some quality-of-life changes, bug fixes, and continued work on performance improvements. Keep an eye on our [status page](https://magicthegatheringarena.statuspage.io/) for the full maintenance schedule and follow us [@MTG\_Arena](http://www.twitter.com/MTG_Arena) for the latest information.


Last, but not least, be sure to tune into [twitch.tv/magic](https://www.twitch.tv/magic) all weekend long for Mythic Championship V, where our *Magic* Pro League faces off against some of the top *MTG Arena* players for the $750,000 prize pool!







