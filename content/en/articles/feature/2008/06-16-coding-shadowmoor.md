---
id: 1ejkhzc2
kind: article
lang: en
path: /en/articles/feature/2008/06-16-coding-shadowmoor
title: Coding Shadowmoor
published: '2008-06-16'
column_slug: feature
column: Feature
authors:
- slug: ryandhuse
  name: Ryan Dhuse
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    lang_detected: en
    capture_id: 614724
    url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    captured_at: '2017-08-16 03:53:12+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    lang_detected: en
    capture_id: 614724
    url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    captured_at: '2017-08-16 03:53:12+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    lang_detected: en
    capture_id: 614724
    url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    captured_at: '2017-08-16 03:53:12+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    lang_detected: en
    capture_id: 614724
    url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
    captured_at: '2017-08-16 03:53:12+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: 1ejkhzc2
  url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
  page_key: magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
  lang: en
  template: drupal
  captured_at: '2017-08-16 03:53:12+00'
  capture_id: 614724
  wayback_url: https://web.archive.org/web/20170816035312id_/http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
- document_id: 1ejkhzc2
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/462&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/462
  lang: en
  template: aspx
  captured_at: '2009-06-03 17:05:14+00'
  capture_id: 259835
  wayback_url: https://web.archive.org/web/20090603170514id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/462&print=true
- document_id: 1ejkhzc2
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/462&=RSS-MTGCOM
  page_key: wizards.com/default.asp?=RSS-MTGCOM&x=mtgcom/feature/462
  lang: en
  template: classic_asp
  captured_at: '2008-06-19 13:29:17+00'
  capture_id: 1262036
  wayback_url: https://web.archive.org/web/20080619132917id_/http://www.wizards.com/default.asp?x=mtgcom/feature/462&=RSS-MTGCOM
- document_id: 1ejkhzc2
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/462,0
  page_key: wizards.com/default.asp?x=mtgcom/feature/462
  lang: en
  template: classic_asp
  captured_at: '2008-07-08 12:28:55+00'
  capture_id: 2019932
  wayback_url: https://web.archive.org/web/20080708122855id_/http://www.wizards.com/default.asp?x=mtgcom/feature/462,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1ejkhzc2
  capture_id: 614724
  url: http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
  wayback_url: https://web.archive.org/web/20170816035312id_/http://magic.wizards.com/en/articles/archive/feature/coding-shadowmoor-2008-06-16
  captured_at: '2017-08-16 03:53:12+00'
  template: drupal
  sha256: 205210a3c02522134f21387a4389f5454a64873c32f742426c126e2faf25c79d
render_recovery: []
---
Hello everyone! My name is Ryan Dhuse (pronounced just like when you're tied in tennis. Don't worry, the silent "H" gets everyone). I'm the lead for the Client and Rules Engine Team for **Magic Online**. You're probably familiar with the position, even if you're not familiar with me. It's the position that Michael "elf" Feuell had before his promotion. 

My team is responsible for coding new card sets and ongoing client development. Over the last couple of months, we've been focusing on some client fixes that are in the pipeline to be released soon.

As I write this, we're currently finishing up card coding for *Eventide*. We'll be challenging R&D to an online draft within a week or two. It's always a toss-up as to whether their greater experience with the set or our zealously guarded knowledge of the few remaining rules bugs wins out. Either way, it's sure to be an epic battle. 

During the *Shadowmoor* development process a few months ago, I collected some screenshots and stories that I'd like to share. When you take a look at the screenshots in this article, you're sure to notice something strange. *Shadowmoor* in 2.5! Even though it was never seen outside the walls of Wizards, the majority of the *Shadowmoor* rules coding was done in 2.5 long before **Magic Online** 3.0 was launched. Because the rules engine is shared between the two systems, it was an easy transition to move it over to 3.0 when the time came. 

[![Air_Elemental](https://i.ormos.uk/f7/be/f7bed7325d288afbf2e9e3d0383f914ebe85ce553dc4f86a13b6a804277ea610.jpg)](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Air%2BElemental)You will also notice a strange card with alpha [Air Elemental](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Air+Elemental) art on a land. That's a special card called Library of Congress that we have to aid development and testing. We use it to quickly set up a game state when we're testing something by hand. Its full card text is:

Library of Congress counts as a basic land.  
 You may pay ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif) rather than pay the mana cost for spells that you play.  
 You may play nine additional lands on each of your turns.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Choose up to nine cards you own from outside the game and put them into your hand.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): End the turn.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Search your library for a card and put that card into your hand. Then shuffle your library.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Choose up to nine cards you own from outside the game and shuffle them into your library.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Draw a card.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Target creature gains haste until end of turn.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): ~this~ deals one damage to target creature or player.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Untap target permanent.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Tap target permanent.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): You gain 50 life.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Destroy target permanent.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Return target permanent to its owner's hand.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Return target card from your graveyard to your hand.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Add ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) to your mana pool.  
