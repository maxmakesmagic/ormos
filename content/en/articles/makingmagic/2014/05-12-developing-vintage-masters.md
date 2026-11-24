---
id: zrmvxk5p
kind: article
lang: en
path: /en/articles/makingmagic/2014/05-12-developing-vintage-masters
title: Developing Vintage Masters
published: '2014-05-12'
column_slug: makingmagic
column: Making Magic
authors:
- slug: ian-duke-4e99a22e
  name: Ian Duke
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    lang_detected: en
    capture_id: 875806
    url: https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    captured_at: '2022-05-18 03:07:45+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    lang_detected: en
    capture_id: 875806
    url: https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    captured_at: '2022-05-18 03:07:45+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    lang_detected: en
    capture_id: 875806
    url: https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    captured_at: '2022-05-18 03:07:45+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    lang_detected: en
    capture_id: 875806
    url: https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
    captured_at: '2022-05-18 03:07:45+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: zrmvxk5p
  url: https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
  page_key: magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
  lang: en
  template: drupal
  captured_at: '2022-05-18 03:07:45+00'
  capture_id: 875806
  wayback_url: https://web.archive.org/web/20220518030745id_/https://magic.wizards.com/en/articles/archive/making-magic/developing-vintage-masters-2014-05-12
- document_id: zrmvxk5p
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/299&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/299
  lang: en
  template: aspx
  captured_at: '2014-05-16 06:36:49+00'
  capture_id: 219297
  wayback_url: https://web.archive.org/web/20140516063649id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/299&print=true
- document_id: zrmvxk5p
  url: https://magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12
  page_key: magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12
  lang: en
  template: drupal
  captured_at: '2022-01-19 14:26:01+00'
  capture_id: 619194
  wayback_url: https://web.archive.org/web/20220119142601id_/https://magic.wizards.com/en/articles/archive/feature/developing-vintage-masters-2014-05-12
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: zrmvxk5p
  capture_id: 219297
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/299&print=true
  wayback_url: https://web.archive.org/web/20140516063649id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/299&print=true
  captured_at: '2014-05-16 06:36:49+00'
  template: aspx
  sha256: 6a031292ce63e5f854df3c2686d30ede3589142d1b2c24d717286197fd6d8188
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Black Lotus
  - Inspiration
  - Ironclaw Orcs
  - Jackal Pup
  - Goblin King
  - Delif's Cube
  occurrences: 12
---
 ***Please note:** The card images as they appear here are not as they will appear in* Vintage Masters*, which will use the modern card frames, Power Nine art from the ****Magic Online**** Cube, and new art for a number of cards. Actual card images will be posted soon.*

  

* * *

  

Hi all! I'm Ian Duke and I work as a developer in **Magic** R&D. I've been with Wizards for about two years, and *Vintage Masters* was my first opportunity to lead the development of a set release. I'm super excited to dive in and tell you all about the process of building this awesome draft format, but since this is a preview article, I'll have to restrain myself a bit! 

Being a developer is all about solving problems and overcoming challenges. Today, I'll share with you the story of one of the challenges our team faced in developing *Vintage Masters*, and how we not only met and exceeded that challenge, but also introduced a new draft archetype in the process. But first—just what is *Vintage Masters*? 

### That Vintage Feeling

