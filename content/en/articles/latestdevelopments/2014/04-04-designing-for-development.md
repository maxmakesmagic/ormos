---
id: 27d653nb
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/04-04-designing-for-development
title: Designing for Development
published: '2014-04-04'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: shawn-main-ef65c5d3
  name: Shawn Main
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    lang_detected: en
    capture_id: 720539
    url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    captured_at: '2022-08-16 01:28:26+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    lang_detected: en
    capture_id: 720539
    url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    captured_at: '2022-08-16 01:28:26+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    lang_detected: en
    capture_id: 720539
    url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    captured_at: '2022-08-16 01:28:26+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    lang_detected: en
    capture_id: 720539
    url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
    captured_at: '2022-08-16 01:28:26+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 27d653nb
  url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
  lang: en
  template: drupal
  captured_at: '2022-08-16 01:28:26+00'
  capture_id: 720539
  wayback_url: https://web.archive.org/web/20220816012826id_/https://magic.wizards.com/en/articles/archive/latest-developments/designing-development-2014-04-04
- document_id: 27d653nb
  url: https://magic.wizards.com/en/articles/archive/designing-development-2014-04-03
  page_key: magic.wizards.com/en/articles/archive/designing-development-2014-04-03
  lang: en
  template: drupal
  captured_at: '2022-06-28 16:19:46+00'
  capture_id: 301838
  wayback_url: https://web.archive.org/web/20220628161946id_/https://magic.wizards.com/en/articles/archive/designing-development-2014-04-03
- document_id: 27d653nb
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/293
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/293
  lang: en
  template: aspx
  captured_at: '2014-04-23 13:58:10+00'
  capture_id: 620798
  wayback_url: https://web.archive.org/web/20140423135810id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/293
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 27d653nb
  capture_id: 620798
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/293
  wayback_url: https://web.archive.org/web/20140423135810id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/293
  captured_at: '2014-04-23 13:58:10+00'
  template: aspx
  sha256: 42e8e71146b18f66f2df66919b2eb0cc18e67beddd71f55492e6b24a3bfbfe3d
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Thespian's Stage
  - Akroan Horse
  - Dampen Thought
  - Kodama's Reach
  - Peer Through Depths
  - Heliod's Emissary
  - Thassa's Emissary
  - Erebos's Emissary
  - bear
  occurrences: 12
---
Greetings! My name is Shawn Main. My proudest accomplishments include directing a punk-rock adaptation of Euripdes's [*Bakkhai*](http://en.wikipedia.org/wiki/The_Bakkhai), coming in 2nd in the [Great Designer Search 2](/en/articles/feature/2011/03-07-the-great-designer-search-2), and lead-designing the *Conspiracy* set, which comes out this summer. 

