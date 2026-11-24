---
id: fx02g8v1
kind: article
lang: en
path: /en/articles/latestdevelopments/2004/01-09-developing-indestructibility
title: Developing Indestructibility
published: '2004-01-09'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    lang_detected: en
    capture_id: 720912
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    captured_at: '2022-09-30 23:32:47+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    lang_detected: en
    capture_id: 720912
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    captured_at: '2022-09-30 23:32:47+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    lang_detected: en
    capture_id: 720912
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    captured_at: '2022-09-30 23:32:47+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    lang_detected: en
    capture_id: 720912
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
    captured_at: '2022-09-30 23:32:47+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - rb4x92dh
sources:
- document_id: fx02g8v1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
  lang: en
  template: drupal
  captured_at: '2022-09-30 23:32:47+00'
  capture_id: 720912
  wayback_url: https://web.archive.org/web/20220930233247id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
- document_id: fx02g8v1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09
  lang: en
  template: drupal
  captured_at: '2022-05-26 04:41:46+00'
  capture_id: 720910
  wayback_url: https://web.archive.org/web/20220526044146id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09
- document_id: rb4x92dh
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb105
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb105
  lang: en
  template: aspx
  captured_at: '2013-02-20 09:00:51+00'
  capture_id: 805041
  wayback_url: https://web.archive.org/web/20130220090051id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb105
- document_id: rb4x92dh
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb105,,de
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb105
  lang: en
  template: classic_asp
  captured_at: '2005-02-18 07:00:31+00'
  capture_id: 1986834
  wayback_url: https://web.archive.org/web/20050218070031id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb105,,de
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: fx02g8v1
  capture_id: 720912
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
  wayback_url: https://web.archive.org/web/20220930233247id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-indestructibility-2004-01-09-0
  captured_at: '2022-09-30 23:32:47+00'
  template: drupal
  sha256: 564f6f82baac2e3de0e2b58378f2a49bceba0ec5383b80a7e69df03427735e83
render_recovery: []
---
I think Mark was right when he cut straight to the chase on Monday … here’s your preview card:

![](https://i.ormos.uk/fd/3f/fd3f0a44a96b2fe68658e721e544028438d88ad6b8332251d6de947de9f73da2.jpg)

I want to spend the rest of this week’s column talking about the new indestructible ability from a developer’s point of view.

All the developers agreed early on that indestructible was quite a cool ability, but none of us were sure exactly how good it was. First we had to figure out exactly what it would mean, of course. It’s all well and good to say “they’re indestructible,” but we spent several months arguing about what precisely that should mean. Everyone knew we wanted indestructible artifacts to survive a [Naturalize](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize), and indestructible artifact creatures should never be killed by combat damage, but that still left a bunch of questions: Should indestructible legends die when there are two in play? Does an indestructible creature die when you use a –x/-x spell to lower its toughness to zero? What if your opponent plays [Wrath of God](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God)? What if they play [Diabolic Edict](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diabolic+Edict)? What if you feed your indestructible artifact to your [Atog](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog)?

![](https://i.ormos.uk/e1/d3/e1d3cb1e2da7839b740334fa7c6664f958b71df2db6807bd668fb620b9118f8c.jpg)These questions were made even more difficult by the fact that we weren’t tied to any specific reminder text or card wordings. We knew we really liked the word “indestructible,” but that’s really all we had to go on. For quite a while we assumed that “Indestructible” would be a keyword ability, but that led to some really awkward wordings like “CARDNAME gains indestructible until end of turn.” *Gains* indestructible?! We wanted to say things like CARDNAME *is* indestructible. The templating team saved us here by figuring out that we could treat “indestructible” as an English-language word rather than a keyword ability.

Of course, none of that answered the question of how exactly indestructible should work in the non-obvious cases. One early version of indestructible said that whenever the artifact went to the graveyard that it would come back into play, and another version said that whenever it would get put into the graveyard you instead left it in play. Both of these versions were broken in the same way. Imagine sacrificing an artifact to something like an [Atog](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog). Well, it would still be there to sacrifice again and again and again. Clearly, indestructible artifacts had to be vulnerable to sacrifice effects. Once we had that figured out, we knew that there were going to be some ways to cause them to go from play into the graveyard. They were just indestructible, not immortal. Rule Manager Paul Barclay really wanted all zero-toughness creatures to die anyway, otherwise he would have to rewrite the rules of the game so that state-based effects wouldn’t keep getting checked and trying to kill them over and over again. He also wanted them to die to the legend rule for similar reasons. From there it was a matter of figuring out what we could easily and clearly explain in reminder text. Drawing the line at destruction effects made sense anyway since the word we were trying to explicate was “indestructible” after all. We knew that most players would not realize that death from combat damage is technically a destruction effect so we went ahead and decided to spell that out in the reminder text and voila – a mechanic was born.

Once we knew exactly what our cool new mechanic would do, it was time to figure out how good it was (and how much mana to charge for it). The indestructible creatures were the hardest ones to balance. The set only has three of them, but they are potentially very powerful and they can go into every deck (regardless of color) so we knew we had to make sure they weren’t broken.

The more we played with them, the more powerful they seemed. We kind of wanted to have at least one creature that was relatively cheap, but even a 1/1 for 3 was too strong and the 2/2 for 5 that we had in the file was quite annoying to play against, especially in Limited where there weren’t a lot of ways to good to get rid of it. Because of the stalemates that can be generated by an indestructible creature in Limited play, we decided not to put any of them at common. Meanwhile, we didn’t want them all to cost an arm and a leg and that’s when somebody suggested that we go the “[Jade Statue](https://web.archive.org/web/20040109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jade+Statue)” route. Huzzah – problem solved! Of course, I’m only allowed to preview one card this week so you’ll have to wait and see how that creature actually turned out, but I can tell you that we’re pretty happy with the way it’s good without being too good …

### Last Week’s Poll Results:

Well, these are actually results from 3 weeks ago, but here’s what you guys thought of the Type 1 restrictions …

<table><thead><tr><th colspan="3"><b>What do you think of these bannings? </b></th>&#10;		</tr></thead><tbody><tr><td>Thumbs Up</td>&#10;			<td>2649</td>&#10;			<td>47.1%</td>&#10;		</tr><tr><td>I don’t care about Type 1</td>&#10;			<td>1420</td>&#10;			<td>25.3%</td>&#10;		</tr><tr><td>Thumbs sideways</td>&#10;			<td>1048</td>&#10;			<td>18.6%</td>&#10;		</tr><tr><td>Thumbs Down</td>&#10;			<td>506</td>&#10;			<td>9.0%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>5623</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

*Randy may be reached at latestdevelopments@wizards.com.*