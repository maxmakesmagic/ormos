---
id: 59yfejdh
kind: article
lang: en
path: /en/articles/magiconline/2004/04-06-one-team-two-team
title: One Team, Two Team…
published: '2004-04-06'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm9
    lang_detected: en
    capture_id: 1950540
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
    captured_at: '2004-08-15 19:17:51+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm9
    lang_detected: en
    capture_id: 1950540
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
    captured_at: '2004-08-15 19:17:51+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm9
    lang_detected: en
    capture_id: 1950540
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
    captured_at: '2004-08-15 19:17:51+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm9
    lang_detected: en
    capture_id: 1950540
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
    captured_at: '2004-08-15 19:17:51+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: 59yfejdh
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm9
  lang: en
  template: classic_asp
  captured_at: '2004-08-15 19:17:51+00'
  capture_id: 1950540
  wayback_url: https://web.archive.org/web/20040815191751id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 59yfejdh
  capture_id: 1950540
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
  wayback_url: https://web.archive.org/web/20040815191751id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm9,,ja
  captured_at: '2004-08-15 19:17:51+00'
  template: classic_asp
  sha256: 9ef6fd2e0deeaef1d0493a66b5ad59db30384649edefce58a347f528a3d276b8
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:techsupport@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - Technical Support
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Viridian[Zealot')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Viridian Zealot
  occurrences: 1
---
### Reimbursement, open beta, and incoming fixes

### Recap: Last Week

The biggest news of last week was the sudden appearance of product in players' accounts. When we started running the script to compensate players for drafts that crashed during the *Darksteel* Release Events, something went wrong. Our mistake resulted in us, as one person put it, “carpet-bombing” players with product. With no rhyme or reason, some players just got stuff.

As we'd done mass grants before, we were concerned with what seemed a well-formed process going so wrong. The reality was, while we'd run scripts to compensate players for leagues and tournaments before, we'd never done so for 8-player queues. Evidently things don't work quite the same in both situations.

Result? Christmas in March for some players and a delay getting the compensation to folks in the queues. We're sorry for the continued wait, but players in the crashed queues aren't going to get their compensation until we've made sure the script is working correctly. I'll let you all know when we're ready to push the button.

Once we realized this problem was only associated with the 8-player queues, we went ahead with the league compensation grants. Those finished up last week, so if you're a person who was in a league that was lost during the *Darksteel* Release Events, you should have your product by now. If you don't please contact Technical Support and let them know what league you were in.

![](https://i.ormos.uk/71/ae/71ae7150501a35e22356e7fcb3baa9d023620cddab5c65253203f0c9ae8fc19e.jpg)For those of you in *Darksteel* leagues that crashed, you won't have gotten your Viridian Zealot avatar yet. That requires a separate script that we'll be running after the open beta finishes. There are two reasons for waiting. One is that you can't change your avatars now due to a bug and that fix is waiting for post-beta. Two is we haven't decided what to do about *Darksteel* Release Events. I'll let everyone know after Thursday where we're going from here.

### Speaking Of Beta…

If you missed the announcement on Friday, as of noon Tuesday, April 6, we'll be in a 48-hour open beta test. The goal is to hammer the heck out of leagues and premier events in hopes we'll be able to return them to the live server. We'll be meeting Thursday afternoon (after we return everyone to the live server) to discuss how things went.

As of the time I'm writing this article, we've had a small number of players on the beta server for about a week. Things have gone well so far, so it's time to see what happens with a larger load of players.

I've had a few updates since Friday (which I'll add to the original announcement).

*   The product given out will match whatever was used in the event. I have, however, been notified that we're not running *Invasion-Planeshift-Apocalypse* or *Seventh Edition* events.
*   In order to switch things over, we have to take the live server offline about an hour before the beta server comes up. This means the live game will be brought down at 11:00 AM (1100 hours) Pacific Daylight Time Tuesday morning.
*   The store will go offline a half hour before the live server comes down (10:30 AM PDT) to make sure orders are processed before the switch.

[Please read the announcement for full details](/en/articles/feature/2004/04-02-please-read-league-and-premier-event-open-beta).

Remember, when you log on to ***Magic** Online* after noon on Tuesday, April 6, you'll be on the beta server. You won't have access to your normal collection until we switch back over to the live server on Thursday, April 8 around noon.

### Who's On First?

Over the course of the last few months, you've heard me talk about many different parts of the development team and a few different code bases. Since we're running an open beta this week, it seems a good time to try and clarify a few things.

When we run an open beta where all players are on the beta server, we don't actually *do* anything to the live codebase. Beta code and live code are on two completely different boxes. This is why you don't see your normal collection during beta—your account's collection information is stored on the live server.

It is, technically, possible to give you a copy of your collection on the beta server. We don't for a couple reasons.

First is because of the possible confusion. Players might log on and initiate trades thinking that it was their normal account. Then, after we switched back to the live server, all the trades would magically go away. At least if players aren't aware we've switched to beta, they're going to ask questions as soon as they see no cards in their collections.

The second reason is due to the time it would take to copy over the information. To make sure everyone had *exactly* what was in his or her account at the switch, we couldn't copy the database information until we shut down the live server. That takes time and would delay getting everyone onto the beta server. We'd rather get the test started and finished as quickly as possible so we can get everyone back to the live game. We'd have even more problems if we took a snapshot at some point before the switch. Imagine buying some boosters from the store on Tuesday morning and seeing them show up in your account. You log back in Tuesday afternoon and the boosters are gone. They aren't really gone; you're just on the beta server with an older version of your collection installed. However, as far as you know, someone may have gotten your password and is stealing your cards.

It's a lot easier to explain that a player has no cards than it is to explain why things seem to be missing.

### What Is This Beta Code Of Which You Speak?

The current beta server contains one major and many minor differences from the live server. The major difference is the fix for leagues and premier events. The minor differences are fixes for various bugs currently on the live game. Let's step into the wayback machine for a minute.

This past February, we added more people to the ***Magic** Online* development team. The dev team basically consists of three parts: the game devs, the card devs, and the store devs. The game devs work on coding the ***Magic** Online* client software and server. The card devs code the game rules, fix card bugs, and make sure their cards work with the live version of the game. The store devs work on everything that makes the ***Magic** Online* store work—from card purchase and delivery to fraud protection.

![](https://i.ormos.uk/6f/eb/6febfe5398da3052c5203cd6b1fc64c4b02b03e106ca67eb2d7592fd9f54fdd8.jpg)

At the beginning of the year, we added some staff to the development team and split the game devs into three areas.

One group is focused on redesigning the entire ***Magic** Online* game. There's no code currently associated with this team. Right now, they're still working on the design-side of the new version. For those of you thinking about the 18-24 month development timeline that was mentioned a few months ago: yes, that timeline included both design *and* development. We'll have a better idea how much longer this will take in about a month or so. The “3.0” group doesn't do anything with the current system. They're focused on getting the redesign done. Programmers are “borrowed” for their expertise occasionally, but we try to avoid that as much as possible.

Next is the live team. Their main responsibility is maintaining the version of ***Magic** Online* that you play on. They're the ones hunting for bugs and doing updates to the system. They aren't tasked with doing any new development to the game and tend to leave the server code alone unless absolutely necessary.

The third group I'm going to call our “live-server task force.” Back in February, this group took the current version of the ***Magic** Online* server code and started cleaning up problems with it. From the point this group was formed until the beginning of March (when *Darksteel* Release Events blew up the live game), their code sat by itself on its own machine. All that team did was try to find where the server code was broken, fix it, test it, and move on to the next problem as soon as they could.

### Conjunction Junction

At the point *Darksteel* Release Events splattered the game at the beginning of March, we had three sets of code. The first was what was on the live game. The second was the same code on the beta server that we used for testing bug fixes before they went out. The third was what the live-server task force had been working on. (Again, as of right now, there's no such thing as “3.0 code” as it's still in the design stage.)

I've covered the details of what happened next during the last month. The task force's code was moved over to the beta server for testing and, eventually, became the live code. At the same time, the devs on the task force were added to our live team. What exists on the live server today is the result of that work plus some bug fixes.

The beta server is based on the live server code. (You can't see if fixes are going to work on the live server unless the beta code and the live code are the same.) At the moment, it contains fixes for leagues and premier events, along with fixes for other bugs (avatar changing, private messaging, etc.).

And this is why we're waiting for the results of the open beta test before we make decisions on lots of things. If things go well, we get to dump a bunch of fixes onto the live server including working leagues and premier events. If things don't go well, we'll have to change the beta server to match the live server, try out all the smaller bug fixes on it (non-league/premier event), then push those out to the live game.

### To Recap

Here's where we stand:

*   Two versions of the ***Magic** Online* code: live and beta. The 3.0 “code” is a bunch of design documents right now.
*   Two game development teams: live and 3.0. The team working on cleaning up the servers is now part of the live team.
*   The card and store developers are separate from the game developers. They work on their individual parts of the game and with the game devs to make sure each part “plays nice” with the others.

Once we see how this week's open beta goes, the team will decide on things like general compensation and Darksteel Release Events. Here's to hoping I've got lots of good news for next week's column.

Until then, see you online.

-Dan