---
id: gsfew6j0
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/09-04-developing-for-multiplayer
title: Developing for Multiplayer
published: '2009-09-04'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    lang_detected: en
    capture_id: 720952
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    captured_at: '2022-08-11 02:54:37+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    lang_detected: en
    capture_id: 720952
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    captured_at: '2022-08-11 02:54:37+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    lang_detected: en
    capture_id: 720952
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    captured_at: '2022-08-11 02:54:37+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    lang_detected: en
    capture_id: 720952
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
    captured_at: '2022-08-11 02:54:37+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: gsfew6j0
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
  lang: en
  template: drupal
  captured_at: '2022-08-11 02:54:37+00'
  capture_id: 720952
  wayback_url: https://web.archive.org/web/20220811025437id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
- document_id: gsfew6j0
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/54
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/54
  lang: en
  template: aspx
  captured_at: '2013-07-07 02:28:53+00'
  capture_id: 623259
  wayback_url: https://web.archive.org/web/20130707022853id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/54
- document_id: gsfew6j0
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-03
  lang: en
  template: drupal
  captured_at: '2021-12-04 02:33:47+00'
  capture_id: 720951
  wayback_url: https://web.archive.org/web/20211204023347id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-03
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gsfew6j0
  capture_id: 720952
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
  wayback_url: https://web.archive.org/web/20220811025437id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-2009-09-04
  captured_at: '2022-08-11 02:54:37+00'
  template: drupal
  sha256: a49f4f8ceeda2e881ca0c46a8d8d946bd156cd41c81cb44110512b36c90fc72b
render_recovery: []
---
This is the end of *Planechase* Week. Although this is Latest Developments, I won't be talking about the development of *Planechase*. Dave Guskin did a great job covering [everything there was to say about that](https://web.archive.org/web/20090904000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/54) on Monday. Instead, today I'll be talking about some things we do in development to make our sets work better in multiplayer games in general, and I'll also talk about why we sometimes don't make such changes even when we identify that we could.

### Infectious Horror

![Infectious Horror](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Infectious+Horror)

 

[Infectious Horror](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Horror) does not have much of a story. It was designed to do exactly what it does, and there aren't even any Multiverse comments about it. A large part of **Magic** development is identifying what is working and protecting those things, and [Infectious Horror](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Horror) always worked exactly like it was supposed to, so we protected it.

### Breath of Malfegor

![Breath of Malfegor](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Breath+of+Malfegor)

 

This card's story is similar to that of [Infectious Horror](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Horror), but the outcome was a little less happy. Aaron Forsythe was the lead designer of *Alara Reborn*, and he designed [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) to be a card that would be fun in multiplayer for people who enjoyed painting enormous targets on their heads. Cards like this, [Syphon Mind](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syphon+Mind), and [Syphon Soul](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syphon+Soul) scale well in multiplayer, but also draw everyone's ire. Many players do not care about this, and they will happily hurt everyone else and cackle as the rest of the table grumbles.

More than one playtester commented during *Alara Reborn* development that the card was really strong in Two-Headed Giant. With starting life totals for that format now at 30 rather than 40, [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) takes a full third out of a team's life total. We noted this and moved on. However, after the *Alara Reborn* Prerelease we got lots of feedback from people who played Two-Headed Giant there that [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) had seriously warped the format. We got to experience this for ourselves at [Grand Prix–Seattle/Tacoma](https://web.archive.org/web/20090904000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/sf/42)'s "[Two-Headed Giant with Wizards employees](https://web.archive.org/web/20090904000000/https://magic.wizards.com/en/events/coverage/massicard-masters-mulligan-madness)" event, where [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) was a huge factor even with only two *Alara Reborn* packs in the mix. Ken Nagle and I chatted about [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) while I was preparing to write this article, and we both agreed that the world might be a slightly happier place if the card had been swapped up to uncommon.

### Feral Hydra

![Feral Hydra](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Feral+Hydra)

 

[Feral Hydra](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Hydra) is a more subtle multiplayer card than the previous two. [Infectious Horror](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infectious+Horror) and [Breath of Malfegor](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breath+of+Malfegor) are both blunt instruments that hurt everyone else in the game. [Feral Hydra](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Hydra) is different. Its counter-adding clause was changed to let both you and your teammates grow it, which is great for Two-Headed Giant, Emperor, and other team multiplayer variants.

