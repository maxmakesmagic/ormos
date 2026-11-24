---
id: k9e7xj0x
kind: article
lang: en
path: /en/articles/makingmagic/2002/05-06-phantom-of-the-soap-opera
title: Phantom of the Soap Opera
published: '2002-05-06'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    lang_detected: en
    capture_id: 228197
    url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    captured_at: '2024-04-15 19:34:38+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    lang_detected: en
    capture_id: 228197
    url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    captured_at: '2024-04-15 19:34:38+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    lang_detected: en
    capture_id: 228197
    url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    captured_at: '2024-04-15 19:34:38+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    lang_detected: en
    capture_id: 228197
    url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
    captured_at: '2024-04-15 19:34:38+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: k9e7xj0x
  url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
  page_key: magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
  lang: en
  template: contentful
  captured_at: '2024-04-15 19:34:38+00'
  capture_id: 228197
  wayback_url: https://web.archive.org/web/20240415193438id_/https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
- document_id: k9e7xj0x
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr19
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr19
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:06:08+00'
  capture_id: 798705
  wayback_url: https://web.archive.org/web/20090604150608id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr19
- document_id: k9e7xj0x
  url: https://magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06
  page_key: magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06
  lang: en
  template: drupal
  captured_at: '2022-08-16 16:57:07+00'
  capture_id: 903963
  wayback_url: https://web.archive.org/web/20220816165707id_/https://magic.wizards.com/en/articles/archive/making-magic/phantom-soap-opera-2002-05-06
- document_id: k9e7xj0x
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr19,,ja,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr19
  lang: en
  template: classic_asp
  captured_at: '2004-12-26 18:43:21+00'
  capture_id: 1973469
  wayback_url: https://web.archive.org/web/20041226184321id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr19,,ja,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: k9e7xj0x
  capture_id: 228197
  url: https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
  wayback_url: https://web.archive.org/web/20240415193438id_/https://magic.wizards.com/en/news/making-magic/phantom-soap-opera-2002-05-06
  captured_at: '2024-04-15 19:34:38+00'
  template: contentful
  sha256: 3255ee438c0f65c923dc32bdc5809fecbf89424cd31f0a37aeb801cef19e7525
render_recovery: []
---
After last week’s anticlimactic story, I thought it only fair to walk you through a *Judgment* mechanic that had some real evolution. In particular, I thought I would focus on a single card to show how the card went through the design (and development) process. The mechanic is the phantom mechanic and the card is Phantom Nishoba.

The phantom mechanic is on a series of white, green and multi-colored white and green creatures in *Judgment*. Each phantom has a printed toughness of 0 and comes into play with a certain number of +1/+1 counters. In addition, they all have the following line of rules text: “If damage would be dealt to CARDNAME, prevent that damage. Remove a +1/+1 counter from CARDNAME.”

What this means in short is that each phantom can survive X-1 fights (or other forms of damage) where X is the number of +1/+1 counters it has. That ability makes them very hard to destroy with damage (combat, direct, etc.). To make matters worse (or better if you’re playing a phantom) the replacement effect happens regardless if there’s a +1/+1 counter on the creature. In English, what that means is that if you manage to increase a phantom’s toughness (with, say, a [Holy Strength](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength)), the phantom will never be destroyed by damage. Essentially, when the creature takes damage, the phantom effect prevents the damage, and when it goes looking for a +1/+1 counter to remove, the game just says, “Oh, there’s no +1/+1 counter. Oh well.”

But this is, of course, is the card as you all get to see it. This isn’t always how the card first appeared.

### Zoinks!

The phantom mechanic was designed by R&D member Brian Tinsman. Brain claims his inspiration for this mechanic was trying to come up with something that could simulate a ghost in game terms. He liked the idea of creatures that were extra resilient and would be tougher to destroy than your average creature. To reflect this flavor, the creatures were called ghosts in design.

Here is the earliest version of Phantom Nishoba:

\[Ghostly Earth Wurm\]  
6GG  
Creature -  
7/7  
Whenever damage is dealt to CARDNAME, prevent that damage and put a -1/-1 counter on CARDNAME.

The early version of the card better demonstrates Brian’s flavor. Each packet of damage, regardless of its amount, shrinks the creature by -1/-1. The reason behind the change from this version to the +1/+1 version is rather simple: we don’t do -1/-1 counters anymore. Okay, that’s not exactly true. We do use them occasionally but only in a very specific way. As an example, [Shambling Swarm](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Swarm) from *Torment* does in fact use -1/-1 counters, but please notice that they only last until end of turn.

Why do we do that? Because 99% of the time we can mimic the desired effect using +1/+1 counters and the loss of the 1% is worth the clarity that only having one type of power/toughness-altering counters creates. When you look across the table and see a creature with counters on it, you know they are +1/+1 counters. I know this paragraph will prompt a few letters, but please know that I’m currently working on my “why simplicity isn’t evil” column in which I will explain in a much larger context why we do things like that. (As an aside, changing to the +1/+1 counters did add the "[Holy Strength](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) and live forever" trick.)

The second thing you’ll note is that the card was originally green. The reason is simply that Brian didn’t realize we were going to do multi-colored cards when he made the mechanic. (As a quick aside, it’s interesting to note that the plan to use white/green -- and only white/green -- multi-colored cards in *Judgment* wasn’t decided until halfway through the design process.)

### Let’s Give Them a Hand-Off

Here’s the card as it was handed off from the design team to the development team:

\[Ghostly Earth Wurm\]  
2GGG  
Creature - \[Spirit\]  
0/0  
CARDNAME comes into play with five +1/+1 counters on it.  
If CARDNAME would be dealt damage, prevent that damage and remove a +1/+1 counter from CARDNAME.  
T: Put a +1/+1 counter on CARDNAME.

Let’s walk through the changes. First, we came up with the idea of allowing one of the ghosts to be able to make itself bigger. Once we attached that ability, we felt we needed to shrink the creature from 7/7 to 5/5, which also allowed us to lower the mana cost.

Next we added some flavor by making the creature a spirit. The design team liked the idea that the phantoms would be ghostly versions of creatures from earlier in the block. We figured that whole herds of white and green creatures were slaughtered during *Torment* and now was the time for payback.

### Let’s See What Develops

Development made a few key changes. First, they decided that they wanted to have a multi-colored phantom (white/green, of course), and they wanted to return it to its former larger size. But they still liked its activated ability. What should they do?

Early on in the development process, a hole opened up in multi-colored. It was then that the development chose to employ a common development technique: they split Ghostly Earth Wurm into two. One half stayed green and kept the activated ability. The other kept the beef and became multi-colored. The former became the card known as Phantom Nantuko, while the latter became [Phantom Nishoba](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba).

To jazz the card up a little once it lost its activated ability, the development team added two basic creature abilities. To keep in the flavor of multi-color, the team decided to make one ability white and the other one green. Trample was obvious, since a creature that big needs some way to break through to deal damage. The "[Spirit Link](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+Link)" ability was added as a cool way to use the creature to aid in your defense. As you beat down you are also building up a life buffer, which is particularly important in multi-player games. (See, we really do keep things like that in mind.)

Meanwhile the creative text guys looked back at all the old white/green creatures to see what cool creature they could “kill” to make the phantom. With slim pickings in white/green in *Odyssey* (they didn't want a Phantom [Mystic Enforcer](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Enforcer)), the team looked back to *Invasion*. Once they saw [Sabertooth Nishoba](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sabertooth+Nishoba) they knew that had their creature.

And thus, [Phantom Nishoba](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba) was born.

Join me next week when we explore the Jedi. (And yes, I’m talking about **Magic**).

Until then, may you have a [Dark Banishing](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) in your hand when your opponent plays his [Phantom Nishoba](https://web.archive.org/web/20020506000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba).

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*