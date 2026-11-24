---
id: 2dhgf0b2
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/10-25-building-a-hydra
title: Building a Hydra
published: '2013-10-25'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    lang_detected: en
    capture_id: 719272
    url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    captured_at: '2022-05-30 19:19:06+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    lang_detected: en
    capture_id: 719272
    url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    captured_at: '2022-05-30 19:19:06+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    lang_detected: en
    capture_id: 719272
    url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    captured_at: '2022-05-30 19:19:06+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    lang_detected: en
    capture_id: 719272
    url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
    captured_at: '2022-05-30 19:19:06+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 2dhgf0b2
  url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
  lang: en
  template: drupal
  captured_at: '2022-05-30 19:19:06+00'
  capture_id: 719272
  wayback_url: https://web.archive.org/web/20220530191906id_/https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
- document_id: 2dhgf0b2
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/270
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/270
  lang: en
  template: aspx
  captured_at: '2014-02-18 22:12:35+00'
  capture_id: 620659
  wayback_url: https://web.archive.org/web/20140218221235id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/270
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2dhgf0b2
  capture_id: 719272
  url: https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
  wayback_url: https://web.archive.org/web/20220530191906id_/https://magic.wizards.com/en/articles/archive/latest-developments/building-hydra-2013-10-25
  captured_at: '2022-05-30 19:19:06+00'
  template: drupal
  sha256: fde67fa67091d5ee88e059a63f573384d52f7cc45bfec58e6f4ea98c78e8e71d
render_recovery: []
---
This is Heroic Week, and I want to talk not about the heroic mechanic, but about being a hero with *Theros*'s branded play campaign—The Hero's Path. We talk a lot about developing the individual cards and sets that come out during the normal **Magic** cycle, but the development team also works on other projects such as intro packs, sample decks, and new projects like this one.

