---
id: 0a0j3t4c
kind: article
lang: en
path: /en/articles/magiconline/2004/04-13-success-criteria
title: Success Criteria
published: '2004-04-13'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm10
    lang_detected: en
    capture_id: 1950033
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
    captured_at: '2005-03-02 20:05:35+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm10
    lang_detected: en
    capture_id: 1950033
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
    captured_at: '2005-03-02 20:05:35+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm10
    lang_detected: en
    capture_id: 1950033
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
    captured_at: '2005-03-02 20:05:35+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm10
    lang_detected: en
    capture_id: 1950033
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
    captured_at: '2005-03-02 20:05:35+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: 0a0j3t4c
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm10
  lang: en
  template: classic_asp
  captured_at: '2005-03-02 20:05:35+00'
  capture_id: 1950033
  wayback_url: https://web.archive.org/web/20050302200535id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0a0j3t4c
  capture_id: 1950033
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
  wayback_url: https://web.archive.org/web/20050302200535id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm10
  captured_at: '2005-03-02 20:05:35+00'
  template: classic_asp
  sha256: 65d66dd7cc94a08bb4806099a585a773a08b6cf412d78d97142d8fd636369169
render_recovery: []
---
* * *

### Updates

Last Thursday we moved new code over from the test server to the live server. Along with the new league code, we put in bug fixes that had been waiting for testing to finish. I'm still working on getting a comprehensive list of fixes from the dev team, and will post it as soon as I can. However, one fix that did go in was for the changing avatars bug . Now that we've got that working, we're hoping to get the avatars out to players who got into the *Darksteel* release leagues that crashed. It sounds like we'll be getting those out sometime this week and I'll get a note up when it happens.

We've encountered two major bugs since bringing the live server back up on Thursday. As reported by Randy, we began receiving reports Thursday afternoon that some players' cards were disappearing. Specifically, cards that had been opened after the update were gone from players' collections after they logged off and back on again. As it turned out, the cards were in memory but not being written to the card database.

*This bug only affected cards that had been opened between when we came up (around 2:00 PM) and 4:30 PM Pacific Daylight Time on Thursday, April 8.* The bug didn't affect cards already in players' collections and didn't affect any cards opened after we bounced the game at 4:30 PM. We sent out compensation and refunds on Friday for anyone affected by this bug. (Details can be found [here](https://web.archive.org/web/20040413000000/http://boards1.wizards.com/showthread.php?s=&threadid=217284).

The second bug appeared Saturday afternoon. ***Magic** Online* encountered a deadlock and wasn't able to bring itself back up. It took the developers about seven hours to finally nail down the bug and fix it. The system has been stable since that fix went in late Saturday night.

Most of the compensation has gone out by now. Last Friday, we sent out compensation for the queues that were lost during *Darksteel* release events along with compensation for Thursday's bug. That leaves us with figuring out what, exactly, general compensation should be and giving out product won during last week's testing.

We should be taking care of beta compensation this week, but I don't have a firm date. And some of the team would like to see leagues up for a while before we decide to give out general compensation. It seems like getting back to that state is a good marker for saying we've finally gotten out of these particular woods. However, it's already been a month since this whole thing started, and we'd like to take care of that soon.

### Success Criteria

Last week I told you we declared the testing a success. Given the performance issues everyone saw, it's not surprising that people are wondering exactly what was successful about it. In fact, some of the ***Magic** Online* Team was wondering the same thing when the dev team said it went well.

Our programmers' goal was to crash the game and come back up without losing data in leagues and tournaments. By that definition, the testing went extremely well. We were able to crash the game repeatedly without problems restoring leagues and tournaments.

So, if the non-programmers on the ***Magic** Online* Team looked askance at the dev team when they said the testing was a success, why did we put up the code?

When it comes to performance issues, much of the problem is that our test server just doesn't have the same horsepower as the live server. Since we haven't been particularly happy with the results of the last couple times we load-tested the system on that rig, we're working on using a different setup. (If that solution works out, we'll also be able to run testing in parallel with the live server. No more shifting everyone back and forth.)

And, as I mentioned above, we had a lot of long-expected bug fixes in the code on the test server. Since they were part of the test code everyone was playing on last week, we could push those fixes out with that update. The fixes hadn't been tested on the old code yet, so we hoped to avoid a longer delay in getting them out to you.

Even given those issues, we still put off switching on the live server Thursday as the team discussed which version to put up. Did we make the right decision? Some would say “no” considering the bugs we had in the next couple days. Some would say “yes” since those were new bugs and at least we have the tested league code on the live server now.

Both bugs were a pain both for you and us. The question now will have to be finding out if we run smoothly after fixing those two, so we can move on to fixing other things. Time will tell.

### Communication Breakdown

Along the same lines, we had some successes and failures when it came down to communications. A communication failure is when we either don't get information out to the community in a timely manner or if the information we do put out is inaccurate. A success is when we achieve both goals.

In my book, the final goal is to achieve both without having to say a word to anyone—internal or external. I know it's hard to believe, but I have no desire to have to be available 24/7 to make posts to the message boards. So, when the posts are coming from someone else on the team, I'm pretty happy. Heck, I'd be happy if the only time you heard from me was this column or playing ***Magic** Online*.

We tried that process this weekend and it's obvious we've got a way to go before I'm off the virtual leash. We had people in place to make the announcements, but the notification process broke down.

Things worked pretty well on Thursday. Randy began posting as soon as we heard about the bug and continued until the issue was resolved. We were partially successful on Saturday when Linda began posting about the downtime and continued until we were back up again. However, it took way too long to get the information to her so she could pass it on to you. 

The main failure is our ability to get information out in a timely manner when it's not during normal business hours. This is the big issue on my plate, because when the process breaks down, I've got to deal with it. So it's back to the drawing board for me. I'm sorry we're still falling down on this.

### Other Items

![](https://i.ormos.uk/51/91/5191b642b4e48c71fa3f59eaaa3aafa02adb759c44d7b300aeda11a85fa1cbd0.jpg)I know many of you have expressed interest in still having *Darksteel* events, even this late in the game. We were ready to toss the idea, but we've still got some time before *Fifth Dawn* releases online. However, I for one will push not to have them unless we see some solid server time with leagues running. I'm sorry, but given a choice between events or server stability, I want to keep ***Magic** Online* up and running.

After this weekend, the team's a bit gun-shy about starting leagues. We saw leagues working during last week's test, but we also didn't see those two bugs. The dev team, understandably, would like some time to monitor the game. The team will be discussing when to flip the switch and I'll let you know as soon as a decision is made.

While all this other stuff has been going on, the team coding *Fifth Dawn* has been making steady progress. We've had a few issues, but it's otherwise going well and should be on time (online release in July—no specific date yet).

Next week I'm planning on introducing our newest team member (or having him introduce himself). In the meantime, I'll post announcements when we've got answers about outstanding items like compensation and leagues.

Sorry again for the problems this weekend. I'll break out the iron and keep working on straightening the communication out.

See you online.  
 -Dan