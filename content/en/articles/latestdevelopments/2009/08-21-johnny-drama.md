---
id: v0sy7xbp
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/08-21-johnny-drama
title: Johnny Drama
published: '2009-08-21'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    lang_detected: en
    capture_id: 723306
    url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    captured_at: '2022-05-23 15:30:14+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    lang_detected: en
    capture_id: 723306
    url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    captured_at: '2022-05-23 15:30:14+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    lang_detected: en
    capture_id: 723306
    url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    captured_at: '2022-05-23 15:30:14+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    lang_detected: en
    capture_id: 723306
    url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
    captured_at: '2022-05-23 15:30:14+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: v0sy7xbp
  url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
  lang: en
  template: drupal
  captured_at: '2022-05-23 15:30:14+00'
  capture_id: 723306
  wayback_url: https://web.archive.org/web/20220523153014id_/https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
- document_id: v0sy7xbp
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/52
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/52
  lang: en
  template: aspx
  captured_at: '2013-07-06 15:08:09+00'
  capture_id: 623236
  wayback_url: https://web.archive.org/web/20130706150809id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/52
- document_id: v0sy7xbp
  url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-20
  page_key: magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-20
  lang: en
  template: drupal
  captured_at: '2021-12-02 13:57:49+00'
  capture_id: 723297
  wayback_url: https://web.archive.org/web/20211202135749id_/https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-20
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: v0sy7xbp
  capture_id: 723306
  url: https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
  wayback_url: https://web.archive.org/web/20220523153014id_/https://magic.wizards.com/en/articles/archive/latest-developments/johnny-drama-2009-08-21
  captured_at: '2022-05-23 15:30:14+00'
  template: drupal
  sha256: 255ddbef737f3f2e602724a72b7dfdd7539e0fb606c76206354b1cdb602c3e87
render_recovery: []
---
This is Exiled Week on Daily MTG. However, I covered Exiled Week [two weeks ago](/en/articles/latestdevelopments/2009/08-07-meet-the-exiled) when I introduced From The Vault: Exiled. That week was Johnny Week, so this week I'll be covering Johnny just like I promised.

I can't do a better job of introducing Johnny than Mark Rosewater did, so I'll quote his seminal "[Timmy, Johnny, and Spike Revisited](/en/articles/makingmagic/2006/03-20-timmy-johnny-and-spike-revisited-4)."

> So why does Johnny play **Magic**? Because Johnny wants to express something. To Johnny, **Magic** is an opportunity to show the world something about himself, be it how creative he is or how clever he is or how offbeat he is. As such, Johnny is very focused on the customizability of the game. Deck building isn't an aspect of the game to Johnny; it's *the* aspect.
> 
> One of the strengths of **Magic** is the ability for players to imbue much of themselves in their decks. When you play Monopoly you don't get emotionally attached to the board. But with **Magic**, your deck becomes an extension of yourself. When your deck wins, you win. When your deck gets complimented, you get complimented. It is this principle that drives Johnnies.

Two weeks ago, Rosewater talked about [designing for Johnny](https://web.archive.org/web/20090821000000/http://archive.wizards.com/magic/Magazine/Article.aspx?x=mtg/daily/mm/29). However, development has a number of tools that it uses to make Johnny happier as well, and I'll share some of them in this column. Each of the three psychographics thrives on different kinds of fun, but it's important to remember that the fundamental fun that all three psychographics have identified can still be fun for anyone, no matter what kind of fun they prefer to have.

### Adjusting Mana Costs

Johnny thrives on combining **Magic** cards and unique and unexpected ways. **Magic**'s core mana mechanic is a huge part of why the game system is balanced and creates fun individual games, but it also can limit players' ability to combine their cards in creative ways. Players often demonstrate their willingness to work around awkward mana requirements by playing decks built around combinations like [Seismic Assault](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seismic+Assault) and [Swans of Bryn Argoll](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swans+of+Bryn+Argoll). Getting both ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) and ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif), or ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) consistently in the same deck takes some doing, but it's clearly worth it to some. Unfortunately, daunting mana requirements like that can dissuade players from trying to build decks around interesting combinations that they find. That gets in the way of a Johnny's potential fun, so we avoid doing it when we can.

 

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Seismic Assault" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Seismic+Assault"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Swans of Bryn Argoll" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Swans+of+Bryn+Argoll"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

There is another tool that we have that relates to mana costs, although we use this other tool as sparingly as possible. Often, designers will create a card that is directed toward Johnny. However, sometimes that card is so potent an engine or so huge a reward that it causes bad things to happen in our Constructed playtesting. When this happens, rather than kill the card entirely, we prefer to just make it expensive enough that it will appeal only to Johnnies. We have found that although this takes some cards away from Spike, it makes Johnny happier for multiple reasons. First, he still gets to play with the crazy text boxes that he wants to play with. Second, he appears more creative compared to the other psychographics because he is the only one playing with those cards. This is a solution that we don't love using, but we do it when we must.

