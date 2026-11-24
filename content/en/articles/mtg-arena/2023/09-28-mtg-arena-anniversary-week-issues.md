---
id: r2q69t61
kind: article
lang: en
path: /en/articles/mtg-arena/2023/09-28-mtg-arena-anniversary-week-issues
title: MTG Arena Anniversary Week Issues
published: '2023-09-28'
column_slug: mtg-arena
column: MTG Arena
authors:
- slug: chris-kiritz-55019ce1
  name: Chris Kiritz
- slug: ben-smith-d24f3c2d
  name: Ben Smith
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    lang_detected: en
    capture_id: 237582
    url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    captured_at: '2024-05-20 06:34:42+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    lang_detected: en
    capture_id: 237582
    url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    captured_at: '2024-05-20 06:34:42+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    lang_detected: en
    capture_id: 237582
    url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    captured_at: '2024-05-20 06:34:42+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    lang_detected: en
    capture_id: 237582
    url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
    captured_at: '2024-05-20 06:34:42+00'
    rule: url.article_section
sources:
- document_id: r2q69t61
  url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
  page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
  lang: en
  template: contentful
  captured_at: '2024-05-20 06:34:42+00'
  capture_id: 237582
  wayback_url: https://web.archive.org/web/20240520063442id_/https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
- document_id: r2q69t61
  url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues?lid=snenn16vjw4f
  page_key: magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues?lid=snenn16vjw4f
  lang: en
  template: contentful
  captured_at: '2024-01-06 01:04:11+00'
  capture_id: 237584
  wayback_url: https://web.archive.org/web/20240106010411id_/https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues?lid=snenn16vjw4f
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: r2q69t61
  capture_id: 237582
  url: https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
  wayback_url: https://web.archive.org/web/20240520063442id_/https://magic.wizards.com/en/news/mtg-arena/mtg-arena-anniversary-week-issues
  captured_at: '2024-05-20 06:34:42+00'
  template: contentful
  sha256: 54bae96fccb5d5320d0f02139682b9e4d86e4ad38827e72e63beea9e18754de5
render_recovery: []
---
Greetings *MTG Arena* players,

Well, this last week sure hasn't gone as we planned. What was originally scheduled to be a celebration of five years of fun hasn't quite lived up to that promise, so today I wanted to apologize. We'll talk a little later about some of the "how," but one of the things that I emphasize with the team is that players don't care what's happening behind the scenes when their experience is bad, they just want to know when it will get better, so let's get to it.

