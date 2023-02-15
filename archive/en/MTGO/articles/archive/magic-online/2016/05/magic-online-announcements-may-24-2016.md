
---
[Link to Wayback Machine](https://web.archive.org/web/20211209075653/https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-announcements-may-24-2016)

[_metadata_:author]:- "David Whitfield"
[_metadata_:description]:- "What Is the Magic Online Weekly Announcements Blog? Every Tuesday, we round up all of the biggest Magic Online news for the Weekly Announcements Blog. Check in weekly for the latest updates! Quick Links Double Pro Tour Qualifier Weekend, with a Monday PTQ Finals Watch Two Super Leagues This Week Upcoming Power 9 Challenge May 28 Upcoming Sealed RPTQ on Saturday, May 28"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1023246"
[_metadata_:publish_date]:- "2016-05-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online Announcements May 24, 2016"
[_metadata_:wayback_capture_timestamp]:- "2021-12-09 07:56:53"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211209075653id_/https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-announcements-may-24-2016"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-announcements-may-24-2016"
---


Magic Online Announcements May 24, 2016
=======================================



 Posted in **Magic Online**
 on May 24, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_davidwhitfield.jpg)
By David Whitfield




 David works on the Magic community team as a content specialist. He spends his days writing about Magic Online and trying to play too many colors at once in Limited. 






 


**What Is the *Magic Online* Weekly Announcements Blog?**


Every Tuesday, we round up all of the biggest *Magic Online* news for the Weekly Announcements Blog.


Check in weekly for the latest updates!




---

Quick Links
===========


* [Double Pro Tour Qualifier Weekend, with a Monday PTQ Finals](#item1)
* [Watch Two Super Leagues This Week](#item2)
* [Upcoming Power 9 Challenge May 28](#item3)
* [Upcoming Sealed RPTQ on Saturday, May 28](#item4)
* [**Extended** Downtime for May 25, 2016](#downtime)
* [Build Notes](#buildnotes)
* [Ongoing and Upcoming Events](#events)
* [Ask us anything on the *Magic Online* Tumblr!](http://wizardsmtgo.tumblr.com/)
* [Download *Magic Online*](http://magic.wizards.com/en/content/download)




---

**Double Pro Tour Qualifier Weekend, with a Monday PTQ Finals**


Attention all Pro Tour hopefuls: there's a double Pro Tour Qualifier (PTQ) weekend coming up! Standard Pro Tour Qualifier Preliminaries and the *Shadows over Innistrad* Sealed Pro Tour Qualifier Preliminaries begin Thursday, May 26, and run through Sunday, May 29. The Standard PTQ Final will deviate from our usual schedule, instead taking place on Monday, May 30, at 9:00 a.m. PT/4 p.m. UTC.


**Please Note**: These are the last Pro Tour Qualifiers for Pro Tour *Eldritch Moon*. During the June 1 downtime, unused **red** PTQ tokens will be removed from player collections, so make sure to use them up if you have any left!


Learn more about *Magic Online* Pro Tour Qualifiers [here](http://magic.wizards.com/en/content/magic-online-pro-tour-qualifiers#EMN_schedule).


[Top](#top)


 




---

**The Year of Modern Flashbacks Resumes**


It's 2016: the Year of Modern Flashbacks! If you want to build up a collection for Modern, these Flashback Drafts add everything you draft to your collection once the event is over. Even if Modern isn't your thing, you can enjoy a leisurely draft through the planes of the past with rotating formats each week!


Triple *Tenth Edition* block Flashback Drafts begin Wednesday, May 25, after the downtime, and are followed up with a triple *Lorwyn* Flashback Draft. The [full Flashback Draft schedule](http://magic.wizards.com/en/MTGO/articles/archive/magic-online/year-of-modern-flashbacks-2015-12-14) has been updated with formats throughout the rest of the year, so mark your calendar for the formats you're most excited about!


[Top](#top)


 




---

**Watch TWO Super Leagues This Week**


Hear ye, hear ye! Let it be known that there are *two* different opportunities to watch a Super League on [twitch.tv/magic](https://www.twitch.tv/magic) each and every week through June 30! Tune in at 5:00 p.m. PT/12 a.m. UTC for Vintage Super League Tuesdays and Community Super League Thursdays!


This week, the Vintage Super League will be holding a last chance qualifier to get into Season 5 and the Community Super League will be playing some Momir!


<https://www.youtube.com/embed/EbLFQNFS_kA>


[Top](#top)





---

**Upcoming Power 9 Challenge May 28**


Play in the upcoming [Power 9 Challenge](http://magic.wizards.com/en/content/magic-online-format-challenges#Power9) on Saturday, May 28 for a chance to win a piece of the Power Nine!


![](https://media.wizards.com/2015/mtgo/power_9_spread_small.png)


[Top](#top)





---

**Upcoming Sealed RPTQ on Saturday, May 28**


A *Shadows over Innistrad* Sealed Regional Pro Tour Qualifier (RPTQ) is coming up on May 28. Please note, these events are only open to players who have qualified through an in-store qualifier event. **The deadline to sign up for this RPTQ is 11:59 p.m. PT/6:59 a.m. UTC, on May 25.**


Learn more about *Magic Online* Regional Pro Tour Qualifiers [here](http://magic.wizards.com/en/MTGO/content/magic-online-regional-ptqs).


[Top](#top)


 




---

**Extended Downtime for May 25, 2016**


* All tournaments will close Wednesday, May 25, at 12:00 a.m. PT/7 a.m. UTC (that's midnight Pacific)
* Store and trade activity will be suspended at approximately 2:45 a.m. PT.
* The system will be down from 3:00 a.m. until 12:00 p.m. PT.

[Top](#top)




---


**Build Notes**


This week’s update includes a refactor of the threading model and state machines in the client. This will make the client more extensible and allow developers to identify and fix client issues more quickly. As a precautionary measure as part of our downtime process we will bring the system up in restricted mode and periodically enable services in the following order: Open play, store purchases, trading, tournament and league play. While this process will take about an hour, we expect to be fully functional at the regularly scheduled end time of 12:00 p.m. PT/7:00 p.m. UTC.


**General**


* Client refactor of the threading model and state machines.
* Update to message handling in all client scenes.

**Known Issues Releasing**


* Duel Scene | Sideboarding timer displays 0:00 when users log in and out.
* Duel Scene | Occasionally matches are not canceled when host leaves hosted match after an opponent joins but before the match starts.
* Collection | A card added to a deck or binder by dragging and dropping it on the deck/binder icon does not display until the deck/binder is reopened
* Play Lobby | Start Button appears for the host when a match automatically starts after a player joins
* Play Lobby | Game Details of a completed Open Play match does not display Replay Game buttons. Replays can still be accessed from Account > Game History.
* Play Lobby | Closing the match window for an in-progress multiplayer match prevents players from observing the match. Players can still view replays of these matches as normal.

**Promo Grants**


* The May MOPR promos will be granted during this downtime.

[Top](#top)





---

**Ongoing and Upcoming Events**


Head on over to our shiny new event calendar at [MTGO.com/Calendar](http://magic.wizards.com/en/content/schedule-magic-online-products-game-info) for an easy-to-digest breakdown of events happening all across *Magic Online*.


[Top](#top)







