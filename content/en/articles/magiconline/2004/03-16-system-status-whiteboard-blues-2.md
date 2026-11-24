---
id: p18jm080
kind: article
lang: en
path: /en/articles/magiconline/2004/03-16-system-status-whiteboard-blues-2
title: 'System Status: Whiteboard Blues'
published: '2004-03-16'
column_slug: magiconline
column: Magic Online
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm6
    lang_detected: en
    capture_id: 1950362
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
    captured_at: '2004-08-13 12:12:05+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm6
    lang_detected: en
    capture_id: 1950362
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
    captured_at: '2004-08-13 12:12:05+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm6
    lang_detected: en
    capture_id: 1950362
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
    captured_at: '2004-08-13 12:12:05+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/dm6
    lang_detected: en
    capture_id: 1950362
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
    captured_at: '2004-08-13 12:12:05+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: p18jm080
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
  page_key: wizards.com/default.asp?x=mtgcom/daily/dm6
  lang: en
  template: classic_asp
  captured_at: '2004-08-13 12:12:05+00'
  capture_id: 1950362
  wayback_url: https://web.archive.org/web/20040813121205id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: p18jm080
  capture_id: 1950362
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
  wayback_url: https://web.archive.org/web/20040813121205id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dm6
  captured_at: '2004-08-13 12:12:05+00'
  template: classic_asp
  sha256: 579c3e74063278387637f2376dc5c8cbddc2aead7c4eed650fdaacf3dad366e7
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:autoCardWindow2('Fatespinner','/global/images/magic/general/Fatespinner.jpg')
  reason: The archived link runs JavaScript. The preview kept its text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Fatespinner')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Fatespinner
  occurrences: 9
- code: unsupported_link
  element: a
  target: mailto:techsupport@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - techsupport@wizards.com
  occurrences: 1
---
### Where we go from here

*On a whiteboard…  
 With black curtains…  
 Near the dev team.*

Whoops, back up there. No curtains. Anyway…

On this whiteboard is a list of how we want to turn things back on in ***Magic** Online*. It's the plan the team came up with at the beginning of last week when we were trying to recover from the problems we encountered during *Darksteel* release. At each step, we said we'd wait and see how things were running for a period of time before continuing.

Well, it's been a long week of false starts, mostly. We keep coming upon roadblocks as we try to progress. On the negative side, that means functionality is returning much more slowly than anyone wants. On the positive side, it means we have a much more narrow range of possible causes when we do hit a problem. All in all, we think the second part is more important than the first.

There's a lot on the list, as we tried to break things down into bite-size chunks. It includes everything we already had on the 2.0 server and runs through bringing back **Premier Events**. Frankly, I shudder when I think about trying them, although we had some success on the beta server with small **Premier Events** running all the way through. However, that's far down the line from where we are today.

While I've tried to communicate clearly what is going on, there are still some outstanding issues. Let me try to fill in the gaps.

### Pointing The Finger

<table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Fatespinner" src="https://i.ormos.uk/e2/ad/e2ad44cbe6663c5cecf1d27f09af82948cc05b13f67262234b57fd3ef7780feb.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table>

No, not that finger. Some players took offense at my statement that we pulled queues on Sunday “due to players abusing a bug with the *Mirrodin* card Fatespinner.” I apologize for that wording. Yes, the bug with Fatespinner is our fault, not the community's. My point was that players were deliberately using the bugged card to win games and that it was unfair to other players—both those who didn't know about the Fatespinner bug and those who chose not to play it.

For those that aren't aware, what the Fatespinner bug did was essentially ignore your opponent's choices when the ability triggered. The buttons would appear, but clicking them didn't allow the game to proceed. Instead, the game sat there waiting as if your opponent hadn't done anything. Your opponent's timer would continue ticking down and the only thing he or she could do at that point was concede or time out.

If you lost a sanctioned game—draft or Constructed—due to the Fatespinner bug, please email Customer Service (techsupport@wizards.com). Include that you're writing in because you lost to Fatespinner, the game number it happened in, and whether it was a draft or Constructed queue game and we'll refund you the cost of entering the queue. I'm sorry that we allowed this bug to continue affecting games as long as we did. Had we acted faster, we certainly could've mitigated the problems Fatespinner caused.

Looking back on this weekend, it would've been better to ban Fatespinner before bringing the queues back up. At least we could've banned it instead of bringing queues down completely. We still have issues to iron out about handling card bugs while they're in the game.

Part of the pain from the Fatespinner bug is, as some of you pointed out, we had already gotten it working on ***Magic** Online*. One of the unfortunate problems that occurred when we moved the beta server code to the live server is we lost some of the bug fixes we'd already put in. Fortunately, for things like the *Darksteel* set, we can batch upload them to the server and be done. It's just the single bugs like this or the text change bugs that creep back to bite us when we're not looking.

In the end, the dev team was able to patch it on Monday. Along with the *Darksteel* patches, we were able to put the queues back up and add *Darksteel* to the draft queues. We delayed adding *Darksteel* cards to Constructed until March 22, 2004 since we want to make sure everyone has time to get the cards they want for their decks.

### Triple-D Drafts

<table><tbody><tr><td><img src="https://i.ormos.uk/35/ba/35ba4ad2d8422f0dfde2305adeb20af143014b860616850ab10be7d2e55440b8.jpg"><br><i>The way we want it to be...</i></td>&#10;</tr>&#10;</tbody></table>

I keep seeing people asking if we're going to bring back triple-*Darksteel* drafts. There are only three times it's normal to be drafting three packs of the same kind. First is in the Core Set draft queues (*Eighth Edition*). Second is when the big set of the block is the only one released so far (*Mirrodin*). Third is during release events.

While we're still planning on holding *Darksteel* release events, now is certainly not the time to decide when those will be. Once we've got some more items up and running that are on our list we'll start talking about when to hold events and what they will be. At the moment, we don't even have leagues restored yet. Planning for new release events would be getting ahead of ourselves.

### Other Stuff

Here's a quick note for anyone who's been waiting to get on our free trial server. Unfortunately, right now all our efforts are dedicated to restoring functionality to the live ***Magic** Online* server. Until we've got things at least back to where we were before the original *Darksteel* launch, we won't be able to put any fixes on the free trial server. I'll make sure to get an announcement out when we've had a chance to update the free trial server.

Finally, I'd like to wrap up on a positive note. The ***Magic** Online* Team would like to thank Nushae and Zinger314 for all their help on the Imprint bug. While neither were able to point to the exact cause of the bug, their work was instrumental in the dev team finding it. Thanks for the effort!

Thanks to everyone for your patience. Sorry it's taking so long, but we are making progress. Every time I see a nice smooth curve on the usage graphs, it makes my heart skip a beat.

I'm sure I didn't catch everything, and I'll get together more answers for next week's column. In the meantime, keep an eye on the Announcements folder for the latest on what's happening with ***Magic** Online*.