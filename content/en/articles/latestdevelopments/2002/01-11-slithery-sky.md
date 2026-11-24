---
id: 6k5bhzav
kind: article
lang: en
path: /en/articles/latestdevelopments/2002/01-11-slithery-sky
title: Slithery Sky
published: '2002-01-11'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    lang_detected: en
    capture_id: 734705
    url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    captured_at: '2022-01-20 01:35:14+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    lang_detected: en
    capture_id: 734705
    url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    captured_at: '2022-01-20 01:35:14+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    lang_detected: en
    capture_id: 734705
    url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    captured_at: '2022-01-20 01:35:14+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    lang_detected: en
    capture_id: 734705
    url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
    captured_at: '2022-01-20 01:35:14+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 6k5bhzav
  url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
  page_key: magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
  lang: en
  template: drupal
  captured_at: '2022-01-20 01:35:14+00'
  capture_id: 734705
  wayback_url: https://web.archive.org/web/20220120013514id_/https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
- document_id: 6k5bhzav
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb2,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb2
  lang: en
  template: classic_asp
  captured_at: '2005-02-18 02:40:21+00'
  capture_id: 1987987
  wayback_url: https://web.archive.org/web/20050218024021id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb2,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 6k5bhzav
  capture_id: 734705
  url: https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
  wayback_url: https://web.archive.org/web/20220120013514id_/https://magic.wizards.com/en/articles/archive/latest-developments/slithery-sky-2002-01-11
  captured_at: '2022-01-20 01:35:14+00'
  template: drupal
  sha256: c93e25daedd19a89c06a03b06ea8f97c92d21febecf673097db2c271567dbd2e
render_recovery: []
---
One of the cool new mechanics in *Torment* is the Nightmares. They’re a bunch of creatures, mostly black, that remove something from the game when they come into play, but give it back when they leave. We called them the "Stranglers" during playtesting and when we played them we would say "strangle you" or "strangle that guy," and so on.

My favorite Nightmare, by far, is [Faceless Butcher](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faceless+Butcher). In fact, I think it might be my favorite card in the entire set because of the cool situations it causes. My most fond memories of playing with *Torment* are games where someone would have out a Nightmare and someone else would play a Faceless Butcher, strangling the strangler and setting off a chain reaction so they could get their stuff back. The timing of when exactly to kill your opponent’s Faceless Butcher is also fun – removing that guy after they attack to get back a surprise blocker is good times.

### INFINITY 1

![](https://i.ormos.uk/55/76/557680ec61ec3b080823a8a1ae13fc464790a6805ea6256785e543c27b981479.jpg)

There are all kinds of loops and chain reactions you can set off with Faceless Butcher. In fact, you can actually cause the game to go off into an infinite loop that never ends if you have three Faceless Butchers and there are no other creatures in play... First, play a Butcher. Now play another one and strangle the first Butcher. OK, now play the third and watch what happens: It comes into play and strangles the one Butcher in play. When that one leaves play, though, it releases Butcher #1 from its icy claws and Butcher #1 looks for someone to strangle. There’s only one choice so it strangles Butcher #3, releasing #2, which strangles #1, etc., etc., etc.

Whenever that happens, the game is a draw. If there were any other creatures in play, though, the game would not be a draw because the way infinite loops usually work in **Magic** is that you pick how many times you want to make the decisions that cause the loop to happen, and then it happens that many times, and then you move on with the game. If there is another creature in play then you have a choice about what to strangle and so your Faceless Butchers can dance around in that loop however many times you like, but then you’ve got to make a different choice (otherwise you are guilty of stalling – an offense punishable by a game loss or a punch in the nose, depending on where you’re playing).

R&D spent a lot of time debating whether or not we wanted to print a card that could realistically lead to infinite loops that draw the game. Previously, it was almost impossible to have an infinite loop with no decisions involved. The easiest one I know of is to target someone with [Grindstone](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grindstone) who has nothing left in his library but two (or more) [Serra Avatar](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avatar)s. The Avatars will keep shuffling themselves back in and the Grindstone will keep grinding away forever. Anyway, we don’t want decision-free infinite loops to come up, but on the other hand we really like the chain reactions that happen when you Butcher someone else’s Butcher. Ultimately we decided that the chances of three Butchers coming into play when there aren’t any other creatures around for them to strangle were small enough that we were willing to print the card the way we did. It’s an interesting thought experiment, but it just isn’t going to happen… much.

### INFINITY 2

There was originally a card in *Torment* that made it a lot easier to draw the game:

Slithering Stalker (later changed to Slithery Stalker)  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)  
 Creature – Nightmare Horror  
 When CARDNAME comes into play, remove target green or white creature from the game. When CARDNAME leaves play, return the removed card to play under its owner’s control.  
 1/1

