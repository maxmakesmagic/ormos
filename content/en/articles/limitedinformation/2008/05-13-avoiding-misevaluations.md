---
id: a06tvknb
kind: article
lang: en
path: /en/articles/limitedinformation/2008/05-13-avoiding-misevaluations
title: Avoiding Misevaluations
published: '2008-05-13'
column_slug: limitedinformation
column: Limited Information
authors:
- slug: stevesadin
  name: Steve Sadin
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    lang_detected: en
    capture_id: 746196
    url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    captured_at: '2022-01-29 08:17:10+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    lang_detected: en
    capture_id: 746196
    url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    captured_at: '2022-01-29 08:17:10+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    lang_detected: en
    capture_id: 746196
    url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    captured_at: '2022-01-29 08:17:10+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    lang_detected: en
    capture_id: 746196
    url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
    captured_at: '2022-01-29 08:17:10+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - dgk72hcy
  - me1cqnfm
sources:
- document_id: a06tvknb
  url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
  page_key: magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
  lang: en
  template: drupal
  captured_at: '2022-01-29 08:17:10+00'
  capture_id: 746196
  wayback_url: https://web.archive.org/web/20220129081710id_/https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
- document_id: dgk72hcy
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/ss6&=RSS-MTGCOM
  page_key: wizards.com/default.asp?=RSS-MTGCOM&x=mtgcom/daily/ss6
  lang: en
  template: classic_asp
  captured_at: '2008-05-16 10:14:44+00'
  capture_id: 1261827
  wayback_url: https://web.archive.org/web/20080516101444id_/http://www.wizards.com/default.asp?x=mtgcom/daily/ss6&=RSS-MTGCOM
- document_id: me1cqnfm
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/ss6,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/ss6
  lang: en
  template: classic_asp
  captured_at: '2008-05-17 06:59:50+00'
  capture_id: 1999488
  wayback_url: https://web.archive.org/web/20080517065950id_/http://www.wizards.com/default.asp?x=mtgcom/daily/ss6,0
- document_id: me1cqnfm
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/ss6&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/ss6
  lang: en
  template: aspx
  captured_at: '2009-06-03 20:11:12+00'
  capture_id: 257078
  wayback_url: https://web.archive.org/web/20090603201112id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/ss6&print=true
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: a06tvknb
  capture_id: 746196
  url: https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
  wayback_url: https://web.archive.org/web/20220129081710id_/https://magic.wizards.com/en/articles/archive/limited-information/avoiding-misevaluations-2008-05-13
  captured_at: '2022-01-29 08:17:10+00'
  template: drupal
  sha256: c91d5dc17c471a9f63e7670b10b06138a9748367ad09694a13266c99108339ef
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 8
---
One of the most important parts of Limited **Magic** is navigating your way around the combat phase. There are a lot of nuances that can come up during a combat, most of which either take place during attack and blocking or in anticipation of attacking and blocking. Persist and wither shake up normal attacking and blocking calculations considerably, but it shouldn't be too hard to take these changes into account as long as you frame them properly.

I'm not going to get too deep into general attacking and blocking theory in this article, though you should expect to hear more from me on the topic as I think it is one of the most interesting and important parts of **Magic**. For those of you who are interested in learning more about blocking and trading, I would strongly recommend that you check out [this excellent article](https://web.archive.org/web/20080513000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/academy/5) by Ted Knutson. 

### Rock-Paper-Scissors

There is a bit of a Rock-Paper-Scissors dynamic that takes place between creatures that don't have persist or wither, creatures with wither, and creatures with persist.

<table><tbody><tr><td><div><div><img alt="Grizzly Bears" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Grizzly+Bears"></div></div></td><td><div><div><img alt="Sickle Ripper" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sickle+Ripper"></div></div></td><td><div><div><img alt="Safehold Elite" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Safehold+Elite"></div></div></td></tr></tbody></table>

