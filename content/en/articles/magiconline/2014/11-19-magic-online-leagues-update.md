---
id: q3w2yt54
kind: article
lang: en
path: /en/articles/magiconline/2014/11-19-magic-online-leagues-update
title: Magic Online Leagues Update
published: '2014-11-19'
column_slug: magiconline
column: Magic Online
authors: []
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
    lang_detected: en
    capture_id: 104976
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
    captured_at: '2016-04-25 09:29:01+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
    lang_detected: en
    capture_id: 104976
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
    captured_at: '2016-04-25 09:29:01+00'
    rule: drupal.posted_in_date
sources:
- document_id: q3w2yt54
  url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
  page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
  lang: en
  template: drupal
  captured_at: '2016-04-25 09:29:01+00'
  capture_id: 104976
  wayback_url: https://web.archive.org/web/20160425092901id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
- document_id: q3w2yt54
  url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19
  page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19
  lang: en
  template: drupal
  captured_at: '2014-12-02 06:47:24+00'
  capture_id: 104938
  wayback_url: https://web.archive.org/web/20141202064724id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: q3w2yt54
  capture_id: 104976
  url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
  wayback_url: https://web.archive.org/web/20160425092901id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2
  captured_at: '2016-04-25 09:29:01+00'
  template: drupal
  sha256: 0efbc49d6b76c320778894e8372263fe27de41038694d3c1ce0a9bea551ea04e
render_recovery: []
---
Greetings *Magic Online* Players,

Earlier this year [I announced our plan to release Leagues](/en/articles/feature/2014/07-16-magic-online-new-beginnings) before the end of 2014. As the team finishes up development, we've found that we'll need more time to ensure that we are shipping at the quality our players expect and deserve and will not be deploying Leagues this year. Today, I want to discuss what is taking longer than expected, when we plan to deliver, and what you'll see when Leagues arrive.

When will Leagues Release?

As we expected, the design of the new version of Leagues required several major changes to *Magic Online*. One of these core requirements is to support a large number of players who are all playing in the same League. This change obviously requires extensive testing and refinement. To meet this need, we simply need more time to make sure the Leagues can support the number of players we want and that experience stays consistent under production load.

The good news is that Leagues will deploy to our Closed Beta in December. We've had Leagues up and running on our internal environments for several months now, and we're excited about getting a group of external players on the system to get their feedback. Beta players should expect an email in their inboxes in a few weeks, and we're still accepting [Closed Beta applications](http://wizards.custhelp.com/app/answers/detail/a_id/2265/kw/closed%20beta) if you want to help out.

If everything goes well over the next couple of months, we're targeting the release of Leagues for the first half of 2015. After our Closed Beta and another few rounds of internal testing, we'll have more information about what our final release date will be.

A Focus on Playing

Leagues have two primary goals: reduce the amount of time it takes for players to participate in competitive *Magic Online* and let players play on their own schedules. To this end, Leagues do not follow the round structure of other tournaments. Instead, when you are ready to battle in your League, you'll just click the Play Next Game button and we'll match you with your next opponent right away. For this paradigm to work, however, we need to make sure we're finding player matches quickly, so we're leveraging the size of our player population to facilitate faster matchmaking. Let's look more closely at what we are doing.

![](http://media.wizards.com/2015/mtgo/11-19-2014_img_1.Jpg)

[Roar of Challenge](https://web.archive.org/web/20141119000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Roar+of+Challenge) | Art by [Viktor Titov](https://web.archive.org/web/20141119000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&artist=%5B%22Viktor%20Titov%22%5D)

First, we want to expand the pool of League players available at any time by allowing many players to join any given League. Our target is measured in the thousands of players, rather than the hundreds allowed in current events. We want to minimize the number of Leagues overall and get all of the players looking for a similar League experience together in one place, such as a single *Khans of Tarkir* League, which lets you play when you want to play. The more players available, the shorter each player will have to wait for a match, regardless of what time of day he or she is looking.

The League structure has also been designed to ensure players are always looking for meaningful matches. League players have a total number of matches that can be played rather than being bound to a set number of matches per week. This lets players play as many of their matches as they like in any time frame they like. Though we will have some player groupings in each League to pair players for matches as evenly as possible (look for details in a future article), the larger population of players available should generally make this separation invisible when it is time to find a match.

In addition to using a general match limit instead of a weekly one, there is no concept of tiebreakers. Each match counts towards your record and prizes available will be earned based on your match wins, not your ranking against other players. Once you've finished your matches, you will receive any prizes you've earned and will then be able to rejoin the League and start anew. This ensures that active League players are always looking for meaningful matches and normalizes the decks and opponents players will face.

Putting this all together creates a system where players can participate in a League at any point and not be at a disadvantage. Players can join at any time, play their matches at any pace, and then earn prizes based on how well they perform. Once they have finished all their matches, they can rejoin the same League and do it all again. This allows players who cannot commit to more than one or two matches per week participate in the same League as a player who can play five matches per day. Couple that with a large player base, and you have a system that lets *Magic Online* players tailor their experience in a way that fits into their busy lives.

In Closing

We're excited about the new play opportunities Leagues brings and can't wait to deliver next year. If you would like to help provide feedback and get a sneak peek at Leagues, apply for the [Closed Beta today](http://wizards.custhelp.com/app/answers/detail/a_id/2265/kw/closed%20beta). Not only will you be able to check out Leagues, you'll able to see other features and card sets early and let us know what you think.

In other *Magic Online* news, Legacy Cube starts this week on Wednesday, November 19. [Check out this announcement](/en/articles/magiconline/2014/11-03-the-new-magic-online-legacy-cube) and coverage from our [Legacy Cube preview event](/en/articles/magiconline/2014/11-10-magic-online-stream-event-extravaganza). On December 3, we'll release another major client update that will improve some outstanding performance and stability issues. This winter, both the Holiday Cube and *Vintage Masters* return for a limited engagement, so mark your calendars. And as always, make sure you keep your eyes on [www.MTGO.com](https://web.archive.org/web/20141119000000/http://magic.wizards.com/en/magic-online) for the latest *Magic Online* announcements and updates.

Thanks and have fun.

Chris Kiritz  
 Digital Business Manager  
*Magic: The Gathering*