---
id: 3vta0pme
kind: article
lang: en
path: /en/articles/youmakethecard2/2003/02-28-you-make-the-card-2-step-3
title: You Make The Card 2 - Step 3
published: '2003-02-28'
column_slug: youmakethecard2
column: You Make the Card 2
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/135
    lang_detected: en
    capture_id: 808840
    url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
    captured_at: '2009-06-03 16:53:06+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/135
    lang_detected: en
    capture_id: 808840
    url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
    captured_at: '2009-06-03 16:53:06+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/135
    lang_detected: en
    capture_id: 808840
    url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
    captured_at: '2009-06-03 16:53:06+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/default.asp?x=mtgcom/feature/135
    lang_detected: en
    capture_id: 2008222
    url: http://wizards.com/default.asp?x=mtgcom/feature/135,,pt
    captured_at: '2005-01-20 17:16:33+00'
    rule: classic.column_marker
    registry_match: registry.explicit
  duplicate_sources:
  - gyb21bnj
sources:
- document_id: 3vta0pme
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/135
  lang: en
  template: aspx
  captured_at: '2009-06-03 16:53:06+00'
  capture_id: 808840
  wayback_url: https://web.archive.org/web/20090603165306id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
- document_id: 3vta0pme
  url: http://wizards.com/default.asp?x=mtgcom/feature/135,,pt
  page_key: wizards.com/default.asp?x=mtgcom/feature/135
  lang: en
  template: classic_asp
  captured_at: '2005-01-20 17:16:33+00'
  capture_id: 2008222
  wayback_url: https://web.archive.org/web/20050120171633id_/http://wizards.com/default.asp?x=mtgcom/feature/135,,pt
- document_id: gyb21bnj
  url: https://magic.wizards.com/en/articles/archive/you-make-card-2-step-3-2003-02-28
  page_key: magic.wizards.com/en/articles/archive/you-make-card-2-step-3-2003-02-28
  lang: en
  template: drupal
  captured_at: '2021-05-03 04:40:18+00'
  capture_id: 1244673
  wayback_url: https://web.archive.org/web/20210503044018id_/https://magic.wizards.com/en/articles/archive/you-make-card-2-step-3-2003-02-28
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 3vta0pme
  capture_id: 808840
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
  wayback_url: https://web.archive.org/web/20090603165306id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/135
  captured_at: '2009-06-03 16:53:06+00'
  template: aspx
  sha256: f0e6e2e8a9d06654f163294f37929b4bae57798fb2a406bfd2c08dfefe68b92c
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Mirari')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Mirari
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Cursed_Scroll')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Cursed Scroll
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:alert("not implemented yet (personlogin)");
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - here
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:alert("not implemented yet (loginsurvey)");
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - Vote now!
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:alert("not implemented yet (mail)");
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - editor@wizards.com
  occurrences: 1
---
For the first “You Make the Card,” the public chose to make a creature.

Been there, done that!

This time--by a wide margin--the people have asked to make a non-creature artifact.

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>Creature or Non-Creature?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Non-creature artifact</td>&#10;    <td>9484</td>&#10;    <td>68.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Artifact creature</td>&#10;    <td>4439</td>&#10;    <td>31.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>13923</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

So, this leads us to the next part of the design phase. But there is a fork in the road. You see, there are two different ways to design **Magic** cards: by flavor and by function.

![Artifact](https://i.ormos.uk/3e/98/3e98d4085759f3cbb14de80ecedcf5a8e724b8a38eece1e7d25361af93c59764.jpg)

### Flavor

This is what we refer to as “top down” design. The idea is that we start by figuring out a cool artifact. Then after we know what the artifact is and what it does, we design mechanics to match. Mirari is an example of a “top down” artifact design. The story called for a round mirrored sphere that enhanced the power of anyone who used it. The design team of *Odyssey* had to then figure out how to translate that ability into a card that would be fun to play.

The upside of this type of design is that it creates cards that drip with flavor. The downside is that it will greatly limit the options for mechanics.

### Function

In this model of design, we start by figuring out what the card does in the game. Once the mechanics are set in stone, we then figure out a flavor that makes sense. Cursed Scroll is an example of an artifact where the mechanics came first and was later given flavor by the creative team.

The upside of this type of design is that it gives the designers the most flexibility for mechanics. The downside is that it’s harder to create a cool connection between flavor and mechanics. Also, this was the path chosen in the first “You Make the Card.” Part of the purpose of this promotion is to give all you a chance to witness different types of design. Thus a second downside of this option is that you would be designing the card the same way you did last time.

So, what should it be? Design by flavor or design by function?

Voting begins today and ends midnight Sunday, March 9.

I’m curious to see what you choose.

You are not logged in. You must be logged in to vote in You Make The Card. To log in and/or register, click here.

 **Vote now!** 

* * *

*Send questions and comments to editor@wizards.com.*