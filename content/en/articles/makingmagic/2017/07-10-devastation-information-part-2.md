---
id: gpr0dcm9
kind: article
lang: en
path: /en/articles/makingmagic/2017/07-10-devastation-information-part-2
title: Devastation Information, Part 2
published: '2017-07-10'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    lang_detected: en
    capture_id: 214873
    url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    captured_at: '2024-05-18 02:48:51+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    lang_detected: en
    capture_id: 214873
    url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    captured_at: '2024-05-18 02:48:51+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    lang_detected: en
    capture_id: 214873
    url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    captured_at: '2024-05-18 02:48:51+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    lang_detected: en
    capture_id: 214873
    url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
    captured_at: '2024-05-18 02:48:51+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: gpr0dcm9
  url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
  page_key: magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:48:51+00'
  capture_id: 214873
  wayback_url: https://web.archive.org/web/20240518024851id_/https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
- document_id: gpr0dcm9
  url: https://magic.wizards.com/en/articles/archive/making-magic/devastation-information-part-2-2017-07-10
  page_key: magic.wizards.com/en/articles/archive/making-magic/devastation-information-part-2-2017-07-10
  lang: en
  template: drupal
  captured_at: '2021-12-09 02:39:37+00'
  capture_id: 875752
  wayback_url: https://web.archive.org/web/20211209023937id_/https://magic.wizards.com/en/articles/archive/making-magic/devastation-information-part-2-2017-07-10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gpr0dcm9
  capture_id: 214873
  url: https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
  wayback_url: https://web.archive.org/web/20240518024851id_/https://magic.wizards.com/en/news/making-magic/devastation-information-part-2-2017-07-10
  captured_at: '2024-05-18 02:48:51+00'
  template: contentful
  sha256: e3754a4866dc78a5d80ba73253828a68514269566bfc7792e7e2ebc2508b2283
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email me
  occurrences: 1
---
[Last week](/en/articles/makingmagic/2017/07-03-devastation-information-part-1), I started my card-by-card design stories of *Hour of Devastation*. I have a lot more stories to get to, so let's get started.

**Dauntless Aven**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dauntless+Aven)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dauntless+Aven)

Most of the time, *Magic* lets you do what you want with your designs. But every once in a while, things that seem like they should work just fine do not. [Dauntless Aven](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dauntless+Aven) is a great example. We make many creatures that have attack triggers—that is, when they attack, they trigger an effect, usually something that feels like a spell. Often attack triggers will grant a creature keyword to another creature, sometimes one that is also attacking, sometimes one that isn't.

It turns out that while this works just fine for most creature keywords, it doesn't work with vigilance. You see, granting vigilance to a creature after attacking has been declared doesn't do anything. Vigilance keeps an attacking creature from tapping, but for the attack trigger to work, the creature with the triggered ability has to attack first, and as all attackers are declared at the same time, that means you've missed the window where granting vigilance will actually allow the creature to both attack and be untapped.

The solution we've come up for this problem is to have the triggered ability untap the creature instead of granting it vigilance. This essentially does what you want granting vigilance to do. This has led to some debate because we've moved untapping creatures mostly out of white into green (note that blue can still "twiddle" creatures—aka tap or untap). We've talked about restricting it to "target attacking creature," but in the end decided it wasn't worth the extra text. White can get a little bit of conditional untapping where most of the time it will just be making creatures feel like they have vigilance.

* * *

**Cycling Deserts**

*   [![Desert of the True](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desert+of+the+True)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+of+the+True)
*   [![Desert of the Mindful](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desert+of+the+Mindful)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+of+the+Mindful)
*   [![Desert of the Glorified](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desert+of+the+Glorified)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+of+the+Glorified)
*   [![Desert of the Fervent](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desert+of+the+Fervent)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+of+the+Fervent)
*   [![Desert of the Indomitable](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Desert+of+the+Indomitable)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+of+the+Indomitable)

For this cycle, I want to talk about a common design phenomenon. When you create cards for something that's already been designed before, whether you realize it or not, that previous design tends to taint how you think about your new design. The case in point is this Desert cycle. In *Arabian Nights*, Richard Garfield made a card called [Desert](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=287341).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=986)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=986)

In my *Amonkhet* design article, I talked about how we considered bringing back [Desert](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=287341) but ended up deciding against it because we didn't like what it did to the environment (making low-toughness creatures harder to play). As such, we decided to design new Deserts. I gave no parameters to the designers; I just asked for top-down desert designs. Interestingly, the first batch all tapped for colorless mana.

It makes sense. You tend to think of a desert as being a place devoid of resources, so at first blush, it doesn't necessarily seem like a place you'd find colored mana. I don't though think the designers went through that thought process, though. I think they were copying off what we did before and the Desert we made before tapped for colorless mana.

