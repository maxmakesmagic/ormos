---
id: w8z3amrd
kind: article
lang: en
path: /en/articles/makingmagic/2002/05-20-keeping-it-simple
title: Keeping It Simple
published: '2002-05-20'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    lang_detected: en
    capture_id: 222339
    url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    captured_at: '2024-04-16 01:16:28+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    lang_detected: en
    capture_id: 222339
    url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    captured_at: '2024-04-16 01:16:28+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    lang_detected: en
    capture_id: 222339
    url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    captured_at: '2024-04-16 01:16:28+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    lang_detected: en
    capture_id: 222339
    url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
    captured_at: '2024-04-16 01:16:28+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: w8z3amrd
  url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
  page_key: magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
  lang: en
  template: contentful
  captured_at: '2024-04-16 01:16:28+00'
  capture_id: 222339
  wayback_url: https://web.archive.org/web/20240416011628id_/https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
- document_id: w8z3amrd
  url: https://magic.wizards.com/en/articles/archive/making-magic/keeping-it-simple-2002-05-20
  page_key: magic.wizards.com/en/articles/archive/making-magic/keeping-it-simple-2002-05-20
  lang: en
  template: drupal
  captured_at: '2022-01-25 22:21:46+00'
  capture_id: 891168
  wayback_url: https://web.archive.org/web/20220125222146id_/https://magic.wizards.com/en/articles/archive/making-magic/keeping-it-simple-2002-05-20
- document_id: w8z3amrd
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr21,,ja,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr21
  lang: en
  template: classic_asp
  captured_at: '2004-11-30 12:54:27+00'
  capture_id: 1974007
  wayback_url: https://web.archive.org/web/20041130125427id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr21,,ja,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w8z3amrd
  capture_id: 222339
  url: https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
  wayback_url: https://web.archive.org/web/20240416011628id_/https://magic.wizards.com/en/news/making-magic/keeping-it-simple-2002-05-20
  captured_at: '2024-04-16 01:16:28+00'
  template: contentful
  sha256: d32055bf5b965f607f8504e832b1a6c9e2adfecf16be6a383ed710389c8c52ef
render_recovery: []
---
“Design is an art; development is a science.” -- R&D saying

About once a month I’ve been trying to take a sensitive issue and explain the reasoning behind it. This month, the topic is the role of simplicity in design.

**Magic** is a very complex game. Its players, on average, are quite smart. Why, then, does R&D go to such lengths to make the cards as simple as possible? Why do we include obvious reminder text? Why do we refuse to redo some cool older card mechanics? What’s R&D up to? Are we drifting from Richard Garfield’s original vision? Are we “dumbing down the game?” What’s going on?

Ironically, the issue of simplicity is a complex one. But I hope in my column today to give you all a better idea of why it’s so important and to explain how it’s actually improving the game. Bye bye, frying pan. Hello, fire!

### Looking Ahead

Let me start by stating the role of a **Magic** designer (or developer): to make **Magic** the best game possible. Not just for next year, but for next century. If my column does nothing else, I want to convey how much time and energy R&D spends to achieve that goal. We understand that we are working on a classic. As such, we feel a great responsibility to think long term about the game. Yes, gasp, R&D has been forced to have vision. What does this have to do with simplicity? Everything!

Here’s **Magic**’s long-term problem. It’s a complex game -- a complex game all about breaking its own rules. Every new card we create adds to this complexity. And the problem only snowballs as each new card has one more card than the last that it can interact with. Plus, we have no plan on stopping. Add to this problem, the following: The rulebook grows by the size of the American Constitution every four months. And the average player doesn’t even own one.

That presents R&D with a real challenge. How do we keep the game fresh without causing it to collapse in on itself? The answer: simplicity. Not of strategy but of card design. Let me explain. The game of **Magic** is about the interaction of the cards. Two very simple spells, for example, can have a complex interaction. Thus, the complexity of the game can rest on the card interactions. The individual cards do not need to be complex. A better way to think of this is to look at the game of chess. Any one chess piece is rather straight-forward. And the overall rules can fit on a single page. Yet, chess has a rich, strategic depth. The same holds true for **Magic**. Card simplicity does not eliminate strategic complexity. In short, this means that choosing to make the cards as simple as possible does not “dumb down the game.” It simply moves the complexity from the cards to the card interactions.

