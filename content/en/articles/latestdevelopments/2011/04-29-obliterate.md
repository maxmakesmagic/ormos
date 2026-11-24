---
id: p7e48z7d
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/04-29-obliterate
title: Obliterate!
published: '2011-04-29'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    lang_detected: en
    capture_id: 729360
    url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    captured_at: '2022-10-03 01:05:50+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    lang_detected: en
    capture_id: 729360
    url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    captured_at: '2022-10-03 01:05:50+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    lang_detected: en
    capture_id: 729360
    url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    captured_at: '2022-10-03 01:05:50+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    lang_detected: en
    capture_id: 729360
    url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
    captured_at: '2022-10-03 01:05:50+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: p7e48z7d
  url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
  page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
  lang: en
  template: drupal
  captured_at: '2022-10-03 01:05:50+00'
  capture_id: 729360
  wayback_url: https://web.archive.org/web/20221003010550id_/https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
- document_id: p7e48z7d
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/140
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/140
  lang: en
  template: aspx
  captured_at: '2013-07-02 02:19:09+00'
  capture_id: 613196
  wayback_url: https://web.archive.org/web/20130702021909id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/140
- document_id: p7e48z7d
  url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-28
  page_key: magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-28
  lang: en
  template: drupal
  captured_at: '2022-07-01 11:18:03+00'
  capture_id: 729348
  wayback_url: https://web.archive.org/web/20220701111803id_/https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-28
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: p7e48z7d
  capture_id: 729360
  url: https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
  wayback_url: https://web.archive.org/web/20221003010550id_/https://magic.wizards.com/en/articles/archive/latest-developments/obliterate-2011-04-29
  captured_at: '2022-10-03 01:05:50+00'
  template: drupal
  sha256: 46901dfddda1ecd0ef47eaf4160fec3b78f0f31d908b8783ef1101382b66b0e8
render_recovery: []
---
Welcome again to the first of two *New Phyrexia* Preview Weeks. As always, I'll be spending this week and next week talking about all the exciting new cards. Before anything else, though, tradition demands that I introduce the development team.

Although *New Phyrexia* was one of the most challenging sets to develop in recent memory, the team we had was one of the more impressive ones we could have assembled. We knew what we were up against, but we were ready for action.

And "Action."

I mean, *New Phyrexia*.

Anyway...

### Aaron Forsythe

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)

Aaron's design and development credits make an impressive list. He led the design of *Alara Reborn*, ***Magic** 2010*, and ***Magic** 2011*, and he also led the development of *Shadowmoor*. I won't list the other teams he's been on, because that would take a while. Aaron is basically awesome at everything relating to **Magic**, and I was pretty excited to learn directly from him.

Aaron's job as the director of **Magic** R&D doesn't give him a lot of time to do pedestrian things like lead design and development teams, so you don't often see him in this spot. However, *New Phyrexia* was a big challenge, and there weren't any other developers that made sense for this slot. Erik had just finished *Mirrodin Besieged*, and neither Zac nor I had yet led a set before. Aaron was happy to step up and take the reins.

### Dave Guskin

