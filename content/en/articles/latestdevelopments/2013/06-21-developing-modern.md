---
id: xc4s0t7g
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/06-21-developing-modern
title: Developing Modern
published: '2013-06-21'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    lang_detected: en
    capture_id: 720950
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    captured_at: '2022-08-18 15:18:44+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    lang_detected: en
    capture_id: 720950
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    captured_at: '2022-08-18 15:18:44+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    lang_detected: en
    capture_id: 720950
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    captured_at: '2022-08-18 15:18:44+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    lang_detected: en
    capture_id: 720950
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
    captured_at: '2022-08-18 15:18:44+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: xc4s0t7g
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
  lang: en
  template: drupal
  captured_at: '2022-08-18 15:18:44+00'
  capture_id: 720950
  wayback_url: https://web.archive.org/web/20220818151844id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-21
- document_id: xc4s0t7g
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/252
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/252
  lang: en
  template: aspx
  captured_at: '2014-04-24 03:58:25+00'
  capture_id: 620425
  wayback_url: https://web.archive.org/web/20140424035825id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/252
- document_id: xc4s0t7g
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-20
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-20
  lang: en
  template: drupal
  captured_at: '2021-10-18 12:51:14+00'
  capture_id: 720938
  wayback_url: https://web.archive.org/web/20211018125114id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-modern-2013-06-20
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: xc4s0t7g
  capture_id: 620425
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/252
  wayback_url: https://web.archive.org/web/20140424035825id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/252
  captured_at: '2014-04-24 03:58:25+00'
  template: aspx
  sha256: bb09affbc9aeeaa7a834d95fc8efb37bbe2652b65544ef05cfd10b718b512ed1
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Tarmogoyf
  - Pillar of Flame
  - Voice of Resurgence
  - Searing Spear
  - Beck
  - Deathrite Shaman
  - Spike Feeder
  - Birthing Pod
  - Mana Leak
  - Dismember
  - Thoughtseize
  - Path to Exile
  - Lava Spike
  - Baleful Strix
  - Shardless Agent
  - Scavenging Ooze
  - Skullclamp
  - Dark Depths
  - Glimpse of Nature
  - Jace, The Mind Sculptor
  - Ponder
  - Preordain
  - Valakut, the Molten Pinnacle
  occurrences: 36
---
This weekend, [Grand Prix Las Vegas](/en/events/2013/lasvegas13/grand-prix-las-vegas-event-information) with *Modern Masters* Limited will break the record for the largest Grand Prix of all time—and that's just preregistration. It shows both how popular the Limited format is and how excited people are for the cards in *Modern Masters*. Modern is a format that we are very excited about internally, and we hope *Modern Masters* helps to provide enough of an influx of cards to open the format to more people, even as **Magic** as a whole continues to grow. From everything I've seen, it looks to be doing that job admirably. 

