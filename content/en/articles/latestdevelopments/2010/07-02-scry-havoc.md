---
id: bqt1xg6n
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/07-02-scry-havoc
title: Scry Havoc
published: '2010-07-02'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    lang_detected: en
    capture_id: 730499
    url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    captured_at: '2022-09-25 18:55:21+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    lang_detected: en
    capture_id: 730499
    url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    captured_at: '2022-09-25 18:55:21+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    lang_detected: en
    capture_id: 730499
    url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    captured_at: '2022-09-25 18:55:21+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    lang_detected: en
    capture_id: 730499
    url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
    captured_at: '2022-09-25 18:55:21+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: bqt1xg6n
  url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
  page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
  lang: en
  template: drupal
  captured_at: '2022-09-25 18:55:21+00'
  capture_id: 730499
  wayback_url: https://web.archive.org/web/20220925185521id_/https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
- document_id: bqt1xg6n
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/97
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/97
  lang: en
  template: aspx
  captured_at: '2013-07-06 19:17:13+00'
  capture_id: 623868
  wayback_url: https://web.archive.org/web/20130706191713id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/97
- document_id: bqt1xg6n
  url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-01
  page_key: magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-01
  lang: en
  template: drupal
  captured_at: '2022-06-30 01:07:03+00'
  capture_id: 730491
  wayback_url: https://web.archive.org/web/20220630010703id_/https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-01
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: bqt1xg6n
  capture_id: 730499
  url: https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
  wayback_url: https://web.archive.org/web/20220925185521id_/https://magic.wizards.com/en/articles/archive/latest-developments/scry-havoc-2010-07-02
  captured_at: '2022-09-25 18:55:21+00'
  template: drupal
  sha256: f9587514c79d6463f3b03177bdcf6a19a2d512951c4e7a81be33b7c1b3c342ea
render_recovery: []
---
Today is the end of the first week of ***Magic** 2011* previews. Just like ***Magic** 2010*, about half of the cards in ***Magic** 2011* are completely new to the game. Unlike ***Magic** 2010*, ***Magic** 2011* contains a non-evergreen keyword mechanic: scry. This is the first time we've done that, and today I'll talk about why we did it here.

At this point, you might be wondering why I'm talking about this in the development article. This sort of thing normally sits in the design slot, as the choice of keyword mechanics for sets usually comes out of design. In the case of ***Magic** 2011* and scry, however, it didn't. As Mark Rosewater mentioned in [his article](/en/articles/makingmagic/2010/06-28-magic-goes-to-eleven) this week, I was on the ***Magic** 2011* design team. We spent a few weeks talking about big picture issues, then a few months making cards and putting together colors. When we were done with that, we took our scry-free set to its lead developer Erik Lauer and asked him what he thought.