![](https://i.ormos.uk/f8/f0/f8f05ac82414b1c15a106241fd19db6dd2e286e43e0ca4e96df0949b3596e2b3.jpg)

**Magic** editor and combo connoisseur Mark Gottleib was all over this card. He pointed out that with [Shifting Sky](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shifting+Sky) in play (set to green or white) and no other creature in play, a single Slithering Stalker would draw the game. When it comes into play it is forced to strangle itself, which causes it to come back into play, whereupon it strangles itself, *ad infinitum*.

It’s not a difficult loophole to plug – we knew all we had to do was add “an opponent controls” to the first ability – but the real question was “Should we?” We know there are some of you out there who would find it amusing to build a deck that's sole goal was to get a draw in every game. Your opponents would probably find it annoying, but to us it didn’t seem like a sound strategy (since if there are any other creatures in play then the “combo” doesn’t work) and the interaction would only come up in Constructed (since Shifting Sky is from *Planeshift* – part of last year’s block). Plus, we kind of liked the way you could use the Stalker in Limited to rescue your own green and white creatures from an opponent’s [Kirtar's Desire](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kirtar%27s+Desire), or other disabilitating enchantments. Anyway, we made a conscious decision to allow this combo to exist.

Gottleib proceeded to build the following deck:

 **Slithery Sky**

Mark Gottleib

12 [Swamp](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) 4 Tainted Isle\* 4 [Darkwater Catacombs](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darkwater+Catacombs) 4 [Underground River](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underground+River)

 

The cards with \*’s are all in *Torment*, so you don’t know them all yet ([Compulsion](https://web.archive.org/web/20020111000000/http://archive.wizards.com/default.asp?x=sideboard/feature/sb20020107a) and [Chainer's Edict](https://web.archive.org/web/20020111000000/http://archive.wizards.com/default.asp?x=sideboard/feature/sb20020103a) have been previewed on the [Sideboard](https://web.archive.org/web/20020111000000/https://magic.wizards.com/en/articles/archive/event-coverage/3rd4th-place-playoff-rob-nadebaum-vs-daniel-clifton-2015-07-22)), but you get the idea. He could try to win with [Haunting Echoes](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Echoes) and [Traumatize](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traumatize), but if that didn’t work out he was more than happy to just draw the game. The rest of the deck is searching plus creature control. The creature removal both slows the game down and makes sure that Slithering Stalker is the only creature in play.

![](https://i.ormos.uk/71/67/71677d427ac8dcf2c04eae8aafcc4c4e72fb3befa615bd72d6afb61d5701228b.jpg)

Gottleib couldn’t believe that we were OK with leaving this combo around. He rejected all of our arguments about it being a bad strategy or not something people would take to tournaments because it was exactly the sort of thing *he* would take to a tournament. Because Gottleib works in Editing, he only had time to sign up for two matches that week, but his record was a very telling 0-0-2! All of his opponents (and the people he played “for fun”) reported significant frustration about having the game just end, in a draw, for seemingly no good reason. We relented and decided to close up that loophole.

Ever since then, whenever we’re forced to figure out whether a decision-free infinite loop is going to come up too often we ask, “Is it easier than three Faceless Butchers with no other creatures?” If the answer is yes, we change the card and if the answer is no, we leave it alone. Loops that are as easy as [Slithery Stalker](https://web.archive.org/web/20020111000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slithery+Stalker) + Shifting Sky are just going to annoy a lot more people than they entertain, so we’re not going to allow them.

*Randy may be reached at latestdevelopments@wizards.com.*