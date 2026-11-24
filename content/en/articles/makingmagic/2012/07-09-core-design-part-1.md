---
id: da65kpvw
kind: article
lang: en
path: /en/articles/makingmagic/2012/07-09-core-design-part-1
title: Core Design, Part 1
published: '2012-07-09'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    lang_detected: en
    capture_id: 872171
    url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    captured_at: '2022-09-26 20:01:39+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    lang_detected: en
    capture_id: 872171
    url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    captured_at: '2022-09-26 20:01:39+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    lang_detected: en
    capture_id: 872171
    url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    captured_at: '2022-09-26 20:01:39+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    lang_detected: en
    capture_id: 872171
    url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
    captured_at: '2022-09-26 20:01:39+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: da65kpvw
  url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
  page_key: magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
  lang: en
  template: drupal
  captured_at: '2022-09-26 20:01:39+00'
  capture_id: 872171
  wayback_url: https://web.archive.org/web/20220926200139id_/https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
- document_id: da65kpvw
  url: https://magic.wizards.com/en/articles/archive/feature/core-design-part-1-2012-07-09
  page_key: magic.wizards.com/en/articles/archive/feature/core-design-part-1-2012-07-09
  lang: en
  template: drupal
  captured_at: '2022-07-02 09:39:34+00'
  capture_id: 616373
  wayback_url: https://web.archive.org/web/20220702093934id_/https://magic.wizards.com/en/articles/archive/feature/core-design-part-1-2012-07-09
- document_id: da65kpvw
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/203
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/203
  lang: en
  template: aspx
  captured_at: '2013-06-29 11:58:11+00'
  capture_id: 645565
  wayback_url: https://web.archive.org/web/20130629115811id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/203
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: da65kpvw
  capture_id: 872171
  url: https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
  wayback_url: https://web.archive.org/web/20220926200139id_/https://magic.wizards.com/en/articles/archive/making-magic/core-design-part-1-2012-07-06
  captured_at: '2022-09-26 20:01:39+00'
  template: drupal
  sha256: 665193873882d464791f48b7c1979bd2dbe096ba5737187bbc1749bb50cd554c
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
From time to time, I like to do mailbag columns where I answer all of your questions. For the last few years, I've been shaking up the mailbag columns by adding themes to them. As ***Magic** 2013* just came out, I thought I'd restrict this mailbag column to questions about the design of ***Magic** 2013*.

