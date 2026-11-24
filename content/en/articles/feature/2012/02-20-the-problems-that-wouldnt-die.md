---
id: q6k7y6xx
kind: article
lang: en
path: /en/articles/feature/2012/02-20-the-problems-that-wouldnt-die
title: The Problems That Wouldn't Die
published: '2012-02-20'
column_slug: feature
column: Feature
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    lang_detected: en
    capture_id: 1144725
    url: https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    captured_at: '2022-09-26 19:53:09+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    lang_detected: en
    capture_id: 1144725
    url: https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    captured_at: '2022-09-26 19:53:09+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    lang_detected: en
    capture_id: 1144725
    url: https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
    captured_at: '2022-09-26 19:53:09+00'
    rule: drupal.div_author
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/183
    lang_detected: en
    capture_id: 589903
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/183
    captured_at: '2014-02-17 19:32:50+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: q6k7y6xx
  url: https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
  page_key: magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
  lang: en
  template: drupal
  captured_at: '2022-09-26 19:53:09+00'
  capture_id: 1144725
  wayback_url: https://web.archive.org/web/20220926195309id_/https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
- document_id: q6k7y6xx
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/183
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/183
  lang: en
  template: aspx
  captured_at: '2014-02-17 19:32:50+00'
  capture_id: 589903
  wayback_url: https://web.archive.org/web/20140217193250id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/183
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: q6k7y6xx
  capture_id: 1144725
  url: https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
  wayback_url: https://web.archive.org/web/20220926195309id_/https://magic.wizards.com/en/articles/archive/problems-wouldnt-die-2012-02-20
  captured_at: '2022-09-26 19:53:09+00'
  template: drupal
  sha256: 3032336ae7f9b530f3f0977d7573d1ed0e9def9b7b352d6a34950a0415fbd2df
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: /sites/all/modules/custom/wiz_legacy_migration/flipcard/flipcard.html?ca=173lg35g9w_en&cb=1fsvobsz3u_en&lang=en
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
I've been around for the creation of many **Magic** sets. I led the development of *Dark Ascension*, ***Magic** 2012*, *Masters Edition IV*, *Archenemy*, and *Masters Edition III*. I served on the development teams for ***Magic** 2013*, *Innistrad*, *New Phyrexia*, *Mirrodin Besieged*, ***Magic** 2011*, *Worldwake*, and ***Magic** 2010*. I was part of the design teams for *Innistrad* and ***Magic** 2011*.

While each of the sets I listed had its own unique personality and challenges, I noticed several problems the lead developer of each of these sets faced every time. Unsurprisingly, I faced each of them during my trip through *Dark Ascension* development. Today, I'll lead you through some of them as well.

We'll start with the biggest one—one that everyone working on every set needs to wrestle with.

### What is This Set Actually About?

Like any work of art, every **Magic** set is about something, and the thing it is about informs all of the individual decisions one must make while making it. For example, *New Phyrexia* is about being assimilated into a creepy, horrifying hive mind, and therefore does its best to make you feel a little violated. There are small color pie bleeds all over the place, Phyrexian mana gives you access to effects from colors you aren't playing at a cost and allows for free spells, and we also put in cards like [Praetor's Grasp](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Praetor%27s+Grasp) that try to feel as transgressive as possible.

