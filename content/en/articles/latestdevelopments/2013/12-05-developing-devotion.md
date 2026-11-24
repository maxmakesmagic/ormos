---
id: wf2hda7j
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/12-05-developing-devotion
title: Developing Devotion
published: '2013-12-05'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: adam-prosak-76cf4169
  name: Adam Prosak
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    lang_detected: en
    capture_id: 720747
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    captured_at: '2015-01-26 05:00:03+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    lang_detected: en
    capture_id: 720747
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    captured_at: '2015-01-26 05:00:03+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    lang_detected: en
    capture_id: 720747
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    captured_at: '2015-01-26 05:00:03+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    lang_detected: en
    capture_id: 720747
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
    captured_at: '2015-01-26 05:00:03+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: wf2hda7j
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
  lang: en
  template: drupal
  captured_at: '2015-01-26 05:00:03+00'
  capture_id: 720747
  wayback_url: https://web.archive.org/web/20150126050003id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: wf2hda7j
  capture_id: 720747
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
  wayback_url: https://web.archive.org/web/20150126050003id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05
  captured_at: '2015-01-26 05:00:03+00'
  template: drupal
  sha256: 58f918cf4e809163a597ea1abb6f9e2e6fc92a47ea126499161fa4c076b12e21
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 3
---
Greetings Everyone!

My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make **Magic: The Gathering** the best game it can be. However, one of the things I've missed during my time here is writing. I harassed [Sam Stoddard](https://web.archive.org/web/20131205000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard) enough, and he agreed to loan me his digital space for a week. Thanks Sam! 

The Devotion Mechanic

Devotion is a mechanic that scales endlessly. Nearly any X spell (such as [Fireball](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball)) is a good example of a scaling spell. The amount of damage [Fireball](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) deals is only limited by the amount of mana you are willing to spend. Scaling cards are interesting because they allow you to play different-powered effect depending on the state of the game. Like other scaling cards, cards with devotion are similarly unlimited. Instead of available mana, a card with devotion counts the mana symbols on your permanents. Devotion is different than most scaling mechanics because many of your cards can count multiple times toward your scaling mechanic. A creature that costs ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) counts for two devotion, so it is difficult to plan on a certain amount of devotion. This makes developing devotion cards very tricky, as we want cards to be fun in the most amount of situations possible. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Fireball"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+the+Fates"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Agent+of+the+Fates"></a></td></tr></tbody></table>

  

Imagine for a second that [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) made 1/1 Elemental tokens rather than 1/0 tokens. If you have a large amount of devotion, [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) is incredibly difficult to beat. We decided to allow players to get around huge [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) by simply killing the [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) itself. Now, [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) is incredible with some highly devoted friends, but only if your opponent can't remove it. That is more fun than your opponent simply sitting there helpless regardless of whether or not he or she can remove the [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves). 

On the other side of things, it is also important to make sure that cards with devotion are reasonable plays even if you don't have much (or any) devotion when you play them. [Fanatic of Mogis](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis) is capable of dealing a large amount of damage, but only if you have heavy devotion. If you don't have that much devotion, playing a 4/2 for ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) isn't the worst thing in the world. We tried to make cards that were appealing enough to play even without optimal devotion. Sitting with a card in your hand all game because you can't get devotion going doesn't provide great game play, so we work to avoid those things. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Master+of+Waves"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Fanatic+of+Mogis"></a></td></tr></tbody></table>

  

Making a Card Weaker?

When developing a card, generally we play around with a mana cost if we want to narrow the range of decks a particular card is played in. For example, if we find that a certain card that costs ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) is played in too many decks, we might change its casting cost to ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) to force it into more heavily green decks. 

However, with devotion, a ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) casting cost is often a benefit rather than a drawback compared to a card that costs ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). In a world of devotion, we have to balance the casting costs on cards differently. [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) itself had a mana cost of 2UU at one point. We actually weakened the card by making it easier to cast. 

