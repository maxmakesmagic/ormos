---
id: 6ex2852h
kind: article
lang: en
path: /en/articles/from-the-lab/2014/07-02-captain-kurkesh
title: Captain Kurkesh
published: '2014-07-02'
column_slug: from-the-lab
column: From the Lab
authors:
- slug: mike-cannon-71256434
  name: Mike Cannon
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    lang_detected: en
    capture_id: 715871
    url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    captured_at: '2016-06-12 23:15:55+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    lang_detected: en
    capture_id: 715871
    url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    captured_at: '2016-06-12 23:15:55+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    lang_detected: en
    capture_id: 715871
    url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    captured_at: '2016-06-12 23:15:55+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    lang_detected: en
    capture_id: 715871
    url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
    captured_at: '2016-06-12 23:15:55+00'
    rule: url.article_section
sources:
- document_id: 6ex2852h
  url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
  page_key: magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
  lang: en
  template: drupal
  captured_at: '2016-06-12 23:15:55+00'
  capture_id: 715871
  wayback_url: https://web.archive.org/web/20160612231555id_/http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
- document_id: 6ex2852h
  url: http://magic.wizards.com/en/articles/archive/captain-kurkesh-2014-07-01
  page_key: magic.wizards.com/en/articles/archive/captain-kurkesh-2014-07-01
  lang: en
  template: drupal
  captured_at: '2014-09-11 23:31:32+00'
  capture_id: 240568
  wayback_url: https://web.archive.org/web/20140911233132id_/http://magic.wizards.com/en/articles/archive/captain-kurkesh-2014-07-01
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 6ex2852h
  capture_id: 715871
  url: http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
  wayback_url: https://web.archive.org/web/20160612231555id_/http://magic.wizards.com/en/articles/archive/lab/captain-kurkesh-2014-07-02
  captured_at: '2016-06-12 23:15:55+00'
  template: drupal
  sha256: fe55f645e16af3bb404c4529d22778dd4453c4054aa9b02319baf527b6153f8a
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 2
- code: unsupported_link
  element: a
  target: mailto:MTGCannon@gmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - MTGCannon@gmail.com
  occurrences: 1
---
Hello laboratorians! We're right in the [middle of *Magic 2015* previews](https://web.archive.org/web/20140702000000/http://magic.wizards.com/en/content/magic-2015-core-set-card-set-archive-products-game-info) this week, and I've got a pretty amazing one to show off. It's a new take on one of my favorite cards of all time, and it also happens to be in the best color in *Magic*.

**Say hello to Kurkesh, Onakke Ancient**.

![](http://media.wizards.com/images/magic/tcg/products/m15/sf0JdVsk2/EN_9u4co8rkxr.png)

Loopholes

My first instinct was to find a loophole in the part of Kurkesh's ability that stops you from using it on mana abilities. Most activated abilities that produce mana are mana abilities, meaning they don't use the stack and can be activated when paying costs for a spell or ability. However, if an ability that produces mana has a target, it is not a mana ability. It has to use the stack like everybody else. It would also be eligible for Kurkesh's trigger.

Unfortunately, there aren't a lot of abilities that produce mana and have a target. [Deathrite Shaman](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathrite+Shaman) is the only recent example. After digging around for a bit, I decided to go with a tried-and-true approach instead. Rather than copy a mana ability directly, I'll copy another ability that allows me to activate the mana ability again. To see what I mean, take a look at [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilded+Lotus) and [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voltaic+Key).

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gilded%20Lotus)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Voltaic%20Key)

