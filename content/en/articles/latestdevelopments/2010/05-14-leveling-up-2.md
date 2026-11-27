---
id: 9a4a07r3
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/05-14-leveling-up-2
title: Leveling Up
published: '2010-05-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 623782
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
    captured_at: '2013-09-21 14:09:22+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 623782
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
    captured_at: '2013-09-21 14:09:22+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 623782
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
    captured_at: '2013-09-21 14:09:22+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 623782
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
    captured_at: '2013-09-21 14:09:22+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 9a4a07r3
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90
  lang: en
  template: aspx
  captured_at: '2013-09-21 14:09:22+00'
  capture_id: 623782
  wayback_url: https://web.archive.org/web/20130921140922id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9a4a07r3
  capture_id: 623782
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
  wayback_url: https://web.archive.org/web/20130921140922id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/90
  captured_at: '2013-09-21 14:09:22+00'
  template: aspx
  sha256: 018c852ed59a2d5c9c877b27be1fc8910bad61f3da1e7f11dfa75f1e6cf58053
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Figure of Destiny
  occurrences: 1
---
![](https://i.ormos.uk/ff/45/ff45980db694abc1c502bf75e169bf5590fc347e701649265625efbb6ec841c4.jpg)

his is the end of Level Up Week on DailyMTG.com. Today I'll talk about two parts of the design and development process that the level up creatures went through.

**Magic** is a game of decisions. Most players who have played **Magic** for a while like staying active in a game by making decisions. Limited games that go on for a long time can make players feel that their decisions don't matter anymore. *Rise of the Eldrazi* games were going to go longer than most games. This risked making it feel too non-interactive. Brian Tinsman patterned the level up mechanic after his popular card Figure of Destiny. We, the developers, liked how level up kept players engaged through long games. We chose to put it in the common rarity to ensure that level up cards were in Limited decks.

The level up ability can be played only when you could cast a sorcery. Some players have expressed disappointment about this. **Magic** is a great game because it is challenging to play. We don't think that challenge should come from difficulty processing what the cards on the board do. Level up creatures that leveled at instant speed would have been very hard to process in combat because they change in unpredictable ways. We print some creatures that change size in combat already. We print them in ways that make them easy to process. We also try to print them in small quantities. Putting level up creatures at common with instant-speed leveling would have made board states harder to process than we like. This is why level up is a sorcery-speed ability. 

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <a href="/en/articles/latestdevelopments/2010/05-14-leveling-up">&#10;          <img src="https://i.ormos.uk/80/a5/80a55e46846a1376163cc928a147e71b5416b3677ccde15987d4a35c0addf263.png">&#10;        </a>&#10;      </td>&#10;      <td> Leveling Up has commas and semicolons. </td>&#10;    </tr>&#10;  </tbody></table>