Nykthos, Shrine to Nyx 

As *Theros* was released, one of development's biggest concerns about the cards concerned [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx). It has been quite some time since we've printed a land capable of making more than one mana, let alone a land that is capable of making a scaling amount of mana. [Tolarian Academy](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy), [Gaea's Cradle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Cradle), and [Cabal Coffers](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Coffers) are lands in a similar space to [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx)—and those lands are among the most powerful cards ever printed and not something we would want to repeat. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Nykthos%2C+Shrine+to+Nyx"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Cradle"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Gaea%27s+Cradle"></a></td></tr></tbody></table>

  

For most of development, [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) was not legendary. There was still a little bit of tension in the card—only tapping for colorless initially hurts when you want to cast [Boros Reckoner](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner) or [Nightveil Specter](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightveil+Specter) with [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) and two other lands. However, it was an auto include in many of our decks in spite of this. The legendary supertype was added, and all of the developers found ourselves wondering how many to add to our decks. 

I am extremely happy with how [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) has played thus far. It is an exciting card, and one that is capable of fueling some truly exciting plays. It is great to make exciting cards that don't overshadow the excitement for other cards. I think that we put enough balances on the card to keep [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) from being excessively powerful. Much like our internal playtesting, deck builders all over the world have struggled with how many copies of [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx) to put into their devotion decks. I've seen any number from zero to four do well at tournaments, and I think this is a great thing. 

The Gods and Their Weapons

The *Theros* Gods are all designed with a similar goal: they require five devotion to turn into creatures, and they have an effect that isn't really worth it unless you have the necessary devotion. For example, [Think Tank](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Think+Tank) isn't exactly the most impressive card, so much of the power in [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea) is the potential to turn her into an oversized creature. 

One of my favorite things about *Theros* is how each God has a weapon that plays well with it. First, each weapon provides two devotion. Counting the God itself as a third devotion symbol, you only need two more of the appropriate color devotion to turn your god into a fearsome creature. The part that I really enjoy is that the weapon's ability plays well with the god's ability. Take a look! 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heliod%2C+God+of+the+Sun"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Heliod%2C+God+of+the+Sun"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spear+of+Heliod"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Spear+of+Heliod"></a></td></tr></tbody></table>

  

Heliod makes tokens, while the [Spear of Heliod](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spear+of+Heliod) is there to give them all a boost. At one point, Heliod had a cheaper activation and made 1/1s. This conflicted with our goals to make the power in turning the God into a creature, so we changed the card into the ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif): 2/1 token you see today. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Thassa%2C+God+of+the+Sea"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bident+of+Thassa"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Bident+of+Thassa"></a></td></tr></tbody></table>

  

Thassa's Bident gives you a reward for each of your creatures that get through for damage. What better ability to pair with the "[Thieving Magpie](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thieving+Magpie)" ability than unblockability?! 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Erebos%2C+God+of+the+Dead"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Erebos%2C+God+of+the+Dead"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whip+of+Erebos"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Whip+of+Erebos"></a></td></tr></tbody></table>

  

The whip gives all of your creatures lifelink, which boosts your life total. This allows you to be more aggressive when it comes to drawing cards with Erebos's ability. One of my favorite things about Erebos is that he turns off the lifelink from an opposing [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whip+of+Erebos). Erebos doesn't like his weapons being used against him. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Purphoros%2C+God+of+the+Forge"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Purphoros%2C+God+of+the+Forge"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hammer+of+Purphoros"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Hammer+of+Purphoros"></a></td></tr></tbody></table>

  

Much like [Heliod, God of the Sun](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heliod%2C+God+of+the+Sun) and [Spear of Heliod](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spear+of+Heliod), the red combo provides a benefit for your creatures and a way to make extra creatures. However, this time the weapon makes the creatures while the God makes them stronger. I think it is interesting that both colors care about making lots of creatures, but each does it in its own way. Red sacrifices things (in this case, lands) and deals direct damage, while white is all about building up an overwhelming army of creatures. 

