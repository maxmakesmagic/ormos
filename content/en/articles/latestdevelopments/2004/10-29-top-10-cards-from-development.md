---
id: h62yc8er
kind: article
lang: en
path: /en/articles/latestdevelopments/2004/10-29-top-10-cards-from-development
title: Top 10 Cards from Development
published: '2004-10-29'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    lang_detected: en
    capture_id: 735510
    url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    captured_at: '2022-08-17 23:44:25+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    lang_detected: en
    capture_id: 735510
    url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    captured_at: '2022-08-17 23:44:25+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    lang_detected: en
    capture_id: 735510
    url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    captured_at: '2022-08-17 23:44:25+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    lang_detected: en
    capture_id: 735510
    url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
    captured_at: '2022-08-17 23:44:25+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: h62yc8er
  url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
  page_key: magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
  lang: en
  template: drupal
  captured_at: '2022-08-17 23:44:25+00'
  capture_id: 735510
  wayback_url: https://web.archive.org/web/20220817234425id_/https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
- document_id: h62yc8er
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af38&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af38
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:39:42+00'
  capture_id: 253238
  wayback_url: https://web.archive.org/web/20090604153942id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af38&print=true
- document_id: h62yc8er
  url: http://magic.wizards.com/en/articles/archive/top-10-cards-development-2004-10-29
  page_key: magic.wizards.com/en/articles/archive/top-10-cards-development-2004-10-29
  lang: en
  template: drupal
  captured_at: '2017-08-24 16:03:06+00'
  capture_id: 1199013
  wayback_url: https://web.archive.org/web/20170824160306id_/http://magic.wizards.com/en/articles/archive/top-10-cards-development-2004-10-29
- document_id: h62yc8er
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af38,,ja
  page_key: wizards.com/default.asp?x=mtgcom/daily/af38
  lang: en
  template: classic_asp
  captured_at: '2005-03-18 21:51:11+00'
  capture_id: 1928523
  wayback_url: https://web.archive.org/web/20050318215111id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af38,,ja
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: h62yc8er
  capture_id: 735510
  url: https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
  wayback_url: https://web.archive.org/web/20220817234425id_/https://magic.wizards.com/en/articles/archive/latest-developments/top-10-cards-development-2004-10-29
  captured_at: '2022-08-17 23:44:25+00'
  template: drupal
  sha256: 29535cf815df9f0d7d762fd33267d8cadf92e865b8359d376d051099dee738bb
render_recovery: []
---
[Last week](/en/articles/feature/2004/10-22-gottliebs-fan-mail), I talked about how developers and designers are different. Designers make cards, and developers massage them. I also mentioned that Mark Gottlieb has made cards, and I have mentioned time and again that I've made cards myself.

That's one of the perks of development—you often get to do a little design on the side. In fact, because developers understand the tournament environment better than designers, many of the cards that shake up or solidify metagames are created by developers.

Here is my list of the Top Ten cards made by development teams since I started working here:

### 10) [Auriok Champion](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Champion)

In the very last week of *Fifth Dawn* development, a lot of us around the department were really worried that Goblin decks, specifically those with [Patriarch's Bidding](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Patriarch%27s+Bidding), were going to be completely out of hand. Goblin Bidding was doing incredibly well in our internal leagues, and was tearing up real-world Standard as well. Lead developer Brian Schneider was on vacation, so Matt Place, Devin Low, and I decided to see if we could come up with a card that would give decks a good solid option against Bidding without being a really obvious [Tsabo's Web](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tsabo%27s+Web)-style hoser.

The problem was that if we wanted to make the card, we needed to figure out how to work it into *Fifth Dawn*, and the art for that set was already all done. We started looking for expendable cards and didn't have to look far. In the file was a common 1/1 creature for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) that got +0/+3 if it was equipped. And to boot it had amazing art featuring a lovely Auriok lady. That card needed to go, and its art had to be put to better use! We came up with a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 1/1 pro-red, pro-black [Soul Warden](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Warden) over the course of a morning and played it for the next few days. It did a good job of giving white a card that could come down early and be a real stickler for Bidding decks. Brian came back to work and decided to go forward with our plan, and we cleared out a slot in rare for the new [Auriok Champion](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Champion).

To do so, we had to take art that was previously on a rare and make a new common that could use it. The old rare was something along the lines of:

> \[Don't Touch My Stuff\]  
> ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)  
>  Enchantment  
>  Whenever an ability of a permanent controlled by an opponent causes one of your artifacts to be put into your graveyard, destroy that permanent and return the artifact card from your graveyard to your hand.

It basically could save your stuff from [Viridian Shaman](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viridian+Shaman)s, [Oblivion Stone](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Stone)s, and the like, but it was a little weird and not well loved. The art showed a magical shield repelling a destructive-minded goblin. The new card that was made to house that art? [Armed Response](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armed+Response).

