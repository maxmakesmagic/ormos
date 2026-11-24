---
id: c8x7pstr
kind: article
lang: en
path: /en/articles/latestdevelopments/2008/07-18-duster-in-the-wind
title: Duster in the Wind
published: '2008-07-18'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: devinlow
  name: Devin Low
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    lang_detected: en
    capture_id: 721257
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    captured_at: '2022-01-25 16:05:32+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    lang_detected: en
    capture_id: 721257
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    captured_at: '2022-01-25 16:05:32+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    lang_detected: en
    capture_id: 721257
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    captured_at: '2022-01-25 16:05:32+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    lang_detected: en
    capture_id: 721257
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
    captured_at: '2022-01-25 16:05:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: c8x7pstr
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
  lang: en
  template: drupal
  captured_at: '2022-01-25 16:05:32+00'
  capture_id: 721257
  wayback_url: https://web.archive.org/web/20220125160532id_/https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
- document_id: c8x7pstr
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl46&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/dl46
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:35:50+00'
  capture_id: 254859
  wayback_url: https://web.archive.org/web/20090604153550id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl46&print=true
- document_id: c8x7pstr
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18
  page_key: magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18
  lang: en
  template: drupal
  captured_at: '2021-10-24 13:50:03+00'
  capture_id: 721256
  wayback_url: https://web.archive.org/web/20211024135003id_/https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18
- document_id: c8x7pstr
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl46&=RSS-MTGCOM
  page_key: wizards.com/default.asp?=RSS-MTGCOM&x=mtgcom/daily/dl46
  lang: en
  template: classic_asp
  captured_at: '2008-08-01 17:44:15+00'
  capture_id: 1261414
  wayback_url: https://web.archive.org/web/20080801174415id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dl46&=RSS-MTGCOM
- document_id: c8x7pstr
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl46,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/dl46
  lang: en
  template: classic_asp
  captured_at: '2008-08-24 05:53:27+00'
  capture_id: 1949720
  wayback_url: https://web.archive.org/web/20080824055327id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dl46,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: c8x7pstr
  capture_id: 721257
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
  wayback_url: https://web.archive.org/web/20220125160532id_/https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0
  captured_at: '2022-01-25 16:05:32+00'
  template: drupal
  sha256: 57e6832ade5063094420054a3d2cd6df7812a70b3cde3b5a3a5f856b06d22d64
render_recovery: []
---
## One little Kithkin who does its job and then some.

Some cards are the ones that get all the buzz. The ones people can't stop talking about. The ones always popping up in decklists. The ones always getting traded back and forth. But while **Magic** development spends a lot of time on these high-profile cards, we also spend a huge amount of time developing even the most humble, low-profile cards in the set.

So today I'll take you through how much development can go into even one of the humblest, lowest-profile cards in all of *Eventide*. Today's honoree? The common, white, five-mana 2/3 flier: [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). While he may not be the talk of the town, he's got several important jobs to do in *Eventide*, and he does them well. And I've got five different development stories to show you how.

