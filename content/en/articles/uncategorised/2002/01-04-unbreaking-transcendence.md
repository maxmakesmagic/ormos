---
id: jnng8p6p
kind: article
lang: en
path: /en/articles/uncategorised/2002/01-04-unbreaking-transcendence
title: Unbreaking Transcendence
published: '2002-01-04'
column_slug: uncategorised
column: uncategorised
authors: []
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 1214079
    url: http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    captured_at: '2017-08-16 17:44:46+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 1214079
    url: http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    captured_at: '2017-08-16 17:44:46+00'
    rule: drupal.posted_in_date
  column:
    page_key: magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 1214079
    url: http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
    captured_at: '2017-08-16 17:44:46+00'
    rule: drupal.posted_in_link
sources:
- document_id: jnng8p6p
  url: http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
  page_key: magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
  lang: en
  template: drupal
  captured_at: '2017-08-16 17:44:46+00'
  capture_id: 1214079
  wayback_url: https://web.archive.org/web/20170816174446id_/http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jnng8p6p
  capture_id: 1214079
  url: http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
  wayback_url: https://web.archive.org/web/20170816174446id_/http://magic.wizards.com/en/articles/archive/unbreaking-transcendence-2002-01-04
  captured_at: '2017-08-16 17:44:46+00'
  template: drupal
  sha256: 3f20d96e3db384344871ed69074f6f4244ebc7d358ae262e51b5cb19f24e70e0
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:alert(%22not%20implemented%20yet%20(mail)%22);
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - latestdevelopments@wizards.com
  occurrences: 1
---
I’ll start off this week with a quick bio, but don’t worry. I promise that there’s a *Torment* card preview in here somewhere — and a window into R&D’s bizarre world.

My name is Randy Buehler. My job title is lead developer for *Magic: The Gathering*. Mark Rosewater will probably describe the difference between design and development in more detail in his own column, and I can’t emphasize enough how fundamental that distinction is to everything R&D does. The design team isn’t supposed to worry about how good a card is or whether it’ll lead to some degenerate combo deck; they’re just supposed to think up cool cards. Then it’s development’s responsibility to test them all, figure out what they should cost, make sure they aren’t broken, and so on. As the lead *Magic* developer, my job is to organize the whole development process. Ultimately, I’m responsible for making sure that nothing goes wrong.

I started playing *Magic* as a graduate student in Minnesota, right before *Homelands* came out. That means I cut my teeth on *Ice Age*, *Fourth Edition*, and *Fallen Empires*. After six months of playing with my roommate and some friends, I discovered tournaments. I was immediately hooked on the adrenaline of competition. Soon I was playing Pro Tour Qualifiers, making the Top 8 of the first one I entered with a [Necropotence](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) deck I downloaded from Usenet. After moving to Pittsburgh, I hooked up with the guys from Carnegie Mellon University who also played a lot of *Magic* and I went to *a lot* of tournaments.

I won the first Pro Tour I qualified for (Chicago 1997), and that’s when my life really changed. I was working on a Ph.D. in History and Philosophy of Quantum Mechanics, but I was making enough money playing *Magic* to pay the bills so I put grad school on hold. Traveling all over the world to play games was a lot more fun. Before my two-year leave of absence was up, I was offered this amazing job at Wizards of the Coast. I decided to change sides and start breaking cards *before* they came out.

I got to Wizards very early in *Invasion* development, and I’ve been on the development team for every *Magic* set since then. *Odyssey* was my first set as lead developer, then last summer I was promoted to lead developer for all of *Magic*. In this weekly column, I’ll give you a peek inside R&D. The people I work with are incredibly talented, and they’ve worked out a lot of interesting theories about what makes *Magic* fun.

