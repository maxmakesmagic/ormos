---
id: wtb1mgw6
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/05-10-splitting-costs
title: Splitting Costs
published: '2013-05-10'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    lang_detected: en
    capture_id: 734875
    url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    captured_at: '2022-08-17 23:43:29+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    lang_detected: en
    capture_id: 734875
    url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    captured_at: '2022-08-17 23:43:29+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    lang_detected: en
    capture_id: 734875
    url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    captured_at: '2022-08-17 23:43:29+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    lang_detected: en
    capture_id: 734875
    url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
    captured_at: '2022-08-17 23:43:29+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: wtb1mgw6
  url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
  page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
  lang: en
  template: drupal
  captured_at: '2022-08-17 23:43:29+00'
  capture_id: 734875
  wayback_url: https://web.archive.org/web/20220817234329id_/https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-10
- document_id: wtb1mgw6
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/246
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/246
  lang: en
  template: aspx
  captured_at: '2014-05-09 13:45:32+00'
  capture_id: 620334
  wayback_url: https://web.archive.org/web/20140509134532id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/246
- document_id: wtb1mgw6
  url: https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-07
  page_key: magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-07
  lang: en
  template: drupal
  captured_at: '2021-11-27 02:18:44+00'
  capture_id: 734873
  wayback_url: https://web.archive.org/web/20211127021844id_/https://magic.wizards.com/en/articles/archive/latest-developments/splitting-costs-2013-05-07
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: wtb1mgw6
  capture_id: 620334
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/246
  wayback_url: https://web.archive.org/web/20140509134532id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/246
  captured_at: '2014-05-09 13:45:32+00'
  template: aspx
  sha256: f27db3f4daa6dca86c8b9183ddbe4f6eb3adfb48e0dd5b26823afbd6e1b16241
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Deathrite Shaman
  - Voice of Resurgence
  - Geist of Saint Traft
  - Snapcaster Mage
  - Thragtusk
  - Sphinx's Revelation
  - Assault & Battery
  - Battery
  - Assault
  - Shock
  - Fire & Ice
  - Crime & Punishment
  - Far & Away
  - Thought Scour
  - Reach Through Mists
  - Turn & Burn
  - Burn
  - Burning-Tree Emissary
  - Turn
  - Wear
  - Tear
  occurrences: 29
---
Mana costs are one of the more interesting, nuanced parts of **Magic** and, in my opinion, one of the most difficult parts of both design and development. The problem is that there aren't really great goalposts for what exactly one mana is worth, and even if there were, they wouldn't be that useful. Making a 1/1 with a small upside generally costs a white or green mana. Drawing a card generally costs one blue mana. Dealing 2 damage generally costs one red mana. Forcing an opponent to discard a card generally costs one black mana. If we were playing the one-mana game, things would be easy, but costs tend to get more complicated when you begin to scale cards up. 

![](http://media.wizards.com/images/magic/daily/ld/ld246_onemana.jpg) 

  

Scaling up costs and effects are far from simply additive. If they were, then the progression of burn spells would get out of hand pretty quickly. ![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif) deal 4? That card would be pretty powerful. Instead, the 3rd damage usually costs one more mana. Want to do a 4th damage? All of a sudden, at three mana the card either has a downside or restricts what it can target. And 5 damage? It gets even steeper. Every time you play a card from your hand, that resource is taken into account when the cost of the effect is calculated. So, drawing a single card is often costed at ![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif), but two cards is generally ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif). Moving up, by the time you get into three-card range, you are generally paying at least four, and more likely five mana. On the other hand, power and toughness for creatures do scale up well. It is not uncommon to see 2/2s for two, 3/3s for three, and 4/4s for four with upsides, and you will sometimes get an even better deal than that. And these are cards with simple effects that are easy to scale—it is much harder when you begin to get more complicated cards like Deathrite Shaman, Voice of Resurgence, or Planeswalkers. 

While it may not have always been true in the early days of **Magic**, we have become good enough at costing cards appropriately now so that it is pretty rare to find a single card in Standard that would see much main-deck play at even one more mana. Top tournament cards like Geist of Saint Traft, Snapcaster Mage, Thragtusk, and Sphinx's Revelation start looking pretty haggard after adding a mana to them; although not always out of the realm of possibility, they would not be the dominating forces that they are. If the option was to just choose the cards we want to be good in Standard and add a mana to everything else, the path would be simple, but that's not our goal. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Snapcaster Mage" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Snapcaster%20Mage&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Sphinx's Revelation" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Sphinx%27s%20Revelation&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