![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Add one mana of any color to your mana pool.

Oh, and thanks to elf, all of its abilities have split second, even before it was a keyword. You can also thank him for that fact that it has creature type Elf, before the tribal type was ever invented. Beware if a dev ever challenges you to a freeform game!

I'm here today to talk about some of the amusing things that came up during *Shadowmoor* development on **Magic Online**. [Midnight Banshee](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Midnight+Banshee) had a bug that seemed pretty powerful at first glance. Our first attempt at coding it resulted in it putting -1/-1 counters on not just the nonblack creatures in play, but those in every other zone as well. Hand, library, graveyard, sideboard, it was all fair game. Of course, counters don't persist across zone changes, and there is no state-based effect check to kill creatures with less than 0 toughness when they aren't in play. If you look at it this way, it had no more effect to the user than a display bug, but a very amusing one nonetheless.

![](https://i.ormos.uk/f3/2d/f32da6086128a5f31ea8a636607f7985ac8698ae0c3e2ca617507396559132d5.png)

This situation could never happen in real life, but it makes great creative fodder for online-only cards such as avatars. How about "All cards in your hand with a discount counter on them cost up to ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif) less?" or "Search your library for a card with a bookmark counter on it?"

Sometimes bugs make cards worse, but sometimes that make them a *lot* better. [Wooded Bastion](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wooded+Bastion) was one card that got a power-up. Very early on, any activated abilities that cost ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green-white.gif) were considered to be planeswalker abilities by the rules engine. You didn't have to pay any mana to activate them, only add loyalty counters. This wouldn't have been so bad if the "can only be played once a turn" restriction was in place, but that's tied to the planeswalker card type. [Wooded Bastion](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wooded+Bastion) isn't a planeswalker, it's a land. The net result was that you could activate its ability as many times as you wanted, putting a loyalty counter on each time. Who doesn't love a one-card infinite mana combo?

[Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King) had his share of amusing issues as well. His converted mana cost was a *little* off initially. We represent mana symbols in the code with one character. 0–9 are easy, but it gets a little less obvious after that. ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif) is "a", ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif) is "b" up through ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless6.gif) ("g") for [Draco](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Draco).

Before we coded the monocolored hybrid (or "twobrid") mana symbols into the rules engine, [Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King)'s mana cost was coming through as the more human-readable "2/w 2/u 2/b 2/r 2/g". The code went through that string looking for things it recognized. It found five 2s, a "b", and a "g". So of course [Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King)'s mana cost became 2 + 2 + 2 + 2 + 2 + 11 + 16 = 37. He was an awesome combo with [Riddle of Lightning](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riddle+of+Lightning) before that one was fixed. My opponents never saw it coming!

[Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King)'s other issue was the sheer amount of ways that you can play it. If we went with the method we use for other hybrid cards, [Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King) would've had 32 distinct options when you clicked on it in your hand. During testing, every time someone went to play it, they would have to carefully scroll through the many available options before misclicking, having to cancel, and starting the process again. Basically, the game ground to a halt any time [Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King) was about to be played. 

This was unacceptable. After a little brainstorming, we came up with a design that focused on reducing the number of clicks and time it takes to play [Reaper King](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King). When you're lucky enough to draw one for the first time, you'll find that you click on it and ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif) shows up in the prompt box. You can toggle between paying ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif) and any colored mana by clicking on the appropriate mana symbol in your status area. Once you have the cost you want, you hit "Okay" to lock it in. We could've had it start as ![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), but you would have to click on the mana symbols you *don't* want to use, and that is counterintuitive.

![](https://i.ormos.uk/b3/52/b3528f142f02a656eb297ba99eeaab66e0a853de89f6d9b76cbf6eeb2e413e73.png)

I wasn't working for Wizards during *Coldsnap* development, but I've heard the story of the snow mana symbol showing up as a pig icon during the beta test. *Shadowmoor* had its own brand of symbol shenanigans, as you can see. I still chuckle every time I see the reminder text. "\[winkey smiley face\] is the untap symbol." Somehow I don't think an emoticon made the short list of possible untap symbols when R&D was typesetting *Shadowmoor*. This one never saw the light of day during the beta, but I almost wish it had just for the humor factor.

![](https://i.ormos.uk/27/77/2777cc33cad5bed2df425f98c0d26d229cbe7935d05b4b1cf03e2cce9d58a858.png)

[Scarscale Ritual](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scarscale+Ritual) had a similar symbolic goof. Left to its own devices, the 2.5 client believed that a checkmark was perfectly understandable shorthand for the cost "Put a -1/-1 counter on a creature you control." Since that cost was new to **Magic Online**, it had to be added to the list of costs that don't get printed in the context menu.

![](https://i.ormos.uk/4c/89/4c89414120a4b52ec861a874359239c3f567648381b0efb22b0c8733d28fc059.png)

Big thanks are due to Lee Sharpe, Jason Radabaugh, Alexis Janson, and Corey Fellows who all contributed in a big way to *Shadowmoor* development. If you see them online (probably playing Commander Singleton Free-For-All), be sure to say "Hi." Special thanks also to our rules quality assurance team of Stephen Fivash, Kendrick Redira, and Keith Poth. We can't fix the bugs if they don't find them. They're a large part of making the release go smoothly. 

I'll leave you with a little riddle that was also one of our test cases during *Shadowmoor* development. The rules engine got it right on the first try, no pressure. How many tokens to you get if you start a solitaire game and play [Ornithopter](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter), [Doubling Season](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doubling+Season), [Flourishing Defenses](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flourishing+Defenses), and then [Grief Tyrant](https://web.archive.org/web/20080616000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grief+Tyrant)? Feel free to head to the forums and compare answers with other readers.