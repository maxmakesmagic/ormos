---
id: 6vhdyvww
kind: article
lang: en
path: /en/articles/latestdevelopments/2016/07-15-a-little-change-will-do-you-good
title: A Little Change Will Do You Good
published: '2016-07-15'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    lang_detected: en
    capture_id: 726644
    url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    captured_at: '2022-08-08 07:42:19+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    lang_detected: en
    capture_id: 726644
    url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    captured_at: '2022-08-08 07:42:19+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    lang_detected: en
    capture_id: 726644
    url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    captured_at: '2022-08-08 07:42:19+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    lang_detected: en
    capture_id: 726644
    url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
    captured_at: '2022-08-08 07:42:19+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 6vhdyvww
  url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
  page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
  lang: en
  template: drupal
  captured_at: '2022-08-08 07:42:19+00'
  capture_id: 726644
  wayback_url: https://web.archive.org/web/20220808074219id_/https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
- document_id: 6vhdyvww
  url: http://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15?tags=Daily%20MTG&lang=en
  page_key: magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15?lang=en&tags=Daily%20MTG
  lang: en
  template: drupal
  captured_at: '2016-07-19 09:04:01+00'
  capture_id: 726645
  wayback_url: https://web.archive.org/web/20160719090401id_/http://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15?tags=Daily%20MTG&lang=en
- document_id: 6vhdyvww
  url: http://magic.wizards.com/en/node/1047206
  page_key: magic.wizards.com/en/node/1047206
  lang: en
  template: drupal
  captured_at: '2016-07-19 22:28:44+00'
  capture_id: 2478967
  wayback_url: https://web.archive.org/web/20160719222844id_/http://magic.wizards.com/en/node/1047206
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 6vhdyvww
  capture_id: 726644
  url: https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
  wayback_url: https://web.archive.org/web/20220808074219id_/https://magic.wizards.com/en/articles/archive/latest-developments/little-change-will-do-you-good-2016-07-15
  captured_at: '2022-08-08 07:42:19+00'
  template: drupal
  sha256: 88e0a0e1e4064ab04a7a7febf4274e2d864c2745a8cbc25846fc2f08184b91f3
render_recovery: []
---
The headline of "Emrakul coming to Innistrad" was exciting and evocative, but actually showing that off turned out to be more difficult than we expected. If we had never done double-faced cards before, then it would be the perfect way to show off things changing. But not only had we done them before, we had a total of three sets in Innistrad blocks already using them—so simply having creatures turn into colorless monstrosities just wasn't enough. It was something, it helped, but we needed more. Similarly, meld was a great evolution of transform, but we couldn't have much more of it in the set than we did, unless we went to a second double-faced card slot—something that I was very wary of doing after having negative experiences with it.

The design team handed off a few mechanical variants in *Eldritch Moon* that were meant to simulate the Eldrazi feel, but while some worked as individual cards, none of them worked as a whole mechanic. The most interesting of the mechanics that came out of late design was one where spells and abilities that affected creatures with a certain keyword didn't stop at end of turn. That mechanic had the unfortunate problem of not actually working with how the rules currently functioned. For instance, I cast [Hope and Glory](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hope+and+Glory) targeting one creature with the keyword and another creature without it. Do they both have +1/+1 forever? What about continuous effects that impact the creatures, how do those work? Is the mechanic still fun if we only make it +X/+X effects? Even if we could have answered all of these questions, we were still left with something that would likely require a huge rewrite of all of our digital versions of *Magic*'s handling of layers, which—less than a year after a mana system rewrite to make colorless mana work—wasn't appealing to anyone. In the end, meld got to be the mechanic from the set that was going to take a ton of work from both rules and digital perspectives (and boy did it), and I went in search of a new mechanic to represent the Eldrazi in the set.

Talking with Kelly Digges and James Wyatt in creative, they made it very clear that they would prefer to not have devoid appear in this block—and luckily I was on the same page with them. However, I also knew that I wanted the Eldrazi to have some kind of color leanings, so that we could focus them in some of the colors rather than all of them. This meant that an ideal mechanic would let you cast these cards for colored mana somehow, but also let the cards be colorless.

When working on a problem like this, I find it important to talk it out with people. I presented the challenge to a number of people within R&D and tried to get them to give me their thoughts on what we had done before that would meet that goal. Not to just use an old mechanic, but to try and find the kind of space the mechanic could exist in—or at least get a good starting point. Things like morph worked, but we had just done it. Erik Lauer suggested ninjutsu as a way to show something transforming into something that couldn't be better shown off in a DFC. And so, I went with that.

# The Stars of Emerge

The very first version of emerge was just a renamed ninjutsu. It probably won't be surprising that ninjutsu is very high on our list of mechanics we would like to revisit again someday with a new name—since we really can't put ninjutsu in a set without going back to Kamigawa. I went about making a small suite of colorless Eldrazi creatures that could use colored mana symbols to ninjutsu themselves out. It was fun (because Ninjas are fun), and they had high enough mana costs as opposed to "regular" Ninjas that we could have enters-the-battlefield triggers without worrying about people using multiples to have multiple triggers happen per turn. Or, if you could—the fact that it would cost ten mana was enough to make it okay.