If you have a [Grizzly Bears](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears), and your opponent has a [Grizzly Bears](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears), you will generally both feel completely fine about a trade. However, if you have a [Grizzly Bears](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and your opponent has a [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickle+Ripper), you will get a little bit of an advantage if they trade. If you have a [Grizzly Bears](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and your opponent has a [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) and they trade, your opponent will get a sizable advantage out of the deal as they still have a card to show for the exchange. If you have a [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickle+Ripper) and your opponent has a [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), you will generally be very happy with that exchange, as the [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite)'s persist trigger won't go off because it died with -1/-1 counters on it.

### Persistence Pays Off

Persist is actually fairly easy to take into account when evaluating potential plays. If a creature with persist dies, its controller gets something very tangible back. While we haven't dealt with persist before *Shadowmoor*, we have dealt with plenty of creatures that have game-altering "leaves play" effects.

Cards like [Mogg War Marshal](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+War+Marshal), [Mudbutton Torchrunner](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mudbutton+Torchrunner), [Dripping-Tongue Zubera](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dripping-Tongue+Zubera), [Scuttling Death](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuttling+Death), etc. all had the potential to have very significant game altering leave play effects. These creatures had game-altering affects not so much in the sense of being overly powerful, but in the sense that they would force players to adjust their normal play and valuations of creatures considerably in order to properly take into account their "leaves play" effects. 

![Scuttling Death](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scuttling+Death)

Playing against soulshift back in Kamigawa block was actually considerably more difficult than playing against persist. Sure, it's normally awesome to trade your 2/2 with a 4/2, but if that 4/2 is a [Scuttling Death](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuttling+Death) that is going to [Raise Dead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead) a significant Spirit creature on its way out, that trade suddenly might become a lot less appealing, especially if that Spirit has soulshift too! When calculating how to deal with soulshift, you wanted to time your trades in such a way that your opponent would get their creatures back either at a time when their mana was particularly tight, or once the returned creature would have a minimal impact on the board.

That is not to say that persist is boring in any way, or easy to play with or around. In fact, minimizing the effectiveness of persist is one of the more important skills necessary for success in *Shadowmoor* Limited.

If you have a persist creature without any -1-1 counters on it, you are probably going to be looking to trade it for another non-wither creature as quickly as possible, as you won't be giving up much board position to do so.

By the same token, but from the other side, one of the keys to dealing with persist is figuring out when to be patient. Now, I know this might sound a bit obvious, but the answer to when you can be patient is "whenever you can afford to be." 

For example, if you have a number of 2/1s (without wither) in your deck, and a 2/2 in play, you should be very hesitant to trade your 2/2 with a [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite). 

### Wither? I Hardly Even Know Her!

While persist presents a lot questions that we have pretty reasonable points of reference to consider, wither presents some new, completely unexplored questions. By their very nature, wither creatures allow for more semi-bluffs than I can even begin to imagine.

![Sootwalkers](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sootwalkers)

Normally, if a player attacks with a 2/1 into your 3/3 it would make sense to block so long as you don't believe that there is some sort of devastating trick, such as a [Hunting Triad](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hunting+Triad) to reinforce their attacker, waiting in the wings. However, if there is a [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickle+Ripper) attacking you and you have only a [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sootwalkers) on defense, you are probably going to want to think twice before blocking. If your opponent is making this attack then you have to consider why he or she is doing it.

In this situation, just as in any similar situation, they are making their attack either because they want you to block, or because they don't expect you to block. Normally you would either decide to call their bluff or not (or if you have mana open and a trick of your own you might be able to call and still get them even if they think they have you).

However, when someone is attacking into a larger creature with a wither creature, they have the benefit that even if they get blocked and they don't have a trick to win the combat outright, they are still getting a pretty good deal out of the exchange.

I've outlined a couple of very basic examples of how you might want to adjust your thought process when dealing with wither or persist creatures. I'm not trying to suggest that it there is some universally correct calculation that tells you when and with what you want to block in these situations, only that there are situations that favor a player slightly more than they normally would. This suggests that it would be worthwhile to at least try to think of a better use for your creatures even if you discover that you can't find a better deal.

There are of course obvious exceptions to this. For example, if you have a 4/2 and a 5/2 in your hand, you are probably going to be itching to turn your opponent's [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) into a 1/1 even if you have to give up a creature in the process.

And, even though you are going to want to think twice before blocking a [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickle+Ripper) with your 3/3, there is one card that will make that block an excellent play pretty much every time...

### Fate Transfer? I Hardly Even Know Her!

Every time a new set comes around, there are a handful cards that are completely misunderstood and either over- or undervalued as a result of that. One of the cards that jumps out at me as being cripplingly misunderstood is [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer).

![Fate Transfer](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fate+Transfer)

I'm fairly certain that [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) is one of the hidden gems of the format. When it is good it tends to be great. However, this doesn't mean that [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) is always good. In fact, it is pretty frequently almost unplayable as a maindeck card. You see, in order to utilize [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) at all, you need to feel confident that there are going to be, on average, at least six cards between your deck and your opponent's decks that work well with [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), including at least two cards that work very well with [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer). 

If your opponent has creatures with persist, then your [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer)s will be slightly better than normal, but opponent's creatures with persist don't actually make [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) any easier to use properly.

To give you a sense of how many -1/-1 counter cards players typically run in a draft deck, I took a peek at [the Top 8 decks](/en/articles/event-coverage/2008/05-04-top-8-decklist) from [GP–Brussels](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en/events/coverage/cornelissen-claims-victory-brussels). 

(Please note that I am talking about each of the below cards in terms of how useful they are for your [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) if they are in your opponent's deck, so if I say that a card is good I mean that it is the type of card that is good for you if your opponent has it and you have [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer).)

#### Antoine Ruel

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (12)

1 [Puresight Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuresight%5D+%5BMerrow%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Merrow Wavebreakers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMerrow%5D+%5BWavebreakers%5D) 1 [Prismwake Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismwake%5D+%5BMerrow%5D) 2 [Wanderbrine Rootcutters](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWanderbrine%5D+%5BRootcutters%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Painter's Servant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainter%5D+%5BServant%5D) 1 [Morselhoarder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMorselhoarder%5D) 

##### Sorcery (4)

1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 2 [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncremental%5D+%5BBlight%5D) 1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

##### Instant (3)

1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 2 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### Artifact (2)

2 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 

##### Enchantment (3)

1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Power of Fire](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D) 

##### Land (16)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

40 Cards 

##### Blue (5)

2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Merrow Wavebreakers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMerrow%5D+%5BWavebreakers%5D) 1 [Prismwake Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismwake%5D+%5BMerrow%5D) 

##### Black (2)

2 [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncremental%5D+%5BBlight%5D) 

##### Red (3)

1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 1 [Power of Fire](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### Multi colored (11)

1 [Puresight Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuresight%5D+%5BMerrow%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 2 [Wanderbrine Rootcutters](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWanderbrine%5D+%5BRootcutters%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Morselhoarder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMorselhoarder%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 2 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### Colorless (19)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Painter's Servant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainter%5D+%5BServant%5D) 2 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 

40 Cards 

##### 2 (11)

1 [Puresight Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuresight%5D+%5BMerrow%5D) 2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Painter's Servant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainter%5D+%5BServant%5D) 2 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Power of Fire](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 2 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### 3 (4)

1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 1 [Prismwake Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismwake%5D+%5BMerrow%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

##### 4 (4)

1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 2 [Wanderbrine Rootcutters](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWanderbrine%5D+%5BRootcutters%5D) 1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 

##### 5 (4)

1 [Merrow Wavebreakers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMerrow%5D+%5BWavebreakers%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 2 [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncremental%5D+%5BBlight%5D) 

##### 6 (1)

1 [Morselhoarder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMorselhoarder%5D) 

24 Cards 

##### Common (33)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Merrow Wavebreakers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMerrow%5D+%5BWavebreakers%5D) 1 [Prismwake Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismwake%5D+%5BMerrow%5D) 2 [Wanderbrine Rootcutters](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWanderbrine%5D+%5BRootcutters%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Morselhoarder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMorselhoarder%5D) 2 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 1 [Power of Fire](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### Uncommon (5)

1 [Puresight Merrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuresight%5D+%5BMerrow%5D) 2 [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncremental%5D+%5BBlight%5D) 2 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### Rare (1)

1 [Painter's Servant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainter%5D+%5BServant%5D) 

##### Mythic (1)

1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Briarberry+Cohort)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Torpor+Dust)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Power+of+Fire)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Puresight+Merrow)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kinscaer+Harpoonist)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Manamorphose)

a:21:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Puresight Merrow";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Thistledown Duo";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Briarberry Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Kinscaer Harpoonist";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Merrow Wavebreakers";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Prismwake Merrow";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Wanderbrine Rootcutters";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Cultbrand Cinder";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Painter's Servant";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Morselhoarder";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Elsewhere Flask";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Curse of Chains";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Torpor Dust";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Burn Trail";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Incremental Blight";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Power of Fire";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Puncture Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Firespout";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Manamorphose";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Antoine Ruel's blue-red splash black deck has a [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultbrand+Cinder), a [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puncture+Bolt), and two [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Blight)s. Evaluating how good these cards are if they are in your opponent's deck and you have [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), the [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puncture+Bolt) is OK, the [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultbrand+Cinder) is good, and the two [Incremental Blight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Blight)s are very good.

1 OK  
 1 Good  
 2 Very good

#### Holger Lange

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (16)

2 [Rune-Cervin Rider](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Cervin%5D+%5BRider%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Windbrisk Raptor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindbrisk%5D+%5BRaptor%5D) 2 [Wildslayer Elves](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildslayer%5D+%5BElves%5D) 1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Raven's Run Dragoon](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaven%5D+%5BRun%5D+%5BDragoon%5D) 2 [Safehold Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BDuo%5D) 2 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Seedcradle Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedcradle%5D+%5BWitch%5D) 1 [Thornwatch Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThornwatch%5D+%5BScarecrow%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Wicker Warcrawler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWicker%5D+%5BWarcrawler%5D) 

##### Sorcery (1)

1 [Safewright Quest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafewright%5D+%5BQuest%5D) 

##### Instant (3)

1 [Viridescent Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridescent%5D+%5BWisps%5D) 1 [Mirrorweave](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMirrorweave%5D) 1 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### Artifact (1)

1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 

##### Enchantment (2)

1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Presence of Gond](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPresence%5D+%5Bof%5D+%5BGond%5D) 

##### Land (17)

8 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

40 Cards 

##### White (4)

2 [Rune-Cervin Rider](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Cervin%5D+%5BRider%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Windbrisk Raptor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindbrisk%5D+%5BRaptor%5D) 

##### Green (5)

2 [Wildslayer Elves](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildslayer%5D+%5BElves%5D) 1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Presence of Gond](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPresence%5D+%5Bof%5D+%5BGond%5D) 1 [Viridescent Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridescent%5D+%5BWisps%5D) 

