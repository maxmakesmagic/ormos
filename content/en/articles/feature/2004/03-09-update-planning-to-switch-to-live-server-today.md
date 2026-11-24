---
id: g8w0nvsb
kind: article
lang: en
path: /en/articles/feature/2004/03-09-update-planning-to-switch-to-live-server-today
title: 'UPDATE: Planning To Switch To Live Server Today'
published: '2004-03-09'
column_slug: feature
column: Feature
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/news030904b
    lang_detected: en
    capture_id: 1829973
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
    captured_at: '2004-09-06 05:40:49+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/news030904b
    lang_detected: en
    capture_id: 1829973
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
    captured_at: '2004-09-06 05:40:49+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/news030904b
    lang_detected: en
    capture_id: 1829973
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
    captured_at: '2004-09-06 05:40:49+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/news030904b
    lang_detected: en
    capture_id: 1829973
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
    captured_at: '2004-09-06 05:40:49+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: g8w0nvsb
  url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
  page_key: wizards.com/default.asp?x=magic/magiconline/news030904b
  lang: en
  template: classic_asp
  captured_at: '2004-09-06 05:40:49+00'
  capture_id: 1829973
  wayback_url: https://web.archive.org/web/20040906054049id_/http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: g8w0nvsb
  capture_id: 1829973
  url: http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
  wayback_url: https://web.archive.org/web/20040906054049id_/http://www.wizards.com/default.asp?x=magic/magiconline/news030904b,,pt
  captured_at: '2004-09-06 05:40:49+00'
  template: classic_asp
  sha256: 5a196dc6ff77640f7250269ca094116465150ba69a38fdee4c3d64c8f6f8aef0
render_recovery: []
---
* * *

The short version of what's going on: While the timeline has changed, most of the details haven't. We'll be moving back over to the live server today with the code currently on the beta servers. There will be a downtime of at least an hour as we do the switch.

As any of you who took the thirty seconds to read this week's column know, I'm pretty pessimistic about the messages coming out of the dev team. What seemed like a solid plan yesterday morning was revised within a half hour of my posting it. By the end of the day, it seemed to have been thrown out the window.

I'll be "cautiously optimistic" about the current plan for a couple reasons. First, the plan has only changed slightly and that's mostly just the timing. Second, we "found" the reason for the instability in the live server last Thursday. While that it took us until yesterday to figure that out doesn't make me terribly positive about the situation, at least the plan to go ahead sounds workable.

What was the problem? The same corrupt data issue that caused the crashes during *Mirrodin* release leagues. We've never found the root cause of these crashes, but we know how to resolve the current problem--we have to remove the corrupt league. Fortunately, the number of *Darksteel* release leagues is small enough that there's a good chance we only have to kill a single one rather than all that were running when we went down last week. There's also a small chance we won't have to remove any at all--small, but it's there. And, of course, there *is* a chance we'll have to remove all of them.

So, with slight modifications to the old plan, here's how we're going forward.

Later today (Tuesday, March 9), we'll be bringing down the beta server. ***Magic** Online* will be down for at least an hour afterwards as we move everything over to the live server. On the initial restart, we'll leave the running *Darksteel* leagues in place. If the modified beta code resolves this problem, all well and good. Given that small chance doesn't come through, we bounce the servers, [**temporarily remove all the leagues**](#leagues), then bring the live server back up.

**Note:** You'll have to close and restart ***Magic** Online* in order to connect to the live server. If you've pointed your shortcut to **magic1.exe** *your client will not update correctly.* You *must* launch **magic.exe** in order to update your client.

After this downtime, we'll come back up on the live server, which means you'll see your actual collections. Initially, no one on the system will be able to trade cards. We'll wait to make sure ***Magic** Online* is performing well before we allow trades on the system.

> This is important, so I'll say it again: We'll be bringing the live ***Magic** Online* server back up today after a planned downtime of at least an hour. When we come back up, you'll have your *real* collection available. As this will be the live server, anything you do with those cards is permanent.