![](https://i.ormos.uk/e4/12/e412dc7fa9e11304ed62bcddde62fb134c7c877174939942ab92bfebd76396c4.jpg)

Ideally, the design team figures out what a set is about. Under normal circumstances, the design team's guess is right, as at the handoff point, the team has spent much more time with the set than anyone else.

Sometimes, however, the design team gets it wrong.

Mark Rosewater has written elsewhere about what happened during *Dark Ascension* design that led to this point, but this is my article, so I'll give my perspective.

Before we get to **Magic**, though, let's take a quick trip to the movies.

*The American* is one of my favorite films. A tense, quiet, and intimate character study of a deeply reserved man, it features a nearly impenetrable performance from George Clooney and a gorgeous, deliciously tragic ending that seems to me both inevitable and perfect. It was marketed, however, as a Bourne-style thriller as opposed to the beautifully constructed character study it was, and so many people went to see it with expectations that were not fulfilled.

![](https://i.ormos.uk/45/b6/45b68492d31b7197c65a5b284257c9b0f449f650247c8d76c0aa771f036f6af6.jpg)

Let's go back to **Magic**. Mark Rosewater is, at heart, an artist. A quick look through his article archives can find you high-concept articles like "[Elegance](/en/articles/makingmagic/2004/10-14-elegance)" and "[80,000 Words](/en/articles/makingmagic/2006/08-07-80-000-words-2)" that push the boundaries of what can be done in a **Magic** article for no other reason than the sheer joy of trying. He often approaches **Magic** sets that way—*Zendikar* exists mostly because he wanted to see if he could design a block around land. Mark is a consummate professional, and will always try to design something appropriate to the space he has been asked to fill, but he gets a big kick out of making things that tickle his artist's brain.

As soon as we settled on a story structure for the *Innistrad* block, it became clear the second set in the block was going to have the bleakest tone. The next question one must ask is how to convey that tone using mechanics in **Magic** text boxes, as text boxes are the most powerful tools we have to communicate with you. **Magic** is a card game, after all, and those text boxes define so much of what you experience while you play.

Mark chose to express the bleak tone of *Dark Ascension* by showing that Innistrad's humans were in trouble. He did this with the fateful hour mechanic.

![Gather the Townsfolk](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gather+the+Townsfolk)

 

Fateful hour does a reasonable job of expressing the idea that the humans are in trouble. The idea of taking advantage of it requires you to fight many of your most basic **Magic** instincts, though. Most players do their very best to avoid being at 5 or less life. Many brand-new **Magic** players will chump-block with their 1/1 to avoid having a 2/2 hit them from 20 to 18, and even I'm uncomfortable thinking about being at 5 life when there are [Brimstone Volley](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brimstone+Volley)s flying around.

The other mechanic Mark used to demonstrate the humans' trials and tribulations was the double-faced cards. The majority of the double-faced cards in *Dark Ascension* are humans who transform into monsters of some sort, be they vampires, zombies, or werewolves—and one of the ones that isn't is a demon who thinks humans are delicious. While I liked this part of the design, I wasn't thrilled about how subtle it was. The exciting part of the card is the transformed side, not the human.

There was one more new mechanic in the first design handoff as well, an evolution of one of *Innistrad*'s mechanics that didn't add much to the thematic tone.

The point of a **Magic** set is to give players cards they want to own. To my mind, none of the new mechanics in the set both expressed the theme of the set and allowed me to make unambiguously appealing **Magic** cards. That was a problem.

The double-faced cards ended up giving me the solution I proposed. If the exciting part of the double-faced cards that tell the story of *Dark Ascension* is the monsters, maybe the exciting part of the whole set is the monsters. What if the story of *Dark Ascension* was about how awesome the monsters were?

While I love *The American*, it tells a subtle and nuanced story that requires two hours. Most people already know how *The Bourne Identity* is supposed to work, so you don't have to do as much to get them calibrated. *Dark Ascension* has to tell its story on a bunch of little pieces of cardboard, so we don't have time for the subtle stuff to do its job alone. Therefore, I asked Mark Rosewater for an all-upside creature mechanic that we could put exclusively on "monsters." He delivered with undying, and when I heard his undying pitch for the first time, I knew we were going to be okay.

![Flayer of the Hatebound](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flayer+of+the+Hatebound)

 

We did several other things to change the focus of the set from "Humans are in trouble" to "Monsters kick ass," including upping the level of tribal support and making a mythic cycle of high-profile gold "monsters." We also added a big pile of cards that like it when you sacrifice Humans, which is so transgressive that it shoves the "Humans are in trouble" message in your face much more effectively than Mark's subtler ideas from before. In the end, however, we had a cohesive message, and everything in the set began to serve that message together.

### This Mechanic is Too Good!

In hindsight, I think I was a little ambitious when I jumped so enthusiastically at undying. As it turns out, creatures with a built-in second lifespan are really good. Our early Limited playtests with the mechanic were attrition-based slogs all about getting two-for-ones with undying guys, which is not our idea of a great time.

The other challenge we faced with undying is that it forces us to make cards that read poorly. The undying line of text is appealing, but creatures that have a built-in second lifetime end up looking smaller than people expect, and that makes them sad. I don't know anyone who likes paying ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) for a 4/1, and it takes some thought to realize that you are getting a free 5/2 out of the deal.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Pyreheart Wolf" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Pyreheart+Wolf"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Nearheath Stalker" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Nearheath+Stalker"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

[Pyreheart Wolf](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyreheart+Wolf) is a perfect example of this. It's a 1/1 for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), which is pretty lame-feeling. It has an ability whose in-play usefulness is hard to process accurately. All in all, it reads kind of stupid. The card is secretly pretty powerful, but most players won't figure that out until they actually attack with it the first time.

While I'm fine with making **Magic** cards whose power you discover a little later on, I prefer it when those cards aren't the ones with the new mechanic that is supposed to excite people. Unfortunately, this happens with some regularity. Mechanics like infect, affinity, and retrace all did the same thing. Hilariously, while undying is technically an upgrade on persist, it has this problem much more acutely than persist does—persist gives you the bigger guy first!

We fought the first of these problems in several ways. [Stormbound Geist](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbound+Geist) and [Sightless Ghoul](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sightless+Ghoul) have built-in restrictions against blocking, and [Strangleroot Geist](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangleroot+Geist) and [Pyreheart Wolf](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyreheart+Wolf) both encourage you to attack. That was enough to make Limited feel reasonable, so we stopped there.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Stormbound Geist" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Stormbound+Geist"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Sightless Ghoul" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sightless+Ghoul"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

We fought the second problem by building a few high-profile cards that didn't look anemic. [Geralf's Messenger](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger), [Strangleroot Geist](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangleroot+Geist), and [Vorapede](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vorapede) are my attempts at that. All three of them inspired some excitement when they were previewed and have seen some degree of Constructed play now, so I'm happy to call that a win.

### How Do We Fit All This Stuff in Here?

While making a **Magic** set, the design team must create enough big ideas to fill out a card set. The development team must condense those ideas down small enough that they fit within the hard constraints of the set. Because the designers know the developers will throw out some fraction of the work, they tend to "over-design"—to put more into the set than they know could possibly be printed.

As a member of several development teams, I appreciate this very much. However, it creates another one of the problems development teams need to solve. We usually toss out some amount of the big ideas without worrying about it, but often the amount of content we like that we leave in is bigger than the space we have to fill.

That happened in a big way with *Dark Ascension*. For quite a while, there were morbid cards and on-color flashback cards in all colors, and there were a few fateful hour cards in blue. That was, of course, on top of an increased amount of tribal synergies, two cycles of spells with off-color flashback costs, thirteen undying creatures, and thirteen double-faced cards. Something was going to have to give. But we also didn't want to cut so deeply that the set's themes were threatened.

![](https://i.ormos.uk/34/6a/346a396ac5b52ca530783c20d17d997b22b3a2bd2049529ba48ba3a131836568.jpg)

In the end, we preserved only the things we thought were either new to *Dark Ascension* or important for continuing a theme or aspect of the feel of *Innistrad*. That meant the double-faced cards, off-color flashback spells, undying creatures, and double-faced cards were safe. Morbid and flashback found themselves under more scrutiny, though. The decks focusing around those mechanics in *Innistrad* were black-green and blue-red respectively, so we took all the morbid cards out of blue and red and all the common and uncommon flashback cards that weren't part of the two cycles out of white, black, and green. I was worried someone might notice and think the set was dry after that, but no one in the next three Limited playtests thought anything was wrong.

### The Set's Themes Are Too Good in Draft!

We have come to the last problem we normally have to deal with in a set's development. After we spend lots of time making new cards that try to make you do a particular thing, we discover to our horror that most of the time in Limited, people only want to do the thing. Oops.

In the case of *Dark Ascension*, we discovered there was too much tribal support in the set. We keep track of how many cards of each color people play in drafts in one of our internal databases, and a few early drafts showed me I had made the four monster tribes so appealing that everyone was drafting allied-color decks. This is a problem because we want you to be able to draft the set many times, and achieving that goal means getting as many different strategies as possible to be viable. If there aren't satisfying enemy-color decks, that's half the possible baseline strategies down the drain—a punishing loss in total Draft lifespan.

I've found two ways to attack this problem. The first way works best early in the process when there's time to test more things, and that is to build more enablers for the underplayed strategies. Unfortunately, when time is shorter, the other method is safer—toning down the power level of the enablers for the strategies that are too good. In the case of *Dark Ascension*, Erik made the specific suggestion that solved the problem.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Briarpack Alpha" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Briarpack+Alpha"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Markov Warlord" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Markov+Warlord"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Tower Geist" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Tower+Geist"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Farbog Boneflinger" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Farbog+Boneflinger"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

All four of the above cards look like simple dudes, but they were originally a cycle of creatures that counted the total number of things in play of their type. [Farbog Boneflinger](https://web.archive.org/web/20120220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Farbog+Boneflinger), for example, used to give –X/–X, where X was the number of Zombies you controlled. Erik suggested I just replace X with 2 on all of those cards and call it a day. As soon as I did that, all the enemy-color strategies Erik so lovingly crafted for *Innistrad* were playable again.

I have joked that the design team's job is to make every **Magic** set different from the other ones, and the development team's job is to make every **Magic** set the same. After all, every set needs to have creatures and spells, have a reasonable curve, have enough ways to destroy all the major card types, and so on. Because development teams have such clear targets, we face problems like the ones in this article over and over again. Happily, as long as we have inventive designers like Mark Rosewater around, the design teams will keep presenting us with variations on those problems we haven't quite solved before, and I don't think **Magic** developers will ever get bored.