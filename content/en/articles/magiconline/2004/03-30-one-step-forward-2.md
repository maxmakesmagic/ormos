---
id: z067fb09
kind: article
lang: en
path: /en/articles/magiconline/2004/03-30-one-step-forward-2
title: One Step Forward
published: '2004-03-30'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm8
    lang_detected: en
    capture_id: 1950484
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
    captured_at: '2005-04-19 05:46:27+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm8
    lang_detected: en
    capture_id: 1950484
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
    captured_at: '2005-04-19 05:46:27+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm8
    lang_detected: en
    capture_id: 1950484
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
    captured_at: '2005-04-19 05:46:27+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm8
    lang_detected: en
    capture_id: 1950484
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
    captured_at: '2005-04-19 05:46:27+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: z067fb09
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm8
  lang: en
  template: classic_asp
  captured_at: '2005-04-19 05:46:27+00'
  capture_id: 1950484
  wayback_url: https://web.archive.org/web/20050419054627id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: z067fb09
  capture_id: 1950484
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
  wayback_url: https://web.archive.org/web/20050419054627id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm8,,fr
  captured_at: '2005-04-19 05:46:27+00'
  template: classic_asp
  sha256: fd62b72d6731fbaeaf8ca69605b083ff40d9228e0893422a3d3ada3368ed8a7a
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Alter_Reality')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Alter Reality
  occurrences: 2
---
* * *

### Eating Oatmeal With A Fork

It's a weird analogy, but reporting on ***Magic** Online* is like eating oatmeal with a fork. While it seems we're making progress, bits keep slipping through the tines and we end up almost back where we started. And, if visible progress is sometimes hard to see working here, it's sometimes completely lost on the outside. Even as I'm stepping up to the plate to deliver some good news, little niggly bits keep coming up.

<table><tbody><tr><td><table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Alter Reality" src="https://i.ormos.uk/58/46/5846fd66236e950cc84e7266a7d662b2c398ad33056b73574a0e2a31683783c3.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table><br><i>Fixed, but overshadowed.</i></td>&#10;</tr>&#10;</tbody></table>

For example, in last week's update, we uploaded a fix for the text-change bug. For anyone who wasn't aware of this, there was a bug that caused games to crash if a card was played that changed the text of another card (ex: Alter Reality). This bug was a major problem for sanctioned games, as a player in a losing position could crash a game and turn it into a draw.

However, after the initial reboot, some old settings got reset in the client code. Suddenly, the **1700 Room** went back to 1800 and the **Casual Trade** room also reappeared. These aren't items we've been spending development time on. It was a simple error that, well, makes us look pretty dumb. The server got reset and everything went back to normal.

And so one less visible, important fix gets overshadowed by a very visible error.

Another piece of news I had for today is that we've had some meetings to decide what to do as a permanent fix to the abuse of the **1700 Room** Constructed queue. For clarification, some groups of players (or single players with multiple accounts) were filling Constructed queues together and conceding quickly to get prizes. Since these tournaments often last somewhere on the order of 5 to 10 minutes, it's obvious that the players' sole intent was to stack the queue and get the prizes without playing. This falls under the category of manipulating the system to alter the outcome of a tournament and is a violation of the ***Magic** Online*[Code of Conduct](/en/articles/uncategorised/2003/12-15-magic-the-gathering-online)(end link).

![](https://i.ormos.uk/4a/de/4adefd414c47ef4101336a8999bdcd9c021e161dd0ad4efeaa5d962f553f4262.jpg)Some of these accounts have been suspended already and the team is continuing to look into abuse cases. However, we also realize that this is only a temporary fix to the problem. I'll get to what we're going to do in a minute, but we've been aware of this problem and have been looking for a solution.

We'd planned on turning off the **1700 Room** Constructed queues until we could implement some changes. Well, they got turned off, all right. Then someone, thinking the queues failed to come up properly after last week's update, set up the queues again. Even more unfortunate, they were set up for one less ticket than they were supposed to be and got abused again over the weekend.

So, even before I can tell everyone about the changes we're going to implement this week, we get some more egg on our faces.

And, many of you have asked, why wasn't redemption turned back on? It was an oversight during last week's update and *will* be turned on this Thursday.

It's unfortunately par for the course that these issues crop up at the most unfortunate of times. I usually just roll with them, but it gets frustrating trying to impart good news only to be interrupted having to explain other things.

### Rant Off, Constructed On

There are two subjects I really wanted to talk about today. The first is what we'd like to do with the Constructed queues. I'm not sure how you're going to receive them (and I'm sure we'll hear on the boards), but we think we can reduce players trying to abuse the system while giving some value to everyone at the same time.

In the **1700 Room**, we're going to bump the cost of entry on the Constructed queue to 7 tickets. We figure that should discourage players from manipulating the system while still making it worthwhile to try to win in the queues.

We're also going to bump entry cost to the regular Constructed queues from 5 to 6 tickets. However, we're also going to increase the prize payout by 2 packs. Constructed queues in the **Sanctioned Tournaments** room will pay out 5 packs for first place, 4 for second, and 2 for third and fourth.

Because we have to code new costs and payouts for this, the changes will be delayed a bit. This is because we're freezing most code changes while we test the big ones.

### One Bug In The Hand

Last week, the dev team was able to reproduce both the initial and cyclical crashes that have plagued events since the Version 2.0 launch. A bug in the league and premier events code causes a stack overflow, which is why the first symptom we found was the bad data in a shared table. During the internal testing, we were able to run leagues and tournaments without crashing and, when the system was deliberately crashed, everything restored correctly.

On Monday, we began a small closed beta test of the new leagues and premier events code. The beta testers and dev team will be pounding on the code as much as they can to see if they can break the patch.

The next step will be a large beta to test leagues and tournaments. I don't have any details yet, but if things go well this week, we'll be opening things up soon to see if we've finally nailed it.

![](https://i.ormos.uk/f5/a8/f5a832a7b567e16d2713ee0b317131022cad5b81aefb66007306bbc26ef1e3b4.jpg)In the meantime, a lot of items we already have fixes for will have to wait to be tested. With continued stability on ***Magic** Online* our focus is getting leagues back up. Hopefully, this will also reopen the **Premier Events** room, but we'll see. Since little tweaks sometimes cause unexpected problems, we're going to see if we can get the leagues and tournament fix in first, then test the fixes for other bugs later.

Keep your fingers crossed and eyes on the Announcement folder. I'll post details there as soon as I have them (end of this week hopefully).

### Two In The Bush

As I said, we're aware of many bugs in ***Magic** Online* that the community wants fixed (**My Games**, offline messaging, etc.). Since it's going to be a bit before we post fixes to those bugs, I'll try and get a comprehensive list of what you can expect after we're done with league and premier event testing. From the sound of it, the other fixes are only waiting for some testing before they'll be ready to go.

I want to thank everyone I chatted with on Friday night for the good time I had. Even though I didn't get to play much, it was nice to just hang with y'all. Sometimes, when I'm trying to eat oatmeal with a fork, it's good to remember why I continue to do this job. Thanks for reminding me.

See you online.

\- Dan Myers