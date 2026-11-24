---
id: php5b19b
kind: article
lang: en
path: /en/articles/makingmagic/2014/02-24-a-la-mode
title: À La Mode
published: '2014-02-24'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    lang_detected: en
    capture_id: 211497
    url: https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    captured_at: '2024-05-18 03:37:29+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    lang_detected: en
    capture_id: 211497
    url: https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    captured_at: '2024-05-18 03:37:29+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    lang_detected: en
    capture_id: 211497
    url: https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    captured_at: '2024-05-18 03:37:29+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    lang_detected: en
    capture_id: 211497
    url: https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
    captured_at: '2024-05-18 03:37:29+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: php5b19b
  url: https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
  page_key: magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:37:29+00'
  capture_id: 211497
  wayback_url: https://web.archive.org/web/20240518033729id_/https://magic.wizards.com/en/news/making-magic/a-la-mode-2014-02-21
- document_id: php5b19b
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/288
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/288
  lang: en
  template: aspx
  captured_at: '2014-04-10 12:47:17+00'
  capture_id: 652319
  wayback_url: https://web.archive.org/web/20140410124717id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/288
- document_id: php5b19b
  url: https://magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24
  page_key: magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24
  lang: en
  template: drupal
  captured_at: '2022-07-01 04:36:14+00'
  capture_id: 863159
  wayback_url: https://web.archive.org/web/20220701043614id_/https://magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24
- document_id: php5b19b
  url: https://magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24-0
  page_key: magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24-0
  lang: en
  template: drupal
  captured_at: '2022-10-05 22:10:32+00'
  capture_id: 863172
  wayback_url: https://web.archive.org/web/20221005221032id_/https://magic.wizards.com/en/articles/archive/making-magic/%C3%A0-la-mode-2014-02-24-0
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: php5b19b
  capture_id: 652319
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/288
  wayback_url: https://web.archive.org/web/20140410124717id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/288
  captured_at: '2014-04-10 12:47:17+00'
  template: aspx
  sha256: 3987f62fa0c806e0c261ebd0103e203b3f0ec8292f279f2109b88cc0aca6c46b
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Fortify
  - Tooth and Nail
  - Naturalize
  - Taste of Paradise
  - Kavu Titan
  - Grizzly Bears
  - Fireball
  - Daru Stinger
  - Primal Clay
  occurrences: 49
---
Welcome to Tribute Week. This week, we'll be exploring the new tribute mechanic from *Born of the Gods*. As often happens during mechanic-based theme weeks, I already explained how it got designed during the previews. ([Here, if you haven't read it](/en/articles/makingmagic/2014/01-21-born-legacy).) So instead, I thought I would talk about a design topic that is key to the tribute mechanic: choice. And I use the word "choice" in particular—if you've never read my two-parter about decisions in **Magic** design, I urge you to give it a look as it is very relevant to today's topic. ([Part 1](/en/articles/makingmagic/2009/07-27-decisions-decisions-part-i). [Part 2](/en/articles/makingmagic/2009/08-10-decisions-decisions-part-ii).) All the spells I am going to discuss today are ones that give the caster a choice of two or more effects when they are cast. In today's article, I thought I'd walk you through a number of different ways we make choice cards and explain the ins and outs of designing them. 

### Modal Spells

 ![370712](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=370712&options=) 

  

Let's begin with the clearest example of a choice card—what is known as the modal spell. A modal spell is defined in the game as any spell that uses the expression "Choose one—," "Choose two—," or "Choose one or both—." Each option is considered a "mode." Fortify, from ***Magic** 2014* (above), is a recent example of a modal spell. 

