---
id: jz3b22f2
kind: article
lang: en
path: /en/articles/latestdevelopments/2002/01-04-unbreaking-transcendence
title: Unbreaking Transcendence
published: '2002-01-04'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 735630
    url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    captured_at: '2022-01-29 00:57:01+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 735630
    url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    captured_at: '2022-01-29 00:57:01+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 735630
    url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    captured_at: '2022-01-29 00:57:01+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    lang_detected: en
    capture_id: 735630
    url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
    captured_at: '2022-01-29 00:57:01+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: jz3b22f2
  url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
  lang: en
  template: drupal
  captured_at: '2022-01-29 00:57:01+00'
  capture_id: 735630
  wayback_url: https://web.archive.org/web/20220129005701id_/https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
- document_id: jz3b22f2
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb1
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb1
  lang: en
  template: aspx
  captured_at: '2012-10-15 07:24:14+00'
  capture_id: 804975
  wayback_url: https://web.archive.org/web/20121015072414id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb1
- document_id: jz3b22f2
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb1,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb1
  lang: en
  template: classic_asp
  captured_at: '2005-01-22 03:26:13+00'
  capture_id: 1986378
  wayback_url: https://web.archive.org/web/20050122032613id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb1,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jz3b22f2
  capture_id: 735630
  url: https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
  wayback_url: https://web.archive.org/web/20220129005701id_/https://magic.wizards.com/en/articles/archive/latest-developments/unbreaking-transcendence-2002-01-04
  captured_at: '2022-01-29 00:57:01+00'
  template: drupal
  sha256: c4ccffff7cfc3bcaf0c680a70ab119f07f905b04ba89a10e8adc88d230493f27
render_recovery: []
---
I’ll start off this week with a quick bio, but don’t worry. I promise that there’s a *Torment* card preview in here somewhere — and a window into R&D’s bizarre world.

My name is Randy Buehler. My job title is lead developer for **Magic: The Gathering**. Mark Rosewater will probably describe the difference between design and development in more detail in his own column, and I can’t emphasize enough how fundamental that distinction is to everything R&D does. The design team isn’t supposed to worry about how good a card is or whether it’ll lead to some degenerate combo deck; they’re just supposed to think up cool cards. Then it’s development’s responsibility to test them all, figure out what they should cost, make sure they aren’t broken, and so on. As the lead **Magic** developer, my job is to organize the whole development process. Ultimately, I’m responsible for making sure that nothing goes wrong.

I started playing **Magic** as a graduate student in Minnesota, right before *Homelands* came out. That means I cut my teeth on *Ice Age*, *Fourth Edition*, and *Fallen Empires*. After six months of playing with my roommate and some friends, I discovered tournaments. I was immediately hooked on the adrenaline of competition. Soon I was playing Pro Tour Qualifiers, making the Top 8 of the first one I entered with a [Necropotence](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) deck I downloaded from Usenet. After moving to Pittsburgh, I hooked up with the guys from Carnegie Mellon University who also played a lot of **Magic** and I went to *a lot* of tournaments.

I won the first Pro Tour I qualified for (Chicago 1997), and that’s when my life really changed. I was working on a Ph.D. in History and Philosophy of Quantum Mechanics, but I was making enough money playing **Magic** to pay the bills so I put grad school on hold. Traveling all over the world to play games was a lot more fun. Before my two-year leave of absence was up, I was offered this amazing job at Wizards of the Coast. I decided to change sides and start breaking cards *before* they came out.

I got to Wizards very early in *Invasion* development, and I’ve been on the development team for every **Magic** set since then. *Odyssey* was my first set as lead developer, then last summer I was promoted to lead developer for all of **Magic**. In this weekly column, I’ll give you a peek inside R&D. The people I work with are incredibly talented, and they’ve worked out a lot of interesting theories about what makes **Magic** fun.

![](https://i.ormos.uk/cf/77/cf77e7f700fdcbf8956d5263592a7abf65586e230407fc5ff69076772b2b21a1.jpg)

### PHASE 1: POLARITY REVERSER

The *Torment* (then called "Vendetta") design file came in with a seemingly innocuous card hiding among the white rares:

\[Polarity Reverser\]  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)  
 Enchantment  
 If damage would be dealt to you, instead you gain that much life.  
 If your life total is 20 or more, you lose the game.

At first glance, it looks like a cool rare. Everyone likes cards that change the rules of the game, and losing the game at 20 life instead of 0 is pretty neat. If you play it when you’re at 1 life, it effectively says “you gain 38 life,” but in a new way. In addition, a timely [Disenchant](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant) can save you before you hit 20, and later you can play another copy to start your life total swinging back the other way.

Henry Stern “broke” that version of the card in the very first sealed deck playtest we had: He simply used mana burn to keep his life total below 20. Since mana burn is loss of life, not damage, he could keep his life total between 20 and 0 forever. Imagine ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), Enchantment, “Your opponents can’t win the game with damage.”

Oops.

### PHASE 2: RAPTURE

At the first opportunity, the card gained an additional ability (and a first attempt at a real name):

Rapture  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)  
 Enchantment  
 If damage would be dealt to you, instead you gain that much life.  
 Whenever you lose life, you gain twice that much life.  
 You lose the game if your life total is 20 or more.

