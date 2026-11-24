---
id: bct4pwa0
kind: article
lang: en
path: /en/articles/latestdevelopments/2016/09-15-putting-some-energy-into-kaladesh
title: Putting Some Energy Into Kaladesh
published: '2016-09-15'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    lang_detected: en
    capture_id: 730051
    url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    captured_at: '2016-12-17 03:57:49+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    lang_detected: en
    capture_id: 730051
    url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    captured_at: '2016-12-17 03:57:49+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    lang_detected: en
    capture_id: 730051
    url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    captured_at: '2016-12-17 03:57:49+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    lang_detected: en
    capture_id: 730051
    url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
    captured_at: '2016-12-17 03:57:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: bct4pwa0
  url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
  lang: en
  template: drupal
  captured_at: '2016-12-17 03:57:49+00'
  capture_id: 730051
  wayback_url: https://web.archive.org/web/20161217035749id_/http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: bct4pwa0
  capture_id: 730051
  url: http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
  wayback_url: https://web.archive.org/web/20161217035749id_/http://magic.wizards.com/en/articles/archive/latest-developments/putting-some-energy-kaladesh-2016-09-16
  captured_at: '2016-12-17 03:57:49+00'
  template: drupal
  sha256: 98cfddfaccae6ef69162b3a16f14873179ee62b7d983f520331bfbe6f4f4c5ff
render_recovery: []
---
Hello and welcome to another edition of Latest Developments. Before you go any further, you should probably spend a few minutes looking over the *Kaladesh* full [card image gallery here](/en/articles/card-image-gallery/2016/09-16-kaladesh).

I will be talking about a number of cards, many of which you may not know, and it might be easier to understand if you have a better idea of what is in the set. Once you are done, come back and we can talk energy.

Energy was a mechanic that was first created in *Mirrodin*—a set that had enough going on that it just didn't need the mechanic. Maro has tried to get the mechanic into sets periodically over the past decade or so, but for various reasons the stars did not align. *Kaladesh* was the set where he put his foot down and decided to really make it work. Luckily, in the past ten years we have improved many of our processes and gotten a lot more people, so there was a better chance we could find the way to make it work.

Of course, none of this was easy. One big problem was identified in early playtesting during design—the developers and the designers used the mechanic very differently. While the designers would play cards that granted energy, and then try to make interesting decisions on when to use them for minor incremental gains, the developers would inevitably just horde the energy and wait for one thing to use it all on—usually the one that had the best conversion rate. The problem was that while it MAY be worth it to spend one energy to jump a creature on the attack, if you waited until the late game, you could get much better returns.

# The Energy Economy

The key to making it so that people didn't horde energy was to make it so that energy had a pretty flat value across the board, in terms of effect. Energy generation could be of different power levels, but the throughput of energy needed to remain the same. That encouraged people not to hoard it for the late game. As development tried to balance these effects, we were quickly running into a problem: there just weren't enough effects that were at the right power level. We could make maybe a dozen commons and uncommons that would work, but after that we needed some other stuff to do. And were having a problem making all of that work.

Part of the issue was that energy wasn't granular enough. Most energy producers made 1 or 2 energy counters, and most spent 1 or 2. It is hard to get enough variability in balanced effects when you only have those options. It also means that once you get to the point that you are spending 3 energy on an effect, it is very strong. Any cards that repeatedly make energy were therefore incredibly powerful. Erik Lauer, who was the set's lead developer for the devign and the first part of development, ended up basically doubling the amount of energy generated, so the cards that wanted to generate EE and spend EE could do so in the same way. But you could also have a card generated EEE and spend EE to better balance out the individual strengths of the cards. Cards could also generate EE and cost only E to use, meaning that it was very easy to keep using their small effects. But having both those and cards with large numbers was still balanced. Basically, once we had those kinds of numbers, we found a large enough versions of energy that we felt we could make cards for both *Kaldesh* and *Aether Revolt*.

# Making Energy Fun for Limited

Whenever we do something new, our first goal is to make sure it can work in Limited. Ultimately, Limited is the environment that we at Wizards have the most control over, and therefore it is the one that is most likely to show off mechanics. If we can't get something to work in Limited, assuming that it is something that shows up at common, it has very little chance of actually working in the real world once it is competing against mechanics that already work. Therefore, most of the early design and development process is about getting mechanics to work and be fun in Limited.

