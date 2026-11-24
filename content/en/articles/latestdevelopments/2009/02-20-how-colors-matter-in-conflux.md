---
id: 1hshw40s
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/02-20-how-colors-matter-in-conflux
title: How Colors Matter in Conflux
published: '2009-02-20'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    lang_detected: en
    capture_id: 723109
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    captured_at: '2022-08-19 18:17:20+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    lang_detected: en
    capture_id: 723109
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    captured_at: '2022-08-19 18:17:20+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    lang_detected: en
    capture_id: 723109
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    captured_at: '2022-08-19 18:17:20+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    lang_detected: en
    capture_id: 723109
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
    captured_at: '2022-08-19 18:17:20+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 1hshw40s
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
  lang: en
  template: drupal
  captured_at: '2022-08-19 18:17:20+00'
  capture_id: 723109
  wayback_url: https://web.archive.org/web/20220819181720id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
- document_id: 1hshw40s
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/26
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/26
  lang: en
  template: aspx
  captured_at: '2013-07-07 17:23:06+00'
  capture_id: 620534
  wayback_url: https://web.archive.org/web/20130707172306id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/26
- document_id: 1hshw40s
  url: http://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18
  lang: en
  template: drupal
  captured_at: '2016-08-12 05:13:03+00'
  capture_id: 723106
  wayback_url: https://web.archive.org/web/20160812051303id_/http://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1hshw40s
  capture_id: 723109
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
  wayback_url: https://web.archive.org/web/20220819181720id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-20
  captured_at: '2022-08-19 18:17:20+00'
  template: drupal
  sha256: 6a73096f03f00d1e7d4c63d84a114671bcea519b7a8391e224cc8da75bafb9f7
render_recovery: []
---
Many Latest Developments columns talk about the journeys of individual cards in painstaking detail, which paints a picture of a world where developers take fully formed design files and quietly tweak numbers and text boxes until the set is ready to print. This is not an entirely accurate picture. Often we identify something that we want a card somewhere in a set to do, discover that there is no such card at the moment, and create one that does what we need done. Other times, we identify cards that aren't working, realize that we don't have anything in mind for the slot, and ask designers for submissions. We are also not afraid to make sweeping changes to entire mechanics to improve game play. This happened during *Conflux* development with the suite of monocolored cards that mechanically encourage multicolor play. Today I'll talk about what happened to those cards and why we decided to change them.

