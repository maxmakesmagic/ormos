---
id: 6hrspqea
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/04-10-building-bolas
title: Building Bolas
published: '2009-04-10'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    lang_detected: en
    capture_id: 718493
    url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    captured_at: '2017-08-16 07:38:06+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    lang_detected: en
    capture_id: 718493
    url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    captured_at: '2017-08-16 07:38:06+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    lang_detected: en
    capture_id: 718493
    url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    captured_at: '2017-08-16 07:38:06+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    lang_detected: en
    capture_id: 718493
    url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
    captured_at: '2017-08-16 07:38:06+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - mt74kpv6
sources:
- document_id: 6hrspqea
  url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
  page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
  lang: en
  template: drupal
  captured_at: '2017-08-16 07:38:06+00'
  capture_id: 718493
  wayback_url: https://web.archive.org/web/20170816073806id_/http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
- document_id: mt74kpv6
  url: https://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-09
  lang: en
  template: drupal
  captured_at: '2021-12-05 00:32:29+00'
  capture_id: 718487
  wayback_url: https://web.archive.org/web/20211205003229id_/https://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-09
- document_id: mt74kpv6
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/33
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/33
  lang: en
  template: aspx
  captured_at: '2013-07-02 00:46:45+00'
  capture_id: 620897
  wayback_url: https://web.archive.org/web/20130702004645id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/33
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 6hrspqea
  capture_id: 718493
  url: http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
  wayback_url: https://web.archive.org/web/20170816073806id_/http://magic.wizards.com/en/articles/archive/latest-developments/building-bolas-2009-04-10
  captured_at: '2017-08-16 07:38:06+00'
  template: drupal
  sha256: 52beeb6b2ac258881daab078a7529170d1016d131876d044ecfa00ecc9090bb3
render_recovery: []
---
![](https://i.ormos.uk/0c/69/0c697cb2c6ba3c2f53f1f85bc0558cf9c3e5b71c6f7d1d6b4d758d41c0f2ae72.jpg)

The *Shards of Alara* block is built around five separate worlds, and including one planeswalker in the block for each shard felt natural. Brady Dommermuth's proposal was to include a planeswalker for each shard other than Grixis in *Shards of Alara* itself, then complete the pattern with [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) in *Conflux*. He thought that the incomplete pattern would make players expectant for what was to come, and that it would build excitement for when we finally printed [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker), the biggest, most badass planeswalker in the Multiverse. The developers and designers thought that this was a cool idea, so we agreed to go along with it.

When *Conflux* development began, we had to do our part to make sure that the payoff was worth it by making [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) into an awesome **Magic** card. This was not easy and took a lot of people a lot of work. We had to ask ourselves many questions as we worked on it, and today I'll walk you through a few of them.

### What Does Nicol Bolas Do?

![](https://i.ormos.uk/9d/01/9d0171d23784dcfaafd525bb914150ffa27d59b926e9ffe3d29896d21afa256e.jpg)

The *Conflux* development team knew that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) needed to carry a ton of the set's weight. To have the best chance of having an awesome [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker), we asked everyone in the company who had any interest to submit [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) designs. Along with that request, we sent out a quick primer on Nicol Bolas from Doug Beyer. It contains too many secrets to show in its entirety, but Doug conveyed these things:

*   He is the most badass planeswalker in the Multiverse.
*   He's a huge and ancient dragon.
*   He loves power more than anything else.
*   He enjoys feeling the mental anguish of other planeswalkers.
*   Most likely, you're already part of one of his schemes and you don't know it.

As the *Conflux* lead developer, Mike also included some requests. He asked that the designs represent what Nicol Bolas means to the designer, that it be casual friendly, and that it read totally awesome. It turned out that just about everyone wanted to help make [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker), and we got tons of submissions.

![](https://i.ormos.uk/95/bb/95bb6108d03b5312b95ea8be620a634215c8976812d431093febb3eff4637b5c.jpg)

The first part of the card that was finalized was the Ultimate. Two Ultimates that almost made it came from Mark Rosewater and Brady Dommermuth. Mark's matched the character of Nicol Bolas quite well. However, it was possible in some situations for it to go off and have the opponent come back quickly. Nicol Bolas is far meaner than that. He thinks nothing of [erasing one of his own minions' minds](https://web.archive.org/web/20090410000000/http://magic.wizards.com/en/articles/archive/alara-unbroken-2009-01-28) if it learns too much about his schemes, and we decided that the things that he does to a planeswalker enemy should be far more horrific than that. Few entities in the Multiverse should be strong enough to survive when Nicol Bolas is done with them. We still liked Mark's ultimate, though, so we decided to save it for a planeswalker who wasn't quite as ruthless, evil, and cruel as Nicol Bolas. Brady's submission was much crueler and meaner, but also had a playful quality to it that Mike Turian thought didn't feel quite right.

One of the other submissions had the germ of an interesting idea. When the *Legends* version of [Nicol Bolas](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas+) hits you, you take 7 damage and you discard your hand. Why can't this one do that too? Mike liked the throwback but wanted something more, so he changed "your hand" to "seven cards" and added "then sacrifices seven permanents." That ultimate received tons of positive comments from everyone who saw it, so Mike decreed that this was the final Ultimate.

One common thread of the designs for [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker)'s first two abilities was the inclusion of one ability that dealt with creatures and another ability that dealt with noncreatures. The earliest version of [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) that had the final ultimate had the abilities "+3: Return target noncreature permanent to its owner's hand, then that player discards a card," and "-1: Destroy target creature." I enjoyed that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) effectively was casting [Recoil](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recoil) and [Terminate](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate), two gold spells whose colored mana symbols added up cleanly to those on Nicol Bolas. Once we got here, we asked a different question.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Recoil" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Recoil"></div>&#10;			</div>&#10;			</td>&#10;			<td><img alt="Terminate" src="http://magic.wizards.com/sites/mtg/files/image_legacy_migration/magic/draftools/760KjI0g5M/img/games15.jpg"></td>&#10;		</tr></tbody></table>

### How Much Does Nicol Bolas Cost?

When I started working here at the end of June, [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) cost ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif). A combination of his high mana cost, fluctuating abilities, and obvious Timmy appeal kept me from taking him seriously in Constructed until his abilities settled down. I then built a green mana ramp deck that used [Rampant Growth](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth), [Fertile Ground](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground), and [Garruk Wildspeaker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker) to pump out big spells quickly, and I knew that I should be playing some kind of super-expensive bomb in it. I started with [Violent Ultimatum](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Ultimatum), but when that worked out pretty well I realized that I could have been playing [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) instead for a similar cost. The call of elder dragon planeswalkers was too powerful, so I moved from four [Violent Ultimatum](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Ultimatum) to three [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) and a [Conflux](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conflux).

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Violent Ultimatum" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Violent+Ultimatum"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Conflux" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Conflux"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

It shocked me how strong [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) was in that deck. I had multiple turn-four [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) games, and at the time I only had to use the plus ability once to be able to use the Ultimate. I have vivid memories of playtester Steve Warner scooping after his fourth draw step to an impending Ultimate. Others started to play him too, and there was growing discontent among some **Magic** playtesters with how quickly [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) was hitting play in Future Future League games. We knew that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) needed to be awesome, but we also knew that it would be a little awkward if games were simply races to Bolas.

