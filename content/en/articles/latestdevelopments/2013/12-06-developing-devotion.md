---
id: f5sp5rj0
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/12-06-developing-devotion
title: Developing Devotion
published: '2013-12-06'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: adam-prosak-76cf4169
  name: Adam Prosak
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/276
    lang_detected: en
    capture_id: 620682
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
    captured_at: '2014-03-31 07:59:00+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/276
    lang_detected: en
    capture_id: 620682
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
    captured_at: '2014-03-31 07:59:00+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/276
    lang_detected: en
    capture_id: 620682
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
    captured_at: '2014-03-31 07:59:00+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/276
    lang_detected: en
    capture_id: 620682
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
    captured_at: '2014-03-31 07:59:00+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
  duplicate_sources:
  - qvh7xrse
sources:
- document_id: f5sp5rj0
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/276
  lang: en
  template: aspx
  captured_at: '2014-03-31 07:59:00+00'
  capture_id: 620682
  wayback_url: https://web.archive.org/web/20140331075900id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
- document_id: qvh7xrse
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06
  lang: en
  template: drupal
  captured_at: '2021-09-19 16:49:25+00'
  capture_id: 720751
  wayback_url: https://web.archive.org/web/20210919164925id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-06
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: f5sp5rj0
  capture_id: 620682
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
  wayback_url: https://web.archive.org/web/20140331075900id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/276
  captured_at: '2014-03-31 07:59:00+00'
  template: aspx
  sha256: 09dcfa34d0c778cc68dd86e35f48d2d66583d8a8889d3aa4a9139235d855d851
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Fireball
  - Master of Waves
  - Fanatic of Mogis
  - Nykthos, Shrine to Nyx
  - Tolarian Academy
  - Gaea's Cradle
  - Cabal Coffers
  - Boros Reckoner
  - Nightveil Specter
  - Think Tank
  - Thassa, God of the Sea
  - Spear of Heliod
  - Thieving Magpie
  - Whip of Erebos
  - Heliod, God of the Sun
  - Island
  - Mutavault
  - Cloudfin Raptor
  - Frostburn Weird
  - Judge's Familiar
  - Omenspeaker
  - Tidebinder Mage
  - Bident of Thassa
  - Cyclonic Rift
  - Disperse
  - Jace, Architect of Thought
  - Ætherling
  - Negate
  - Pithing Needle
  - Ratchet Bomb
  - Triton Tactics
  - Wall of Frost
  - Swamp
  - Temple of Silence
  - Desecration Demon
  - Erebos, God of the Dead
  - Gray Merchant of Asphodel
  - Lifebane Zombie
  - Pack Rat
  - Devour Flesh
  - Doom Blade
  - Hero's Downfall
  - Thoughtseize
  - Underworld Connections
  - Duress
  - Pharika's Cure
  - Xathrid Necromancer
  - Forest
  - Mountain
  - Stomping Ground
  - Temple of Abandon
  - Arbor Colossus
  - Burning-Tree Emissary
  - Elvish Mystic
  - Nylea, God of the Hunt
  - Polukranos, World Eater
  - Scavenging Ooze
  - Sylvan Caryatid
  - Voyaging Satyr
  - Domri Rade
  - Garruk, Caller of Beasts
  - Xenagos, the Reveler
  - Burning Earth
  - Chandra, Pyromaster
  - Destructive Revelry
  - Mistcutter Hydra
  - Mizzium Mortars
  - Nylea's Disciple
  - Sylvan Primordial
  - Wasteland Viper
  occurrences: 123
---
Greetings Everyone!

My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make **Magic: The Gathering** the best game it can be. However, one of the things I've missed during my time here is writing. I harassed [Sam Stoddard](https://web.archive.org/web/20131211013038/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard) enough, and he agreed to loan me his digital space for a week. Thanks Sam! 

### The Devotion Mechanic