### Getting Weird

![Mirror of Fate](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mirror+of+Fate)

Another tool in the **Magic** development toolbox that we use to satisfy Johnnies is to make cards weirder. If we notice that a set doesn't have enough Johnny appeal, we are not afraid to take a perfectly normal card and twist it into something that looks unusable and narrow but will give a few players great joy to play with.

This happened in a memorable way for one particular card in ***Magic** 2010*. We were unhappy with the text box for [Mirror of Fate](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror+of+Fate) very late into development, and it never really settled down for longer than a week or so. In one of our last meetings, lead developer Erik Lauer brought a full-color printout of the card's art and decreed that we were going to make a seriously wacky card. I believed that we were going to make a wacky card, but what I didn't believe was just how wacky he wanted to get. Our first attempts were strange, but they were not wacky enough for Erik. Seeing our frustration, he decreed with a sly smile that part of the card's effect would be exiling your entire library. It didn't take us long from there to get to the [Doomsday](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doomsday)-esque text we have. We left the meeting scratching our heads at the bizarre card we had made, but we were confident that some enterprising players would figure out what to do with it. Lo and behold, just yesterday on this site über-Johnny Noel deCordova shared with us [a way to use it](https://web.archive.org/web/20090821000000/http://archive.wizards.com/magic/Magazine/Article.aspx?x=mtg/daily/ftl/52) to entertaining effect.

### Single Cards

Clever tapestries of interactions in sets is great for Johnny. On the other hand, one good build-around card can keep a Johnny occupied for a very long time. When developers find a card that fits this description, we fight to protect it. When we see an opportunity to make a card a better build-around for Johnny, we take it.

![Didgeridoo](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Didgeridoo)

I did not internalize this particular lesson until very recently. *Masters Edition 3* is the first **Magic** set that I was the lead developer for, and I'll be spending an entire article talking about it next week. However, today I will spoil a card early, and that card is [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo). Lead designer Erik Lauer built a small number of tribal themes into *Masters Edition 3*, one of which is Minotaurs. Naturally, he included [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo) as a support card for that tribe. In one of my early development passes I discovered that the set contained no Minotaurs that cost more than four mana to "cheat" into play with [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo). Intending to rectify this, I searched for Minotaurs in early **Magic** that cost more than four and was bewildered to find that there were none. Furious, I nearly cut [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo) from the set. However, resident Timmy-Johnny Ken Nagle intervened. Before Ken came to Wizards, he played enough **Magic** that he was able to explore nearly every card in most sets. He told me that [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo)'s existence would have prompted him to make a casual Minotaur deck, and cutting it would have cost him five to ten hours of fun. In the last Limited playtest we did, [Serious Fun](https://web.archive.org/web/20090821000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?page=0&tag=seriousfun&description=Serious%20Fun) author Kelly Digges opened a [Didgeridoo](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Didgeridoo), first-picked it, and drafted exactly the Minotaur deck that Ken told me he would have built. I'm glad that Ken convinced me to keep it.

### Alternate Limited Strategies

Johnnies get to shine most brightly in Constructed formats, where there are few restrictions on the cards they play with. However, as developers it's important to us that Limited be fun for everyone as well. We make Limited more fun for Johnny by seeding formats with alternative strategies that can be discovered. Most games of Limited are decided by creatures attacking and blocking, but most does not need to mean all, and even games that are decided by attacking and blocking can be won in strange ways that Johnny enjoys.

 

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Dampen Thought" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Dampen+Thought"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Tome Scour" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Tome+Scour"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

One classic alternative strategy that we often build into Limited environments is decking. Decking as a strategy was mainstream by design in straight *Ravnica: City of Guilds* Limited, but when everyone is able to see and build a strategy it loses some of its appeal to Johnnies because it ceases to be something that is unique to them. Better for Johnny is a card like [Dampen Thought](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dampen+Thought) in *Champions of Kamigawa*. It is an uncommon, so it didn't show up as often as [Vedalken Entrancer](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vedalken+Entrancer) or [Lurking Informant](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lurking+Informant) did in *Ravnica*, and the splice-based decks it produced looked nothing like normal Limited decks, often playing seven or fewer creatures in their 40 cards. This is the sort of thing that makes Johnny happiest. ***Magic** 2010*'s [Tome Scour](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tome+Scour) was an attempt to seed a potential milling deck into the limited format; one copy of [Tome Scour](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tome+Scour) can't make an entire milling deck work in the same way that one [Dampen Thought](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dampen+Thought) can, but I have still seen many people draft [Tome Scour](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tome+Scour) decks in ***Magic** 2010* Limited. Sometimes those people have even been lucky enough to have picked up a [Traumatize](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traumatize) or two, and others have been clever enough to add red to their decks for [Burning Inquiry](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Inquiry) backup!

### A Little Johnny in All of Us

Those are four tools that we use to improve Johnny's experience. However, the Johnny impulse drives players to things that can be fun for any **Magic** player, and we have ways of bringing that fun to other players too. Here are two of them.

### Engineered Combinations

One way that we can bring Johnny fun to any **Magic** player is by engineering two or more individually appealing cards so that they combine in fun ways. One of the earliest such combinations was [Royal Assassin](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Royal+Assassin) with [Icy Manipulator](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Icy+Manipulator). Back in the early days of **Magic**, players loved both of these cards and were more than willing to play either of them on their own. However, in combination they turned into a creature-slaughtering machine. Many Spikes and Timmies found themselves experiencing snatches of Johnny fun as they used the two cards together. The inclusion of both [Blinding Mage](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Mage) and [Royal Assassin](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Royal+Assassin) in ***Magic** 2010* is no accident, and it is a nod to that classic combination.

 

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Junktroller" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Junktroller"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Tunnel Vision" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Tunnel+Vision"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

A more recent example that resonates for me comes from triple *Ravnica* Limited. I enjoyed the change of pace that the blue-black milling deck offered, and I drafted it a lot. I learned while I drafted that format that [Junktroller](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Junktroller), although it read poorly, was a very good card for those decks. It blocked extremely well, and thanks to the Dimir guild's transmute mechanic it was possible to search up cards that you had put on the bottom of your deck and play them again. Another card that I grew to love was [Tunnel Vision](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tunnel+Vision). It appeared to me to be a bizarre rare at first, but it became quite potent when I learned to remember what cards were in the draft and likely to be in my opponent's deck. It usually milled my opponent for a bunch of cards, especially after the first game when I had seen most of their deck. However, in combination with [Junktroller](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Junktroller), [Tunnel Vision](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tunnel+Vision) was a six-mana way to win the game. I'm not a Johnny by nature, but I had a ton of fun every time I pulled off this combination!

### Limited Depth

One of the best tools we have that brings Johnny fun to the most hardcore of Spikes is building very deep Limited environments. When there are lots of potential strategies to be drafted in a set, it's very possible for any enterprising player to find an underdrafted one, get a powerful and unexpected deck, then feel smart as his friends marvel at what he found. We have done this for a long time in expansion sets, but ***Magic** 2010* lead developer Erik Lauer made full use of his freedom to make new cards to build hidden strategies into his draft format.

![Trumpet Blast](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trumpet+Blast)

White has the best cheap creatures in ***Magic** 2010*, and aggressive white-red decks can get tons of value out of [Trumpet Blast](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast) when they have many creatures in play. However, [Trumpet Blast](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast) is nowhere near as powerful in red decks that use other colors because it's hard to get as many cheap creatures. Slower controlling blue-red decks, for example, often have around ten to twelve creatures and have no use for a [Trumpet Blast](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast). However, there is also an aggressive blue-red deck in ***Magic** 2010* that is happy to use unimpressive cheap flyers like [Zephyr Sprite](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zephyr+Sprite) and [Sage Owl](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+Owl) along with [Trumpet Blast](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast)s and [Lava Axe](https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe)s to do tons of damage very quickly. I enjoyed watching players discover this deck firsthand during unsanctioned side drafts at U.S. Nationals a few weeks ago. The people I was playing with were among the most diehard Spikes in the world, but they were still having plenty of good Johnny fun while they made unexpected discoveries.

Speaking of Johnny cards, let's look at last week's poll.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>Which of the following <i>Magic 2010</i> cards do you like the most?</b></th>&#10;		</tr></thead><tbody><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Open+the+Vaults">Open the Vaults</a></td>&#10;			<td>1914</td>&#10;			<td>24.0%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polymorph">Polymorph</a></td>&#10;			<td>1232</td>&#10;			<td>15.5%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warp+World">Warp World</a></td>&#10;			<td>1163</td>&#10;			<td>14.6%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Inquiry">Burning Inquiry</a></td>&#10;			<td>978</td>&#10;			<td>12.3%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren">Alluring Siren</a></td>&#10;			<td>933</td>&#10;			<td>11.7%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hive+Mind">Hive Mind</a></td>&#10;			<td>891</td>&#10;			<td>11.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Megrim">Megrim</a></td>&#10;			<td>575</td>&#10;			<td>7.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20090821000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror+of+Fate">Mirror of Fate</a></td>&#10;			<td>288</td>&#10;			<td>3.6%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7974</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

I didn't have anything specific that I wanted to get out of this poll; it's merely a pile of the Johnniest cards in ***Magic** 2010* that I saw in one pass. I saw some complaints in my forums from people who didn't like any of these cards. I'm okay with that; it probably just means that you aren't a Johnny. Part of the exercise for me was seeing which of these cards was most appealing to everyone, so thank you for your feedback.