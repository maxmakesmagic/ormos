---
id: 8wx5ybhb
kind: article
lang: en
path: /en/articles/makingmagic/2012/05-28-planechasing-your-dream
title: Planechasing Your Dream
published: '2012-05-28'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    lang_detected: en
    capture_id: 904361
    url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    captured_at: '2022-09-05 20:25:32+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    lang_detected: en
    capture_id: 904361
    url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    captured_at: '2022-09-05 20:25:32+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    lang_detected: en
    capture_id: 904361
    url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    captured_at: '2022-09-05 20:25:32+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    lang_detected: en
    capture_id: 904361
    url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
    captured_at: '2022-09-05 20:25:32+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: 8wx5ybhb
  url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
  page_key: magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
  lang: en
  template: drupal
  captured_at: '2022-09-05 20:25:32+00'
  capture_id: 904361
  wayback_url: https://web.archive.org/web/20220905202532id_/https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
- document_id: 8wx5ybhb
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/197
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/197
  lang: en
  template: aspx
  captured_at: '2013-06-26 16:14:23+00'
  capture_id: 645421
  wayback_url: https://web.archive.org/web/20130626161423id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/197
- document_id: 8wx5ybhb
  url: https://magic.wizards.com/en/articles/archive/feature/planechasing-your-dream-2012-05-28
  page_key: magic.wizards.com/en/articles/archive/feature/planechasing-your-dream-2012-05-28
  lang: en
  template: drupal
  captured_at: '2022-07-02 09:20:20+00'
  capture_id: 655647
  wayback_url: https://web.archive.org/web/20220702092020id_/https://magic.wizards.com/en/articles/archive/feature/planechasing-your-dream-2012-05-28
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 8wx5ybhb
  capture_id: 904361
  url: https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
  wayback_url: https://web.archive.org/web/20220905202532id_/https://magic.wizards.com/en/articles/archive/making-magic/planechasing-your-dream-2012-05-25
  captured_at: '2022-09-05 20:25:32+00'
  template: drupal
  sha256: f345c53e7a76698d56a082550ad3f57a2b1e35001053bc15998c8c0da6f13b4e
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
*Here in the United States we're observing the national holiday of Memorial Day, and the office at Wizards of the Coast is closed. We'll be back with new columns tomorrow, Tuesday, May 29. In the meantime, since* Planechase *(2012 Edition) releases this coming Friday (June 1), we went back into the archives to share Mark Rosewater's article about the original* Planechase *published in 2009.* 

*So... uh... disregard the bit at the end where he talks about Zendikar spoilers.*

***DailyMTG.com** Staff*

* * *

  

Welcome to *Planechase* Week! In case you've been hiding under a rock, *Planechase* is a brand-new product geared towards multiplayer play. The twist is that your duel keeps jumping from plane to plane (with use of a brand new type of card: plane cards), causing all sorts of chaos to happen to and around you. Today I'm going to explain where this product came from as well as talk about some of the design challenges the team had to overcome.

Speaking of the design team, I think I should start by introducing them to you.

Brian Tinsman (lead)