Devotion is a mechanic that scales endlessly. Nearly any X spell (such as Fireball) is a good example of a scaling spell. The amount of damage Fireball deals is only limited by the amount of mana you are willing to spend. Scaling cards are interesting because they allow you to play different-powered effect depending on the state of the game. Like other scaling cards, cards with devotion are similarly unlimited. Instead of available mana, a card with devotion counts the mana symbols on your permanents. Devotion is different than most scaling mechanics because many of your cards can count multiple times toward your scaling mechanic. A creature that costs ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif) counts for two devotion, so it is difficult to plan on a certain amount of devotion. This makes developing devotion cards very tricky, as we want cards to be fun in the most amount of situations possible. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Fireball" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Fireball&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Agent of the Fates" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Agent%20of%20the%20Fates&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Imagine for a second that Master of Waves made 1/1 Elemental tokens rather than 1/0 tokens. If you have a large amount of devotion, Master of Waves is incredibly difficult to beat. We decided to allow players to get around huge Master of Waves by simply killing the Master of Waves itself. Now, Master of Waves is incredible with some highly devoted friends, but only if your opponent can't remove it. That is more fun than your opponent simply sitting there helpless regardless of whether or not he or she can remove the Master of Waves. 

On the other side of things, it is also important to make sure that cards with devotion are reasonable plays even if you don't have much (or any) devotion when you play them. Fanatic of Mogis is capable of dealing a large amount of damage, but only if you have heavy devotion. If you don't have that much devotion, playing a 4/2 for ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif) isn't the worst thing in the world. We tried to make cards that were appealing enough to play even without optimal devotion. Sitting with a card in your hand all game because you can't get devotion going doesn't provide great game play, so we work to avoid those things. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Master of Waves" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Master%20of%20Waves&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Fanatic of Mogis" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Fanatic%20of%20Mogis&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### Making a Card Weaker?

When developing a card, generally we play around with a mana cost if we want to narrow the range of decks a particular card is played in. For example, if we find that a certain card that costs ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) is played in too many decks, we might change its casting cost to ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) to force it into more heavily green decks. 

However, with devotion, a ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) casting cost is often a benefit rather than a drawback compared to a card that costs ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif). In a world of devotion, we have to balance the casting costs on cards differently. Master of Waves itself had a mana cost of 2UU at one point. We actually weakened the card by making it easier to cast. 

### Nykthos, Shrine to Nyx

As *Theros* was released, one of development's biggest concerns about the cards concerned Nykthos, Shrine to Nyx. It has been quite some time since we've printed a land capable of making more than one mana, let alone a land that is capable of making a scaling amount of mana. Tolarian Academy, Gaea's Cradle, and Cabal Coffers are lands in a similar space to Nykthos, Shrine to Nyx—and those lands are among the most powerful cards ever printed and not something we would want to repeat. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Nykthos, Shrine to Nyx" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Nykthos,%20Shrine%20to%20Nyx&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Gaea's Cradle" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Gaea%27s%20Cradle&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

For most of development, Nykthos, Shrine to Nyx was not legendary. There was still a little bit of tension in the card—only tapping for colorless initially hurts when you want to cast Boros Reckoner or Nightveil Specter with Nykthos, Shrine to Nyx and two other lands. However, it was an auto include in many of our decks in spite of this. The legendary supertype was added, and all of the developers found ourselves wondering how many to add to our decks. 

I am extremely happy with how Nykthos, Shrine to Nyx has played thus far. It is an exciting card, and one that is capable of fueling some truly exciting plays. It is great to make exciting cards that don't overshadow the excitement for other cards. I think that we put enough balances on the card to keep Nykthos, Shrine to Nyx from being excessively powerful. Much like our internal playtesting, deck builders all over the world have struggled with how many copies of Nykthos, Shrine to Nyx to put into their devotion decks. I've seen any number from zero to four do well at tournaments, and I think this is a great thing. 

