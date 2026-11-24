---
id: cpqa4bwx
kind: article
lang: en
path: /en/articles/makingmagic/2012/12-10-price-of-progress-simple-fixes
title: 'Price of Progress: Simple Fixes'
published: '2012-12-10'
column_slug: makingmagic
column: Making Magic
authors:
- slug: nate-price-0a72a9e2
  name: Nate Price
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    lang_detected: en
    capture_id: 228652
    url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    captured_at: '2024-05-18 04:09:21+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    lang_detected: en
    capture_id: 228652
    url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    captured_at: '2024-05-18 04:09:21+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    lang_detected: en
    capture_id: 228652
    url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    captured_at: '2024-05-18 04:09:21+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    lang_detected: en
    capture_id: 228652
    url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
    captured_at: '2024-05-18 04:09:21+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - jhe4r3dr
sources:
- document_id: cpqa4bwx
  url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
  page_key: magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:09:21+00'
  capture_id: 228652
  wayback_url: https://web.archive.org/web/20240518040921id_/https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
- document_id: jhe4r3dr
  url: https://magic.wizards.com/en/articles/archive/making-magic/price-progress-simple-fixes-2012-12-10
  page_key: magic.wizards.com/en/articles/archive/making-magic/price-progress-simple-fixes-2012-12-10
  lang: en
  template: drupal
  captured_at: '2021-10-27 12:50:27+00'
  capture_id: 905704
  wayback_url: https://web.archive.org/web/20211027125027id_/https://magic.wizards.com/en/articles/archive/making-magic/price-progress-simple-fixes-2012-12-10
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: cpqa4bwx
  capture_id: 228652
  url: https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
  wayback_url: https://web.archive.org/web/20240518040921id_/https://magic.wizards.com/en/news/making-magic/price-progress-simple-fixes-2012-12-10
  captured_at: '2024-05-18 04:09:21+00'
  template: contentful
  sha256: 5763a5f9f0cf983f8e950129e06b00549166457da3fd60f484d5eff39cf9af7b
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 4
---
As we talked about [last week](/en/articles/makingmagic/2012/12-03-price-of-progress-paying-the-price), one of the easiest sets of mistakes to make while constructing a Sealed Deck is mistakes involving mana. You could make a mistake putting the proper amount of lands of each type in your deck to support the spells you'd like to play. You could be playing a combination of spells that would make the construction of a proper mana base impossible. Your mana base could prevent you from consistently playing the spells you want at the time you want. The list goes on.