When we first come up, we'll be in "no-pay" mode, which means you won't be able to join any events. Since there won't be any leagues, queues, or tournaments spawning anyway, this shouldn't be a problem. There's no current information on when we'll start putting events back into the system. I'll tell you when I know more.

The developers will continue to hunt for bugs that need fixing during this time. If the system comes down on it's own, they'll probably keep it down until they have a fix ready for any errors they found. It's also likely that they'll have some more updates ready each day, so we may have planned downtimes to prop the code after they've tested it. Again, I'll make sure we get word out before the dev team brings the game down for any updates.

I'm not sure when the next status meeting will take place. It could be late this afternoon, tomorrow morning, or an hour after we come up. It all depends on how ***Magic** Online* behaves after we bring it back up. I'll let you know when these meetings happen and what comes out of them. At the very least, I'll let you know how things stand this afternoon.

The second step will be turning trading back on. Again, we want ***Magic** Online* stable before we allow transactions in the game. It may be days before we deem the game stable enough to allow trading again, we don't know right now. We'll let you know when it happens.

The third step will be to turn queues back on, followed by reopening the ***Magic** Online* Store. Obviously, it doesn't make sense to have queues available if you can't get product, so these two items are closely related.

The next milestone we'll be waiting for is to see if the queues are completing and ***Magic** Online* is still stable. Sometime after we hit that mark, we'll turn the leagues back on. Again, we haven't decided yet what we're going to do about the *Darksteel* release leagues, but I'll have more information after we know how well the game is doing.

In short, here's what's happening: 

*   We'll be switching over to the live server today.  
  

*   Initially, we'll bring the server up with running leagues in place (no new ones spawning). However, there's only a small chance that the beta code will fix the crash problem. If it doesn't, the game will bounce, [**we'll remove the leagues**](#leagues), then bring the game back up.  
  

*   When the live server comes up, we'll be in no-pay mode until further notice.  
  

*   No trades will be allowed until further notice. This will be the first item we'll decide to turn on, so the game may be up for quite a while before this changes.  
  

*   The first events we'll bring back up are the queues. Shortly thereafter, the ***Magic** Online* Store will reopen.  
  

*   If the queues are completing and the game is still stable, we'll bring leagues back up.  
  

*   During this time, if things are going well, we'll decide how to continue *Darksteel* release events. Along with this, we'll decide what to do about any leagues that had to be removed from the game and ones that are shortened by the downtime.

Keep an eye on the [Announcements folder](https://web.archive.org/web/20040309000000/http://boards1.wizards.com/forumdisplay.php?s=&forumid=217) for more information, including when we'll be doing the switch to the live servers this afternoon.

There is no definite timeline because the entire plan is dependant on performance of the master server. Several times I've posted what was going on only to have to modify those statements later. I'd rather give you a plan with no timeline than to promise again what we fail to deliver.

I'll continue bringing you information as it occurs, or at least an occasional statement that there's nothing new. Better to hear things are status quo than to hear nothing at all.

***Leagues***

Yes, we'll remove *all* the leagues initially. However, we're saving all the data to give us the chance to find the one (or more) that became corrupted. If we find the corruption, we can remove only the league (or leagues) we have to before putting them back on the server.

**Note:** We won't have any information about the leagues that were running for a while. We'll post information once we have it, but don't expect it immediately after we come back up.

We don't have any specific plans right now for the continuation of *Darksteel* release events. Once we are stable, we *might* be able to extend the time on the currently running leagues. If we can't, there will be a contingency plan in place. Again, I have no details because right now everything is focused solely on getting the live server back up and stable.

What I can say is that we certainly want to continue *Darksteel* release events and we don't want those players who were able to join release leagues last week to feel cheated due to the downtime. We'll keep this in mind when we have a chance to sit down and figure out how to go forward.

You probably are getting as sick of hearing this as I am of saying it, but it has to be said: I'm sorry for the continued problems with ***Magic** Online.*

Thanks again for your patience.  
 Dan