However, it also does something else. Our resident multiplayer aficionado Ken Nagle is well-known within the Pit for loving to play politics in multiplayer games, and [Feral Hydra](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Hydra) enables lots of this even when Ken has no teammates. If you found yourself in a multiplayer game with a Ken-controlled [Feral Hydra](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Hydra), you would likely experience intense negotiation over just who that Hydra attacked. I wouldn't be surprised if you ended up paying to grow it every once in a while to get Ken to leave you alone. It's not often that we have opportunities to enable this kind of play in natural ways, but we take them when we can so that people like Ken can make "friends" even when they have no teammates.

### Merfolk Sovereign

![Merfolk Sovereign](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Merfolk+Sovereign)

 

Sometimes we make minor changes to cards that don't change their mechanics very much, but make the card work a little better in multiplayer. Merfolk Soverign received this treatment. Originally, it could only tap to make your own Merfolk unblockable. **Magic** editor Del Laugel noted during templating that we could simply remove the words "you control" from it, which would allow a player to help out a teammate's Merfolk or play politics in a free-for-all. In this case, we were happy to make the change. Because all we had to do was remove words on a targeting restriction, the change was essentially costless. If you play multiplayer, you have the chance to use [Merfolk Sovereign](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Sovereign) in more ways, but if you don't the change does not affect you at all.

### Graft

We also sometimes change cards to be more multiplayer-friendly even if there are costs that we must pay to do it. The first version of graft, *Dissension*'s blue-green mechanic, allowed you to move +1/+1 counters only to your own creatures. I was not here during *Dissension* development, but I can only assume that the conversation about how graft would work were very similar to the conversation we had about [Merfolk Sovereign](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Sovereign). We saw an opportunity to make the cards with the graft mechanic work better in multiplayer (and also enable the unusual design of [Cytoplast Manipulator](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cytoplast+Manipulator)), and after some discussion the costs to the change were deemed to be worth it.

![Cytoplast Manipulator](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cytoplast+Manipulator)

 

Some of you may be wondering to yourself what the downside of this change to graft is. If you play **Magic Online**, however, you may have already guessed. On **Magic Online**, every triggered ability requires a click to get past. In the case of graft, each graft trigger requires two clicks: the first to pass priority while it is on the stack, and the second to choose whether or not to move a +1/+1 counter. Taking "you control" off of the graft trigger means that every time an opponent's creature enters the battlefield, a **Magic Online** player who controls a creature with graft must pass priority while the graft trigger is on the stack, then tell **Magic Online** not to give that creature a +1/+1 counter.

This may not sound bad, but *Ravnica* block has plenty of cards that put multiple tokens into play. A [Bramble Elemental](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramble+Elemental) receiving a [Pollenbright Wings](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pollenbright+Wings) will force a graft player to click four times for each graft creature they control, and eight more times per graft creature each time the [Bramble Elemental](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramble+Elemental) connects for damage. This is a lot of clicking. In the case of graft the change played so well on paper that it was worth it, but we do think about how card changes affect **Magic Online**.

### Fertilid

![Fertilid](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fertilid)

 

In my opinion, [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) is an example of when making a card multiplayer-friendly may not have been worth it. Many cards in *Morningtide* changed to be friendlier to Two-Headed Giant play. As part of this push, [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) gained the "target player" text that allowed a player to use [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) to help out his teammate. [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) was already a mildly complicated card before this change, and adding "target player" to the activated ability is an extra thing to parse when one is trying to decipher the card for the first time. Every "target player" clause requires one to decide whether or not the effect is supposed to be directed at oneself or another, and this processing must happen every time one encounters the card until it is internalized.

The other reason might not have changed [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) to target is that the great majority of [Rampant Growth](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth) effects are not targeted. On a creature like Emberwilde Auger that deals damage to a player, there is no way to write the card without the word "target," and every spell that damages players also uses target. Because the text on Emberwilde matches what I am used to on [Lava Axe](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) and [Lava Spike](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Spike), it doesn't cost me any processing time. However, [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid)'s text may trip me up if I am used to playing with [Rampant Growth](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth) and [Sakura-Tribe Elder](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder), neither of which target a player.