### Rapture/Lich

12 [Swamp](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)  
 4 Tainted Plains\*  
 4 [Caves of Koilos](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caves+of+Koilos)  
 4 [City of Brass](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=City+of+Brass)

4 Pestilence Rite\*  
 4 [Duress](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duress)  
 4 [Vindicate](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vindicate)  
 4 [Nefarious Lich](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nefarious+Lich)  
 4 Rapture  
 4 Dark Tutor Blood\*  
 4 [Phyrexian Arena](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Arena)  
 4 [Addle](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Addle)  
 4 [Gerrard's Verdict](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard%27s+Verdict)

Not exactly elegant, but it did capture the intended functionality. Enter Mark Gottlieb and Bill “Quill” McQuillan. Quill’s the lead **Magic** editor, but he was moonlighting as a developer for *Torment* to get a look at what exactly R&D does with the card file before Editing gets their hands on it. Mark Gottlieb was the *Torment* set editor. He’s also a contributing editor for *Games* magazine and an aficionado of crazy combos. (I’ll be talking about another one of his creations next week.) Boy, did he have fun with Rapture. In a nutshell, crazy things happen when you put that version of the card and Nefarious Lich on the table.

To the right is the deck that Quill used to exploit Gottleib’s combo. The \*’s mark *Torment* cards that I’m not allowed to tell you about. However, the powers-that-be are letting me tell you the cards’ real names: Pestilence Rite was the playtest name for a card now called Sickening Dreams. Dark Tutor Blood got some mana added to its cost (in part because of this deck) and was eventually renamed Insidious Dreams. Tainted Plains wound up as Tainted Field.

Picture the board after Rapture and [Nefarious Lich](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nefarious+Lich) hit the table. Whenever you would take damage, you have your choice of two things to replace it with. You can remove cards from your graveyard with the Lich or you can gain life with Rapture. Of course, you choose to gain the life because the Lich will replace *that* with drawing cards. So you never take damage again, but you draw lots and lots of cards.

![](https://i.ormos.uk/39/ed/39ed146cb75430c2cbf9422fb68585e70bee8d537047eff19dc069619071ef43.jpg)

Actually, the combo gets even crazier than that. When you tap a pain land, you draw a card instead of taking the damage. If you take mana burn, you draw two cards per point of mana burn. [Phyrexian Arena](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Arena) is insanely powerful. You would lose 1 life, but instead you’d gain 2 life, but instead you draw two cards. You wind up drawing four cards every turn instead of two! Even without knowing what those other two *Torment* cards do, I’m sure you can imagine how easy it is to win from that position.

The team took one look at this deck in action and knew we had to change something. Well, really we took two looks, confirmed the timing rules with our rules experts, tried it out ourselves because it was so crazy to experience, and *then* knew we had to change something. We first added a second white mana to Rapture’s cost. Then a third white mana. The card had been undercosted at four mana anyway, and by adding colored mana, we were trying to make it impossible to play in the same deck as Nefarious Lich.

![](https://i.ormos.uk/a3/a4/a3a4ed88040be3b1dd343234f195b445c744cc680e2e5f5884d5f660af8763a0.jpg)

### PHASE 3: TRANSCENDENCE

Finally, the templating team solved our problem for us. (The templating team is where Editing and the **Magic** rules manager figure out how to word the cards so they work the way R&D wants them to.) Instead of setting up the card as a replacement ability (you gain life *instead* of taking damage), they templated it as a triggered ability (whenever you lose life, you *then* gain life). So the card finally wound up as [Transcendence](https://web.archive.org/web/20020104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transcendence), as it appears in *Torment*.

This card has the same effect as the original design in most circumstances, but it doesn’t interact quite as well with Nefarious Lich. Now if you have both enchantments on the table, the Lich replaces damage that would be deal to you with removing cards from the graveyard. You don’t actually take damage, so you never gain life with Transcendence. Interestingly, the combo does still work with loss of life, including mana burn, because the Lich doesn’t replace life loss. It is left as an exercise to the reader to see if you can still break these cards.

So there you go — your first look into the (sometimes crazy) goings on inside **Magic** development. The designers thought up a cool card and the development team had to both figure out how much to charge for it and make sure it wasn’t overpowered. As usual, we needed to raise the price because the effect is pretty powerful. And in this case, the card actually was broken, but the wording change we used to make the card easier to understand (changing the life gain to a triggered ability) also reduced its combo potential.

*Randy may be reached at latestdevelopments@wizards.com.*

*"I got a flurry of emails about my article and a couple of them pointed out a misunderstanding I made. When we changed Transcendence to a triggered ability, I should have said that it no longer interacts with Nefarious Lich *quite as well*. Damage will no longer cause you to draw cards while both enchantments are on the table. However loss of life (including from mana burn) *will*. That’s because the replacement effect of the Lich only replaces damage… not loss of life. When you lose life it will still trigger the Transcendence, causing you to gain life, draw cards, etc. Since I knew the Pestilence Rite that fueled our combo deck didn’t work anymore, I mistakenly assumed the whole combo was broken. It isn’t, and we’ve now edited the article appropriately." -- Randy*