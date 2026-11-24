---
id: p6210jvs
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/09-05-delving-the-pits
title: Delving the Pits
published: '2014-09-05'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    lang_detected: en
    capture_id: 300712
    url: http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    captured_at: '2016-09-06 02:01:38+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    lang_detected: en
    capture_id: 300712
    url: http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    captured_at: '2016-09-06 02:01:38+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    lang_detected: en
    capture_id: 300712
    url: http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
    captured_at: '2016-09-06 02:01:38+00'
    rule: drupal.div_author
sources:
- document_id: p6210jvs
  url: http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
  page_key: magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
  lang: en
  template: drupal
  captured_at: '2016-09-06 02:01:38+00'
  capture_id: 300712
  wayback_url: https://web.archive.org/web/20160906020138id_/http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: p6210jvs
  capture_id: 300712
  url: http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
  wayback_url: https://web.archive.org/web/20160906020138id_/http://magic.wizards.com/en/articles/archive/delving-pits-2014-09-05
  captured_at: '2016-09-06 02:01:38+00'
  template: drupal
  sha256: d98edd1a8c8a92937fc99afda601ac79396bf43b2d9da4c45427d85db2406fa3
render_recovery: []
---
This week on Latest Developments, I have an exciting preview card for you—one that uses one of the set's returning mechanics, delve. Before I show off the card, though, I want to talk about the origins of delve in *Khans of Tarkir*, and how we used that to create the card I will preview today.

# The Origins of Delve in Tarkir

Getting the right mechanic for the Sultai was difficult. One of the major mechanics talked about in design was Gold tokens. The Sultai were rich, and the idea is that they would accumulate Gold, which they could spend to go over the top of their opponents. The plan was to make them a controlling color pair and win games through their ability to generate more resources than their opponents.

