---
id: fthrfrbf
kind: article
lang: en
path: /en/articles/feature/2002/08-02-tending-the-land
title: Tending the Land
published: '2002-08-02'
column_slug: feature
column: Feature
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    lang_detected: en
    capture_id: 1198355
    url: https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    captured_at: '2021-10-22 13:10:25+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    lang_detected: en
    capture_id: 1198355
    url: https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    captured_at: '2021-10-22 13:10:25+00'
    rule: drupal.posted_in_date
  column:
    page_key: magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    lang_detected: en
    capture_id: 1198355
    url: https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
    captured_at: '2021-10-22 13:10:25+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/tending-land-2002-08-02
    lang_detected: en
    capture_id: 735334
    url: https://magic.wizards.com/en/articles/archive/latest-developments/tending-land-2002-08-02
    captured_at: '2021-09-25 12:46:43+00'
    rule: drupal.div_author
sources:
- document_id: fthrfrbf
  url: https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
  page_key: magic.wizards.com/en/articles/archive/tending-land-2002-08-02
  lang: en
  template: drupal
  captured_at: '2021-10-22 13:10:25+00'
  capture_id: 1198355
  wayback_url: https://web.archive.org/web/20211022131025id_/https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
- document_id: fthrfrbf
  url: https://magic.wizards.com/en/articles/archive/latest-developments/tending-land-2002-08-02
  page_key: magic.wizards.com/en/articles/archive/latest-developments/tending-land-2002-08-02
  lang: en
  template: drupal
  captured_at: '2021-09-25 12:46:43+00'
  capture_id: 735334
  wayback_url: https://web.archive.org/web/20210925124643id_/https://magic.wizards.com/en/articles/archive/latest-developments/tending-land-2002-08-02
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: fthrfrbf
  capture_id: 1198355
  url: https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
  wayback_url: https://web.archive.org/web/20211022131025id_/https://magic.wizards.com/en/articles/archive/tending-land-2002-08-02
  captured_at: '2021-10-22 13:10:25+00'
  template: drupal
  sha256: 683a96339a3b1559168cde0578c09552e65f05c1858cdbc74ad13de41bb83d5d
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:latestdevelopments@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - latestdevelopments@wizards.com
  occurrences: 1
---
I can't say I'm surprised by the results of last week's poll:

<table><tbody><tr><td colspan="3"><b>Do you think Squirrels belong in Magic?</b></td>&#10;		</tr><tr><td>Yes</td>&#10;			<td>7551</td>&#10;			<td>81.8%</td>&#10;		</tr><tr><td>No</td>&#10;			<td>1681</td>&#10;			<td>18.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>9232</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr><tr><td></td>&#10;		</tr></tbody></table>

Squirrels may not be the most bad-ass monsters to raze the *Magic* world, but they're quite popular nonetheless.

![30 land](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb31_pic1_en.jpg)

This week I'd like to talk about something quite fundamental to *Magic*: land. It's awfully hard to play without it, but it's often overlooked. Personally, I've always been a big fan of land--I even finished second at the first Grand Prix–Boston (losing to Jon Finkel in the finals) with a whopping *thirty* lands in my *Tempest* Block Constructed "Counter-Phoenix" deck. During playtesting, we kept burning [Whispers of the Muse](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse) just to dig for more land to set up [Shard Phoenix](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shard+Phoenix) - [Forbid](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forbid) locks, so eventually we simply replaced the Whispers with four more lands.

I brought that love of land to Wizards with me. In fact, on my very first day on the job I was thrown into one of the early *Invasion* development meetings, where they were talking about land. The team knew the set should have good multicolored lands because they wanted players to build decks around all the cool multicolored cards we were planning to print. In addition, the team was rapidly coming to realize that [Rishadan Port](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rishadan+Port) was better than it was intended to be. So they started talking about making the *Invasion* multilands untargetable.

That didn't sound terribly useful to me, but there I was on my first day on the job, so I just listened for a bit more. The multilands in the set at the time looked something like this:

\[White-Blue Land\]  
 Land  
 When CARDNAME comes into play, return a plains or an island to your hand.  
 T: Add W or U to your mana pool.