![](https://i.ormos.uk/db/7a/db7a1461380a9b1b1a818e73c45395d72f8612ab206ac03a18ba077cb013bd23.jpg)

For several years, Dave worked on the technology side of things, working on projects like [Gatherer](https://web.archive.org/web/20110429000000/http://gatherer.wizards.com/Pages/Default.aspx). He always spent some of his spare time with R&D on development or design teams, as well as contributing to the Future Future League. Recently, he moved into **Magic** R&D full time as a digital developer. He's been on all kinds of product teams, as well as doing some more back-end work to improve our rare-polling software. Dave's creative instincts always seem to push him to the new and different, which was what we would need for this set.

### Zac Hill

![](https://i.ormos.uk/98/ff/98ff84c36158a8091193fe55e8d3028e6e766bb343fd8e5051e08a78fcb62548.jpg)

This is Zac's second development team. Although he's the most recent hire among full-time developers, he has already found a distinctive voice and style that guides his development instincts. Happily, that style is different from any of the rest of us, and his voice is adding to the diversity that helps us make **Magic** work for lots of different kinds of players. It'll be a little while before you see a set that he leads, but you'll be seeing more and more of his work these days. For example, he worked on the *Scars of Mirrodin* intro packs, and he built the [*New Phyrexia* Event Decks](/en/articles/arcana/2011/04-27-new-phyrexia-event-decks).

### Tom LaPille

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

Hey, that's me! I write this column, so you know lots of things about me already. I also led ***Magic** 2012* development, so you'll get to hear even more about me in a few months. Let's just move on so I don't have to [write about myself in third person](/en/articles/latestdevelopments/2011/01-21-development-under-siege) again.

### Erik Lauer

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

The last time I told you about Erik in one of these articles, I said that *Mirrodin Besieged* was the eleventh major set in a row that he had been part of the team for. *New Phyrexia* is his twelfth. No one we know of has a run anywhere close to this. Unfortunately for the streak, Erik was not part of the ***Magic** 2012* development team. Regardless, he got that deep into the streak because he's really good at this. He led ***Magic** 2010*, ***Magic** 2011*, and *Mirrodin Besieged*, and you'll see his work again in six months or so when [*Innistrad* releases](/en/articles/arcana/2011/03-14-announcing-innistrad-2).

 

Phyrexia is one of **Magic**'s most famous long-standing villains, and the name *New Phyrexia* gives us some expectations to deliver on. There's a significant backlog of Phyrexian cards in **Magic**, and that was a resource we were determined to use. But how best to use it?

We already had some experience with a variation on this technique in *Mirrodin Besieged*, where we took famous *Mirrodin* block cards and corrupted them with Phyrexian influence. [Inkmoth Nexus](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkmoth+Nexus), [Viridian Corruptor](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viridian+Corruptor), and [Blightsteel Colossus](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightsteel+Colossus) are all examples of this. Those were all easy to do, because we were taking something pure and famous and making it creepy and evil. It is more complicated to take something that was already creepy and evil and make it more so in a compelling way.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="48158" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;multiverseid=48158"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Blightsteel Colossus" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Blightsteel+Colossus"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

Although this was a more challenging task, we still took it on. You can see the results of this in the [Card Image Gallery](https://web.archive.org/web/20140523205939/http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/newphyrexia/spoiler). [Geth's Verdict](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geth%27s+Verdict) is a [Diabolic Edict](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diabolic+Edict) that makes the opponent lose a bonus life. [Mortis Dogs](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortis+Dogs) is like [Hollow Dogs](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+Dogs), except it can make your opponent lose multiple bonus life. [Surgical Extraction](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Surgical+Extraction) is like [Extirpate](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Extirpate), but free. These are all like famous cards you remember, but a bit more transgressive.

![](https://i.ormos.uk/1a/a6/1aa6a95074d29becdcf9faf3819b148bf95da58c66c67448c6df936af4e7f69a.jpg)

Those are nice, but they aren't the most direct thing we could do. There are a number of cards with "Phyrexian" in the name that have impacted Constructed **Magic** history. [Phyrexian Arena](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Arena). [Phyrexian Plaguelord](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Plaguelord). [Phyrexian Ironfoot](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Ironfoot). [Phyrexian Processor](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Processor). Perhaps the most famous of these, though—and the one that we chose to be the Phyrexian face of the *Phyrexia vs. the Coalition* duel deck—is [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator).

![](https://i.ormos.uk/1a/8c/1a8c236c315fc745625e08f8778b2e46b23c01223952fd573ae27f5b69645429.jpg)

[Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator) holds a strange place in **Magic** history for me. It is quite undercosted for its stats, but has a huge drawback in creature fights. Fortunately for [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator)s everywhere, the era of Standard when [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator) was legal was not one that encouraged fights between creatures. Several different fast combination decks were running rampant, and those decks were often interested in killing you on turn three or four without casting a single creature spell. Someone who was interested in fighting that needed both disruption and a fast clock, and that's exactly what black decks with [Duress](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duress)es, [Dark Ritual](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual)s, and [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator)s offered. In this strange way, a card that represented one of the evil faction's most potent weapons served as a noble hero, and it continued to do this for several years in Extended any time someone needed a powerful anti-combination beatdown card for their sideboard.

![5559](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=5559)

 

Unfortunately, among more casual players, [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator) may be seen as famous and powerful, but it sure isn't popular. Who wants to sacrifice their own permanents? I have met very few new or casual players who habitually play with or against only creatureless decks, so it's hard for many of them to imagine a game that doesn't involve creatures doing damage to each other. There's also the possibility that someone just casts a [Lightning Bolt](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) on your guy and makes you sacrifice three permanents at very little cost. None of this is that appealing.

[Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator), then, is a powerful weapon, but can get you very punished if you use it in the wrong situation.

That may have seemed Phyrexian at the time. Our vision of *New Phyrexia*—as created by Aaron Forsythe and Ken Nagle, the two players in R&D with the strongest griefing tendencies—is one of all-upside griefing that leaves your opponent not knowing what they're supposed to do and feeling a little bit violated. Phyrexia doesn't destroy all the creatures on the battlefield; it destroys all the creatures on the battlefield [and rips some out of your library to boot](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Life%27s+Finale). Phyrexia doesn't just exile a permanent. It [disallows the opponent from casting every other copy](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exclusion+Ritual).

![](https://i.ormos.uk/70/08/70085bfe6a3a2d7a631d983774755c6b8b5950baa3b66e4daf11a260c971cda2.jpg)

It is logical, then, that Phyrexia doesn't make itself sacrifice permanents. That's what the opponent is for.

Seems like we just found ourselves a card.

If we're going to let you have it that good, though, you're playing mono-black.

![](https://i.ormos.uk/95/e8/95e8b80ce7c4cc783193f98b904dfe1cb773b4261948ad20c2db899d8db705cf.jpg)

Yeah.

So this card. You might have noticed that between this and other things elsewhere in the set, we gave black some serious Constructed love. That wasn't an accident. Black was underplayed at this point in our Future Future league, and Aaron came in with an agenda to do something about that. I look forward to seeing how much of an effect the black cards in this set have on Standard.

Also, this card is one of the few recipients of a development tweak inspired by our worry about how good the card was that actually made the card stronger instead of weaker. The last such tweak I can remember was on [Kitchen Finks](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks), which became a 3/2 so that [Reveillark](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark) could not return it. In the case of [Phyrexian Obliterator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Obliterator), we tried the card for a while without trample. The problem with this was that often players would just chump-block it with 1/1s while slowly sacrificing permanents for several turns, which caused games to grind on and on in unfun ways. It felt a bit similar to an Eldrazi, except that it cost four mana instead of eight or more. Rather than encourage this, we just gave the thing trample so that games would end with more expediency. This also makes the card a more direct comparison to [Phyrexian Negator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Negator), which made some people's design sensibilities happier.

For me, [Phyrexian Obliterator](https://web.archive.org/web/20110429000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Obliterator) serves as a perfect flagbearer for what *New Phyrexia* is doing. It's a callout to a famous Phyrexian card. It's very powerful standing on its own. And, most importantly, it feels just a few steps over the line of what **Magic** cards should do.

![](https://i.ormos.uk/f5/fd/f5fd1ec121114ff280e54fe8d7b066483447b6d266676e76f7c0d802dc9e882b.jpg)

*New Phyrexia* Prereleases start a week from tomorrow. A few members of R&D will be traveling around the United States to different regional Prereleases; I can't speak for anyone else, but I'll be at my old stomping grounds in Columbus, Ohio if you want to catch me. I had a blast working on this set, and I look forward to playing it with some of you.

 

### Last Week's Poll

<table><tbody><tr><td colspan="3"><b>What do you think of the current Standard environment? </b></td>&#10;		</tr><tr><td>It's awesome!</td>&#10;			<td>102</td>&#10;			<td>4.9%</td>&#10;		</tr><tr><td>It's good.</td>&#10;			<td>418</td>&#10;			<td>20.1%</td>&#10;		</tr><tr><td>It's okay.</td>&#10;			<td>517</td>&#10;			<td>24.8%</td>&#10;		</tr><tr><td>It's bad.</td>&#10;			<td>351</td>&#10;			<td>16.9%</td>&#10;		</tr><tr><td>It's terrible!</td>&#10;			<td>298</td>&#10;			<td>14.3%</td>&#10;		</tr><tr><td>I haven't played Standard with Mirrodin Besieged.</td>&#10;			<td>397</td>&#10;			<td>19.1%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>2083</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>