##### Multi colored (10)

1 [Raven's Run Dragoon](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaven%5D+%5BRun%5D+%5BDragoon%5D) 2 [Safehold Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BDuo%5D) 2 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Seedcradle Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedcradle%5D+%5BWitch%5D) 1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Safewright Quest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafewright%5D+%5BQuest%5D) 1 [Mirrorweave](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMirrorweave%5D) 1 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### Colorless (21)

8 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Thornwatch Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThornwatch%5D+%5BScarecrow%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Wicker Warcrawler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWicker%5D+%5BWarcrawler%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 

40 Cards 

##### 1 (3)

1 [Seedcradle Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedcradle%5D+%5BWitch%5D) 1 [Safewright Quest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafewright%5D+%5BQuest%5D) 1 [Viridescent Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridescent%5D+%5BWisps%5D) 

##### 2 (4)

1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 2 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 

##### 3 (2)

1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Presence of Gond](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPresence%5D+%5Bof%5D+%5BGond%5D) 

##### 4 (9)

2 [Rune-Cervin Rider](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Cervin%5D+%5BRider%5D) 2 [Wildslayer Elves](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildslayer%5D+%5BElves%5D) 1 [Raven's Run Dragoon](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaven%5D+%5BRun%5D+%5BDragoon%5D) 2 [Safehold Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BDuo%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Mirrorweave](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMirrorweave%5D) 

##### 5 (3)

1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Wicker Warcrawler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWicker%5D+%5BWarcrawler%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 

##### 6 (1)

1 [Thornwatch Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThornwatch%5D+%5BScarecrow%5D) 

##### 7 (1)

1 [Windbrisk Raptor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindbrisk%5D+%5BRaptor%5D) 

23 Cards 

##### Common (34)

8 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Rune-Cervin Rider](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Cervin%5D+%5BRider%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 2 [Wildslayer Elves](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildslayer%5D+%5BElves%5D) 1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Raven's Run Dragoon](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaven%5D+%5BRun%5D+%5BDragoon%5D) 2 [Safehold Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BDuo%5D) 2 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Thornwatch Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThornwatch%5D+%5BScarecrow%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Safewright Quest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafewright%5D+%5BQuest%5D) 1 [Presence of Gond](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPresence%5D+%5Bof%5D+%5BGond%5D) 1 [Viridescent Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridescent%5D+%5BWisps%5D) 

##### Uncommon (4)

1 [Seedcradle Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedcradle%5D+%5BWitch%5D) 1 [Wicker Warcrawler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWicker%5D+%5BWarcrawler%5D) 1 [Manamorphose](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManamorphose%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 

##### Rare (2)

1 [Windbrisk Raptor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindbrisk%5D+%5BRaptor%5D) 1 [Mirrorweave](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMirrorweave%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crabapple+Cohort)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Watchwing+Scarecrow)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Presence+of+Gond)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Viridescent+Wisps)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wildslayer+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Safehold+Sentry)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

a:21:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Rune-Cervin Rider";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Safehold Sentry";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Windbrisk Raptor";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Wildslayer Elves";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Crabapple Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Raven's Run Dragoon";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Safehold Duo";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Safehold Elite";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Seedcradle Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Thornwatch Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Watchwing Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Wicker Warcrawler";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Shield of the Oversoul";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Safewright Quest";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Presence of Gond";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Viridescent Wisps";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Mirrorweave";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Manamorphose";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Illuminated Folio";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Holger Lange's green-white deck has two [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite)s, which raises the value of [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) slightly, [Thornwatch Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornwatch+Scarecrow), which probably isn't relevant unless you have some very good [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects, two [Wildslayer Elves](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildslayer+Elves), which could be either OK or very good for you depending on how many 4-toughness creatures and/or [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects your deck has, and [Wicker Warcrawler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wicker+Warcrawler), which can sometimes be good, but has very conditional usefulness.

