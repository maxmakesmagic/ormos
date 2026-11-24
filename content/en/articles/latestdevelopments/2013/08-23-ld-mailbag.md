---
id: dprg19fe
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/08-23-ld-mailbag
title: LD Mailbag
published: '2013-08-23'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    lang_detected: en
    capture_id: 620560
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    captured_at: '2014-02-15 01:38:14+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    lang_detected: en
    capture_id: 620560
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    captured_at: '2014-02-15 01:38:14+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    lang_detected: en
    capture_id: 620560
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    captured_at: '2014-02-15 01:38:14+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    lang_detected: en
    capture_id: 620560
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
    captured_at: '2014-02-15 01:38:14+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
  duplicate_sources:
  - v56kx4rq
sources:
- document_id: dprg19fe
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
  lang: en
  template: aspx
  captured_at: '2014-02-15 01:38:14+00'
  capture_id: 620560
  wayback_url: https://web.archive.org/web/20140215013814id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
- document_id: v56kx4rq
  url: https://magic.wizards.com/en/articles/archive/latest-developments/ld-mailbag-2013-08-23
  page_key: magic.wizards.com/en/articles/archive/latest-developments/ld-mailbag-2013-08-23
  lang: en
  template: drupal
  captured_at: '2022-08-15 07:58:21+00'
  capture_id: 723454
  wayback_url: https://web.archive.org/web/20220815075821id_/https://magic.wizards.com/en/articles/archive/latest-developments/ld-mailbag-2013-08-23
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: dprg19fe
  capture_id: 620560
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
  wayback_url: https://web.archive.org/web/20140215013814id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/261
  captured_at: '2014-02-15 01:38:14+00'
  template: aspx
  sha256: dcb99f57dde38c60c6541a929e87ea6bd7dfd8c41da7f48265942e50e35a19bf
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Astral Steel
  - Ground Rift
  - Hindering Touch
  - Domri Rade
  - Sorin, Lord of Innistrad
  - Jace, Memory Adept
  occurrences: 10
---
On this week's Latest Developments, I decided to open it up to a mailbag. I asked you all for some questions, and you responded! I don't have the room to respond to all of them, but I did get to a few. I hope that this can become a regular feature of the column, so keep sending them into me, and I will get to them on a semi-regular basis.

First off, one from one of my trusty editors, Mike:

**Mike McArtor: How many different sets/products does a developer work on at any one time?** 

Simple answer: Many. Long answer: We have between one to three sets in design at any given time (each of which needs one core developer), and two to four sets in development (each of which needs two or three core developers). And that is only looking at the four main expansions, without getting into all the various ancillary products that we produce. For me, I am currently on the design team for one set (for which I will also be on the development team), finishing up development of another, leading three ancillary products, and hopefully getting ready to lead my first expansion in a few months. So, yeah, it can get pretty busy at times. On any given day, I can be working on two years or more of **Magic** products in the pipeline. 

Of course, even when you aren't actively working on a set, it is expected of developers to spend some time going over the other sets in development and making notes in Multiverse, as well as participating in the [FFL](/en/articles/latestdevelopments/2013/08-16-days-of-future-future-part-2), so even when you aren't working directly on a set, you are providing input to the people who are. 

> [@samstod](https://twitter.com/samstod) What percentage of cards go through development unchanged? 
> 
> &mdash; Wil Blanks (@HairlessThoctar) [August 16, 2013](https://twitter.com/hairlessthoctar/statuses/368243363603963904)

  

At the most basic level, almost everything gets changed a bit, but many of the changes aren't what might be considered meaningful. Creature types can change if they aren't important, or the wording might be reworked to prevent some kind of weird rules loophole or to reduce clicks on **Magic Online**. We might change a card from ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif) to ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif) and leave the rest intact—do you consider that a change? I would, but it might not be the kind of changes you are expecting. 

I'd estimate that something like 60–80% of the cards that start off in a design handoff file get either eliminated or have some kind of meaningful tweak to them—be it changes to power and toughness, abilities, or casting cost. There are just too many knobs on any given **Magic** card to not turn one of them. Development may be playtesting Limited and find that white-blue isn't working because all of their good commons exist on the same curve points, so we will do the necessary changes to move a card or two up or down a mana to make the deck work better. We don't do it because there was something wrong with the initial card, just because the iteration that sets need to go through to improve requires that things change over time. 