![](https://i.ormos.uk/a3/6d/a36dd10d2c3fc276be174ee8eddec1746517762f6258fef0edb23b0930f59dda.jpg)

[Nefarox, Overlord of Grixis](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nefarox%2C+Overlord+of+Grixis) | Art by [Aleksi Bricolt](https://web.archive.org/web/20120709000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Aleksi%20Bricolt%22%5D)

As I've done the last two years, to get my questions I turned to my [Twitter](https://twitter.com/maro254) feed. Here's what I asked for:

> ![](https://i.ormos.uk/70/bc/70bc85fd3464f22128ee2186db536381ee5631b92efe94b6d90afc6dca487737.jpg)
> 
> [maro254](http://www.twitter.com/maro254) I'm doing a mailbag column about ***Magic** 2013*. Help me by asking design-oriented ***Magic** 2013* questions. Single tweet per question. Thanks.

I got a bunch of good questions, so I decided to turn this into a two-parter. Let's get started.

> ![](https://i.ormos.uk/30/fc/30fcbd17488cf850465ca91c3fb12ba81c0bcd2547affb67027e7bd16955a3c0.jpg)
> 
> [FearsomeCritter](http://www.twitter.com/FearsomeCritter) @maro254 Don't know if this is design: did anyone push for legend rule reminder text? Are you concerned about it?

I'm sure it was talked about, but the fact that the cards are rare and the rule only comes up when you have at least two of them in your deck, we decided that it wasn't something beginning players were going to run into much.

> ![](https://i.ormos.uk/2e/03/2e038dc5c7c7c6c3cae7d34f29e82f4d93b52165c53522e101a0490be07a7218.jpg)
> 
> [SweetoothTKC](http://www.twitter.com/SweetoothTKC) @maro254 What new design space did you explore with exalted in M13?

The goal of bringing back mechanics in the core sets isn't about expanding the design space. In fact, one of our goals in bringing back mechanics is about finding the simplest versions to help give some flavor to the core set without raising complexity too much.

To answer the question, the biggest design space we explored was putting the mechanic into a color that it had never been before, black.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nefarox%2C+Overlord+of+Grixis"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Nefarox%2C+Overlord+of+Grixis"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Servant+of+Nefarox"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Servant+of+Nefarox"></a></div></div></td></tr></tbody></table>

> ![](https://i.ormos.uk/a1/c0/a1c0a695cb9006d26d58e1366cb46c9216edfe6eee863b68deef56eb9ae25f9e.jpg)
> 
> [spaceyjdjames](http://www.twitter.com/spaceyjdjames) @maro254 How does design choose a returning mechanic for a core set?

A nice follow-up to the last question.

There are several things we look for in a returning core mechanic:

> *   It has to be easy to grasp. If a player cannot read the text once and understands what it does (not necessarily how you strategically would use it), it's not a good core mechanic.
> *   The mechanic has to be something that can be done on relatively straightforward cards. While we will make new cards with the mechanic, as I explained above we tend not to explore new design space with it.
> *   Having flavor helps, as the core sets cares more about resonance.
> *   It has to be something we're not planning to repeat in an expert expansion any time soon. As we now return a mechanic every block, we want to make sure not to use something in a core set that we might want to use in an upcoming block. (Expert expansions have more restrictions and thus get first pick of returning mechanics.)

Those guidelines tend to reduce the available mechanics to a small list.

> ![](https://i.ormos.uk/6c/1b/6c1b1b6348dbd9c381528b9fbe8fddb50165807d42c8bfb4a4d85fd8afe28465.jpg)
> 
> [wbyeast](http://www.twitter.com/wbyeast) @maro254 M13 mechanics look advanced compared to other sets. How will we teach noobs with such complex cards?

I feel we've shifted our thinking about the core set over the last five years (since the design of ***Magic** 2010*). While simplicity is still valued, it is not the prime goal that it once was when we defined the core set as the entry point into **Magic**.

We now believe that **Duels of the Planeswalkers** is the best entry point and it leads into the core set. This means the core set is less about being as simple as possible and more about showing off what **Magic** has to offer (while still not overwhelming the newer player). That's why we're playing up resonance, showing off more of the Multiverse, bringing back popular reprints, and including a returning rotating mechanic.

![](https://i.ormos.uk/b5/c7/b5c76384d26147894eb7fc25b0ba1a474990592375b6af80c79ecbdee49bfdab.jpg)

[Battle of Wits](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits) | Art by [Jason Chan](https://web.archive.org/web/20120709000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Jason%20Chan%22%5D)

> ![](https://i.ormos.uk/61/5e/615e0a97b1446d90435193ebcdeed1da4fa9387ecd7bd7790e4463a00cdc87c5.jpg)
> 
> [EdGuise88](http://www.twitter.com/EdGuise88) @maro254 Knowing Titans were leaving this time, how did you go about looking to replace the cycle? Did you know what you wanted instead?

What we wanted most was "not a cycle." We wanted a bunch of independently exciting mythic rares but ones that each stood on their own.

> ![](https://i.ormos.uk/44/11/44118978e60a08a8e9979cf82169b3504f45aa7e43c42d6e6ca4700e444dbf12.jpg)
> 
> [Moshne](http://www.twitter.com/Moshne) @maro254 How important to you is bridging the two adjoining blocks together with the core and what cards were designed for it?

A big part of the core set design and development these days is making sure that the set both introduces things to send off last year's block with a bang (for example, allowing [Rancor](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor) to interact with infect) and sets up the next year's block (for example—oh, I can't tell you this one).

> ![](https://i.ormos.uk/af/e7/afe71d51d32178fcb8b44a8c2c68b82f563554094a1ee6be896c56f5bbcc6c02.jpg)
> 
> [gray\_embrace](http://www.twitter.com/gray_embrace) @maro254 What's the reasoning behind reprinting many of these "casual rares" like Door to Nowhere and [Battle of Wits](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits) in M13?
> 
> <table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Door+to+Nothingness"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Door+to+Nothingness"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Battle+of+Wits"></a></div></div></td></tr></tbody></table>

The existence of a lot of casual players who we believe will enjoy them.

> ![](https://i.ormos.uk/6c/9a/6c9a00e7a04ebc282cb84757d585a92c0429725ed57fea8c770033a11e40a0c3.jpg)
> 
> [epramono](http://www.twitter.com/epramono) @maro254 How do reprinted cards influence the overall design of the set? Do they get picked first or last? Are they based on flavors?

Reprints work very differently in a core set than they do in an expert expansion. One of the identities of the core set is a place where we can bring back reprints we think the audience wants to play again (in Standard, as they're still playable in older formats). Because of this, the structure of core sets is much more flexible, allowing a wider range of reprints.

The biggest issue with reprints in a core set is making sure they are okay in the various metagames that will use them. In an expert expansion, there is much more of a need to fit into the themes of the block, but the core set is dialed down a bit thematically.

![](https://i.ormos.uk/be/6d/be6d31d926bfd7fab13ecda69f930bc3edac502940233b49988ccf5cc71a5411.jpg)

[Clone](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone) | Art by [Kev Walker](https://web.archive.org/web/20120709000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Kev%20Walker%22%5D)

> ![](https://i.ormos.uk/6d/52/6d5287e81488377ee4f19dd31c7c1ad9a53f8f8209bcd2fd068a13db26100433.jpg)
> 
> [Spencer\_AZ](http://www.twitter.com/Spencer_AZ) @maro254 Does design decide how many, and which, reprints are in each core set?

Design will put the reprints it wants into the design file it hands off. Development will make changes, like every **Magic** file, and some of those changes will be swapping what reprints are in the set. Reprints are a combination of both design and development.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Clone"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jayemdae+Tome"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Jayemdae+Tome"></a></div></div></td></tr></tbody></table>

> ![](https://i.ormos.uk/d9/20/d92007445fd79a50d2133d7115648512dd31354f91460f41b8a6208fe9850a5c.jpg)
> 
> [Pattapit](http://www.twitter.com/Pattapit) @maro254 Most blocks centered around a theme (top down, nostalgia, CLR, etc). M13 seems to have many diff themes. Was this the plan?

Core sets are designed very differently from expert expansions. Expert expansions are all about the block design, which requires them to be fit into a larger framework. The core sets stand on their own, so it's important they play into whatever theme that core set is using. Note that core set themes are much milder than block themes that tend to push the design into more restrictive places.

> ![](https://i.ormos.uk/f4/73/f47355526bba808e4f962b320cc5862bccbf7dd24a20f9871111aba0cf51a725.jpg)
> 
> [joshuamilliken](http://www.twitter.com/joshuamilliken) @maro254 What is your favorite card you designed in the set?

That's tough. I'll call a three-way tie between [Battle of Wits](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits), [Clock of Omens](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clock+of+Omens), and [Oblivion Ring](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring). [Battle of Wits](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits) because I love alternative win cards and this is the best one I've ever designed. [Clock of Omens](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clock+of+Omens) because the Johnny in me loves designing engine cards (cards that turn one resource into another) and this one is an interesting one. [Oblivion Ring](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) because it defines the avenue that I am most interested in exploring with how white removal works.

Note that I don't have much time to focus on the core set (working on all the expert expansions), so I didn't make any of the new cards in the set.

![](https://i.ormos.uk/c6/31/c63197a299619041f9509df4f33590f70f3542fa5f101266ee75356a2487d359.jpg)  

> ![](https://i.ormos.uk/11/32/11327ecfbd2d217f229733e368f4c636944958ac1268b8994c00ad28421cead4.jpg)
> 
> [OriginalOestrus](http://www.twitter.com/OriginalOestrus) @maro254 What made you decide to include cards that offer different win conditions (e.g., [Door to Nothingness](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Door+to+Nothingness), [Battle of Wits](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits)) in M13?

Alternative win conditions are very popular and in a core set they help communicate very loudly that the very nature of the game can be changed by new cards.

> ![](https://i.ormos.uk/10/74/1074a04ac9c3a413e4ada05cdb232a0861180ab86f289a10ba9455f246eb5569.jpg)
> 
> [CurlyfryUSA34](http://www.twitter.com/CurlyfryUSA34) @maro254 Do you go into design feeling the need for a drastic change with M13? (No Titans, [bops](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), trademark creatures like a certain spider.)

I don't think the goal of the ***Magic** 2013* design team was one of drastic change. In fact, I wouldn't even characterize the design of the set *as* one of drastic change. Each year, we want to keep some constants while shaking things up. Because we want to add new things each year, it means some old things have to go away.

While [Birds of Paradise](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) and [Giant Spider](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Spider) might have been surprises, the exit of the Titans shouldn't have come as too big a shock. The Titans have had a huge impact on the tournament scene and it's important to rotate out tournament-defining cards to help change how formats like Standard get played.

> ![](https://i.ormos.uk/2e/03/2e038dc5c7c7c6c3cae7d34f29e82f4d93b52165c53522e101a0490be07a7218.jpg)
> 
> [SweetoothTKC](http://www.twitter.com/SweetoothTKC) @maro254[Thundermaw Hellkite](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite) looks amazing. How long has Ramp;D wanted a Constructed-worthy dragon and how did design start making one?

[Doug Beyer](https://web.archive.org/web/20120709000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer)'s comments about [Thundermaw Hellkite](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite) were, "This was the one card that I felt I kind of stepped over the line of design into development. When I handed the set over to development, I said to [Zac](https://web.archive.org/web/20120709000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Zac%20Hill) \[Hill, the set's lead developer\], 'Please make sure this is very good. That's the design intent.'"

![](https://i.ormos.uk/e3/2d/e32d3959d7a6beed4c7c208ccb0919818c2391a9bb0c3296ee58721e2ccc1b74.jpg)

[Thundermaw Hellkite](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite) | Art by [Svetlin Velinov](https://web.archive.org/web/20120709000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Svetlin%20Velinov%22%5D)

> ![](https://i.ormos.uk/bd/df/bddf59fb942dcdf3b22e879db56100df4b15d888b79ce560f1c86a2ab870cd3b.jpg)
> 
> [joelniddrie](http://www.twitter.com/joelniddrie) @maro254 During the design process was [Trading Post](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trading+Post) ever a land? If so, why was it changed? If not, why isn't it a land?

I believe it was always an artifact. The biggest reason is this: The card has a lot of text on it. One of our design rules for lands is that they have to produce mana. That would have forced extra text onto the card and it doesn't fit.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Thundermaw+Hellkite"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trading+Post"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Trading+Post"></a></div></div></td></tr></tbody></table>

> ![](https://i.ormos.uk/2e/03/2e038dc5c7c7c6c3cae7d34f29e82f4d93b52165c53522e101a0490be07a7218.jpg)
> 
> [SweetoothTKC](http://www.twitter.com/SweetoothTKC) @maro254 Was DotP 2013 taken into consideration when you were designing new cards in M13 and, if so, how?

Very much so. The two design teams (***Magic** 2013* and **Duels of the Planeswalkers** 2013) worked together to figure out what needs could be met with the same cards. One of the things they decided was to have five of the challengers in **Duels** be a cycle of legendary creatures that would show up in ***Magic** 2013*. These legends would also be the cards the M13 intro decks would be built around.

The two teams also looked for cards that made sense in both M13 and in decks in **Duels**. I believe when the dust settled there were around sixty(?) cards that overlapped the two. A few of the new designs were even for cards created to fit a need for **Duels** that M13 found a home for.

> ![](https://i.ormos.uk/64/34/64349956a09be33bbc509201ee6464ea4545f14247aa6510594723edfbea29d9.jpg)
> 
> [34thGingerbread](http://www.twitter.com/34thGingerbread) @maro254 Are mono-colored creatures with alternate mana abilities really a better option than multicolored creatures?

Off-color activations (as Ramp;D refers to them) work differently in one important way. Because the second color mana is in the activation, it doesn't require you to wait to cast the creature until you have both colors. This makes these cards a little easier to splash as you are not punished quite as hard for not drawing your off-color mana. Also, traditional multicolor cards (aka gold cards) are a bigger splash than off-color activations, and the goal of this set was to keep the focus on [Nicol Bolas](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker), who was, on purpose, the only gold card in the set.

![](https://i.ormos.uk/a4/b4/a4b4ee598585994a5c4282689dffb15a9e792343d9ba1ecc1270de2eb6259877.jpg)

[Nicol Bolas, Planeswalker](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) | Art by [D. Alexander Gregory](https://web.archive.org/web/20120709000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22D.%20Alexander%20Gregory%22%5D)

> ![](https://i.ormos.uk/47/e3/47e30bd1a41f21112952324d75a49e89b4293879f97b46fe5bf5c3dcdd710c88.jpg)
> 
> [Kengy5](http://www.twitter.com/Kengy5) @maro254 Is there any formula to the number of mythic rares each color gets when not balanced? Red was shorted two core sets in a row.

There is no formula. Ramp;D decided years ago there was no easy way to balance the colors in mythic rare (mostly because we like having the occasional mythic rare artifact, land, or multicolored card, which makes the math no longer divisible by five), so we'd get close each time but not worry about the small variance. There's no bookkeeping built into the system to check against how the colors wound up in previous set's mythic rares.

> ![](https://i.ormos.uk/8e/64/8e6493455d3fb50c60826d4cc8add44ad9ff2cae688cb13be596d710236c4a2a.jpg)
> 
> [SSJTapkar](http://www.twitter.com/SSJTapkar) @maro254 Why the focus on one Planeswalker (seen in the packaging)? We've never had a core be story-driven. Sorry if it's been explained.

Packaging has specific needs, one of which is for one central image. Having more than one focal point makes the packaging seemed cluttered. [Nicol Bolas](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) being on packaging was because he seemed like a strong image to wrap the set around. It also helped that the story had many heroes but only one villain.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nicol+Bolas%2C+Planeswalker)](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker)

  

> ![](https://i.ormos.uk/a7/39/a739da5f3778511cd11b606ad27ddccdf11b983b9c343b9733fc241df4844110.jpg)
> 
> [JoshuaLemish](http://www.twitter.com/JoshuaLemish) @maro254 Are any of the core set abilities like exalted going to carry over or will they be dropped like bloodthirst in M12?

The current plan is for the returning core set mechanic to stay in for one set and then be replaced by a new one the following year. This means you should enjoy exalted in ***Magic** 2013* because ***Magic** 2014* has a new toy for you to play with.

> ![](https://i.ormos.uk/2d/dc/2ddcb79a17f386f4ebe54a2bc1aae5487767fac04999ad5bc2c76e7e9d7daa87.jpg)
> 
> [Voraath](http://www.twitter.com/Voraath) @maro254 Is M13 designed in mind with the current Standard rotation or the coming fall rotation?

Both are very much kept in mind.

> ![](https://i.ormos.uk/04/67/0467b77ede70d9032fb35caf7db4d312b098cb3456c5234d6a86ded8831fea9d.jpg)
> 
> [markabq](http://www.twitter.com/markabq) @maro254 Although the unwashed masses say they prefer all upside cards (e.g., Merfolk lords), are they really better for the game?

I strongly believe yes. One of the things we've learned over the years is that there's a lot to keep track of in the game of **Magic**. One way to help the players is to minimize the number of important pieces of information about their cards that sits in the rules text of the opponent's cards. Players expect to look at their cards for information about their side and vice versa for their opponents, but looking at your opponent's cards for your information and vice versa is not expected or intuitive. All upside cards is one means of helping solve this problem.

> ![](https://i.ormos.uk/d3/94/d394ade8c9d95337a40567cb7f70df124243ceaac4506aaf4fac31fbbf129e2d.jpg)
> 
> [301865564](http://www.twitter.com/301865564) @maro254 Why the sudden addition of haste rules text? Seems clunky when haste is so old and is the first keyword most players learn.

Our philosophy about reminder text is that we put it wherever we think it's needed. Experienced players can much more easily learn to skip over it than new players can learn how to find the information, provided they even understand there is information they do not know. In other words, the greater evil is not enough information—not too much.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hellion+Crucible"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Hellion+Crucible"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Brute"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Reckless+Brute"></a></div></div></td></tr></tbody></table>

> ![](https://i.ormos.uk/2b/a8/2ba88e690f746b7e02324fa764e710cb017809da05111a90730c756dd66eda28.jpg)
> 
> [TheSundry](http://www.twitter.com/TheSundry) @maro254 M13 will be the first core set ever w/out a cycle of "lucky charms." What made the team finally decide to let them go?

The Lucky Charms (a nickname for a cycle of artifacts that gain you life for a certain color of spells being played—there's been two different versions in **Magic**'s history) have been around since Alpha. We argue about them every year because newer players love them but they take up five slots every year. **Magic** is all about ebb and flow, so the design team decided it was time to give them a break and let some other cards shine. This slot was used for the new ring cycle.

![](https://i.ormos.uk/41/d3/41d3b0d922c1bc5e2f975fdedb42969903b658cdca063be3163a7fcf602a6f71.jpg)  

> ![](https://i.ormos.uk/1f/80/1f800aae7ea0a57a0a23270e75fb042ea84578ff81d564d386a7f7cbeb96904f.jpg)
> 
> [IredaleLuke](http://www.twitter.com/IredaleLuke) @maro254 How did Richard Garfield's original vision for **Magic** affect the design for M13?

I've talked about how Ramp;D has uncut sheets from Beta framed and hanging on the wall.

![](https://i.ormos.uk/e2/46/e24605a13eff1bea1af02b9fa14b6ed7947e6be6d53fe834aba6fc35281175cb.jpg)

*Original photo from Maro's Article [80,000 Words](https://web.archive.org/web/20120709000000/http://archive.wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr240amp;page=7).*

One of the reasons we did this was to force us to just look at the starting game a lot. Richard came up with something magical, and while Alpha/Beta wasn't perfect, it got a lot of things right. While trying to take **Magic** to new heights, we always want to remember what Richard did when he first made the game and make sure that his vision shines in the product throughout its life. That's the biggest impact Richard's vision had on ***Magic** 2013*.

> ![](https://i.ormos.uk/dd/5e/dd5e24e4d9324a9c83ccc5b5d6c6e0b1cd5f8b75d732e2993a1cdcf3fece28ce.jpg)
> 
> [bloodyspasm](http://www.twitter.com/bloodyspasm) @maro254 Why is [Nicol Bolas](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) the only multicolored card? The concept of more than one color does not seem difficult to grasp for new players.

You've heard of the straw that broke the camel's back. It's very easy to keep looking at things in isolation and saying "This concept isn't so hard." But as you start stringing all these little things together, they become complex. Could the core set ever have multicolored cards? Sure, but we didn't feel that this was the core set to introduce it *en masse*. One high-profile card, we felt, would do a lot to introduce the concept without bogging down new players.

> ![](https://i.ormos.uk/d0/45/d045216e26dbd353319cdf84e447b117c9a3967975213e9fb4fe13ff0aa31a6f.jpg)
> 
> [ThePilat](http://www.twitter.com/ThePilat) @maro254 Why [Rancor](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor)?

We feel it's a powerful, popular card that's good but not so good that it can't come back. As we've shown with [Lightning Bolt](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt), we like to occasionally reintroduce powerful cards from **Magic**'s past to shake things up. [Rancor](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor) is following in Lighting Bolt's footsteps.

> ![](https://i.ormos.uk/0d/99/0d99860f64697f6cb4eb464358ebd98d8cfcf8a1fdf2c99d37d2e825a5db17e7.jpg)
> 
> [KyleMueting](http://www.twitter.com/KyleMueting) @maro254 What was the discussion behind removing [Incinerate](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate)'s "anti-regeneration" clause and replacing the card with [Searing Spear](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear)?

For a long time, we used to add the "target creature cannot regenerate" text on most of our kill spells. We even invented the term "bury" to mean "destroy it and it cannot regenerate." One day, we asked ourselves, why? Why do we keep hosing regeneration? It wasn't powerful. In fact, it meant very little because it was useless against so many kill spells.

We decided in a meeting one day: "Let's make regeneration not suck. Let's stop hosing it." So we stopped adding the anti-regeneration text. [Searing Spear](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear) was created so we didn't have to reprint [Incinerate](https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) and hose regeneration.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rancor"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120709000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Searing+Spear"></a></div></div></td></tr></tbody></table>

> ![](https://i.ormos.uk/d1/3e/d13e3eb4b154211d463f27762b0ecaac8c120cf9c1613785d5e7ea1313aab713.jpg)
> 
> [Milambus](http://www.twitter.com/Milambus) @maro254 What's the main difference between designing a card for a core set vs. an expansion?

Our expert expansions are very well defined. For example, *Innistrad* was a horror-themed block. That meant that design was looking to make very specific types of cards. We wanted each card to ooze the horror genre, so that warped our card design. The core set has less theme forcing its hand so it tends to be a bit more straightforward.

> ![](https://i.ormos.uk/e3/40/e340bca5a0187aefb6cd77ba268102a0ee0a2d5d145ad894cf58389dc8d4f254.jpg)
> 
> [Steve\_Will](http://www.twitter.com/Steve_Will) @maro254 Were there any ***Magic** 2013* cards which were "shoo-ins" for inclusion? Easy choices which defined the "gaps" other cards had to fill?

Have you ever seen a cheerleading movie (and if you haven't, props to you) where it's time for try-outs and the head cheerleader explains that it doesn't matter who's been on the team before? Everyone is on equal footing and has to prove themselves in the try-out. I feel the core set is like that.

No card is "guaranteed in," even if it's been in many times before. Each card has to prove why it makes sense in *this* core set. You'll notice that ***Magic** 2013* is missing some iconic cards from previous core sets. That doesn't mean they'll never return, but it meant they weren't the right fit for this set.

How Would You Like This Mailbagged?

That's all the time I have for today. Join me next week when I'll answer more of your design questions about ***Magic** 2013*.

Until then, may you do something interesting enough that people want to ask you questions about how you do it.

  

But Wait, There's More

[Last week](https://web.archive.org/web/20120709000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/202), I listed a few jobs here at Wizards for those of my readers who might think it's cool to work on **Magic**. It proved so popular that I've decided to post a few more jobs. Today's two jobs are for web developers. Things you need:

> *   Knowledge of HTML
> *   Knowledge of CSS
> *   Knowledge of JavaScript
> *   Knowledge of **Magic**

The first job is doing [**DailyMTG.com** CMS](http://jobs.hasbro.com/job/Renton-Associate-Producer-Job-WA-98055/1999407/).

The second job is doing [weekend events CMS](http://jobs.hasbro.com/job/Renton-Associate-Producer-TEMPORARY-Job-WA-98055/1999406/).

If either of these sounds up your alley, give them a look. Come join the fun.

![](https://i.ormos.uk/6c/d6/6cd63cd7ec3a074fd9b83a13301f754e108ce0a6f97c456237c93ac02d5cacfe.jpg)![](https://i.ormos.uk/a6/0b/a60b79fd523fd93f6439921c2e11b5bfff5c64eb0ed239c9cfdab04900a6ec93.jpg)[![](https://i.ormos.uk/85/68/85681924af087d16b8c4556dd7b5bc518906c42e5608b491ae3f6b89725d81a9.jpg)](https://web.archive.org/web/20120709000000/http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/league-facts)![](https://i.ormos.uk/76/cb/76cbedbeeab08bef30860e26085aecd98a18dc4dc70b7064f730666d4ccf4882.jpg)![](https://i.ormos.uk/e2/1a/e21aa3591ec006ee40c48c81364afa88626bcd7b5cd9dd52aa7ddf36e155ac21.jpg)![](https://i.ormos.uk/80/c4/80c449c23b7c7a45922eaafaf0e94414853c78447c41868778f679093e820acf.jpg)[![](https://i.ormos.uk/70/15/7015dc36644380bf3001b06e7ab517b088d6ec2e1bfba8709e54bcad187ed8fb.jpg)](https://web.archive.org/web/20120709000000/http://archive.wizards.com/Magic/Digital/DuelsOfThePlaneswalkers.aspx)