![](http://wizards.com//magic/images/mtgcom/authorpics/authorpic_briantinsman.jpg)

While Brian's name pops up a lot in my column, let me start by letting you in on something you might not know: **Magic** design isn't Brian's day job. Yes, Brian is in Ramp;D, and yes he's a designer, but his normal responsibilities are overseeing new business design (a.k.a. making up stuff we don't have yet). But Brian's proven to be adept at **Magic** design so we borrow him as much as we can.

Brian's stock in trade as a designer (and the reason he was put in charge of new design) is his love of the unknown. I joke sometimes that Brian's so "out of the box" that he doesn't even know there is a box. Brian just loves exploring the unexplored and venturing out into the proverbial virgin snow of card design, so when Aaron had to figure out who was supposed to lead the very unorthodox "Hopscotch" design (*Planechase*'s codename), Brian was on top of his list—and rightfully so, as Brian and his team knocked this design out of the park.

Aaron Forsythe

![](http://wizards.com//magic/images/mtgcom/authorpics/authorpic_aaronforsythe.jpg)

While Aaron wasn't on the design team from day to day, he gets counted as a member of the team as he was instrumental in creating the structure of what *Planechase* would become. Much more of this below as I let you see in Aaron's own words his initial vision of *Planechase*. Aaron's been on a bit of a design hit streak recently, having led the design of both *Alara Reborn* and ***Magic** 2010*. *Planechase* should only help this streak.

Peter Knudson

![](http://wizards.com//mtg/images/daily/mm/mm54_peter.jpg)

Neither Brian or Aaron needed a real introduction, because if you're a regular reader of Making Magic (and if not, come on, step it up) you hear me talk about them all the time. Peter, though, is a different case. I'm not sure his name has ever come up in one of my articles before (although you might have seen him in [Tom's article on Friday](https://web.archive.org/web/20211130193418/https://magic.wizards.com/en/articles/archive/making-magic/Magic/Magazine/Article.aspx?x=mtg/daily/ld/53)). Peter spent a year interning in Ramp;D before moving on. No matter what Peter was up to, from stickering playtest cards to organizing playtest decks, he did so with a giant smile on his face. So when the *Planechase* design team was being assembled, Peter was asked to join, because Brian felt he would both enjoy it and add a unique insight to the team. Peter threw his all into this design, and much of its success is owed to Peter's time and dedication.

Ken Nagle

![](http://wizards.com//magic/images/mtgcom/authorpics/authorpic_KenNagle.jpg)

Each member of the Pit has their pet issues. One of Ken's is multiplayer play. Whenever a card could be tweaked to make it slightly more efficient or fun for multiplayer play, Ken will make a comment in Multiverse. So when Brian started a design team for a multiplayer product, it was pretty obvious Ken should be involved. I think when Ken was asked if he wanted to be on the design for *Planechase* his response was "Hell, yes."

For those of you that don't remember, three years ago Ken was just another reader of "Making **Magic**". He participated in a little something called [*The Great Designer Search*](https://web.archive.org/web/20120528000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/designersearch/home) which led to him being hired by Ramp;D. In the next six months, you'll see him on three design teams (*Planechase*, *Zendikar* and *Worldwake*), the last of which he led. Ken's come a long way and I see a bright future for him in **Magic** design. (He was just given the keys to the "Action" design—following, of course, "Lights" and "Camera.")

The Planar Chase

![](http://wizards.com//mtg/images/daily/mm/mm54_elaineAndMark.jpg)  

So where does the design of *Planechase* begin. It begins with Elaine Chase. (Hmm, *Planechase* – Elaine Chase; conspiracy theorists go!) Elaine Chase is the brand director for **Magic** (she was recently promoted from brand manager – that position went to Mark Purvis, but I talked about that [a few weeks back](https://web.archive.org/web/20120528000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/50)). This whole thing started because the **Magic** Brand Team (lead by Elaine) was trying to come up with **Magic** products that the multiplayer Free-for-All crowd would enjoy. *Planechase* began with that audience in mind.

Be aware that we didn't start anywhere near the product we ended up with. The first idea (which I cannot tell you because we are probably going to do it some day) was having problems when Elaine pitched the idea of doing something similar to a format called Chaos **Magic**. (This name can be confusing, though, as different groups had different names for this format and some groups use the phrase "Chaos **Magic**" to refer to a completely different format.)

![](http://wizards.com//mtg/images/daily/mm/mm54_pcSplash1.jpg)  

It is hard to pin down where Chaos **Magic** started, as it appears to have been independently created by a bunch of different people/groups. The idea behind it was that it would be fun to create some system wherein things randomly happen and/or environments randomly change. When the changes occurred and what could happen varied from group to group.

Another format that either predated or coincided with Chaos **Magic** (depending on who you ask) is a format known as Enchant World tournaments. This is a format that I was very much involved in, so I understand the progression a little better. Enchant World tournaments started shortly after *Legends* released (back in 1994) and introduced the idea of enchant world cards (now called world enchantments). The tournament followed the flavor of planeswalking, in that the plane that the tournament was being played in kept randomly changing (at the discretion of the head judge) and as it did so it would have ripple effects throughout all the games being played in the tournament. With time we moved away from just using actual world enchantments and started using any global effect card (mostly artifacts and enchantments). I bring up Enchant World tournaments because their flavor was very similar to what *Planechase* became.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120528000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Concordant+Crossroads"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Concordant+Crossroads"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120528000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Abyss"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=The+Abyss"></a></div></div></td><td></td></tr></tbody></table>

So Elaine and the **Magic** brand team came to Aaron Forsythe, in his role as the director of **Magic** Ramp;D, and asked for a multiplayer free-for-all design that played into what made Chaos **Magic** so fun. Aaron thought over the idea and then came up with his take on what the product should be. As I researched this article, I came across the original design spec document (this is what is given to the design team to give them a heads-up and let them know what is expected from them). Four years back, I wrote [a feature article](https://web.archive.org/web/20120528000000/https://magic.wizards.com/magic/magazine/Article.aspx?x=mtgcom/feature/287) in which I showed off the design philosophy document from *Ravnica*. That went over very well, so I thought it might be fun to let you see some of what Aaron put together and then use that to explain some of the key elements to *Planechase*'s design. Note that I'll jump in with a few relevant comments along the way.

Before I begin, I want to be up-front with you guys: due to some confidential stuff, the document you see has been edited. None of the stuff I took out had any great impact on the design itself.

> **Initial Ramp;D Spec – Hopscotch (multiplayer "Chaos Magic")**

The codename for *Planechase* was "Hopscotch." I assume the name was trying to hint at the playfulness/casualness of the product.

> **Aaron Forsythe**

> **\[*Planechase*\] encourages fun multiplayer game play \[...\] and really brings to life the "You are a Planeswalker" concept. The game simulates going from plane to plane and makes you the center of the action as opposed to focusing on pre-fabbed characters like Garruk and Jace.**

As you can see, it was very important to Aaron that this product connect with planeswalkers. Planeswalkers are the main characters of **Magic**, and Aaron saw this product as having the perfect hook to tie into planeswalking. The idea of shifting the fight from plane to plane, I believe, is where the Enchant World tournaments show their influence.

> **Ideal contents of each unit:**  
> 
> *   **60-card Standard-legal deck (a)**
> *   **10 fixed oversized "planar" cards (b)**
> *   **A six-sided die (c)**
> *   **Two inserts (d)**

Another interesting thing to see here is that the basic make-up of the set was created by Aaron before the hand-off to the design team. As you will see, the design team had plenty of problems to work through, but the basic make-up of the product was not one of them.

> **Four different units would be produced.**
> 
> **(a) 60-card Standard-legal deck**  
> **Each unit would contain one of four different 60-card Standard decks, not unlike Theme Decks. They would be built with multiplayer free-for-all in mind, including scaling spells and convoluted combos. Each would probably be two colors.**
> 
> **The "Standard-legal" part is negotiable.**

It turns out the "Standard-legal" part was quite negotiable, as the final product decks can only be described as Legacy-legal. In the end, we decided that people who were likely to enjoy *Planechase* didn't particularly care to be limited to just Standard. As such, the team was allowed to pull cards from throughout **Magic** history.

> **(b) 10 fixed oversized "planar" cards**  
> **The planar cards would be the size of Vanguard cards (about the size of two normal cards side-by-side) but on a more shuffle-able stock. The cards would be laid out horizontally. They will need a specially designed back that ideally incorporates the planeswalker symbol.**
> 
> **Each would be flavored as a plane from the Multiverse (or a part of a plane, so that we could make many different versions of Mirrodin, Ravnica, etc.). Each would have unique art and a game-altering line of text.**
> 
> **Examples:** 
> 
> <table><tbody><tr><td><b>Rootwater, Rath</b></td><td><b>At the beginning of each player's upkeep, he or she returns a nonland permanent he controls to its owner's hand.</b></td></tr><tr><td><b>Brass City, Rabiah</b></td><td><b>Whenever a land is tapped for mana, it produces mana of any color.</b></td></tr><tr><td><b>Otaria, Dominaria</b></td><td><b>Instants and sorceries have flashback equal to their mana costs.</b></td></tr></tbody></table>
> 
>   
> 
> **Each deck would contain 10 unique cards.**
> 
> **Each player in a game using this format is required to have a 10-card minimum singleton planar deck. They can be chosen and combined to best work with decks you've built yourself, much like Vanguard.**

While the product went through numerous changes, the idea of plane cards was a constant from the beginning. You can see that even the deck construction rules for plane cards show up in this document.

> **(c) A six-sided die**  
> **Dice rolling is a key component to the game play; you "planeswalk" randomly on certain die rolls. Ideally this will include a specially-tooled die that has the planeswalker symbol as one face and either the five mana symbols as the other five, or pips in the shape of the five mana symbols (with the planeswalker symbol being "1"). These could be used as promotional items elsewhere, deferring some of the cost.**
> 
> **The tooling of the die is not a deal-breaker.**

Now we get to a key part of the product that Aaron didn't predict 100%. He was correct on the die (and as I'll explain in a moment, even that wasn't a shoo in for most of the set's design), and he was correct with the idea of the planeswalker symbol but he didn't foresee the inclusion of the chaos symbol.

It's All in the Details

From reading the overview, you might think that most of the team's work was done. Aaron had laid out the basic idea, he had the contents of each box, he had the plane cards, he had the die. The rest was just smoothing out the details, right? Wrong. While Aaron did a great job outlining *Planechase*, he left all the details very vague. The design team's job was to figure all these details out. This was not an easy job. I'll walk through the key ones:

**How exactly do players planeswalk to a new plane?**

![](http://wizards.com//mtg/images/daily/mm/mm54_pcDiePw.jpg)

Okay, Aaron laid out a device to add randomness to the decision but how exactly would it work? When is the die rolled? The team started with the idea that the die would be rolled at a preset time each turn. The problem with this was twofold: First, playtesting showed that no matter what time you picked, players would often forget to roll the die. Second, the planar cards needed to generate effects. Some of the effects could be continuous (such as a "[Mana Flare](https://web.archive.org/web/20120528000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Flare)" effect), but others wanted to trigger. It was very important to coordinate when the plane changed with the timing of those triggers. All this leads to the next question:

**How were the planes going to affect play?**

Aaron foresaw the planes as having global enchantment–like effects, but many variants of Chaos **Magic**, which this product was inspired by, also had one-shot spell-like effects. The desire to have the ability to create these effects led to the answer the team was searching for. How do you keep players from forgetting to roll? Make the roll something they want to do. Also, by having something to inspire players to roll, you allow players the option to not roll. This helped fix the problem of players who felt bad because they rolled themselves out of a plane they wanted to stay in.

![](http://wizards.com//mtg/images/daily/mm/mm54_pcSplash2.jpg)  

The other innovation was the idea of allowing rerolls using mana with each roll costing one more than the last. This limited plane jumping early in the game when mana was tight but allowed more flux later in the game when players had access to more mana. Coupled with this idea was the concept that you could create triggers that happened when you came to and left the plane. This would ensure that the act of changing planes would have many dynamic moments. 

**How would the randomness work?**

From reading Aaron's design spec, you might assume that the six-sided die was a given throughout the design. In fact, the design team spent a lot of time trying to figure out if the die was necessary. The team tried everything they could think of to add the necessary randomness without rolling a die. The avenue they spent the most time on was trying to see if the deck itself could provide the randomness. 

The other problem the six-sided die was causing was that the forced once-a-turn roll with a single planeswalker symbol wasn't causing plane jumping to happen enough. As this feature was key to the game play, they knew they had to find a way to make it happen more frequently. It was this desire to increase the frequency of plane jumping that led to the idea of allowing players to pay for more rolls. Once the multiple rolls were added in, along with a second effect on the die, the math started working correctly.

**What planes were they supposed to use?**

One of the key roles of this product was to support the flavor of the game. As such, the Creative Team was very involved in the choosing of the planes. Not since *Time Spiral* block can I think of a product that more rewards the fan who's been paying attention to all the worlds we've visited. The design team spent a lot of time trying to make sure that the mechanic for each world really fit what that world was.

![](http://wizards.com//mtg/images/daily/mm/mm54_pcCards.jpg)  

Which raises a question I know a lot of you are wondering: which came first, the mechanics or the plane? The answer is a little of both. Some planes, such as Lethe Lake and The Eon Fog, were first created as cards that the team thought would mechanically play well, while others, like Shiv, Bant, and Grixis, were created with the plane in mind.

Chase the Plane

The result of all this hard work is what I feel is one of the most innovative things we've designed under my tenure as Head Designer. The best designs are the ones that seem so natural that all the choices seemed obvious. *Planechase* has this in spades. I am quite proud with what Brian and his team were able to accomplish, and I strongly urge you to give *Planechase* a try. I can't think of a product in recent times that has caused more laughing and good times in the Pit than *Planechase*.

![](http://wizards.com//mtg/images/daily/mm/mm54_pcSplash3.jpg)  

That's it for today. Join me next week when *Zendikar* previews begin (although stick around for a little appetite whetting in a moment).

Until then, may you know the joy of jumping from plane to plane.

But Wait, There's More

Back in my column in *The Duelist* (called "Insider Trading"), I made it a habit to give a few teasers in the magazine before a set came out. Players enjoyed them so much that I've continued to do them in Making Magic. So without further ado, here's some things you can expect in *Zendikar*. (A quick note to readers who have never read one of these before: I might not be telling you everything about the cards I talk about.)

![](http://wizards.com//mtg/images/daily/mm/mm54_zenCross.jpg)

*   A card that is a two-card kill combo with a rare card in ***Magic** 2010*.
*   A spell capable of making a 14/1 token.
*   A creature that can sacrifice itself to make a planeswalker go to the graveyard.
*   A legendary octopus
*   A spell that can allow you for no mana to put a creature from your library into play.
*   A card with the reminder text "The land continues to burn..."
*   A card that allows you to pay eight mana for four 4/4 fliers
*   A creature whose rules text includes the phrase "you win the game."
*   A cycle of cards that players have been begging us to print for years.

In addition, here are a few card names from the set:

*   Electropotence
*   Grappling Hook
*   Journey to Nowhere
*   Lotus Cobra
*   Sphinx of Lost Truths
*   Vampire's Bite

And this is just the tip of the iceberg. Definitely come back next week, when I can *finally* talk about my baby.

![](https://i.ormos.uk/8b/b1/8bb1514434d03f5c7657795e0f85266b424dfa24a81d5b70be739ff057ea3e58.png)![](https://i.ormos.uk/1c/81/1c8195ce1a8b449975fa1ac645d73f0ae8e0c2a000a3357f7170096e8a0dd9b7.png)![](https://i.ormos.uk/0f/9a/0f9a62031a3329cc4f623c962ef9df551170ecf0d634d5fa017a34f8d18d493e.png)

* * *

  
![](http://wizards.com//mtg/images/daily/features/banners/AVR_ArticleFooterBanner_FNM_Top.jpg)[![](http://wizards.com//mtg/images/daily/features/banners/AVR_ArticleFooterBanner_FNM_Button01_Static.jpg)](https://web.archive.org/web/20120528000000/http://archive.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/avacynrestored/productinfo)[![](http://wizards.com//mtg/images/daily/features/banners/AVR_ArticleFooterBanner_FNM_Button02_Static.jpg)](https://web.archive.org/web/20120528000000/http://archive.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/avacynrestored/cig)