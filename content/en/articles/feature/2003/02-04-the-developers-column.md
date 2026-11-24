---
id: 3kqd654d
kind: article
lang: en
path: /en/articles/feature/2003/02-04-the-developers-column
title: The Developers' Column
published: '2003-02-04'
column_slug: feature
column: Feature
authors:
- slug: jesseroberts
  name: Jesse Roberts
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/articlejr020403
    lang_detected: en
    capture_id: 1822836
    url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
    captured_at: '2005-04-04 04:14:58+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/articlejr020403
    lang_detected: en
    capture_id: 1822836
    url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
    captured_at: '2005-04-04 04:14:58+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/articlejr020403
    lang_detected: en
    capture_id: 1822836
    url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
    captured_at: '2005-04-04 04:14:58+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/articlejr020403
    lang_detected: en
    capture_id: 1822836
    url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
    captured_at: '2005-04-04 04:14:58+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: 3kqd654d
  url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
  page_key: wizards.com/default.asp?x=magic/magiconline/articlejr020403
  lang: en
  template: classic_asp
  captured_at: '2005-04-04 04:14:58+00'
  capture_id: 1822836
  wayback_url: https://web.archive.org/web/20050404041458id_/http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3kqd654d
  capture_id: 1822836
  url: http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
  wayback_url: https://web.archive.org/web/20050404041458id_/http://wizards.com/default.asp?x=magic/magiconline/articlejr020403
  captured_at: '2005-04-04 04:14:58+00'
  template: classic_asp
  sha256: 61c60583d63a0b001e9e02f406559e1d4c5481a3a04d87e7392c3174613434c1
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Lowland_Tracker')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Lowland Tracker
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Goblin_Grappler')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Goblin Grappler
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Artificial_Evolution')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Artificial Evolution
  occurrences: 2
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Mistform_Ultimus')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Mistform Ultimus
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Faceless_Butcher')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Faceless Butcher
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Nantuko_Husk')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Nantuko Husk
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Phantom_Nishoba')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Armadillo_Cloak')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Armadillo Cloak
  occurrences: 1
---
### To Bug Or Not To Bug

* * *

Hello again. It's been a little while since we've updated you on what the development team here at Wizards of the Coast is up to, so I thought I'd pop in and introduce myself. My name is Jesse Roberts and I'm the Quality Assurance Manager for ***Magic: The Gathering** Online.*

Quality assurance is a pretty nebulous term, so now is probably a good time to give you a brief summary of what I actually do. In the most general terms, I head up the effort to test the software systems that make up the game we all know and love. This includes testing both technical things like server performance and more abstract things like card interactions. I'm betting that card interactions are, as a whole, more interesting to you than the minutia of software development, so I'll stick to the fun stuff for this article.

Card interaction testing takes place as soon as a new card set is coded and available on the test server. We start coding the cards as soon as the research and development team is willing to hand off a set as relatively stable entity. This gives us two or three months to find as many bugs as we can with the set before it has to go live. Our testing generally focuses first on making sure that new mechanics and abilities work appropriately under generic conditions.

Since identical abilities use mostly identical code, it's fairly safe to say that if the provoke ability on Lowland Tracker works under normal conditions, the same ability on Goblin Grappler will work under the same conditions. In this way, we can validate the basic functionality of a set in less than a day. We simply go through and put each card from the set in play, making sure that all a card's abilities get used at some point. This gives us a basic idea of how the set is doing, but it only finds bugs very early in the development cycle. Bugs that can be found this way are low-hanging fruit--easily found and quickly eliminated.

<table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Artificial Evolution" src="https://i.ormos.uk/63/ed/63eda4eed737350967b4c9e008a5d08fe9b749f4ad6dee1d6ac1631e2973998d.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table>

