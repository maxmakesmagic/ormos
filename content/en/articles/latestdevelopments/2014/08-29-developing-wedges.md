---
id: ksjhtzb5
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/08-29-developing-wedges
title: Developing Wedges
published: '2014-08-29'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    lang_detected: en
    capture_id: 737644
    url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    captured_at: '2016-05-08 07:22:16+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    lang_detected: en
    capture_id: 737644
    url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    captured_at: '2016-05-08 07:22:16+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    lang_detected: en
    capture_id: 737644
    url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    captured_at: '2016-05-08 07:22:16+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    lang_detected: en
    capture_id: 737644
    url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
    captured_at: '2016-05-08 07:22:16+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: ksjhtzb5
  url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
  page_key: magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
  lang: en
  template: drupal
  captured_at: '2016-05-08 07:22:16+00'
  capture_id: 737644
  wayback_url: https://web.archive.org/web/20160508072216id_/http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ksjhtzb5
  capture_id: 737644
  url: http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
  wayback_url: https://web.archive.org/web/20160508072216id_/http://magic.wizards.com/en/articles/archive/ld/developing-wedges-2014-08-29
  captured_at: '2016-05-08 07:22:16+00'
  template: drupal
  sha256: 901a8eb323061a321e60c88886907c30a4fd5b22d074f347a91229df551978ea
render_recovery: []
---
For Wedge Week, I wanted to talk about some of the successes and failures we have had with wedges in the past. I hope that if you are in Seattle this weekend, you try to attend the PAX party, where you will get an opportunity to see the unveiling of many cards from *Khans of Tarkir*. And if you're not, stay glued to social media Saturday night—there will be a lot of very exciting cards to preview.

The Problem with Wedges

One of the hardest parts of making a wedge set like *Khans of Tarkir* is that there isn't a ton of design space in many of the three-color combinations. The enemy colors are generally best defined by what they are not, as compared to each other, so putting one color with its two enemies doesn't lead to natural designs like shards do. Not that the shard cards were all perfect, but figuring out what one primary color has in common with two secondary colors is a much easier exercise than figuring out how to make wedge cards.

![](http://media.wizards.com/images/magic/daily/ld/2014/ktkwedge.gif)

Creating wedge cards can quickly become a box-checking exercise, if you aren't careful. Want to make a wedge card? Take a creature with pretty regular stats and give it one keyword from each color. [Lightning Angel](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Angel), for example, falls into this category—a flying (blue), haste (red), and vigilance (white) 3/4 for four mana. Making a few cards like this is acceptable, but it's not something we wanted to build an entire set around. Development didn't want to get into a situation where we couldn't change the cards we were given from design, ether because no more keywords existed or because the design space was too limited.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning%20Angel)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning%20Angel)

One solution that we hit upon, and that Mark Rosewater and the design team were happy with, was making sure that our wedge cards first and foremost felt like they belonged in their respective clans. Shards actually hit upon this same thing, as they needed to make three sets with shard cards, and finding that much design space was also difficult. They definitely stretched some cards by using the flavor and mechanics of each shard to make them work, but I think they were (overall) very successful. Exalted on a blue creature wasn't the most intuitive thing from a flavor perspective, but it worked as part of the total package. I believe Khans was more than able to find satisfying places for its wedge cards by using that criteria, and I am excited for you to start seeing them very soon.

Planting Seeds for Khans

Getting Khans to work required some planning for us beforehand. The cards I got to preview from *Magic 2015* were the enemy-color [pain lands](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&text=+%5B%22deals+1+damage+to+you%22%5D&set=+%5B%22Magic%202015%20Core%20Set%22%5D). I saw many players guess correctly that this was a plant for a wedge set in *Khans of Tarkir*.

