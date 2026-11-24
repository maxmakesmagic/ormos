---
id: tzz1zvh1
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/01-09-to-kill-a-planeswalker
title: To Kill a Planeswalker
published: '2009-01-09'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    lang_detected: en
    capture_id: 723383
    url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    captured_at: '2022-09-29 20:57:51+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    lang_detected: en
    capture_id: 723383
    url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    captured_at: '2022-09-29 20:57:51+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    lang_detected: en
    capture_id: 723383
    url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    captured_at: '2022-09-29 20:57:51+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    lang_detected: en
    capture_id: 723383
    url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
    captured_at: '2022-09-29 20:57:51+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: tzz1zvh1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
  lang: en
  template: drupal
  captured_at: '2022-09-29 20:57:51+00'
  capture_id: 723383
  wayback_url: https://web.archive.org/web/20220929205751id_/https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
- document_id: tzz1zvh1
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/20
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/20
  lang: en
  template: aspx
  captured_at: '2013-07-07 19:46:36+00'
  capture_id: 618538
  wayback_url: https://web.archive.org/web/20130707194636id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/20
- document_id: tzz1zvh1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-08
  page_key: magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-08
  lang: en
  template: drupal
  captured_at: '2022-01-28 09:44:53+00'
  capture_id: 723378
  wayback_url: https://web.archive.org/web/20220128094453id_/https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-08
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: tzz1zvh1
  capture_id: 723383
  url: https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
  wayback_url: https://web.archive.org/web/20220929205751id_/https://magic.wizards.com/en/articles/archive/latest-developments/kill-planeswalker-2009-01-09
  captured_at: '2022-09-29 20:57:51+00'
  template: drupal
  sha256: 3a1af7d75a89df9bbb4dd4e33a23fbfe337815117b2cb36cec06908e29a5e5a7
render_recovery: []
---
*As you may recall, Latest Developments was in flux for the latter part of last year, with a rotating crew of authors from the development team. I'd like to take this opportunity to thank Ken Nagle, Bill Stark, Mike Turian, Matt Place, Erik Lauer, and Tom LaPille for sharing their different views and stories about **Magic** development. Now, it's my pleasure to announce that Tom has stepped up to write the column on a weekly basis. Please join me in welcoming him as a weekly author!*  
 –Kelly Digges, **magicthegathering.com** editor

Previous Latest Developments columnists have often shown you examples of how we develop individual cards. For example, my predecessor Devin Low wrote [an entire column](/en/articles/latestdevelopments/2008/12-26-multiverse-macabre) about the journey of just one card from design to print. However, we develop in broader strokes too. We often think about entire mechanics, sets, and blocks. We also think about what's best for the game as a whole. For example, we recently spent time thinking about whether printing a card with the line "Destroy target planeswalker" on a card would make **Magic** more or less fun.