![](https://i.ormos.uk/85/f1/85f168b254da257c00e74bd041d0470a209090159acfab1d52d533b282a70743.jpg) 

Tarmogoyf | Art by [Ryan Barger](https://web.archive.org/web/20130621000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22ryan%20barger%22])

Modern has provided us a non-rotating format that is far more accessible than Legacy or Vintage, but still retains many of the qualities that people enjoy in those formats—such as a more stable metagame, the ability to play and tweak the same deck week after week, and simply a much more powerful card pool than Standard. This accessibility has allowed us to run PTQs using it, a feat that was never really possible with Legacy, but it also puts additional pressure on us to makes sure we don't break the format while developing cards for Standard.

I've heard before the common wisdom that we don't really develop for Legacy or Modern, but that isn't quite true. While it is true that Standard and Limited make up the majority of our sanctioned tournaments, and therefore get the majority of our attention and development resources, we do make sure to look out for Modern, Legacy, and Commander. Our playtesting of the formats is minimal, but most of our developers are knowledgeable enough to keep an eye out while working on the sets in development. We have to be the most careful with Standard and Limited because they are also the formats that have the least ability to deal with cards that are too powerful, because of the work we do on balancing them. If we are off on how strong a card is (and we always will be now and then), there is a real risk that the format will warp around that card.

When developing for Standard, we make sure to include enough cards that can act as answers that the format can adjust. The dance of cards like Pillar of Flame moving from the main deck, to the sideboard, to not being included at all—if Zombies or Voice of Resurgence become too oppressive, red decks can start moving their Pillars to the main deck and pushing other decks out of the format; in response, decks that are good against Pillar of Flame but not the removal spell it replaced (say, Searing Spear) will thrive, and the metagame will keep moving around. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Pillar of Flame" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Pillar%20of%20Flame&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Voice of Resurgence" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Voice%20of%20Resurgence&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Trying to engineer this kind of movement in Modern, or Legacy for that matter, in the amount of time we have to develop a set would be nearly impossible. The formats just have so many moving parts and so many directions to go in, the best we can do is come up with cards we find to be really fun and interesting and see what they do to the format. We do spend a lot of time discussing cards we are concerned about, like Beck or Deathrite Shaman, but ultimately, unless the card presents a clear and present danger to the format, we leave it up to the best judgment of the set's lead developer. 

### Calculated Risks

Keeping Modern interesting does mean taking a few risks here and there, though. If you have seen the [**Magic** 2014 Card Image Gallery](https://web.archive.org/web/20140218214856/http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2014coreset/cig), you might see a card named Archangel of Thune. When developing the card for Standard, it was noted that in Legacy and Modern, it allows for an infinite loop with Spike Feeder to gain unbounded life and put an unbounded number of +1/+1 counters on creatures you control. We discussed the implications of this, but ultimately it was decided that, even if it fits as another possible combo enabler in the Birthing Pod decks, those decks are already filled up to the brim with different combo engines, so Archangel of Thune didn't provide a huge risk, and the card remained unchanged going into M14. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Spike Feeder" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Spike%20Feeder&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Birthing Pod" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Birthing%20Pod&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

While a two-card combo like this might seriously threaten Standard, it takes a lot more than that to threaten Modern, because of the strength and variety of answers available. Decks have access to cards like Mana Leak, Dismember, Thoughtseize, Path to Exile, and the like. 

We have to be careful when putting combos into the format that are hard to interact with, but ones that open themselves up to creature removal are usually relatively safe.

The larger risks that we have to deal with in Modern is putting in too many redundant effects that create a critical mass in a deck (for instance, every new Lava Spike variant we print gets the Burn deck one card closer to being able to consistently deal 20 by turns three or four easily) or hyper-efficient two-for-ones. As the format develops, though, and we release more and more cards, it should keep building up resilience and over time be able to handle more threats. 

We are able to take bigger risks with Legacy and Commander in products such as *Planechase* or **Magic: The Gathering**—Commander because they don't interact with Standard or Modern, and the power level of Legacy is more able to handle a much stronger influx of cards. It is in these products that we can target cards that are more focused on making an impact in Legacy, which has resulted in such cards as Baleful Strix, Shardless Agent, and Scavenging Ooze becoming role players in the format. Of course, just because a card starts out in one of these products doesn't mean that it will stay there forever. In case you missed it in [the Arcana a couple weeks ago](/en/articles/arcana/2013/06-05-magic-2014-intro-packs-d14-boosters), Scavenging Ooze will be making its Standard/Modern debut following the release of **Magic** 2014. Having played with the card quite a bit over the past year, I am looking forward to seeing its impact in Standard, but also seeing what it can do in Modern. I don't know that it will dethrone Tarmogoyf as the king of the green two-drops, but it will at the least play a good Apollo Creed to Tarmogoyf's Rocky Balboa. Boy, do I hope [that reference](http://en.wikipedia.org/wiki/Rocky_%28film_series%29) didn't date me too much. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Scavenging Ooze" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Scavenging%20Ooze&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Tarmogoyf" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Tarmogoyf&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### Keeping the Format in Check

One of the hardest parts for the developers working on creating the basics of the Modern format was settling on the correct [banned list](https://web.archive.org/web/20140410124645/http://www.wizards.com/Magic/TCG/Resources.aspx?x=judge/resources/sfrmodern). Of course, the cards like Skullclamp that have proven themselves to be too powerful for even Legacy are easy ones to put on the chopping block, but there are a lot of cards in the gray area that we left off the list for the [**Magic Online** Community Cup](/en/events/2011/mtgoccup11/magic-online-community-cup-thursday) but added to the list by the time we officially announced it for [Pro Tour Philadelphia](/en/events/2011/ptphi11/estratti-starts-modern-revolution-in-philly). 

The banned list for Modern has been a matter of much discussion both by our player base and internally at Wizards. Having a banned list as large as the one in Modern isn't a thing we want to do, but we believe it is what is right for the format as it currently exists. There are many cards on the list that many players would love to play with... heck, there are cards on there I would love to play with. While removing cards from the banned list would increase the number of cards in the format, it also has the very real risk of doing so at the cost of reducing the number of viable decks in the format. Our goal with Modern is to provide a format that allows for a wide variety of decks, where no single strategy is too dominant, and where turn-three wins are not consistent. Cards like Skullclamp; Dark Depths; Glimpse of Nature; or Jace, The Mind Sculptor exist at such a high power level when combined with all of the other sets in Modern that putting one of them into the format would inevitably alter the format to be all about that one card. Other cards, like Ponder and Preordain, just provide so much cardflow to the combo decks that they become nearly impossible for "fair" decks to compete against. While I don't think the banned list is perfect, I think it is getting very close, and the diversity the format has shown over the past year, despite going through the wringer at many high-level events, is a testament to that. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Skullclamp" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Skullclamp&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="265979" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=265979&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

That being said, we removed Valakut, the Molten Pinnacle from the banned list just about a year ago, and we have been very happy with how that change affected the format. It has also slotted into about the range we expected—powerful, but not dominant. As the format evolves, and we add new cards to the format, there may well be room for some of the other cards on the banned list to come off. 

### Modern Moving Forward

As I mentioned earlier, in about a month, Modern players will soon get their first opportunity to play with Scavenging Ooze in the format. As we approach the two-year mark of Modern as a format, and the first cycle of cards designed and developed with Modern in mind begin to be released, I am excited about how the format will continue to evolve. The more we have had a chance to play with the actual format (and not just a theorycrafted version of it) and the more that we see what kind of decks emerge in it, the better we are able to design cards that will fit into the format but not break Standard. Knowing what is coming up in ***Magic** 2014*, *Theros*, and beyond, I am very excited to see how Modern continues to grow and adapt, and to create new tools to increase the depth of the format. 

Sam

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_FNM_Top.jpg) 

[![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_FNM_Button01_Static.jpg)](https://web.archive.org/web/20130621000000/http://staging.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/dragonsmaze/productinfo) [![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_FNM_Button02_Static.jpg)](https://web.archive.org/web/20130621000000/http://staging.wizards.com/Magic/TCG/article.aspx?x=mtg/tcg/dragonsmaze/cig) 

  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130621000000/http://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[Developing%20Modern]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130621000000/http://staging.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325153238/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 