(This probably looks familiar because this design eventually turned into the *Planeshift* Lairs, like [Darigaaz's Caldera](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darigaaz%27s+Caldera).)

The more I thought about these, the worse they seemed to me. They reminded me of [Undiscovered Paradise](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undiscovered+Paradise), which I always thought was overrated because it's hard to build up a solid mana base if your land keeps returning to your hand. [Undiscovered Paradise](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undiscovered+Paradise) was decent, but only because it tapped for all five colors, which allowed it to fuel three- to five-color decks. I had trouble imagining that a cycle of five of these two-color bounce lands could support the weight of a fully multicolored environment, so I made my first development-team contribution:

"Why don't we just do 'comes-into-play-tapped' dual lands?"

They stared at me, so I elaborated. "They're just like [Tundra](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tundra) except they come into play tapped and don't count as an island or a plains."

![Coastal Tower is almost a Tundra](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb31_pic2_en.jpg)

Their first reaction was "No way--that's way too good." In fact, R&D had already considered exactly those lands and decided on theoretical grounds that they were significantly better than basic lands, and thus we couldn't print them.

Luckily, I had actually had this conversation before with several of my old Team CMU buddies. Mike Turian, for one, has always maintained that Wizards should just reprint the dual lands as they originally were. Who cares that they're strictly better than basic lands? All they really do is let people play their spells. *Magic* is definitely more fun when both players can play all the cards they draw, so something about Mike's simple argument always rang true to me. I never thought the original duals should actually be reprinted, especially since the reprint policy forbids it, but I always did think Wizards could print better lands than they had been printing. Block Constructed hammered this home when *Tempest* block's "depletion" lands (and comes-into-play-tapped enemy-color pain lands) failed to support multicolored play. Urza block was even worse--even after two rounds of card bannings, it was hard to stray too far from monocolor because you just couldn't build a consistent mana base to play all of your spells (though [Yavimaya Elder](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yavimaya+Elder) helped a bit). Masques block had similar problems that were exacerbated by the presence of Port.

Pat Chapin was another former teammate who had also sounded off on this issue. Chapin is famous for putting together his own homemade sets of *Magic* cards that we would often "Chapin Draft" with. At some point, he decided to try out comes-into-play-tapped dual lands, and they seemed good--but not too good. That meant when I was in my first *Invasion* development team meeting proposing those very lands, I had a bit of confidence because I had some experience playing with them.

"They're not too good," I claimed . . . and, much to my relief, everyone else was willing to listen to the new guy. They still seemed skeptical, but they reasoned that it couldn't hurt to try them out. The team decided to switch over to the crazy lands long enough to get a read on how good they actually were. If they were too good, we could always go back to the bounce lands. And if they weren't too good, then that was even better--we wanted good lands because we wanted everyone to be able to play their spells.

The rest of the story is pretty obvious. Those lands were indeed good--but not too good--and [Coastal Tower](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coastal+Tower) et al. wound up having pretty much exactly the effect they were intended to have on *Invasion* block, Standard, and casual play. In fact, they were initially rares (like most of our multilands), but we decided it was so important to the environment that people be able to consistently play their multicolored cards that we lowered them to uncommon status so that there would be more of them floating around.

Later, the *Planeshift* team decided that more multilands were a good idea, so the bounce multis wound up there--but instead producing *three* different colors. That fit the three-color *Planeshift* theme quite nicely (Charms, Lairs, etc.) and put them at a pretty interesting power level.

![Coastal Tower, Adarkar Wastes, and Skycloud Expanse](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb31_pic3_en.jpg)

Since *Invasion,* R&D's land philosophy has evolved and become better defined. Several more developers with a lot of competitive Constructed *Magic* experience joined the department, and Brian Schneider in particular agreed that it was okay to print really good lands--that it was actually good for the game to allow people to build consistent mana bases.

R&D's new goal is to try to put a cycle of two-color lands into each and every block--a plan good enough to support two-color decks in Block Constructed. That would ensure three cycles of decent multilands in Standard at any given time (the two blocks plus the base set), which should allow for some three- or maybe even five-color decks.

There should also be some monocolored decks, of course, and we'll continue to make cards that reward you for playing one color, such as [Mutilate](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutilate) and [Mind Sludge](https://web.archive.org/web/20020802000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sludge) for black. But our goal is to make sure that (unlike during the *Tempest* era) multicolored play is always an option. 

* * *

*Randy may be reached at latestdevelopments@wizards.com.*