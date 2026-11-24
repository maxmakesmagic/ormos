---
id: 2sj12x9p
kind: article
lang: en
path: /en/articles/feature/2002/02-25-security-and-stability
title: Security and Stability
published: '2002-02-25'
column_slug: feature
column: Feature
authors:
- slug: john-doyle-online-technical-lead-cae2746f
  name: John Doyle, Online technical lead
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    lang_detected: en
    capture_id: 666818
    url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    captured_at: '2021-12-03 04:59:12+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    lang_detected: en
    capture_id: 666818
    url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    captured_at: '2021-12-03 04:59:12+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    lang_detected: en
    capture_id: 666818
    url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    captured_at: '2021-12-03 04:59:12+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    lang_detected: en
    capture_id: 666818
    url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
    captured_at: '2021-12-03 04:59:12+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: 2sj12x9p
  url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
  page_key: magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
  lang: en
  template: drupal
  captured_at: '2021-12-03 04:59:12+00'
  capture_id: 666818
  wayback_url: https://web.archive.org/web/20211203045912id_/https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2sj12x9p
  capture_id: 666818
  url: https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
  wayback_url: https://web.archive.org/web/20211203045912id_/https://magic.wizards.com/en/articles/archive/feature/security-and-stability-2002-02-25
  captured_at: '2021-12-03 04:59:12+00'
  template: drupal
  sha256: d28f417d41d07f56f2938d30cd198b80a4a382de1c5a620fec66e260be8895ab
render_recovery: []
---
One of the more common comments I see on the **Magic** Online forums is, “How can Wizards keep the cards safe on their servers?” The perceived threats listed in the posts range from power outages to hackers to disastrous hardware failure. We here at Wizards and the fine folks at Leaping Lizard have been working on mechanisms to keep the data on the servers safe and secure for many months now.

The security systems designed for the game are extensive. The program design itself makes checking the integrity of data simple, plus we have implemented a multi-layered security design intended to make the game difficult to hack and to make intrusions to the network and servers detectable.

The client (meaning the software on your computer) provides the means to display the art and communicate with the **Magic** Online servers. The client’s communication to and from **Magic** Online is encrypted. The game works on a client-server model; there is no peer-to-peer communication between you and your opponent. This will prevent players from determining their opponents' IP addresses and using that information to interfere with the progress of games.

All the cards used in the game are stored in a central database. The database is accessed by the login servers as you sign into the game, retrieving, among other things, the cards assigned to your account.

All trading of cards between players is performed on the **Magic** Online servers and the results are written to the database. The cards are assigned to the appropriate accounts and can be tracked by administrators. This will keep trades safe and secure, in an electronic sense anyway.

Cards are purchased via the E-Commerce site at [magiconlinestore.wizards.com](https://web.archive.org/web/20020225000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magconlinestore.wizards.com). Boosters, tournament packs, event tickets, and theme decks are purchased and delivered to the game database to be assigned to your account. When a player logs into the game, they will find the packs they purchased and can use them to enter sealed events or open them to build decks.

The cards themselves are not "created" until the packs are opened in the game. Once a card is created, it is assigned a unique identifier and associated with the user’s account. It is this identifier which provides the means to verify cards in the system have come from a legitimate source.

This mechanism creates an audit trail by which a customer service representative can track a transaction from the purchase through the creation of cards from an individual booster or deck following all trades and concluding at redemption. It also ensures two records of each transaction are maintained, one within the E-Commerce database and one within the game.

<table><tbody><tr><td><br><i>All the necessary steps are being taken to insure your online collection will be safe.</i></td></tr></tbody></table>

The game system itself is quite resilient. Leaping Lizard has designed a wonderful, modular system of game and login servers to keep game play going through technical problems. Players chat, trade, and enter events on Login servers. When a game starts, the players move to a game server. A master server maintains state for all games in progress and communicates with the database as necessary. If a game server goes down, the game shifts to another server and the game is recreated at its current stage by the master. This allows the game to continue seamlessly for the players.

Of course, no matter how resilient the system design, disasters can happen. The Wizards team is working on the Disaster Recovery planning for the new system. All server and networking components for the system are at least doubly redundant. This doesn’t mean there will never be a crash, just that the recovery should be quick. The data integrity design uses a layered model, incorporating a number of technologies including tape backup. We believe we can recover data from a major crash to within a tolerance of fifteen minutes. Testing will continue to verify the methodology and improve the tolerances, if possible.

Most of the slowdowns and crashes in the beta test lately are due to the integration of the E-Commerce engine with the game. Transaction auditing, customer service and moderator tools, load testing, and optimizations will consume the technical team from now until launch. Each time the testers uncover a bug or crash the servers they move us a little closer to that goal. Thanks for the good work!

John Doyle  
 Johnd on **Magic** Online

*Comments? Email editor@wizards.com.*