![Kithkin Spellduster](https://i.ormos.uk/1e/dd/1edd475855d5da264fc2f67c16aff8e15a6b117a07a39e063915249cb8c85525.jpg)

### Test of the Twins

There's a long history of white creatures dissolving enchantments, and *Morningtide* and *Eventide* each had one, until we noticed a problem between them. See if you can spot it:

> CW03\_MOR  
>  Puff Pastry  
>  3W  
>  Creature - Elemental  
>  0/0  
>  Flying  
>  CARDNAME comes into play with two +1/+1 counters.  
>  1W, Remove a +1/+1 counter from CARDNAME: Destroy target enchantment.

> CW02\_EVE  
>  Winged Demystifier  
>  3W  
>  Creature - Kithkin Wizard  
>  2/2  
>  Flying  
>  Persist (When this creature is put into a graveyard from play, if it had no -1/-1 counters on it, return it to play under its owner's control with a -1/-1 counter on it.)  
>  1W, Sacrifice CARDNAME: Destroy target enchantment.

What's the problem with these two cards? The problem is they're actually both the same card. Each one comes out as a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 Flier, you can pay ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and shrink your flier to 1/1 to destroy an enchantment, and then you can pay ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and sacrifice your flier to destroy a second enchantment. Continuing the similarity, adding +1/+1 counters to either card lets you destroy more enchantments, whether by adding more +1/+1 counter ammunition to spend or by removing the -1/-1 counter from persist. The two versions interact differently against [Shock](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) or combat damage, but the overall role of the two cards is very much the same.

Both *Morningtide* and *Eventide* were in development at the time, and the two cards were too similar. Whether by changing numbers or changing abilities, one of them would have to move. The two cards edged into a tense staring contest. Each card was poised to attack, waiting for the other one to blink. It was so quiet you could hear a +1/+1 counter drop.

Suddenly a fierce hail of demystifying broke out, with enchantments being torn apart right and left! Or maybe that was some movie I saw. Oh right, I am getting it confused with the movie "*Hexhunter vs. [Wispmare](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wispmare): [Tempest of Light](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tempest+of+Light)."* In any case, The *Morningtide* team decided to move its card to ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) with one +1/+1 counter, largely to make room for *Morningtide*'s [Burrenton Bombardier](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burrenton+Bombardier) to change to ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 flying, and for [Kithkin Zephyrnaut](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Zephyrnaut), [Order of the Golden Cricket](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order+of+the+Golden+Cricket), and [Ballyrush Banneret](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ballyrush+Banneret) all to settle on 2 power at white common.

<table><tbody><tr><td><a href="https://web.archive.org/web/20080718000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&amp;name=Elvish%2BHexhunter"></a><a href="https://web.archive.org/web/20080718000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&amp;name=Elvish%2BHexhunter"><img alt="Elvish_Hexhunter" src="https://i.ormos.uk/90/cc/90cc25fdbe432ffff36468a25887b69d5fbd235fb69fdf8078d7972fa055d87d.jpg"></a></td>&#10;			<td><a href="https://web.archive.org/web/20080718000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&amp;name=Wispmare"></a><a href="https://web.archive.org/web/20080718000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&amp;name=Wispmare"><img alt="Wispmare" src="https://i.ormos.uk/1b/bc/1bbcac0cc0da89837993fa2896cbf469afc63b13297e894cb2e1a02af2ce9d79.jpg"></a></td>&#10;		</tr></tbody></table>

By now you probably recognize the *Morningtide* and *Eventide* cards as [Shinewend](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend) and [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). The cute part about [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) still being ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 at the time was that when the ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) died and persisted, it basically popped out a [Shinewend](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend). And when [Shinewend](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend) got reinforced for 1, it basically popped into a [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster).