At one point, the following playtest card was floating around in the *Conflux* Limited pool.

![](https://i.ormos.uk/02/bd/02bd6e26dd2c68cdea21bbc603946e5a5a15b71c18971e304a603d1fdb01cc51.jpg)

One of the following things is true:

1.  The *Conflux* team decided to move [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) to eight mana, but there was a typo when they entered the new mana cost into the file. The software we use to produce playtest stickers from raw Multiverse files misinterpreted that typo and we ended up with a [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) that has a converted mana cost of 45 and requires snow mana. That physical card shares a place of honor on my desk with a hand-painted parrot made out of balsa wood, a whiteboard that I use to summon things, and a *Masters Edition 2* [Wall of Kelp](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Kelp) playtest sticker.

2.  The *Conflux* team asked Multiverse's artificial intelligence module to recost [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker), and then printed playtest cards before checking its work. Apparently Multiverse and Bolas had a history, since Multiverse's recosting was quite mean to everyone else's favorite elder dragon planeswalker. The team decided that requiring snow mana was a little extreme, so Aaron Forsythe and Mark Rosewater went to the Multiverse server room, inserted their keys simultaneously and entered their passwords, then hit the big Multiverse manual override button. We made [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) cost a mere eight mana and then locked its database entry before turning the system's brain back on.

A few people were interested in costing [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) at ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) to match the *Legends* version. Del Laugel, our ever-vigilant editor, brought us back to reality by telling us that that the name "[Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker)" only gave us room to use five mana symbols. The creative team really liked that name, so we stayed with ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) so that they could keep it.

I kept testing the card in the same deck at eight mana and found it to be just barely clunky enough for me to not auto-include it. It was still fun to play with, though, so I kept one in the deck and told myself that it would be okay because I would never draw two.

### How Many Turns Does It Take to Ultimate?

The first version of [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) that we played with started at five loyalty. His plus ability was +3 and his Ultimate was -7 to match up with the other sevens in the Ultimate's text, so that meant that there was only one turn of ticking between his arrival and the annihilation of the opponent's hand and board.