The insidious thing about this (it happens quite a lot in design) is that no one sets out to give themselves the design restriction. It's just that the first person to design it made a decision that felt sensible, and that stake in the mental design space just shifts how you think about it.

To the best of my memory, this cycle wasn't designed until *Hour of Devastation*. And I think it was done during a Desert mini-team, which had been assigned the task of designing more Deserts. It wasn't until then that someone asked the question, "Do Deserts have to tap for colorless mana?" And the answer was no, there was no requirement.

The cool thing about this cycle is that it gets to show off an important part of the set. The Hekma, the protective barrier, has fallen and now the desert is encroaching into the city. By using lands with colored mana, we get to better convey that the city has fallen to the ravages of the desert. Without the colored mana, it would be harder to convey the sense that something once thriving has become a desert. And this all came about because someone was able to look past what has been done to see what could be done.

* * *

**Fraying Sanity, Overwhelming Splendor, and Torment of Scarabs**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fraying+Sanity)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fraying+Sanity)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Overwhelming+Splendor)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Splendor)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Torment+of+Scarabs)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torment+of+Scarabs)

I talk often about things being evergreen. Evergreen keywords and abilities are things we do (almost) every set. They are part of the basic tools of *Magic* design. The next group is the deciduous mechanics. These are tools in our tool box that we as designers can use whenever we wish, but there's no expectation that it will show up frequently. Hybrid mana and double-faced cards are good examples of deciduous things. We can use them when they help us accomplish something but have no need to stick them places where they aren't helpful.

Curses have become deciduous. They started in *Innistrad* as a minor component of the set, playing into the Gothic horror theme. We then continued them into *Dark Ascension*. The *Commander (2013 Edition)* design team found a use for them and so designed some new Curses. Then when we returned to Innistrad in *Shadows over Innistrad*, we included one on the double-sided card [Accursed Witch](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accursed+Witch)/[Infectious Curse](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Curse). Then came *Amonkhet* with its Egyptian theme and Curses also felt at home. Because we were avoiding doing too much "dead and dusty" tomb raider–ish tropes, we only printed two. *Hour of Devastation* continues this trend by including three more, all of which were designed to play into the "disaster movie" feel of the set—the Curse causes a snowballing effect, pushing you closer and closer to defeat.

* * *

**God-Pharaoh's Gift**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=God-Pharaoh%27s+Gift)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=God-Pharaoh%27s+Gift)

One of the themes of *Hour of Devastation* is that things are not what they seemed. Nicol Bolas made a lot of promises to the people of Naktamun, and he delivered them, but not quite in the way they expected. For instance, the people knew that something big happened when the dead crossed through the [Gate to the Afterlife](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife). Rather than a glorious afterlife though, the dead get to become part of Bolas's giant Zombie army.

To capture this reveal, we made what we call a "throw forward" in *Amonkhet* with this card:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gate+to+the+Afterlife)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife)

A throw-forward is a card that references another card that doesn't yet exist, leaving the players to speculate what this other card might do. The parallel, in this case, is that the people of Naktamun were doing the exact same thing with the [Gate to the Afterlife](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife) as the players were, trying to imagine what reward awaits the victors of the Trials who pass through the gate.

[God-Pharaoh's Gift](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=God-Pharaoh%27s+Gift) was designed top-down to represent Bolas turning the dead into Eternals. The artifact does exactly that, essentially granting the eternalize mechanic to any creature, turning them into an Eternal. The two cards combo nicely together as the [Gate to the Afterlife](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife) allows you to bypass the higher mana cost of [God-Pharaoh's Gift](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=God-Pharaoh%27s+Gift) (for example, this allows you to get it out turn four with a good draw).

We've made a few lackluster throw-forward cards in the past, but I'm hoping this one actually inspires some deck designs.

* * *

**Hazoret's Undying Fury**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hazoret%27s+Undying+Fury)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazoret%27s+Undying+Fury)

I often talk about how *Magic* is not one game, but actually many games united through a shared collection of cards and a rules system. This diversification of games, also known as formats, requires R&D to challenge itself to find ways to push colors in new directions to allow them to better play in particular formats. For [Hazoret's Undying Fury](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazoret%27s+Undying+Fury) we were looking at the more casual formats, Commander in particular. Red was initially designed very much with two-player play in mind. Red is the short-term advantage color that throws away long-term gain for short-term accomplishments, but this becomes problematic in formats where short-term strategies are mostly ineffective.

We've spent a lot of time trying to figure out how to give red things that will play better in longer multiplayer games. We want to do this though in a way that feels red, that plays into red's philosophy rather than making it play more like another color. [Hazoret's Undying Fury](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazoret%27s+Undying+Fury) has us playing around with the concept of chaos. Red, as white's foil, is the color of chaos, so we've been trying to find ways to allow it to do things that can have big—but often unknown—effects.

This card plays into the space of giving red some late-game card advantage without it losing its unpredictable nature. Back red into a corner and fireworks can happen, but not something carefully planned out because that simply isn't red's way.

* * *

**Hollow One**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hollow+One)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+One)