![](https://i.ormos.uk/fe/c0/fec027e9c5867403d91b776fd6296e473daf99f316afe2423a93e10684630f3a.jpg) 

  

*Vintage Masters* was conceived as a way of introducing the [Power Nine](/en/articles/arcana/2003/10-15-the-power-nine) cards to **Magic Online**. It was to be a special, **Magic Online**–only release that would also rerelease many cards that are important to Constructed Vintage play. The goal was to eventually sync up the online Classic format with the traditional Vintage format. We want both Vintage aficionados and new competitors alike to be able to experience the awesomeness of Vintage through the convenience of **Magic Online**. 

When *Modern Masters* debuted we were overwhelmed with positive feedback about how much players enjoyed the Limited play. It was then that we realized we could do a similar thing with *Vintage Masters*. We set out to create a fully draftable, high-powered Limited environment that captures the fun and nostalgia of playing with the strongest and most iconic cards from **Magic**'s early history. 

However, we knew we didn't want to simply replicate the *Modern Masters* experience—we wanted to make *Vintage Masters* stand out on its own. Aaron Forsythe, director of **Magic** R&D, came up with the idea of building *Vintage Masters* from only the set of cards that aren't currently Modern legal. This would emphasize the feeling of the Vintage experience and play up the nostalgia of the early days of **Magic**. As any Legacy or Vintage player can tell you, there's no shortage of awesome, iconic cards to draw from in the pre-*Eighth Edition* period. 

We ended up with an awesome set.

Whether you've been playing **Magic** since 1993 or have only ever heard of Black Lotus spoken of in hushed whispers in the back room of your local card shop, I encourage you to check out *Vintage Masters* when it launches June 13. While we certainly pulled no punches in making the set as fun as possible for experienced players, you don't need to have been playing **Magic** for decades in order to jump in and enjoy the set. Many of the archetypes are visible at the surface level, but we also infused the draft environment with enough depth to keep things fresh for ten, fifteen, twenty drafts and beyond. 

### Restrictions Breed Creativity

Limiting our focus to the pool of cards that aren't Modern legal was both the biggest challenge and the most fun aspect of working on *Vintage Masters*. This restriction asked the design and development teams to be much more creative in how we built the set, and I firmly believe the draft environment ended up a much more fun, distinct, and nostalgic experience as a result. 

![](https://i.ormos.uk/b3/56/b35697ccc248090cc40142df02f1e6aec986c1322b0fd7ece3c74b1e415a9f5d.jpg) 

Inspiration | Art by [Izzy](https://web.archive.org/web/20140512000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Izzy%22])

It turns out that **Magic** has evolved in many ways over the years. For example, the color pie has changed in several subtle and not-so-subtle ways. Black used to be the color of fast mana rituals before that was shifted into red. White used to be better at destroying both artifacts and enchantments than green was. In addition, the relative balance between creatures and spells was much different. Big creatures didn't really exist at common, and in general instants and sorceries were much stronger, relative to creatures. 

When design handed off the file to development, many of these imbalances from the early days of **Magic** were showing through. The powerful, iconic spells we knew we wanted to include in the set were outshining many of the interesting synergies design had built in. Certain color combinations were working very well, but others were lagging behind. Of course, that's nothing unusual for a **Magic** set at that stage of the process, so the development team set to work tweaking and tuning and bringing things into balance. 

### Homeless Pups

For the most part, our iteration was working well. We largely focused on making strategies stronger, since we wanted to maintain the high power level and splashy plays that make eternal formats so enjoyable. However, we found that we were hitting a ceiling in some areas. Certain color combinations and strategies weren't coming up to par with the rest of the set. In particular, the color red was turning out to be a challenge.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="4825" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=4825&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="207" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=207&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*Examples of cards that were cut.* 

  

What we found in testing was that players were snapping up the premium red burn spells and splashing them, but no one was building decks with red as the main color. The problem? The creatures were too weak. We began a massive exploration, poring over every possible red creature from **Magic**'s early days, and even considering dramatic rarity shifts in order to get red's creature curve in line. We were able to make a few changes that helped somewhat, but ultimately the team wasn't satisfied. After all, some of the most efficient creatures red had access to in those days were Ironclaw Orcs and Jackal Pup. Not exactly impressive! 

Even though we were a ways into the development process at this point, we still kept the design team very much looped in on our progress. When we discussed the difficulty we were having with red, designer Ethan Fleischer came up with a brilliant idea.

 ![Goblin Warchief](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Goblin%20Warchief&options=) 

  

Goblins!

### Red Goes Green

While red's creatures from this time period were weak on their own, Ethan suggested that we could lean on tribal synergies to bring up the collective power level. I was skeptical. I thought that the Goblins wouldn't play well with the rest of the set and what the other colors were trying to do. I also wasn't sure we'd even be able to get the power level of the Goblins up to par. Design had tried some other tribal strategies earlier in the process and they didn't work well, which left me hesitant to try again.

Luckily, development-team member Adam Prosak stood up for his green-skinned buddies. At the next team meeting, Adam brought a list of all the Goblins we had access to, including his recommendations for which would be the most fun and powerful to play with. Once the team saw his plan laid out, we agreed to give it a try in the next draft playtest.

It worked wonders. What we found was that because the Goblins were individually weaker than many of the cards in the set, they tended to float around the draft table longer. Eventually, someone would figure out that red was open and start collecting a Goblin tribal package. Instead of seeing a bunch of Ironclaw Orcs and Jackal Pups lap the table indefinitely, we saw the player who was "supposed" to be base red assemble a powerful tribal deck. 

![](https://i.ormos.uk/7d/48/7d485845e8fc18649c432f1fec59cf13c2102b01718b1b2ff85fd2da582ca2c7.jpg) 

Goblin King | Art by [Ron Spears](https://web.archive.org/web/20140512000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Ron+Spears%22])

The result? A 3–0 victory for the Goblin King of the playtest. We saw the similar things happen in future playtests. While Goblins wasn't always the dominant deck of the draft, it took its place as one of many viable strategies, and one of many things red can do in the set. 

### Drafting Constructed

While our job of developing the set was far from done, we had successfully overcome one of the major challenges we'd run in to. We continued polishing the set from there, and I can say I'm very happy with where we ended up. The result is a Cube-like draft experience that captures more of a Constructed feel than traditional Limited formats often do. Beyond the basic two-color combinations, there are plenty of sideways strategies and unique build-around cards at higher rarities. This creates a huge variety of experiences and keeps the format fresh for many, many drafts.

![](https://i.ormos.uk/21/9f/219f3a1872c48e6723277ca6452408210f1deff6789858b739781f609a72e358.jpg) 

Delif's Cube | Art by [Mark Tedin](https://web.archive.org/web/20140512000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Mark+Tedin%22])

I hope you enjoyed this journey through one of the challenges we faced in building *Vintage Masters*. For a more in-depth look at what it's like to work on such a unique and exciting set, join me for my next article in early June, where I'll take us through a development retrospective. Until then, enjoy preview week! 

[![](http://media.wizards.com/images/magic/daily/footers/JOU/EN_JOU_ArticleFooter_PTPre_Details_Static.png)](https://web.archive.org/web/20140512000000/https://accounts.onlinegaming.wizards.com/) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Ian Duke](https://i.ormos.uk/82/2b/822b917034ff4543ec86ea9e0a479c80f7232f507471856a098422ca9b0c809b.jpg "Ian Duke")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Ian Duke</b>&#10;        <br>&#10;        &#10;        <br>&#10;        <a href="https://web.archive.org/web/20140512000000/http://www.wizards.com/company/emailtoauthor.asp?author=Ian%20Duke&amp;amp;headline=[Developing%20Vintage%20Masters]">Email Ian</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20140512000000/http://www.wizards.com/magic/magazine/archive.aspx?author=ian%20duke">Author Archive</a>&#10;        <br>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Ian Duke is a developer in **Magic** R&D and has been with Wizards of the Coast since 2012. A gift of an *Ice Age* starter deck in 1995 sparked Ian's lifelong passion for **Magic**. He also enjoys math, physics, board games, and puzzles. To the surprise of few, his favorite guild is Azorius. 

 