### The Gods and Their Weapons

The *Theros* Gods are all designed with a similar goal: they require five devotion to turn into creatures, and they have an effect that isn't really worth it unless you have the necessary devotion. For example, Think Tank isn't exactly the most impressive card, so much of the power in Thassa, God of the Sea is the potential to turn her into an oversized creature. 

One of my favorite things about *Theros* is how each God has a weapon that plays well with it. First, each weapon provides two devotion. Counting the God itself as a third devotion symbol, you only need two more of the appropriate color devotion to turn your god into a fearsome creature. The part that I really enjoy is that the weapon's ability plays well with the god's ability. Take a look! 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Heliod, God of the Sun" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Heliod,%20God%20of%20the%20Sun&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Spear of Heliod" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Spear%20of%20Heliod&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Heliod makes tokens, while the Spear of Heliod is there to give them all a boost. At one point, Heliod had a cheaper activation and made 1/1s. This conflicted with our goals to make the power in turning the God into a creature, so we changed the card into the ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif): 2/1 token you see today. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Thassa, God of the Sea" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Thassa,%20God%20of%20the%20Sea&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Bident of Thassa" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Bident%20of%20Thassa&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Thassa's Bident gives you a reward for each of your creatures that get through for damage. What better ability to pair with the "Thieving Magpie" ability than unblockability?! 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Erebos, God of the Dead" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Erebos,%20God%20of%20the%20Dead&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Whip of Erebos" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Whip%20of%20Erebos&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

The whip gives all of your creatures lifelink, which boosts your life total. This allows you to be more aggressive when it comes to drawing cards with Erebos's ability. One of my favorite things about Erebos is that he turns off the lifelink from an opposing Whip of Erebos. Erebos doesn't like his weapons being used against him. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Purphoros, God of the Forge" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Purphoros,%20God%20of%20the%20Forge&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hammer of Purphoros" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hammer%20of%20Purphoros&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Much like Heliod, God of the Sun and Spear of Heliod, the red combo provides a benefit for your creatures and a way to make extra creatures. However, this time the weapon makes the creatures while the God makes them stronger. I think it is interesting that both colors care about making lots of creatures, but each does it in its own way. Red sacrifices things (in this case, lands) and deals direct damage, while white is all about building up an overwhelming army of creatures. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Nylea, God of the Hunt" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Nylea,%20God%20of%20the%20Hunt&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Bow of Nylea" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Bow%20of%20Nylea&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

This is easily my favorite pair. I love that both of them individually help your creatures, which is something very green. Their combination is the most subtle, and one that is difficult to appreciate until you play with it. The combination of deathtouch and trample is very powerful—likely my favorite keyword interaction. If your opponent blocks your 5/5 with a single creatures, he or she will take 4 trample damage because 1 damage is lethal damage with deathtouch.

### Types of Devotion Decks

One of the most interesting things about Devotion is that it doesn't point you in a direction of how fast your deck wants to be. The only thing it really demands is that your deck has permanents. A faster devotion deck can flood the board with creatures and attempt to overwhelm an opponent. A slower devotion deck can use its permanents to slow down a game and take control. As the game goes longer, there are more likely to be more permanents in play, thus making the devotion card stronger.

[Pro Tour *Theros*](/en/events/2013/ptths13/dezani-proclaims-allez-les-bleus-at-pro-tour) was a perfect example of all of the various types of devotion decks. Devotion decks did incredibly well, and each of them had its own unique style. 

### Jérémy Dezani

Jérémy Dezani's Mono-Blue Devotion 

Standard – Winner, Pro Tour Theros