A couple of weeks later, pro player Zvi Mowshowitz joked in an online article that the card he would be submitting for the **Magic** Invitational would be a white card that removed all Goblins from the game and prevented any more from being played. We were a step ahead of Zvi and thought we had a slightly more elegant solution. Of course, by the time *Fifth Dawn* hit Constructed in the real world, Goblins had been supplanted by Affinity as the aggro deck of choice, making [Auriok Champion](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Champion) not all that necessary. I am pleased, however, that the card was well-received by casual players and is considered one of the cooler cards in the set by them.

### 9) [Viridian Zealot](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viridian+Zealot)

As the *Mirrodin* Standard and Block environments were being sketched out internally, we decided to really hammer home green's hatred of artifacts as a sort of “check” on the ridiculous artifact decks we knew would spring forth from the cards available.

The original version of the card was called “Cool Cat,” and activated for only ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). The idea behind the card was to make an efficient creature that could wreck artifacts and not be dead against non-artifact decks. There was some argument about whether it should destroy enchantments, but with [Astral Slide](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide) running around we kept him as a walking [Naturalize](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize).

The card was eventually weakened due to the frustration of many players (myself included) at the inability to keep a single artifact on the table for more than a turn. The artifact block is not all that fun when you can't use your artifacts! Of course, as Affinity decks came together, it later became obvious that artifacts were public enemy number one. Quirky artifact decks had no chance in the environment. Seeing as how the Zealot isn't showing up in the numbers we expected, the change may have been unnecessary.

![Samurai of the Pale Curtain](https://i.ormos.uk/34/0e/340ebf5d0e46a500cc9a184f2de5b530730d31e396f7c88f9a013659909b6605.jpg)

### 8) [Samurai of the Pale Curtain](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samurai+of+the+Pale+Curtain)

As *Champions of Kamigawa* Standard began shaping up in our internal league, a few things were evident. [Skullclamp](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp) was insane. [Eternal Witness](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eternal+Witness) was everywhere. Kamigawa had its own share of annoying stuff going on, including soulshift and the “death” triggers on the Dragons. We wanted an elegant way to stop people from being able to abuse their graveyards willy-nilly. We quickly came up with “Planar Samurai,” a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 with bushido 1 that had a static ability similar to the old card [Planar Void](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Planar+Void). By making the ability a replacement rather than a trigger, it allowed us to keep [Skullclamp](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp) from drawing cards, [Disciple of the Vault](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) from triggering, and modular from working at all. The original version prevented cards from going to the graveyard from anywhere, not just permanents in play, so it really weakened [Eternal Witness](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eternal+Witness). And the best part was that, for all it did to dampen the powerful cards from *Mirrodin* block, it had a real part to play within Kamigawa as well, keeping soulshift and Dragon triggers in check.

We ran into problems with the original wording because it still allowed tokens to go to the graveyard, even though cards did not. This mattered a lot with [Skullclamp](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp) still around, especially because of interactions with cards like [Genesis Chamber](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Genesis+Chamber) and [Beacon of Creation](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beacon+of+Creation). Fearful that this subtlety would go unnoticed by most players and lead to a lot of arguing, we toned it down a little to just affect permanents.

### 7) [Darksteel Citadel](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darksteel+Citadel)

As the indestructible mechanic was being fleshed out during *Darksteel* development (how annoying was it, how many cards should have it, what kinds of cards can it go on, etc.), **Magic**'s lead developer at the time -- Randy Buehler -- postulated that perhaps an indestructible artifact land would be cool. He shopped the idea around to see if people liked it.

I'll admit that I gave it my personal thumbs-up at the time. It is a great card conceptually; too bad it ended up so darn good.

![Kodama of the North Tree](https://i.ormos.uk/48/e5/48e502e6725ccda1d674efe4120a88ac27fdafbeae5e0c4748bf7d43f315ef8c.jpg)

### 6) [Kodama of the North Tree](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kodama+of+the+North+Tree)

There was a lot of discussion early on in Kamigawa development about how good a legendary creature should be compared to a non-legendary creature of the same mana cost. The consensus was that they should be noticeably better, but not by a factor so large that players would falsely perceive what we call “power-creep,” which is a phenomenon that occurs when we feel that we constantly have to outdo ourselves in terms of the power level of cards from set to set. We generally try to avoid overall creep of sets over time, but we like cards to at least look like their better than stuff we've made previously. In other words, we wanted legendary creatures to match players' perceptions of how good legendary creatures should be without going over. Once those loose guidelines were in place, the team noted that none of the green legends in the set that were meant to be impressive “fatties” felt like they were any better than non-legendary creatures of the same cost. So the team decided to make one out of whole cloth.

The first attempt at the North Tree was a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) 6/6 untargetable trampler. I remember Brian Schneider coming out of the development meeting and calling to Paul Sottosanti, “Paul, would you be excited by a five-mana 6/6 untargetable trampler?”

Needless to say, we were all pretty excited, and threw that big boy into tons of decks. And you know what? He was never dying. It was impossible to muster six points of power against it on defense, and in usually just ran everyone over. So we came to our senses and lowered his toughness to four--still an awesome card.

### 5) [Rude Awakening](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rude+Awakening)

The design file for [Fifth Dawn](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fifth+Dawn) did not contain any rare entwine cards, and the development felt there should be some. Development lead Brian Schneider, always a fan of [Early Harvest](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Early+Harvest), wanted a card that could untap all your lands, and designed [Rude Awakening](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rude+Awakening).

In our testing, we found that the card wasn't played as [Early Harvest](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Early+Harvest) very much at all except in the occasional goofy [Mind's Desire](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire) deck. Instead it was almost like a green [Fireball](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball), used to finish off unsuspecting opponents with an attack for 16 out of the blue. We liked that effect enough to print the card.

