---
id: 97g8e624
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/05-22-running-for-the-borderposts
title: Running for the Borderposts
published: '2009-05-22'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    lang_detected: en
    capture_id: 730440
    url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    captured_at: '2022-08-17 08:38:00+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    lang_detected: en
    capture_id: 730440
    url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    captured_at: '2022-08-17 08:38:00+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    lang_detected: en
    capture_id: 730440
    url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    captured_at: '2022-08-17 08:38:00+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    lang_detected: en
    capture_id: 730440
    url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
    captured_at: '2022-08-17 08:38:00+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 97g8e624
  url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
  page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
  lang: en
  template: drupal
  captured_at: '2022-08-17 08:38:00+00'
  capture_id: 730440
  wayback_url: https://web.archive.org/web/20220817083800id_/https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
- document_id: 97g8e624
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/39
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/39
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:26:23+00'
  capture_id: 622583
  wayback_url: https://web.archive.org/web/20130706052623id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/39
- document_id: 97g8e624
  url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-21
  lang: en
  template: drupal
  captured_at: '2021-11-27 13:57:05+00'
  capture_id: 730438
  wayback_url: https://web.archive.org/web/20211127135705id_/https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-21
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 97g8e624
  capture_id: 730440
  url: https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
  wayback_url: https://web.archive.org/web/20220817083800id_/https://magic.wizards.com/en/articles/archive/latest-developments/running-borderposts-2009-05-22
  captured_at: '2022-08-17 08:38:00+00'
  template: drupal
  sha256: 602671cbde7a916a4a4ed152e169e732c7189963bb9c725521d341e8e1ba4927
render_recovery: []
---
This week is Solid Gold Week, which celebrates *Alara Reborn*'s status as the only set that is made of one hundred percent multicolored cards. This was a theme that all of **Magic** R&D loved, but it put many constraints on what we could do during development.

These constraints reared their head early in development when *Alara Reborn* lead developer Matt Place decided to add more mana fixing to the set. The design handoff included a cycle of landcycling creatures that eventually became [Sanctum Plowbeast](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctum+Plowbeast) and its friends, but Matt wanted even more mana fixing. Additionally, he knew that cards like the Obelisks, [Armillary Sphere](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armillary+Sphere), and the basic landcycling cards in *Conflux* would already give people plenty of ways to fix their mana on turn two and three. In order to increase diversity, Matt wanted a cycle that would help players with their mana starting on turn one. In any ordinary set, we could have accomplished this with some kind of "comes into play tapped" lands. However, *Alara Reborn*'s hook requires that every card in it be multicolored. We were going to have to come up with something clever to solve this problem.

