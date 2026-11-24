---
id: 37k1a94a
kind: article
lang: en
path: /en/articles/uncategorised/2003/10-01-everything-is-fine-nothing-is-broken
title: Everything Is Fine. Nothing Is Broken.
published: '2003-10-01'
column_slug: uncategorised
column: uncategorised
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/news100103a
    lang_detected: en
    capture_id: 1831148
    url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
    captured_at: '2005-04-04 04:47:08+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/news100103a
    lang_detected: en
    capture_id: 1831148
    url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
    captured_at: '2005-04-04 04:47:08+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/news100103a
    lang_detected: en
    capture_id: 1831148
    url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
    captured_at: '2005-04-04 04:47:08+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/news100103a
    lang_detected: en
    capture_id: 1831148
    url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
    captured_at: '2005-04-04 04:47:08+00'
    rule: classic.column_marker
sources:
- document_id: 37k1a94a
  url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
  page_key: wizards.com/default.asp?x=magic/magiconline/news100103a
  lang: en
  template: classic_asp
  captured_at: '2005-04-04 04:47:08+00'
  capture_id: 1831148
  wayback_url: https://web.archive.org/web/20050404044708id_/http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 37k1a94a
  capture_id: 1831148
  url: http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
  wayback_url: https://web.archive.org/web/20050404044708id_/http://wizards.com/default.asp?x=magic/magiconline/news100103a,,fr
  captured_at: '2005-04-04 04:47:08+00'
  template: classic_asp
  sha256: 5e88046c059bf19528c6df29800554a3fb8c3f5c4a0bbe6cb65a4982dbad5e35
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Teferi[s_Curse')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Teferi's Curse
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Balshan_Collaborator')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - occasional flavor text writer
  occurrences: 1
---
### Where We Are. Where We're Going.

* * *

On the afternoon of July 28, 2003, I bolted early from GenCon and hopped on a plane from Indianapolis to Seattle. I wanted to make sure I got back in time for the launch of ***Magic** Online* Version 2.0 that night. I got into the office about 11:00 PM and, along with the development team, basically didn't leave for the next two weeks.

How could a few feature changes be such an unprecedented disaster for ***Magic** Online?* Well, it wasn't the visible stuff that was causing so much trouble (although it did cause some); it was the background changes. The development team made significant modifications to the server architecture to -- among other things -- get around some memory restrictions. 

Evidently, the system didn't like that much.

We also found out that, while our test harness was just fine for load testing ***Magic** Online,* it was lacking in the "random player behavior" department. Everything ran smoothly in test. Inevitably, however, the minute the code went live, players found every hole we didn't. I guess there's no real substitute for a large number of live players going about their normal business.

Over the next two months, the upgrade would cause strife, headaches, and much shaking of our fists at the sky as the codebase for ***Magic** Online* continued to foil our every attempt to get the game up and running well. Now that we've got everything back to a semblance of normality, it's time to look forward. From what I've read on the message boards, that seems to be what most of you want, too.

<table><tbody><tr><td><p>The title of this article has less to do with current status than does my taking a moment to laugh at myself. Thanks to a <a href="https://web.archive.org/web/20031001000000/http://wizards.com/leaving.asp?url=http://www.misetings.com&amp;origin=magic_magiconline_news100103a">MiseTings.com</a> contributor, we have a new version of <a>Teferi's Curse</a> specifically for <i><b>Magic </b>Online. </i>(No, that doesn't mean it's going to be available for play.) As an <a>occasional flavor text writer</a>, I found it even funnier.</p>&#10;<p>Thanks again to everyone who injected some humor into the situation -- even if you were ripping us apart at the time. While it certainly wasn't funny that we couldn't get <i><b>Magic </b>Online </i>stable for such a long stretch of time, it definitely gave our sense of the ridiculous a workout. (No, I wasn't typing my updates from a hotel room in Vegas; although I wished I were most of the time.)</p>&#10;</td>&#10;<td><img src="https://i.ormos.uk/6f/86/6f8615dbe65130229bf7d2cfd54e83a3cadee7e48bfdc41a69cbd5874bca1598.jpg"></td>&#10;</tr>&#10;</tbody></table>

No, not everything is completely back to normal in ***Magic** Online.* Yes, we had to pack some functionality off to the drawing board. However, at some point we had to declare the worst Version 2.0 beasts vanquished and get things moving forward. While we could spend all our development time tweaking the game to get everything checked out five-by-five, with *Mirrodin* launch just around the corner, we need to put our resources toward that.

I can't tell you that we've completely fixed everything that went wrong behind the scenes. The team did a fairly substantial post-mortem on the Version 2.0 launch, and we've changed the way we do some things. (The most obvious example is the implementation of the beta server.) However, only time will tell if we've taken the right course. I can promise that we're going to continue working out our processes until we get it right.

So I'm not going to tell you "Everything's fine" and "Nothing's broken" -- I've had enough egg on my face to eat a steady diet of omelets for the past couple months. We did, however, get items like the new player interface and the new tutorials into ***Magic** Online.* Since we're trying to improve the new-player experience, we're pretty happy that those items are up and running -- even if it took longer than anybody expected.

On behalf of the team, I apologize for ***Magic** Online* going south for such an extended period of time. It's been a rough ride for both new and old players, and we're only too happy to walk away with the lessons learned and put the experience behind us. We hope that the [upcoming shindig](/en/articles/uncategorised/2003/10-08-update-chucks-virtual-party) will appropriately express our thanks for the trouble.

Thanks for playing. I'll see you online.

Dan