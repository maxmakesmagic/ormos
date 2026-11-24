---
id: 6avj0aae
kind: article
lang: en
path: /en/articles/feature/2003/09-19-updates-bans-betas-and-adepts
title: Updates, Bans, Betas, And Adepts
published: '2003-09-19'
column_slug: feature
column: Feature
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped091903
    lang_detected: en
    capture_id: 1831794
    url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
    captured_at: '2005-04-03 17:35:11+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped091903
    lang_detected: en
    capture_id: 1831794
    url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
    captured_at: '2005-04-03 17:35:11+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped091903
    lang_detected: en
    capture_id: 1831794
    url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
    captured_at: '2005-04-03 17:35:11+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped091903
    lang_detected: en
    capture_id: 1831794
    url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
    captured_at: '2005-04-03 17:35:11+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: 6avj0aae
  url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
  page_key: wizards.com/default.asp?x=magic/magiconline/oped091903
  lang: en
  template: classic_asp
  captured_at: '2005-04-03 17:35:11+00'
  capture_id: 1831794
  wayback_url: https://web.archive.org/web/20050403173511id_/http://wizards.com/default.asp?x=magic/magiconline/oped091903
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 6avj0aae
  capture_id: 1831794
  url: http://wizards.com/default.asp?x=magic/magiconline/oped091903
  wayback_url: https://web.archive.org/web/20050403173511id_/http://wizards.com/default.asp?x=magic/magiconline/oped091903
  captured_at: '2005-04-03 17:35:11+00'
  template: classic_asp
  sha256: a59a2eee11c8eb48b683814e0a734fa59f9a42cfd07d583a01b2319dbbd8a6cc
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Entomb')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
### Friday Commentary As Random As Grog

* * *

I've been meaning to start doing a series of "editorials" about what's going on behind the scenes of ***Magic** Online.* However, with the craziness of the past two months, I haven't been able to get around to it. There are a bunch of niggly bits that seem to need some clarification, so it seems a prime opportunity to start now. We'll see if I can keep it up in the coming weeks.

### The Development List

If you haven't checked out the [Tech Updates page](/en/articles/feature/2003/10-09-magic-online-tech-updates) recently, then you might've missed that the [Development List page](/en/articles/updates/2003/09-19-magic-online-development-list) has been updated and changed. I'm going to keep a list of what features are being worked on right now and what stage in development they're at. This also assumes that my annoying child routine continues working on the developers.

**Me:** Are we there yet?  
**Devs:** No.  
**Me:** Are we there yet?  
**Devs:** NO.  
**Me:** Are we there yet?  
**Devs: NO.** Here have some update notes and go play somewhere else. Please!

Assuming no one arms the development team, I should be fine.

Here's what each stage of development means:

*In Design* -- This is what's on the virtual drawing board. Items that are *In Design* may be planned out or might only be in the idea stage right now. None of these items are being coded at the moment and they won't appear on the live server for a long time yet.

For example, both the automatching feature and **Casual Trade** rooms are back to the *In Design* stage. This means that we're still planning on implementing them, but other items are a priority for the team right now (like *Mirrodin* cards).

*In Development* -- This is what's being coded right now. Items that are *In Development* are being worked on by the programmers, but haven't hit testing yet. Things in this stage are still a good ways away from appearing on the live server.

For example, *Mirrodin* cards are still listed as *In Development.* A card set won't leave this stage until all cards are in testing.

*In Testing* -- Like it says, this is what's being tested right now. Items that are *In Testing* are close to release, but haven't passed muster yet. Things in this stage may be pushed back to *In Development* (or even *In Design,* if necessary) if serious errors appear during testing.

For example, the Royal Assassin avatar is listed as *In Testing* because we've had to fix a few errors with the implementation, but it's almost ready to be given out.

*Next Update* -- This is what's coming in the next scheduled update. Items listed as *Next Update* will appear on a scheduled update day. While we **are** back to a weekly update schedule, that doesn't necessarily mean new code is going into the game every week--it may just be scheduled maintenance.

As items leave *In Testing* and the development team tells me they're ready to prop new code, I'll add them to the *Next Update* list.