Allow me to elaborate. Many games of **Magic** are essentially fights between armies of creatures and spells that support them. However, variety is hugely important to how fun a game is over the long term, and one of the reasons **Magic** is awesome is that it can produce strange situations that challenge players of any experience level. In fact, we deliberately make cards that produce those situations to keep players interested. For example, we might make [Cloudstone Curio](https://web.archive.org/web/20090109000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Cloudstone%2BCurio), or [Swans of Bryn Argoll](https://web.archive.org/web/20090109000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Swans%2Bof%2BBryn%2BArgoll).

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Cloudstone Curio" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Cloudstone+Curio"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Swans of Bryn Argoll" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Swans+of+Bryn+Argoll"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

 

Sometimes these cards don't end up being too powerful, and they lead to fun and interesting games. Other times, they are really powerful and they beat you over and over again until you decide it's not worth playing against them anymore. The natural reaction to that is to start looking for ways to defeat the offending deck. If you find cards that you think will solve your problem, you'll adjust your own deck and then be ready to play again. On the other hand, if you don't find an answer, you might get frustrated and give up completely. Why keep playing when you know exactly what will happen to you and you can't stop it?

 

Here in **Magic** R&D, we try to make sure that there are adequate answers to anything powerful you might encounter so that you don't get stuck without a way to deal with a power card or combination. On a very basic level, we make lots of cards that target card types. Are you losing to your friend's enchantment deck? There are 18 cards in Standard that can destroy enchantments, including more than one that takes care of every enchantment in play. Artifacts got you down? There are a total of 18 cards in Standard that destroy artifacts. We also make cards that interact with specific zones. A new player might experience some bewilderment when they encounter their first opponent who is abusing the graveyard with reanimation spells or dredge cards, but a little searching will turn up [Relic of Progenitus](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Relic+of+Progenitus), [Beckon Apparition](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beckon+Apparition), [Faerie Macabre](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre), [Heap Doll](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll), and various other cards they can use to interact with their opponents' graveyards. Finally, we print cards that attack more abstract strategies. Is your opponent trying to kill you by playing a lot spells in one turn? [Rule of Law](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rule+of+Law) will stop them in their tracks.

We really like to print answer cards like [Naturalize](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize), [Relic of Progenitus](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Relic+of+Progenitus), and [Rule of Law](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rule+of+Law). They aren't subtle, but when you really need an answer to something and you're desperate, it's much better if we can give you an obvious answer so the search isn't difficult and you find what you need. Sometimes, however, we do print more subtle answers. [Stifle](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle) was placed in *Scourge* as an answer to storm. Unfortunately, making the connection that [Stifle](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle) is good against storm cards requires some sophisticated rules knowledge. Specifically, one needs to know that storm creates a triggered ability, or be able to figure that out from the storm reminder text. Happily, players identified [Stifle](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle) as a storm answer and adopted it en masse, and the card is now a staple in both Extended and Legacy.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Stifle" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Stifle"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Riftsweeper" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Riftsweeper"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

 

The worst-case situation from our perspective is that we provide an answer that is too subtle for players to identify. When that happens, we might as well not have printed any answer. [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) is a great example of this. The suspend mechanic has the potential to create unfun situations where one player has no choice but to stare at impending doom as a suspended card ticks down to zero. [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) was intended to be a powerful way for green decks to interact with those suspended cards. Two-mana 2/2 creatures like [Kami of Ancient Law](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kami+of+Ancient+Law) and [Samurai of the Pale Curtain](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samurai+of+the+Pale+Curtain) have often been popular answer cards, so we assumed that players would play [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) as well. However, parsing the phrase "face-up card that's removed from the game" to mean "suspended card" requires some sophistication, and even if you know that a suspended card is both face up and removed from the game you might search for cards that have "suspended" in rules text, fail to find any cards you thought were powerful enough to help, and conclude that we had given you nothing. Both [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) and [Pull from Eternity](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+from+Eternity) would have been much easier to identify if they had both targeted "suspended cards." We were happy to see [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) play an important role in Uri Peleg's victory over Patrick Chapin in the Finals of the 2007 World Championships, but [Riftsweeper](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) never became popular in the **Magic** community at large, and we consider that to be a development failure.

 

![Ajani Vengeant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ajani+Vengeant)

Speaking of card types, impending doom, and subtle answer cards, let's talk about planeswalkers. Planeswalker is a permanent type, and cards that mention that type outside of reminder text are conspicuously absent from **Magic**. A planeswalker can inspire feelings of hopelessness as it ticks up in loyalty toward its "ultimate," which is always jaw-dropping no matter which planeswalker you're talking about. Perhaps your opponent will have five 4/4 Dragons next turn, or everything he or she controls will become indestructible until the end of the game. Either way, it's not looking good. Planeswalkers have very clearly shown themselves to be powerful in tournament **Magic**, and we know that they are even more powerful than that in casual **Magic**. Casual games are more likely to include slow building up to powerful effects and very little early attacking than tournament games, and that is exactly the kind of situation in which a planeswalker is most powerful. The incremental advantages it provides add up turn after turn, and an activation of the ultimate may very well end the game on the spot.

The game of **Magic** already contains many ways to deal with planeswalkers. First, they can be attacked with creatures. Second, any damage dealt to a player by a spell can be redirected to any planeswalker that player controls. Finally, many cards can specifically interact with them. They are permanents, so cards like [Vindicate](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vindicate) and [Oblivion Ring](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) can remove them. Their abilities are activated abilities, so [Pithing Needle](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle) and [Voidstone Gargoyle](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voidstone+Gargoyle) can prevent them from functioning. A planeswalker's loyalty is tracked with counters, so [Æther Snap](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86ther+Snap) reduces the loyalty of all planeswalkers in play to 0, which causes them to promptly be put into the graveyard.

It's great that these exist, but they all require some amount of rules knowledge or sophistication to identify. Attacking a planeswalker is reasonably intuitive, as is sending an Incinerate at one. However, you would have to know very well how a planeswalker worked before identifying their abilities as activated abilities. It wouldn't be so bad if we could write "Remove a loyalty counter from [Garruk Wildspeaker](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker): put a 3/3 beast token into play," but there's too much information we have to convey on the card to have room for that. Finally, someone who happened to use pen and paper rather than dice to track the loyalty of planeswalkers might not keep it in the front of his mind that planeswalker loyalty is tracked with counters.

At first, we wondered if we were supposed to print bizarrely pigeonholed cards that happened to be very good against planeswalkers. For example, we could print something like this:

 

> Go Home, Meddlesome Mage  
>  1R  
>  Instant  
>  Go Home, Meddlesome Mage deals damage to target player equal to the number of counters on target permanent that player controls.

Imagine that your opponent just played [Elspeth, Knight-Errant](https://web.archive.org/web/20090109000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elspeth%2C+Knight-Errant) and made a soldier token. During his end step, you play Go Home, Meddlesome Mage targeting him and Elspeth. When the spell resolves, it sees that Elspeth has 5 loyalty counters on her, identifies that the spell is about to deal 5 damage, then asks you if you want to deal the damage to your opponent or a planeswalker he controls. You choose to deal the damage to Elspeth, and she is reduced to 0 loyalty and put into the graveyard. Of course, no matter how much loyalty a planeswalker has, this hypothetical card will kill it. This is about as engineered as a planeswalker-killing card can get, and yet it still requires a multiple-step chain of logic to identify how it works. We can spend all day engineering cards like this to dodge around actually using the word "planeswalker" in the text box, but at the end of the day the cards that we were engineering would have just been better written as "destroy target planeswalker."

![Elspeth, Knight-Errant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elspeth%2C+Knight-Errant)

The game-play benefits to printing "destroy target planeswalker" are obvious. It isn't any fun when you encounter something really powerful that you don't know what to do with, and printing a card that just up and kills planeswalkers is a great way to give people an answer to them. Why, then, do we not just print that?

We haven't printed that card yet because of the problems it causes with the flavor behind the planeswalkers. Perhaps the largest problem is that a planeswalker going to the graveyard doesn't actually represent that planeswalker dying. Your life total represents your health, but a planeswalker's loyalty total represents how friendly he or she feels toward you. A planeswalker card goes to the graveyard when it has no loyalty counters—that is, when he or she gets fed up with your inability to provide protection and decides not to help you anymore. However, the only words **Magic** uses to describe an object being put into a graveyard from play are "destroy" and "sacrifice," and neither is quite appropriate for the flavor here. Ignoring this would cause some strange situations because each player in a game of **Magic** represents a planeswalker. A player who encountered the hypothetical "destroy target planeswalker" card after learning that that he and his opponent represent planeswalkers but before encountering a planeswalker card might very well think that this card would immediately win the game by destroying his opponent—a very powerful card indeed!

Another problem is that in the **Magic** multiverse, planeswalkers are incredibly rare and therefore most denizens of any given plane will never encounter one in their lifetime. Since the cards in each set represent spells that are available on a particular plane, it doesn't make much sense that someone on a plane would develop a spell that targets a planeswalker, much less a spell that specifically makes a planeswalker just unhappy enough to stop helping out a different planeswalker who called in a favor.

It's easy to flippantly say that game-play considerations should always trump flavor, but that view is naïve. The rich fantasy flavor that the **Magic** creative team provides is massively important to the appeal of the game, and our planeswalkers are the stars of the show. In the end, we need to take into account both the desire for them to play as well as they possibly can and the desire for the flavor to make perfect sense when we are making decisions.

It is not surprising that the various denizens of the Magic R&D "Pit" turned one developer's joke about printing "destroy target planeswalker" into a large and very serious discussion. I can't share the results of that discussion, but happily that is because it isn't over. In fact, we'd love to hear what you think!

Just like previous authors of Latest Developments, I'll include a poll at the end of each article, and I'll often use it to try to figure out what the community as a whole thinks about certain things. I can't promise that we'll do everything you collectively vote for, but I look forward to getting your feedback.