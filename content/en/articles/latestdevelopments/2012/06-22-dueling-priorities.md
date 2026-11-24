---
id: 1q38zada
kind: article
lang: en
path: /en/articles/latestdevelopments/2012/06-22-dueling-priorities
title: Dueling Priorities
published: '2012-06-22'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    lang_detected: en
    capture_id: 721237
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    captured_at: '2022-10-03 10:23:52+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    lang_detected: en
    capture_id: 721237
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    captured_at: '2022-10-03 10:23:52+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    lang_detected: en
    capture_id: 721237
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    captured_at: '2022-10-03 10:23:52+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    lang_detected: en
    capture_id: 721237
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
    captured_at: '2022-10-03 10:23:52+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 1q38zada
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
  page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
  lang: en
  template: drupal
  captured_at: '2022-10-03 10:23:52+00'
  capture_id: 721237
  wayback_url: https://web.archive.org/web/20221003102352id_/https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
- document_id: 1q38zada
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/200
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/200
  lang: en
  template: aspx
  captured_at: '2013-07-07 19:22:40+00'
  capture_id: 618560
  wayback_url: https://web.archive.org/web/20130707192240id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/200
- document_id: 1q38zada
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-21
  lang: en
  template: drupal
  captured_at: '2022-07-07 08:19:10+00'
  capture_id: 721233
  wayback_url: https://web.archive.org/web/20220707081910id_/https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-21
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1q38zada
  capture_id: 721237
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
  wayback_url: https://web.archive.org/web/20221003102352id_/https://magic.wizards.com/en/articles/archive/latest-developments/dueling-priorities-2012-06-22
  captured_at: '2022-10-03 10:23:52+00'
  template: drupal
  sha256: 7645564cd9e4baaaf2167c1264d670f74dca874b695d01d2a5be7982718fb7e5
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: http://archive.wizards.com/magic/flipcards/flip.html?ca=Delver%20of%20Secrets&cb=Insectile%20Aberration&lang=en
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
I write my articles on Thursday and Friday a week before they’re posted, which means I can do nifty tricks like load up **DailyMTG.com** on my web browser and copy-paste stuff. Last week, apparently I promised to talk about "How we develop both **Duels** and the sets (like ***Magic** 2013—*my first lead!) that tie in with it."

Man! I’ve been writing for like fifteen seconds and already have an article idea. How lucky!

So I suppose I’ll do just that. This looks like it’ll be another two-parter. First, I want to talk about the development process of **Duels**, or at least how *I’ve* approached that process for the last three games. Second, I’ll talk about what it’s like to develop a core set with **Duels** in mind.

Okay. Ready, and, break! Go! Fight! Win!

### Fight Club

We have an entire digital team at Wizards full of awesome people and an entire team at Stainless Games full of awesome people who do most of the game-design work for **Duels**. Combined, their efforts help create the structure of the campaign, the ladder, features, mechanics, and narrative progression, as well as designing the AI, the UI, the graphics, and most of the overall "arcade" experience **Duels** is famous for.