As [I've mentioned](/en/articles/latestdevelopments/2013/02-15-developing-standard) [in previous articles](/en/articles/latestdevelopments/2013/05-03-balancing-for-fun), our goal with balancing cards for Standard is to make a large enough environment that there are plenty of things to do, and enough possibilities to keep the metagame evolving. The challenge in development is figuring out what else about a card can change to get it to where we are happy with its power level after we've gotten it to the correct mana cost. This part of the process is where we have a lot of room to create fun and interesting cards. Costs can still change in this period if we find that new text that improves the card justifies the extra mana. 

The other part of the cost equation, and part of the area where we have a lot of room to expand, is versatility. You always pay a cost for versatility. There is an age-old struggle built into **Magic** between playing cards that are full of raw power, but are narrow, versus cards that are slightly less powerful, but give you options in how to use them. Generally, if a card can be played as an instant, it costs slightly more than a version that is a sorcery, or is slightly less powerful. Burn that targets either creatures or players is generally more cost effective than ones that can target both. X spells are almost always a "bad deal" on each individual line on the curve, but more than make up for it because other spells don't give you unbounded options for damage, card draw, or lifegain. Deciding when it is appropriate to fill your deck with power, or when with versatility, and then deciding what is the appropriate mix in between, are some of the most engaging parts of **Magic** deck building and something that keeps formats constantly evolving. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Syncopate" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Syncopate&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Aurelia's Fury" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Aurelia%27s%20Fury&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

One of the fascinating parts of working on **Magic** is that the resource system is only so granular, and that leads to the truism that restrictions breed creativity. An alternative-reality version of **Magic** may be able to charge you fractional resources, create 3.1/3.6 creatures, or do fractional damage, but outside of *Unhinged*, if a card is teetering between two and three mana, it is development's job to decide what to charge for that card. Some of that can be made up by moving costs between ![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif) and ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif), and sometimes gold options are also there to find better ways of making up for the power of a card by increasing the difficulty to cast it. In the end, though, a lot of development's work is taking the cards that made it through from design and figuring out how and when their costs and effects need to be adjusted to fit better at the right whole numbers. This is without really even getting into the amazing cavalcade of options available with power and toughness, but that will have to wait for another article. 

With all of that out of the way, I want to talk about split cards and what they have to do with this equation. Split cards, when they were originally developed, took these rules into account, and tended to charge about half of one mana more than you would generally expect to pay or ding the card in another way. Looking at an old split card, Assault & Battery, Batteryis one mana more than you would generally pay for a 3/3 token, and Assault, being a sorcery-speed Shock, was generally worse than other options at the time. If you were playing a red-green deck, however, you were more than happy to include the card in your deck, because of the versatility it provided. In no other split card from the original batch is this more evident than Fire & Ice, where both halves are not quite good enough for a tournament-caliber card, but it has seen a huge amount of tournament play because of how amazingly versatile it is, sometimes slowing an opponent down on turn two or delaying an attacker and replacing itself, sometimes killing a creature. 

![](http://media.wizards.com/images/magic/daily/ld/ld246_assault.jpg) 

  

Fuse added an interesting new twist to split cards and how we created them. While the names were related before, the effects were not. There was no need for Crime & Punishment to have any kind of interesting interaction because you were casting one side or the other. On returning to split cards in *Dragon's Maze*, and with the addition of fuse to give them something new, it was important to the design that the cards interact. Each side needed to stand on its own, but also to create its own two-card combo if the card could be fused. This was not a simple task, but I believe all the work that went into finding cards that were fun and interesting was well worth the effort. 

When it came time to develop these, more work had to go into making sure that each card was appropriately costed for all three of its modes, since the cards were designed to be more powerful when fused together. In effect, the costing I mentioned earlier where you take into account the versatility is built into the card as well as the additive properties. Far & Away each cost about a mana more than you'd probably expect to pay for both the sacrifice and bounce effects, but the sum of the two isn't two mana overcosted, it's much closer to one. There were a few where the fused cost was actually probably a bit cheap for what we would've charged for the effect, and so there were a few "back to the drawing board" moments. It was important to find not only the right costs, but also effects that behave appropriately when fused, while still being interesting and fun. 

Imagine we had made this split card:

> U/R  
>  Draw/Burn  
>  Sorcery/Sorcery  
>  Draw a card./Deal 2 damage to target creature.

The card isn't very interesting—just ![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif) to draw a card is not an effect we do much unless there is reason or a good rider to stick on it (for instance, Thought Scour or Reach Through Mists), so the card probably wouldn't have existed. Other than that, this card would've been possible under older split card versions, but it quickly becomes more powerful than what we generally print today in concert with fuse. In order to get the card to work as a fuse card, we would probably have to cost it closer to ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)/![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif). None of that fixes the fact that the card just wouldn't fit under the criteria we were looking at for fuse. 

Turn & Burn goes a very different direction, and instead of attempting to just have each half worth an easy card, it finds two effects that can combine well into one powerful effect and sometimes be worth two cards. There will be attack steps that you can Burn your opponent's Burning-Tree Emissary andTurn his or her Thragtusk for a very effective block, but you have to work to get that value out of it, which is how all of the fuse cards work. Value is fun, but it is more fun if there is some kind of hoop you need to jump through to get it, rather than if it is just given to you. Hopefully, this means that when you do decide to fuse Turn & Burn on a single target to get rid of a larger creature, you don't feel like you missed out on something—you just took the value you were given and used it in the right way. 

![](http://media.wizards.com/images/magic/daily/td/td242_4_juhna278zk.jpg) 

  

I hope the selection of fuse cards we came up with accomplishes the goals we had when we set out to make them—fun and versatile cards that would make for more interesting games of **Magic**. I know that in my playing, I have had a lot of fun attempting to get two-for-ones out of Turn & Burn, and bouncing my own creature with Far & Away for good effect, while also appreciating the times when using a Wear by itself was worth more than holding out hope my opponent would cast an enchantment to Tear. I believe it is precisely these kinds of decisions that keep **Magic** interesting, and I hope we can bring more of them to you in the future. 

![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueNow_Top.jpg) ![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueNow_leftOfButton.jpg) [![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueNow_Button_Static.jpg)](/en/events/2011/league-facts/avacyn-restored-league) ![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueNow_RightOfButton.jpg) [![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueNow_Bottom_Static.jpg)](https://web.archive.org/web/20140425110727/http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/dragonsmaze/productinfo) 

  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130510000000/http://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[Splitting%20Costs]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130510000000/http://staging.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325153238/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 