![](https://i.ormos.uk/0c/1b/0c1ba7941c1eaee6f5d66215b84bd8611fd2a5bcaa8661ed6ca8fa8800feb134.jpg)

Swallow the Hero Whole | Art by [Scott Chou](https://web.archive.org/web/20131025000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Scott%20Chou%22%5D)

### Call to Adventure

The story begins when I, a humble **Magic** development intern, was looking for my place in the world. [Dave Guskin](https://web.archive.org/web/20130701052407/https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Guskin), who had then recently begun spearheading all of the branded play activities, was working on the Hero's Path campaign, and part of that was an idea for an in-store activity where you could fight a hydra. Many members of the Pit were interested in throwing out ideas, but as *Theros* was in development and "Huey" in design, many of them also didn't have time. And that is where I came in.

One of the advantages of being a new intern is that you have a lot more time on your hands than the other employees, and I took the opportunity to show the world what I could come up with. This was also a great test of my chops as a game designer, not just as a competitive **Magic** player.

I put together a prototype, taking my inspiration from [Horde **Magic**](/en/articles/seriousfun/2011/10-18-up-up-down-down-left-right-left-right-b-a-shuffle-3), [a variant designed by Peter Knudson](http://www.quietspeculation.com/2011/09/horde-magic-a-new-way-to-play-magic-and-survive-zombie-invasions/), who was a former R&D intern. The idea was that instead of spawning wave after wave of Zombies, the Hydra would be wave after wave of heads, each with a different enchantment ability (this was an enchantment set after all). In this version, the goal of the game was to mill out the Hydra. The Hydra would start with three random heads in play, and then during its turn, it would flip the top card of its library and cast it. Some of these were small spells like deal 1 damage to each creature, while others were heads. When you killed a head, it would then mill from its library until you hit another head, then cast it. When the deck was empty, and you killed the last head, the Hydra was defeated. For this version, it meant you had to kill twelve heads.

![](https://i.ormos.uk/a9/a1/a9a17e2516d732e35c23f28cae40a42904208eb440932638acd18f05082a80a5.jpg)

Like any good prototype, this accomplished some of the goals of what we were looking for, but left a lot of room for improvement. The most notable problem was that because all of the heads had different effects, and only some did damage, the game felt a lot like a prison deck. Some of the designs, like Taxing Head above, were very weak in the late game, and utterly brutal in the early game. Some of this was fixed by changing the starting heads to a fixed line up, but it didn't solve the problems.

At the same time, [Ryan Miller](https://web.archive.org/web/20120725070559/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Miller), former **Duel Masters** and **Kaijudo** lead designer, also put together his version of the game where the cards represented heads, and during each of the Hydra's turns, it would flip the top card of the Hydra's library. There were actual **Magic** creatures in there that it would cast. The other spells that were in the deck were Hydra spells. If the Hydra met the threshold in the top right for the number of heads, it would cast the spell. Otherwise, it would go into the Hydra's resource pile and act as a "head" to count toward further spells. While there were a lot of very good things in this design, it was a bit too complicated to work on auto-pilot, and required a human to make decisions for it, including attacking and blocking.

![](https://i.ormos.uk/70/aa/70aa23c576cff817189901d24c7dc82a41af1d77dacb67262d593cf09fba983e.jpg)

When I was eventually officially tasked with creating the real prototype for the game, I took elements from both my design and Ryan's, such as creating much more interesting spell effects and a few threshold effects that would only happen if the Hydra had a certain number of heads. After a few weeks of fiddling with the prototype, I turned it over to [Ken Nagle](https://web.archive.org/web/20140327225845/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle), who was leading the design of the product.

### Continuing Quality Improvements

The interplay between design and development is one of the elements that make us very strong as a department. Even though I had what appeared to be a workable game, it was far from as good as it could be. One of the reasons that we have both design and development teams is that we have found that handing our sets over to other people to work on leads to a higher quality product in the end. To that end, what the Hydra needed was someone to spend time coming from a different angle and trying out new things with the product. I had a set of goals that I wanted to accomplish, but so did Ken. He was able to really expand what I had pictured the Hydra was into something far more robust.

When the set came back from design, a lot had changed. Ken did a wonderful job at creating a number of fun and interesting individual designs for the heads and spells, including a few "whammy" spells for the Hydra, which he had found players enjoyed. He also added several rules, such as that Hydra head's abilities turned off when they were tapped, and that you could attack a Hydra head to tap it. This created more of a feeling like you were playing a real opponent that you could interact with instead of a program. It gave me a much better picture of the back and forth that I wanted the encounter to have.

![](https://i.ormos.uk/b0/3d/b03de7e951da1b5792538b10e50c0b78ebce711a384c7c780eebebe0c8265b12.jpg)

I was given the position of the lead for a small team, meeting for about two hours a week, to develop the Hydra. My team was [Erik Lauer](https://web.archive.org/web/20140223104405/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Erik%20Lauer), **Magic**'s head developer, and Charles Rapkin, who works in our organized play department and would be one of the people responsible for messaging and getting stores to run the Hydra Game Day in the future.

The first development playtest showed many of the strengths, as well as the weaknesses, of the design at that point. One of Erik Lauer's biggest strengths as a developer is that he doesn't always follow the rules. While everything had been put into place with a clear goal of what the player was supposed to do, he immediately did the opposite—not killing the heads on purpose. While the tapping of heads gave the player a lot of strategic decisions, they often made the game too easy. A few quick creatures and the player would just "farm" the Hydra heads, turning off the ones that dealt damage and letting the ones that weren't doing much survive until the player had enough of a board presence to kill everything at the same time.

Another round of changes occurred—heads not tapping when attacked, heads "regenerating" by revealing the top two cards, and each untapped head dealing damage. If players wanted to, they could play cards to tap the heads to interact with them (and the Hero cards would give that opportunity), but it meant that they did need to do the "Hydra" thing and actually cut them off at some point.

### Keeping It Simple

One of the items that I had been pushing for and working on from my earliest versions of the Hydra Challenge was a playmat that would contain all of the rules and set-up instructions for the Hydra. My reasoning was that a self-playing game intended for game stores only works if it doesn't require one human to teach it to someone else. There needed to be a way to make the rules as intuitive and easy as possible so a player could play it on his or her own. This did come with some baggage, though. While the upside was that a player didn't have to memorize the rules before beginning, it also meant that the rules needed to fit in a small space, which meant quickly pairing down the rules to the ones that really mattered.

![](https://i.ormos.uk/e2/e0/e2e00475d4faba2811bdb8f3732f32bf7a318a28005c9aba9ae5b9a3c53c5a4c.jpg)

It was during this time that the experience as a whole became far less complicated, but I think also was greatly strengthened as a result. The concept of "elite" and regular heads was added to make it clear how to start the game, as well as giving the game more variety. The elite heads took some of the more fun enchantment abilities and turned them into triggers. It also created more "[You're Gonna Need a Bigger Boat](http://www.youtube.com/watch?v=2I91DJZKRxs)" moments when a normal head died into a elite head.

In some of the feedback I have received, players have noted that the Hydra is weak against cards like [Ratchet Bomb](https://web.archive.org/web/20131025000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ratchet+Bomb) and [Mind Grind](https://web.archive.org/web/20131025000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Grind). Some of the earliest versions of the rules attempted to solve all of these problems, but what I quickly learned was that the attempts to fix everything was just going to require a lot more work than was really worth it. In the earliest attempts to get this to work, I had tried to get every card imaginable to interact in a sensible way with the Hydra, but that just meant the players were constantly rereading the rules text to figure out which printed corner-case was put in place to deal with the current situation. Rather than addressing them one by one, we ended up cutting them down and implementing more generalized rules such as "just have fun." If a player came in with the dedicated goal to trounce the Hydra with a specialized deck, then that player was going to trounce it, and that was okay. It was far more important to keep the rules at a manageable level.

### A Hero's Reward

One of the most useful resources that R&D has for testing our products comes not from R&D, but from one floor above: customer service. If you have ever called us to resolve a problem, chances are you spoke with a customer service representative. One of the perks of working in customer service is getting to come to the Pit on a regular basis to playtest upcoming sets or other products. There is a real risk that the people within R&D can get so into the minute details of game play or design that we miss the blatantly obvious things. Customer service playtesters are wonderful at giving us a preview of how people less familiar with the products will handle what we are producing.

![](https://i.ormos.uk/80/08/80083e366df73478954dc8b8e75652c6ae4f68c3885f346f0618ede80ccf31fe.jpg)

Strike the Weak Spot | Art by [Jason A. Engle](https://web.archive.org/web/20131025000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Jason%20A.%20Engle%22%5D)

Something that we found during playtesting with customer service was that a lot of the Hydra battle was determined in the first few turns, when the player would take a lot of damage and would then just be racing the Hydra. Unless the deck he or she was playing had lifegain, it would feel more like a vice slowly crushing the player than an epic battle. The customer service representatives would often get frustrated as they would go to low life in the first few turns before managing to get a foothold in the game, only to get struck down by a card when the Hydra would live for a few more turns.

It got to the point where they often didn't like killing the heads, because they would often end up in a worst spot than when they knew how much they would be taking in the next turn. We attempted to make the opening turns of the game less brutal, but that often led to matchups where the Hydra posed no real threat. Getting the deck to operate at the exact level in the middle was looking impossible.

When talking with Ken Nagle, he mentioned that a number of video games have reward systems where you can regain health for completing tasks. From this conversation, an idea emerged—giving the player a reward when he or she killed one of the heads, the player would be up on the deal. This is where the hero's reward mechanic emerged. What we found right away was that we could increase the early game potency of the Hydra, and the player would often feel like things were hopeless—until he or she managed to kill a head or two. The player would begin to recover, only for the Hydra to get a lucky break and get the player close to death again. With this one mechanic, the back and forth between the player and the Hydra became a real thing, making the whole experience feel more like an interactive battle than just a clock to race.

That wasn't the final piece of development on the Hydra, but it was the final major change that got it into range of what it is today. A lot of work went into it by a lot of people that I haven't even mentioned here—from Dave Guskin's continuous championing of the project and getting a version of it to be sold on shelves, to creative for concepting and commissioning the artwork and designing the card backs, to our editing team for getting the rules to not only make sense but also work. Every product at Wizards goes through a tremendous number of hands, and all of them are required to make things work as well as they do.

### The Hero's Journey

I am very proud of what we managed to accomplish with the Face the Hydra challenge. I feel we got a lot right in the design and development of the Face the Hydra Challenge Deck, but there is always room for improvement. I have heard a lot of very interesting rules suggestions from different people, as well as ideas on how to modify the challenge to fit different kinds of decks—from Limited to Commander. It was always my hope that, with this project, I could inspire people to try to make their own Challenge Decks or modify this one to better suit what they are looking to compete against.

I hope you all enjoyed this step on the Hero's Path, and I look forward to what we have to offer next year.

Until next time,  
 Sam ([@samstod](https://twitter.com/@samstod))