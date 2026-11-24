---
id: zgm68gs9
kind: article
lang: en
path: /en/articles/feature/2002/02-25-security-and-stability-2
title: Security and Stability
published: '2002-02-25'
column_slug: feature
column: Feature
authors:
- slug: johndoyle
  name: John Doyle
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/feature/17
    lang_detected: en
    capture_id: 2010572
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
    captured_at: '2005-03-23 00:09:59+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/feature/17
    lang_detected: en
    capture_id: 2010572
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
    captured_at: '2005-03-23 00:09:59+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/feature/17
    lang_detected: en
    capture_id: 2010572
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
    captured_at: '2005-03-23 00:09:59+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/feature/17
    lang_detected: en
    capture_id: 2010572
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
    captured_at: '2005-03-23 00:09:59+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: zgm68gs9
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
  page_key: wizards.com/default.asp?x=mtgcom/feature/17
  lang: en
  template: classic_asp
  captured_at: '2005-03-23 00:09:59+00'
  capture_id: 2010572
  wayback_url: https://web.archive.org/web/20050323000959id_/http://www.wizards.com/default.asp?x=mtgcom/feature/17
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zgm68gs9
  capture_id: 2010572
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/17
  wayback_url: https://web.archive.org/web/20050323000959id_/http://www.wizards.com/default.asp?x=mtgcom/feature/17
  captured_at: '2005-03-23 00:09:59+00'
  template: classic_asp
  sha256: ff508d65dfdfa13e98e2d37646a59e5385eaf03897fc51fb06e4d04b4d82166a
render_recovery:
- code: unsupported_link
  element: a
  target: "\n\t\t\tmailto:\n\t\t\teditor@wizards.com"
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - editor@wizards.com
  occurrences: 1
---
* * *

One of the more common comments I see on the **Magic** Online forums is, “How can Wizards keep the cards safe on their servers?” The perceived threats listed in the posts range from power outages to hackers to disastrous hardware failure. We here at Wizards and the fine folks at Leaping Lizard have been working on mechanisms to keep the data on the servers safe and secure for many months now.

![](https://i.ormos.uk/74/66/7466c2d30b8641710e671bed8e47bf6ed61244f4ec15dbabba916aa3d96ec399.jpg)

The security systems designed for the game are extensive. The program design itself makes checking the integrity of data simple, plus we have implemented a multi-layered security design intended to make the game difficult to hack and to make intrusions to the network and servers detectable.

The client (meaning the software on your computer) provides the means to display the art and communicate with the **Magic** Online servers. The client’s communication to and from **Magic** Online is encrypted. The game works on a client-server model; there is no peer-to-peer communication between you and your opponent. This will prevent players from determining their opponents' IP addresses and using that information to interfere with the progress of games.

All the cards used in the game are stored in a central database. The database is accessed by the login servers as you sign into the game, retrieving, among other things, the cards assigned to your account.

All trading of cards between players is performed on the **Magic** Online servers and the results are written to the database. The cards are assigned to the appropriate accounts and can be tracked by administrators. This will keep trades safe and secure, in an electronic sense anyway.

Cards are purchased via the E-Commerce site at [magiconlinestore.wizards.com](https://web.archive.org/web/20020225000000/http://www.wizards.com/magconlinestore.wizards.com). Boosters, tournament packs, event tickets, and theme decks are purchased and delivered to the game database to be assigned to your account. When a player logs into the game, they will find the packs they purchased and can use them to enter sealed events or open them to build decks.

The cards themselves are not "created" until the packs are opened in the game. Once a card is created, it is assigned a unique identifier and associated with the user’s account. It is this identifier which provides the means to verify cards in the system have come from a legitimate source.

This mechanism creates an audit trail by which a customer service representative can track a transaction from the purchase through the creation of cards from an individual booster or deck following all trades and concluding at redemption. It also ensures two records of each transaction are maintained, one within the E-Commerce database and one within the game.

<table><tbody><tr><td><img src="https://i.ormos.uk/04/0a/040a736fdccaf89eeb76c678556c2fc7978451d359bf7bceeccc9470369d911e.jpg"><br><i>All the necessary steps are being taken to insure your online collection will be safe.</i></td>&#10;</tr>&#10;</tbody></table>

The game system itself is quite resilient. Leaping Lizard has designed a wonderful, modular system of game and login servers to keep game play going through technical problems. Players chat, trade, and enter events on Login servers. When a game starts, the players move to a game server. A master server maintains state for all games in progress and communicates with the database as necessary. If a game server goes down, the game shifts to another server and the game is recreated at its current stage by the master. This allows the game to continue seamlessly for the players.

Of course, no matter how resilient the system design, disasters can happen. The Wizards team is working on the Disaster Recovery planning for the new system. All server and networking components for the system are at least doubly redundant. This doesn’t mean there will never be a crash, just that the recovery should be quick. The data integrity design uses a layered model, incorporating a number of technologies including tape backup. We believe we can recover data from a major crash to within a tolerance of fifteen minutes. Testing will continue to verify the methodology and improve the tolerances, if possible.

Most of the slowdowns and crashes in the beta test lately are due to the integration of the E-Commerce engine with the game. Transaction auditing, customer service and moderator tools, load testing, and optimizations will consume the technical team from now until launch. Each time the testers uncover a bug or crash the servers they move us a little closer to that goal. Thanks for the good work!

John Doyle  
 Johnd on **Magic** Online

* * *

*Comments? Email editor@wizards.com.*