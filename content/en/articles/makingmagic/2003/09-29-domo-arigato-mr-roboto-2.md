---
id: xcjv19h7
kind: article
lang: en
path: /en/articles/makingmagic/2003/09-29-domo-arigato-mr-roboto-2
title: Domo Arigato, Mr. Roboto
published: '2003-09-29'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    lang_detected: en
    capture_id: 215011
    url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    captured_at: '2024-04-29 02:56:25+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    lang_detected: en
    capture_id: 215011
    url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    captured_at: '2024-04-29 02:56:25+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    lang_detected: en
    capture_id: 215011
    url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    captured_at: '2024-04-29 02:56:25+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    lang_detected: en
    capture_id: 215011
    url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
    captured_at: '2024-04-29 02:56:25+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: xcjv19h7
  url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
  page_key: magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
  lang: en
  template: contentful
  captured_at: '2024-04-29 02:56:25+00'
  capture_id: 215011
  wayback_url: https://web.archive.org/web/20240429025625id_/https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
- document_id: xcjv19h7
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr91
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr91
  lang: en
  template: aspx
  captured_at: '2009-06-04 14:58:52+00'
  capture_id: 804427
  wayback_url: https://web.archive.org/web/20090604145852id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr91
- document_id: xcjv19h7
  url: https://magic.wizards.com/en/articles/archive/making-magic/domo-arigato-mr-roboto-2003-09-29
  page_key: magic.wizards.com/en/articles/archive/making-magic/domo-arigato-mr-roboto-2003-09-29
  lang: en
  template: drupal
  captured_at: '2022-01-26 22:40:03+00'
  capture_id: 877187
  wayback_url: https://web.archive.org/web/20220126224003id_/https://magic.wizards.com/en/articles/archive/making-magic/domo-arigato-mr-roboto-2003-09-29
- document_id: xcjv19h7
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr91
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr91
  lang: en
  template: classic_asp
  captured_at: '2005-06-04 07:57:09+00'
  capture_id: 1982554
  wayback_url: https://web.archive.org/web/20050604075709id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr91
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: xcjv19h7
  capture_id: 215011
  url: https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
  wayback_url: https://web.archive.org/web/20240429025625id_/https://magic.wizards.com/en/news/making-magic/domo-arigato-mr-roboto-2003-09-29
  captured_at: '2024-04-29 02:56:25+00'
  template: contentful
  sha256: 155659e41320a7f46579813a9f6f91fcdd452f5444028824b446f2f467113746
render_recovery: []
---
Welcome to Artifact Creature Week! In honor of *Mirrodin*'s release, we're going to spend this week talking about colorless creatures (and I don't mean animated lands). Since I have the honor of writing the design column, I thought I'd use "Making Magic" this week to discuss the challenges of designing artifact creatures (and artifacts in general) and then take a look at the design of a few of the artifact creatures in *Mirrodin*.

### There's No Place Like Gnome

I guess I should start by letting you in on a trade secret. Designing good artifacts is very, very hard. Why? A number of reasons:

**1) Artifacts Don't Play Nice With The Color Wheel** - The most important aspect of artifacts comes from what they aren't. And by that, I mean colored. I've spent numerous columns explaining how crucial the color wheel is to **Magic**. Artifacts throw a giant monkey wrench into the works. The color wheel had a little party and artifacts simply weren't invited.

