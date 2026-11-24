---
id: r91p2xrw
kind: article
lang: en
path: /en/articles/uncategorised/2019/10-30-player-solutions-with-companion
title: Player Solutions with Companion
published: '2019-10-30'
column_slug: uncategorised
column: uncategorised
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    lang_detected: en
    capture_id: 763207
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    captured_at: '2022-07-03 11:06:19+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    lang_detected: en
    capture_id: 763207
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    captured_at: '2022-07-03 11:06:19+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    lang_detected: en
    capture_id: 763207
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    captured_at: '2022-07-03 11:06:19+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    lang_detected: en
    capture_id: 763207
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
    captured_at: '2022-07-03 11:06:19+00'
    rule: url.article_section
sources:
- document_id: r91p2xrw
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
  page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
  lang: en
  template: drupal
  captured_at: '2022-07-03 11:06:19+00'
  capture_id: 763207
  wayback_url: https://web.archive.org/web/20220703110619id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: r91p2xrw
  capture_id: 763207
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
  wayback_url: https://web.archive.org/web/20220703110619id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/player-solutions-companion
  captured_at: '2022-07-03 11:06:19+00'
  template: drupal
  sha256: 5618b3939485a14c723630ffbccf83f0ce39c05e1b4ee1a7e86cd26a4dad5140
render_recovery: []
---
This week's *Magic: The Gathering* *Companion* release includes updates to a few issues that were impacting users as well as a behind-the-scenes look at what we're working on for coming weeks.

**Random Player Seatings for Draft**

Our beta testers quickly pointed out early in development that there was an issue with draft seatings: they're not random. Instead, the player who joined the event first is seated in seat 1, the second player in seat 2, and so forth. The latest version updates the seating algorithm to place players randomly and solves this problem.

**Tournaments Failing in Phone "Sleep" States**

Another big item we've heard from many of our iOS testers is that allowing your phone to go to sleep while running a tournament with *Companion* can create a fail state that causes the tournament to become corrupted and unable to continue. That's a worst-case scenario for users, and we wanted it fixed quickly. This build ensures that bug isn't experienced by users, though, closing the app and reloading it *will* still cause your events to be erased. We're working on a feature to help improve that experience later as well, but for now, the bug causing events to crash simply because users didn't want to leave their phone open for long stretches of time is fixed.

**What's up Next . . .**

As I've said before, and have received questions about via email and social media, the changes you see in the Open Beta version of *Companion* every two weeks are only a small part of the work the devs are doing. In addition to these user-facing changes, we're working on big steps forward for the technology in the backend. Most important is the ability for you and all the players in your event to participate in the same event experience each using your version of *Companion*. Participants will be able to manage the pairings, results, and standings of the event through the *Companion* app on their phone. The team has been hard at work building this feature set, and it has occupied the bulk of their time. I'm hoping to show some of what this feature looks like soon and roll it out later this year.

In addition to that large feature lift, we're also working on a set of features we call the "daily engagement features." When we initially set out to build *Companion*, we knew running events was a complex problem we wanted to solve well but that most *Magic* players don't need that functionality on a daily basis. The daily engagement features allow us to solve problems players need solutions for daily. Our UX team has just completed the work on our first designs for those, and I'll be talking about them more in the coming weeks. As always, thanks for supporting *Companion*!