<table><tbody><tr><td><h3>Banned Cards</h3>&#10;<p>The announcement went out at the beginning of September that <a href="https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=/default.asp?x=dci/announce/dci20030901a#brlist&amp;origin=magic_magiconline_oped091903">Entomb was added to the Banned List for Extended format</a>. Naturally, since Online Extended is different than physical Extended, players were asking if Entomb would be banned on <i><b>Magic </b>Online. </i>The answer is: Yes.</p>&#10;<p>Entomb will be banned from <i><b>Magic </b>Online </i>Extended events as of October 1, 2003. While it's not as powerful a card in the limited cardpool of Online Extended, we're trying to keep things as similar in the online and physical tournament worlds as possible. So, when a card is banned or restricted in the physical game, the same will happen in the online version.</p>&#10;<p>For those of you who want to use it in casual games, you can always play Open format.</p>&#10;</td>&#10;<td><table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Entomb" src="https://i.ormos.uk/ad/27/ad27eb78e7ee9d9bc2e81cd2981dce5e1dacc1ceddcbd2fff73cab0301b59518.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

### Beta Server

The development team says we probably have a few more days of testing using the current beta server setup. The amount of time may be adjusted depending on what bugs we turn up, of course. In this case, we'll probably be taking the beta server down once **Premier Events** testing is done.

While we're still having open beta testing, I'll be checking in with the development team every weekday morning to see what the status is. Once I know, I'll post whatever information I have to the [Announcements folder](https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=http://boards1.wizards.com/forumdisplay.php?forumid=217&origin=magic_magiconline_oped091903).

Current plan is to continue using the beta server for limited open cardset testing. This means that a limited number of players will be invited to help test on the beta server.

In an attempt to stave off the flood of emails and chat requests, let me try to make this clear:  
  
***Neither the Adepts nor the Customer Service team has any information on who will be invited to help test on the beta server the next time it opens up.***

If you receive an invite, you're in. If you don't, you aren't. This doesn't mean you'll always be a tester or will never be a tester. After this round of testing, the next time the beta server goes up will be for *Mirrodin* card testing.

### Adepts

I've seen quite a few complaints about Adepts not helping players out in some situations, not having answers to player questions, or "merely" directing players to where they can get information or have their concerns addressed. Evidently, there's some confusion about exactly an Adept's job entails.

While the ***Magic** Online* Adepts are there to help you find the information you need, their main responsibility is to handle player conduct issues within the game. Since the Adepts aren't Technical Support or Customer Service representatives, they can't help you directly with problems [handled by those groups](https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=/default.asp?x=magic/magiconline/csmain&origin=magic_magiconline_oped091903), which is why they'll direct you there if they don't have an answer you need.

Since the Adepts are the most visible people on the ***Magic** Online* Team, it's understandable that you'll want to vent your frustrations on them. Please don't--they can't do anything to fix the current problems with ***Magic** Online.* However, since they do collect issues to pass on to other parts of the team, they're your best allies when there are system issues.

Please be kind to the Adepts. They have an incredibly tough job when problems with ***Magic** Online* occur--having to be in front of the community while not actually being able to do anything to fix the problems. If you have an in-game question, don't hesitate to talk to an Adept. Even if they don't have answers, they can point you in the right direction. If you need to vent, please do so on the [***Magic** Online* Message Boards](https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=http://boards1.wizards.com/forumdisplay.php?forumid=142&origin=magic_magiconline_oped091903)--we have them so you do have a place to raise your voice and we can hear it.

### What's Coming

There's some good stuff coming in the next few weeks on ***Magic** Online.* I'll have more for you about the "virtual party" (hopefully a better name for it), including a survey about part of what you'll be getting. We're also planning a "State of the Game" article, to tell you more about where we are and where we're going.

In the meantime, I'll leave you with [this](https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=http://www.weebls-stuff.com/toons/21/&origin=magic_magiconline_oped091903).

See you online. (Did someone say [IPA this Sunday](https://web.archive.org/web/20030919000000/http://wizards.com/leaving.asp?url=http://boards1.wizards.com/showthread.php?threadid=100070&origin=magic_magiconline_oped091903)?)

-Dan