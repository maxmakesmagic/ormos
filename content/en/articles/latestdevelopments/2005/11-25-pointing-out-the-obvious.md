---
id: ce26zacj
kind: article
lang: en
path: /en/articles/latestdevelopments/2005/11-25-pointing-out-the-obvious
title: Pointing Out the Obvious
published: '2005-11-25'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    lang_detected: en
    capture_id: 729713
    url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    captured_at: '2022-08-18 09:03:47+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    lang_detected: en
    capture_id: 729713
    url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    captured_at: '2022-08-18 09:03:47+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    lang_detected: en
    capture_id: 729713
    url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    captured_at: '2022-08-18 09:03:47+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    lang_detected: en
    capture_id: 729713
    url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
    captured_at: '2022-08-18 09:03:47+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - ed3f153p
sources:
- document_id: ce26zacj
  url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
  lang: en
  template: drupal
  captured_at: '2022-08-18 09:03:47+00'
  capture_id: 729713
  wayback_url: https://web.archive.org/web/20220818090347id_/https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
- document_id: ed3f153p
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af94&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af94
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:42:11+00'
  capture_id: 253387
  wayback_url: https://web.archive.org/web/20090604154211id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af94&print=true
- document_id: ed3f153p
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af94
  page_key: wizards.com/default.asp?x=mtgcom/daily/af94
  lang: en
  template: classic_asp
  captured_at: '2008-03-24 15:08:04+00'
  capture_id: 1929713
  wayback_url: https://web.archive.org/web/20080324150804id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af94
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: ce26zacj
  capture_id: 729713
  url: https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
  wayback_url: https://web.archive.org/web/20220818090347id_/https://magic.wizards.com/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-25
  captured_at: '2022-08-18 09:03:47+00'
  template: drupal
  sha256: 49f70cf2291d3e5b65ee79fd79209d6c7f744975abee83a7e9b0904ffbfacedb
render_recovery: []
---
*Wizards of the Coast is out of the office for the Thanksgiving holiday, and will return with new articles beginning Monday, November 28. In case you missed it, what follows is the article that ran in this slot last week. Have a great weekend, and we’ll see you Monday!*

*Scott Johns, **magicthegathering.com** Content Manager*

I've been having a good time with **Magic** lately. You might think that because working on **Magic** is my job that I always have a good time with it. But that's not entirely true—anything has its ups and downs, and sometimes being too close to the game drives me away for a time. But not lately.

Last weekend I played in a “draft marathon” at a local card shop, in which I drafted the full *Invasion* block, the full *Odyssey* block, the full *Mirrodin* block, and then *Ravnica*. Although I didn't do well enough to make the top 8 (I'm gradually losing my competitive focus), I still had a ball. At work, on top of developing the upcoming “Snap” set and starting up design for the block after *that*, I've been working on the theme decks for the upcoming *Coldsnap* expansion, which are quite a trip down memory lane. The [first-ever Legacy Grand Prix](https://web.archive.org/web/20051125000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgevent/gpphi05/welcome)—something I've been pushing for personally for a long time—was a fantastic event. I'm making arrangements to attend Worlds in Japan in a couple weeks. And my old pal John Rizzo has resurfaced over at [StarCityGames](http://www.starcitygames.com/).

Fun times indeed. A perfect time, then, to have my readers do something fun as well.

At the draft marathon, several of the players were telling me that they enjoyed *Ravnica* Limited so much because so many of the cards were hard to evaluate correctly in Limited. That got me thinking. Then I read that Scott Wills was leaving this site, so I started perusing his archive. And that also got me thinking. Then I had to turn in my Limited pointing results for Snap to Matt Place, and that *really* got me thinking. Why not do another Limited pointing article?

What is Limited pointing? It's a way for **Magic** developers to gauge the power level of individual colors for both sealed deck and draft. Each developer assigns a number to each card based on how powerful he perceives it to be, then those numbers are averaged and analyzed in an attempt to balance things out. Here's a snippet from the relevant section of our Developer's Handbook explaining the scale we use:

> *…\[H\]ere is the fundamental definition of our rating: Given that this is the first card you see (of your 75-card sealed deck or first pack, first pick in draft), how happy are you – on a scale of 0.0 - 5.0 – to see it? Furthermore, your ratings should be linear (that is, you'd be just as happy with a 3.5 and a 2.5 or with two 3.0's). Also, to be technically correct, this all assumes that your goal is to win – winning makes you “happy.”*
> 
> *The following elaborations of this scale are merely guidelines, designed to clarify the scale defined above:*
> 
> ***5.0**: I will always play this card. Period.*
> 
> ***4.5**: I will almost always play this card, regardless of what else I get.*
> 
> ***4.0**: I will strongly consider playing this as the only card of its color.*
> 
> ***3.5**: I feel a strong pull into this card's color.*
> 
> ***3.0**: This card makes me want to play this color. (Given that I'm playing that color, I will play this card 100% of the time.)*
> 
> ***2.5**: Several cards of this power level start to pull me into this color. If playing that color, I essentially always play these. (Given that I'm playing that color, I will play this card 90% of the time.)*
> 
> ***2.0**: If I'm playing this color, I usually play these. (70%)*
> 
> ***1.5**: This card will make the cut into the main deck about half the times I play this color. (50%)*
> 
> ***1.0**: I feel bad when this card is in my main deck. (30%)*
> 
> ***0.5**: There are situations where I might sideboard this into my deck, but I'll never start it. (10%)*
> 
> ***0.0**: I will never put this card into my deck (main deck or after sideboarding). (0%)*

Here are some examples from the recent *Kamigawa* block to help you understand the scale.

*   [Umezawa's Jitte](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte) – 5.0. Always played, always first picked, always ridiculous.
*   [Meloku, the Clouded Mirror](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meloku%2C+the+Clouded+Mirror) – 4.0. You can easily imagine playing Meloku as your only blue card in a sealed deck, and being very happy doing so.
*   [Kokusho, the Evening Star](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kokusho%2C+the+Evening+Star) – 3.5. He makes you want to play black, and you'll always run him if you are black.
*   [Glacial Ray](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Ray) – 2.75. Some people may point it even higher than this.
*   [Mothrider Samurai](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mothrider+Samurai) – 1.75. There are times when you'd play white and not run this guy, but they're rare.
*   [Sakura-Tribe Scout](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Scout) – 0.75. You don't want to play this guy, but it happens.
*   [One with Nothing](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=One+with+Nothing) – 0.0. ‘Nuff said.

Got it? Now it's your turn. Take a look at the cards below, then enter your results into the Limited Pointing Survey.

We'll start off with a chunk of blue commons. Take a look at this list and come up with a rating for each one:

*   [Stasis Cell](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis+Cell)
*   [Surveilling Sprite](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Surveilling+Sprite)
*   [Tattered Drake](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tattered+Drake)
*   [Terraformer](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terraformer)
*   [Tidewater Minion](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tidewater+Minion)
*   [Vedalken Dismisser](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vedalken+Dismisser)

Next up are gold uncommons, which, as a whole, may be the most powerful group of Limited cards in the set. Where do these rate?

*   [Lightning Helix](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix)
*   [Moroii](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moroii)
*   [Pollenbright Wings](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pollenbright+Wings)
*   [Psychic Drain](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychic+Drain)
*   [Putrefy](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy)
*   [Selesnya Sagittars](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Selesnya+Sagittars)

Finally, here are some black rares. Rares are interesting, as they are often hit-or-miss in Limited. Just how good are these six?

*   [Blood Funnel](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Funnel)
*   [Dark Confidant](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Confidant)
*   [Empty the Catacombs](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empty+the+Catacombs)
*   [Helldozer](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Helldozer)
*   [Hex](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hex)
*   [Hunted Horror](https://web.archive.org/web/20051125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hunted+Horror)

You can click [here](#poll) to enter your results in the Limited Pointing Survey. I'll compile the results, then compare the readers vs. R&D in a future article. Have fun!

### Last Week's Poll

<table><thead><tr><th colspan="3">Which is the better draft format in general?</th>&#10;		</tr></thead><tbody><tr><td>Big set / small set 1 / small set 2</td>&#10;			<td>3520</td>&#10;			<td>42.1%</td>&#10;		</tr><tr><td>Big set / big set / big set</td>&#10;			<td>2998</td>&#10;			<td>35.9%</td>&#10;		</tr><tr><td>I don't draft</td>&#10;			<td>1511</td>&#10;			<td>18.1%</td>&#10;		</tr><tr><td>Neither</td>&#10;			<td>331</td>&#10;			<td>4.0%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>8360</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

That's my pick as well. This has been an ongoing argument here in R&D as we talk with Organized Play about scheduling future events.