2 Persist  
 4 OK or very good depending on how much toughness and/or [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects your deck has.

#### Rogier Kleij

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (14)

1 [Grim Poppet](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BPoppet%5D) 1 [Wingrattle Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWingrattle%5D+%5BScarecrow%5D) 1 [Rattleblaze Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleblaze%5D+%5BScarecrow%5D) 1 [Gravelgill Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BDuo%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 2 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 2 [Sootstoke Kindler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootstoke%5D+%5BKindler%5D) 2 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Blistering Dieflyn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlistering%5D+%5BDieflyn%5D) 1 [Cragganwick Cremator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCragganwick%5D+%5BCremator%5D) 1 [Inkfathom Infiltrator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BInfiltrator%5D) 

##### Sorcery (4)

1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 1 [Beseech the Queen](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeseech%5D+%5Bthe%5D+%5BQueen%5D) 1 [Corrupt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 

##### Instant (2)

1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 

##### Artifact (2)

1 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 1 [Umbral Mantle](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmbral%5D+%5BMantle%5D) 

##### Enchantment (1)

1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 

##### Land (17)

5 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 12 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

40 Cards 

##### Black (5)

1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Beseech the Queen](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeseech%5D+%5Bthe%5D+%5BQueen%5D) 1 [Corrupt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 

##### Red (3)

1 [Blistering Dieflyn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlistering%5D+%5BDieflyn%5D) 1 [Cragganwick Cremator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCragganwick%5D+%5BCremator%5D) 1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 

##### Multi colored (10)

1 [Gravelgill Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BDuo%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 2 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 2 [Sootstoke Kindler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootstoke%5D+%5BKindler%5D) 2 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Inkfathom Infiltrator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BInfiltrator%5D) 1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 

##### Colorless (22)

5 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 12 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Grim Poppet](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BPoppet%5D) 1 [Wingrattle Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWingrattle%5D+%5BScarecrow%5D) 1 [Rattleblaze Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleblaze%5D+%5BScarecrow%5D) 1 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 1 [Umbral Mantle](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmbral%5D+%5BMantle%5D) 

40 Cards 

##### 1 (3)

1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 

##### 2 (4)

2 [Sootstoke Kindler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootstoke%5D+%5BKindler%5D) 1 [Inkfathom Infiltrator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BInfiltrator%5D) 1 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 

##### 3 (4)

1 [Wingrattle Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWingrattle%5D+%5BScarecrow%5D) 1 [Gravelgill Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BDuo%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Umbral Mantle](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmbral%5D+%5BMantle%5D) 

##### 4 (5)

2 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Blistering Dieflyn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlistering%5D+%5BDieflyn%5D) 1 [Cragganwick Cremator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCragganwick%5D+%5BCremator%5D) 1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 

##### 5 (3)

2 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 

##### 6 (3)

1 [Rattleblaze Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleblaze%5D+%5BScarecrow%5D) 1 [Beseech the Queen](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeseech%5D+%5Bthe%5D+%5BQueen%5D) 1 [Corrupt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 

##### 7 (1)

1 [Grim Poppet](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BPoppet%5D) 

23 Cards 

##### Common (33)

5 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 12 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Wingrattle Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWingrattle%5D+%5BScarecrow%5D) 1 [Rattleblaze Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleblaze%5D+%5BScarecrow%5D) 1 [Gravelgill Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BDuo%5D) 2 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 2 [Sootstoke Kindler](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootstoke%5D+%5BKindler%5D) 2 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Blistering Dieflyn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlistering%5D+%5BDieflyn%5D) 1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Burn Trail](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurn%5D+%5BTrail%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 1 [Elsewhere Flask](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElsewhere%5D+%5BFlask%5D) 

##### Uncommon (5)

1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Inkfathom Infiltrator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BInfiltrator%5D) 1 [Beseech the Queen](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeseech%5D+%5Bthe%5D+%5BQueen%5D) 1 [Corrupt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Umbral Mantle](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmbral%5D+%5BMantle%5D) 

##### Rare (2)

1 [Grim Poppet](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BPoppet%5D) 1 [Cragganwick Cremator](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCragganwick%5D+%5BCremator%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Corrupt)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rattleblaze+Scarecrow)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sootstoke+Kindler)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elsewhere+Flask)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

a:22:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"5";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"12";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Grim Poppet";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Wingrattle Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Rattleblaze Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Gravelgill Duo";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ashenmoor Gouger";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Cultbrand Cinder";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Sootstoke Kindler";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Sootwalkers";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Blistering Dieflyn";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Cragganwick Cremator";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Inkfathom Infiltrator";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:4:"Scar";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Burn Trail";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Aphotic Wisps";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Beseech the Queen";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Corrupt";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Gloomlance";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Torture";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Elsewhere Flask";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Umbral Mantle";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Rojier Kleji's black-red deck has a [Rattleblaze Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rattleblaze+Scarecrow) and a [Wingrattle Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wingrattle+Scarecrow) to make things slightly better, a [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scar), which is OK, 2 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultbrand+Cinder)s, and a [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torture) all of which are good and a [Grim Poppet](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Poppet) which is very good.

2 Persist  
 1 OK  
 3 Good  
 1 Very good

#### Gabriel Nassif

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (15)

1 [Tatterkite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTatterkite%5D) 1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Devoted Druid](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevoted%5D+%5BDruid%5D) 1 [Hungry Spriggan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHungry%5D+%5BSpriggan%5D) 2 [Nurturer Initiate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNurturer%5D+%5BInitiate%5D) 2 [Kulrath Knight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKulrath%5D+%5BKnight%5D) 1 [Boggart Ram-Gang](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BRam-Gang%5D) 2 [Mudbrawler Raiders](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbrawler%5D+%5BRaiders%5D) 1 [Rosheen Meanderer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRosheen%5D+%5BMeanderer%5D) 1 [Tattermunge Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTattermunge%5D+%5BDuo%5D) 2 [Farhaven Elf](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFarhaven%5D+%5BElf%5D) 

##### Sorcery (2)

1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 1 [Gleeful Sabotage](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGleeful%5D+%5BSabotage%5D) 

##### Instant (4)