![](https://i.ormos.uk/28/10/281019ea17210ae9ec24af0f8dd3a498b6d0e401ee50adf2f85e99b1bceeb658.jpg)

For a short period of time, we flirted with making lands that just happened to be multicolored. Cards like [Ghostfire](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostfire) and [Transguild Courier](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transguild+Courier) show that Magic can support lines of text that set a card's color. The obvious thing to do is simply to make this card:

> Blue-White Gimmick Tapland  
>  Land  
>  Blue-White Gimmick Tapland comes into play tapped.  
>  Blue-White Gimmick Tapland is blue and white.  
>  T: add W or U to your mana pool.

We mocked up this card, and then stared at it for a while. Initially we were pleased with our own cleverness. However, before long the card morphed before our eyes. What we saw then was much less appealing.

> Blue-White Gimmick Tapland  
>  Land  
>  Blue-White Gimmick Tapland comes into play tapped.  
>  Blue-White Gimmick Tapland is technically multicolored, but dodges the spirit of Alara Reborn's theme in an obnoxious and unsatisfying way.  
>  T: add W or U to your mana pool.

It was clear that these lands did not hit the same notes that [Ghostfire](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostfire) and [Transguild Courier](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transguild+Courier) did. [Ghostfire](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostfire) was a cool card because it had an awesome new frame, it was a reference to **Magic**'s past, and it was part of *Future Sight*'s suite of cards with novel lines of text. It felt like part of the whole of *Future Sight*, but in a set entirely made out of colorless artifacts and lands, Ghostflame would feel sorely out of place.

![](https://i.ormos.uk/54/56/5456b907bcb6566a451892c981954234622eba68d84e308b3ea9856bd4057c8b.jpg)

Similarly, [Transguild Courier](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transguild+Courier) fit beautifully into *Dissension* because it had many cards that keyed mechanically off of multicolored cards. However, it was not trying to be an exclusively multicolored set. [Transguild Courier](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transguild+Courier) in *Alara Reborn* would have felt like just as much of a cop-out as our Blue-White Gimmick Tapland did.

![](https://i.ormos.uk/00/85/0085ccd4b8d99c9761ea9a4379f9964b2e6519332a38b44bdc4d99c5dd5811c3.jpg)

Another strike against this design was an issue with the card's frame. We use two different kinds of frames for lands that produce multiple colors of mana. One of them is for lands that produce only two colors, and the other is for lands that make more than two. Here are two examples.

 

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Underground River" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Underground+River"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Jungle Shrine" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Jungle+Shrine"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

When we pitched the above design to the editing team, they asked us how we would indicate graphically that the card was multicolored. Our first answer was to use the gold highlight that [Jungle Shrine](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jungle+Shrine) uses, but they helpfully pointed out that [Jungle Shrine](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jungle+Shrine) is not itself multicolored. This meant that any graphical messaging of these lands' multicolored status would be inconsistent with cards that were already being printed. The combination of the unpleasant design and graphical messaging problems killed this idea.

![](https://i.ormos.uk/69/95/6995125fa19b266d55a044017176b2664a18ed8cdcf06e71d1b8f983736c5f7b.jpg)

On almost all **Magic** cards, the color of a card is defined by its mana cost. This is something that lands simply do not have. **Magic Online** dataminer and **Magic** templating team member Lee Sharpe suggested that we try writing a mana cost in the upper right hand corner of a land, which could be played either using the once per turn land drop or by paying the mana cost. I liked this idea a lot in the moment, so I shopped it around to various people. Unfortunately, every time I showed my land-with-a-mana-cost to anyone not working on *Alara Reborn*, they assumed that to play it they would need to both spend the mana cost and use their turn's land drop. I returned from that quest to discover rules manager Mark Gottlieb asking some disquieting questions. Would lands with a mana cost use the stack? How can some things with mana costs use the stack and some not use the stack? How can some lands use the stack and other lands not use the stack? Between the confusion and the rules issues, this idea was just not going to work.

The next idea that we investigated was mana artifacts. *Shards of Alara* had already introduced both single-colored and multicolored artifacts. *Shards* included those only in Esper colors, but the *Alara Reborn* design file also included five multicolored Equipment. Because design was willing to put multicolored artifacts across all the colors, we were safe to try some kind of colored mana stones.

This idea was more promising, but had pitfalls of its own. Whatever artifacts we made had to include both colors of mana in the mana cost, which hurt our ability to print clean mana-fixing cards. Imagine this card:

> Awkward Black-Red Mana Stone  
>  BR  
>  Artifact  
>  T: add B or R to your mana pool.

This card is not much of a mana fixer. It provides black and red mana, but only to someone who already has access to both of those colors. However, it is a potent mana accelerator for a black-red deck. Two-mana mana-accelerating artifacts also often have implications in Constructed. For example, I [wrote about](/en/articles/latestdevelopments/2009/03-27-fixing-the-environment) the effect that *Ravnica* block's signets had on Standard. We like it when **Magic** changes over time, and we didn't want *Shards of Alara* block to feel the same as *Ravnica* block. Therefore, we chose to avoid two-mana artifact acceleration in *Alara Reborn*.

Matt's list of constraints was beginning to pile up. He needed a cycle of artifact mana stones that included two colors of mana in their mana cost and produced those same two colors of mana. Those artifacts needed to cost more than two mana. However, they also needed to begin to fix people's mana on turn one. These goals looked contradictory, but our crack group of **Magic** designers and developers kept plugging away.

Our next attempt was to approximate the lands we started with by replacing the playing of a land with the playing of one of our artifacts. However, this path was fraught with peril. **Magic**'s rules do not easily support skipping something that has not yet happened as a cost, and there is no resource named "land drop" in the rules that can be spent to play a card. Therefore, this simply didn't work.

![Rock Jockey](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rock+Jockey)

 

Another attempt was to use the same technology that [Rock Jockey](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rock+Jockey) uses. The proposed line of text was, "You may play this card without paying its mana cost if you have not played a land this turn. If you do, you can't play lands this turn." This approximates the cost of the land drop. However, [Rock Jockey](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rock+Jockey) costs ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) in addition to this "cost," while these mana stones would have no mana cost in addition to the free play text. This means that one could play as many of these mana stones as he or she had on the first turn, making for explosive and silly starts from decks that played all twenty available copies of them. This was untenable, so we gave up on that template.

We still liked the idea of playing one of the new mana stones as though it were a land. However, all of the cleanest ways to express this idea had problems. Therefore, we went looking for less clean templates that still did what we wanted. The first attempt that came close was this:

> Blue-White Stone  
>  1WU  
>  Artifact  
>  You may return an untapped basic land to your hand rather than pay Blue-White Stone's mana cost.  
>  Blue-White Stone comes into play tapped.  
>  T: Add W or U to your mana pool.

This card had a lot of words to parse, but it did a reasonable imitation of a comes-into-play tapped vanilla dual land as long as you had enough basic lands in your deck. These mana stones also cost more than two mana, so they did essentially all of the things that Matt wanted. This made it easy for him to decide to add them to the file.

We did a number of Limited playtests with the mana stones like this, and they did essentially everything they were designed to do. Over time, however, we became dissatisfied with the "return an untapped basic land" clause. There were two main reasons for the dissatisfaction. Multiple designers complained that returning an untapped basic land didn't feel much like a cost and that because of that, the mechanical action of picking up an untapped land to play a card was very strange. The other complaint was that it asked players to tap their lands in an unnatural order when doing many things in one turn. In normal situations, many players tap basic lands for mana to play spells before they tap nonbasic lands that make multiple colors so that they have maximum flexibility for playing later spells. When one of these is in a player's hand, that player needs to be careful to leave a basic land untapped when playing multiple spells or lose the ability to later play a mana stone for the alternate cost. I made the error of tapping all my basic lands a few times, and those were not pleasant experiences.

Both of these problems were solved cleanly when someone suggested that we replace returning an untapped basic land with paying one mana and returning any basic land. The inclusion of mana into the alternate cost made playing the card by paying the alternate cost feel much more natural. It also meant that players could tap their lands in any order and not be punished later in a turn. This gave us the versions of the cards, later named Borderposts, that made it to print!

![](https://i.ormos.uk/c7/02/c7024bfabe9d647b54067693957a2193aac8f7c1cfcbbe137e8e21cf388e5829.jpg)

The journey that led us to the Borderposts was harrowing. While we were in the middle of it, I sometimes wasn't sure that we would end up with a workable design. However, Matt believed in us, and we produced exactly what he wanted. The Borderposts have more words on them than we would have preferred, but they do exactly what we needed them to do and make *Alara Reborn* are more fun set to play while sticking with the set's theme.

We're proud of *Alara Reborn*, and the **Magic Online** *Alara Reborn* release is already in full swing! Release events began two days ago, and will continue running until June 5. We hope you take advantage of this opportunity to play with

### Magic Online Banned and Restricted Explanation

Each month, the **Magic Online** Banned and Restricted Committee considers each **Magic Online**–exclusive format and determines what changes need to be made, if any. This is a change to existing policy. Online formats that are also DCI formats, such as Standard, Extended, and Classic, will still be handled by the DCI in quarterly updates. This month's announcement was two days ago, and [Demonic Consultation](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) and [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) were restricted in **Magic Online** Classic. Here's **Magic** developer Erik Lauer with an explanation of the changes.

![Erik Lauer](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

Recently, decks using [Demonic Consultation](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) and [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) have dominated the **Magic Online** Classic format. Beginning June 3, [Demonic Consultation](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) and [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) are restricted in Classic. There are no changes to any other online formats.

![Demonic Consultation](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Demonic+Consultation)

 

A one-mana spell which both tutors for a card and puts it into your hand is an efficient enabler for degenerate combination decks. [Demonic Consultation](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) is in some ways more efficient than [Demonic Tutor](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor), [Imperial Seal](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperial+Seal), and [Vampiric Tutor](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Tutor), which are already on the restricted list. [Demonic Consultation](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) will join them this June.

![Necropotence](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Necropotence)

 

[Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) is one of the most powerful card advantage cards ever printed. Restricting cards around [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence+) would hurt the decks that use it, but there would always be both efficient ways of getting [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence+) into play and ways to use a large number of cards to kill an opponent. The **Magic Online** B&R Committee has chosen to attack the problem at the source. As of June 3, [Necropotence](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) is restricted.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>What is your favorite mythic rare in <i>Alara Reborn</i>?</b></th>&#10;		</tr></thead><tbody><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sen+Triplets">Sen Triplets</a></td>&#10;			<td>1588</td>&#10;			<td>22.1%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Extinction">Lord of Extinction</a></td>&#10;			<td>1113</td>&#10;			<td>15.5%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jenara%2C+Asura+of+War">Jenara, Asura of War</a></td>&#10;			<td>961</td>&#10;			<td>13.4%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Uril%2C+the+Miststalker">Uril, the Miststalker</a></td>&#10;			<td>834</td>&#10;			<td>11.6%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Broodmother">Dragon Broodmother</a></td>&#10;			<td>649</td>&#10;			<td>9.0%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thraximundar">Thraximundar</a></td>&#10;			<td>573</td>&#10;			<td>8.0%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx+of+the+Steel+Wind">Sphinx of the Steel Wind</a></td>&#10;			<td>520</td>&#10;			<td>7.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Nexus">Maelstrom Nexus</a></td>&#10;			<td>463</td>&#10;			<td>6.4%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karrthus%2C+Tyrant+of+Jund">Karrthus, Tyrant of Jund</a></td>&#10;			<td>370</td>&#10;			<td>5.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defiler+of+Souls">Defiler of Souls</a></td>&#10;			<td>113</td>&#10;			<td>1.6%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7184</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

Whenever I run one of these polls, I try to guess which cards will be most popular before I open up the results page. This poll's results were flatter than I would have guessed. It's very cool to see [Sen Triplets](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sen+Triplets) at the top, though. As I write this, I am sitting next to rules manager Mark Gottlieb, who both designed it and put in many hours of work to make it actually function within **Magic** rules. He and I are both glad that his work paid off to make an awesome card.

My favorite of these cards is [Jenara, Asura of War](https://web.archive.org/web/20090522000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jenara%2C+Asura+of+War). That card became as powerful as it is very late in development and I was one of the people responsible for that, so I have a soft spot for it. I also had an awesome time playing with it in the Standard Bant deck I played at the *Alara Reborn* prerelease. I enjoy both efficient creatures and creatures that can become enormous, and Jenara is both of those things.