<table><tbody><tr><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nylea%2C+God+of+the+Hunt"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Nylea%2C+God+of+the+Hunt"></a></td><td><a href="https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bow+of+Nylea"><img alt="" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Bow+of+Nylea"></a></td></tr></tbody></table>

  

This is easily my favorite pair. I love that both of them individually help your creatures, which is something very green. Their combination is the most subtle, and one that is difficult to appreciate until you play with it. The combination of deathtouch and trample is very powerful—likely my favorite keyword interaction. If your opponent blocks your 5/5 with a single creatures, he or she will take 4 trample damage because 1 damage is lethal damage with deathtouch.

Types of Devotion Decks

One of the most interesting things about Devotion is that it doesn't point you in a direction of how fast your deck wants to be. The only thing it really demands is that your deck has permanents. A faster devotion deck can flood the board with creatures and attempt to overwhelm an opponent. A slower devotion deck can use its permanents to slow down a game and take control. As the game goes longer, there are more likely to be more permanents in play, thus making the devotion card stronger.

[Pro Tour *Theros*](https://web.archive.org/web/20131205000000/http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/ptths13/welcome) was a perfect example of all of the various types of devotion decks. Devotion decks did incredibly well, and each of them had its own unique style. 

Jérémy Dezani

#### Jérémy Dezani's Mono-Blue Devotion

##### 

[![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en/decklist/deck-list-7d4a5fd44f5523502e80b33cd4b20fb7.txt?n=J%C3%A9r%C3%A9my%20Dezani%27s%20Mono-Blue%20Devotion)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (2)

2 [Jace, Architect of Thought](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Jace,]+[Architect]+[of]+[Thought]) 

##### Creature (30)

4 [Cloudfin Raptor](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cloudfin]+[Raptor]) 4 [Frostburn Weird](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Frostburn]+[Weird]) 4 [Judge's Familiar](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Judge]+[Familiar]) 4 [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Master]+[of]+[Waves]) 4 [Nightveil Specter](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nightveil]+[Specter]) 2 [Omenspeaker](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Omenspeaker]) 4 [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thassa,]+[God]+[of]+[the]+[Sea]) 4 [Tidebinder Mage](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Tidebinder]+[Mage]) 

##### Instant (3)

2 [Cyclonic Rift](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cyclonic]+[Rift]) 1 [Disperse](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Disperse]) 

##### Artifact (1)

1 [Bident of Thassa](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Bident]+[of]+[Thassa]) 

##### Land (24)

21 [Island](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Island]) 3 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 

60 Cards 

##### Sideboard (15)

1 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 2 [Jace, Architect of Thought](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Jace,]+[Architect]+[of]+[Thought]) 2 [Ætherling](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[%C3%86therling]) 3 [Negate](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Negate]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 2 [Ratchet Bomb](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Ratchet]+[Bomb]) 1 [Triton Tactics](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Triton]+[Tactics]) 3 [Wall of Frost](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wall]+[of]+[Frost]) 

##### Blue (35)

4 [Cloudfin Raptor](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cloudfin]+[Raptor]) 4 [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Master]+[of]+[Waves]) 2 [Omenspeaker](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Omenspeaker]) 4 [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thassa,]+[God]+[of]+[the]+[Sea]) 4 [Tidebinder Mage](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Tidebinder]+[Mage]) 1 [Bident of Thassa](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Bident]+[of]+[Thassa]) 2 [Cyclonic Rift](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cyclonic]+[Rift]) 1 [Disperse](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Disperse]) 4 [Jace, Architect of Thought](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Jace,]+[Architect]+[of]+[Thought]) 2 [Ætherling](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[%C3%86therling]) 3 [Negate](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Negate]) 1 [Triton Tactics](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Triton]+[Tactics]) 3 [Wall of Frost](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wall]+[of]+[Frost]) 