If I activate the Key targeting [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilded+Lotus), I can use Kurkesh's trigger to copy that ability and change the target to [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voltaic+Key). When the abilities resolve, the Key will untap itself as well as the Lotus. Tap the Lotus for three red mana and do it all again, with a net gain of one mana each time. To finish the game, I'll employ a classic infinite-mana win condition. [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banefire) is a major upgrade to the old-school [Fireball](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball). It protects itself from both counterspells and damage prevention, making it almost completely certain your opponent will die, outside of shenanigans like [Seht's Tiger](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seht%27s+Tiger) that prevent your opponent from being a legal target.

[Impulse](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Impulse) and [Ponder](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) can help you dig for the combo pieces, and [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fabricate) can directly search out either [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilded+Lotus) of [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voltaic+Key). I've also added a single [Goblin Cannon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Cannon) as a [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banefire) substitute that can be searched for with [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fabricate). Meanwhile, [Counterspell](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) and [Mana Leak](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) can hold the fort long enough for you to get everything put together.

#### Ancient Key

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (4)

4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 

##### Sorcery (11)

4 [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFabricate%5D) 4 [Ponder](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 3 [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanefire%5D) 

##### Instant (12)

4 [Impulse](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImpulse%5D) 4 [Mana Leak](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Counterspell](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 

##### Artifact (9)

4 [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 4 [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoltaic%5D+%5BKey%5D) 1 [Goblin Cannon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCannon%5D) 

##### Land (24)

3 [Cascade Bluffs](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCascade%5D+%5BBluffs%5D) 4 [Steam Vents](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 8 [Island](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 5 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### Blue (20)

4 [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFabricate%5D) 4 [Impulse](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImpulse%5D) 4 [Ponder](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 4 [Mana Leak](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Counterspell](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 

##### Red (7)

4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 3 [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanefire%5D) 

##### Colorless (33)

4 [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 4 [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoltaic%5D+%5BKey%5D) 1 [Goblin Cannon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCannon%5D) 3 [Cascade Bluffs](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCascade%5D+%5BBluffs%5D) 4 [Steam Vents](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 8 [Island](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 5 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### 1 (11)

4 [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoltaic%5D+%5BKey%5D) 4 [Ponder](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 3 [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanefire%5D) 

##### 2 (12)

4 [Impulse](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImpulse%5D) 4 [Mana Leak](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Counterspell](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 

##### 3 (4)

4 [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFabricate%5D) 

##### 4 (5)

4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 1 [Goblin Cannon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCannon%5D) 

##### 5 (4)

4 [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 

36 Cards 

##### Common (25)

4 [Impulse](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImpulse%5D) 4 [Ponder](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 4 [Mana Leak](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 8 [Island](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 5 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

##### Uncommon (13)

4 [Voltaic Key](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoltaic%5D+%5BKey%5D) 4 [Fabricate](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFabricate%5D) 4 [Counterspell](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 1 [Goblin Cannon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCannon%5D) 

##### Rare (11)

4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 3 [Banefire](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanefire%5D) 4 [Shivan Reef](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 

##### Mythic (11)

4 [Gilded Lotus](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 3 [Cascade Bluffs](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCascade%5D+%5BBluffs%5D) 4 [Steam Vents](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kurkesh%2C+Onakke+Ancient)

[Deal Another Hand](https://web.archive.org/web/20140702000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fabricate)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Goblin+Cannon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Impulse)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Voltaic+Key)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kurkesh%2C+Onakke+Ancient)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shivan+Reef)

Joining Forces

I also wanted to build a deck that could take advantage of both Kurkesh and [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rings+of+Brighthearth). That meant that the combo had to involve artifacts and had to produce either one red or two colorless mana on each iteration.

One of the other cards that came to mind when thinking of artifacts with powerful abilities was [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mimic+Vat). Of course the Vat doesn't do anything on its own, but the power level of its ability can scale up tremendously depending on what creature has been exiled.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rings%20of%20Brighthearth)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mimic%20Vat)

In this case, [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Composite+Golem) was the one I selected. Although a bit expensive to cast, if gives you all but one of that mana back immediately, and the ability to sacrifice itself makes it much easier to get the Golem imprinted on [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mimic+Vat). Once that's taken care of, you can activate the Vat, pay an additional one or two mana, and get two [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Composite+Golem) tokens. Sacrificing those will give you back ten mana, at least twice as much as you paid to begin with.

There's still the issue of untapping [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mimic+Vat), however. Without a way to do that, you could only make that five or six extra mana once. Fortunately, a previous core set brought back a card that's perfect for the job. [Clock of Omens](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clock+of+Omens) allows you to tap the two [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Composite+Golem) tokens you make to untap [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mimic+Vat), resetting everything for another go around.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Composite%20Golem)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clock%20of%20Omens)

This deck also makes infinite mana and therefore could use the same win conditions as the previous one. However, I wanted to show off some other options as well. [Sands of Delirium](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sands+of+Delirium) is an excellent choice, particularly if your opponent has a way to survive being dealt an arbitrarily large amount of damage. I also added in [Moonlit Wake](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonlit+Wake). Although it doesn't win outright, it does make it almost impossible for your opponent to do so unless he or she is playing an infinite combo as well.

Since [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Composite+Golem) can be prohibitively expensive, I've included [Worn Powerstone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worn+Powerstone) to help you get there a bit sooner. [Day of Judgment](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) can also be used to buy time, especially against aggressive creature-based decks. Finally, [Enlightened Tutor](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enlightened+Tutor) can search for any piece of the combo save Kurkesh. Fortunately, [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rings+of+Brighthearth) works just as well.

#### Golem Vat

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (8)

4 [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BComposite%5D+%5BGolem%5D) 4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 

##### Sorcery (4)

4 [Day of Judgment](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### Instant (4)

4 [Enlightened Tutor](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnlightened%5D+%5BTutor%5D) 

##### Artifact (19)

4 [Worn Powerstone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWorn%5D+%5BPowerstone%5D) 4 [Clock of Omens](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClock%5D+%5Bof%5D+%5BOmens%5D) 4 [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMimic%5D+%5BVat%5D) 3 [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRings%5D+%5Bof%5D+%5BBrighthearth%5D) 4 [Sands of Delirium](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSands%5D+%5Bof%5D+%5BDelirium%5D) 

##### Enchantment (1)

1 [Moonlit Wake](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonlit%5D+%5BWake%5D) 

##### Land (24)

4 [Battlefield Forge](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 3 [Rugged Prairie](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRugged%5D+%5BPrairie%5D) 4 [Sacred Foundry](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 7 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 6 [Plains](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### White (9)

1 [Moonlit Wake](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonlit%5D+%5BWake%5D) 4 [Enlightened Tutor](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnlightened%5D+%5BTutor%5D) 4 [Day of Judgment](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### Red (4)

4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 

##### Colorless (47)

4 [Worn Powerstone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWorn%5D+%5BPowerstone%5D) 4 [Clock of Omens](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClock%5D+%5Bof%5D+%5BOmens%5D) 4 [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMimic%5D+%5BVat%5D) 3 [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRings%5D+%5Bof%5D+%5BBrighthearth%5D) 4 [Sands of Delirium](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSands%5D+%5Bof%5D+%5BDelirium%5D) 4 [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BComposite%5D+%5BGolem%5D) 4 [Battlefield Forge](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 3 [Rugged Prairie](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRugged%5D+%5BPrairie%5D) 4 [Sacred Foundry](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 7 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 6 [Plains](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### 1 (4)

4 [Enlightened Tutor](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnlightened%5D+%5BTutor%5D) 

##### 3 (16)

4 [Worn Powerstone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWorn%5D+%5BPowerstone%5D) 4 [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMimic%5D+%5BVat%5D) 3 [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRings%5D+%5Bof%5D+%5BBrighthearth%5D) 4 [Sands of Delirium](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSands%5D+%5Bof%5D+%5BDelirium%5D) 1 [Moonlit Wake](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonlit%5D+%5BWake%5D) 

##### 4 (12)

4 [Clock of Omens](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClock%5D+%5Bof%5D+%5BOmens%5D) 4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 4 [Day of Judgment](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### 6 (4)

4 [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BComposite%5D+%5BGolem%5D) 

36 Cards 

##### Common (13)

7 [Mountain](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 6 [Plains](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

##### Uncommon (17)

4 [Worn Powerstone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWorn%5D+%5BPowerstone%5D) 4 [Clock of Omens](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClock%5D+%5Bof%5D+%5BOmens%5D) 4 [Composite Golem](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BComposite%5D+%5BGolem%5D) 1 [Moonlit Wake](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonlit%5D+%5BWake%5D) 4 [Enlightened Tutor](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnlightened%5D+%5BTutor%5D) 

##### Rare (23)

4 [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMimic%5D+%5BVat%5D) 3 [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRings%5D+%5Bof%5D+%5BBrighthearth%5D) 4 [Sands of Delirium](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSands%5D+%5Bof%5D+%5BDelirium%5D) 4 [Kurkesh, Onakke Ancient](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKurkesh,%5D+%5BOnakke%5D+%5BAncient%5D) 4 [Day of Judgment](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 4 [Battlefield Forge](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 

##### Mythic (7)

3 [Rugged Prairie](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRugged%5D+%5BPrairie%5D) 4 [Sacred Foundry](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Worn+Powerstone)

[Deal Another Hand](https://web.archive.org/web/20140702000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Day+of+Judgment)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sacred+Foundry)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sands+of+Delirium)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clock+of+Omens)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

Further Exploration

Of course, these two ideas are far from the only things you can do with a card as open-ended as Kurkesh, Onakke Ancient. In fact, there are literally hundreds of artifacts that are willing to work with the Ogre. I'll quickly run through a few of my favorites to perhaps lubricate a few of those mental gears and help you come up with your own decks.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Isochron%20Scepter)

[Isochron Scepter](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Isochron+Scepter) is just as open-ended has Kurkesh is, giving you hundreds of options to work with. With all those cheap instants to choose from, I'm sure there are more than a few that can lead to some fantastic shenanigans.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Prototype%20Portal)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul%20Foundry)

[Prototype Portal](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prototype+Portal) and [Soul Foundry](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry) can be used to make token copies of a permanent, similar to [Mimic Vat](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mimic+Vat). However, these copies stick around permanently. If the artifact you make with the *Portal* also has an activated ability, Kurkesh can copy that as well.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Legacy%20Weapon)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sword%20of%20the%20Ages)

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Keening%20Stone)

Believe it or not, there are even some cards without imprint that can work with Kurkesh. [Legacy Weapon](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Legacy+Weapon) can exile two permanents at once for just one extra red mana, and Sword of Ages can deal twice as much damage as it normally would. [Keening Stone](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keening+Stone) can get rid of your opponent's library extremely quickly by copying the ability. You'll mill three times as many cards as you would with just one activation.

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mycosynth%20Lattice)

You can also do some other tricks to increase your options even further. Using a card like [Mycosynth Lattice](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mycosynth+Lattice) opens up Kurkesh to all the possibilities [Rings of Brighthearth](https://web.archive.org/web/20140702000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rings+of+Brighthearth) has access to, while still retaining the one-mana trigger cost. Even Planeswalker abilities can be copied. Although it won't add more loyalty counters, since that's the cost to activate the ability rather than its effect, it won't remove any more either, and you'll still get an extra copy of the ability.

Kurkesh You Later

Well, I'll leave the rest of Kurkesh's potential for you to explore for now. Feel free to send me any deck ideas you come up with at MTGCannon@gmail.com. In fact, I'd love to see the decks you can come up with for any M15 card. The full set [will be revealed soon](https://web.archive.org/web/20140702000000/http://magic.wizards.com/en/content/magic-2015-core-set-card-set-archive-products-game-info), and this is the best time to start brewing up new deck ideas. Get those Johnny minds humming, because I might very well be featuring some of your decks in the next few weeks. See ya!