![Voltaic Brawler](http://media.wizards.com/2016/images/daily/cardart_KLD_Voltaic-Brawler.jpg)

Voltaic Brawler | Art by [Raymond Swanland](https://web.archive.org/web/20160915000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Raymond+Swanland%22%5d)

The first part to making energy fun in Limited was solved just by having enough different cards that allowed for interesting decisions. We needed a large number of functional, but maybe a little boring, cards like Thriving Turtle and Thriving Rhino. Once you have those cards, you start to get a lot more utility out of cards like Aethertorch Renegade, Era of Innovation, or Whirler Virtuoso. Basically, we need enough of a spread of different strategies within the set that you will have some decks that are just using energy because some of the cards are good; and you will have decks that are going out of their way to maximize energy generation, and have a wide variety of energy outputs.

Voltaic Brawler is one of the best ways to convert energy into a resource. But because it needs to attack, it doesn't stockpiling energy in the same way that a card like Electrostatic Pummeler does. Making energy work for Limited meant that we needed a little bit of each. We wanted the average person playing Limited to have some energy in their deck, but not to make that the focus of every deck. At the same time, we did want some people to go really deep on their energy decks, and include cards like Sage of Shaila's Claim and Woodweaver's Puzzleknot. Much like how almost any deck in *Shadows* Limited could have some delirium cards, but you could also made a deck that was very focused on actually turboing out delirium. We wanted that same kind of strategy to work with energy.

Once we had the scaffolding in place, we had to tweak things for balance.

Much like how we used the difference between 2R and 1RR and RRR in balancing casting costs, we also used the timing on triggers for energy to make up the difference between when something might cost E or EE. We got to use similar activation abilities to determine which deck this was best in: an attack deck, or something that might want to turtle up. Or just finding what the right balance for your deck is. In the end, I think you will all enjoy energy. For Limited, it creates the variability of game play that Maro was going for when pitching energy as a mechanic. And for Constructed...well, let me get into that.

# Making Energy Work in Constructed

Energy is, without a doubt, a very parasitic mechanic. We have a real love/hate relationship with parasitic mechanics. They are very fun and novel when they work correctly (and for Limited), but they often struggle in Constructed. We worry about pushing anything linear too hard. Linear themes can cause other sets a hard time in Standard, since they don't usually contain cards that work well with those themes. Luckily, energy has some linearity, but the mechanic doesn't get exponentially better the more energy cards you play. There is just some level of diminishing returns that we could play into. As a whole, we ended up steering toward cards that used energy in chunks with tap or a trigger, as opposed to ones you could effortlessly pump infinite mana into.

We knew that finding that balance would be a difficult challenge without making a decent number of cards that could be self-contained with their energy usage. So we made a lot of "somewhat self-contained cards." While we were already planning on doing a lot of that for Limited, we needed to go a little further for Constructed. We needed cards that were strong enough to play in decks by themselves, with no other energy, so that people would be enticed to trying to make them work.

![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_58fPS8uzKG.png)![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_wuMjzH4TNw.png)

![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_qPgHGpyvNN.png)![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_pj0qmvj6PT.png)

Once people were including these cards in their decks, there was more room for cards that were a little more about energy generation. Cards like that would likely be a bit too weak if your deck didn't include energy. But they'd be a good (if not the best) choice for a deck that is trying to do something with energy.

![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_12TjF3LAAX.png)![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_rBGihVt6ij.png)

![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_lLXtzHPW0D.png)![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_qFvJXXsSfN.png)

One of the things we want for new sets is for people to identify their decks as doing something new when a new set comes out. Rotation helps this, but so does the cards in the new set having a real impact that pushes things in a new direction. Energy does that...unless you're playing only one energy card in your deck. Once you have moved to two, you start getting into interesting new territory. You can pick and choose how to use your energy to maximize whichever cards you are using, and you start getting interesting decisions. At some point, you can go all-the-way and look to move to a deck whose primary goal is to produce energy, and then do something cool with it like Aetherworks Marvel. This variety of decks should make energy feel less like a monolithic part of the format, where everyone is trying to accomplish the same thing, and instead like the alternate resource it is intended to be.

That's it for this week. Next week, as you get ready to go to [your local Prereleases](https://web.archive.org/web/20160915000000/http://locator.wizards.com/), I'll be talking about fabricate.

Until next time,

Sam ([@samstod](https://twitter.com/@samstod))