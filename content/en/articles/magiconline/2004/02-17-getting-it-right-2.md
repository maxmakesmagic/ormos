---
id: jkwmx92d
kind: article
lang: en
path: /en/articles/magiconline/2004/02-17-getting-it-right-2
title: Getting it Right
published: '2004-02-17'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm2
    lang_detected: en
    capture_id: 1950251
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
    captured_at: '2005-04-04 23:29:22+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm2
    lang_detected: en
    capture_id: 1950251
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
    captured_at: '2005-04-04 23:29:22+00'
    rule: registry.known_article
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm2
    lang_detected: en
    capture_id: 1950251
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
    captured_at: '2005-04-04 23:29:22+00'
    rule: classic.byline
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm2
    lang_detected: en
    capture_id: 1950251
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
    captured_at: '2005-04-04 23:29:22+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: jkwmx92d
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm2
  lang: en
  template: classic_asp
  captured_at: '2005-04-04 23:29:22+00'
  capture_id: 1950251
  wayback_url: https://web.archive.org/web/20050404232922id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jkwmx92d
  capture_id: 1950251
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
  wayback_url: https://web.archive.org/web/20050404232922id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm2,,pt,0
  captured_at: '2005-04-04 23:29:22+00'
  template: classic_asp
  sha256: 21fb48319ef39e68fe0a3e89d8cb303b9a48eccf2b34ad32e3c4b86521621681
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:autoCardWindowSR('Mindslaver')
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - Mindslaver
  occurrences: 1
---
### Current issues and the big picture

There are several issues I know the ***Magic** Online* community is concerned about. First, you need to know exactly where we are in regards to repairing the game.

![](https://i.ormos.uk/2b/65/2b65047e29c8353bb42d3e66a889c4fc995363e7fdb2110e49d0267374e944f2.jpg)When the big crashes happened during the *Mirrodin* Release Events, we had to make a hard decision regarding the **Premier Events** room. Obviously we don't want to have tournaments shut off; however, making ***Magic** Online* completely unstable was even more intolerable. So, tournaments were taken down and we've not made an attempt to bring them back up again until we're able to correct the underlying problem.

After this disappointment, the whole team entered into what we called “Pause and Reflect” mode. I wish this were as Zen as it sounds. What it consisted of was everyone looking hard at the resources we have and what needs to be done to make ***Magic** Online* work the way we want. Let's just say that making tough calls on a game that so many people are invested in leads to some impassioned arguments.

The conclusion the team came to is that, rather than some patchwork solution, ***Magic** Online* needs to be rebuilt from the ground up. Given the time frame we're talking about that's a tough decision to have to make, but the point is *we need to get it right*. (We're just as unhappy about the current situation as you are, but no one wants to go through another Version 2.0 launch, either.) That also leads to deciding what can be done about the *current* state of the game during that rebuilding process. Given that a total rebuild would take a minimum of 18 months (and probably more than that), what was an acceptable condition for ***Magic** Online* in the meantime?

### Resource Management

In the end, it comes down to a balancing act between giving the community a working game while also getting a new version built. At the moment, we have most of the features necessary to keep ***Magic** Online* working on a basic level--you can play both Limited and Constructed games, trade cards, and chat with other players. The major missing piece is the **Premier Events** room.

<table><tbody><tr><td>&#10;<h3><i>Making tough calls on a game that so many people are invested in leads to some impassioned arguments...</i></h3>&#10;</td></tr>&#10;</tbody></table>

So, shuffling of resources ensued. We've got a small team dedicated to keeping the current version of ***Magic** Online* up and running. This includes bug fixes and new set coding. The rest of the team is focused on the long-term rebuild of the game. But where does that leave the **Premier Events** room for now?

One of the reasons you haven't had an update on this in a while is that there's not much to talk about yet. As most of you know, the **Premier Events** room and server stability issues are tied together. We brought in extra programmers to concentrate on fixing the **Premier Events** room, which means cleaning up the master server code. As they make progress on fixing master server code, we get closer to being able to have tournaments again.

While there's been promising news from the code cleanup folks, we're still concerned about stability. The good news is we may be able to go after the tournament code directly in the near future. The bad news, however, is we also may conclude that it's impossible to bring tournaments back up without sacrificing stability. When it comes to making calls on the current state of the game, stability is the number one issue, followed by tournament play.

What that means is we may have to make the decision that there will be no tournaments until the full rebuild is complete. In that scenario, that means the **Premier Events** room stays closed for at least the next 18 months—maybe more. No decision has been made yet and the timing for the full rebuild isn't set in stone. In the meantime, we still have folks dedicated to master server code cleanup on the current system.

### Weekly Updates

While we're going to continue bringing down the system on Thursday each week, there's not always a lot to talk about regarding those updates. Usually we're only doing routine maintenance or other items that make no visible difference to the ***Magic** Online* game itself. Part of last week's downtime was to load operating system patches, which is about as exciting as downloading OS patches for your home computer. The only other item of note was that we propped some new code to the store in preparation for [this week's price change](/en/articles/announcements/2004/01-12-pending-price-increase-and-other-news).

While those updates were invisible, you'll probably notice this week's downtime. Specifically, due to the price changes on Thursday, February 19, the ***Magic** Online* Store will be down most of the day. Current estimates are in the 2- to 4-hour range. Once the game goes down Thursday morning (about 8:00 AM Pacific Standard Time), the store won't be back up for a while. There will be an in-game announcement when the store is open again.

### *Darksteel* Beta Status And Release Events

In other news, according to Jess' risk assessment from the beginning of last week, we're still on target for the March 1 release of *Darksteel* cards on ***Magic** Online*. There were about 50 bugs the team was working on and nothing that should push back the release date.

You can get all the details of the *Darksteel* Release Leagues [here](/en/articles/uncategorised/2004/02-02-darksteel-release-event-announcement). However, during planning, something slipped our minds. Let's rectify that situation now.

![](https://i.ormos.uk/2d/a3/2da3743fd8b681e88c8054f5d32ee9c1b2788f94a3855289b357470184dc8fbc.jpg)Beginning after the update on Thursday, March 4, you'll be able to play in limited triple-*Darksteel* drafts. Until the release leagues stop respawning on Monday, March 8, there will be a *Darksteel-Darksteel-Darksteel* draft queue available along with the regular ***Magic** Online* draft queues. These queues will have all *Darksteel* boosters as prizes.

Enjoy them while you can—triple-*Darksteel* drafts will only be available while release leagues are spawning. (Regular *Mirrodin-Mirrodin-Darksteel* draft queues will remain.)

### Upcoming Topics

I know some of you have concerns about cheating in the *Darksteel* Release Leagues. I brought these concerns to the Steering Committee last week, and it looks like I'll have some answers for you in next week's column. I'll also talk about what may've been the hardest **Magic** card we've ever coded…and it wasn't Mindslaver.