This is the fifth time we have used the cycling mechanic in a tournament-legal block (*Urza's* block, *Onslaught* block, *Time Spiral* block, *Shards of Alara* block, and *Amonkhet* block). After so many uses, you'd think we'd have trouble finding new variants, but I love how we always find new pockets to explore. [Hollow One](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+One) is a perfect example. We do cost-reduction mechanics all the time, but we've never crossed it with cycling before. Okay, we did once on a card called [Fluctuator](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=5806) from *Urza's Saga*, but that reduced the cost of cycling, not vice versa.

[Hollow One](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+One) actually does something a little different than most cost-reduction cards. Cycling (mostly) costs mana to use, so it's not that you're going to cast [Hollow One](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+One) all that often without access to five mana, but the reduction allows you to essentially apply the mana you use for cycling to also pay for [Hollow One](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hollow+One). It's just a very different way to make use of cycling, one I'm happy we found five times in.

* * *

**The Hour Cycle**

The Hour cycle is a first: a story spotlight cycle. The five main parts of the story are told through a single rare cycle. The people of Naktamun were taught that if they worked hard and sacrificed, it would eventually lead to Bolas's return to Amonkhet. On that day, it was foretold that five things would happen. This cycle covers those five things and shows that while Bolas lives up to the letter of the law, he doesn't always live up to its spirit. Note that the sequence of the hours matches neither *Magic*'s traditional color order (white, blue, black, red, green) nor the order of the Trials (white, blue, green, black, red). Instead it is white, black, green, blue, red.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hour+of+Revelation)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hour+of+Revelation)

**Hour of Revelation** – When the second sun comes to rest before Bolas's horns, the Hour of Revelation shall begin. It starts the [Gate to the Afterlife](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife) opening. That is when the horror begins. Most sets have a white mass-destruction spell, and as the Hour of Revelation is the start of the city's destruction, it felt like the perfect place for a board wipe. To give it a bit different of a feel, we put on a cost-reduction rider. If the world is filled with enough people, the destruction comes a bit easier.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hour+of+Glory)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hour+of+Glory)

**Hour of Glory** – The first of Bolas's Gods to arrive is The Scorpion God. He comes and kills all the monocolor Gods, other than Hazoret who manages to escape. Watching your mostly benevolent Gods slaughtered in front of you by another God is pretty terrifying. Mechanically, we knew we wanted this to be a kill spell. We gave it a God rider so that if it kills a God, it removes any copies from the hand.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hour+of+Promise)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hour+of+Promise)

**Hour of Promise** – Next up is The Locust God that unleashes a horde of locusts that eat through the Hekma. You know, the protective barrier keeping the desert and all the dangerous monsters out. As this is the story point where the desert and Zombies start encroaching on the city, we liked making it a Desert enabler that helps you get Zombie tokens. Green naturally does land-fetching and token-making, so this felt like a good fit.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hour+of+Eternity)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hour+of+Eternity)

**Hour of Eternity** – The Scarab God then arrives and reanimates all the Eternals from the necropolis. The supposed reward of the Trials was a glorious afterlife, so finding out your friends and loved ones have become part of a giant Zombie army, one currently attacking you, is a bit of a rough discovery. To capture the reanimation of the Eternals, the card lets you "Eternalize" as many creatures as you're able to pay for/have in your graveyard. (Note the card mimics eternalize without technically granting the ability to your dead creatures.) Blue is not traditionally a reanimation color, but in this set it is one of the eternalize colors, so we felt it was an acceptable bend.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hour+of+Devastation)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hour+of+Devastation)

**Hour of Devastation** – Finally we get to the Hour the set is named after. This is when Bolas himself shows up and we get the final showdown between Bolas and the Gatewatch. As the defeat cycle demonstrates, this goes very poorly for the Gatewatch. Because we wanted the card to be destructive and hit the story point, the damage hits not just creatures but all planeswalkers other than Bolas.

We're still experimenting with how we want to use the story spotlight cards, but I like how *Hour of Devastation* uses them in a brand-new way.

* * *

**Pain Deserts**

