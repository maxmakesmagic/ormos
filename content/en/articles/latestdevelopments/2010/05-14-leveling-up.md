---
id: 5wgt0byt
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/05-14-leveling-up
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
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 173422
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
    captured_at: '2010-08-28 07:52:49+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 173422
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
    captured_at: '2010-08-28 07:52:49+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 173422
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
    captured_at: '2010-08-28 07:52:49+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/ld/90
    lang_detected: en
    capture_id: 173422
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
    captured_at: '2010-08-28 07:52:49+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 5wgt0byt
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/ld/90
  lang: en
  template: aspx
  captured_at: '2010-08-28 07:52:49+00'
  capture_id: 173422
  wayback_url: https://web.archive.org/web/20100828075249id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 5wgt0byt
  capture_id: 173422
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
  wayback_url: https://web.archive.org/web/20100828075249id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/90&page=2
  captured_at: '2010-08-28 07:52:49+00'
  template: aspx
  sha256: e4dd40c188df4d1668419b09256c78d81d796cb6b2408ed06d207500d07c0fa6
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Figure_of_Destiny')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Figure of Destiny
  occurrences: 1
---
![](https://i.ormos.uk/86/54/865470560a72643fbed1e865131c0e0603f847cf904648dac5c4173a33e3fa6a.png)

This is the end of Level Up Week on DailyMTG.com. Today I'll talk about two parts of the design and development process that the level up creatures went through. 

Games that remain fun for repeated plays tend to give players meaningful decisions to make, and experienced **Magic** players love that **Magic** gives them lots of choices. Limited games that go long, though, often lead to both players running out of cards. When both players are playing off the top of their decks on a stalled board, that feeling of choice is greatly reduced. The important thing isn't which player plays better, it's who is luckier. Reducing a game that is often so skill-based to luck is a bit of a letdown. 

![](https://i.ormos.uk/15/c8/15c82d2c6c4883e09c178e6ee794a4fb180e48014770023e81a867b6e393c715.jpg) 

  

That feeling of a lack of control was exacerbated in *Rise of the Eldrazi* Limited by the increased length of games. For Eldrazi to matter, games needed to go long, but players also needed something fun to do while they waited for the Eldrazi to happen. Inspired by Figure of Destiny, Brian Tinsman chose level up mechanic to give players a thing to do in the intervening turns. 

Later on in development, the team had to choose whether level up would appear in the common rarity or not. My fellow developers and I could have gone either way on this. It's obvious that in the end we chose to use it at common, and one of the considerations that led us to this was that we wanted players to have enough things to do during long games. Putting level up only at uncommon would have given players fewer outlets for all the extra mana that they would have sitting around, and that sounded worse than having them easily accessible.

![](https://i.ormos.uk/54/47/54470d8fb798cb269566f793625218a0dc9545201f91512ac188689a13f6d437.png) 

  

One of the initial reactions to levelers from players was frustration that the level up ability could be played only as a sorcery. Hearing that feedback was challenging for us. **Magic** will never be a simple game, but as developers we do our best to put the complexity where complexity is fun. In our experience, trying to make strategic decisions is fun, but board states that are so tricky to understand that it's hard to get the the strategic level are less fun. Designers and developers both found that creatures with level up that leveled at instant speed often created the latter situation. The exchange of mana for size was different on different level up creatures. A pile of open mana accompanying a creature with level up could be tricky to process; a pile of open mana accompanying multiple creatures with level up could be bewildering. 

We sometimes make creatures that can be bigger than they say they are. A splash of this is fine, because **Magic** should challenge you in different ways from game to game. However, we didn't want to put players in the position of having to read, process, and act on complicated boards that could change at instant speed in game after game of *Rise of the Eldrazi* Limited. Rather than do that, we chose to have the level up ability work at sorcery speed. 

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <a href="/en/articles/latestdevelopments/2010/05-14-leveling-up-4">&#10;          <img src="http://www.wizards.com/mtg/images/daily/ld/ld90_button2.png">&#10;        </a>&#10;      </td>&#10;      <td> Leveling Up has commas, semicolons, pictures, and headings. </td>&#10;    </tr>&#10;  </tbody></table>