![](http://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/rb00101pr.jpg)

### PHASE 1: POLARITY REVERSER

The *Torment* (then called "Vendetta") design file came in with a seemingly innocuous card hiding among the white rares:

\[Polarity Reverser\]  
 3W  
 Enchantment  
 If damage would be dealt to you, instead you gain that much life.  
 If your life total is 20 or more, you lose the game.

At first glance, it looks like a cool rare. Everyone likes cards that change the rules of the game, and losing the game at 20 life instead of 0 is pretty neat. If you play it when you’re at 1 life, it effectively says “you gain 38 life,” but in a new way. In addition, a timely [Disenchant](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant) can save you before you hit 20, and later you can play another copy to start your life total swinging back the other way.

Henry Stern “broke” that version of the card in the very first sealed deck playtest we had: He simply used mana burn to keep his life total below 20. Since mana burn is loss of life, not damage, he could keep his life total between 20 and 0 forever. Imagine 3W, Enchantment, “Your opponents can’t win the game with damage.”

Oops.

### PHASE 2: RAPTURE

At the first opportunity, the card gained an additional ability (and a first attempt at a real name):

Rapture  
 3W  
 Enchantment  
 If damage would be dealt to you, instead you gain that much life.  
 Whenever you lose life, you gain twice that much life.  
 You lose the game if your life total is 20 or more.

#### Rapture/Lich

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Sorcery (16)

4 [Duress](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 4 [Vindicate](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVindicate%5D) 4 [Addle](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAddle%5D) 4 [Gerrard's Verdict](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGerrard%5D+%5BVerdict%5D) 

##### Enchantment (8)

4 [Nefarious Lich](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNefarious%5D+%5BLich%5D) 4 [Phyrexian Arena](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BArena%5D) 

##### Land (16)

12 [Swamp](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Caves of Koilos](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 

##### Other (20)

4 Tainted Plains\* 4 City of Brass              4 Pestilence Rite\* 4 Rapture 4 Dark Tutor Blood\* 

60 Cards 

##### Black (16)

4 [Duress](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 4 [Nefarious Lich](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNefarious%5D+%5BLich%5D) 4 [Phyrexian Arena](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BArena%5D) 4 [Addle](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAddle%5D) 

##### Multi colored (8)

4 [Vindicate](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVindicate%5D) 4 [Gerrard's Verdict](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGerrard%5D+%5BVerdict%5D) 

##### Colorless (36)

12 [Swamp](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 Tainted Plains\* 4 [Caves of Koilos](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 City of Brass              4 Pestilence Rite\* 4 Rapture 4 Dark Tutor Blood\* 

60 Cards 

##### 1 (4)

4 [Duress](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 

##### 2 (8)

4 [Addle](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAddle%5D) 4 [Gerrard's Verdict](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGerrard%5D+%5BVerdict%5D) 

##### 3 (8)

4 [Vindicate](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVindicate%5D) 4 [Phyrexian Arena](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BArena%5D) 

##### 4 (4)

4 [Nefarious Lich](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNefarious%5D+%5BLich%5D) 

24 Cards 

##### Common (40)

12 [Swamp](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 Tainted Plains\* 4 City of Brass              4 Pestilence Rite\* 4 [Duress](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 4 Rapture 4 Dark Tutor Blood\* 4 [Addle](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAddle%5D) 

##### Uncommon (4)

4 [Gerrard's Verdict](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGerrard%5D+%5BVerdict%5D) 

##### Rare (16)

4 [Caves of Koilos](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Vindicate](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVindicate%5D) 4 [Nefarious Lich](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNefarious%5D+%5BLich%5D) 4 [Phyrexian Arena](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BArena%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

[Deal Another Hand](https://web.archive.org/web/20020104000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Duress)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vindicate)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vindicate)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vindicate)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Phyrexian+Arena)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

a:13:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"12";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Caves of Koilos";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:4;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:5;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Duress";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Vindicate";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Nefarious Lich";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:9;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:10;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Phyrexian Arena";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Addle";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Gerrard's Verdict";s:22:"field\_card\_image\_front";a:0:{}}}} 

Not exactly elegant, but it did capture the intended functionality. Enter Mark Gottlieb and Bill “Quill” McQuillan. Quill’s the lead *Magic* editor, but he was moonlighting as a developer for *Torment* to get a look at what exactly R&D does with the card file before Editing gets their hands on it. Mark Gottlieb was the *Torment* set editor. He’s also a contributing editor for *Games* magazine and an aficionado of crazy combos. (I’ll be talking about another one of his creations next week.) Boy, did he have fun with Rapture. In a nutshell, crazy things happen when you put that version of the card and Nefarious Lich on the table.

To the right is the deck that Quill used to exploit Gottleib’s combo. The \*’s mark *Torment* cards that I’m not allowed to tell you about. However, the powers-that-be are letting me tell you the cards’ real names: Pestilence Rite was the playtest name for a card now called Sickening Dreams. Dark Tutor Blood got some mana added to its cost (in part because of this deck) and was eventually renamed Insidious Dreams. Tainted Plains wound up as Tainted Field.

Picture the board after Rapture and [Nefarious Lich](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nefarious+Lich) hit the table. Whenever you would take damage, you have your choice of two things to replace it with. You can remove cards from your graveyard with the Lich or you can gain life with Rapture. Of course, you choose to gain the life because the Lich will replace *that* with drawing cards. So you never take damage again, but you draw lots and lots of cards.

![](http://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/rb00102lich.jpg)

Actually, the combo gets even crazier than that. When you tap a pain land, you draw a card instead of taking the damage. If you take mana burn, you draw two cards per point of mana burn. [Phyrexian Arena](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Arena) is insanely powerful. You would lose 1 life, but instead you’d gain 2 life, but instead you draw two cards. You wind up drawing four cards every turn instead of two! Even without knowing what those other two *Torment* cards do, I’m sure you can imagine how easy it is to win from that position.

The team took one look at this deck in action and knew we had to change something. Well, really we took two looks, confirmed the timing rules with our rules experts, tried it out ourselves because it was so crazy to experience, and *then* knew we had to change something. We first added a second white mana to Rapture’s cost. Then a third white mana. The card had been undercosted at four mana anyway, and by adding colored mana, we were trying to make it impossible to play in the same deck as Nefarious Lich.

![](http://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/rb00103transcendence.jpg)

### PHASE 3: TRANSCENDENCE

Finally, the templating team solved our problem for us. (The templating team is where Editing and the *Magic* rules manager figure out how to word the cards so they work the way R&D wants them to.) Instead of setting up the card as a replacement ability (you gain life *instead* of taking damage), they templated it as a triggered ability (whenever you lose life, you *then* gain life). So the card finally wound up as [Transcendence](https://web.archive.org/web/20020104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transcendence), as it appears in *Torment*.

This card has the same effect as the original design in most circumstances, but it doesn’t interact quite as well with Nefarious Lich. Now if you have both enchantments on the table, the Lich replaces damage that would be deal to you with removing cards from the graveyard. You don’t actually take damage, so you never gain life with Transcendence. Interestingly, the combo does still work with loss of life, including mana burn, because the Lich doesn’t replace life loss. It is left as an exercise to the reader to see if you can still break these cards.

So there you go — your first look into the (sometimes crazy) goings on inside *Magic* development. The designers thought up a cool card and the development team had to both figure out how much to charge for it and make sure it wasn’t overpowered. As usual, we needed to raise the price because the effect is pretty powerful. And in this case, the card actually was broken, but the wording change we used to make the card easier to understand (changing the life gain to a triggered ability) also reduced its combo potential.

* * *

*Randy may be reached at latestdevelopments@wizards.com.*

*"I got a flurry of emails about my article and a couple of them pointed out a misunderstanding I made. When we changed Transcendence to a triggered ability, I should have said that it no longer interacts with Nefarious Lich *quite as well*. Damage will no longer cause you to draw cards while both enchantments are on the table. However loss of life (including from mana burn) *will*. That’s because the replacement effect of the Lich only replaces damage… not loss of life. When you lose life it will still trigger the Transcendence, causing you to gain life, draw cards, etc. Since I knew the Pestilence Rite that fueled our combo deck didn’t work anymore, I mistakenly assumed the whole combo was broken. It isn’t, and we’ve now edited the article appropriately." -- Randy*