##### Multi colored (12)

4 [Frostburn Weird](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Frostburn]+[Weird]) 4 [Judge's Familiar](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Judge]+[Familiar]) 4 [Nightveil Specter](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nightveil]+[Specter]) 

##### Colorless (28)

21 [Island](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Island]) 4 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 2 [Ratchet Bomb](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Ratchet]+[Bomb]) 

75 Cards 

##### 1 (10)

4 [Cloudfin Raptor](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cloudfin]+[Raptor]) 4 [Judge's Familiar](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Judge]+[Familiar]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 1 [Triton Tactics](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Triton]+[Tactics]) 

##### 2 (18)

4 [Frostburn Weird](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Frostburn]+[Weird]) 2 [Omenspeaker](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Omenspeaker]) 4 [Tidebinder Mage](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Tidebinder]+[Mage]) 2 [Cyclonic Rift](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cyclonic]+[Rift]) 1 [Disperse](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Disperse]) 3 [Negate](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Negate]) 2 [Ratchet Bomb](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Ratchet]+[Bomb]) 

##### 3 (11)

4 [Nightveil Specter](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nightveil]+[Specter]) 4 [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thassa,]+[God]+[of]+[the]+[Sea]) 3 [Wall of Frost](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wall]+[of]+[Frost]) 

##### 4 (9)

4 [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Master]+[of]+[Waves]) 1 [Bident of Thassa](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Bident]+[of]+[Thassa]) 4 [Jace, Architect of Thought](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Jace,]+[Architect]+[of]+[Thought]) 

##### 6 (2)

2 [Ætherling](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[%C3%86therling]) 

50 Cards 

##### Common (35)

21 [Island](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Island]) 4 [Cloudfin Raptor](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cloudfin]+[Raptor]) 4 [Frostburn Weird](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Frostburn]+[Weird]) 2 [Omenspeaker](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Omenspeaker]) 1 [Disperse](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Disperse]) 3 [Negate](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Negate]) 

##### Uncommon (8)

4 [Judge's Familiar](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Judge]+[Familiar]) 1 [Triton Tactics](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Triton]+[Tactics]) 3 [Wall of Frost](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wall]+[of]+[Frost]) 

##### Rare (20)

4 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 4 [Nightveil Specter](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nightveil]+[Specter]) 4 [Tidebinder Mage](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Tidebinder]+[Mage]) 1 [Bident of Thassa](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Bident]+[of]+[Thassa]) 2 [Cyclonic Rift](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Cyclonic]+[Rift]) 2 [Ætherling](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[%C3%86therling]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 2 [Ratchet Bomb](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Ratchet]+[Bomb]) 

##### Mythic (12)

4 [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Master]+[of]+[Waves]) 4 [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thassa,]+[God]+[of]+[the]+[Sea]) 4 [Jace, Architect of Thought](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Jace,]+[Architect]+[of]+[Thought]) 

75 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island) 

[Deal Another Hand](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tidebinder+Mage)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thassa%2C+God+of+the+Sea)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thassa%2C+God+of+the+Sea)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bident+of+Thassa)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cloudfin+Raptor)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nightveil+Specter)

  

Jérémy Dezani's deck is devoted to blue and [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea). With eight one-drops, Dezani won the Pro Tour with the most aggressive of the devotion decks. Attempting to quickly overwhelm opponents with a quick [Thassa, God of the Sea](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+God+of+the+Sea) or a [Master of Waves](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves), Dezani used devotion to get 5/5 indestructible creatures for three mana and 10 (or more) power's worth of creatures for four mana. Who said blue is always a control color? 

  

Kentarou Yamamoto

#### Kentarou Yamamoto's Mono-Black Devotion

##### 

