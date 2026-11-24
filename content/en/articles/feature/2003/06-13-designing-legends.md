---
id: wvc8rfpd
kind: article
lang: en
path: /en/articles/feature/2003/06-13-designing-legends
title: Designing Legends
published: '2003-06-13'
column_slug: feature
column: Feature
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    lang_detected: en
    capture_id: 301844
    url: https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    captured_at: '2022-05-26 06:18:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    lang_detected: en
    capture_id: 301844
    url: https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    captured_at: '2022-05-26 06:18:58+00'
    rule: drupal.posted_in_date
  column:
    page_key: magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    lang_detected: en
    capture_id: 301844
    url: https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
    captured_at: '2022-05-26 06:18:58+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-legends-2003-06-13
    lang_detected: en
    capture_id: 720540
    url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-legends-2003-06-13
    captured_at: '2022-01-20 21:13:25+00'
    rule: drupal.div_author
sources:
- document_id: wvc8rfpd
  url: https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
  page_key: magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
  lang: en
  template: drupal
  captured_at: '2022-05-26 06:18:58+00'
  capture_id: 301844
  wayback_url: https://web.archive.org/web/20220526061858id_/https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
- document_id: wvc8rfpd
  url: https://magic.wizards.com/en/articles/archive/latest-developments/designing-legends-2003-06-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/designing-legends-2003-06-13
  lang: en
  template: drupal
  captured_at: '2022-01-20 21:13:25+00'
  capture_id: 720540
  wayback_url: https://web.archive.org/web/20220120211325id_/https://magic.wizards.com/en/articles/archive/latest-developments/designing-legends-2003-06-13
- document_id: wvc8rfpd
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb75
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb75
  lang: en
  template: aspx
  captured_at: '2010-01-24 00:22:43+00'
  capture_id: 805398
  wayback_url: https://web.archive.org/web/20100124002243id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb75
- document_id: wvc8rfpd
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb75,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb75
  lang: en
  template: classic_asp
  captured_at: '2005-02-18 03:08:28+00'
  capture_id: 1992295
  wayback_url: https://web.archive.org/web/20050218030828id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb75,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: wvc8rfpd
  capture_id: 301844
  url: https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
  wayback_url: https://web.archive.org/web/20220526061858id_/https://magic.wizards.com/en/articles/archive/designing-legends-2003-06-13
  captured_at: '2022-05-26 06:18:58+00'
  template: drupal
  sha256: 979a7aab1e2150e96f70e7d40ffbf0e73e6311eb7702fe1f393ba4b0e83df885
render_recovery: []
---
![Designing Legends](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb75_pic1_en.jpg)

The most obvious and important category of top-down design is when you start from some flavorful concept and then try to design a mechanic that gives life to this concept. [Extra Arms](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Extra+Arms) does this quite well, as do [Form of the Dragon](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Form+of+the+Dragon) and [Frozen Solid](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frozen+Solid). However, there’s a whole additional category of top-down design work that gets done for **Magic** cards: Designing Legends. Development teams often find themselves doing this design work themselves so I know a bit about it and in this week’s article I’ll look at the way we designed a few of the Legends in *Scourge*.

The trick to designing and developing a Legend is that you come up with a mechanic that is both cool and true to the story behind the Legend. In other words, you start from the flavor of what the Legend means to **Magic**’s storyline and then try to come up with a card that represents that. (If you’ve been reading along this week you can see immediately why I’m calling this a kind of top-down design.)

### Long Live the King

Once we figured out that the sliver tribe was going to make a comeback in *Legions*, a number of people suggested “You gotta do a Sliver King!” Well having a “king” didn’t really make sense given that the slivers are hive-like and the Queen is in charge, but that didn’t make the idea any less cool. We decided to trust that our creative team would come up with a way to let us do a really big, splashy sliver that cost WUBRG (“Sliver Ancient” was our first thought) and so we proceeded to try to design one.

Design teams usually take the first crack at figuring out what abilities would make sense on our Legends. Their first thought was to have the Sliver Ancient help the slivers share abilities with *all* the creatures in play … so “Slivers gain all abilities of each nonsliver creature in play.” I think they knew this wasn’t going to work because there’s a comment in the file from Worth Wollpert saying “Paul is going to murderize us when he sees this. :)” Rules Manager Paul Barclay did indeed veto this ability as soon as he saw it. Gaining abilities works out fine for most abilities, but the problems start when you look at cards like [Lhurgoyf](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lhurgoyf)s that set the power and toughness of a creature. How big is your [Blade Sliver](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blade+Sliver) if Sliver Ancient is in play alongside a [Nightmare](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) and an [Ancient Ooze](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Ooze)? (Now you start to see you why we need a guy like Paul …)