![Howling Mine](https://i.ormos.uk/18/07/1807a258af4d8f853c97ccbb184a42906811abe9c60f8fd6d872e768bf336406.jpg)

This isn't to say that R&D hasn't tried to fit artifacts into the color wheel. We've even managed to keep a few abilities (milling, [howling mine](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=howling+mine) effects, etc.) relegated to primarily artifacts. But it's a square peg and a round hole. Artifacts are defined by their ability to do anything. Their colorlessness is their freedom. To quote an old (and I do mean old) Saturday Night Live sketch: "It's a curse and a blessing".

The blessing is that artifacts have very little limitations. The curse is that artifacts have very little limitations. As I've explained in my column on numerous occasions, restrictions breed creativity. Having a wide open field is rather daunting.

In addition, although artifacts don't make great use of the color wheel, they still have to be kept from stepping on its toes. This has lead R&D to make a global rule concerning artifacts: artifacts cannot do anything better than the worse color at that ability. For example, an artifact with creature destruction should not be good enough that every green deck uses it.

To be fair, R&D is a little flexible with this rule (such as when half the set is artifacts), but the general spirit looms over every design. This problem is especially present in artifact creatures. Blue's creatures, for example, are clearly several notches below colors like green and white. And artifact creatures aren't supposed to exceed blue's.

So, what is a designer to do? The key rests in being extra creative. The best way to keep from usurping colored abilities is to find offbeat abilities that don't obviously translate into a particular color. This isn't easy. Thus the "very, very hard" line from above.

**2) Artifacts Are Victims of Flavor** - I believe a key factor that players like about artifacts is that they are conceptually very logical. They're things. They're magical items. They make sense. This puts an interesting constraint on design. In order for an artifact to "feel" right, it has to have clear connection between what its flavor and its mechanic. Enchantments? Whatever. They're magic. They're made up anyway. Players don't have any expectations. But artifacts? Artifacts are real, so they better damn make sense.

This isn't to say that every artifact makes perfect sense (what's a [howling mine](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=howling+mine) exactly?), but that the best artifacts are the ones that have a consistent logic. I'm sure this isn't something most players think about, but it's an important part of what makes artifacts tick design-wise. And once again, doing this properly is "very, very hard".

**3) Artifacts Have a "Wacky" Rep** - Because of Reason #1, designers have gone out of their way to be more inventive with the kinds of effects players see on artifacts. Combine this with the fact that artifacts skew towards rare (common artifacts don't exist in most sets and uncommon artifacts tend to be utility-based) and you create a self-fulfilling prophecy where artifacts are "weirder" than normal cards.

To combat this in *Mirrodin*, we purposefully dropped the rarity threshold on artifacts. In English, this means we put things that would normally be uncommon at common, normally rare at uncommon, and left extra complicated at rare. This is why, for example, uncommon artifacts in *Mirrodin* might seem like rare artifacts that you might find in a normal set. This expectation towards odder effects is yet more pressure that complicates artifact design.

**4) *Mirrodin* Is Half Artifact** - The design team felt strongly that *Mirrodin* had to have a high number of artifact cards to create the environment we wanted. An average set might have forty artifacts in it (and I'm not talking about the skimpy artifact levels of the last few years). *Mirrodin* has over one hundred sixty! It has the equivalent of four sets worth of artifacts. That's a lot of artifacts to design.

In fact, there was some (not me) in R&D who didn't believe we could create that many interesting artifacts. As you can see, we proved them wrong. (At least, I sure hope we have.)

**5) Artifact Creatures Have Any More Limitations** - Of all the card types, R&D creates more creatures than any other. As such, creatures are better spelled out than any other card type. This makes artifact creature design even harder because there's less virgin design space to explore.

Luckily, the designers love a good challenge. And with *Mirrodin*, we had our hands full.

### Creature Features

But enough of my yapping, let's get to the design stories. How did some of *Mirrodin*'s artifact creatures come into being?

[Bosh, Iron Golem](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bosh%2C+Iron+Golem) - Normally, the creative team lets the design team know what legends are needed for the story. Using the information provided, the design team designs cards to fit the flavor. Bosh was pretty straight-forward. He was a bad-ass golem that liked to destroy artifacts. The designers and developers tried a number of different ideas. In the end, the development team took an ability that the design team had turned in on a rare red "monkey" (you see, in the **Magic** universe monkeys, for some reason, really hate artifacts). Because this grab and fling flavor felt very red, the card was given a red activation.

[Clockwork Dragon](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clockwork+Dragon) - When *Alpha* first came out, there was no pre-built community to absorb and figure out the cards (plus the Internet was still in its early stages). As such, some of the "hot" cards in early **Magic** had a lot more to do with splash value than play value. One such card was [Clockwork Beast](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clockwork+Beast). If you wanted a [Clockwork Beast](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clockwork+Beast) (or [The Hive](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Hive) oddly enough) you had to crack one open in a booster pack because no one was going to be crazy enough to trade it to you.