2 [Barkshell Blessing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarkshell%5D+%5BBlessing%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### Artifact (2)

1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 1 [Gnarled Effigy](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGnarled%5D+%5BEffigy%5D) 

##### Land (17)

10 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

40 Cards 

##### Red (1)

1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### Green (8)

1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Devoted Druid](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevoted%5D+%5BDruid%5D) 1 [Hungry Spriggan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHungry%5D+%5BSpriggan%5D) 2 [Nurturer Initiate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNurturer%5D+%5BInitiate%5D) 2 [Farhaven Elf](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFarhaven%5D+%5BElf%5D) 1 [Gleeful Sabotage](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGleeful%5D+%5BSabotage%5D) 

##### Multi colored (11)

2 [Kulrath Knight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKulrath%5D+%5BKnight%5D) 1 [Boggart Ram-Gang](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BRam-Gang%5D) 2 [Mudbrawler Raiders](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbrawler%5D+%5BRaiders%5D) 1 [Rosheen Meanderer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRosheen%5D+%5BMeanderer%5D) 1 [Tattermunge Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTattermunge%5D+%5BDuo%5D) 2 [Barkshell Blessing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarkshell%5D+%5BBlessing%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

##### Colorless (20)

10 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Tatterkite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTatterkite%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 1 [Gnarled Effigy](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGnarled%5D+%5BEffigy%5D) 

40 Cards 

##### 1 (4)

2 [Nurturer Initiate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNurturer%5D+%5BInitiate%5D) 2 [Barkshell Blessing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarkshell%5D+%5BBlessing%5D) 

##### 2 (3)

1 [Devoted Druid](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevoted%5D+%5BDruid%5D) 1 [Gleeful Sabotage](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGleeful%5D+%5BSabotage%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### 3 (8)

1 [Tatterkite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTatterkite%5D) 1 [Hungry Spriggan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHungry%5D+%5BSpriggan%5D) 1 [Boggart Ram-Gang](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BRam-Gang%5D) 1 [Tattermunge Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTattermunge%5D+%5BDuo%5D) 2 [Farhaven Elf](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFarhaven%5D+%5BElf%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

##### 4 (4)

2 [Mudbrawler Raiders](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbrawler%5D+%5BRaiders%5D) 1 [Rosheen Meanderer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRosheen%5D+%5BMeanderer%5D) 1 [Gnarled Effigy](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGnarled%5D+%5BEffigy%5D) 

##### 5 (4)

1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 2 [Kulrath Knight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKulrath%5D+%5BKnight%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 

23 Cards 

##### Common (31)

10 [Forest](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Crabapple Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrabapple%5D+%5BCohort%5D) 1 [Devoted Druid](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDevoted%5D+%5BDruid%5D) 1 [Hungry Spriggan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHungry%5D+%5BSpriggan%5D) 2 [Nurturer Initiate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNurturer%5D+%5BInitiate%5D) 2 [Mudbrawler Raiders](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbrawler%5D+%5BRaiders%5D) 1 [Tattermunge Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTattermunge%5D+%5BDuo%5D) 2 [Farhaven Elf](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFarhaven%5D+%5BElf%5D) 2 [Barkshell Blessing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarkshell%5D+%5BBlessing%5D) 1 [Gleeful Sabotage](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGleeful%5D+%5BSabotage%5D) 1 [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuncture%5D+%5BBolt%5D) 

##### Uncommon (8)

1 [Tatterkite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTatterkite%5D) 2 [Kulrath Knight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKulrath%5D+%5BKnight%5D) 1 [Boggart Ram-Gang](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BRam-Gang%5D) 1 [Rosheen Meanderer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRosheen%5D+%5BMeanderer%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Illuminated Folio](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIlluminated%5D+%5BFolio%5D) 1 [Gnarled Effigy](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGnarled%5D+%5BEffigy%5D) 

##### Mythic (1)

1 [Firespout](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirespout%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Barkshell+Blessing)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hungry+Spriggan)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nurturer+Initiate)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

a:20:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"10";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Tatterkite";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Crabapple Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Devoted Druid";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Hungry Spriggan";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Nurturer Initiate";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Kulrath Knight";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Boggart Ram-Gang";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Mudbrawler Raiders";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Rosheen Meanderer";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Tattermunge Duo";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Farhaven Elf";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Barkshell Blessing";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Mercy Killing";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Firespout";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Gleeful Sabotage";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Puncture Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Illuminated Folio";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Gnarled Effigy";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Gabriel Nassif's green-red deck has a [Puncture Bolt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puncture+Bolt) which is OK, 2 [Kulrath Knight](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kulrath+Knight)s and a [Boggart Ram-Gang](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Ram-Gang), which are OK or very good depending on your deck,and [Gnarled Effigy](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gnarled+Effigy), which is always good.

1 OK  
 3 OK or very good depending on how much toughness and/or [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects your deck has.  
 1 Good

#### Alexandre Peset

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (14)

1 [Lurebound Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLurebound%5D+%5BScarecrow%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 2 [Kithkin Shielddare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKithkin%5D+%5BShielddare%5D) 1 [Resplendent Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BResplendent%5D+%5BMentor%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Plumeveil](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumeveil%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Oona, Queen of the Fae](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOona,%5D+%5BQueen%5D+%5Bof%5D+%5Bthe%5D+%5BFae%5D) 1 [Elvish Hexhunter](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHexhunter%5D) 1 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Scrapbasket](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapbasket%5D) 

##### Sorcery (1)

1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

##### Instant (3)

1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Last Breath](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BBreath%5D) 1 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 

##### Enchantment (4)

1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Puca's Mischief](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuca%5D+%5BMischief%5D) 

##### Land (18)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

40 Cards 

##### White (8)

1 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 2 [Kithkin Shielddare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKithkin%5D+%5BShielddare%5D) 1 [Resplendent Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BResplendent%5D+%5BMentor%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 1 [Last Breath](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BBreath%5D) 1 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 

##### Blue (1)

1 [Puca's Mischief](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuca%5D+%5BMischief%5D) 

##### Multi colored (10)

1 [Plumeveil](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumeveil%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Oona, Queen of the Fae](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOona,%5D+%5BQueen%5D+%5Bof%5D+%5Bthe%5D+%5BFae%5D) 1 [Elvish Hexhunter](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHexhunter%5D) 1 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 

##### Colorless (21)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Lurebound Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLurebound%5D+%5BScarecrow%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Scrapbasket](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapbasket%5D) 

40 Cards 

##### 1 (1)

1 [Elvish Hexhunter](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHexhunter%5D) 

##### 2 (8)

2 [Kithkin Shielddare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKithkin%5D+%5BShielddare%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Last Breath](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BBreath%5D) 1 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 

##### 3 (6)

1 [Lurebound Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLurebound%5D+%5BScarecrow%5D) 1 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 1 [Plumeveil](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumeveil%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### 4 (3)

1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Scrapbasket](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapbasket%5D) 1 [Puca's Mischief](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuca%5D+%5BMischief%5D) 

##### 5 (2)

1 [Resplendent Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BResplendent%5D+%5BMentor%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 

##### 6 (2)

1 [Oona, Queen of the Fae](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOona,%5D+%5BQueen%5D+%5Bof%5D+%5Bthe%5D+%5BFae%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

22 Cards 

##### Common (34)

9 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 2 [Kithkin Shielddare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKithkin%5D+%5BShielddare%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Elvish Hexhunter](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHexhunter%5D) 1 [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BElite%5D) 1 [Scrapbasket](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapbasket%5D) 1 [Shield of the Oversoul](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShield%5D+%5Bof%5D+%5Bthe%5D+%5BOversoul%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Last Breath](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BBreath%5D) 1 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 

##### Uncommon (4)

1 [Lurebound Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLurebound%5D+%5BScarecrow%5D) 1 [Resplendent Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BResplendent%5D+%5BMentor%5D) 1 [Plumeveil](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumeveil%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

##### Rare (2)

1 [Oona, Queen of the Fae](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOona,%5D+%5BQueen%5D+%5Bof%5D+%5Bthe%5D+%5BFae%5D) 1 [Puca's Mischief](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPuca%5D+%5BMischief%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Last+Breath)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oona%2C+Queen+of+the+Fae)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lurebound+Scarecrow)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kithkin+Shielddare)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)

a:23:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Lurebound Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Watchwing Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ballynock Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Kithkin Shielddare";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Resplendent Mentor";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Safehold Sentry";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Plumeveil";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Silkbind Faerie";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Gravelgill Axeshark";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Oona, Queen of the Fae";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Elvish Hexhunter";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Safehold Elite";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Scrapbasket";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Shield of the Oversoul";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Turn to Mist";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Steel of the Godhead";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Curse of Chains";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Puca's Mischief";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Spectral Procession";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Last Breath";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Inquisitor's Snare";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Alexandre Peset's white-blue deck has a [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) and a [Safehold Elite](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), which make things slightly better, but no cards that generate -1-1 counters on their own.

2 Persist

#### Kamiel Cornelissen

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (17)

1 [Lockjaw Snapper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLockjaw%5D+%5BSnapper%5D) 1 [Scuttlemutt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScuttlemutt%5D) 1 [Isleback Spawn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsleback%5D+%5BSpawn%5D) 1 [Cinderbones](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCinderbones%5D) 1 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 2 [Loch Korrigan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoch%5D+%5BKorrigan%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Cemetery Puca](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCemetery%5D+%5BPuca%5D) 1 [Ghastlord of Fugue](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastlord%5D+%5Bof%5D+%5BFugue%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Inkfathom Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BWitch%5D) 1 [Sygg, River Cutthroat](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSygg,%5D+%5BRiver%5D+%5BCutthroat%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Grief Tyrant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrief%5D+%5BTyrant%5D) 1 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 

##### Instant (4)

1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 2 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 

##### Enchantment (2)

1 [Helm of the Ghastlord](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHelm%5D+%5Bof%5D+%5Bthe%5D+%5BGhastlord%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 

##### Land (17)

1 [Sunken Ruins](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 7 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

40 Cards 

##### Blue (3)

1 [Isleback Spawn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsleback%5D+%5BSpawn%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 

##### Black (7)

1 [Cinderbones](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCinderbones%5D) 1 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 2 [Loch Korrigan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoch%5D+%5BKorrigan%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 2 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 

##### Multi colored (11)

1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Cemetery Puca](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCemetery%5D+%5BPuca%5D) 1 [Ghastlord of Fugue](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastlord%5D+%5Bof%5D+%5BFugue%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Inkfathom Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BWitch%5D) 1 [Sygg, River Cutthroat](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSygg,%5D+%5BRiver%5D+%5BCutthroat%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Grief Tyrant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrief%5D+%5BTyrant%5D) 1 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Helm of the Ghastlord](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHelm%5D+%5Bof%5D+%5Bthe%5D+%5BGhastlord%5D) 

##### Colorless (19)

1 [Sunken Ruins](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 7 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Lockjaw Snapper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLockjaw%5D+%5BSnapper%5D) 1 [Scuttlemutt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScuttlemutt%5D) 

40 Cards 

##### 1 (4)

1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 2 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 

##### 2 (2)

1 [Inkfathom Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BWitch%5D) 1 [Sygg, River Cutthroat](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSygg,%5D+%5BRiver%5D+%5BCutthroat%5D) 

##### 3 (7)

1 [Scuttlemutt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScuttlemutt%5D) 1 [Cinderbones](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCinderbones%5D) 1 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Cemetery Puca](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCemetery%5D+%5BPuca%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 

##### 4 (5)

1 [Lockjaw Snapper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLockjaw%5D+%5BSnapper%5D) 2 [Loch Korrigan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoch%5D+%5BKorrigan%5D) 1 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Helm of the Ghastlord](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHelm%5D+%5Bof%5D+%5Bthe%5D+%5BGhastlord%5D) 

##### 5 (3)

1 [Ghastlord of Fugue](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastlord%5D+%5Bof%5D+%5BFugue%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 

##### 6 (1)

1 [Grief Tyrant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrief%5D+%5BTyrant%5D) 

##### 7 (1)

1 [Isleback Spawn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsleback%5D+%5BSpawn%5D) 

23 Cards 

##### Common (30)

7 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Cinderbones](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCinderbones%5D) 1 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 2 [Loch Korrigan](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoch%5D+%5BKorrigan%5D) 1 [Silkbind Faerie](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilkbind%5D+%5BFaerie%5D) 1 [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGravelgill%5D+%5BAxeshark%5D) 1 [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCultbrand%5D+%5BCinder%5D) 1 [Sootwalkers](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSootwalkers%5D) 1 [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScar%5D) 1 [Helm of the Ghastlord](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHelm%5D+%5Bof%5D+%5Bthe%5D+%5BGhastlord%5D) 1 [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorture%5D) 2 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 

##### Uncommon (5)

1 [Lockjaw Snapper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLockjaw%5D+%5BSnapper%5D) 1 [Scuttlemutt](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScuttlemutt%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Inkfathom Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkfathom%5D+%5BWitch%5D) 1 [Grief Tyrant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrief%5D+%5BTyrant%5D) 

##### Rare (4)

1 [Isleback Spawn](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsleback%5D+%5BSpawn%5D) 1 [Cemetery Puca](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCemetery%5D+%5BPuca%5D) 1 [Ghastlord of Fugue](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastlord%5D+%5Bof%5D+%5BFugue%5D) 1 [Sygg, River Cutthroat](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSygg,%5D+%5BRiver%5D+%5BCutthroat%5D) 

##### Mythic (1)

1 [Sunken Ruins](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sunken+Ruins)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cinderbones)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Inkfathom+Witch)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Silkbind+Faerie)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Isleback+Spawn)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:24:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Sunken Ruins";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Lockjaw Snapper";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Scuttlemutt";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Isleback Spawn";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Cinderbones";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Faerie Macabre";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Loch Korrigan";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Leech Bonder";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Silkbind Faerie";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Cemetery Puca";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Ghastlord of Fugue";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Gravelgill Axeshark";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Inkfathom Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Sygg, River Cutthroat";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Cultbrand Cinder";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Grief Tyrant";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Sootwalkers";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:4:"Scar";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Helm of the Ghastlord";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Torture";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Aphotic Wisps";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Consign to Dream";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Kamiel Cornelissen's winning blue-black deck has a [Gravelgill Axeshark](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) to make things slightly better, a [Scar](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scar) and a [Grief Tyrant](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grief+Tyrant) which are OK, a [Torture](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torture) and a [Cultbrand Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultbrand+Cinder) which are good and a [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leech+Bonder) and a [Lockjaw Snapper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lockjaw+Snapper) which are very good.

1 Persist  
 2 OK  
 2 Good  
 2 Very good

#### Gaetan Lefebvre

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (14)

1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Faerie Swarm](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BSwarm%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Knacksaw Clique](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnacksaw%5D+%5BClique%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Whimwader](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhimwader%5D) 1 [Midnight Banshee](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMidnight%5D+%5BBanshee%5D) 2 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 1 [Swans of Bryn Argoll](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwans%5D+%5Bof%5D+%5BBryn%5D+%5BArgoll%5D) 1 [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSickle%5D+%5BRipper%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Manaforge Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManaforge%5D+%5BCinder%5D) 1 [Murderous Redcap](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BRedcap%5D) 

##### Sorcery (4)

2 [Scarscale Ritual](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarscale%5D+%5BRitual%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 1 [Ghastly Discovery](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastly%5D+%5BDiscovery%5D) 

##### Instant (3)

1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 

##### Land (17)

8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

##### Other (2)

2 Aethertow 

40 Cards 

##### Blue (8)

1 [Faerie Swarm](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BSwarm%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Knacksaw Clique](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnacksaw%5D+%5BClique%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Whimwader](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhimwader%5D) 1 [Ghastly Discovery](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastly%5D+%5BDiscovery%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 

##### Black (6)

1 [Midnight Banshee](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMidnight%5D+%5BBanshee%5D) 2 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 1 [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSickle%5D+%5BRipper%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 

##### Multi colored (6)

1 [Swans of Bryn Argoll](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwans%5D+%5Bof%5D+%5BBryn%5D+%5BArgoll%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Manaforge Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManaforge%5D+%5BCinder%5D) 1 [Murderous Redcap](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BRedcap%5D) 2 [Scarscale Ritual](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarscale%5D+%5BRitual%5D) 

##### Colorless (20)

8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 2 Aethertow 

40 Cards 

##### 1 (3)

1 [Manaforge Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManaforge%5D+%5BCinder%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 

##### 2 (3)

1 [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSickle%5D+%5BRipper%5D) 2 [Scarscale Ritual](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarscale%5D+%5BRitual%5D) 

##### 3 (6)

1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 2 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Ghastly Discovery](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastly%5D+%5BDiscovery%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 

##### 4 (6)

1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Faerie Swarm](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BSwarm%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Knacksaw Clique](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnacksaw%5D+%5BClique%5D) 1 [Swans of Bryn Argoll](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwans%5D+%5Bof%5D+%5BBryn%5D+%5BArgoll%5D) 1 [Murderous Redcap](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BRedcap%5D) 

##### 5 (2)

1 [Whimwader](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhimwader%5D) 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 

##### 6 (1)

1 [Midnight Banshee](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMidnight%5D+%5BBanshee%5D) 

21 Cards 

##### Common (33)

8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Swamp](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Watchwing Scarecrow](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwing%5D+%5BScarecrow%5D) 1 [Kinscaer Harpoonist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKinscaer%5D+%5BHarpoonist%5D) 1 [Whimwader](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhimwader%5D) 2 [Faerie Macabre](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BMacabre%5D) 1 [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSickle%5D+%5BRipper%5D) 1 [Manaforge Cinder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManaforge%5D+%5BCinder%5D) 2 [Scarscale Ritual](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScarscale%5D+%5BRitual%5D) 2 Aethertow 1 [Gloomlance](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGloomlance%5D) 1 [Aphotic Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAphotic%5D+%5BWisps%5D) 1 [Ghastly Discovery](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhastly%5D+%5BDiscovery%5D) 1 [Consign to Dream](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConsign%5D+%5Bto%5D+%5BDream%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 

##### Uncommon (4)

1 [Faerie Swarm](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BSwarm%5D) 1 [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeech%5D+%5BBonder%5D) 1 [Ashenmoor Gouger](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAshenmoor%5D+%5BGouger%5D) 1 [Murderous Redcap](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BRedcap%5D) 

##### Rare (3)

1 [Knacksaw Clique](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnacksaw%5D+%5BClique%5D) 1 [Midnight Banshee](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMidnight%5D+%5BBanshee%5D) 1 [Swans of Bryn Argoll](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwans%5D+%5Bof%5D+%5BBryn%5D+%5BArgoll%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Swarm)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Knacksaw+Clique)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leech+Bonder)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

a:22:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Watchwing Scarecrow";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Faerie Swarm";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Kinscaer Harpoonist";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Knacksaw Clique";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Leech Bonder";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Whimwader";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Midnight Banshee";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Faerie Macabre";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Swans of Bryn Argoll";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sickle Ripper";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ashenmoor Gouger";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Manaforge Cinder";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Murderous Redcap";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Scarscale Ritual";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Gloomlance";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Aphotic Wisps";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Ghastly Discovery";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Consign to Dream";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Cerulean Wisps";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Gaetan Lefebvre's blue-black deck has a [Murderous Redcap](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) to make things better, 2 [Scarscale Ritual](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scarscale+Ritual), and a [Sickle Ripper](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickle+Ripper), which are good, and a [Midnight Banshee](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Midnight+Banshee) and a [Leech Bonder](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leech+Bonder), which are very good.

1 Persist  
 3 Good  
 2 Very good

#### Raphael Levy

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (13)

2 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Deepchannel Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeepchannel%5D+%5BMentor%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 2 [Barrenton Cragtreads](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarrenton%5D+%5BCragtreads%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Somnomancer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSomnomancer%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 1 [Zealous Guardian](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZealous%5D+%5BGuardian%5D) 1 [Glen Elendra Liege](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BLiege%5D) 

##### Sorcery (1)

1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

##### Instant (6)

1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 2 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 1 [Niveous Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNiveous%5D+%5BWisps%5D) 

##### Enchantment (3)

1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 

##### Land (17)

1 [Mystic Gate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BGate%5D) 8 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

40 Cards 

##### White (7)

2 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 2 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 1 [Niveous Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNiveous%5D+%5BWisps%5D) 

##### Blue (4)

2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Deepchannel Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeepchannel%5D+%5BMentor%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 

##### Multi colored (12)

2 [Barrenton Cragtreads](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarrenton%5D+%5BCragtreads%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Somnomancer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSomnomancer%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 1 [Zealous Guardian](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZealous%5D+%5BGuardian%5D) 1 [Glen Elendra Liege](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BLiege%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 

##### Colorless (17)

1 [Mystic Gate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BGate%5D) 8 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

40 Cards 

##### 1 (3)

1 [Zealous Guardian](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZealous%5D+%5BGuardian%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 1 [Niveous Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNiveous%5D+%5BWisps%5D) 

##### 2 (9)

2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Somnomancer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSomnomancer%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 2 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 

##### 3 (6)

2 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### 4 (3)

2 [Barrenton Cragtreads](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarrenton%5D+%5BCragtreads%5D) 1 [Glen Elendra Liege](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BLiege%5D) 

##### 6 (2)

1 [Deepchannel Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeepchannel%5D+%5BMentor%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

23 Cards 

##### Common (34)

8 [Plains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 8 [Island](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Ballynock Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBallynock%5D+%5BCohort%5D) 2 [Briarberry Cohort](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBriarberry%5D+%5BCohort%5D) 1 [Safehold Sentry](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafehold%5D+%5BSentry%5D) 2 [Barrenton Cragtreads](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBarrenton%5D+%5BCragtreads%5D) 1 [Somnomancer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSomnomancer%5D) 1 [Thistledown Duo](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThistledown%5D+%5BDuo%5D) 1 [Zealous Guardian](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZealous%5D+%5BGuardian%5D) 1 [Torpor Dust](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorpor%5D+%5BDust%5D) 1 [Turn to Mist](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BMist%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Curse of Chains](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCurse%5D+%5Bof%5D+%5BChains%5D) 1 [Cerulean Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCerulean%5D+%5BWisps%5D) 2 [Inquisitor's Snare](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInquisitor%5D+%5BSnare%5D) 1 [Niveous Wisps](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNiveous%5D+%5BWisps%5D) 

##### Uncommon (4)

1 [Deepchannel Mentor](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeepchannel%5D+%5BMentor%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Mercy Killing](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMercy%5D+%5BKilling%5D) 1 [Spectral Procession](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpectral%5D+%5BProcession%5D) 

##### Rare (1)

1 [Glen Elendra Liege](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BLiege%5D) 

##### Mythic (1)

1 [Mystic Gate](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BGate%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mystic+Gate)

[Deal Another Hand](https://web.archive.org/web/20080513000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Glen+Elendra+Liege)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ballynock+Cohort)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Steel+of+the+Godhead)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Barrenton+Cragtreads)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Inquisitor%27s+Snare)

a:22:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Mystic Gate";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ballynock Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Briarberry Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Deepchannel Mentor";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Safehold Sentry";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Barrenton Cragtreads";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Mistmeadow Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Somnomancer";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Thistledown Duo";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Zealous Guardian";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Glen Elendra Liege";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Mercy Killing";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Torpor Dust";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Turn to Mist";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Steel of the Godhead";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Curse of Chains";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Cerulean Wisps";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Spectral Procession";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Inquisitor's Snare";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Niveous Wisps";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Raphael Levy's white-blue deck has no cards that aid [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer).

### What Does It Take for Me to Play [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer)?

![Barkshell Blessing](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Barkshell+Blessing)

Without having any cards to aid [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) on my own I would want to have [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) against Gaeten Lefebvre's deck, Kamiel Cornellissen's deck, and Rojier Kleji's deck all the time, and Gabriel Nassif's deck and Holger Lange's if I had a lot of [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)s or 4+ toughness creatures.

In light of the anecdotal evidence that I found by looking at the Top 8 of GP–Brussels, I would feel comfortable playing [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) in my main deck if I had as little as 1 [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effect (for the big green wither creatures), three cards that are OK with [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), such as creatures with persist, and one card that is very good with [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), such as [Chainbreaker](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chainbreaker). 

Interestingly enough, having [Giant Growth](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects raises the value of [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer) considerably, as they make your [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer)s way better against high-power green creatures with wither.

Hopefully you'll excuse me for spending so much time talking about [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), but I think it is one of the most interesting and difficult to evaluate cards in the format. Sure, sometimes it will fit into your deck like a glove, but a lot of times I think that it would be a good inclusion in decks that it might not look that impressive in.

### Misunderstandings

I've told you how I feel about [Fate Transfer](https://web.archive.org/web/20080513000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Transfer), but I want to know: which *Shadowmoor* cards do you think are misunderstood and either undervalued, overvalued or both as a result?