![](https://i.ormos.uk/d6/b1/d6b1923a10f2f0b6d9b9b639489a171bd4ea584b14f9f4d8d6163a3eb01514af.jpg)

[Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) | Art by [Yeong-Hao Han](https://web.archive.org/web/20121210000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Yeong-Hao%20Han%22%5D)

Fortunately, we looked at a few great ways to prevent these issues from cropping up in your builds. Most of them involved a quick, basic look at the math behind the decisions, which hopefully helped you understand why the mistakes were, in fact, mistakes. Mana issues are deceptive traps, difficult to see unless they are very clearly outlined, and even then they can be difficult to spot. This week, we'll take a look at some quick tips to help internalize some of the things we learned last week, as well diving into some of the specifics of *Return to Ravnica* mana.

### Math Minor

There are a large number of things that have to be done in the limited amount of time set aside for building decks in a Sealed Deck tournament. You have to quickly analyze your card pool, find your bombs and removal, identify strong colors, examine mana curves, compare sets of cards against others, and properly build the mana base for your deck. This can all be quite hectic, and can frequently come down to the last minutes. Doing probability math, even very basic math, doesn't usually rate very highly on things to do during this period. While probability is your greatest weapon when trying to build a deck with a good mana base, there isn't a whole lot of time to do it, especially if you're building your deck right.

![](https://i.ormos.uk/f4/3f/f43f6946905db3a54d56d73a0ba580d8a0db5f85c923723bbeff75460d1164b8.jpg)

[Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) | Art by [John Avon](https://web.archive.org/web/20121210000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22John%20Avon%22%5D)

Fortunately, you shouldn't have to. Much of the math can be condensed down into rules that are easy to internalize and remember at a moment's notice. Understanding these rules not only makes it much easier to actually build the mana base in an efficient manner, it helps you to make the most of your time in other areas of the build. Things like this will ultimately come together to make you a more efficient deck builder, and you will ultimately be building better decks.

Time to get to the rules:

*   You need between two and four mana sources to cover any splash
*   If you need to be absolutely sure you are going to hit your land drops on turns four, five or six every time, you need to be playing eighteen lands
*   If you count the number of cards of a particular color in your deck and take two-thirds of that, it's a pretty good estimate of the number of lands of that color you should be playing

Keeping these three simple guidelines in mind when building your deck will go a long way to shoring up any potential mistakes, as well as helping you make better use of your time. It is important to remember that these are only very basic guidelines, and that there will almost certainly be times when you need to alter them. That said, they still provide a wonderful starting point. Let's take a brief glance at them one at a time.

### Splish Splash

*You need between two and four mana sources to cover any splash.*

It is incredibly hard to resist the call of powerful cards, even if it is apparent from your card pool that you will not be playing that color. As such, you will end up frequently entertaining the idea of splashing a card or two into your deck. In order to be able to consistently cast your splash cards, you need to make sure your mana base has the appropriate support.

First, let me say that five cards is not a splash. Once you hit four or five cards, you are looking at a secondary color for a deck. Five cards is one-eighth of your deck, so nearly every opening hand is likely to have one card of that color. The idea of a splash is that it is a small percentage of your deck and it provides your deck something it needs. It's an accessory, not a main part of the wardrobe.

![](https://i.ormos.uk/c2/d0/c2d09e342a0713501313835a458f10220c7dec448760cfda753d09c73f6dd01b.jpg)

[Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island) | Art by [Richard Wright](https://web.archive.org/web/20121210000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Richard%20Wright%22%5D)

As such, you should be looking to keep your splash small—from one to three cards. In addition, it is important that your splash cards not have a heavy mana requirement. Splashing a card that costs two mana of that color obviously requires two mana sources in play during the part of the game that you want that spell to have an effect. If you want to be casting your "splashed" [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annihilating+Fire) around turn four or five, you need to have around seven red sources in your deck to ensure that you can afford the double red in the cost.

To determine where in the two to four spectrum that your splash falls, you need to consider a few things. First, if you need to be able to reliably cast your splash cards around turn four or so, lean toward four sources, even if you are only splashing one card. Second, if you do decide to splash a card with a double-mana requirement, you have to play four sources. Third, if you don't really care when you cast your splash cards, you can start with two mana sources for one splash card and then add another land for each other card you splash.

### Gotta Hit 'Em All

*If you need to be absolutely sure you are going to hit your land drops on turns four, five or six every time, you need to be playing eighteen lands.*

I will admit that much of the probability math I've been giving you to figure out the number of lands you need to be playing is slightly different than the actual math that needs to be done. Instead of calculating the chance of drawing the cards you need, I should be calculating the chance of *not* drawing them and subtracting that from 100%. But that is a more complicated calculation, and this isn't a math class. The calculations I've been doing are far simpler, easier to do in your head (which is really important), and are close enough to the correct answers that I'm fine using them as guidelines.

That said, using them to calculate the number of lands needed for this rule will let you down. Rather than do the long calculation, just trust me on this. If your deck is incredibly reliant on making sure that it hits the fourth-turn land drop every game, you really need to be playing eighteen mana sources, at least. For six, it's closer to twenty, but you can get away with like eighteen lands and a Keyrune. Most decks won't *need* to hit six the same way a deck will need to hit four, so don't be confused. Six-drops will have an incredible impact on the game no matter when you cast them, and hitting them around turn eight or so rather than turn six usually doesn't make much of a difference. If your deck is a bit light on its drops for turns one through three, you *have* to hit those four-drops. If your opponent is playing a bunch of fliers and you sided into a few [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Towering+Indrik)s to deal with them, you *have* to hit it on turn four. If you're playing Golgari and you want to be able to begin scavenging on turns four, five, or six, you're in the same boat. You have to play eighteen lands.

### Counting Cards

*If you count the number of cards of a particular color in your deck and take two-thirds of that, it's a pretty good estimate of the number of lands of that color you should be playing.*

This one will certainly help speed things up when it comes to building your mana base. It's a fairly simple rule that happens to be more or less right. There are certainly some things that will force you to want to play more or less, but this is a good starting point. For example, if your deck is thirteen blue cards and ten white cards, this rule gives you eight Islands and seven Plains. Moving that up to nine Islands and eight Plains to make the full seventeen lands is more or less going to be right every time. Say you're playing seven blue cards and sixteen white cards. That's four Islands and ten Plains. Instinct would tell you that adding two Islands and one Plains to complete the seventeen lands would be a reasonable decision, and instinct wouldn't let you down in this case. Following this rule is a great base for a correct mana base.

![](https://i.ormos.uk/33/c9/33c90e4fa03fed4e2dcff5db52b73a4a03ff17735c7fb1b89bb900a0fb64393f.jpg)

[Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) | Art by [Richard Wright](https://web.archive.org/web/20121210000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Richard%20Wright%22%5D)

With that in mind, there are a few things to consider that will modify this, and they're related to things we talked about last week. First, if there are cards with double-mana requirements in a color, you need to skew slightly more in that direction. The same goes for a color that has a bunch of one-, two-, and three-drops in it. In these spots, you can add the extra lands needed to make a full land count to this color alone, or even consider taking away from the other color. Let your conscience be your guide. Remember, the idea is to make it easier to cast these cards while not making it more difficult to cast the other ones. If you can't do that, there might be an issue with the mana requirements in your deck. The two most frequent examples of this are when a secondary color makes up all of the early drops in a deck, or when there are cards from each color that have multiple-mana requirements in their casting cost. These situations are bad in general and should be avoided whenever possible.

### Ravnica to the Rescue

*Return to Ravnica* is such a sweetheart. It knows that it's forcing you to play multicolored cards and two or three colors. It knows that it's got a lot of cards that have double-mana requirements, sometimes of two different colors on the same card. It knows these things, and it wants to help. *Return to Ravnica* has got a large number of ways built into it to ease this mana burden.

First, you have the rare multicolor lands, like [Blood Crypt](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Crypt) and [Hallowed Fountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hallowed+Fountain), and the common Guildgates. Having these in your pool make mana much more reasonable, especially for splashes. For splashes that are integral to the deck, such as a couple of black removal spells in a deck that doesn't have any other removal, simply add the multicolor land and count it as a mana source of the non-splash color. In an Izzet deck with no red removal, count that [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+Guildgate) as a red source. This doesn't hurt your red mana count and effectively gives you a free extra black source, making casting your splash easier. On the other hand, if the splash isn't as important or doesn't require as much mana, feel free to count it as one of the splash color's mana sources. This will be especially useful if the other color the land can produce is one that is in high demand in your deck. For example, if you're splashing some Selesnya cards into an Azorius deck with multiple [Sunspire Griffin](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunspire+Griffin)s, count those [Selesnya Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Selesnya+Guildgate)s as a green source. This deck needs a bunch of white mana sources, so covering your splash and giving yourself extra white mana sources is an ideal solution.

<table><tbody><tr><td><div><div><img alt="Sunspire Griffin" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sunspire+Griffin"></div></div></td><td><div><div><img alt="Selesnya Guildgate" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Selesnya+Guildgate"></div></div></td></tr></tbody></table>

Second, you have the Keyrunes. These are unique because they serve multiple purposes. They provide splash mana sources and mana acceleration for those decks with a large number of late-game cards, and they also serve as creatures if the deck's main colors are the guild of the Keyrune. It's important not to overlook the Keyrunes' ability to attack, as most of them are quite potent attackers. However, it's important not to think of them as creatures if the guild is a splash guild. Sure, you will occasionally be able to activate a splashed Keyrune if you draw a second mana source, but I wouldn't count on it the same way that a [Rakdos Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+Keyrune) is almost always a 3/1 first-striker in a Rakdos deck. It's also important to consider that the Keyrunes can count as a mana source for a splash color instead of a land. If you need four mana sources, you can simply run three appropriate lands and the Keyrune. It also counts as a mana source when figuring the eighteen you need to make sure you hit four, five, and six, but I would probably still play the extra land in that case. One last point about Keyrunes is not to overlook their ability to help speed up the game. While I'm not overly fond of using an off-color Keyrune to help ramp a deck, there certainly are situations when a deck needs to hit five or six mana as early as possible, and I would certainly entertain the idea in those cases.

<table><tbody><tr><td><div><div><img alt="Rakdos Keyrune" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rakdos+Keyrune"></div></div></td><td><div><div><img alt="Frostburn Weird" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Frostburn+Weird"></div></div></td></tr></tbody></table>

*Return to Ravnica*'s final helper is hybrid mana. Hybrid mana is such a deceptive helper, but after enough games with it, you really begin to see its value. A card that is hybrid in a deck's two main colors might as well be an artifact. You can cast it with virtually any combination of lands in the deck. In addition, it lets cards find homes in different decks. You can play [Frostburn Weird](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frostburn+Weird) in an Izzet deck, sure, but it also has a home in Azorius and Rakdos decks. It's important not to be blinded by the color combination in the hybrid cost. It may seem simple, but I've seen a number of people overlook putting a hybrid card into a deck that is only playing one of the hybrid colors. Hybrid mana exists to give a card multiple functions and multiple homes. This is invaluable in Sealed deck, which requires a critical mass of good cards to have a reasonable deck. Hybrid mana makes it so you have cards in your pool that go into multiple decks you could build, making it so much easier to reach this critical mass regardless of the build you choose.

### Homework, Ho!

Last week's homework was a doozy. The pool was admittedly not very good, especially not compared with some of the pools I'd given you to work with in previous weeks. The idea behind this week's pool is that I wanted to sneak a card pool that simply isn't that great. You're going to have a bunch of these in your career as a **Magic** player, and getting a handle on how to deal with them is going to be very important. You really need to identify which cards are your best ones and find a way to play them if possible. That being said, you have to remember that you have to still be able to fill a curve and avoid mana issues if possible. Mediocre card pools allow you to shift the rules we've been talking about a little, especially in the mana department, if you feel it warrants it. After all, if you feel like you're going to lose games thanks to an underwhelming power level, it could be worth it to risk some losses to mana issues to avoid that.

To begin, the white was fairly unimpressive, to say the least. Other than [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martial+Law), [Trostani's Judgment](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trostani%27s+Judgment), and a few good creatures, there isn't really anything to write home about. Blue isn't too much better, but it's aided by the fact that its creatures are just better than the white ones. Black is pretty much useless except for its removal spells. Red and green are really where the depth is in this Sealed Pool, but they both really lack a solid early game. As for bombs, you've got [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martial+Law), which isn't anything super exceptional; [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift), which is much better when your deck can put early pressure on opponents; and [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing), which is one of the best cards in the set.

<table><tbody><tr><td><div><div><img alt="Cyclonic Rift" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Cyclonic+Rift"></div></div></td><td><div><div><img alt="Collective Blessing" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Collective+Blessing"></div></div></td></tr></tbody></table>

Let's see what you guys came up with!

First, there were a number of players who identified [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing) as the best card in the pool and dove into a Selesnya deck. Here's an example from Gemore:

#### Gemore's Homework

##### 

![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (11)

1 [Azorius Justiciar](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BJusticiar%5D) 1 [Centaur Healer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCentaur%5D+%5BHealer%5D) 1 [Concordia Pegasus](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConcordia%5D+%5BPegasus%5D) 1 [Keening Apparition](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeening%5D+%5BApparition%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 2 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 2 [Trained Caracal](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrained%5D+%5BCaracal%5D) 1 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D)

##### Sorcery (2)

1 [Coursers' Accord](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoursers%27%5D+%5BAccord%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D)

##### Instant (4)

2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Selesnya Charm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BCharm%5D) 1 [Trostani's Judgment](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrostani%5D+%5BJudgment%5D)

##### Enchantment (6)

1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D) 1 [Death's Presence](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeath%5D+%5BPresence%5D) 1 [Ethereal Armor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthereal%5D+%5BArmor%5D) 1 [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartial%5D+%5BLaw%5D) 2 [Soul Tithe](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BTithe%5D)

##### Land (17)

8 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)

40 Cards

##### White (10)

1 [Azorius Justiciar](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BJusticiar%5D) 1 [Concordia Pegasus](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConcordia%5D+%5BPegasus%5D) 1 [Keening Apparition](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeening%5D+%5BApparition%5D) 2 [Trained Caracal](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrained%5D+%5BCaracal%5D) 1 [Ethereal Armor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthereal%5D+%5BArmor%5D) 1 [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartial%5D+%5BLaw%5D) 2 [Soul Tithe](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BTithe%5D) 1 [Trostani's Judgment](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrostani%5D+%5BJudgment%5D)

##### Green (8)

1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 2 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 1 [Death's Presence](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeath%5D+%5BPresence%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D)

##### Multi colored (5)

1 [Centaur Healer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCentaur%5D+%5BHealer%5D) 1 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D) 1 [Coursers' Accord](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoursers%27%5D+%5BAccord%5D) 1 [Selesnya Charm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BCharm%5D)

##### Colorless (17)

8 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)

40 Cards

##### 1 (6)

2 [Trained Caracal](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrained%5D+%5BCaracal%5D) 1 [Ethereal Armor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthereal%5D+%5BArmor%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D)

##### 2 (5)

1 [Concordia Pegasus](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConcordia%5D+%5BPegasus%5D) 1 [Keening Apparition](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeening%5D+%5BApparition%5D) 1 [Selesnya Charm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BCharm%5D) 2 [Soul Tithe](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BTithe%5D)

##### 3 (2)

1 [Centaur Healer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCentaur%5D+%5BHealer%5D) 1 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D)

##### 4 (5)

1 [Azorius Justiciar](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BJusticiar%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 2 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 1 [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartial%5D+%5BLaw%5D)

##### 5 (1)

1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D)

##### 6 (4)

1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D) 1 [Coursers' Accord](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoursers%27%5D+%5BAccord%5D) 1 [Death's Presence](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeath%5D+%5BPresence%5D) 1 [Trostani's Judgment](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrostani%5D+%5BJudgment%5D)

23 Cards

##### Common (32)

8 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 9 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Centaur Healer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCentaur%5D+%5BHealer%5D) 1 [Concordia Pegasus](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConcordia%5D+%5BPegasus%5D) 1 [Keening Apparition](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeening%5D+%5BApparition%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 2 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 2 [Trained Caracal](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrained%5D+%5BCaracal%5D) 1 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 1 [Coursers' Accord](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoursers%27%5D+%5BAccord%5D) 1 [Ethereal Armor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEthereal%5D+%5BArmor%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Trostani's Judgment](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrostani%5D+%5BJudgment%5D)

##### Uncommon (5)

1 [Azorius Justiciar](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BJusticiar%5D) 1 [Selesnya Charm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BCharm%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D) 2 [Soul Tithe](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BTithe%5D)

##### Rare (3)

1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D) 1 [Death's Presence](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeath%5D+%5BPresence%5D) 1 [Martial Law](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartial%5D+%5BLaw%5D)

40 Cards

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20121210000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul+Tithe)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Giant+Growth)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Justiciar)

a:21:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Azorius Justiciar";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Centaur Healer";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Concordia Pegasus";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Keening Apparition";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Korozda Monitor";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Rubbleback Rhino";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Towering Indrik";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Trained Caracal";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Vassal Soul";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Collective Blessing";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Coursers' Accord";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Death's Presence";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Ethereal Armor";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Giant Growth";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Martial Law";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Selesnya Charm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Slime Molding";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Soul Tithe";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Trostani's Judgment";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}}

  

I like an attempt to run the [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing). After all, it is clearly the best card in the entire pool. There will be games that it simply wins on its own. That said, the concession in this deck is the fact that you have to play about a half-dozen fairly unimpressive cards. [Trained Caracal](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trained+Caracal) is a card I virtually never want to be playing. Even with the creature enhancers in this deck, it is simply too underpowered for my tastes. [Soul Tithe](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Tithe) is another card that I'm not really keen on. It's very conditional. If you get it on something good, your opponent will likely keep it around, as he or she will do if you put it on something inexpensive. It's at its best on something cast on the curve, in the early part of the game. Other than that, it's simply too unreliable.

Unfortunately, since this card pool isn't that strong, concessions like this often have to be made. This deck did the right thing by identifying bombs and trying to play them, identifying what it wants to do (play creatures and enhance them), building a curve, and avoiding mana problems. This deck isn't a bad one and is a perfectly good representative of an acceptable deck to come out of this pool.

Others decided to eschew the Selesnya build for one that packs more consistent removal. Here's a Rakdos build from silasw:

#### silasw's Homework

##### 

![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (13)

1 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Catacomb Slug](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSlug%5D) 1 [Dark Revenant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRevenant%5D) 1 [Drainpipe Vermin](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrainpipe%5D+%5BVermin%5D) 1 [Grim Roustabout](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BRoustabout%5D) 1 [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BShadow%5D) 1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 2 [Zanikev Locust](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZanikev%5D+%5BLocust%5D)

##### Instant (8)

1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D) 1 [Electrickery](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrickery%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 1 [Launch Party](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLaunch%5D+%5BParty%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Artifact (2)

1 [Codex Shredder](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCodex%5D+%5BShredder%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D)

##### Land (17)

1 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 8 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D)

40 Cards

##### Blue (1)

1 [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)

##### Black (9)

1 [Catacomb Slug](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSlug%5D) 1 [Dark Revenant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRevenant%5D) 1 [Drainpipe Vermin](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrainpipe%5D+%5BVermin%5D) 1 [Grim Roustabout](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BRoustabout%5D) 1 [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BShadow%5D) 2 [Zanikev Locust](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZanikev%5D+%5BLocust%5D) 1 [Launch Party](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLaunch%5D+%5BParty%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Red (9)

1 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Electrickery](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrickery%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### Multi colored (2)

1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D)

##### Colorless (19)

1 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 8 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 1 [Codex Shredder](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCodex%5D+%5BShredder%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D)

40 Cards

##### 1 (5)

1 [Drainpipe Vermin](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrainpipe%5D+%5BVermin%5D) 1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Codex Shredder](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCodex%5D+%5BShredder%5D) 1 [Electrickery](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrickery%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### 2 (3)

1 [Grim Roustabout](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BRoustabout%5D) 1 [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### 3 (5)

2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D)

##### 4 (4)

1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Dark Revenant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRevenant%5D) 1 [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BShadow%5D) 1 [Launch Party](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLaunch%5D+%5BParty%5D)

##### 5 (2)

1 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Catacomb Slug](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSlug%5D)

##### 6 (4)

1 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 2 [Zanikev Locust](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZanikev%5D+%5BLocust%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

23 Cards

##### Common (30)

1 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 8 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 1 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Catacomb Slug](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSlug%5D) 1 [Drainpipe Vermin](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrainpipe%5D+%5BVermin%5D) 1 [Grim Roustabout](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BRoustabout%5D) 1 [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BShadow%5D) 1 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Electrickery](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrickery%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 1 [Launch Party](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLaunch%5D+%5BParty%5D)

##### Uncommon (9)

1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Dark Revenant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRevenant%5D) 1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 2 [Zanikev Locust](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZanikev%5D+%5BLocust%5D) 1 [Codex Shredder](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCodex%5D+%5BShredder%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Rare (1)

1 [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCyclonic%5D+%5BRift%5D)

40 Cards

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

[Deal Another Hand](https://web.archive.org/web/20121210000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Street+Spasm)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cyclonic+Rift)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rakdos+Guildgate)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

a:25:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Rakdos Guildgate";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Batterhorn";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Bloodfray Giant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Catacomb Slug";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Dark Revenant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Drainpipe Vermin";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Grim Roustabout";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Perilous Shadow";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Rakdos Cackler";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Tenement Crasher";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Viashino Racketeer";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Zanikev Locust";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Annihilating Fire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Auger Spree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Codex Shredder";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Cyclonic Rift";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Electrickery";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Explosive Impact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Izzet Keyrune";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Launch Party";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:23;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Street Spasm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:24;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Ultimate Price";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}}

  

This deck certainly has more reliable removal than the Selesnya deck. Seven removal spells gives this deck answers to an incredibly large variety of threats. The only real problem I have with this version of the deck is the creatures. The black creatures from the pool are simply abysmal, unfortunately. There aren't any of the marquee black creatures, like [Dead Reveler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dead+Reveler)s or [Ogre Jailbreaker](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ogre+Jailbreaker), that really make the black decks run well. This deck has a reasonable late game, although it isn't overly powerful. Three impressive six-drops are reasonable ways to finish the game, as is [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perilous+Shadow), and [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift) can really do some damage, but these cards are all best when there was some early pressure, which this deck really can't do. I'm also not too keen on the [Codex Shredder](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Codex+Shredder) plan, which I'd probably cut to add the powerful [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nivmagus+Elemental) in this spell-heavy deck.

![](https://i.ormos.uk/00/0b/000b4d9c96bc7c0e489b151fe6134f9bea02b28a1708ec3597477b3b1afd369e.jpg)  

Despite this, I applaud the fact that this deck also stayed on target. While it doesn't have the best curve in the world, it has a clear goal in mind: getting to the late game. Between the defensive cards like [Perilous Shadow](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perilous+Shadow), [Grim Roustabout](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Roustabout), and [Catacomb Slug](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Catacomb+Slug), and the plethora of removal, the deck really wants to hit the part of the game where its six-drops can do their work. It also avoids the mana problems nicely with a simple splash, well supported, that doesn't really have an imperative timetable. It also benefits from the fact that sometimes a boatload of removal will allow even the worst creatures to get the job done.

This week, I had my [Grand Prix Nagoya](https://web.archive.org/web/20121210000000/https://magic.wizards.com/en/events/coverage/okitas-glorious-rise-nagoya) coverage compatriot, and the face of DailyMTG.com's Limited Information column, [Steve Sadin](https://web.archive.org/web/20130520112843/http://www.wizards.com/magic/magazine/archive.aspx?author=steve%20sadin), take a crack at this Sealed Deck pool. Here's what he came up with:

#### Steve Sadin's Homework

##### 

![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (13)

2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 3 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D)

##### Sorcery (1)

1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D)

##### Instant (7)

1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Enchantment (1)

1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D)

##### Land (18)

6 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Golgari Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolgari%5D+%5BGuildgate%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D)

40 Cards

##### Black (1)

1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Red (10)

2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### Green (8)

1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 3 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D)

##### Multi colored (3)

1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D)

##### Colorless (18)

6 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Golgari Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolgari%5D+%5BGuildgate%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D)