![Card art for Workshop Warchief by Zoltan Boros](https://media.wizards.com/2023/images/daily/cardart_snc_workshop_warchief.jpg) 

The short answer is, we're working on it but don't have an official timeline yet. For many, the game is fine, but there are certain areas that are still experiencing issues that we're troubleshooting. As a steward of this game that so many play each day, I know this isn't a fulfilling answer, but it is where we are right now, and for that we're sorry.

On the bright side, most areas of the game are currently stable and functional (and if you read the entire article, you'll even see where we made improvements), though we're treading with some caution as we're not fully out of the woods yet. Here's our current status:

*   Premier Drafts are up and running after being disabled part of last week. We messaged players who may have been affected. We've heard some feedback that we may have missed some players and will validate that this week, but …
*   Player inbox is currently disabled as we're troubleshooting some issues that started on Friday and persisted through the weekend. This means that messaging slated for the last couple days of our anniversary is paused until we get that sorted out. Once we're confident the system is working correctly, we'll finish our anniversary messaging.
*   The system is currently stable, but we're aware of a brief outage that occurred early Monday morning (Pacific time), but we believe that was coincidental and not related to our core issues. Unfortunately, it has complicated our investigations.

As for next steps, we'll continue to troubleshoot and fix the underlying issues that *are* creating disruptions. We've already made a couple fixes that are minimizing some of our symptoms, but we've not yet cured the illness. While we don't expect more unplanned disruptions, our team remains on high alert in case they happen.

We'll need to deploy additional fixes over the next week or two as we identify solutions to issues, and while we'd expect those deployments to be like our normal release process, there is a chance a full system outage may be required. If that is the case, then we'll let players know the day prior to the outage. 

Finally, once we're comfortable that all systems are go, we'll turn on anything that is disabled and get back to the fun. Thanks for all your support and may all your topdecks be great.

**Chris Kiritz  
Executive Producer, *Magic* Digital**

 

…Oh, are you still here and interested in learning more? Great, let's pull back the curtain a bit and talk about how we got here. First, a peek at our process (queue the *Schoolhouse Rock!* music).

## The "How"

Everything we do starts on a software engineer's machine. We have a problem or need, and they create the code that solves that problem or need. Sometimes it is one engineer, sometimes a team, but the general process is the same.

Once they've completed their work and run some basic tests, we identify which release that change will go into. Easy or time-sensitive things might go into a release that is only a couple weeks away. Other changes might need extensive testing, have high risk, or require other changes to be delivered first. In that world, the work is checked into a release that may be months away.

Once checked into a release, our QA team tests it using a variety of manual and automated tests. This will be both discrete tests around the change, as well as more generalized system tests to ensure the change hasn't inadvertently affected other parts of the game. As the release gets close to the live date, we raise the bar on what can be considered for that release—it is easier to get changes in for a release that is two months away than it is to get a change in for a release that is two weeks away.

The P0 Live Team is a strike team of the people best qualified to solve P0 issues—critical issues more important than Priority 1. 

A couple weeks before a release goes to the public, we lock it down so no additional changes are made as we prepare to submit it to our publishing partners, like Apple and Google, for review.

On the day of release, we deploy to live and then move players gradually over from the old version of *MTG Arena* to the new version. This is when you get your download notification and grab the latest version. When everything goes well, that is the entirety of the release. 

Last Tuesday, we updated some database services as part of our general ongoing maintenance. This is like keeping your phone operating system up to date to ensure you're getting the latest features and security updates. Since we're always cautious when dealing with major systems like our databases, this work was completed in March and then propagated to all our internal environments for feature testing, load testing, and just a general soak to see if anything organically crops up as we go about our daily work. After months of internal operation and stabilization, we felt confident in releasing to our production environment.

Unfortunately, after that release went live, we found that it didn't behave on production the way we expected, but instead degraded the performance of various system messages. While this was unnoticeable in most areas of the game, Premier Draft felt this degradation acutely. After we discovered the issue, we disabled Premier Draft and activated our Priority Zero Live Team (otherwise known as the P0 Live Team) to troubleshoot. The P0 Live Team is a strike team of the people best qualified to solve P0 issues—critical issues more important than Priority 1.

## Ben Smith Talks Premier Drafts

Ben Smith, a senior software engineer, was the person who built the Premier Draft system and a shoo-in member of the P0 Live Team dealing with Premier Draft problems, so I'm going to turn it over to him for the next part:

As the author of the current implementation of Premier Draft and avid Draft player, I take a special interest in Draft issues. Draft is the format I play most, and positive player experience is important to me (I'm not only the Premier Draft president but I'm also a client). Now that Premier Drafts are back online, we have some time to talk about what happened and what steps were taken to correct the situation.

During Premier Draft's construction, one of our top priorities was the protection of player choices. Every draft pick we successfully received was written to the database immediately. In the unlikely event of a service crash, player picks were not lost. In a general best practices sense, this felt correct. Losing data is always bad, right? Let's protect it.

Last week, a sudden and unexpected database performance issue sprang up. Our services suffered from severe delays during database writes, where actions taken by players are recorded for future reference. Behind the scenes, engineers were scrambling to investigate and diagnose the issue. Most of the system continued to work as normal, with slightly noticeable wait times. However, the impact on Premier Draft was catastrophic.

The processing of player picks ground to a near halt, backing up severely, such that card picks were not being processed until after their pick timer had expired. Picks hung, card pools were composed of auto-pick soup, dogs and cats were living together, mass hysteria! We couldn't subject our players to the nightmarish hellscape of lost card picks, packs that never arrived, or unresponsive draft picking screens. Premier Draft had to be taken offline until we could resolve the issue.

As the database issue dragged on, we began exploring options for making draft more resilient under our degraded performance conditions. We found ourselves challenging our previous assumptions. Do we need to write every player pick to the database? After all, draft data is only necessary for a short time until the picking phase of a draft is over. What do we do with this data?

Our saved draft data was only used during a server crash recovery scenario. Any interrupted draft was reloaded from data when one of the players returned and triggered the draft to be resumed. Since there was no guarantee that any of the other seven players in the draft had returned, most interrupted players would return to an auto-picked card pool. These players would certainly (and justifiably) be unhappy with their draft experience.

We asked ourselves "why are we supporting this draft recovery scenario?" Over the past two years, the ominous specter of draft-related server crashes has never come to visit. As an avid drafter myself, I would certainly prefer to start a new draft where I could pick new cards uninterrupted rather than returning to an auto-picked card pool and have the added chore of requesting reimbursement.

Since Premier Draft's database support existed only to support an undesirable recovery scenario for a problem that was extremely rare, we opted to remove it completely. With the frequent database writes removed, Premier Draft is now less sensitive to database performance issues. Players returning to a draft interrupted by a server crash can start a new draft on the same event without having to request reimbursement.

To be clear, while Premier Draft-related service crashes have been extremely rare, network and connectivity outages may still impact a player's draft experience. In these cases, players may return to an auto-picked card pool, as the draft is still running successfully, but the player is unable to interact with it.

Now that the new draft code is in place, we are providing a more performant player experience with a better outcome in the unlikely event of a Premier Draft service crash.

As part of the leadership team, I am often part of the P0 Live Team, and I'm always impressed with how the team rises to meet challenges. While we would obviously prefer players never experience issues, we're aware that we must be prepared to solve problems on the fly, and having a team you can trust to engage in direct and active conversations while looking for player-facing solutions is a key component to successfully running a game like this.

If you've made it this far, hopefully it's been interesting, informative, or both. Thanks again for being the best community in the world, and hopefully next time I'm writing something like this, it isn't in response to a major issue.

Good luck and have fun,

**Chris**

![Card art for Riveteers Confluence by Vladimir Krisetskiy](https://media.wizards.com/2023/images/daily/cardart_snc_riveteers_confluence.jpg)