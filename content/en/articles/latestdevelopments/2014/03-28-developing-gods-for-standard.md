---
id: 7484gjxf
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/03-28-developing-gods-for-standard
title: Developing Gods for Standard
published: '2014-03-28'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    lang_detected: en
    capture_id: 720899
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    captured_at: '2022-08-14 04:17:22+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    lang_detected: en
    capture_id: 720899
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    captured_at: '2022-08-14 04:17:22+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    lang_detected: en
    capture_id: 720899
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    captured_at: '2022-08-14 04:17:22+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    lang_detected: en
    capture_id: 720899
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
    captured_at: '2022-08-14 04:17:22+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 7484gjxf
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
  lang: en
  template: drupal
  captured_at: '2022-08-14 04:17:22+00'
  capture_id: 720899
  wayback_url: https://web.archive.org/web/20220814041722id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-gods-standard-2014-03-28
- document_id: 7484gjxf
  url: https://magic.wizards.com/en/articles/archive/developing-gods-standard-2014-03-27
  page_key: magic.wizards.com/en/articles/archive/developing-gods-standard-2014-03-27
  lang: en
  template: drupal
  captured_at: '2021-10-28 21:59:25+00'
  capture_id: 301887
  wayback_url: https://web.archive.org/web/20211028215925id_/https://magic.wizards.com/en/articles/archive/developing-gods-standard-2014-03-27
- document_id: 7484gjxf
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/292
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/292
  lang: en
  template: aspx
  captured_at: '2014-06-09 08:15:11+00'
  capture_id: 620795
  wayback_url: https://web.archive.org/web/20140609081511id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/292
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 7484gjxf
  capture_id: 620795
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/292
  wayback_url: https://web.archive.org/web/20140609081511id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/292
  captured_at: '2014-06-09 08:15:11+00'
  template: aspx
  sha256: 7b1e415bd363221df75c307a949e9ca62fcd5933bee7ac50a3835b0542569294
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Polukranos
  - Stormbreath Dragon
  - Fleecemane Lion
  - Boros Reckoner
  - Nightveil Specter
  - Burning-Tree Emissary
  - Thoughtseize
  - Fade into Antiquity
  - Elspeth, Sun's Champion
  - Wall of Frost
  occurrences: 20
---
Mark Rosewater pointed out in [his article on Monday](/en/articles/makingmagic/2014/03-24-modern-gods) that the Gods went through a ton of iterations in design because we knew we needed to get them right. The last time we did something approaching an enchantment block was Urza's block, and while the block contained a ton of enchantments, all of the power was in the artifacts. That is a clear lesson that people generally view a block based on the powerful and iconic cards that come out of the block, and less by what the intentions of that block are by us. Mark often says that if your theme doesn't show up at common, it isn't your theme. Well, for development, we take a similar view of Standard—if the set's theme doesn't show up in Standard, then we did something wrong. 

We wanted bestow, devotion, monstrosity, and heroic to show up to some extent in Standard, although the exact number of each cards that would show up was less important than getting the overall feel of the block to impact the format. We look at some mechanics and say, "This mechanic will have a Standard deck based around it," and others and say, "This mechanic will have sweet individual cards that we can get to work in Standard." Devotion is an example of a mechanic that ends up creating decks around it, while monstrosity is pretty hard to make a deck around, so we instead tried to create individual designs that would show up in existing decks, like Polukranos, Stormbreath Dragon, and Fleecemane Lion. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Stormbreath Dragon" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Stormbreath%20Dragon&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Fleecemane Lion" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Fleecemane%20Lion&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Of course, theme is often different than the exact mechanical tie for the set, but we want each year's Standard to be dramatically changed by each block, and to allow for the years to feel different due to the new thing that each block is doing. The design theme behind *Theros* is that the enchantments are the work of the Gods, which puts the source of the enchantments front and center—getting the set to work as a whole meant getting the Gods to work. We also knew from the get-go that the Gods were going to make up five of the fifteen mythic rare slots in *Theros*, and take up a full half in both *Born of the Gods* and *Journey into Nyx*. We use the mythic rare slot to show off some of the most interesting and unique cards in our sets, so it really wasn't an option to have the cards fall flat—we needed them to be awesome. Thankfully, Erik Lauer and his team managed to come up with a (relatively) simple design that used text on the cards that we had never really used before, with enough knobs to tweak that development felt we could make good use of the cards. 

### Taking Risks