40 Cards

##### 1 (5)

1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### 2 (1)

1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### 3 (4)

2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D)

##### 4 (5)

1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 3 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D)

##### 5 (3)

2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D)

##### 6 (4)

2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

22 Cards

##### Common (34)

6 [Forest](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Plains](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Golgari Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolgari%5D+%5BGuildgate%5D) 1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 1 [Korozda Monitor](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKorozda%5D+%5BMonitor%5D) 1 [Rubbleback Rhino](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRubbleback%5D+%5BRhino%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 3 [Towering Indrik](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTowering%5D+%5BIndrik%5D) 2 [Viashino Racketeer](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViashino%5D+%5BRacketeer%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D) 2 [Giant Growth](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D)

##### Uncommon (4)

1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Slime Molding](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlime%5D+%5BMolding%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Rare (2)

1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 1 [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollective%5D+%5BBlessing%5D)

40 Cards

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20121210000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Street+Spasm)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Golgari+Guildgate)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Viashino+Racketeer)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nivmagus+Elemental)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Towering+Indrik)

a:22:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Golgari Guildgate";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Rakdos Guildgate";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Batterhorn";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Bloodfray Giant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Korozda Monitor";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Nivmagus Elemental";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Rubbleback Rhino";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Tenement Crasher";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Towering Indrik";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Viashino Racketeer";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Annihilating Fire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Auger Spree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Collective Blessing";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Explosive Impact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Giant Growth";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Slime Molding";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Street Spasm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Ultimate Price";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}}

  