[![View a sample hand of this deck](https://i.ormos.uk/b4/b1/b4b1cd4db83413dd60cb392a5774d1cb699cdbad1c855057956f91e70ab413bc.png)](https://web.archive.org/web/20131211030420/http://www.wizards.com/magic/samplehand.asp?x=mtg/daily/ld/276&decknum=1) 

[![Download a .dek file for use in Magic Online](https://i.ormos.uk/7d/67/7d67a37edff07800cb466fa53a1880fe4f5a9f5af21d4a85210e22956ee20ec0.png)](https://web.archive.org/web/20131206000000/http://www.wizards.com/magic/mtgdailyld276x1.dek?x=mtg/daily/ld/276&decknum=1) 

  
 

<table>&#10;          <tbody><tr>&#10;            <td colspan="2">&#10;              <p>Main Deck</p>&#10;              <p>60 cards&#10;									</p>&#10;            </td>&#10;            <td>&#10;          </td></tr>&#10;          <tr>&#10;            <td>21 &#10;&#10;		<a>Island</a><br>3 &#10;&#10;		<a>Mutavault</a><br><hr>24 lands<br><br>4 &#10;&#10;		<a>Cloudfin Raptor</a><br>4 &#10;&#10;		<a>Frostburn Weird</a><br>4 &#10;&#10;		<a>Judge's Familiar</a><br>4 &#10;&#10;		<a>Master of Waves</a><br>4 &#10;&#10;		<a>Nightveil Specter</a><br>2 &#10;&#10;		<a>Omenspeaker</a><br>4 &#10;&#10;		<a>Thassa, God of the Sea</a><br>4 &#10;&#10;		<a>Tidebinder Mage</a><br><hr>30 creatures<br><br></td>&#10;            <td>1 &#10;&#10;		<a>Bident of Thassa</a><br>2 &#10;&#10;		<a>Cyclonic Rift</a><br>1 &#10;&#10;		<a>Disperse</a><br><hr>4 other spells<br><br>2 &#10;&#10;		<a>Jace, Architect of Thought</a><br><hr>2 planeswalkers<br><br><div><b><i>Sideboard</i></b></div>2 &#10;&#10;		<a>Ætherling</a><br>2 &#10;&#10;		<a>Jace, Architect of Thought</a><br>1 &#10;&#10;		<a>Mutavault</a><br>3 &#10;&#10;		<a>Negate</a><br>1 &#10;&#10;		<a>Pithing Needle</a><br>2 &#10;&#10;		<a>Ratchet Bomb</a><br>1 &#10;&#10;		<a>Triton Tactics</a><br>3 &#10;&#10;		<a>Wall of Frost</a><br><hr>15 sideboard cards<br><br></td>&#10;            <td>&#10;              <div>&#10;                &#10;              </div>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>

![](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&multiverseid=10100000&type=card) 

  
 

  

Jérémy Dezani's deck is devoted to blue and Thassa, God of the Sea. With eight one-drops, Dezani won the Pro Tour with the most aggressive of the devotion decks. Attempting to quickly overwhelm opponents with a quick Thassa, God of the Sea or a Master of Waves, Dezani used devotion to get 5/5 indestructible creatures for three mana and 10 (or more) power's worth of creatures for four mana. Who said blue is always a control color? 

  

### Kentarou Yamamoto

Kentarou Yamamoto's Mono-Black Devotion 

Standard – Top 8, Pro Tour Theros

[![View a sample hand of this deck](https://i.ormos.uk/b4/b1/b4b1cd4db83413dd60cb392a5774d1cb699cdbad1c855057956f91e70ab413bc.png)](https://web.archive.org/web/20131211030425/http://www.wizards.com/magic/samplehand.asp?x=mtg/daily/ld/276&decknum=2) 

[![Download a .dek file for use in Magic Online](https://i.ormos.uk/7d/67/7d67a37edff07800cb466fa53a1880fe4f5a9f5af21d4a85210e22956ee20ec0.png)](https://web.archive.org/web/20131206000000/http://www.wizards.com/magic/mtgdailyld276x2.dek?x=mtg/daily/ld/276&decknum=2) 

  
 

<table>&#10;          <tbody><tr>&#10;            <td colspan="2">&#10;              <p>Main Deck</p>&#10;              <p>60 cards&#10;									</p>&#10;            </td>&#10;            <td>&#10;          </td></tr>&#10;          <tr>&#10;            <td>4 &#10;&#10;		<a>Mutavault</a><br>1 &#10;&#10;		<a>Nykthos, Shrine to Nyx</a><br>16 &#10;&#10;		<a>Swamp</a><br>4 &#10;&#10;		<a>Temple of Silence</a><br><hr>25 lands<br><br>4 &#10;&#10;		<a>Desecration Demon</a><br>1 &#10;&#10;		<a>Erebos, God of the Dead</a><br>4 &#10;&#10;		<a>Gray Merchant of Asphodel</a><br>4 &#10;&#10;		<a>Lifebane Zombie</a><br>2 &#10;&#10;		<a>Pack Rat</a><br><hr>15 creatures<br><br></td>&#10;            <td>2 &#10;&#10;		<a>Devour Flesh</a><br>4 &#10;&#10;		<a>Doom Blade</a><br>4 &#10;&#10;		<a>Hero's Downfall</a><br>4 &#10;&#10;		<a>Thoughtseize</a><br>4 &#10;&#10;		<a>Underworld Connections</a><br>2 &#10;&#10;		<a>Whip of Erebos</a><br><hr>20 other spells<br><br><div><b><i>Sideboard</i></b></div>1 &#10;&#10;		<a>Devour Flesh</a><br>4 &#10;&#10;		<a>Duress</a><br>1 &#10;&#10;		<a>Erebos, God of the Dead</a><br>4 &#10;&#10;		<a>Pharika's Cure</a><br>1 &#10;&#10;		<a>Pithing Needle</a><br>4 &#10;&#10;		<a>Xathrid Necromancer</a><br><hr>15 sideboard cards<br><br></td>&#10;            <td>&#10;              <div>&#10;                &#10;              </div>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>

![](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&multiverseid=10100000&type=card) 

  
 

  

On the other end of the spectrum, Kentarou Yamamoto's mono-black deck was the most controlling of the devotion decks. Using permanents such as Underworld Connections and Whip of Erebos, Yamamoto's permanents were more reliable in providing devotion. This allowed Yamamoto to play many removal spells without fearing for his devotion count. 

  

### Makihito Mihara

Makihito Mihara's Colossal Gruul 

Standard – Top 8, Pro Tour Theros

[![View a sample hand of this deck](https://i.ormos.uk/b4/b1/b4b1cd4db83413dd60cb392a5774d1cb699cdbad1c855057956f91e70ab413bc.png)](https://web.archive.org/web/20131211030430/http://www.wizards.com/magic/samplehand.asp?x=mtg/daily/ld/276&decknum=3) 

[![Download a .dek file for use in Magic Online](https://i.ormos.uk/7d/67/7d67a37edff07800cb466fa53a1880fe4f5a9f5af21d4a85210e22956ee20ec0.png)](https://web.archive.org/web/20131206000000/http://www.wizards.com/magic/mtgdailyld276x3.dek?x=mtg/daily/ld/276&decknum=3) 

  
 

<table>&#10;          <tbody><tr>&#10;            <td colspan="2">&#10;              <p>Main Deck</p>&#10;              <p>60 cards&#10;									</p>&#10;            </td>&#10;            <td>&#10;          </td></tr>&#10;          <tr>&#10;            <td>9 &#10;&#10;		<a>Forest</a><br>2 &#10;&#10;		<a>Mountain</a><br>4 &#10;&#10;		<a>Nykthos, Shrine to Nyx</a><br>4 &#10;&#10;		<a>Stomping Ground</a><br>4 &#10;&#10;		<a>Temple of Abandon</a><br><hr>23 lands<br><br>3 &#10;&#10;		<a>Arbor Colossus</a><br>4 &#10;&#10;		<a>Burning-Tree Emissary</a><br>4 &#10;&#10;		<a>Elvish Mystic</a><br>2 &#10;&#10;		<a>Nylea, God of the Hunt</a><br>4 &#10;&#10;		<a>Polukranos, World Eater</a><br>3 &#10;&#10;		<a>Scavenging Ooze</a><br>4 &#10;&#10;		<a>Sylvan Caryatid</a><br>4 &#10;&#10;		<a>Voyaging Satyr</a><br><hr>28 creatures<br><br></td>&#10;            <td>3 &#10;&#10;		<a>Domri Rade</a><br>4 &#10;&#10;		<a>Garruk, Caller of Beasts</a><br>2 &#10;&#10;		<a>Xenagos, the Reveler</a><br><hr>9 planeswalkers<br><br><div><b><i>Sideboard</i></b></div>2 &#10;&#10;		<a>Burning Earth</a><br>2 &#10;&#10;		<a>Chandra, Pyromaster</a><br>1 &#10;&#10;		<a>Destructive Revelry</a><br>1 &#10;&#10;		<a>Mistcutter Hydra</a><br>3 &#10;&#10;		<a>Mizzium Mortars</a><br>2 &#10;&#10;		<a>Nylea's Disciple</a><br>1 &#10;&#10;		<a>Sylvan Primordial</a><br>2 &#10;&#10;		<a>Wasteland Viper</a><br>1 &#10;&#10;		<a>Xenagos, the Reveler</a><br><hr>15 sideboard cards<br><br></td>&#10;            <td>&#10;              <div>&#10;                &#10;              </div>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>

![](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&multiverseid=10100000&type=card) 

  
 

  

[In his deck tech](/en/events/2013/ptths13/video-deck-tech-colossal-gruul-with-makihito-mihara), Makihito Mihara made it clear he was playing a combo deck. With 4 Voyaging Satyr and 4 Nykthos, Shrine to Nyx, Mihara was looking to generate a large amount of mana. Garruk, Caller of Beasts; Arbor Colossus; and Polukranos, World Eater are great things to spend that mana on. 

  

* * *

  

Standard is shaping up to be a great format, with devotion being an important part of many different decks. It's also important that devotion isn't the only thing that you can do. We like making lots of exciting new things, but we work to make sure that any given thing isn't so powerful that nothing else is worth doing. Given the success of Esper Control, white beatdown and other non-devotion decks, there are plenty of options in Standard.

Thanks for joining me this week,

Adam Prosak

  
  

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Details_Static.png)](https://web.archive.org/web/20140427185532/http://www.wizards.com/Magic/Magazine/Article.aspx?x=events/magic/fnm) [![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Info_Static.png)](https://web.archive.org/web/20140406121204/http://www.wizards.com/Magic/tcg/products.aspx?x=mtg/tcg/products/theros) [![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_CIG_Static.png)](https://web.archive.org/web/20131206000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?set=[%20Theros%20]) 

  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Adam Prosak](https://i.ormos.uk/c0/a9/c0a94240f34bb8dddfba6ac5e334cbf89cb606c22e021336d1e084422d82ffe9.jpg "Adam Prosak")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Adam Prosak</b>&#10;        <br>&#10;        <a href="https://twitter.com/adam_prosak">@Adam_Prosak</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20131206000000/http://www.wizards.com/company/emailtoauthor.asp?author=Adam%20Prosak&amp;amp;headline=[Developing%20Devotion]">Email Adam</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20131206000000/http://www.wizards.com/magic/magazine/archive.aspx?author=adam%20prosak">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140325154830/http://www.wizards.com/magic/magazine/archive.aspx?tag=uncharted%20realms&amp;description=uncharted%20realms">Uncharted Realms Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

From Friday Night **Magic** to the Pro Tour, Adam Prosak loves all types of tournament **Magic**. Currently, Adam is working in R&D as a development intern. 

 