[![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en/decklist/deck-list-b2c860695828287019a4113eef2a575e.txt?n=Kentarou%20Yamamoto%27s%20Mono-Black%20Devotion)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (15)

4 [Desecration Demon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Desecration]+[Demon]) 1 [Erebos, God of the Dead](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Erebos,]+[God]+[of]+[the]+[Dead]) 4 [Gray Merchant of Asphodel](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Gray]+[Merchant]+[of]+[Asphodel]) 4 [Lifebane Zombie](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Lifebane]+[Zombie]) 2 [Pack Rat](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pack]+[Rat]) 

##### Sorcery (4)

4 [Thoughtseize](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thoughtseize]) 

##### Instant (10)

2 [Devour Flesh](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Devour]+[Flesh]) 4 [Doom Blade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Doom]+[Blade]) 4 [Hero's Downfall](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Hero]+[Downfall]) 

##### Artifact (2)

2 [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Whip]+[of]+[Erebos]) 

##### Enchantment (4)

4 [Underworld Connections](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Underworld]+[Connections]) 

##### Land (25)

4 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 1 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 16 [Swamp](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Swamp]) 4 [Temple of Silence](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Silence]) 

60 Cards 

##### Sideboard (15)

1 [Erebos, God of the Dead](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Erebos,]+[God]+[of]+[the]+[Dead]) 1 [Devour Flesh](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Devour]+[Flesh]) 4 [Duress](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Duress]) 4 [Pharika's Cure](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pharika]+[Cure]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 4 [Xathrid Necromancer](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xathrid]+[Necromancer]) 

##### Black (49)

4 [Desecration Demon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Desecration]+[Demon]) 2 [Erebos, God of the Dead](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Erebos,]+[God]+[of]+[the]+[Dead]) 4 [Gray Merchant of Asphodel](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Gray]+[Merchant]+[of]+[Asphodel]) 4 [Lifebane Zombie](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Lifebane]+[Zombie]) 2 [Pack Rat](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pack]+[Rat]) 3 [Devour Flesh](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Devour]+[Flesh]) 4 [Doom Blade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Doom]+[Blade]) 4 [Hero's Downfall](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Hero]+[Downfall]) 4 [Thoughtseize](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thoughtseize]) 4 [Underworld Connections](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Underworld]+[Connections]) 2 [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Whip]+[of]+[Erebos]) 4 [Duress](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Duress]) 4 [Pharika's Cure](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pharika]+[Cure]) 4 [Xathrid Necromancer](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xathrid]+[Necromancer]) 

##### Colorless (26)

4 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 1 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 16 [Swamp](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Swamp]) 4 [Temple of Silence](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Silence]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 

75 Cards 

##### 1 (9)

4 [Thoughtseize](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thoughtseize]) 4 [Duress](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Duress]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 

##### 2 (13)

2 [Pack Rat](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pack]+[Rat]) 3 [Devour Flesh](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Devour]+[Flesh]) 4 [Doom Blade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Doom]+[Blade]) 4 [Pharika's Cure](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pharika]+[Cure]) 

##### 3 (16)

4 [Lifebane Zombie](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Lifebane]+[Zombie]) 4 [Hero's Downfall](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Hero]+[Downfall]) 4 [Underworld Connections](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Underworld]+[Connections]) 4 [Xathrid Necromancer](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xathrid]+[Necromancer]) 

##### 4 (8)

4 [Desecration Demon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Desecration]+[Demon]) 2 [Erebos, God of the Dead](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Erebos,]+[God]+[of]+[the]+[Dead]) 2 [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Whip]+[of]+[Erebos]) 

##### 5 (4)

4 [Gray Merchant of Asphodel](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Gray]+[Merchant]+[of]+[Asphodel]) 

50 Cards 

##### Common (31)

16 [Swamp](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Swamp]) 4 [Gray Merchant of Asphodel](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Gray]+[Merchant]+[of]+[Asphodel]) 3 [Devour Flesh](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Devour]+[Flesh]) 4 [Duress](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Duress]) 4 [Pharika's Cure](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pharika]+[Cure]) 

##### Uncommon (4)

4 [Doom Blade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Doom]+[Blade]) 