After building six or seven decks, from Izzet to Selesnya to Golgari, Sadin ended up with this red-green number splashing for two different colors.

As he explained it to me, the card pool is, obviously, very weak overall. The creatures generally aren't that good, so it was important to play as many good ones as he could. He wanted to play [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing), since it's by far the best card in this pool and likely to be the best card in either your or your opponent's decks most of the time. This version of the deck runs a lighter curve, since there really were few early creatures in these two colors. Fortunately, this deck has an incredible turn four and is capable of neutralizing an opponent's early aggression as soon as it gets there. This made him feel more comfortable about having such a light early game. The only card in his deck that he really wants to cast early in the game is [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nivmagus+Elemental), which can really get out of hand with all of the cheap spells this deck has access to.

![Nivmagus Elemental](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nivmagus+Elemental)

  

This is an important time to talk about the two-color splash that Sadin chose to go with. Since his deck doesn't have early game requirements other than the Nivmagus, he felt comfortable splashing for two colors. The main reason to avoid this is that it really hurts a deck's ability to hit the lands it needs in the early stages of the game. Since all his deck really wants is possibly a Mountain by turn three and a Forest by turn four, splashing for two colors doesn't really hurt that. Also, he had two Guildgates, allowing his black splash to be more or less free. Since neither of his two splashed cards really needs to be on the table in a timely fashion, he chose to go with the deck that had the most power, even though it was four colors. Again, this is a perfect example of a deck that adds slightly more mana issues to give the deck a significantly lower chance of losing to the fact that it generally has worse cards. Remember, though, without all of these factors being the case, this is an incredibly risky move, and not one I recommend you take.

Lastly, here is my deck:

#### Nate Price's Homework

##### 

![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (13)

1 [Bellows Lizard](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBellows%5D+%5BLizard%5D) 1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 2 [Nivix Guildmage](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivix%5D+%5BGuildmage%5D) 1 [Tower Drake](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTower%5D+%5BDrake%5D) 2 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D)

##### Sorcery (1)

1 [Inaction Injunction](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInaction%5D+%5BInjunction%5D)

##### Instant (7)

1 [Dispel](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Inspiration](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInspiration%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

##### Artifact (1)

1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D)

##### Enchantment (1)

1 [Pursuit of Flight](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPursuit%5D+%5Bof%5D+%5BFlight%5D)

##### Land (17)

1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 2 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)

40 Cards

##### Blue (4)

1 [Tower Drake](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTower%5D+%5BDrake%5D) 1 [Dispel](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 1 [Inaction Injunction](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInaction%5D+%5BInjunction%5D) 1 [Inspiration](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInspiration%5D)

##### Black (1)

1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### Red (10)

1 [Bellows Lizard](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBellows%5D+%5BLizard%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 1 [Pursuit of Flight](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPursuit%5D+%5Bof%5D+%5BFlight%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

##### Multi colored (7)

1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 2 [Nivix Guildmage](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivix%5D+%5BGuildmage%5D) 2 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D)

##### Colorless (18)

1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 2 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D)

40 Cards

##### 1 (5)

1 [Bellows Lizard](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBellows%5D+%5BLizard%5D) 1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D) 1 [Dispel](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### 2 (5)

2 [Nivix Guildmage](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivix%5D+%5BGuildmage%5D) 1 [Inaction Injunction](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInaction%5D+%5BInjunction%5D) 1 [Pursuit of Flight](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPursuit%5D+%5Bof%5D+%5BFlight%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D)

##### 3 (6)

1 [Tower Drake](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTower%5D+%5BDrake%5D) 2 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D)