Pulling this info from my past, I knew *Mirrodin* was going to have some clockwork creatures (although notice that the mechanic has been updated to use +1/+1 counters). Of course, this meant we had to have a rare clockwork creature. And when you think of rare creatures, you think of dragons. Thus, the [Clockwork Dragon](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clockwork+Dragon) was born. I also liked that the signature dragon of the set would be an artifact dragon.

[Copper Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Copper+Myr), [Gold Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gold+Myr), [Iron Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Iron+Myr), [Leaden Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaden+Myr), [Silver Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silver+Myr) - This cycle was created very early in the *Mirrodin* design. Since that time, nothing about the cards has changed. Well, okay, they did go from being gnomes to being myr but everything else from the mana cost to the ability to the power/toughness was there from practically day one.

[Duplicant](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duplicant) - This card was created during development. A number of players on the Internet have wished that it could copy the entire creature instead of just the power, toughness, and creature type. Well, the card used to do exactly that. This was what the development team had in mind when they created it. But the rules couldn't support the mechanic (go look up the ruling on [Vesuvan Doppelganger](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuvan+Doppelganger) if you want to see why) so the change was made very late in development.

[Frogmite](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frogmite) & [Myr Enforcer](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Myr+Enforcer) - I created these guys during the first batch of affinity cards. They went in the file and never changed. I knew I wanted some artifacts with affinity - artifacts because it was the only way to make cards that could potentially cost nothing. By the way, these guys are very good. Definitely check them out because I believe you'll see them in tournament play.

[Goblin War Wagon](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+War+Wagon) - This card is a nod to the *Arabian Nights* card [Brass Man](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brass+Man). There was some discussion whether we wanted to use the word Goblin on an artifact as the word makes a title sound red.

[Leveler](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leveler) - This card started because I wanted a 10/10 artifact creature for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif). Why? I don't know. Because it just seemed cool. But to do this, I knew I needed a drawback. And not some wimpy drawback. A real drawback. But I wanted something simple. Removing your library from the game came pretty quickly for some reason. Also, like the myr cycle, this card was published exactly as it was created in early design.

[Lodestone Myr](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lodestone+Myr) - This card (known as Magnetron in design) was inspired by the *Tempest* card [Telethopter](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Telethopter) (designed interestingly by my dad, Gene). I liked the idea of other artifacts being a resource for this card. During design we limited the artifacts to non-equipment artifacts because it was confusing when they were tapped or untapped (players tend to treat them like creature enchantments and tap them along with the creature). Development thought this was clunky (and unnecessarily weaker) and changed the activation back to any artifact.

[Myr Mindservant](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Myr+Mindservant) - Several people on the boards have asked why this guy doesn't let you shuffle your opponent's library. That way, they say it could combo with [Psychogenic Probe](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychogenic+Probe). The answer is that it used to and I convinced the development team to change it. You see, back in *Alliances* (during my first development team) I designed [Soldier of Fortune](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soldier+of+Fortune) (at least I believe I did - I'm sure one of the *Alliances*' designers will write to me if I'm remembering this wrong). I've always considered it to be a mistake. Forcing your opponent to continually shuffling is annoying (and mean). I don't mind cards that do it once in the process of achieving some effect, but as a repeatable effect it's simply rude. You want to shuffle your own library for some tactical advantage? Fine. You want to continually shuffle your opponent's library? Sorry. As far as I'm concerned it should be off-limits.

[Pentavus](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pentavus) - The design team originally thought about putting Tetravus in the set (afterall, [Triskleion](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triskleion) and [Tetravus](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tetravus) have always been a pair in my mind), but the card had a few too many clunky elements (you did know that you can't enchant a tetravite token?) so we redesigned it. To change things up we changed it to five +1/+1 counters. The name was the logical response.

[Platinum Angel](https://web.archive.org/web/20030929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel) - I just wanted to give credit where credit are due. The design team did not make this card. It was created by the development team (Brandon Bozzi, Randy Buehler, Elaine Chase, Brian Schneider, Henry Stern, and Brian Tinsman). I think it turned out great and I just wanted to give props for a job well done.

### If You Build Them…

I hope today's column has given you a better insight into the design of artifact creatures. As you can see, they're a little harder to create than one might first imagine.

Join me next week when I continue my trek behind the scenes of *Mirrodin* design.

Until then, may your myr army overrun your opponent.

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*