Some playtesters weren't thrilled with this even at eight mana. It played very much like a sorcery with the text box "Target player peeks at the top card of their deck. If it is not totally awesome, that player loses the game." I was one of the playtesters who was uncomfortable with that game play. I enjoy games of **Magic** that go back and forth, and I argued that one more turn of possible topdecks would increase the feeling that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) was a planeswalker, not a complicated [Cruel Ultimatum](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Ultimatum) variant.

The big thing standing in the way was the feedback that we had received about [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) from members of the company outside of R&D. The two features that received the most positive comments were that his plus ability was a whopping +3 and that it only took one turn to reach the Ultimate. Mike values the feedback we get from outside the pit and was concerned about taking away one of the most-loved parts of the card, but eventually the pressure to give the extra turn was too great.

### Can We Make This Card More Awesome?

Mike really wanted [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) to be as exciting as possible, and he was sad that some of that luster had been eroded. Playtesting had forced him to both add a mana to the mana cost and add a turn to the time it takes to reach the Ultimate, and he felt that it was high time that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) take a little power back.

In the final *Conflux* development meeting, Mike and the rest of his team made two last-minute changes to [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) that made him both more powerful and even more cruel. They decreed that instead of returning noncreature permanents to their owner's hands, [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) would outright destroy them. They also decided that instead of destroying creatures, he would gain control of them. These changes made him more powerful, but also much more ruthless and unyielding. After all, why would an elder dragon planeswalker merely put off what he could deal with now? Why would he destroy a creature when he could instead rewrite its mind?

![](https://i.ormos.uk/c0/72/c0726bd5c5ec7b5b210d7d74410915bae95dd63902844f2b73aebeeb190bd0df.jpg)

The *Conflux* team also decided to put the cost of Bolas's Ultimate at -9. They needed to choose a cost that kept Bolas's Ultimate from going off after one turn, but wanted to avoid double digit numbers because that would have read much worse. The only number they could choose was 9, so they went with that. These were the last changes to [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nicol%2BBolas%252C%2BPlaneswalker) before he went off to print.

I am personally quite happy with where Bolas ended up. He is expensive enough to keep him from ending games in the same way over and over, and it takes two turns to make him loyal enough to use his Ultimate. Because of that, however, the *Conflux* team was able to make him even more impressive and dominating while he is in play. That's exactly where I hoped the card would be, and we're glad that the world has embraced him so happily.

### Who Doesn't Love Nicol Bolas?

![](https://i.ormos.uk/36/a3/36a36d4c3b9efd55974efe524839ed54f211b972dce11ddf68727b35aec9eb2a.jpg)

No one! This was only the second theme week dedicated to a single character that we've ever had on this site, but Nicol Bolas deserves it. He was the centerpiece of *Conflux* from the very beginning of its design, and we put in a lot of work to make sure that the wait for the Grixis shard's planeswalker would be worth it. I hope you enjoyed Nicol Bolas Week, and make sure to come back next Monday for the beginning of *Alara Reborn* previews!

 

### Last Week's Poll

<table><tbody><tr><td colspan="3"><b>Which of these is your favorite?</b></td><td> </td>&#10;<td> </td>&#10;		</tr><tr><td><a href="http://gatherer.wizards.com/magic/draftools/760KjI0g5M/img/split3.jpg">Nicol Bolas, Plains // Walker</a></td>&#10;			<td>2642</td>&#10;			<td>48.0%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker">Nicol Bolas, Planeswalker</a></td>&#10;			<td>2160</td>&#10;			<td>39.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090410000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas">Nicol Bolas</a></td>&#10;			<td>704</td>&#10;			<td>12.8%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>5506</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

The **Magic** web team put in tons of work to make this year's April 1 update happen. The ["totally normal" draft viewer](https://web.archive.org/web/20090410000000/http://magic.wizards.com/en/articles/archive/draft-viewer-412009-2009-04-01)'s back-end programming, joke writing, and images combined with the text and images for the [*From the Vault: Vaults* announcement](https://web.archive.org/web/20090410000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/arcana/158) represent many man-hours of work, and we hope you enjoyed it. I was excited to have a poll that both showed off their work and was dripping with dragony goodness.

Personally, I'm in the minority that likes the original the best. I've always enjoyed nontraditional interpretations of fantasy tropes, and there's something about an enormous dragon calmly reading in his library that makes me very happy. Of course, a Dragon Plains is also pretty awesome, and that was almost enough to pull me over to that camp. I'm glad that many of you liked the humorous split card, and as always, thanks for voting.

\[The survey originally included in this article has been removed.\]