---
id: 71bgywe9
kind: article
lang: en
path: /en/articles/feature/2004/12-16-vanguard-online
title: Vanguard Online
published: '2004-12-16'
column_slug: feature
column: Feature
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/article121604
    lang_detected: en
    capture_id: 1821657
    url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
    captured_at: '2007-08-07 12:16:52+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/article121604
    lang_detected: en
    capture_id: 1821657
    url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
    captured_at: '2007-08-07 12:16:52+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/article121604
    lang_detected: en
    capture_id: 1821657
    url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
    captured_at: '2007-08-07 12:16:52+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/article121604
    lang_detected: en
    capture_id: 1821657
    url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
    captured_at: '2007-08-07 12:16:52+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: 71bgywe9
  url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
  page_key: wizards.com/default.asp?x=magic/magiconline/article121604
  lang: en
  template: classic_asp
  captured_at: '2007-08-07 12:16:52+00'
  capture_id: 1821657
  wayback_url: https://web.archive.org/web/20070807121652id_/http://www.wizards.com/default.asp?x=magic/magiconline/article121604
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 71bgywe9
  capture_id: 1821657
  url: http://www.wizards.com/default.asp?x=magic/magiconline/article121604
  wayback_url: https://web.archive.org/web/20070807121652id_/http://www.wizards.com/default.asp?x=magic/magiconline/article121604
  captured_at: '2007-08-07 12:16:52+00'
  template: classic_asp
  sha256: 985b11b5bc1e9feff11cd78e3bccd638164fa1b7c76ec82922a652f1a0fdf40c
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Fallen_Angel')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Fallen Angel
  occurrences: 2
---
* * *

We've been really hesitant to talk much about new features for ***Magic** Online* since we can't really do much with the current code. As we've explained before, we're committed to maintaining our release schedule of new card expansions, but all our other development resources are devoted to Version 3. The initial goal for V-3 is to replicate all the existing functionality on a code base that is scalable (so we can handle a lot more users), extensible (meaning we can easily add more functionality), and stable (of course). Meanwhile, we're also taking this opportunity to clean up and improve our user interface since we needed to rewrite that code anyway.

After we successfully launch V-3 (hopefully in the fourth quarter of 2005), then we get to start having all the fun conversations we've been looking forward to about what new features to add to the game (well, other than card sets, of course). Internally, we often refer to “3-A” and “3-B” where “3-B” is where all the new functionality goes. Our list of cool stuff we want to add in version 3-B is really long and keeps growing every day. Eventually, we'll probably start dividing it up into bite-sized chunks and trying to give you guys new features on a somewhat regular basis in 2006 and beyond.

So that's the big picture … and with that disclaimer out of the way, I'm going to share one of our ideas with you: There's no ETA yet, but there is a general consensus inside Wizards of the Coast that we definitely want to add *[Vanguard](https://web.archive.org/web/20070826053054/http://www.wizards.com/default.asp?x=magic/products/vanguard)* functionality to ***Magic** Online* at some point.

*Vanguard* will be a special format and if you choose to play a game using the Vanguard format, then whatever avatar you're using to represent you will give you special powers inside the game. Every avatar in the game will have a unique set of *Vanguard* powers (and you have to own the avatar to be able to use it for a *Vanguard* game). Specifically, each one modifies your starting life total and your opening hand size as well as giving you a special ability.

![](https://i.ormos.uk/26/b8/26b891a79dc4798e96d748d5b2dd649612089d72055073bc01ff1849557d1681.jpg)So, for example, if you happen to own a Fallen Angel avatar (maybe because you won it in one of [our special Holiday Events](/en/articles/feature/2004/12-14-christmas-holiday-events) \*hint, hint\*) and you're using it to play a *Vanguard* game, then when you start the game, a special Vanguard window will pop up and show you what effects your avatar has on the game. R&D has been working on *Vanguard* for a little while now and our current version of Fallen Angel says “Whenever a creature goes to your graveyard from play, target opponent loses 1 life and you gain 1 life.” When playing Fallen Angel, you still start the game with the normal 7 cards, but your opening life total is 15 (instead of 20). Things are still subject to change at this point, but hopefully this gives you a sense of the way *Vanguard* works.

We think this format will be an awesome new addition to ***Magic** Online's* casual constructed rooms and there's actually an outside chance we could get this functionality before V-3 comes out. Because our card programmers are getting better and better every set, they may actually “get ahead” of our card set release schedule and have some time to devote to new formats like *Vanguard*. For example, they actually finished coding the last card in *Betrayers of Kamigawa* last week, fully six weeks before the set's Beta test can begin. Anyone who has participated in our previous Beta tests for new card sets knows that we're sometimes racing to get all the cards coded before the paper prerelease, which is when the set goes public and our MTGO Beta testing can begin. This time around we'll actually have plenty of time for internal Alpha testing and the set should be in great shape by the time any of you see it. 2005 does have four releases (*Betrayers*, *Saviors*, *Ninth Edition*, and *Ravnica*) but if things continue to go well maybe we'll be able to sneak out *Vanguard* sooner rather than later.