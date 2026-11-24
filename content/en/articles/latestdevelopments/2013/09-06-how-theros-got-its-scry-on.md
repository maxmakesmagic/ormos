---
id: fhg1zwj7
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/09-06-how-theros-got-its-scry-on
title: How Theros Got Its Scry On
published: '2013-09-06'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    lang_detected: en
    capture_id: 723187
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    captured_at: '2022-05-26 05:36:03+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    lang_detected: en
    capture_id: 723187
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    captured_at: '2022-05-26 05:36:03+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    lang_detected: en
    capture_id: 723187
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    captured_at: '2022-05-26 05:36:03+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    lang_detected: en
    capture_id: 723187
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
    captured_at: '2022-05-26 05:36:03+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: fhg1zwj7
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
  lang: en
  template: drupal
  captured_at: '2022-05-26 05:36:03+00'
  capture_id: 723187
  wayback_url: https://web.archive.org/web/20220526053603id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-06
- document_id: fhg1zwj7
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/263
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/263
  lang: en
  template: aspx
  captured_at: '2014-02-17 11:08:03+00'
  capture_id: 620579
  wayback_url: https://web.archive.org/web/20140217110803id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/263
- document_id: fhg1zwj7
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-05
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-05
  lang: en
  template: drupal
  captured_at: '2022-01-16 11:20:34+00'
  capture_id: 723172
  wayback_url: https://web.archive.org/web/20220116112034id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-theros-got-its-scry-2013-09-05
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: fhg1zwj7
  capture_id: 620579
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/263
  wayback_url: https://web.archive.org/web/20140217110803id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/263
  captured_at: '2014-02-17 11:08:03+00'
  template: aspx
  sha256: 4d360f3694c90cddd3b9cae7bc27d8733672b8e97de6d11324292d089e8f5ab3
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Rancor
  - Stand Firm
  - Serum Visions
  - Supreme Verdict
  occurrences: 6
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - the scry lands
  occurrences: 1