### 4) [Troll Ascetic](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Troll+Ascetic)

I remember being invited to a playtesting meeting when I was still working on the website. [Astral Slide](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide)/[Lightning Rift](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift) decks were just hitting the tournament scene, and we were given the question, “What kind of green creature can exist in a world full of Rifts and Slides?”

The group came up with [Troll Ascetic](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Troll+Ascetic), a 3/2 green regenerator that had a unique twist on untargetability. You could still equip and enhance it, but your opponent couldn't touch it. The original regeneration cost on it was a generous ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), but the team was receiving complaints about the power level from frustrated playtesters (one Troll could ruin a Zombie deck's entire day), so we ratcheted it down a notch.

### 3) [Nantuko Shade](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Shade)/[Mutilate](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutilate)/[Mind Sludge](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sludge)

*Torment*'s distinction as the black set seems inherently tied to these three cards, so you may be surprised to know that they weren't part of the file handed off by design. Yes, the design file had more black cards than any other color, and had lots of cards that interacted with black in new ways, such as [Tainted Forest](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tainted+Forest) and [Balshan Collaborator](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balshan+Collaborator). You certainly noticed all the black cards and black-influenced cards when you went through the set, but when it came time to build decks, very few cards screamed “Play lots and lots of black!”

After some brainstorming and careful consideration, Henry Stern and the rest of the development team came up with [Nantuko Shade](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Shade), [Mutilate](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutilate), and [Mind Sludge](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sludge). By adding these three cards, each of which gets more potent the more [Swamp](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s that are in your deck, the team made black a real force in constructed, plus gave the set just what it needed -- cards that let you know in no uncertain terms that this set belonged to black.

### 2) Kamigawa Dragons

[The Dragons](https://web.archive.org/web/20041029000000/http://gatherer.wizards.com/default.asp?term=dragon_spirit&fields=%7Ctype&format=ChampionsofKamigawa&color=All&output=summary&sort=name&first=1) were a rough patch in the Kamigawa design. The team knew it wanted five Dragons, it had art commissioned for five Dragons, but when the file was handed over, the Dragons had no definitive design. They were essentially left up to development.

After looking at the art and determining that they didn't have “breath weapons,” reading the creative documents and determining that they were really intelligent, and reviewing all the older cycles of Dragons we' d done previously to make sure something innovative was attempted, the team, lead by Schneider, came up with the “goes to graveyard” triggers that hinted at these Dragons' will to survive, as well as their supernatural ties.

Henry Stern made the very important suggestion to lower their mana costs from 7 to 6, and Mons Johnson came up with the unique mana cost system (Blue and red—the “dragon” colors—have very splashable Dragons, whereas green—the color that rarely ever gets decent flyers—has a Dragon that needs to be played in a dedicated green deck).

![Platinum Angel](https://i.ormos.uk/4a/1e/4a1efd6f21907eadf3489f18f913d178589f1a7107f8b5f0676546f36c546405.jpg)

### 1) [Platinum Angel](https://web.archive.org/web/20041029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel)

A great card… but not a particularly interesting story. As I said before in my "[Angels in the Outfield](/en/articles/latestdevelopments/2004/06-25-angels-in-the-outfield)" article, we had art of a metallic Angel and no card to put it on. Development brainstormed ideas and came up with the idea that the Angel was your personal protector—you couldn't lose the game as long as it was on the table. And so was made one of the most loved and hated cards of recent memory.

Next week, kickin' it old school style: My trip to Richmond to play Vintage, and another Top Ten list—the ten finalists for the new name of Type 1.5!

### Last Week's Poll:

<table><thead><tr><th colspan="3">Do you own any of the Power Nine? </th>&#10;		</tr></thead><tbody><tr><td>No</td>&#10;			<td>8599</td>&#10;			<td>69.1%</td>&#10;		</tr><tr><td>I don't even know what those are</td>&#10;			<td>2033</td>&#10;			<td>16.3%</td>&#10;		</tr><tr><td>Yes all nine</td>&#10;			<td>647</td>&#10;			<td>5.2%</td>&#10;		</tr><tr><td>Yes one card</td>&#10;			<td>531</td>&#10;			<td>4.3%</td>&#10;		</tr><tr><td>Yes two or three cards</td>&#10;			<td>315</td>&#10;			<td>2.5%</td>&#10;		</tr><tr><td>Yes four to eight cards</td>&#10;			<td>313</td>&#10;			<td>2.5%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>12438</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>