I offer up *Odyssey* as proof of this contention. While all the cards are pretty straightforward, the interaction between threshold, flashback, and the graveyard has made for a complex game (especially in limited). R&D is not out to rob **Magic** of any of its richness. Quite the opposite, actually. We’ve realized that **Magic**’s longevity rests on the elegance of its pieces (aka cards), but its heart as a game lies in the interaction of those pieces. The beauty of chess lies not in the queen but in the queen’s gambit. Or in **Magic** terms, it’s not the [Ancestral Recall](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall) that gives the game its heart, but the concept of card advantage.

### For Art’s Sake

I believe that design as a creative endeavor is an art form. As such, I actually treat my design as I used to treat my writing. (For those coming in late to my column, before working at Wizards I was a writer in Hollywood.) One of the key lessons I learned about writing was the importance of brevity. “Art,” one of my favorite teachers would always say, “is the act of expressing as much as possible with as little as possible.”

In screenwriting, for example, I was taught that you begin every scene as late as you can and exit as early as you can. All that should exist is what needs to exist. This is the other side of the coin of simplicity: aesthetics. This is a sub-topic too big for this article so I’ll have to promise to cover it in a future column. I mention it here because it is the other important reason for simplicity. Keeping the cards simple enhances them in a subtle but very potent (and poetic) way.

### Nuts and Bolts

Enough of the big picture. Let’s get down to the practical implications of simplicity. How does it affect the design of cards? Well, in four important ways: removing needless text, removing needless mechanics, consolidation, and focusing the rules of the cards. Let’s attack these one at a time.

### Removing Needless Text

One of the most basic ways to simplify cards is to eliminate needless text. Needless text is defined as rules text that has little to no impact on the game. Most often the text exists as a way to add some flavor to the card. A perfect example would be the card [Castle](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Castle) from Alpha. (“Your untapped creatures gain +0/+2. Attacking creatures lose this bonus.”) The last sentence, “Attacking creatures lose this bonus,” was added specifically to keep the card from affecting attacking creatures that didn’t tap to attack. (Only [Serra Angel](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Angel) in Alpha.) How often does that interaction happen? Not often. Is it worth a second sentence? R&D decided no and changed the card for *Sixth Edition*.

So what do five words matter? Why even bother to make a fuss? Because the biggest threat to **Magic**’s long-term health is not the large excesses (they’re easy to catch) but the accumulations of small ones. Text space is a valuable resource. If it doesn’t do enough, it has to go. I like to think of this as a weight loss regimen for the game. To stay healthy, it has to stay trim.

### Removing Needless Mechanics

At its heart, **Magic** is a game of exploration. And not just for the players. R&D uses new sets to try out new mechanics. Sure, we can play test them, but nothing really shows a mechanic’s mettle like millions of players slugging it out. Some mechanics will succeed while others will fail. Part of R&D’s job is deducing which are the former and which are the latter. The successes will see print again while the failures will not. This is probably the most controversial category as many players feel that once an idea is introduced it is forever part of the game.

A good example of this would be the ability banding. Introduced in Alpha, banding was a staple ability that appeared in all expansions as well as the basic set. By *Weatherlight*, R&D realized that it was inherently flawed. The reason? Too many players simply didn’t understand how it worked. R&D took a lot of heat for removing banding. But banding's supporters didn’t understand why it had to go. *They* understood it.

The focus was, unfortunately, on what *left* the game. What people didn’t notice was what R&D added to take its place. You see, R&D liked the flavor of banding. It felt strongly that part of white’s flavor was the ability for the horde of small creatures to take down a big creature in combat with minimal loss. But rather than accomplish it with one confusing mechanic, R&D chose to replace it with numerous simpler mechanics that in conjunction produced a similar effect.