Anyway, a couple days before the handoff from design to development they changed the Sliver Ancient to give all the abilities from the original *Tempest* Slivers plus an additional ability:

> Slivers get +1/+1 and gain flying, first strike, haste, and 2: regenerate this creature.  
>  Sacrifice CARDNAME: Sliver legends get +13/+13 until end of turn.

That the Sliver King could sacrifice himself to give target Sliver Legend +13/+13 did fit in with the flavor of the Queen being the one who really wears the pants in the Sliver family (that or [Mistform Ultimus](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistform+Ultimus) does) and it was kind of a cute card, but in the end the development team decided it was too narrow and not exciting enough. As I pointed out in an aside a couple of weeks ago, cooler heads prevailed and we realized this card should be more than just a joke that references five-year-old cards.

The next step for the development team was figuring out precisely what the flavor was that we should be attempting to give life to. Since the slivers got into Otaria through the Riptide Project, that’s really where our big splashy WUBRG sliver should come from too. By the time of Scourge, our creative team figured the wizards would be desperately trying to control the sliver infestation they had unleashed on their world so that was the flavor we decided to go for. One designer suggested a [Survival of the Fittest](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest) variant, which the team thought might play well, but then we decided that for WUBRG we didn’t actually need to force players to discard a sliver and so we went with the more powerful version that you see in *Scourge*. And then the Sliver stealing ability seemed like the perfect way to round out the card.

![Sliver Overlord by Tony Szczudlo](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb75_pic3_en.jpg)

### All Things to All Tribes

[Karona, False God](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karona%2C+False+God) was an even better example of the top-down design process that many Legends go through. The creative team told the designers about her and their first attempt was the following:

> \[Charoma, Goddess of Doom\]  
>  6WB  
>  Creature -- Goddess Legend  
>  6/6  
>  Haste, protection from spells and abilities  
>  At the beginning of each player s upkeep, untap CARDNAME and that player gains control of it.  
>  At the beginning of your combat phase, tap each other untapped creature you control and that creature deals damage to you equal to its power.

Note that she’s white-black because she was formed from a bizarre merger between [Akroma](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma) and [Phage](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phage). She’s also a savage, savage beating for your opponents – first she attacks them and then the turn after you play her all of their own creatures attack them too. She shrunk down to 5/5 pretty quickly so she would be quite so much of an “I win” card (especially in Limited), but at the end of our testing we concluded that she still wasn’t all that interesting to play with.

More importantly, the more the creative team filled us in on her story, the worse this mechanic seemed to fit. Every tribe sees her as whatever they most want from a god-figure. So she was supposed to be all things to all people. But all this version did was force creatures to turn on their controllers. That was often part of the results of her influence, but the coolest thing about her was missing. There had to be some way to capture that flavor on a card, especially in a tribal block. We summarized the story and her role in it as best as we could in one email to the designers, and asked them to submit their recommendations. One of the submissions was a “super-lord” where you chose a creature type when she came into play and then that tribe all got +3/+3. It was nice that she could go help out any tribal deck, but the development team thought it would be even cooler if we combined that ability with the “hot potato” vibe from the original design. *Now* we felt we had captured the way in which everybody on Otaria sees her as whatever inspires them to fight.

Meanwhile, we knew she had started out as [Akroma](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma) plus [Phage](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phage), but a black-white mana cost no longer seemed to do her justice; she had evolved into so much more. It’s not like she was only a false god to the black and white tribes, so we changed her mana cost to have all five colors of **Magic** represented.

![Karona, False God by Matthew D. Wilson](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb75_pic2_en.jpg)

I covered the third *Scourge* Legend, [Bladewing the Risen](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bladewing+the+Risen), in a [previous article](https://web.archive.org/web/20030613000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb69). It is interesting to note that Bladewing was not really a top-down card; its Legendary status wasn't added until the card was in development.

Most Legends in **Magic** go through a process pretty similar to the ones that created [Sliver Overlord](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sliver+Overlord) and [Karona](https://web.archive.org/web/20030613000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karona). The design team takes the first crack at them, but then (like all **Magic** cards) the development team has to check them out and make sure they are fun and balanced and sensible. With Legends the difference is that the development team has to pay close attention to the flavor of the card. They are all inherently top-down cards and we have to make sure their mechanic matches their flavor since (unlike most cards) we can’t really change the flavor just to fit a mechanic that we happen to like.