![](https://i.ormos.uk/10/1e/101e5182aca13bfa59096088f6f550d49c5247e492db14f6a54cd22ea588b2cd.jpg) 

  

So why am I introducing myself and talking about things that aren't **Magic** development? Because Sam asked me if I could step in for him this week to talk about being an outsider. Well, it was more specific than that. He asked me to talk about being a **Magic** designer on a development team. 

### Two Teams Diverged

R&D is built on the notion that specialization is necessary, but that crosspollination is critical. This philosophy is apparent in every aspect of our work. For example, the design and development teams each sit together, but are separated by only the low cubicle walls of the Pit, so conversations can flow back and forth.

Design and development (along with creative, editing, and the rest of the company) ultimately have a singular goal: making awesome card sets. The main difference is that we're handling the cards at different stages in their lifecycle, so we put our attention on different areas, and, as a consequence, require slightly different skill sets.

At its essence, design is responsible for vision, development for execution. Mark Rosewater's favorite metaphor is that designers are deck builders and developers are deck tuners. My own background is theater, so I prefer to think of designers as playwrights and developers as stage directors. The first group imagines the story, while the second deals with the realities of bringing those words to life.

![](https://i.ormos.uk/8b/07/8b07177402bea45a2a6714f81df943512cab6f2820844f9802d8ae0b07758262.jpg) 

Thespian's Stage | Art by [John Avon](https://web.archive.org/web/20140404000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22john%20avon%22])

As a consequence, design does a great deal of blue-sky thinking—"How might we represent the gods of ancient Greece in **Magic** terms?" Whereas, development deals with more practicalities—"Does this expression of the gods work? Can we simplify it? What's the right devotion threshold for two-color Gods?" 

But while each team has a different focus, each needs to consider the work of the other. Design teams always have a developer responsible for tasks like card costing and preventing challenges down the road by considering questions like, "Is this mechanic developable?" And similarly, development teams always contain a designer. The majority of the designer's work is simply being part of the team, participating in playtests, and giving feedback about what is and isn't working, but the designer does have three specific responsibilities.

### 1\. Keep the Design Vision in Mind

Late in design, the lead will create a handoff document, detailing the set's vision. This document explains the goals for the set and what's been done to achieve those goals—themes, mechanics, major card cycles. The handoff document is an important guide because the card set will change heavily during development and the vision should be maintained even as individual cards come and go.

The designer on the team has the responsibility of ensuring that this document is observed. For example, during *Theros* development, one of my important tasks was protecting flavorful designs that looked out of place. Akroan Horse didn't particularly connect to Limited archetypes and the card looked strange stripped of context, so there was a temptation to remove the card to free up space, but individual flavorful designs were critical to establishing the Greek-inspired world of Theros. 

 ![Akroan Horse](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Akroan%20Horse&options=) 

  

### 2\. Provide a Different Viewpoint

![](https://i.ormos.uk/fe/34/fe34f06959c9e34c01d96f8a6cf018f2fd2e16b1d43c90843d21610e29d6c40b.jpg) 

Outside of work, I regularly draft and play Commander, Planechase, and Momir Basic. I made up a Constructed format called Gatherer-Terrible, where you're restricted to cards rated [less than 2 on Gatherer](https://web.archive.org/web/20140404000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&rating=+%3C[2]). I just finished putting together FlavorCube, built from the most flavorful cards in the history of the game. And one of my favorite things is teaching the game to brand-new players. That is to say: the ways I'm excited to play **Magic** often look pretty different from those of the average developer. 

Developers are drawn from the crème de la crème of professional **Magic** players. This gives them a deep insight into the mindset of competitive players, which is absolutely critical. But there are many different types of **Magic** players in the world, playing the game in myriad ways, and we need to make the game for all of them. 

While some designers have tournament credentials (Ken Nagle played on the Pro Tour, Dan Emmons was a JSS finalist), designers are often better at representing the kitchen table experience. And it becomes the designer's responsibility to simply provide a different point of view, particularly keeping in mind how less-experienced players might interact with cards.

During *Modern Masters* development, we wanted draft archetypes that echoed popular Constructed decks like Faeries and Storm, but we needed to find strategies for certain color pairs. I have a great love for quirky draft archetypes, so I suggested trying the zero-creatures Dampen Thoughts deck from triple-*Champions of Kamigawa* Draft. We already knew we wanted some arcane spells like Kodama's Reach and Peer Through Depths, so the strategy fit and let players relive one of the most unique Limited strategies ever. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Kodama's Reach" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Kodama%27s%20Reach&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Peer Through Depths" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Peer%20Through%20Depths&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### 3\. Design Cards

Everyone in R&D is adept at designing individual cards. Seriously. I'm pretty sure that every designer and every developer has made at least one card that you absolutely love. So why does this get listed as a designer task when the development team would already be eminently capable? Well, the thing designers tend to be especially good at is designing quickly. This is a valuable skill because we're willing to try out a LOT of new ideas, so there's a constant churn as we add cards to a set, playtest, evaluate, kill the cards that aren't playing right, and design new cards to try again.

For example, during *Theros* development, after reshuffling some bestow abilities and using up the most logical keywords at common, we needed simple lines of text for the uncommon bestow cards. We could have stopped the meeting and had everyone bring back ideas next time, but I was the designer on the team and Erik Lauer looked to me to rattle off a dozen suggestions—lines of text that were simple, grokable, familiar, and that I thought would be fun for both Auras and creatures. Then the developers pored over those suggestions, debated them, and put into the file the cards that would go on to be Heliod's Emissary, Thassa's Emissary, and Erebos's Emissary. 

![](https://i.ormos.uk/71/55/7155837af00fc1043102f9715d9fe8694eef0a615b85e15456df4080067b2d30.jpg) 

  

### Many Hats

When I started in R&D three years ago, one of the biggest surprises for me was how much overlapping work was being done simultaneously. I'd consistently read Making Magic and Latest Developments since their inception, but was unprepared for the scope. To give a sense of the pipeline right now—two sets are in active design, one set is in predesign, one set has been having a few meetings before starting design, three sets are in development, and three supplemental products are in development (assuming I'm not forgetting anything!). There are only six core designers and eight core developers, which, if you start doing the math, means that everyone is wearing a lot of hats. 

This sometimes gives you focus whiplash. One meeting might be early predesign, where you're talking about world design and how different sets relate to a three-act story structure and, during the next meeting, you might be balancing commons across the colors—asking very focused development questions like "Should this creature be a 3/3 or a 3/4?" But working across multiple sets at once itself creates valuable cross pollination—bringing the knowledge of one set's development plan is often very useful to the following set's design. So while we segment into two different teams, the process at every level functions less like a conveyor belt and more like a conversation.

Thanks for letting this outsider talk about a different perspective on development.  
  
 Shawn (exit, pursued by a bear)  
[@shawnmain](https://twitter.com/@shawnmain)

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_Details_Static.png)](/en/articles/event-coverage/undated/friday-night-magic-6) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_Info_Static.png)](https://web.archive.org/web/20140424103615/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/bornofthegods) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_FNM_CIG_Static.png)](https://web.archive.org/web/20140404000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?set=[%22Born%20of%20the%20Gods%22]) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Shawn Main](https://i.ormos.uk/f8/3b/f83b7c2d164a18a665378b13e7adec05a979b390fc07e360fae3fdfa6f560cab.jpg "Shawn Main")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Shawn Main</b>&#10;        <br>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140404000000/https://www.wizards.com/company/emailtoauthor.asp?author=Shawn%20Main&amp;amp;headline=[Designing%20for%20Development]">Email Shawn</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20140110115422/http://www.wizards.com/magic/magazine/archive.aspx?author=shawn%20main">Author Archive</a>&#10;        <br>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Shawn Main is a designer for **Magic: The Gathering**. He joined Wizards of the Coast from the [Great Designer Search 2](/en/articles/feature/2011/03-07-the-great-designer-search-2) after years of directing theater, training medical students, and playing multiplayer **Magic**. 

 