I have used [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid)'s ability to target a teammate in Two-Headed Giant several times. However, I don't think that the extra fun that I and others have had doing that outweighs the confusion that I have seen when people have tried to decipher what [Fertilid](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertilid) does and how to use it correctly the first time they see it.

### Divination

![Divination](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Divination)

 

[Divination](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination)'s story is very interesting for a card that has three words of rules text. It looks like a very simple card that would be uncontroversial, but inside the Pit we had vigorous discussions about it. A few people, including Mark Rosewater, felt very strongly that [Divination](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) should read "Target player draws two cards" to allow wins via decking or targeting a teammate. Aaron Forsythe, on the other hand, wanted to do the simplest possible implementation of basic cards in ***Magic** 2010*, so he fought against the "target" wording. Most people who read this web site are experienced **Magic** players, but targeting is not a simple concept to many beginning **Magic** players. [Divination](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) could work without having to invoke the word target, and Aaron chose to do that.

I'm very glad in hindsight that we stayed with "Draw two cards" on [Divination](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination). However, my reason for being glad has changed over time. ***Magic** 2010*'s focus on top-down design produced a very resonant set, and because of that I have been paying much more attention to top-down flavor on cards. In the case of [Divination](https://web.archive.org/web/20090904000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination), it makes no sense to me that a divination spell would allow someone other than its caster to gain knowledge. He might choose to share the knowledge that he gained from the spell with another wizard, but the knowledge goes to him first. "Target player draws two cards" moves the card away from this concept, and that hurts the flavor too much for me to think that adding a little bit of multiplayer potential is worth it.

![](https://i.ormos.uk/56/73/567327bf0d9ef3b327947deaede8ba2b54a2d2153255428e98eff03e4b697adf.jpg)

### Coming Attractions

This is an exciting time for me as a Magic developer. Tons of things I spent lots of time working on are releasing all at once. I talked [last week](/en/articles/latestdevelopments/2009/08-28-masters-of-the-multiverse) about the **Magic Online**–only release of *Masters Edition III*; online Prerelease events for that set begin the day after this article goes up, and the set goes on sale next Monday, September 7. This coming Monday also marks the beginning of *Zendikar* previews. Although I wasn't on the design or development team for *Zendikar*, my handprints are all over the set. I helped design the final versions of two of the set's major mechanics, and my preview card next Friday is one of the cards I made during that design process. Amazingly, that card made it all the way through development unchanged from the very first version I put into Multiverse. My expectation is that it will be popular and sought-after, and I'm excited that I get to show it to you!

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>How many other players were part of the last game of Magic you played?</b></th>&#10;		</tr></thead><tbody><tr><td>0</td>&#10;			<td>341</td>&#10;			<td>4.5%</td>&#10;		</tr><tr><td>1</td>&#10;			<td>3311</td>&#10;			<td>44.0%</td>&#10;		</tr><tr><td>2</td>&#10;			<td>1279</td>&#10;			<td>17.0%</td>&#10;		</tr><tr><td>3</td>&#10;			<td>1063</td>&#10;			<td>14.1%</td>&#10;		</tr><tr><td>4</td>&#10;			<td>547</td>&#10;			<td>7.3%</td>&#10;		</tr><tr><td>5</td>&#10;			<td>354</td>&#10;			<td>4.7%</td>&#10;		</tr><tr><td>6+</td>&#10;			<td>628</td>&#10;			<td>8.3%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7523</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

I ran this poll on a whim to lead into my article this week. I did not expect anywhere near a twelfth of you to respond that your last game of **Magic** had six or more other players in it. That is so many players! We are very good at developing **Magic** so that two-player games are fun, and this article shows you how we adjust cards to make multiplayer games of all sizes work better. However, we don't often think about multiplayer games on that scale. If you often play games of multiplayer **Magic** that have six or more other players in them, I encourage you to click the "Respond via email" link below and tell me what sorts of cards make your huge multiplayer games better, and what sorts of cards make them worse. Thanks!

[![](https://i.ormos.uk/39/a4/39a4c7e62d3dd48bbc707fe9eb6cd2b191ea72fe6775cbbdf4926914ef17a4e3.jpg)](https://web.archive.org/web/20090904000000/http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/planechase-facts)