![](https://i.ormos.uk/6e/1a/6e1a72800f45e0f1926291b12d86388a2945c12ba08bcaf0d25dabb27a3b29e0.jpg)  

Overall, Erik was pleased with what we had made. His background in traditional fantasy gaming made it easy for him to love the Titans, and the rest of the set was classic core set **Magic** with plenty of appealing new cards. Erik's main worry with the set was that it played a little too similarly to ***Magic** 2010*. **Magic** is the most fun when it changes over time, and he wanted to ensure that there was enough change in the experience of playing **Magic** with the core set from year to year. Erik's suggestion to deal with this was to add a simple keyword that could be put on flavorful cards. He even had a helpful suggestion about which keyword to use!

We try to have an overlap of one person between the design and development teams of any given set. For ***Magic** 2011*, that was me—so I was privy to all the discussions the team had with Erik about why and how he wanted to use scry. It's been a while since then, though, so I don't feel comfortable telling you what Erik's exact thoughts were. Instead, I will tell you the reasons why I am happy that we used scry.

### Scry Is Flavorful

One of the things I love about **Magic** core sets under our new model is that the majority of the cards do a great job of standing on their own. When you look at, for example, Mitotic Ooze, everything about the card fits together, including the name, the art, and the text box. Although I was the one who submitted that card during design, I am told that the same card has been submitted by a handful of other people. That me and those other submitters all agree on what an ooze is supposed to do is indicative of why the card works as a whole package. 

![](https://i.ormos.uk/d6/5b/d65bbb54df1a1cf139885881cf2d684738c821a07ecb76ec82dc59aa8145f371.jpg)  

Not every **Magic** card can be as perfect as Mitotic Slime at matching mechanic and concept, and in fact **Magic** needs cards that aren't as perfect in order to be fun. For example, it's hard to say exactly what having kicker or a landfall ability means creatively. That's fine; there's nothing wrong with [Steppe Lynx](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steppe+Lynx) or [Burst Lightning](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burst+Lightning), and we'll keep making cards like that. However, the hallmark of our new core sets is spot-on baseline fantasy flavor, and extra text that doesn't improve the match of flavor and mechanics would only get in the way.

![](https://i.ormos.uk/fe/9e/fe9ec725616cef58b123c98d141db4e67d169e0baa2a98626da42eddd7320645.jpg)  

Happily, scry doesn't have this problem. The specific act of scrying is exactly the sort of thing that you might expect a magic-user to do, and it's not much of a stretch to put the word on other concepts that involve looking into the future. It may be a keyword mechanic that has never been in a core set before, but its flavor match makes it a perfect fit for a core set.

### Scry Gives Color Definition

![](https://i.ormos.uk/84/b7/84b73f7431f0fc6de96fe0553e036c2f94505eda58472709713d471536220cec.jpg)

One of Erik's favorite things to do with his sets is make each color play differently in Limited. He knows that **Magic**'s endless variety is a huge part of its appeal, and making each color feel different and unique lets us put more variety into one Limited format. You can draft white-blue in ***Magic** 2011* one day, then draft black-green a day later and have totally different games. A second benefit of each color having a distinct feel is that a player who likes playing **Magic** a particular way is more likely to find a color that lets him do that. Both of these things are part of why **Magic** can be fun for so long and for so many different people.

You might be a little confused right now about what this has to do with scry. In *Fifth Dawn* and *Future Sight*, scry appeared on cards of all five colors. This is not the case in ***Magic** 2011*. As I talked about before, we didn't randomly write scry on cards that didn't have it before and call it a day. Instead, we looked for the fantasy ideas that it made sense to use scry to express, and made those. As it turns out, scry works best on cards that represent looking into the future, and looking into the future is solidly in blue's realm. Therefore, most of the scry cards in ***Magic** 2011* are blue. 

Erik had already followed that chain of logic through when he suggested scry, and knew that it would give him a way to differentiate blue from other colors. If you are the kind of person who likes controlling the future and manipulating the cards on top of your deck, then I suggest playing with blue at your [***Magic** 2011* Prerelease](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments). Of course, the fit between blue and scry was already pretty natural, as the sort of person who values the ability to scry is quite likely to already be drawn to blue's card drawing effects. Overall, it was a perfect match.

The [***Magic** 2011* Visual Spoiler](https://web.archive.org/web/20130706191817/http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2011/spoiler) contains several cards with scry. I'll talk briefly about each of them, then introduce today's preview card.

### Foresee

A month ago, I told you that [Divination](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) was not in ***Magic** 2011*. The addition of scry made it obvious that we were supposed to cut [Divination](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) for [Foresee](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Foresee). [Foresee](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Foresee) is a reprint, but it easily clears the high bar that a preexisting card must jump over to get into a core set. It has a great name, a text box that does exactly what it sounds like it should and nothing more, and art with a great visual pun. We didn't need to make a new card here, so we didn't.

![](https://i.ormos.uk/73/eb/73eba89a365187ef9b1c0d3f3d39fbd8a8e2cda551e14a461f14fa382dc7f72a.jpg)  

### Preordain

The previous attempt at this kind of card was *Fifth Dawn*'s [Serum Visions](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serum+Visions). In hindsight, [Serum Visions](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serum+Visions) is kind of a dumb card, since it doesn't do the things in the order you want. Why would you draw a card before you did the scrying action? The whole point is to control what you draw, and it makes more sense to start now than to have to draw a random card before I get to select my cards. [Serum Visions](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serum+Visions) is also not a great name, as we aren't always on Mirrodin. Here, we exercised our ability to make new cards and printed a new card with the right mechanic and a better name.

![](https://i.ormos.uk/30/5c/305c7f01916f0a8c70563ebade77519a36eed7c051b977be672d3e936fb3c6bb.jpg)  

### Augury Owl

[Sage Owl](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) is a subject of some debate among people at Wizards. Focus groups have shown that very new players adore it. There are also several people here who think that the feelings of hopelessness it inspires when a more experienced player plays it and sees nothing useful are not worth the price of admission. Augury Owl is intended to be a [Sage Owl](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) that everyone can love; it is all of the appeal with none of the potential hopelessness, as you can just dump the bad cards on the bottom of your deck. This is a subtle card, but it is quite potent. I enjoyed watching its stock continue to rise as we played ***Magic** 2011* Limited.

![](https://i.ormos.uk/c1/12/c1120c8259f47f11bc243dd9507e5f5fc020c40a038a85b3d35c32efef1ecc24.jpg)  

### Crystal Ball

Crystal Ball is, well, a crystal ball. Sometimes a card just speaks for itself.

![](https://i.ormos.uk/1d/d6/1dd6dea5d213a2f3a5d828e012a83029fffcbdf1e49ef7b2216db1b6f550b42e.jpg)  

### Viscera Seer

And finally, here's my preview card.

![](https://i.ormos.uk/68/56/685668e8a16df6450cfe3d44eca02d50221091a4359ee1894c560cb2a21eb24b.jpg)  

Wait a minute. This card isn't blue. What gives?

Aaron Forsythe was the lead designer of ***Magic** 2011*. He liked the idea of putting scry into the set, but he wanted to make sure that we used it everywhere we could. Erik was right that the most obvious cards for scry were blue, but Aaron wanted to look elsewhere. He led the design team in a pass to look for non-blue creative concepts that could be represented by scry. Most of them were stretches, but the idea of sacrificing a living being and using its innards to learn something through arcane means hit us pretty hard. It also struck us as being black. This card is the result.

There are plenty of things to do with Viscera Seer in ***Magic** 2011* Limited. Sacrificing creatures for a small effect normally isn't great, but doing it in response to a removal spell is a lot better. You can also use it with token creatures. Going all the way through a Mitotic Ooze, for example, will put you seven cards closer to whatever you are looking for. Reassembling Skeleton can even come back over and over again to keep being eaten. In Constructed, you should note that Viscera Seer is a Vampire and happens to work quite nicely with [Bloodghast](https://web.archive.org/web/20100702000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodghast).

Next weekend is the [***Magic** 2011* Prerelease](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments), held in local stores and convention halls across the world. It'll be your first chance to get your hands on all the new cards, and also your first chance to play core set Limited with scry. We hope that when you look a week into your future, you see ***Magic** 2011* cards!

[![](https://i.ormos.uk/60/c8/60c852c400d9fbe775708fbd01d92e843e51c781c01d7375f2d78c82ab1446f3.jpg)](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments)