---
id: 10f6vh2j
kind: article
lang: en
path: /en/articles/latestdevelopments/2004/04-23-turning-the-sorcery-knob
title: Turning the Sorcery Knob
published: '2004-04-23'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    lang_detected: en
    capture_id: 735577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    captured_at: '2022-01-25 21:22:17+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    lang_detected: en
    capture_id: 735577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    captured_at: '2022-01-25 21:22:17+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    lang_detected: en
    capture_id: 735577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    captured_at: '2022-01-25 21:22:17+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    lang_detected: en
    capture_id: 735577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
    captured_at: '2022-01-25 21:22:17+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - dk3q141e
sources:
- document_id: 10f6vh2j
  url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
  page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
  lang: en
  template: drupal
  captured_at: '2022-01-25 21:22:17+00'
  capture_id: 735577
  wayback_url: https://web.archive.org/web/20220125212217id_/https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
- document_id: dk3q141e
  url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23-0
  lang: en
  template: drupal
  captured_at: '2022-08-17 16:52:34+00'
  capture_id: 735580
  wayback_url: https://web.archive.org/web/20220817165234id_/https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23-0
- document_id: dk3q141e
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af11
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af11
  lang: en
  template: aspx
  captured_at: '2009-06-04 14:35:12+00'
  capture_id: 777972
  wayback_url: https://web.archive.org/web/20090604143512id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af11
- document_id: dk3q141e
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af11
  page_key: wizards.com/default.asp?x=mtgcom/daily/af11
  lang: en
  template: classic_asp
  captured_at: '2005-02-04 21:38:34+00'
  capture_id: 1925994
  wayback_url: https://web.archive.org/web/20050204213834id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af11
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 10f6vh2j
  capture_id: 735577
  url: https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
  wayback_url: https://web.archive.org/web/20220125212217id_/https://magic.wizards.com/en/articles/archive/latest-developments/turning-sorcery-knob-2004-04-23
  captured_at: '2022-01-25 21:22:17+00'
  template: drupal
  sha256: 1fe00ae183117f91dc2df2cbbc9af011001ac1a5687bf8f2aa5f94ccec77918a
render_recovery: []
---
Although instants and sorceries are categorized as two different card types, their effects are usually very similar. Both have one-shot uses and go to the graveyard right away. Of any two card types, the line between sorceries and instants is blurred more than any other (even that between artifacts and global enchantments).

As Mark pointed out in [his column this week](https://web.archive.org/web/20040423000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr120) and [Randy in a column from last June](https://web.archive.org/web/20040423000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb77), we here in *Magic* design and development understand the tension that sorceries add to game play: tapping out on your own turn for an effect creates more interesting decisions than always being able to wait for the best time to play your cards. But the underlying message of both of those articles was that instants are just “better” than sorceries. Well, I have something to say there.

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_af11_picmain_en.jpg)

They're right! If spell A is an instant and spell B is a sorcery with the same mana cost and effect, spell A is a just a better card.

There are many effects that we are willing to do as both instants and sorceries, and in most cases you can see that we “charge more” for an effect if we do it as an instant. A clean example would be the Core Set card [Blaze](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blaze) versus [Volcanic Geyser](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Geyser), which first appeared in *Mirage*. Both deal X damage to target creature or player, but the instant version costs R more than the sorcery. One mana is a good baseline estimate of what the difference is worth. Another example would be the instant [Opportunity](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opportunity), and its *Portal* parallel, [Tidings](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tidings). Both are fair cards for their costs. [Volcanic Hammer](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Hammer) and [Carbonize](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carbonize) have a similar relationship, and it stands to reason that if [Inspiration](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspiration) is ok at 3U then a 2U sorcery version would be an ok card as well. I agree.

This algorithm works pretty well for card drawing and direct damage, but it breaks down when looking at other types of spells. Can you infer from [Mind Rot](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) that we would do a 3B or 2BB instant that made your opponent discard two cards? I hardly think so. Does [Boomerang](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boomerang) mean that a sorcery for U that bounced any permanent is a printable card? No, it does not.

There are exceptions in the other direction as well. If [Savage Twister](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savage+Twister) is a sorcery that deals X damage to each creature for XRG, what would an instant that did the same thing cost? XRRG? X1RG? No, just [XRR. And it would have cycling 3 thrown on it for free. Rules are made to be broken, I suppose.](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=XRR.+And+it+would+have+cycling+3+thrown+on+it+for+free.+Rules+are+made+to+be+broken%2C+I+suppose.)

If you understand that being an instant has a cost attached to it, you probably are glad we've kept so many effects as sorceries. For example, the *Invasion* rare [Rout](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rout) is a [Wrath of God](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) clone that can be played as an instant for 5WW. If seven mana is a fair cost for an instant Wrath, I can't imagine any respectable control player asking for us to print that card as opposed to the traditional four-mana Wrath. When it comes right down to it, the type line on instants and sorceries is another "knob" we can turn when balancing cards.

Sometimes when we need to make a card a little worse but still would like it to be played, switching it from instant to sorcery is the better alternative to adding mana. If [Echoing Ruin](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Echoing+Ruin) was a 2R instant as opposed to its current 1R sorcery form, would it be a better card? Would a 1R instant [Firebolt](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebolt) be better than what was printed? It would be close, but the answer is most likely no. So contrary to what I said before, maybe instants *aren't* just better than sorceries!

When developing sets, we like to turn the instant-sorcery knob a lot as we try to balance cards and mechanics. Just this week we found some acceptable middle ground on a powerful white spell in *Betrayers of Kamigawa* by changing it to a sorcery. One of the last changes we made to *Fifth Dawn* was changing a common instant to a sorcery because it was causing its color to be disproportionately overplayed.

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_af11_pic1_en.jpg)

Looking at the in-print sets, there are several more cards that had their types change in development. [AEther Snap](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=AEther+Snap) was changed from an instant to a sorcery (and its mana cost increased) because it was too devastating of a hoser against the block's major mechanics. [Hunger of the Nim](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hunger+of+the+Nim) underwent the same change to make black a little worse in limited. We go the other way, too. [Thirst for Knowledge](https://web.archive.org/web/20040423000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge) was designed as a sorcery because it almost always is a card drawing spell. But development decided that hairs could be split in the card's favor and deemed it a "card filtering" spell (meaning you end up with the same number of cards in hand after you cast it as you had before), and changed it to an instant. Of course, we all know that it really is a card-drawing spell, but, like I said before, rules are made to be broken.

The next time you play a sorcery and wish to yourself, "I wish this was an instant," chances are that it was at some point. We try lots of things here in R&D in our quest to make *Magic* as interesting as possible, and care is given to each card's cost, commonality, and—of course—card type.

### Last Week's Poll

<table><tbody><tr><td colspan="3"><b>Do you have a singular favorite Magic artist?</b></td>&#10;		</tr><tr><td>Yes—an artist you don't really use any more.</td>&#10;			<td>2417</td>&#10;			<td>26.5%</td>&#10;		</tr><tr><td>Yes—an artist you are currently using.</td>&#10;			<td>2391</td>&#10;			<td>26.2%</td>&#10;		</tr><tr><td>No—I like several artists equally.</td>&#10;			<td>2371</td>&#10;			<td>26.0%</td>&#10;		</tr><tr><td>No—I don't really care.</td>&#10;			<td>1931</td>&#10;			<td>21.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>9110</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

Wow, that couldn't have been more even! Perhaps in future polls I will delve into who people's actual favorites are.

* * *

*Aaron may be reached at latestdevelopments@wizards.com.*