![](https://i.ormos.uk/61/c8/61c84561eeac0c5511c780ae073d2c36259c994259894c248d6722ba264a63d7.jpg)

The designers of *Conflux* were obligated to continue the multicolor theme of *Shards of Alara* while also introducing new twists. *Shards of Alara* contained many monocolored cards with activation costs that used other colors of mana from the card's home shard. *Conflux* does contain some of these, but the designers also chose to include monocolored cards that have conditional static and triggered abilities that turn on based on multicolor play. They tried various incarnations of these, and eventually chose to key off of basic lands. For example, a black card would give you a bonus if you controlled an [Island](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island). The file that the designers handed off to development contained about ten cards like that, and they emphasized to the developers that those cards were important because they gave the set more of a multicolor feel without using tons of gold cards.

One of the first things that developers do with sets fresh out of design is play lots of Limited. This helps us identify what is fun and not fun about what the commons in the set are doing. It's also useful because if a set's commons have problems, then it's likely that the uncommons and rares that are riffs on the themes of those commons also have problems.

Our early Sealed Deck and draft playtests quickly showed us that much of the power at common was located in the "basic land matters" cards. For example, the design handoff versions of [Parasitic Strix](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) and [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) looked like this:

> Parasitic Strix  
>  2U  
>  Artifact Creature – Bird  
>  2/2  
>  Flying  
>  When Parasitic Strix comes into play, if you control a Swamp, target player loses 2 life and you gain 2 life.

> Sedraxis Alchemist  
>  2B  
>  Creature - Zombie Wizard  
>  2/2  
>  When Sedraxis Alchemist comes into play, if you control an Island, return target nonland permanent to its owner's hand.

Those cards were very, very powerful. Seasoned players might recall that [Blind Hunter](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blind+Hunter) and [Man-o'-War](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War) were both famously high picks in their respective draft formats. [Parasitic Strix](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) doesn't give you a second chance at draining your opponent, but it also costs one less and gives you the ability to play it before you have a [Swamp](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp), which are both big advantages. [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) doesn't compare quite as well to its predecessor as [Parasitic Strix](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) does, but it was still very powerful compared to our modern commons. [Dark Temper](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Temper) was also comically strong in Limited when it only required a [Swamp](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp). It did a pretty good impression of [Terminate](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate), and when it wasn't doing that, 2 damage was still quite exciting much of the time.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Parasitic Strix" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Parasitic+Strix"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Sedraxis Alchemist" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sedraxis+Alchemist"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

One way to handle this would have been to add some mana to the costs of those cards. The basic land–requiring versions of [Parasitic Strix](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) and [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) are both still powerful at four mana. However, we weren't thrilled with having great Limited cards that should be showing off the themes of the set be anemic-looking four-mana 2/2's. We noted the problem and kept looking at the rest of the set.

![Dark Temper](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dark+Temper)

We also play Constructed early in a set's development, but with much less structure than we use when specifically testing competitive Standard. By encouraging people to play whatever they want, we can identify which new cards are the most exciting and fun, and we try to protect those cards as the set moves through development.

![](https://i.ormos.uk/d6/74/d6743a112177d0dc55d8255e4d48ecdc869d7e04d9d4d187063743ec714d2cc9.jpg)

When we did this, we discovered that requiring basic lands plays very poorly in Constructed. Playing multiple colors almost always involves playing some number of nonbasic lands. Using "basic land matters" to reward multicolor play worked fine for Limited, but in Constructed it was really frustrating. We wanted to run multiple colors to play the new cards, but the very thing that we had to do to support the actual gold cards made the "basic land matters" cards worse. This is clearly very bad for cards that are supposed to be exciting and fun to play with in any multicolor deck.

![Cliffrunner Behemoth](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cliffrunner+Behemoth)

For example, [Cliffrunner Behemoth](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) stood out to many people as a card that they wanted to play with. At the time, it looked like this:

Cliffrunner Behemoth  
 3G  
 Creature - Rhino Beast  
 5/3  
 Cliffrunner Behemoth has haste as long as you control a Mountain. Cliffrunner Behemoth has lifelink as long as you control a Plains.

The most natural thing to do with it was to put it in a mainly green deck that splashed white or green. Those decks wanted to use cards like [Noble Hierarch](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch) and [Birds of Paradise](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) to speed out big creatures. However, those decks didn't have room for very many [Plains](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) or [Mountain](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s if they wanted to both consistently play a mana creature on turn one and be able to play white or red cards if their mana creatures got killed. This left playtesters who tried to build for [Cliffrunner Behemoth](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) frustrated. Some people built awkward mana bases to try to play with the card despite the difficulties; others simply gave up.

The same thing happened to people who tried to play [Bloodhall Ooze](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) and [Kederekt Parasite](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) together. At the time, they looked like this:

Bloodhall Ooze  
 R  
 Creature – Ooze  
 1/1  
 At the beginning of your upkeep, if you control a Swamp, you may put a +1/+1 counter on Bloodhall Ooze. At the beginning of your upkeep, if you control a Forest, you may put a +1/+1 counter on Bloodhall Ooze.

Kederekt Parasite  
 B  
 Creature – Horror  
 1/1  
 Whenever an opponent draws a card, if you control a Mountain, you may have Kederekt Parasite deal 1 damage to that player.

Suppose you are trying to build a black-red FFL deck. You probably want to play four each of [Sulfurous Springs](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfurous+Springs) and [Graven Cairns](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Graven+Cairns), and you might play some [Auntie's Hovel](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auntie%27s+Hovel)s if you choose to play some Goblins. [Bloodhall Ooze](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) asks you to control a [Swamp](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) and [Kederekt Parasite](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) asks you to control a [Mountain](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain), so you might think about splitting the rest of your lands between those two basic land types. However, that fights with the rest of the cards you want to be playing. You would like to be able to play [Flame Javelin](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Javelin)s and [Figure of Destiny](https://web.archive.org/web/20090220000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Figure%2Bof%2BDestiny), but those cards are clearly maximized when all of your lands make red. However, you also don't want to play [Bloodhall Ooze](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) without [Swamp](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s! This was not a fun situation.

![](https://i.ormos.uk/fb/07/fb07e6bdcc7b2361bed53ebd42ae1f4e09398de6f08d7e8b84b02383a4cfe211.jpg)

The final realization that we made was that in many cases there wasn't a ton of difference in play between actual gold cards and the basic land–requiring monocolored versions of these cards. How different is that version of [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) from a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) 2/2 [Man-o'-War](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War)? How different is that version of [Rhox Meditant](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Meditant) from a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/4 that draws you a card? Clearly there is some upside to being able to play them without getting the bonus, but under optimal conditions they felt very close to just being gold. *Conflux* already had tons of gold cards, so we weren't happy if all this mechanic was doing was giving it even more of them even if they weren't gold by mana cost.

It was clear at this point that there were problems across the board with these cards. We were struggling with ourselves about whether to cost them so that they were attractive and very powerful or awkward-looking but still good. They weren't fun in Constructed, and they didn't feel that different from gold cards. At this point, lead developer Mike Turian decided that something needed to be done. Of course, we also needed to preserve the structure that design had built for us. In order to solve this problem, we went back to the designers. The mechanic that they liked second best in design was keying off of controlling colored permanents, so we changed all the cards that required basic lands to the new mechanic and started testing again.

We knew that the Limited cards we were worried about before were now less powerful. [Parasitic Strix](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix), [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist), and [Dark Temper](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Temper) were previously all sure bets when you cast them, because we avoid making land destruction spells that work at instant speed. Now, people could respond to these cards by destroying the permanent that you were planning on using to satisfy the condition. This is clearly less powerful. However, we were okay with that because it meant that we were no longer fighting with ourselves about whether to make the cards exciting or properly balanced. Because they were weaker, we could do the cheaper and more attractive versions and feel good about it.

Although this worked in our favor in Limited, we initially worried that it would hurt us in competitive Constructed. If the cards that were on the edge of Constructed that used the mechanic before were now weaker there also, they might be too weak to play at all. Happily, the opposite turned out to be true and the cards thought would be good in Constructed actually became stronger thanks to the ability to get full value out of them while playing lots of nonbasic lands that supported the actual gold cards you wanted to play.

[Cliffrunner Behemoth](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) improved a lot because of the change. Lots of people had blue-white-green decks with [Noble Hierarch](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch)s, [Birds of Paradise](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), and tons of cheap efficient gold creatures. Most of these creatures were white, so [Cliffrunner Behemoth](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) didn't have to work hard to gain lifelink in these decks. It also played very well in red-green decks with *Shadowmoor* cards like [Vexing Shusher](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Shusher), [Boggart Ram-Gang](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Ram-Gang), and Boar-Tusk Liege. We also discovered the amusing combination of [Figure of Destiny](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny) and [Cliffrunner Behemoth](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth), which worked out much better than I thought it would when we tried it with all of the *Shadowmoor* filter lands that include green.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Vexing Shusher" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Vexing+Shusher"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Boggart Ram-Gang" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Boggart+Ram-Gang"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

[Kederekt Parasite](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) and [Bloodhall Ooze](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) also profited from the change. Black-red beatdown decks including some combination of those cards with [Shambling Remains](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Remains), [Ashenmoor Gouger](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashenmoor+Gouger)s, Demigods of Revenge, and [Blightning](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning)s were staples of our *Conflux*-era FFL testing. Those decks were all fun. Playtester Steve Warner also discovered the amusing combination of [Spiteful Visions](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiteful+Visions) and [Kederekt Parasite](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite), and he has killed me before by using [Ghitu Encampment](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Encampment)s as red permanents for his Parasites.

![](https://i.ormos.uk/2d/30/2d30ea30961377190b22bf398be38ed9b42bd89747231a4e9f2cd1a630a8043d.jpg)

Finally, we were excited because the new versions of the cards didn't feel exactly like gold cards. Even if you have all the right mana, you still need to put together the right group of permanents to get the bonuses. This is exactly the sort of thing that we like to see in a second set twist of a mechanic. It's different from gold cards, but it plays great with gold cards because your gold cards help trigger them and because the nonbasic lands you want to play to support your gold cards don't get in the way. I also really enjoy how swingy and interactive the printed versions of the cards are. Sometimes your [Sedraxis Alchemist](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) is a full-blown [Man-o'-War](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War), which feels very powerful. Other times, your opponent gets to thwart you with a removal spell and you become sad. That kind of back-and-forth interaction makes for great **Magic**.

In the end, I'm thrilled with where the "color matters" cards ended up. They are fun and exciting in Limited and better in Constructed than I ever thought they could be, and they feel like a unique and new development of the block's themes. I hope you enjoy playing with them in the real world as much as I did in the Pit!

<table><tbody><tr><td colspan="3"><b>What is your favorite <i>Conflux</i> mythic rare that is not <a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker">Nicol Bolas, Planeswalker</a>?</b></td><td> </td>&#10;<td> </td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus">Progenitus</a></td>&#10;			<td>1654</td>&#10;			<td>23.3%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Archangel">Maelstrom Archangel</a></td>&#10;			<td>1620</td>&#10;			<td>22.8%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethersworn+Adjudicator">Ethersworn Adjudicator</a></td>&#10;			<td>899</td>&#10;			<td>12.7%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Apocalypse+Hydra">Apocalypse Hydra</a></td>&#10;			<td>692</td>&#10;			<td>9.8%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror-Sigil+Sergeant">Mirror-Sigil Sergeant</a></td>&#10;			<td>663</td>&#10;			<td>9.3%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling">Thornling</a></td>&#10;			<td>624</td>&#10;			<td>8.8%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Child+of+Alara">Child of Alara</a></td>&#10;			<td>394</td>&#10;			<td>5.6%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Malfegor">Malfegor</a></td>&#10;			<td>346</td>&#10;			<td>4.9%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conflux">Conflux</a></td>&#10;			<td>205</td>&#10;			<td>2.9%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7097</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

I asked this week's question in a sideways way because I thought that [Nicol Bolas, Planeswalker](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) was the obvious leading candidate for favorite mythic rare, and I didn't want the poll to come back with tons of votes for him and none for anyone else. I would have guessed that more people would have Nicol Bolas as a favorite. Although he did get a plurality of votes, it seems now that I could have run one poll with all ten mythic rares and gotten something reasonable out of it. I was happy to see that the five-color theme clearly was speaking to people since the top two non-Nicol Bolas picks were [Progenitus](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus) and [Maelstrom Archangel](https://web.archive.org/web/20090220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Archangel), but I was sad to see that less than ten percent of respondents picked my favorite card in the set. Once again, thanks for your feedback.

\[The survey originally included in this article has been removed.\]