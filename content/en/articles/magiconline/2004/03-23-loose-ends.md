---
id: 9v78hdd6
kind: article
lang: en
path: /en/articles/magiconline/2004/03-23-loose-ends
title: Loose Ends
published: '2004-03-23'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm7
    lang_detected: en
    capture_id: 1950446
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
    captured_at: '2005-05-05 06:13:18+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm7
    lang_detected: en
    capture_id: 1950446
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
    captured_at: '2005-05-05 06:13:18+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm7
    lang_detected: en
    capture_id: 1950446
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
    captured_at: '2005-05-05 06:13:18+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm7
    lang_detected: en
    capture_id: 1950446
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
    captured_at: '2005-05-05 06:13:18+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: 9v78hdd6
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm7
  lang: en
  template: classic_asp
  captured_at: '2005-05-05 06:13:18+00'
  capture_id: 1950446
  wayback_url: https://web.archive.org/web/20050505061318id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9v78hdd6
  capture_id: 1950446
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
  wayback_url: https://web.archive.org/web/20050505061318id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm7,,pt
  captured_at: '2005-05-05 06:13:18+00'
  template: classic_asp
  sha256: 4a2cc0a8d3b197c9a0ab356e64b2f76ae7125e76544087dad4220e72649b45e5
render_recovery: []
---
* * *

### Updates

First, I'd like to apologize for the length of yesterday's downtime. The system wasn't able to bounce as it usually does and it wouldn't reset remotely. The delay was due to one of our techs having to go to the server farm and take care of it manually. I don't have any more information on what caused the deadlock yet. I also need to go over the notification system, as we didn't get any word out to you about what was going on. I'll see what I can do about both items in the coming week.

A couple big issues will be taken care of with this Thursday's update. One is that we'll be updating ***Magic** Online* with a fix for the text change bug that crashes games. The other is that redemption will be available after the system comes back up.

### What To Write About?

When the ***Magic** Online* team originally approached me about acting as communication manager and player advocate for the game, things were much different. The game was as stable as it was likely to get and part of the team had embarked on the full redesign. We'd hoped to give players an insider's view of the game along with some information and updates. I'd also voice player concerns to the team and get them addressed.

The problems with the *Darksteel* release changed everything. The status quo of weekly articles wasn't enough to communicate what was going on, so the information flow was opened wide and you saw a lot of me on the boards and on the site. Then, as things settled down, the amount of information also decreased. As some of you pointed out on the boards, I didn't have anything left that you hadn't already heard.

With redemption being turned back on and the text change bug being fixed, that makes the next big issue leagues. Since we began restoring functionality, we've actually been more stable than we've been in quite some time. However, we don't have leagues or premier events running.

Premier events were taken down last fall due to a bug that crashed the system. And, as we've seen recently, release leagues seem to cause the same problem. So, why not turn regular leagues back on?

![](https://i.ormos.uk/46/bb/46bb0c418161114d0d68a37edeb5957cd83590a5152602b917475ec13535d370.jpg)

As it turns out, the premier events and leagues share a common bug—one that kills the server. We haven't tracked the bug down, but we've seen evidence that it is a single bug. There's a table that both leagues and premier events write to and we've found the same corrupted data coming from both types of events. It's evidently the frequency of the data being written that exacerbates the bug.

Therefore, when regular leagues are running, we don't see crashes *as often* as when we launch release leagues. However, the bug is still affecting the system and causing some stability issues. While we want leagues up and running again, server stability is always the priority. So, leagues are down as the dev team hunts down this bug.

Which, of course, begs the question: Why weren't they hunting the bug down before?

It was towards the end of last year that the ***Magic** Online* team decided on the strategy of keeping the current game alive while part of the team went off to rebuild it from scratch. There was no way to retrofit the kind of architecture changes the game needs, as we learned during the Version 2.0 launch.

When we brought in extra help early this year, we set a portion of the team aside to see what they could do about cleaning up the Version 2.0 code. This effectively created three teams: 

*   One team was reworking the game from the ground up. They don't make any changes to the live game at all.
*   One team was responsible for keeping ***Magic** Online* alive. They make some minor bug fixes and monitor the system, but don't do extensive changes to the game.
*   One team was working in the background making extensive changes to the live server code—just not on the live server. Basically, they were finding broken things and fixing them to see what kind of progress they could make.

None of these teams were specifically tasked with fixing the premier events/leagues bug. However, we had hoped that the last team might clean up the code enough that finding this bug would be possible. When we had problems at *Darksteel* release, the last two groups basically became one team. Until that time, we hadn't realized leagues and premier events were experiencing *exactly* the same problem.

The code on the live server now isn't a new version of ***Magic** Online*, it's a cleaned up version of the 2.0 code. And now we have everyone from the last two teams working on fixing leagues and premier events. 

### Compensation

There are evidently some lingering questions about compensation for players in non-release leagues that ended during the crash. The announcement was correct when it said players get one booster pack per week the league ran. That means if you were in the first week of a league, you'll get a booster. If you were in the fourth week of a league, you'll get four. **[Check the original announcement for full details](/en/articles/feature/2004/03-11-continuing-coverage-event-and-league-compensation)**.

We also realize that the entire community was inconvenienced by the crashes—whether you were in an event or not. We've had some discussion about what we'd like to give everyone for the problems caused by the *Darksteel* release leagues. We aren't going to be ready to make any announcements until we're back to where we were before *Darksteel* release. Once we reach that point, we'll be better able to see what reasonable compensation is for sticking with us through this.

You can take two things away from that statement, however. First, we *are* planning on compensating everyone for the interruption to normal play. Second is that we *will* be restoring leagues to ***Magic** Online*. It's not a question of “if”, just a question of “when”. Hopefully that'll be sooner rather than later, but I'm not making any bets until I hear that league code is ready for beta testing.

In the meantime, keep posting your questions to the boards. Whether or not you get immediate answers from me, I am taking your concerns to the team.