---
You may have [heard from Mark Rosewater](http://markrosewater.tumblr.com/post/60151583699/who-is-the-brilliant-individual-who-first-suggested) that of all of the mechanics in *Theros*, scry is the one that wasn't handed off from design. The story of how scry was added to *Theros* is one that I am excited to tell because it is one I had a hand in. During my early days of being an intern, before I was on many teams, and well before I was leading products, I spent most of my days [FFL](/en/articles/latestdevelopments/2013/08-16-days-of-future-future-part-2)ing and playing in Limited playtests. It was during this time that [Erik Lauer](https://web.archive.org/web/20140301070036/http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer), who was the lead developer of *Theros*, was telling me about the problem he was trying to solve for the set—making it so players would actually play with Auras so the Limited games weren't constantly decided by people either drawing all of their heroic creatures and no enablers, or all of their Auras and no creatures to put them on. We had already split up bestow into having two costs—one for the creature, and one to cast it as an Aura—which had helped, but it had not solved the problem as a whole. Erik was in the process of putting in cards like Commune with the Gods to help, but a few commons wouldn't be enough. 

![](https://i.ormos.uk/6d/92/6d92e2ac257e2353d1550321b63c25ba54d3bc0390269efdd900bda98244c9fd.jpg) 

  

Taking a step back for a second—one of the design goals of *Theros* was to get players to actually cast Auras on their creatures. This is traditionally something that new players like very much, because it is easy to understand how powerful turning one creature into Voltron is, but it quickly becomes weaker when played in more serious settings due to removal. It took years for **Magic** to design Auras that actually saw play in a competitive arena, and we couldn't have every Aura in the set at the level of Rancor. While heroic and bestow both went a long way to making the value proposition good enough in Limited, they didn't solve the problem alone. Players wanted to run them (and often did), but they were also having problems getting them to work well enough to put up winning records. Development needs to make sure that, in a given set, the design goals are not only met, but they are met in a way that is satisfying to players and not just a box-checking activity while we decide what we care about and make that the powerful thing to do in the set's Limited environment. 

 ![Rancor](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Rancor&options=) 

  

When development works on a set, it takes the design goals and tries to find solutions to make them work not just in design playtests, but in the real world. One of the lessons from *Avacyn Restored* was that getting your mechanic to work by reducing the effectiveness of the removal can work in a vacuum, but it doesn't help when people try and play those cards in other settings. Development needed to find a way to make the set fun, while incorporating one of the higher-variance types of game play into something people would actually want to do and be rewarded for. And that meant finding a way to reduce the inherent variance that goes along with casting Auras. 

Back to the story at hand. After mulling over the problem for a day or two, I had an insight. "What about scry?" I asked Erik. "It would help people manipulate their decks enough to get the cards they needed, and it really fits into the Greek theme with oracles and seers." Erik thought about this for a moment and agreed that it would do that, but he would have to run the idea past Mark Rosewater. Luckily, Mark agreed that it would help solve the problems while still fitting into his overall view of what made *Theros*, *Theros*. One playtest later and things were already starting to improve. 

One of the things we discovered early on is that [scry 1](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+[scry]+[1]+![2]) is generally a much more fun rider on a spell or ability than higher numbers. It is less powerful, for sure, but it is far quicker operationally, because it doesn't ask you to plan your next two or three turns in advance. It also doesn't have the tension where you will often basically burn a [scry 2](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+[scry]+[2]) spell like Stand Firm just to dig further in your deck. We wanted to entice players to cast the spells and get some value out of the scry, not make scrying itself the reason for casting them. With scry 1, you just look at the top card, decide if you want to keep it or not, and then go on with your turn. It was important to have some scry in the set that was at higher numbers, but we didn't want so much of it that games of Limited would be overly defined by bomb rares, since players would be able to very aggressively dig for them. We wanted to get scry to create the card flow at the rate we found to be the most enjoyable. 

 ![Stand Firm](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Stand%20Firm&options=) 

  

The other benefit of adding scry to the set was that we didn't have a plan yet for what the ten dual lands would look like in the block. We knew that we wanted ten, and that we wanted them to not play so well with the [Ravnica dual lands](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&format=+[%22Return+to+Ravnica+Block%22]&type=+[%22Land%22]&text=+[or]&name=+![Promenade]+![Maze%27s]) that decks would be three colors by default. We needed duals that you would be able to run twelve of if you really wanted to force a twenty-four-dual-land mana base like *Return to Ravnica* Standard, but that would have enough of a downside that it was a well thought-out decision rather than something with little to no opportunity cost. I think we discovered a pretty good balance of those goals and creates a cycle of lands that incorporate a lot of the feel of the block into their design. Introducing... the scry lands: 

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <img src="https://i.ormos.uk/a5/b2/a5b22efd60f8090f51614c5ab81198999cc902fc309b68c61264bb11e9a44bdf.jpg">&#10;      </td>&#10;      <td>&#10;        <img src="https://i.ormos.uk/3d/87/3d87df8c81c6207f785451dcbdb3d5591e6a61596a03abe25a811967f9a04a2f.jpg">&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <img src="https://i.ormos.uk/c1/d9/c1d9ad8d161763b725f9498c878ad9726b6efcad305959d1c50d972a81a72196.jpg">&#10;      </td>&#10;      <td>&#10;        <img src="https://i.ormos.uk/ca/b8/cab82ed1c5847320d6ba94c0eb5f1708c8e0148f76c6e9499bb78bb400066c56.jpg">&#10;      </td>&#10;    </tr>&#10;    <tr>&#10;      <td colspan="2">&#10;        <div>&#10;          <img src="https://i.ormos.uk/61/b6/61b62280632dd9e276f318470451c14856c235a0decc355e582ec7573fb44230.jpg">&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Since we knew we would have all ten in the block, we went ahead right away and commissioned all ten pieces of art, which let us hold off on the decision on which duals to include in *Theros* until we'd had time to playtest Standard. We tried all the allieds, all of the enemies, and a few random mashups. [Tom LaPille](https://web.archive.org/web/20140309095604/http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille) made a strong argument, though, that the previous year in Standard had extra time with the [*Return to Ravnica* shocklands](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Return+to+Ravnica%22]&type=+[%22Land%22]&text=+[life]), and that the [*Gatecrash* color pairs](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Gatecrash%22]&type=+[%22Land%22]&text=+[life]) could use some extra time in the spotlight, so that is the model we went with. This left us with five more for the rest of the block. What will the order be for their release? You'll have to wait and see. 

### Visions of Topdecks

There was some concerns within development that the scry lands might be too powerful. They may not look as strong on the surface as the shocklands, but they have one very important thing going for them—each one is basically a slightly smaller Serum Visions. Except, you know, it's a land instead of replacing itself. They have a tendency to reduce mulligans by increasing your odds of hitting your third or fourth land when keeping a hand with just two lands, but they do so at the cost of sometimes preventing you from curving out. They also mean that your four-land opening hands in midrange or aggro decks are better able to keep from flooding out. Now, most decks don't have too many turn-one plays, so the cost of the land coming into play tapped on turn one is very low. In addition, drawing one late in the game is generally stronger than drawing another shockland or basic. 

![](https://i.ormos.uk/c3/22/c322128bd59550916b0e17428a179ab5dadd0311b2d3220db8819692d5f22d35.jpg) 

Temple of Silence | Art by [Karl Kopinski](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22karl+kopinski%22])

  

Entering the battlefield tapped is a large downside on a land, but from the [Vivids](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&name=+[Vivid]) to the [Alara tri-lands](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&format=+[%22Shards+of+Alara+Block%22]&type=+[%22Land%22]&text=+[enters]+[tapped]&name=+![Spire]) to the [*Worldwake* man lands](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Worldwake%22]&type=+[%22Land%22]&text=+[becomes]+[creature]) to the [Hideaway cycle](https://web.archive.org/web/20130906000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+[hideaway]&type=+[%22Land%22]), we have seen that this doesn't keep the lands out of Constructed, although it does make decisions on how many colors you want to run in your deck far more difficult than the shockland/checkland mana bases. If you want to run a three-color deck, you will run into more situations where you are playing lands tapped when you don't want to, or taking more damage from your shocklands than you did in the previous year. We don't want to keep three-color decks from existing, just make them feel different from the previous year and give a lot of good reasons for deciding to play two colors instead. 

On the flip side to this, running a deck with a whole lot of scry lands does help these kinds of decks dig further and faster for the spells they need. While a three-color control deck with eight or more scry lands may have problems hitting everything on curve, it is going to probably get the Supreme Verdict more often because it is seeing extra cards due to its mana base. At the same time, an aggro deck running scry lands (even off-color ones) will often miss out on hitting all of its creatures on curve but will have a better overall balance of lands and/or spells than an aggro deck not running any scry lands at all. These cards are powerful, but they have tradeoffs, and I look forward to seeing how these impact deck-building decisions as the year goes on. 

### The R&D Challenge

Before I sign off this week, I wanted to talk about a great tournament we are running tomorrow (September 6) on [**Magic Online**](https://web.archive.org/web/20140217125411/http://www.wizards.com/Magic/Digital/MagicOnline.aspx?x=mtg/digital/magiconline/download). The R&D Challenge is a series we run about once every three months where you have the opportunity to play against members of R&D to see if you can beat us at our own game. This time, the format is Modern. The event costs 12 tickets to enter, and players who 5–0 will not only receive a *From the Vault: Twenty* and a healthy supply of boosters, but will also share in any winnings that the Wizards of the Coast team would've won in the tournament. 

More information on the tournament [can be found here](/en/articles/feature/2013/09-02-community-wins-the-2013-community-cup). 

The tournament starts at 12:00 p.m. Pacific, Friday, September 6, on **Magic Online**. I hope to see you there. 

Until next week,

Sam

  
  

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_Prerelease_Details_Static.png)](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments) [![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_Prerelease_Minisite_Static.png)](https://web.archive.org/web/20140217221742/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/theros) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130906000000/http://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[How%20Theros%20Got%20Its%20Scry%20On]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325153238/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 