Development attempts to fulfill design's vision of a set, but doing so means a lot of changes. I like to think of it this way—design writes the book, and development makes the movie version. We take the plot, structure, and characters that design hands over and try and concentrate what we believe is working and reduce the focus on (or remove) what isn't. Sometimes, that means adding new characters, combining others, or removing subplots, but we do so to fit it all into the constraints of a two-hour runtime. In this case, the runtime is Standard. Okay, so, yeah... the metaphor sort of breaks down at some point, but the process of working together to produce sets creates what we believe to be a better product as a whole.

![](http://media.wizards.com/images/magic/daily/ld/ld261_dontflipitsnotactuallyarealmovie.jpg) 

  

> [@samstod](https://twitter.com/samstod) Great article again. Quick Q: Does dev have a list of &quot;red flags&quot; such as &quot;generates 2+ mana&quot; or &quot;casts without paying mana&quot;? 
> 
> &mdash; Bassim El-Wakil (@Bass\_Wakil) [August 17, 2013](https://twitter.com/bass_wakil/statuses/368716404632977409)

  

We look out for a lot of things, but the main ones that we know we have to test are:

*   Cheap card draw
*   Free spells
*   Spells that generate mana
*   Spells that have a repeatable effect that doesn't use mana
*   Expensive cards with ETB abilities

A large percentage of the really huge mistakes in the *Urza's Saga* era, for example, may have been solved by just using that above criteria and giving all of those cards some extra TLC. Also, if you ever find a card with the phrase "if you played it from your hand" on it, you can bet that someone decided to add that to keep anything too crazy from happening. 

> [@samstod](https://twitter.com/samstod) How often does Development have to scrap an entire mechanic for various reasons? 
> 
> &mdash; Joel Smith (@SweetoothTKC) [August 14, 2013](https://twitter.com/sweetoothtkc/statuses/367712699020374016)

  

It happens occasionally in development, although it occurs more often in design or "devign" through contact between the design and development teams. The usual question tends to be, "Is this a mechanic that development thinks they can work with?" Some mechanics just aren't. It may be working in design, but the mechanic just doesn't lend itself to enough cards (often cards that would be interesting in Constructed), or there is no meaningful way to tweak the cards in ways that matter. If a mechanic naturally gets around one of the red flags I mentioned above, then it is on thin ice unless we can figure out a way to let development do some fine tweaking on the cards.

The final reason we might cut a mechanic is because the requirements on how to cost the cards make them unappealing. It might make them balanced, but the goal is to make cards that are both balanced and appealing. If making the card balanced takes away the second part, then it might be time to find a new mechanic.

> [@samstod](https://twitter.com/samstod) Do you believe Storm can be fixed? 
> 
> &mdash; Joel Smith (@SweetoothTKC) [August 14, 2013](https://twitter.com/sweetoothtkc/statuses/367707506706894848)

  

This is very much a follow-up to the previous question. Storm can be fixed in the sense that we could print more cards with storm and put them in a set and not have them break Standard, or Modern, or even Legacy, but those cards are probably not very exciting. Storm has the inherent problem that the only way the cards will see play is in decks that are going to abuse them. This makes it incredibly hard to make interesting storm cards for Constructed without risking breaking them. It would also put a lot of restrictions on what kind of cheap spells we could print for the year before or after.

We could produce more storm cards like Astral Steel, Ground Rift, or Hindering Touch, but I suspect that is not what people are hoping for if we were to announce that storm is a returning mechanic in some block. I think that keywords like replicate, overload, or multikicker end up doing a lot of the work that storm does while still giving the cards the kind of knobs that development would be happier being able to work with. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Astral Steel" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Astral%20Steel&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hindering Touch" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hindering%20Touch&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

> [@samstod](https://twitter.com/samstod) do you guys have cycles of dual lands preprepared for future blocks, or come up with them at the time 
> 
> &mdash; Dean Convery (@DeanConvery) [August 14, 2013](https://twitter.com/deanconvery/statuses/367688223818285056)

  

We have some general ideas on what we are looking to print for the future, but very little set in stone. There are cycles we would like to complete, and various strong ideas of how to make interesting and balanced dual lands, but we sort of need to wait for the right time to release them. If you assume the [shocklands](https://web.archive.org/web/20130823000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+[%22Land%22]&text=+[pay]+[2]+[don%27t]+[tapped]) are about as strong as we want to print a dual land in Standard, and the [*Odyssey* filter lands](https://web.archive.org/web/20130823000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Odyssey%22]&type=+[%22Land%22]&name=%7C[Valley]%7C[Ridge]%7C[Expanse]%7C[Catacombs]%7C[Quarry]%7C[Prairie]) are a little too weak for Standard, then you aren't looking at a very wide band of power—and we have mined a whole lot of the better designs. 

If at all possible, we try and use something thematic to the block we are printing the cards in. The example of this is the [duals that check for creature types](https://web.archive.org/web/20130823000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Lorwyn%22]&type=+[%22Land%22]&text=+[reveal]+[card]) in *Lorwyn*. They will work for as long as the set is in Standard, also give options for tribal decks for the rest of time, and let us save other dual land designs for years that need them or where their explicit design will help in the future—such as the [checklands](https://web.archive.org/web/20130823000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Innistrad%22]&type=+[%22Land%22]&text=+[unless]+[control]) in *Innistrad* providing the base for *Return to Ravnica*–year Standard's mana base. 

> [@samstod](https://twitter.com/samstod) you were always keen on &quot;lorwyn power level&quot; planeswalkers - do you think the last few sets did it right? Or were some too weak? 
> 
> &mdash; Greg (@uselessend) [August 14, 2013](https://twitter.com/uselessend/statuses/367500032661913600)

  

The original *Lorwyn* power level of Planeswalkers is about what we are shooting for when we design new Planeswalkers. Of the five in that set, Jace and Garruk are perhaps slightly stronger than where we would aim a Planeswalker today, while Liliana and Chandra are probably just a smidge too weak. That doesn't mean that we won't have Planeswalkers stronger than Jace and Garruk, or weaker than Liliana or Chandra, but that our estimate of their power will be somewhere between those. We are always going to be a little off in the too-weak or too-strong direction, and making sure there is some room on both ends of that keeps the 'walkers at about the right level. 

The only real problem with Jace and Garruk isn't exactly that they are too strong as cards, but they provide a little bit too much strength while being deck-agnostic. That could be a goal of Planeswalkers, but I think they are much more interesting as cards if they require a little work. It's hard to find a blue deck that didn't want to run original Jace, at least in its sideboard, and original Garruk would fit into about any green deck. What we try to do now is create Planeswalkers that are a little less about raw power through utility, and require a bit more from your deck.

Some good examples of this working in current standard are Domri Rade (who requires a heavy creature commitment); Sorin, Lord of Innistrad (who really needs tokens in your deck to maximize his potential); and Jace, Memory Adept (who works great as a control finisher but can't protect himself). While there have been Planeswalkers that didn't hit over the last few years, some of that is less about the cards themselves and more about the decks those cards went into not being quite strong enough. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Domri Rade" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Domri%20Rade&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Sorin, Lord of Innistrad" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Sorin,%20Lord%20of%20Innistrad&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  
  

* * *

  

That is it for this week. If you have questions for a future mailbag, send them through the email link below here and I will try to get to them in a future article.

Until next time,

Sam

  
  

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

![](http://media.wizards.com/images/magic/daily/footers/M14/EN_M14_ArticleFooter_FNM_Top.jpg) 

[![](http://media.wizards.com/images/magic/daily/footers/M14/EN_M14_ArticleFooter_FNM_Button01_Static.jpg)](https://web.archive.org/web/20140219062636/http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/magic2014/productinfo) [![](http://media.wizards.com/images/magic/daily/footers/M14/EN_M14_ArticleFooter_FNM_Button02_Static.jpg)](https://web.archive.org/web/20140217002906/http://www.wizards.com/Magic/TCG/article.aspx?x=mtg/tcg/magic2014/cig) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130823000000/http://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[LD%20Mailbag]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325153238/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 