##### 4 (2)

1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Inspiration](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInspiration%5D)

##### 5 (2)

2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D)

##### 6 (3)

2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

23 Cards

##### Common (32)

1 [Rakdos Guildgate](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BGuildgate%5D) 2 [Swamp](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 7 [Mountain](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Island](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Bellows Lizard](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBellows%5D+%5BLizard%5D) 1 [Tower Drake](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTower%5D+%5BDrake%5D) 2 [Vassal Soul](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVassal%5D+%5BSoul%5D) 2 [Batterhorn](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBatterhorn%5D) 2 [Tenement Crasher](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTenement%5D+%5BCrasher%5D) 1 [Dispel](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 1 [Inaction Injunction](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInaction%5D+%5BInjunction%5D) 1 [Pursuit of Flight](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPursuit%5D+%5Bof%5D+%5BFlight%5D) 1 [Annihilating Fire](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnihilating%5D+%5BFire%5D) 1 [Auger Spree](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAuger%5D+%5BSpree%5D) 1 [Inspiration](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInspiration%5D) 1 [Explosive Impact](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExplosive%5D+%5BImpact%5D)

##### Uncommon (7)

1 [Rakdos Cackler](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BCackler%5D) 2 [Nivix Guildmage](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivix%5D+%5BGuildmage%5D) 1 [Bloodfray Giant](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfray%5D+%5BGiant%5D) 1 [Ultimate Price](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUltimate%5D+%5BPrice%5D) 1 [Izzet Keyrune](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BKeyrune%5D) 1 [Street Spasm](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStreet%5D+%5BSpasm%5D)

##### Rare (1)

1 [Nivmagus Elemental](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNivmagus%5D+%5BElemental%5D)

40 Cards

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rakdos+Guildgate)

[Deal Another Hand](https://web.archive.org/web/20121210000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bellows+Lizard)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ultimate+Price)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tower+Drake)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Batterhorn)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dispel)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:23:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Rakdos Guildgate";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bellows Lizard";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Rakdos Cackler";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Nivmagus Elemental";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Nivix Guildmage";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Tower Drake";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Vassal Soul";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Bloodfray Giant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Batterhorn";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Tenement Crasher";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Dispel";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Inaction Injunction";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Pursuit of Flight";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Ultimate Price";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Annihilating Fire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Izzet Keyrune";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Auger Spree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Inspiration";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Street Spasm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Explosive Impact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}}

  

I wanted to both play as much removal as I could and run as aggressive a deck as I could. Because of this, I went with the Izzet side of the pool. It gives you a bunch of removal, especially with the easy black splash. It has a really good set of early game creatures, perfect for complementing the removal and [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift). It has great late-game potential with [Nivix Guildmage](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nivix+Guildmage), two six-drops, and [Cyclonic Rift](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cyclonic+Rift). I made sure to include the Keyrune to help me get to six faster, as well as potentially giving another attacker in a pinch. I chose to leave the [Dynacharge](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dynacharge) in the board since the deck doesn't have a tremendously heavy early game, just one that is good enough to get by.

<table><tbody><tr><td><div><div><img alt="Nivix Guildmage" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Nivix+Guildmage"></div></div></td><td><div><div><img alt="Izzet Keyrune" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Izzet+Keyrune"></div></div></td></tr></tbody></table>

Ultimately, I felt that this version of the deck was much more in line with the way I like to play, and would give me a much better chance against better decks. The potential to interact well at both the early and late stages of the game, as well as the large amount of removal, made me decide that I'd rather play this deck than any of the others. That being said, I was really close to having a red-green deck splashing the [Collective Blessing](https://web.archive.org/web/20121210000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing). As you can see, when a Sealed pool is weaker, there are many more reasonable options than when it is overtly powerful. In powerful pools, many of the decisions are made for you already, and it's simply up to you to fine tune the deck. In bad pools, it's up to you to find the best strategy and decide which lines you are able to cross to give yourself the best chance of winning. I have a really good example of this for a later week that I'll use in a homework, but for now, here's a different set of cards to work with:

[![](https://i.ormos.uk/db/7b/db7b346a572f6abfc2124de8bcbe450278987ac01aa223721834f0c302fbebd3.jpg)](https://web.archive.org/web/20121218100815/http://www.wizards.com/magic/sealeddeckbuilder/index.html?draftid=pop_20121210)

[![](https://i.ormos.uk/2a/7a/2a7aeaff64c1d7acc7979f9abccf68735c2248a25e8558e02a20f16bc81a0408.jpg)](https://web.archive.org/web/20121218100815/http://www.wizards.com/magic/sealeddeckbuilder/index.html?draftid=pop_20121210)

  

There is a lot of mana fixing in this pool, so I'll be interested to see what cards you decide to splash for, if any, and how you support it. Good luck with your builds, and I'll see you next week!