Unlike most sets, where our plants are focused around cards that can boost us synergies in the upcoming set, what we needed for *Khans of Tarkir* block was a way to print some cards that could make sure that people were able to cast their spells reliably. What we found in our initial testing of *Khans of Tarkir* Standard was that the [*Innistrad* duals](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&set=+%5B%22Innistrad%22%5D&text=+%5Btapped%5D+%5Bunless%5D) were pushing people toward playing two-color decks instead of the wedge decks we were hoping for, because too many lands entered the battlefield tapped. We knew we would want to print a lot of powerful cards at costs like ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) and ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), but if they couldn't be cast until turn four, they just weren't doing their job. The green decks in particular got some amazing turn-two plays, in theory—but actually casting their cards on turn two turned out to be way too hard, and if we tried to adjust the power level to make up for that, we were going to end up with creatures that would be far too frustrating to play against when they did enter on that turn.

![](http://media.wizards.com/2014/images/cardart/cardart_burley.jpg)

Art by [Sam Burley](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Sam%20Burley%22%5D)

The pain lands do the job we were hoping for: you can run eight in a wedge-colored deck, but there will be the downside of occasionally having to pay a lot of life to cast your spells. Most decks will be more than willing to make this tradeoff, but we didn't want to make this kind of thing free. This lets Khans create wedges that are all capable of showing up in Standard, while at the same time not making it a "play a wedge or lose" proposition.

Looking Back on Wedge Successes and Failures

For this, I want to focus on just the cards we've printed in booster packs. The Commander and *Planechase* wedge cards do, on a whole, a better job of conveying what *Khans of Tarkir* is going for with wedges by making the cards make sense as a package, rather than trying to convince you where each color starts and ends.

*Apocalypse*'s Wedge Cycle—*Apocalypse* was all about enemy colors, which meant the introduction of the first wedge cards. It was here that we got the names Ana, Dega, Raka, Necra, and Ceta. (I'll be honest—I will be really happy if the Khans names of Mardu, Jeskai, Abzan, Temur, and Sultai erase those other names from history.) There were a lot of cards that encouraged you to play these three-color decks, like the [Sanctuaries](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5B%22Sanctuary%22%5D&set=+%5B%22Apocalypse%22%5D) or the [-volvers](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5B%22volver%22%5D&set=+%5B%22Apocalypse%22%5D) , but only five actual wedge cards in the set:

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning%20Angel)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning%20Angel)

[Lightning Angel](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Angel)—This card is acceptable, but is somewhat boring. It is powerful, but not in a way that is interesting. It is analogous to a card like [Woolly Thoctar](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar)—a fine uncommon, but not what I would expect out of a rare.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Overgrown%20Estate)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overgrown%20Estate)

[Overgrown Estate](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overgrown+Estate)—Now, this is a somewhat better way to do a wedge card, but it does have some serious execution problems. It's not perfect, but it takes a card that makes sense in black-green ([Dark Heart of the Wood](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Heart+of+the+Wood)), and expands it into being able to sac any land. Pay no attention to the fact that this is basically [Zuran Orb](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zuran+Orb), though.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Guided%20Passage)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guided%20Passage)

[Guided Passage](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guided+Passage)—This card is a hot mess. GUR is hard because green is so heavily a creature color, but blue and red are not. This throws in enough weirdness that it's possible to buy the color combinations, but not if you look too hard.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fervent%20Charge)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fervent%20Charge)

[Fervent Charge](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fervent+Charge)—Another design that plays up the idea that red, white, and black creature decks tend to go wide. It works, but not as satisfyingly as I would like, although making it an attack trigger goes a long way to selling the colors. Adding a keyword or two, and maybe scaling back on the power and toughness bonus, would've gone a long way for me.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fungal%20Shambler)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fungal%20Shambler)

[Fungal Shambler](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fungal+Shambler)—this is a noble attempt. Blue and black both make sense as saboteur colors at the time, and green has gotten a lot more since the printing of this card. B-