*   [![Shefet Dunes](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shefet+Dunes)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shefet+Dunes)
*   [![Ipnu Rivulet](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ipnu+Rivulet)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ipnu+Rivulet)
*   [![Ifnir Deadlands](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ifnir+Deadlands)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ifnir+Deadlands)
*   [![Ramunap Ruins](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ramunap+Ruins)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ramunap+Ruins)
*   [![Hashep Oasis](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hashep+Oasis)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hashep+Oasis)

In *Amonkhet* design, we played around a little with Desert synergy before ultimately deciding to leave most of it to *Hour of Devastation*. One thing we tried was having every Desert that sacrificed itself for effect sacrifice a Desert rather than just sacrifice itself. It was a way to make "Desert tribal" without putting a lot of extra words on cards. And then we playtested it.

And it ended up being pretty loud (R&D slang for heavily encouraging players to pay attention to it) and pretty powerful. It also had a side effect of pushing players into stretching how many colorless lands they'd play (as all our deserts at the time produced colorless mana (see the cycling Deserts above). We realized that we had to be careful how much "sacrifice a Desert" we used.

When this cycle got designed, we were playing around with the idea of having colored activations for sacrifices. (I believe this predated Deserts tapping for colored mana.) We knew we wanted a little "sacrifice a Desert" in *Hour of Devastation*, and we liked how this cycle's color requirement would work to keep too many of the cycle from ending up in the same deck. And that is how this cycle ended up being the only "sacrifice a Desert" lands in the set.

* * *

**Khenra Eternal**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Khenra+Eternal)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Khenra+Eternal)

As a historian of *Magic*, I find it interesting to follow certain threads to watch how things have changed over time. [Khenra Eternal](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Khenra+Eternal) is a good example of the latest in a line of cards I call the "[Scathe Zombies](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scathe+Zombies)." The line begins obviously with its namesake, [Scathe Zombies](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scathe+Zombies), in *Limited Edition (Alpha)* way back in 1993.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=81)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=81)

At the time, only green had a 2/2 vanilla creature (a creature with zero rules text) for two mana, [Grizzly Bears](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). For black (as well as white and red) it cost three mana. Flash forward seven years to the set *Nemesis* (from 2000).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=21310)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=21310)

Finally, black could have a 2/2 creature. It just couldn't block. In the very next set, *Prophecy*, black got another 2/2 for 1B.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=24603)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=24603)

This time it came with the drawback of having to pay an upkeep of B every turn. The next evolution didn't happen for eleven years: in *Innistrad* from 2011, we printed [Walking Corpse](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=413376)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=413376)

This was considered controversial at the time. R&D had hours and hours of arguments about it, but in the end we decided that the creature curve had evolved enough over the years that a vanilla 2/2 for 1B was allowable. The creature was repeated, albeit with a new name ([Gutter Skulk](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gutter+Skulk)) and extra creature type (Rat) in *Gatecrash* two years later. Which brings us to *Amonkhet*.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Miasmic+Mummy)](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Miasmic+Mummy)

For the first time, black gets a 2/2 with an ability that isn't a complete drawback. [Khenra Eternal](https://web.archive.org/web/20170710000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Khenra+Eternal) takes it a step further to be the first 1B 2/2 with an upside. This might not be the kind of thing most people get excited about, but it's interesting to me.

# The Twilight *Hour*

That's all the time we have for today. I hope you're enjoying all the stories. As always, I'm curious on any feedback on either today's column or *Hour of Devastation* itself. You can email me or talk to me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro)).

Join me next week for Part 3**.**

Until then, may you devastate an opponent or two.

* * *

 

##### #450: R&D Wave Three

##### #450: R&D Wave Three

38:26

From time to time, I dedicate a show to talking about the many people who have worked on *Magic*. In this podcast, I'm talking again about R&D—this time covering the group I dub the "third wave."

[Download MP3 Format](http://media.wizards.com/2017/podcasts/magic/drivetowork450_rndwavethree.mp3)

 

##### #451: Becoming a Game Designer

##### #451: Becoming a Game Designer

38:38

One of the questions I get most often is "How can I become a game designer?" I answer that question in this podcast.

[Download MP3 Format](http://media.wizards.com/2017/podcasts/magic/drivetowork451_becomingagamedesigner.mp3)

*   [**Episode 449**](http://media.wizards.com/2017/podcasts/magic/drivetowork449_counters.mp3) Counters (30.1 MB)
*   [**Episode 448**](http://media.wizards.com/2017/podcasts/magic/drivetowork448_otherwizardsgames_pt-2.mp3) Other Wizards Games, Part 2 (24.2 MB)
*   [**Episode 447**](http://media.wizards.com/2017/podcasts/magic/drivetowork447_otherwizardsgames_pt-1.mp3) Other Wizards Games (26.5 MB)