![](https://i.ormos.uk/12/d7/12d76941db9d4be48c88ffc390c01182d3a48fd1e987104bc0f330d67af14a20.jpg)

[Chandra, the Firebrand](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%2C+the+Firebrand) | Art by [D. Alexander Gregory](https://web.archive.org/web/20120622000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22D.+Alexander+Gregory%22%5D)

What’s left to traditional development—although increasingly Wizards Digital is tackling this task as well—is deck design and balance.

So how do you go about doing this? What does design mean for **Duels** that it doesn’t mean to "regular" **Magic?** How is balancing a **Duels** matchup different from balancing a regular metagame, or from balancing a Limited environment?

I’d say the first step is to zoom out a little bit and talk about the big picture. As I’ve mentioned before, **Duels** piggybacks off the structure of traditional one-on-one fighting games and draws inspiration from some of the mechanics that make those games work. The most important one, to me, is *identity*. Each character in a good fighting game has a unique personality, and that personality is evoked by every aspect of that character: special moves, special combos, costuming, play pattern, movement, poise, taunts—you name it. It’s telling that Ken and Ryu from *Street Fighter II*, identical at first, were quickly differentiated along the axis of Fireball/Dragon Punch. As a game designer, you want definition, because definition broadens the overall experience and creates opportunities for player investment in the characters.

How does that apply to **Duels?**

If I’m balancing, say, a Standard red deck, what I care most about are how that deck’s games play out against a weighted cross-section of the format. I focus my attention on what the cards *do*. For **Duels**, what’s even more important is how the cards *feel*. Chandra is your red mage, and Chandra casts fire spells. Not rock spells, not lightning spells—fire spells. Her play pattern should feel like that of a pyromancer, not that of amalgamated game mechanics differentiated across the color pie. That means a lot of shotgun-blast burn spells, hard-hitting but vulnerable creatures, and strategic rather than tactical subtlety (she’s not just going to set *anything* on fire—but she’s definitely going to set *something* on fire).

<table><tbody><tr><td><img src="https://i.ormos.uk/d4/62/d46204a8025235ad0646a3fc7a8a31e2022711d8a0738263cda178846542c665.jpg"></td>&#10;			<td><img src="https://i.ormos.uk/22/e0/22e08ca419c5b997bbac0894c56e4568b9324d93a6ea24ae3e7f4cac3a7448be.jpg"></td>&#10;		</tr></tbody></table>

Contrast this, then, with Krenko, Mob Boss. He’s another red **Duels** deck, but he plays out totally different from Chandra. Boy digs himself some goblins, and the only thing he digs even more are—*more* goblins! He has a much more creature-oriented feel and boasts a play pattern far more characteristic of a seedy underworld kingpin than a feisty fire-prodigy.

So when you’re designing a deck for **Duels**, you really want to start out with a character and a feel. When I was designing the Karn deck for **Duels** 2012, I knew he was a giant silver golem with legendary, almost unrivaled power. When I designed the Nissa deck, I knew she drew most of her strength from the Elves she corralled to her side. When I designed the Kiora deck, I envisioned her as a primeval summoner of the deep with ancestral, almost religious devotion to the creatures she controlled. I believe these visions panned out in the way these decks played, and that play pattern captures those feelings of identity and investment that are so important to the **Duels** experience.

Obviously, though, you can’t just cobble cards together into decks and call it a day. You have to balance them against one another; otherwise, the experience you spend so much time cultivating will dissolve as players realize most of the choices you present to them aren’t really choices at all.

What’s different about **Duels** in relation to regular **Magic** is that it’s a closed environment. In Standard, people can alter their decks however they want in response to whatever they want, so it’s kind of a quantum system where the more you engineer, the less you can be confident exactly what you’re engineering. Instead, the one constant you want to try and ensure is *change,* which is why you try to ensure as much as possible that power levels are relatively flat and a variety of counter-strategies are available for most conceivable dominant strategies. Similarly, for Limited, people are going to open and draft different product every time, so you get to generate a lot of that variance from the system itself.

In **Duels,** you know exactly which options are available to each and every deck. Everything is comparatively fixed, so you’re not trying to ensure *change* and *evolution* as much as you’re trying to ensure fun play patterns and a relatively normalized overall power level. Your metagaming happens on a deck-by-deck level, rather than card-by-card, as some strategies are naturally favored over other ones. Because I was involved in leading ***Magic** 2013*, I didn’t get a chance to dive into **Duels** 2013 deck development like I did across the previous two iterations. But I did get my paws dirty on a card or two here and there.

### Learning to Walk Again

So that’s how you work on **Duels**. But what happens when you need to work on a **Magic** set that’s all about **Duels?**

That’s what ***Magic** 2013* Lead Designer Doug Beyer and I were charged with doing, along with our respective teams, almost two years ago. We were to create an *integrated* experience that tied **Duels** and "paper **Magic**" products together in an unprecedented, paradigm-setting way. We’d be *starting* with another game, and building an experience to highlight it, and that entailed a fundamentally different process than most of our other sets.

![](https://i.ormos.uk/f7/a8/f7a8a5e8c2ac796056515a1cfb07bbe83d52468c689892f2ff6396764cf655ba.jpg)

[Nicol Bolas, Planeswalker](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) | Art by [D. Alexander Gregory](https://web.archive.org/web/20120622000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22D.+Alexander+Gregory%22%5D)

One thing was clear to me from the start: I would *absolutely not* compromise the integrity of the **Magic** set itself in service to this goal. As Lead Developer, I *poured* myself into this set. I have devoted more time and care and attention into ***Magic** 2013* than anything else I’ve ever created. It’s my baby. I want to snuggle with it. And I was not about to sacrifice the beauty of the resulting work to execute some kind of marketing tie-in.

<table><tbody><tr><td><img src="https://i.ormos.uk/2d/5c/2d5ce0ba83a4ab09cbb74616252a019a0844c465a37d39b46a40849d004a5e16.jpg"></td>&#10;			<td><img src="https://i.ormos.uk/ae/11/ae116a1ff2da1a29b3715976b02115e3a5ea2595c9c6173285b4929ebcd3c122.jpg"></td>&#10;		</tr></tbody></table>

Fortunately, we didn’t have to. As veteran **DailyMTG.com** readers have heard a zillion times by now, *restrictions breed creativity*. True to form, the **Duels** tie-in sparked innovative ideas and solutions that make ***Magic** 2013*, in my mind, the most exciting core set since ***Magic** 2010*. But we had to do a few things differently.

The broadest adjustment was this: we knew **Duels** would be structured around our five legendary bosses, and that you could only include one copy of each boss card in the **Duels** deck. That meant that the set had to have enough boss-centered real-estate to convey the feel of each character successfully. It also meant that the bosses themselves needed to have distinct enough personalities that such a feeling would actually be of substance—you can’t, you know, create an interesting deck that feels like a French-vanilla 4/4 flier, or whatever.

Our solution was to create what we called "Timmy Build-Arounds," or characters that lent themselves to certain strategies by producing big effects when you bought into that strategy. This allowed the **Duels** decks to feel distinct while having the totally awesome side effect of seeding a bunch of Limited archetypes into the set from the get-go. What that means is that even though ***Magic** 2013* is a core set, we’ve tried to weave some of the cool, atypical build-arounds that characterize expansion-level Limited into this set, too. We’ll see whether that pans out once the set is released, but those archetypes form the core of some of the boss decks in **Duels** as well.

<table><tbody><tr><td><img src="https://i.ormos.uk/b3/7d/b37d1bf28af363e61ccd1bc34bd9028847a72a8cd1739f50971105eded9b616d.jpg"></td>&#10;			<td><img src="https://i.ormos.uk/34/24/34241cc4009c324d9a7657c90ad553c907d6dac61e9c78ee32bce5803d43a944.jpg"></td>&#10;		</tr></tbody></table>

Another important structural change was that we knew the plot of **Duels** 2013 would center around jumps from plane to plane. After all, **Magic** is about Planeswalkers, and to make planeswalking feel special you have to catch a glimpse of all the vast and possibility-rich worlds that characterize the **Magic** universe and make it so compelling. What this means is that ***Magic** 2013* departs a *little* bit from the generic top-down fantasy feel that has characterized the last three core sets. Now, when I say "a little" I mean just that. For the most part, we’re focusing on the same trope-intensive fantasy-world resonance that has made the past few sets so successful. But we’re *also* trying to seed the set with dynamic images of **Magic’s** diverse planescape—Innistrad, Ravnica, Shandalar, Alara, all of it. In **Magic**, there’s not just one world to explore and, to me, that’s kind of awesome. ***Magic** 2013* attempts to showcase that*.*

![](https://i.ormos.uk/40/f2/40f22dc7908489ad7616b317ac45caaa56d4aa15ccf4d378491b11a47e142da4.jpg)

Finally, of course, every good game has got a villain. And who’s more villainous in **Magic’s** universe than the man himself, good ol’ [Nicky B.](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) We knew **Duels** would build to a climactic battle with the notoriously nefarious master-schemer, and so we knew we wanted him to feature prominently in the set. That meant, for the first time ever, we’d have a gold card in the core set—along with *six* Planeswalkers instead of the usual five. Moreover, [Nicol Bolas](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) is not exactly the kind of guy to chill, sit back, and function as a figurehead for something. He’s no mere poster-boy. He commands *respect*, and he has *earned* it, and he’s going to demonstrate that to you by showing up on battlefields and smashing face. To that end, we’ve put a *lot* of cards into the set that ought to help you cast the guy. While ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) might look like a lot—and it is—he’s definitely quite the stomping once he comes down.

How good will he turn out be in the end? Well, obviously I can’t say for sure, but I know it’s getting kind of lonely out here being the only person to have Top 8ed a Pro Tour playing [Nicol Bolas, Planeswalker](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) in my deck. I’d love some company, and I’d be lying if I said I haven’t taken a step or two to try and get him to show up.

### Pieces of You

**Duels** has influenced ***Magic** 2013* in other, more subtle ways too, of course. Each boss has a card pointing to him or her, and we went to great lengths to ensure a large overlap between ***Magic** 2013* cards and **Duels** 2013 decks. If you have friends new to **Magic** who got their start in **Duels**, they’ll find ***Magic** 2013* very familiar and welcoming. The end result is, I believe, an experience that works out better for players of both games. But don’t just trust me because I’m the one talking to you—try out **Duels** for yourself! The game carries an absolutely *insane* value for the price, and we even kick you back a couple exclusive promo cards for trying it out. We’re releasing this year on more platforms than ever before, including—for the first time (perhaps most excitingly)—the iPad. So I guarantee you there’s some device on which you can play **Duels** conveniently. It’s worth it; I promise.

As for ***Magic** 2013*, which releases next month?

I myself can’t wait.

 

Finally, I should talk briefly about the recent B&R changes, which you can find [here](/en/articles/feature/2012/06-20-june-20-2012-dci-banned-restricted-list-announcement). Arguably, the biggest news might be the *lack* of news—that in Standard, no cards were banned. We’re very aware of the high percentage of White-Blue Delver decks in the field and are following that trend very closely, so we hope y’all understand that we’re paying a lot of attention to the format and are taking the evolution of the metagame very seriously. But when you compare its win percentage to other previously dominant decks—obviously excluding mirror-matches—it’s nowhere near in the range of something like Caw-Blade or Faeries. We looked at numerous tournaments, both in real life and on **Magic Online**, and the deck’s win rate hovers very close to 50%. Moreover, certain popular decks boast very strong matchups against Delver, and those results hold up over multiple events. Most importantly, tournaments attendance isn’t falling; in fact, it’s at an all-time high! The deck certainly puts people into the Top 8, and the deck certainly can win once it gets there—but so can other decks, as we’ve seen on the independent tournament circuit and at World **Magic** Cup Qualifiers. When you take all of that into account, it just doesn’t make a lot of sense to ban a card right now and not let y’all play with the decks you’ve spent so much time and effort putting together. We’re aware, of course, that some of the best players in the world are winning an awful lot with White-Blue Delver decks, and we’re certainly not contesting that the deck’s power skyrockets in the hands of a very capable player. It’s simply that when making decisions like this, it’s important for us to consider the format as a whole.

That said, we’re keeping our eyes open and are certainly willing to take action if Delver starts to threaten the format more severely.

<table><tbody><tr><td>&#10;			<div>&#10;			<div>&#10;			<div><img alt="1624" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;multiverseid=1624"></div>&#10;			</div>&#10;			</div>&#10;			</td>&#10;			<td></td>&#10;		</tr></tbody></table>

The second big piece of news was that we un-banned [Land Tax](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Land+Tax) in Legacy. Tax is one of the most powerful cards we’ve ever printed, but we’re hoping it will contribute to the diversity of a format in which white is comparatively under-represented. We’re keeping an eye on some of the format’s other powerhouses—it turns out the "pay life to draw cards" mechanic is still *really* good after all these years—but right now we want to see what the introduction of [Land Tax](https://web.archive.org/web/20120622000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Land+Tax) winds up doing.

Feedback, of course, is vital to the process, so we welcome your thoughts. Speak up in the forums, or send me an email, or get a hold of me on Twitter and let me know what you think!

Zac ([@zdch](https://twitter.com/#!/zdch))