The goal of the [Future Future League](https://web.archive.org/web/20140328000000/http://www.wizards.com/magic/magazine/archive.aspx?tag=Future_Future_League) isn't to produce sets that have zero chance of ever seeing cards in them banned in Standard. We want to keep the odds low—about one every ten years—but we need to take enough risks that things are exciting. The big risk for *Theros* was that the Gods would be too strong, since as they spend much of their time as simply indestructible enchantments, they are incredibly hard to deal with, but very unequally with colors. We could've made them not indestructible, but we also felt it was important that they were hard to deal with. It created challenges for us, developmentally, but (much like in design) restrictions breed creativity. 

Our goal for the Gods was to power the cards to the point where the enchantment half of the cards aren't quite worth playing in Constructed if there are no creatures attached to them. We knew that we wanted these cards to mainly show up in decks that could reliably turn them on. It meant, though, that the cards would be incredibly powerful once turned on. The Gods are not small creatures, and they will quickly take over a game if they are ever actually allowed to attack. We like things like this—fun and powerful cards that bring the game to a conclusion are good for the environment as a whole. It's when we occasionally print cards that are powerful, not terribly fun, and don't bring the game to a conclusion, that we run into problems.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Heliod, God of the Sun" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Heliod,%20God%20of%20the%20Sun&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Thassa, God of the Sea" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Thassa,%20God%20of%20the%20Sea&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### Risk Mitigation

Part of getting the Gods to work was getting devotion to work—something I think it is safe to say has showed up a bit this year. In terms of fully powering it up, we couldn't have asked for much better than the hybrid cycles of the previous year, specifically the HHH cards in *Gatecrash*, such as Boros Reckoner and Nightveil Specter, but also the lowly HH of Burning-Tree Emissary. The fact that they were in creature form (and not enchantment) also meant that every deck that wanted to maximize its ability to turbo-up the devotion for its Gods would be susceptible to some creature removal, meaning there was a good place for the metagame to go to even if the Gods were a bit too strong. 

Beyond the mechanics, though, we also knew we wanted to seed some cards in the block that would see play if we were wrong. Then, over time, we could add more to the format so players who were tired of not being able to kill Gods would have options. Very early on, Erik Lauer knew he wanted Thoughtseize in the set. We knew from the get-go that it isn't the most fun card, but we also knew it would give black a way to deal with Gods, and enchantments as a whole, if we ended up low on their power-level estimates. We had just lived through two years of black being pretty heavily underrepresented with Scar's block, due to its inability to deal with artifacts (and, more specifically, the Swords), and didn't want to see another two years where black couldn't deal with enchantments. We also added Fade into Antiquity to *Theros* to give green a Limited card that could show up in Constructed as a "measure of last resort" in Standard, for at least a few months. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Boros Reckoner" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Boros%20Reckoner&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Thoughtseize" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Thoughtseize&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### Finding the Right Designs

For cards like the Gods, a lot of the design work actually happens in development. Generally, design gets the overall picture very close to what we want, and development needs to sculpt the cards to get them to the right level to see play in Standard. So, while we knew what Heliod, Nylea, Mogis, and Xenagos were about, we needed to figure out how to translate that into cards that could see play in Standard.

What we settled on for the Gods in *Theros* were creatures that added enchantment-like abilities that were always active, and activated abilities. These Gods also got weapons, so we tried to figure out a way to make all of these abilities work in some way that made sense—for example, Erebos's whip gains you life to use for his card-drawing ability. Purphoros's hammer makes tokens, which have haste due to the Hammer's own ability, and enter and deal 2 damage to each opponent due to Purphoros's "whenever a creature enters the battlefield" trigger. etc., etc. Beyond even that, the abilities on the creatures were tailored to be ones that helped out actual decks that we were playing in Standard. Nylea gives trample in part because we saw how much of a problem green decks were having dealing with Elspeth, Sun's Champion, and she provided a great solution for beating those decks. We tried to make these Gods do generically what the creature-based decks in these colors wanted them to do, hoping they would have a high chance of being one-ofs or two-ofs in a lot of decks—as aiming these at four-ofs becomes hard when dealing with legendary creatures that don't often die. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Erebos, God of the Dead" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Erebos,%20God%20of%20the%20Dead&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Whip of Erebos" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Whip%20of%20Erebos&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

For *Born of the Gods*, we took a somewhat different approach. With its two-color Gods, we had a much better idea of exactly which decks would want to play each God, and tried to tailor those Gods to fit into those decks. For example, Xenagos was clearly created to fit within a Red-Green Monsters deck, which it has in the current Standard. Ephara was meant to work in weenie-type decks that could create tokens, Mogis in aggressive black-red decks, Phenax in mill-control decks (Try him with Wall of Frost. It's pretty cool.), and Karametra in ramp decks. Due to the nature of these Gods, we knew they would be less likely to show up in as many decks in Standard as the *Theros* Gods, but they would be more impactful in the strategies they did show up in. Up until this point, I would say these Gods have underperformed against our expectations a bit, but I think there is still room for them to find their own footing as the metagame continues to shift in the next year and a half they are in Standard. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Xenagos, God of Revels" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Xenagos,%20God%20of%20Revels&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Phenax, God of Deception" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Phenax,%20God%20of%20Deception&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

In a few short weeks, you will get to see what the Gods look like in *Journey into Nyx*. How will these Gods stack up next to the *Theros* and Born Gods? I guess time will tell. 

Until next time,  
 Sam ([@samstod](https://twitter.com/@samstod)) 

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_Details_Static.png)](/en/articles/event-coverage/undated/friday-night-magic-6) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_Info_Static.png)](https://web.archive.org/web/20140424103615/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/bornofthegods) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_CIG_Static.png)](https://web.archive.org/web/20140328000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?set=[%22Born%20of%20the%20Gods%22]) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140328000000/http://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[Developing%20Gods%20for%20Standard]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325153238/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 