![Shinewend](https://i.ormos.uk/6d/a2/6da2a4605ae7a4c97d05cf42c7859ef23a4601106e0027a0f6ef24a8d74c2ac2.jpg)

To smooth out the mana costs and power/toughness of the set, [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) eventually advanced to his final ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/3 form. The ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 flier slot, once so coveted by the two cards, ended up abandoned by both of them.

### The *Eventide* Style of Persist

Now the second story. Part of the key to block design is finding ways to link the sets in the block together, yet give each of the sets its own unique identity. Well-designed block plans perform this balancing act on a wide spectrum, from large and obvious to small and subtle.

The most obvious, global way that *Shadowmoor* and *Eventide* "compare and contrast" in this manner is that they're both hybrid sets, but one is allied-color and one is enemy-color. On the other end of the spectrum, one of the most subtle ways that *Eventide* is different from *Shadowmoor* is the way the two sets use persist.

*Shadowmoor* has six persist creatures with "comes into play" abilities: [Furystoke Giant](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furystoke+Giant), [Kitchen Finks](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks), [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), [Puppeteer Clique](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique), [Twilight Shepherd](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twilight+Shepherd), and [Woodfall Primus](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodfall+Primus). *Shadowmoor* has no Persist creatures with "sacrifice me" abilities.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Woodfall Primus" src="https://i.ormos.uk/b2/e7/b2e7f61c72c2e5eb67c4a53c8a20c04480568168f1e80a2ac76e88760cfe9139.jpg"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Aerie Ouphes" src="https://i.ormos.uk/8f/0d/8f0da9b17952b0bfbfbc559c3a400a2bad74b2f6d988c626d5c382bb238b6eed.jpg"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

Conversely, *Eventide* has four Persist creatures with "sacrifice me" abilities: [Aerie Ouphes](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aerie+Ouphes), [Glen Elendra Archmage](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage), [Grazing Kelpie](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grazing+Kelpie), and [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). And *Eventide* has no persist creatures with "comes into play" abilities.

Persist allows you to get two uses of out of either a "comes into play" or a "sacrifice me" ability. But each set's persist creatures get two uses of out their abilities in their own way.

### "Creature — Kithkin"

![Rustic Clachan](https://i.ormos.uk/62/09/620987a94017f3b0172726536fc7b1f50e1ebdd886e41c2c178ce8b991cdb0d0.jpg)

Time for a third story. Fellow columnist and **Magic** R&D all-star Doug Beyer did the concepting work for *Eventide*. In addition to his role on the creative team, Doug had also worked on the development teams for *Lorwyn* and *Shadowmoor*, giving him considerable insight into the mechanics of the two blocks. During *Eventide* concepting, Doug used this mechanical knowledge to help set up flavor concepts and creature types that would intentionally flow well into the individual tribal themes of *Lorwyn* and *Morningtide*.

One example is [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). Before writing out a full concept for the card, Doug wrote this note into Multiverse to show his creative team colleagues what he was leaning towards:

> DB 8/14: Kithkin, to combo with kithkin Reinforce land?

Doug's right. [Burrenton Bombardier](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burrenton+Bombardier), [Mosquito Guard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosquito+Guard), and [Rustic Clachan](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rustic+Clachan) are all Kithkin cards with reinforce, and reinforcing your persist creature to recharge it is a fun little combo. Reinforce cards like the [Pro Tour–winning](/en/articles/event-coverage/2008/02-16-top-8-decks) card [Mosquito Guard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosquito+Guard) already let you convert spells and lands into +1/+1 counters. Combining them with [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) lets you convert those spells and lands into extra [Demystify](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demystify)s.

Doug Beyer and *Eventide* lead developer Matt Place also worked together to ensure that [Nettle Sentinel](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nettle+Sentinel), [Twinblade Slasher](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twinblade+Slasher), [Talara's Battalion](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talara%27s+Battalion), and [Bloom Tender](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloom+Tender) were all Elves, that [Wake Thrasher](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wake+Thrasher) was a Merfolk, and the other creatures were particular creature types, in order to open them up to mechanical synergies with *Lorwyn* and *Morningtide*.

### "Creature — Wizard"

Story number four: The "class" creature type is especially relevant on persist cards too. Developer Mons Johnson quickly found during *Shadowmoor* development that having the persist creature [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) be a Goblin Rogue, as the Redcap once was, was a particularly terrible idea.

![Oona's Blackguard](https://i.ormos.uk/73/d7/73d78a30c354ed02f51c88cff3ba84ac885816851ea4191d9d5290c7fa36d243.jpg)

Mons took advantage of the Redcap's creature type by building a deck with [Oona's Blackguard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard), [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), and sacrifice outlets like [Greater Gargadon](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Gargadon) and [Nantuko Husk](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk). Mons would get [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) and [Oona's Blackguard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard) into play, then start sacrificing the Redcap to his Husk or Gargadon.

Every time the [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) came back into play with a -1/-1 counter through Persist, [Oona's Blackguard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard) put a +1/+1 counter on the Redcap because it was a Rogue. There's a rule that a +1/+1 counter and a -1/-1 counter on the same creature annihilate each other and disappear. So the Redcap would be back without any counters on it at all, dealing 2 damage to the opponent's face. Sacrifice the Redcap again, deal 2 more damage. Sacrifice it 8 more times, and, well, you get the idea.

This combo was a little too consistent, especially since one of the combo pieces had persist, and another of the combo pieces didn't even need to be in play (the [Greater Gargadon](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Gargadon)). It was enough to get us to change the [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap)'s creature type to the even more flavorful Goblin *Assassin.*

Message to [Scarblade Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scarblade+Elite): You're welcome.

Tricky Mons built a similar deck using [Bramblewood Paragon](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon), [Nantuko Husk](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk), and [Safehold Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), who was at the time an Elf Warrior. Infinite sacrifices made the [Nantuko Husk](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk) immediately lethal, and he sometimes added an [Essence Warden](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Warden) to gain infinite life. [Safehold Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) became an Elf Scout.

Mons had hit the nail on the head twice in a row, and it was enough to make us wonder: Should we just yank Rogue, Warrior, and Wizard—the three creature types with similar lords in *Morningtide*—off of all the persist creatures? This would damage some of the creative choices, since the concept of [Puppeteer Clique](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique) was very much a Wizard, and the concept of [Scuzzback Marauders](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuzzback+Marauders) was very much a Warrior.

In the end, as we often decide with infinite win-the-game combos, we decided that these combos between persist and *Morningtide* class lords are actually pretty fun and good for **Magic**, as long as they're not too hyper-efficient. Our playtesting had suggested that that [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), [Oona's Blackguard](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard), [Safehold Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), and [Bramblewood Paragon](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon) all had a shot to be powerful tournament contenders (as they have indeed turned out to be, at varying levels) even without creating infinite win-the-game combos between them.

But if people are willing to commit to their combos with a higher-mana-cost persist creature, instead of the two-mana [Safehold Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) or the very powerful four-mana [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), we wanted to give them the chance to "go infinite" and win the game that way. So while [Safehold Elite](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) and [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) became Scouts and Assassins, you can still go infinite with these combos with five-mana Persist Warriors, Wizards, and Rogues.

Possibilities include [Furystoke Giant](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furystoke+Giant), [Puppeteer Clique](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique), and [Scuzzback Marauders](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuzzback+Marauders) in *Shadowmoor*, all at five mana. Since [Glen Elendra Archmage](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) is less universal than [Murderous Redcap](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), and doesn't have the Redcap's "comes into play" ability, we were ok with letting [Glen Elendra Archmage](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) and [Sage of Fables](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) create infinite sacrifices, even though [Glen Elendra Archmage](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) matches the Redcap's four mana. Using the [Glen Elendra Archmage](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) in the combo with [Sage of Fables](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) even lets you counter an infinite number of noncreature spells along the way.

![Sage of Fables, Glen Elendra Archmage, and Nantuko Husk](https://i.ormos.uk/84/4e/844e79e2218e359e82f3decfc1b0729f7dd5aa1378a40596545ec087b3d06688.jpg)

And what's the final *Eventide* card that creates infinite win-the-game sacrifice combos with *Morningtide* class lords? But of course: [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster).

### The Gift of Lockdown

And the final story. All ten [Steel of the Godhead](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+of+the+Godhead)–style hybrid Auras in Shadowmoor and Eventide can be totally devastating if they don't get stopped. Fortunately there are a variety of ways to stop them. One of the reasons [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) is so good at blowing up Auras is to put commons into *Shadowmoor* and *Eventide* that are good at blowing up the hybrid Auras before they get too out of hand. Another common that's fantastic at blowing up the Auras in *Eventide* is [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder).

![Gift of the Deity](https://i.ormos.uk/66/6b/666b767ca91bec1e398aaea70f20820fd5710b1dd3d361ce211f6fb285235da5.jpg)

But although [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) were intended to be able blow up the hybrid Auras, the black-green Aura [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) didn't get the memo. Midway through *Eventide* development, [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) cost ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black-green.gif), giving [Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure), deathtouch, and +2/+2 to black-green creatures.

Many debates had already been waged about whether these ten hybrid Auras should be common or uncommon. The development team leads for *Shadowmoor* and *Eventide* had both concluded that the auras should be both common and very powerful—as long as they landed on the correctly colored creatures and didn't get disrupted by the opponent.

The chance of the Auras getting ruined by the opponent is a big part of why the Auras can be so powerful. When they work, they are awesome. But when you play a [Cerulean Wisps](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cerulean+Wisps) in the middle of combat to turn the opposing enchanted creature blue, turn off all of its Aura's color-based abilities, and kill both the enchanted creature and the Aura while drawing a card in the process, you can totally crush them.

The card "[Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)" has always been a very powerful uncommon. [Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure) effects with a power/toughness bonus are even nastier, since you can lock down your opponent from ever building up creatures. For example, if you play [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) on your Rendclaw Troll on turn four and attack, you can kill an opposing creature or two by forcing them to block, and stick your opponent with a nasty dilemma. If your opponent plays anything up to a 3/6, you just attack, force it to block, and kill it, losing nothing. If he or she doesn't play a creature, you just smash your opponent for 4 damage.

If your opponent plays the red-white Aura [Scourge of the Nobilis](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+of+the+Nobilis), [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) are decent answers. You'll take some damage, then play your creature and destroy the Aura.

![Wickerbough Elder](https://i.ormos.uk/a4/0a/a40a21729c128d3d81d601614b9117cda3c28a0447fc39447621538889710fa3.jpg)

But against a four-mana [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity), [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) weren't able to answer the problem. If you played a turn-four [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder), it would just get [Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)d and destroyed before it could activate. If you played a turn-five Spellduster Kithkin, it would just get [Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)d and destroyed as well.

On the face of it, [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) could persist back into play and blow the Aura up, and sometimes that would happen. But out of all ten color pairs, black-green has the most creatures with wither (including [Rendclaw Trow](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rendclaw+Trow), [Noxious Hatchling](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noxious+Hatchling), and often [Woodlurker Mimic](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodlurker+Mimic)), meaning that [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) could not even persist back into play.

In the end, the combination of [Lure](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure), power-pumping, toughness-pumping, and deathtouch in a four mana version of [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) just locked down too many people too quickly during playtesting, stopping them from playing any more creatures too early. We still loved the thrill of power it gives when you play it, but five mana gives just a bit more breathing room before the pummeling starts.

And it gives you a little more time to play and activate your [Wickerbough Elder](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) or [Kithkin Spellduster](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) without them getting bludgeoned to death by [Gift of the Deity](https://web.archive.org/web/20080718000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) before they can activate to destroy it.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>Are you going to the <i>Eventide</i> Prerelease?</b></th>&#10;		</tr></thead><tbody><tr><td>Yes</td>&#10;			<td>3736</td>&#10;			<td>44.4%</td>&#10;		</tr><tr><td>No</td>&#10;			<td>3476</td>&#10;			<td>41.3%</td>&#10;		</tr><tr><td>Not Sure</td>&#10;			<td>1196</td>&#10;			<td>14.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>8408</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

Wizards sent a huge contingent, over a dozen people, to the Seattle pre-release to gunsling and talk about *Eventide*. It's hard to resist the lure of playing with real **Magic** cards instead of playtest stickers! Mark Gottlieb happened to find himself in Denver that weekend, so of course he dropped in on the Denver prerelease to gunsling and have a good time.

Mark your calendars: Prereleases will occur all over the world for Shards of Alara on September 27. Many new prereleases will now be happening in local card stores, as well as many pre-releases happening in giant halls just like before.

### This Week's Poll

<table><tbody><tr><td><b>Starting in <i>Lorwyn,</i> a sixteenth creature-token-card/rules-card was added to <b>Magic</b> packs. Was the change good or bad?</b> GoodBadIt's complicated</td>&#10;		</tr></tbody></table>