![](https://i.ormos.uk/0a/52/0a52012997f8603f2aa57e5bb4e585bbbf158363d39b4f27f082b64f1fb83f11.jpg)

This plan of design's caused some problems for development. First off, the Gold token mechanic has been talked about many times and never used, but it did appear on one card in *Born of the Gods*, as well as a card in *Journey into Nyx*. Because we were introducing a Gold token for the first time with that set, we would want this set to use Gold in the same way. That meant we would have to lock down the mechanic incredibly early—if we went with it.

The second problem with Gold is that development was very wary about counters that made mana of any color in a wedge set. What we worried would end up happening was that we would have four three-color wedge clans and one five-color clan. Development was pretty sure that if the Sultai made tokens, those would need to make colorless mana. And all of a sudden, we have a mechanic that looks almost identical to the Spawn tokens in *Rise of the Eldrazi*. In fact, many of the designers and developers who were still around from when that set was being worked on remarked about how similar the two paths for the mechanics were.

![](http://archive.wizards.com/mtg/images/daily/arcana/421_spawn1.jpg)

In the end, development highly recommended to design to kill Gold, and it did. I wouldn't be surprised to see the mechanic rear its head again in the future, but it will probably not be in a gold set. Or, at the least, it will be one of the primary mechanics of the gold set, not limited to one faction. I believe that Gold generating mana of any color is correct, and would be a good use for the primary color-fixing mechanic for Limited in a set, but there has to be some color balance for the mechanic.

In any case, this left us in need of a mechanic for Sultai. Erik Lauer, who would be the lead developer for the set, realized that black-green-blue was perfect for a graveyard mechanic, since that is the natural overlap for those three colors, and the set didn't have one set up yet. The first thought he had was to look at delve, a mechanic that players had expressed interest in, and one we knew we could create exciting Constructed cards out of. Fortunately, creative had already imagined the Sultai would use legions of undead as servants, so the creative fit of delve being their resource mechanic made perfect sense.

![](http://media.wizards.com/images/magic/daily/ld/2014/cardart_cg9861cdt7.jpg)

 Art by [Ryan Alexander Lee](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Ryan+Alexander+Lee%22%5D)

# Developing a Finisher

Once delve was in the set, it was time to find the best ways to use the mechanic. I think *Future Sight* did a pretty good job of highlighting the most interesting delve cards: a fatty, a removal spell, and an X spell. We had to do a lot more cards than just that, though, if we wanted to fill out the slots needed for the mechanic in a large set. We needed to figure out how to put it on basic Limited commons and splashy rares. All of this while getting the cards to the point where they were castable without a full graveyard, but not too strong if you fill up your graveyard quickly.

One thing we are always looking for in *Magic* is control finishers. They are good if they can be varied—after all, we don't want all of our games finishing in the same way—and if they can be both expensive and flexible enough that players will have some options when choosing between them. [Ætherling](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therling), as an example, was the finisher we put in *Dragon's Maze*, which was there to encourage blue decks to have counterspells and to let games end once the creature hit play.

We don't want all of our finishers to be big blue creatures, though. We want some variety. For this card, we wanted something that would reward blue-black control decks, not the white-blue ones that have been dominating Standard for the past year. We also wanted something that could be cast as an instant, and in this case to act in a similar way to [Sphinx's Revelation](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) in giving the control decks a good reason to play instants and not just be tap-out control. But, enough teasing, let me introduce you to Empty the Pits:

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_cg9861cdt7.png)

The card comes at quite a cost—it takes six mana to generate your first zombie—but it scales very well. Control players of yesteryear might even recognize something very familiar about this card: it scales in a very similar way to [Psychatog](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog). Although you can't discard cards from your hand to fuel Empty the Pits, you actually get a much better deal on Zombies from Empty the Pits than you did for power with [Psychatog](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog).

In a long control-on-control game, it is very easy for graveyards to fill up, and provide fuel for Empty the Pits. This card lets you heavily punish an opponent for tapping out by letting you flood the board with more than enough attackers to take someone from 20 to 0. Creating ten tokens takes twenty-four mana. It may seem like an impossible feat, but I can tell you that it isn't. There are more than enough ways in *Khans of Tarkir* to get some cards in your graveyard, and since there will no longer be an [uncounterable board sweeper](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Supreme+Verdict) in Standard, it is possible for a control deck to protect whatever Zombies are left after the first attack.

# Fill The Pits

Of course, what is a pit without something to throw in it? Much like the decadent leaders of the Sultai clan, it's important to have enough bodies to step on in order to make your power. Well, metaphorical bodies. We don't actually need to eat bodies out of the pits—anything will do. That means that Empty the Pits will work great with spells that let you draw and discard cards, or even just cards like [Commune with the Gods](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Commune+with+the+Gods) that will end up putting more cards in your graveyard. Commune itself puts two-and-a-half Zombies into the 'yard if you find a creature and three if you don't. If you don't want to go too out of your way to fill up your graveyard, you can always get incidental graveyard filling by just playing your standard game plan as a control deck, starting turn one with a card I expect to be pretty popular.

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_gxump3gx5a.png%20)

That's an easy one. Much like how [Grim Lavamancer](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Lavamancer) used [fetch lands](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&text=+%5Bsearch%5D+%5Byour%5D+%5Blibrary%5D&set=%7C%5B%22Onslaught%22%5D%7C%5B%22Mirage%22%5D%7C%5B%22Zendikar%22%5D) to power up his abilities, the fetch lands in Khans help power up delve by giving you fast and easy cards to delve away.

As an aside, [Tome Scour](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tome+Scour) was originally in *Magic 2015* instead of [Mind Sculpt](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sculpt). After playing games with Empty the Pits at a more aggressive cost, we swapped the cards to make sure it wasn't too easy to power out huge delve spells on turn three or four. We did leave one card in that we knew would help a lot, though. When it comes to actually casting Empty the Pits, there is a card in *Magic 2015* that you might want to consider playing as a one-of in your control decks.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Urborg,%20Tomb%20of%20Yawgmoth)](https://web.archive.org/web/20140905000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg,%20Tomb%20of%20Yawgmoth)

While we didn't put Urborg into *Magic 2015* to interact with Empty the Pits, we found that it let us add extra colored costs to the spell without the fear of making it uncastable in Standard, for at least the first year, and let us keep the cost at simply ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) (yes, we did investigate ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)) without worrying about the card being a dominant force in Standard for its entire lifespan.

That's all I have for this week. I don't have a preview card for next week—the entire set will be live on our site, so instead I will go over the development team for the set and tell some stories from the development of *Khans of Tarkir*.

Until next time,

Sam ([@samstod](https://twitter.com/samstod))