The way to think of most modal spells is that they provide the caster with multiple spells of which they can choose one to cast (and sometimes more than one—I'll get to those in a moment). Usually, the choices you are given are worth less than the cost of the spell, but the flexibility the spell provides makes up for the cost deficit. It turns out that choice makes spells more powerful.

For the modal spells that offer you two choices, usually the choices are connected in some way. For aesthetic purposes, it's important that the spell not feel like two distinct spells but rather one spell that has some range for what it can do. If the two effects are wider apart, it is common for the designer to make sure one or more elements carries over. For example, let's take a look at Fortify above. The first ability is an aggressive attacking ability while the second one is a defensive blocking ability. By making the boost the same, changing a stat by +2 on all your creatures, the two modes of this spell feel connected, and thus the overall spell feels like one spell rather than two. Fortify also uses the trick of making the two spells contrast (one affects power while the other affects toughness) to make them feel like two sides of a coin, and thus interrelated. 

It's also very important for these type of choice spells—well, all choice spells—that there is an interesting choice to be made by the caster of the spell. If the player will choose the same mode the vast majority of the time, the choice card is not living up to its potential, play-wise.

While Fortify is the example of a basic modal card, there are a number of variations: 

**Charms** 

 ![Azorius Charm](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Azorius%20Charm&options=) 

  

We'll begin with charms. These are cards that give the caster not two, but three choices. The first [charms showed up in *Mirage*](https://web.archive.org/web/20140224000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+[Charm]&set=+[%22Mirage%22]) and were monocolored. Since then, we've done various multicolor charms, with the latest showing up in [*Return to Ravnica* block](https://web.archive.org/web/20140224000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+[Charm]&block=+[%22Return%20to%20Ravnica%22]). Because charms have three effects to choose from, they tend to be a little smaller in nature, which makes them have a bit of a different feel. 

Charms tend to have effects too small to justify a card by themselves, but having the choice of three of these mini effects are worthy of the card, due to the flexibility. Because the overall flavor is a collection of small effects, their being small is enough to connect them aesthetically, and designers don't often try to connect the effects mechanically.

The interesting design challenge of charms comes on two-color versions. One-color charms just have all effects from that color, while three-color charms have one from each color, but two doesn't divide evenly into three. The solution is to make one effect the first color, one effect the second color, and one effect that is an overlap between what the two colors can do.

**Commands** 

 ![141819](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=141819&options=) 

  

The [commands](https://web.archive.org/web/20140224000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Lorwyn%22]&name=+[Command]) were a cycle from *Lorwyn* where the caster was given four choices and had to choose two. I am including them here because although we've only done them once, they were very popular and people have been asking for new commands ever since. The trick to designing commands is that you want four abilities that can combine together well no matter which two you pick. Both charms and commands are difficult to do too many of because there are only so many abilities available to any one color. 

**Entwine** 

 ![48122](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=48122&options=) 

  

Entwine was a mechanic from *Mirrodin* block that gave you modal cards and then gave you the extra ability, for more mana, to cast both effects. The trick to designing the effects for entwine is that you have to make them such that they have synergy when combined. For example, the first ability of Tooth and Nail allows you to get creatures from your library and put them into your hand, while the second ability allows you to put creature cards from your hand onto the battlefield. Each is valuable by itself, but together combine to have an even more potent ability to put creatures from your library directly onto the battlefield. 

Entwine cards have a limited design space because there are only so many effects in each color combination that can synergize when combined.

**Split Cards** 

![](https://i.ormos.uk/f5/68/f568600ae3e67f3aabf9b790bbd7d0fad5d8087ef66e220b6a54bfc0b968077f.jpg) 

  

The split cards first showed up in *Invasion* block and take the choose-one modal theme to the visual extreme, displaying it as two different miniature cards. Because the words "choose one" don't actually appear (and because they do not share a mana cost), split cards are not technically modal cards and thus get their own category. Nonetheless, the split card is just a glorified modal card that lays out two choices for the caster. 

Because of the layout, split cards are allowed to be a bit more varied in their effects, and it is not as crucial that the two cross over aesthetically. This is because the flavor of the card is that it's actually two cards. If anything, the thing that links the cards together is the name, as split cards are always named as \_\_\_\_\_\_\_ & \_\_\_\_\_\_\_. When designing split cards, we always start with the names, as they are the hardest thing to do. We then design to the names. 

![](https://i.ormos.uk/04/14/0414ca53231b349e3f0253d6e63be4df703050e340def7b73a1bc682795ce003.png) 

  

The fuse mechanic, introduced in *Dragon's Maze*, is just the entwine mechanic applied to split cards (the ability was called "splitwine" in design). Like normal split cards, the split cards with fuse are not technically modal cards, although they follow all the same rules for design that entwine cards have. The added rules text limitation makes them even harder to create. 

**Choice of Type of Target** 

 ![370802](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=370802&options=) 

  

The next type of choice card, like split cards, isn't all that different from a modal card, but the text is written without the "choose one." These cards have two effects, one that each affects a different type of card. The Naturalize from above, for example, is a destruction card that can destroy either an artifact or an enchantment. Realize that if we wanted, Naturalize could be written out like this: 

![](https://i.ormos.uk/35/5a/355a3dd42dff91cf48219aeff46c49a1d02b46934f31389a5e96bb109e0a2cb0.jpg) 

  

The point of this is that the difference between a modal card and other choice cards is a thin line that could easily be shifted by templating. Now, technically, not using the "choose one" text makes the card play different in certain scenarios (for example, a Naturalize can be redirected from an artifact to enchantment where a modal card cannot change modes when redirected), but for most practical uses they are almost identical. 

This type of choice card is the most common and can be used most easily at lower rarities. While Naturalize does actually give you two choices, like the modal spells, it feels more like a singular spell than two spells that you have to choose between. I think that is another reason we don't use the "choose one" wording on these cards. 

The key to designing these types of cards is just picking effects that are able to affect different targets. The most common choices are either spells that affect two different permanent types or ones that hit a permanent type, most usually a creature, and a player. The biggest disconnect when choosing two different targets is not the mechanical aesthetics—as spells being able to affect different things feels natural—but the flavor. When you start to mix and match different targets, sometimes it's hard to define flavorfully what exactly the spell is. (For example, what destroys a creature or an enchantment?)

**Variable Spell** 

 ![3150](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=3150&options=) 

  

This next type of choice card has a base effect and then, for an extra cost (usually mana), you can either expand the spell in some way or get an additional ability that most often is synergistic with the first ability. This has become a very popular way to make new mechanics, so let's walk through the different ones **Magic** has used. 

**Kicker** 

 ![23106](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=23106&options=) 

  

The granddaddy of this type of spell is the kicker mechanic. There were a few individual spells like Taste of Paradise, above, from *Alliances*, that did this before kicker came around, but kicker is what put this section on the map. Kicker first appeared in *Invasion* and allowed the caster to spend more mana to boost the spell in some way, most often making a larger version of the effect. This means that, as with split cards, each effect comes with a different cost. 

The trick to designing a good kicker spell is to find an effect that will have different value at different times in the game. For example, Kavu Titan should often be played at whatever cost you are able to pay for it. There's a very famous story in R&D back when I used to play in the [Future Future League](/en/articles/latestdevelopments/2013/08-16-days-of-future-future-part-2). Randy Buehler gave me a mono-green deck to play and I went 4–0. After that week, Randy informed me that the Grizzly Bears in my deck were actually Kavu Titans. The next week I went 2–2. The big lesson was that I needed to treat my Kavu Titans like Grizzly Bears when I only had two mana but as a 5/5 trampler when I had five. 

The best kicker designs have that quality, where they hold value at both costs. Like modal spells, it's okay if each of these costs is higher than you would pay if the card only had a single effect. For example, we make strictly better than ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) for a 2/2 in most sets yet having a Grizzly Bear with the upside that it's a 5/5 trampler later in the game is quite a bargain. 

**Multikicker** 

 ![197769](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=197769&options=) 

  

Multikicker first showed up in *Worldwake* and it is a tweak on kicker that allows the caster to pay the kicker cost as many times as he or she likes. Multikicker cards are designed a little differently from kicker cards, as they have to be more scalable, so they can be cast at regular increments. Usually, this means that they are less optimized but more flexible. 

**Replicate** 

 ![96864](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=96864&options=) 

  

Replicate was the Izzet mechanic from the original *Ravnica* block in the set *Guildpact*. It allowed the caster to pay a cost to copy the spell. Like multikicker, this additional cost could be paid as many times as caster was able to pay, but can choose new targets. Also, like multikicker, this means that the effects for replicate had to be things that could scale. In general, replicate spells tend to be smaller effects to allow more opportunity to use the replicate costs. 

**Conspire** 

 ![158689](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=158689&options=) 

  

Conspire is basically a replicate variant from *Shadowmoor*,where you can tap two untapped creatures to make another copy of the spell. Unlike replicate, conspire can only be used once per spell. This restriction allowed design to make slightly bigger effects, although it also worked well with smaller effects. 

**Evoke** 

 ![370535](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=370535&options=) 

  

Evoke is a mechanic from *Lorwyn* that acts like a backwards kicker creature. Rather than spend more to add an enters-the-battlefield effect to a creature, evoke allows you to spend less to basically give up the creature and just get the enters-the-battlefield effect. Technically, you get the creature either way, but if the alternate cost is paid, the creature is immediately sacrificed once it hits the battlefield. 

The trick to designing evoke cards is similar to making good kicker cards, in that you want the "spell only" and "spell with creature" choices to both be viable at the point of the game where you can cast them. Evoke's biggest restriction is that it's tied to creatures.

**Buyback** 

 ![4843](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=4843&options=) 

  

I'm not sure if buyback, from *Tempest* block, should count as a choice card or not. It does give you a choice, but that choice doesn't change the effect. It allows you to choose whether or not get to keep the spell in your hand after you cast it. Designing buyback cards is very tricky, because any spell you can cast every turn can get very degenerate, even for effects that normally are pretty benign. 

**Splice** 

 ![50299](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=50299&options=) 

  

Splice, from *Champions of Kamigawa* block, is similar to buyback in that the choice is about getting to cast the spell again. Splice effects are grafted onto other spells, so they have more restrictions than buyback spells. Also, because you have to cast them after playing another spell, splice effects want to be pretty cheap. 

### Spells With a Scalable Effect

I wasn't sure whether to include this group as the subset as the last one but I decided to give it its own section. This grouping of cards are ones that, instead of having two choices, have an effect that allows the caster to have a scalable effect through some cost—not always mana.

**X Spells** 

 ![197](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=197&options=) 

  

The most basic type of spell in this category is an X spell. This is a spell that allows the caster to choose some amount of colorless mana that is then used to define an aspect of the spell. X spells started back in Alpha and show up in just about every set.

The key to designing an X spell is to figure out some variable that can exist at any number chosen. That variable, though, can be used on very different aspects of the spell. Also, as Fireball above shows, sometimes the mana spent can be used for more than one variable. 

**Amplify** 

 ![42278](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=42278&options=) 

  

Amplify was a creature mechanic from *Legions* that allowed you to add +1/+1 to the creature for each card in your hand of a certain creature type you revealed. Amplify differs from X spells in that the resource used to set the variable isn't mana. The trick to designing amplify creatures was to try and make creatures where the power was relevant. Sometimes this meant adding a creature keyword like trample or flying. Other times, as with Daru Stinger above, it meant giving the creature an ability that cared how many +1/+1 counters were on the creature. Amplify had a limited design space and only makes sense in a set with a strong tribal theme. 

**Devour** 

 ![174968](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=174968&options=) 

  

Devour was a creature mechanic from *Shards of Alara* block in the Jund shard. The mechanic allowed you to sacrifice creatures when the creature with devour entered the battlefield and then add an appropriate amount of +1/+1 counters. This is yet another scalable effect with yet another different resource being used, in this case creatures you control on the battlefield. The devour mechanic doesn't require all that much design as trading creatures for +1/+1 counters provided plenty of interesting game play. 

**Sweep** 

 ![74201](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=74201&options=) 

  

Sweep was an ability word from *Saviors of Kamigawa* on instants and one sorcery where you could return basic lands of the appropriate type to your hand to determine how big the effect of the spell was. *Saviors of Kamigawa* had a "hand size matters" theme and sweep was one way to help fill up your hand. It is yet another example, though, of a scalable effect. One of the signs that sweep wasn't a very deep mechanic was that we only printed four of them (one of many reasons I believe using an ability word for sweep was a mistake). 

### Other Options in Your Hand

This subset of choice cards gives you a second ability that can be used while the card is in your hand.

**Cycling** 

 ![5692](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=5692&options=) 

  

The cycling mechanic, originally appearing in *Urza's Saga* block, allows you to discard a card in your hand for some mana cost to get a card from the top of your library. The unique quality to this mechanic is that one choice, that of drawing a card, is consistent from card to card. The trick to designing a good cycling card is to choose an effect that you will only sometimes want to cycle, to ensure that there is always a decision whether or not to cycle the card. If the card is always cycled or never cycled, it is not doing a good job of providing choice. 

 ![41142](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=41142&options=) 

  

In *Onslaught* block, we started making cycling cards that had an effect when cycled. In many ways, this allowed cycling to mirror a kicker card. Usually, the cycling effect created a smaller "cantrip" version of the spell. These spells required effects with a number, to allow a big and small version. 

**Typecycling** 

 ![376323](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=376323&options=) 

  

In *Scourge*, the third set of the *Onslaught* block, we introduced a variant on cycling we called \[basic land\]cycling, where you could spend mana to discard the card and instead of drawing a card, you could get the appropriate basic land from your deck. Then, in *Future Sight*, we riffed off the idea of typecycling with this card: 

 ![130325](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=130325&options=) 

  

Vedalken Æthermage introduced the idea that cards could cycle for various things other than basic land. We have yet to do any typecycling other than basic land since Veldaken Æthermage was printed, but the rules have been created to allow it.

Typecycling is a little different to design than cycling because it comes with some form of tutoring. To make these cards work, the typecycling has to be on a card that you are willing to cycle to get the thing you need. For instance, \[basic land\]cycling tends to go on more expensive cards that you have less use of in the early game, making it easier to choose to discard them for basic land. Typecycling, like cycling, also tends to like to be on cards that have more conditional uses, allowing you to cycle them more often.

**Reinforce** 

 ![152963](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=152963&options=) 

  

When I designed this mechanic in *Morningtide*, I pitched it as a cycling variant. The only difference was, instead of getting a card when you discard the card in your hand, you instead get some number of +1/+1 counters. The design space for this mechanic was much more limiting than cycling, because there were a lot fewer spell effects/creatures that naturally connected with the granting of +1/+1 counters. 

**Channel** 

 ![87341](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=87341&options=) 

  

During *Saviors of Kamigawa*, we decided to do a number of cards that you could sacrifice from your hand for mana to generate an effect, usually tied thematically in some way to the base ability of the card. To connect these cards, we chose to give them an ability word, channel. Since then, we've decided this was a mistake, and while we have created cards that could be discarded from the hand for effect, we no longer label them as channel. The trick with designing these types of cards is making sure the discard effect feels like an organic part of the card by having it connect mechanically to the main card. 

**Transmute** 

 ![87992](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=87992&options=) 

  

Transmute, the Dimir mechanic from the original Ravnica block, allows you to discard the card to tutor for a card with the same converted mana cost. Like cycling and the other cycling variants, the key to designing this mechanic is making sure that you want to trade in the card some of the time, which often means that the cards with transmute are more situational.

**Forecast** 

 ![107379](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=107379&options=) 

  

Forecast, the Azorius mechanic from *Dissension*, has a slightly different twist. You can cast the spell normally but you also have the option of activating the card in your hand to generate a smaller effect. The two effects of the cards were designed so if you are able to do both on the same turn, they have synergy with one another. As with any cards with two effects that have synergy, the design space for this mechanic is limited. 

### Choice-Based Creatures

This category is all creatures that allow the caster a choice of which version of the creature he or she wants.

**Creatures With Options** 

 ![1017](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=1017&options=) 

  

The granddaddy of this type of card is Primal Clay from *Antiquities*, where the caster was given three different options of what he or she could get. A lot of cards like this these days are done with an optional cost and they appear up above in the Variable Spell section. 

**Morph** 

 ![39492](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=39492&options=) 

  

The morph mechanic first showed up in *Onslaught* block and allowed players to play creatures with morph, face down, as vanilla 2/2s. The morph mechanic then allowed players to pay a certain cost, almost always mana, to turn the card face up and turn into whatever creature was on the face-up side. Morph is a very deep mechanic worthy of an entire column to describe its design, but as this article is already on the long side, I'll just say that the key to designing morph creatures is understanding that the mystery quality of the cards is very important. The fun of morph cards is that any face-down card has the potential to be any morph creature, forcing the opponent to have to figure out what it is. 

**Unleash** 

 ![Carnival Hellsteed](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Carnival%20Hellsteed&options=) 

  

Unleash was the Rakdos mechanic from *Return to Ravnica*, where the caster of the creature could choose to add a +1/+1 counter when casting it. If he or she did, the creature then wasn't allowed to block. This mechanic worked fine with vanilla and French vanilla creatures. The key was making sure that giving up blocking had some relevance to the card. You wanted the player casting it to be tempted to put the +1/+1 counter on it, but often with some hesitation. 

**Imprint** 

 ![46741](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=46741&options=) 

  

I wasn't sure where to stick this mechanic, so I gave it its own category. Imprint was a mechanic from *Mirrodin* block (and later reprinted in *Scars of Mirrodin* block) where the player had to exile a card when casting the spell (the exiled card came from different places), which then was used as a marker to determine something about the spell. This mechanic was originally used exclusively on artifacts. 

Imprint cards were very hard to design because you needed to make them open enough to allow a lot of flexibility. You also wanted to make sure that the card mattered in a way that couldn't be replicated by simply making a singular choice (such as color or card type). Imprint cards proved to have a very narrow design space, so we have opted each time to make fewer but higher-profile ones.

### Choice Cards with Opponent Choosing

This last category gets us to the theme of the week.

**Punisher** 

 ![35891](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&MultiverseId=35891&options=) 

  

This mechanic, first seen in *Odyssey* block, is a spell where the opponent gets a choice. Both choices are bad for the opponent and usually are effects slightly stronger than the mana cost would normally allow. Punisher cards all have dealing damage directly to the opponent as one of the options. In *Odyssey* block, the inability for the caster to control the option allowed us to make choices on the punisher cards that are normally out of red's color pie. 

**Tribute** 

 ![Ornitharch](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Ornitharch&options=) 

  

And finally, we end today talking about tribute cards. Tribute cards are obvious descendants of punisher cards but have a few key differences. First, all of the tribute cards are creatures (and for flavor reasons, monsters). Second, one option on all the tribute cards is the choice of putting some number of +1/+1 counters on the creature, dictated by the number that appears in the keyword. The other effect is usually a spell effect either doing something bad to the opponent or good for the caster.

The trick for the tribute cards was making sure the designs were choices that were never easy for the opponent. If one option is the clearly correct choice, the tribute cards lose a lot of their play value. As such, [Tom LaPille and his development team](/en/articles/feature/2014/01-13-devign-inspiration) worked very hard to find a good balance between the two options. Design helped to make sure that each card had choices that would most often have an impact on the game play. 

Because you are trying to create some variety with creature size, tribute is limiting in how many cards you can include in a single set. Note that this is more about a restriction within a set than between sets.

### A Few Choice Words

Whew! As you can see, designers have a lot of choice of choice cards and we keep making more because players tend to love having choices. I hope today's column gave you a little insight into the different types of choice cards design has created over the years.

As always, I am happy to hear what you have to say about choice cards. Drop me an email, respond in the thread, or just talk to me in any of my many social media outlets ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro#)). 

Join me next week when I talk nuts and bolts.

Until then, may you have many choices available to you.

  

* * *

  

### "Drive to Work #98—1996"

My first podcast this week is a continuation of my 20 Years in 20 Podcasts series. Today I focus on **Magic**'s fourth year—1996. 

### "Drive to Work #99—*Torment*, Part 1"

My second podcast today is the first in my series on the design of *Torment* (aka the "black set"). 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      &#10;      &#10;      <div id="magic1"> Multi </div>&#10;      &#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*   [**Episode 99**](https://media.ormos.uk/ac/bd/acbd15aec5ecc95741ef46d6d01e7e8af3e14de99b65b2dce27b112ace4530b1.mp3) : *Torment, Part 1* (13.9 MB)
*   [**Episode 98**](https://media.ormos.uk/3e/9d/3e9d52ac85ab8d70e944da8e52d6c3cb4fb953f081f9862e26e50aa4645cede4.mp3) : *1996* (14.2 MB)
*   [**Episode 97**](https://media.ormos.uk/0a/6d/0a6d165358500fd019f8649e4c86235aaa5a87df5770a14aa20dfe1d491e4639.mp3) : *Blogatog* (15.9 MB)
*   [**Episode 96**](https://media.ormos.uk/cb/eb/cbeb44f767e9f03d4ed9a7512f100b2e7f22af39cada5c34d99520a1cf920277.mp3) : *New World Order* (13.4 MB)
*   [**Episode 95**](https://media.ormos.uk/dc/2f/dc2f209c2db3c26b2ccd4b63bfef2dd87bef213cc476b3c80246b99e00a52a81.mp3) : *Emotional Connection* (13.2 MB)  

*   [**Complete Drive To Work Podcast Archive**](/en/articles/makingmagic/undated/drive-to-work-podcast-archive)

  
  

* * *

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_Launch_Details_Static.png)](https://web.archive.org/web/20140224000000/http://www.wizards.com/Promo/HerosPath/Default.aspx) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_Prerelease_Minisite_Static.png)](https://web.archive.org/web/20140424103615/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/bornofthegods) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Mark Rosewater](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg "Mark Rosewater")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Mark Rosewater</b>&#10;        <br>&#10;        <a href="https://twitter.com/maro254">@maro254</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140224000000/http://www.wizards.com/company/emailtoauthor.asp?author=Mark%20Rosewater&amp;headline=[A%20La%20Mode]">Email Mark</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140415025705/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140410010616/https://www.wizards.com/magic/magazine/archive.aspx?tag=making%20magic&amp;description=making%20magic">Making Magic Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Working for **Magic** R&D since October, 1995, Mark Rosewater is currently the head designer. His hobbies include spending time with his family, talking about **Magic** on every known medium (including [a daily blog](http://markrosewater.tumblr.com/) and a [weekly podcast](https://itunes.apple.com/us/podcast/magic-gathering-drive-to-work/id580709168)), and writing about himself in the third person. 

 