The *Planar Chaos* Dragons—part of the gimmick of *Planar Chaos* was that it was an "alternative-reality" version of *Magic*, with a lot of cards that were color shifted to show off this theme. It made a lot of sense to take what were probably the most iconic shard creatures at that time—the [*Invasion* Dragons](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&subtype=+%5B%22Dragon%22%5D&type=+%5B%22Legendary%22%5D&set=+%5B%22Invasion%22%5D)—and [turn them into wedge colors](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&subtype=+%5B%22Dragon%22%5D&type=+%5B%22Legendary%22%5D&set=+%5B%22Planar+Chaos%22%5D).

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oros,%20the%20Avenger)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oros,%20the%20Avenger)

[Oros, the Avenger](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oros%2C+the+Avenger)—Flavor goes a long way here, for me. Sparing white creates makes this feel like a card that couldn't exist in black or red alone, and therefore sells the package to me, at least.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Numot,%20the%20Devastator)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Numot,%20the%20Devastator)

[Numot, the Devastator](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Numot%2C+the+Devastator)—I can't say enough bad things about Numot. Besides land destruction not being very fun, and sticking an ability that can be either game-winning or useless on a six-drop Dragon, I actually yearn for the days where [Lightning Angel](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Angel) was the right intersection.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Intet,%20the%20Dreamer)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intet,%20the%20Dreamer)

[Intet, the Dreamer](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intet%2C+the+Dreamer)—Oddly enough, I feel like Intet feels more of a RUG card today than when it was printed, due to putting the [Elkin Bottle](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) text onto more and more red cards.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vorosh,%20the%20Hunter)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vorosh,%20the%20Hunter)

[Vorosh, the Hunter](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vorosh%2C+the+Hunter)—Other than the fact that this card flies, it could be mono-green. I wish there was something else on this card that gave the blue and black elements some weight.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Teneb,%20the%20Harvester)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teneb,%20the%20Harvester)

[Teneb, the Harvester](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teneb%2C+the+Harvester)—The downside of Teneb is that he is pretty close to being a mono-black card. On the plus side, the ability makes a lot of sense in the colors that it has been assigned.

*Lorwyn*—*Lorwyn*'s tribes were unbalanced in terms of color, which was pretty interesting. Treefolk were in the interesting spot of being the only tribe in three colors—white-black-green—and therefore contained the only actual wedge card in the block.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Doran,%20the%20Siege%20Tower)](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doran,%20the%20Siege%20Tower)

[Doran, the Siege Tower](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doran%2C+the+Siege+Tower)—Doran may be the best wedge card we have designed, at least up until *Khans of Tarkir*. Instead of picking something obvious, Doran points out that white, black, and green creatures tend to have more toughness than average, and he gives those creatures the bonus of dealing damage equal to that number. He was popular because you could build decks around him (getting a huge advantage from having cheap creatures with high toughness), but he also worked great as a commander—or even by himself, as a 5/5.

*Khans of Tarkir*

Zurgo, Helmsmasher—The only card so far revealed from *Khans of Tarkir*, Zurgo shows off our current thinking on how to get wedges to work in modern-day *Magic*. Zurgo, in my opinion, feels very much like the Mardu horde. My favorite part of him is one that I actually suggested early on in development. A common complaint about [Sengir Vampire](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sengir+Vampire) text is that it never actually happens. Either the creature isn't chump blocked, or it is blocked by a creature large enough to kill it. Zurgo gets around that by being large enough that chump blocking is a good idea, but not so large that your opponent can't try and deal with him on the next turn. It sets him up in the perfect spot for the text not only to happen, but also often to matter, as going up to 3 toughness removes him from being vulnerable to many forms of removal you see in Standard, such as [Magma Jet](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magma+Jet) and [Magma Spray](https://web.archive.org/web/20140829000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magma+Spray).

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_y11uj54lgh.png)

That's it for this week. Next week, I'm back with a pretty exciting preview card, one that I am almost positive will make a splash in Standard, despite its pretty steep cost—![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif). What could this card be? Come back next week to find out.

Until next time,  
 Sam ([@samstod](https://twitter.com/samstod))