While the mechanic was as fun as I remember ninjutsu being, the actual creatures were less satisfying to play. The thing about ninjutsu was that it was mostly on small creatures, which meant that your opponent didn't just lose when you hit them with the Ninja once. When we were trying it with Eldrazi, the enters-the-battlefield triggers were interesting, but the big deal was that most of the creatures were secretly just [Lava Axe](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe)s and [Searing Flesh](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Flesh)es. Interesting effects may have read interestingly, but your opponent was dead before anything interesting actually happened.

At the time we were testing this, the creative team had some qualms with it—nothing that would kill it, but it didn't make a ton of sense that the creature would return to your hand. That's really not what the Eldrazi were doing in this world. Instead, it would make more flavorful sense if the creature had to die. I was fine with this, since it let us make more of the power in the emerge creature and give it a powerful trigger rather than worrying that people would always be up two-for-one or more whenever they put one onto the battlefield.  
  
 In talking with David Humpherys, he felt strongly that attacking with the creatures was wrong, and preferred if it happened at sorcery speed when you could normally cast the creature. He suggested getting a rebate of some kind—either the converted mana cost or the power of the creature—as a reward. It also, in his mind, fit the story. In talking with the creative team, they were very happy with that change, as were the other members of the development team.

What excited me about this, especially when going with converted mana cost rather than power, was that we could easily make the mechanic feel very "Johnny-ish" by letting players sacrifice creatures with powerful enters-the-battlefield effects and weak stats. In *Shadows*, that meant things like [Drunau Corpse Trawler](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drunau+Corpse+Trawler). Still, I knew I would need to make more creatures that could do this, and created [Enlightened Maniac](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enlightened+Maniac), [Exultant Cultist](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exultant+Cultist), and [Primal Druid](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Druid) at common to help reward those kinds of strategies.

![Enlightened Maniac](http://media.wizards.com/2016/images/daily/cardart_EMN_Enlightened-Maniac.jpg)

[Enlightened Maniac](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enlightened+Maniac) | Art by [Jaime Jones](https://web.archive.org/web/20160715000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5b%22Jaime+Jones%22%5d)

# Making Emerge Creatures

Once we had the final version of the mechanic, it was time to actually make the cards using it. The initial idea of just blue and green ended up creeping into black, because we felt we had some really good creative ideas for how emerge could play out there—but also because putting a mechanic in three colors instead of two creates much more play in Limited. We wanted the "cheap" emerge creatures to start at at least seven mana, which played out well in letting you curve them out on turn four. The general rule was that, at least for the Limited cards, we wanted these to be powerful creatures that could help swing the game in your favor, but not the be-all-end-all of things to do. We also got a lot of gameplay out of small changes in the mana costs of the emerge creatures, so that an eight-drop, for instance, doesn't cleanly curve on anything. You can cast it on turn five, but you may leave a mana up to do it. On the other hand, if you miss your fifth land drop, it can also be a strong play that keeps you from stalling out in the game.

The two important constraints on every emerge card were that it had to be something that was actually worth the sacrifice cost, but also couldn't be so huge of an effect that the game was basically over when you cast it. After all, balancing emerge creatures was difficult since every mana you add only pushes back the turn it can hit the battlefield by about half a turn. Because we didn't want to include the text "sacrifice a non-Eldrazi creature" due to both length and clunkiness, we also had to worry about chaining multiple emerge creatures in one turn. Certainly, there were points when [Lashweed Lurker](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lashweed+Lurker) would see multiple turns in a row bouncing a land against a helpless opponent.

We wanted to have at least two emerge creatures at common—which meant finding ones that could have large enough impacts on the game for them to be solid early picks, but not end up having everyone chasing those cards and colors in the draft. Draw a card was great on [Wretched Gryff](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wretched+Gryff) because giving you a solid flier on turn four was powerful, but you had a big tempo loss. [It of the Horrid Swarm](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=It+of+the+Horrid+Swarm) let the emerge decks sort of go the other way—create a ton of power on the ground to keep from getting overwhelmed as they traded away their tempo.

At the higher rarities, we wanted to make sure to hit flash, which was such a fun ability on emerge that two cards in blue got it. One of the best parts about putting [Archaeomancer](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archaeomancer)'s ability on an emerge creature was that it was more likely that you could get a huge advantage by having not only a removal or card draw spell your opponent would have to deal with again, but also, the creature had large enough stats that it could actually block that next turn. [Elder Deep-Fiend](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elder+Deep-Fiend) was created as a direct callback to [Mistbind Clique](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistbind+Clique), since champion and emerge shared a lot of similarities, and it was a good spot for a rare emerge creature to live in. [Decimator of the Provinces](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decimator+of+the+Provinces) was a cute callback to [Craterhoof Behemoth](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craterhoof+Behemoth), and [Distended Mindbender](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Distended+Mindbender) let us push incredibly powerful discard on a creature without worrying that the flickering on [Eldrazi Displacer](https://web.archive.org/web/20160715000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eldrazi+Displacer) would lock people out of the game.

These creatures were difficult to get "right," and I wouldn't be surprised to find that a few of them are a little larger than they need to be. Due to the nature of Eldrazi being a bit over the top, most of them started at larger stats than we would normally start creatures at, and we generally playtested to see whether we needed to pull back or if they were fine where they were.  
  
 As a whole, I am very proud of how emerge turned out. There were a lot of difficulties with the mechanic, both designing it and balancing it, but (in my mind) it solved most of the challenges put before it and did so while being flavorful and fun. I hope you all enjoy what it does for both Limited and Constructed games.

That's it for this week. Join me next week when I start going through the M-Files for *Eldritch Moon*.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))