##### Rare (38)

4 [Mutavault](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mutavault]) 1 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 4 [Temple of Silence](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Silence]) 4 [Desecration Demon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Desecration]+[Demon]) 4 [Lifebane Zombie](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Lifebane]+[Zombie]) 2 [Pack Rat](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pack]+[Rat]) 4 [Hero's Downfall](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Hero]+[Downfall]) 4 [Thoughtseize](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Thoughtseize]) 4 [Underworld Connections](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Underworld]+[Connections]) 2 [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Whip]+[of]+[Erebos]) 1 [Pithing Needle](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Pithing]+[Needle]) 4 [Xathrid Necromancer](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xathrid]+[Necromancer]) 

##### Mythic (2)

2 [Erebos, God of the Dead](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Erebos,]+[God]+[of]+[the]+[Dead]) 

75 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mutavault) 

[Deal Another Hand](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mutavault)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Devour+Flesh)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desecration+Demon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desecration+Demon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Doom+Blade)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

  

On the other end of the spectrum, Kentarou Yamamoto's mono-black deck was the most controlling of the devotion decks. Using permanents such as [Underworld Connections](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Connections) and [Whip of Erebos](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whip+of+Erebos), Yamamoto's permanents were more reliable in providing devotion. This allowed Yamamoto to play many removal spells without fearing for his devotion count. 

  

Makihito Mihara

#### Makihito Mihara's Colossal Gruul

##### 

[![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en/decklist/deck-list-b689526b44adea76f95c839c5d9ca3fd.txt?n=Makihito%20Mihara%27s%20Colossal%20Gruul)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (9)

3 [Domri Rade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Domri]+[Rade]) 4 [Garruk, Caller of Beasts](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Garruk,]+[Caller]+[of]+[Beasts]) 2 [Xenagos, the Reveler](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xenagos,]+[the]+[Reveler]) 

##### Creature (28)

3 [Arbor Colossus](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Arbor]+[Colossus]) 4 [Burning-Tree Emissary](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning-Tree]+[Emissary]) 4 [Elvish Mystic](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Elvish]+[Mystic]) 2 [Nylea, God of the Hunt](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea,]+[God]+[of]+[the]+[Hunt]) 4 [Polukranos, World Eater](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Polukranos,]+[World]+[Eater]) 3 [Scavenging Ooze](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Scavenging]+[Ooze]) 4 [Sylvan Caryatid](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Caryatid]) 4 [Voyaging Satyr](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Voyaging]+[Satyr]) 

##### Land (23)

9 [Forest](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Forest]) 2 [Mountain](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mountain]) 4 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 4 [Stomping Ground](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Stomping]+[Ground]) 4 [Temple of Abandon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Abandon]) 

60 Cards 

##### Sideboard (15)

1 [Xenagos, the Reveler](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xenagos,]+[the]+[Reveler]) 2 [Burning Earth](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning]+[Earth]) 2 [Chandra, Pyromaster](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Chandra,]+[Pyromaster]) 1 [Destructive Revelry](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Destructive]+[Revelry]) 1 [Mistcutter Hydra](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mistcutter]+[Hydra]) 3 [Mizzium Mortars](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mizzium]+[Mortars]) 2 [Nylea's Disciple](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea]+[Disciple]) 1 [Sylvan Primordial](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Primordial]) 2 [Wasteland Viper](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wasteland]+[Viper]) 

##### Red (7)

2 [Burning Earth](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning]+[Earth]) 2 [Chandra, Pyromaster](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Chandra,]+[Pyromaster]) 3 [Mizzium Mortars](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mizzium]+[Mortars]) 

##### Green (34)

3 [Arbor Colossus](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Arbor]+[Colossus]) 4 [Elvish Mystic](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Elvish]+[Mystic]) 2 [Nylea, God of the Hunt](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea,]+[God]+[of]+[the]+[Hunt]) 4 [Polukranos, World Eater](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Polukranos,]+[World]+[Eater]) 3 [Scavenging Ooze](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Scavenging]+[Ooze]) 4 [Sylvan Caryatid](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Caryatid]) 4 [Voyaging Satyr](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Voyaging]+[Satyr]) 4 [Garruk, Caller of Beasts](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Garruk,]+[Caller]+[of]+[Beasts]) 1 [Mistcutter Hydra](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mistcutter]+[Hydra]) 2 [Nylea's Disciple](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea]+[Disciple]) 1 [Sylvan Primordial](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Primordial]) 2 [Wasteland Viper](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wasteland]+[Viper]) 

##### Multi colored (11)

4 [Burning-Tree Emissary](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning-Tree]+[Emissary]) 3 [Domri Rade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Domri]+[Rade]) 3 [Xenagos, the Reveler](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xenagos,]+[the]+[Reveler]) 1 [Destructive Revelry](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Destructive]+[Revelry]) 

##### Colorless (23)

9 [Forest](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Forest]) 2 [Mountain](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mountain]) 4 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 4 [Stomping Ground](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Stomping]+[Ground]) 4 [Temple of Abandon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Abandon]) 

75 Cards 

##### 1 (7)

4 [Elvish Mystic](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Elvish]+[Mystic]) 1 [Mistcutter Hydra](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mistcutter]+[Hydra]) 2 [Wasteland Viper](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wasteland]+[Viper]) 

##### 2 (19)

4 [Burning-Tree Emissary](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning-Tree]+[Emissary]) 3 [Scavenging Ooze](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Scavenging]+[Ooze]) 4 [Sylvan Caryatid](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Caryatid]) 4 [Voyaging Satyr](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Voyaging]+[Satyr]) 1 [Destructive Revelry](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Destructive]+[Revelry]) 3 [Mizzium Mortars](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mizzium]+[Mortars]) 

##### 3 (3)

3 [Domri Rade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Domri]+[Rade]) 

##### 4 (15)

2 [Nylea, God of the Hunt](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea,]+[God]+[of]+[the]+[Hunt]) 4 [Polukranos, World Eater](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Polukranos,]+[World]+[Eater]) 3 [Xenagos, the Reveler](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xenagos,]+[the]+[Reveler]) 2 [Burning Earth](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning]+[Earth]) 2 [Chandra, Pyromaster](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Chandra,]+[Pyromaster]) 2 [Nylea's Disciple](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea]+[Disciple]) 

##### 5 (3)

3 [Arbor Colossus](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Arbor]+[Colossus]) 

##### 6 (4)

4 [Garruk, Caller of Beasts](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Garruk,]+[Caller]+[of]+[Beasts]) 

##### 7 (1)

1 [Sylvan Primordial](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Primordial]) 

52 Cards 

##### Common (21)

9 [Forest](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Forest]) 2 [Mountain](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mountain]) 4 [Elvish Mystic](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Elvish]+[Mystic]) 4 [Voyaging Satyr](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Voyaging]+[Satyr]) 2 [Nylea's Disciple](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea]+[Disciple]) 

##### Uncommon (7)

4 [Burning-Tree Emissary](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning-Tree]+[Emissary]) 1 [Destructive Revelry](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Destructive]+[Revelry]) 2 [Wasteland Viper](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Wasteland]+[Viper]) 

##### Rare (29)

4 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nykthos,]+[Shrine]+[to]+[Nyx]) 4 [Stomping Ground](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Stomping]+[Ground]) 4 [Temple of Abandon](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Temple]+[of]+[Abandon]) 3 [Arbor Colossus](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Arbor]+[Colossus]) 3 [Scavenging Ooze](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Scavenging]+[Ooze]) 4 [Sylvan Caryatid](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Caryatid]) 2 [Burning Earth](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Burning]+[Earth]) 1 [Mistcutter Hydra](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mistcutter]+[Hydra]) 3 [Mizzium Mortars](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Mizzium]+[Mortars]) 1 [Sylvan Primordial](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Sylvan]+[Primordial]) 

##### Mythic (18)

2 [Nylea, God of the Hunt](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Nylea,]+[God]+[of]+[the]+[Hunt]) 4 [Polukranos, World Eater](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Polukranos,]+[World]+[Eater]) 3 [Domri Rade](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Domri]+[Rade]) 4 [Garruk, Caller of Beasts](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Garruk,]+[Caller]+[of]+[Beasts]) 3 [Xenagos, the Reveler](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Xenagos,]+[the]+[Reveler]) 2 [Chandra, Pyromaster](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[Chandra,]+[Pyromaster]) 

75 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest) 

[Deal Another Hand](https://web.archive.org/web/20131205000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Abandon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Polukranos%2C+World+Eater)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Abandon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stomping+Ground)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Polukranos%2C+World+Eater)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Burning-Tree+Emissary)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elvish+Mystic)

  

[In his deck tech](https://web.archive.org/web/20131205000000/http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/ptths13/video8), Makihito Mihara made it clear he was playing a combo deck. With 4 [Voyaging Satyr](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voyaging+Satyr) and 4 [Nykthos, Shrine to Nyx](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nykthos%2C+Shrine+to+Nyx), Mihara was looking to generate a large amount of mana. [Garruk, Caller of Beasts](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Caller+of+Beasts); [Arbor Colossus](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arbor+Colossus); and [Polukranos, World Eater](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polukranos%2C+World+Eater) are great things to spend that mana on. 

  

* * *

  

Standard is shaping up to be a great format, with devotion being an important part of many different decks. It's also important that devotion isn't the only thing that you can do. We like making lots of exciting new things, but we work to make sure that any given thing isn't so powerful that nothing else is worth doing. Given the success of Esper Control, white beatdown and other non-devotion decks, there are plenty of options in Standard.

Thanks for joining me this week,

Adam Prosak

  
  

![](http://archive.wizards.com/mtg/images/widgets/storelocator/SmallStoreLocator_Background_Left.png)

![](http://archive.wizards.com/mtg/images/widgets/storelocator/EN_SmallStoreLocatorGOText.png)

[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Details_Static.png)](https://web.archive.org/web/20131205000000/https://archive.wizards.com/Magic/Magazine/Article.aspx?x=events/magic/fnm)[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Info_Static.png)](https://web.archive.org/web/20131205000000/http://archive.wizards.com/Magic/tcg/products.aspx?x=mtg/tcg/products/theros)[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_CIG_Static.png)](https://web.archive.org/web/20131205000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?set=[%20Theros%20])

  
  

  
![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg)![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

![Adam Prosak](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_adamprosak.jpg)**Adam Prosak**  
[@Adam\_Prosak](https://twitter.com/adam_prosak)  
[Email Adam](https://web.archive.org/web/20131205000000/http://magic.wizards.com/company/emailtoauthor.asp?author=Adam%20Prosak%1Aamp;amp;headline=[Developing%20Devotion] "Click to send email to the author.")[Author Archive](https://web.archive.org/web/20131205000000/http://magic.wizards.com/Magic/Magazine/Archive.aspx?author=Adam%20Prosak)  
[Uncharted Realms Archive](https://web.archive.org/web/20131205000000/http://magic.wizards.com/Magic/Magazine/Archive.aspx?tag=Uncharted%20Realms%1Aamp;description=Uncharted%20Realms)  

From Friday Night **Magic** to the Pro Tour, Adam Prosak loves all types of tournament **Magic**. Currently, Adam is working in Ramp;D as a development intern.