To that end we loaded white with numerous weenie-aiding abilities: [Advance Scout](https://web.archive.org/web/20020520000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Advance%2BScout) (granted to itself and others), [Heavy Ballista](https://web.archive.org/web/20020520000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Heavy%2BBallista) (“T: CARDNAME deals N damage to target attacking or blocking creature”), [Angelic Page](https://web.archive.org/web/20020520000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Angelic%2BPage) (“T: Target attacking or blocking creature gets +N/+N until end of turn”), [Honor Guard](https://web.archive.org/web/20020520000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Honor%2BGuard), and [Vigilant Martyr](https://web.archive.org/web/20020520000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Vigilant%2BMartyr) (“Sacrifice CARDNAME: Regenerate target creature”). Thus, a similar flavor was created without the need for confusion.

It’s important for R&D to have the ability to experiment. **Magic** without experimentation would be a boring, predictable world. One of the side effects of this experimentation is that some ideas will disappear never to be seen again. But have faith in R&D that if the mechanic filled an important role, we will find a new way to accomplish the same goal.

### Consolidation

Another one of the steps R&D takes to simplify the game is consolidation. What this means is that R&D is always looking for ways to group similar cards together. A good example of this is creature types. Back in the day, we made new creature types without thinking. The more detailed the better. [Zephyr Falcon](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zephyr+Falcon) was a falcon. [Osai Vultures](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Osai+Vultures) was a vulture. [Birds of Paradise](https://web.archive.org/web/20020520000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) was a mana bird. This was flavorful but created a big problem. What if we wanted to make a card that connected a number of related creatures, such as birds? A bird lord with the power to command his feathered friends seemed obvious and cool. But the game didn’t allow it. So, we did what R&D always does when we examine a potential change, we looked at all the options and decided which would make the game better.

Which is better we asked, to have a diversity of flavor or to have greater interactivity of the cards? Is **Magic** a better game for having falcons or is it better because you can build a deck with a bird theme? As we looked into it we realized that consolidating all the birds didn’t eliminate falcons flavor-wise. The title and art could still convey "falcon-ness." And you could still build a deck of all falcons. But by making all birds into creature type bird, we allowed players to mix and match their birds. Consolidation of creature types created diversity in deck building options. This is a good example of how simplicity can at times expand the games’ interactions.

### Focusing the Rules on the Cards

As I explained earlier, **Magic** rules are becoming more and more unwieldy. In order to compensate for this, R&D has been putting responsibility for the rules on the cards themselves. Players may not read the rulebook, but they have to read the cards. The ramification of this shift is two-fold. First, it adds an important restriction to design. Cards can only have abilities that can be explained on the card itself. This means an ability like phasing which requires pages of rulebook support to explain will never again see the light of day.

I’m sure this will upset some of you as it seems R&D is limiting what we allow ourselves to do. And we are. But for a very important reason. We don’t want **Magic** to become a game where only a few informed people can play. Rather, we are embracing Richard’s original vision of **Magic** where the game existed in the cards. Every time a card forces a player to leave the game to find a rulebook, the game loses an integral part of what makes it special. **Magic** has to live in the cards. The world of possibilities within this restriction is immense. I promise that R&D will still be able to deliver whole new worlds of richness.

The second impact of this philosophy is the reliance on reminder text. I know this is a touchy issue. Numerous emails I’ve received go on for at least a paragraph about how **Magic** players know “walls can’t attack.” (A quick side note -- reminder text for many common terms, including walls, has recently been removed from the expert expansions.) My response is that reminder text serves a vital role, one so important that I think players need to be more tolerant. Reminder text keeps the game in the cards and ensures an influx of new players. Without these two factors, **Magic**’s long-term health is in jeopardy. As such, I feel it’s worth the small aggravation of skipping over the occasional line of italic text.

### So It Goes

As you can see, each decision R&D makes takes into account a very sweeping vision of the game. We do not simplify to lessen the game, but to strengthen it. We are pruning to protect what remains. Hopefully, this column has given you some hefty thoughts to chew on. As I hope most my columns illuminate, designing (and developing) **Magic** is a very complex endeavor. But one thing remains simple, our goal: to make **Magic** the best game ever.

Join me next week as I take a peek at the token creatures of **Magic**.

Until then, may you enjoy the elegance of a single **Magic** card.

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*