Then things get trickier. Given the number of cards in the system, we can't possibly test every card's interaction with every other card. (This wouldn't be particularly useful even if we could, since most of the interactions tested in this way wouldn't be particularly interesting or tricky.) Instead, we go through the new set and, using input from the developers, flag cards for in-depth testing that we believe are particularly troublesome. Cards that get flagged generally have complex abilities or a broad range of interactions with other cards. Cards like Artificial Evolution and Mistform Ultimus require a lot of playtesting online to make sure they work under as many conditions as we can dream up.

Thankfully, the number of cards that have unique or complex abilities is small relative to the size of the total set. Our current list of things for intensive testing in the *LegionsTM* set includes all the keyword abilities and fourteen individual cards. This doesn't mean we don't look at other things, it just means that less than ten percent of the cards in the set give me a heart attack when I read the text.

### Bugzilla

Some of you out there are already involved in helping out our testing efforts. The bug database that lives at [http://www.lplizard.com/bugzilla/](https://web.archive.org/web/20030204000000/http://wizards.com/leaving.asp?url=http://www.lplizard.com/bugzilla/&origin=magic_magiconline_articlejr020403) hosts over eighteen thousand bug reports, mostly filed by players who catch the bugs we don't find before they make their way into the live environment. The majority of these have to do with specific cards and their behavior under specific circumstances. Needless to say, this is an invaluable resource. The sheer number of possible card interactions makes it next to impossible for us to check absolutely every combination before card sets are released into the wild. Once thousands of users sink their teeth into a new set, however, we find out what we missed pretty quickly.

Of course, there are a few issues we see over and over again that aren't actually bugs, but misunderstandings. So, for your edification, here are the top three bugs that aren't bugs.

**1\. Faceless Butcher Ate My Homework.**  
 Lot's of people file bugs letting us know that they didn't get their removed creature back when Faceless Butcher leaves the game. While it's definitely a little deflating to see your favorite creature vanish into the ether, it isn't a bug. If your opponent gets rid of Faceless Butcher while its comes into play ability is still on the stack (perhaps by sacrificing it to Nantuko Husk), the leaves play ability resolves first, and doesn't do anything since nothing has been removed yet. The comes into play ability resolves last, and your creature says goodbye till your next game.

<table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Phantom Nishoba" src="https://i.ormos.uk/78/b1/78b127d0629a5c3ad87ac0e5d3224b468e5dbefb368ad20897822dc63ddc69d8.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table>

  
**2\. That Phantom That Wouldn't Die**  
 This one was more popular immediately following the release of the *JudgmentTM* set, but it was so prolific, it's got a special place in my heart. Players used to love to swarm the customer service room and Bugzilla to let us know that you couldn't destroy a Phantom with an Armadillo Cloak on it. They were at least partly right. You certainly couldn't destroy it using damage.

The Phantom ability has two parts: First, it prevents all damage to the creature; second, a counter is removed every time damage is prevented. The first part functions even when there are no counters left to remove. So, as long as there's something keeping the creature's toughness above zero when all the counters are gone, the creature's not going anywhere unless you've got a way to dispose of it that doesn't involve damage. (See #1 above for a nice way to banish pesky Phantoms.)

**3\. Shuffle Off To Buffalo**  
 The shuffler is a tricky (and sensitive) issue for players. From our side, we're pretty much completely convinced that the shuffling algorithm is sufficiently random. You can reference Chris Green's explanation of our shuffling code at [http://www.lplizard.com/mtgo/developer/shuffle.htm](https://web.archive.org/web/20030204000000/http://wizards.com/leaving.asp?url=http://www.lplizard.com/mtgo/developer/shuffle.htm&origin=magic_magiconline_articlejr020403).

Unfortunately, not even a completely random shuffler can save you from the occasional bad draw, frustrating as it is. 

The quality assurance cycle doesn't end with card testing. New formats and user interface changes demand constant attention, and there's a certain amount of time that has to be spent reviewing old functionality to make sure that something new hasn't thrown a monkey wrench into the works.

We're pushing hard to get the *Legions* set, as well as a few other goodies, ready to go live in upcoming updates.

Keep your fingers crossed.