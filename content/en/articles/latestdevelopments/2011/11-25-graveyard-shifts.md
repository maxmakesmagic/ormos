---
id: k4brrnyy
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/11-25-graveyard-shifts
title: Graveyard Shifts
published: '2011-11-25'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    lang_detected: en
    capture_id: 722947
    url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    captured_at: '2022-10-05 13:31:19+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    lang_detected: en
    capture_id: 722947
    url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    captured_at: '2022-10-05 13:31:19+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    lang_detected: en
    capture_id: 722947
    url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    captured_at: '2022-10-05 13:31:19+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    lang_detected: en
    capture_id: 722947
    url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
    captured_at: '2022-10-05 13:31:19+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: k4brrnyy
  url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
  lang: en
  template: drupal
  captured_at: '2022-10-05 13:31:19+00'
  capture_id: 722947
  wayback_url: https://web.archive.org/web/20221005133119id_/https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
- document_id: k4brrnyy
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/170
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/170
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:44:44+00'
  capture_id: 614402
  wayback_url: https://web.archive.org/web/20130706054444id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/170
- document_id: k4brrnyy
  url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-21
  lang: en
  template: drupal
  captured_at: '2021-10-25 23:50:35+00'
  capture_id: 722946
  wayback_url: https://web.archive.org/web/20211025235035id_/https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-21
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: k4brrnyy
  capture_id: 722947
  url: https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
  wayback_url: https://web.archive.org/web/20221005133119id_/https://magic.wizards.com/en/articles/archive/latest-developments/graveyard-shifts-2011-11-25
  captured_at: '2022-10-05 13:31:19+00'
  template: drupal
  sha256: e02b0630b9f50edd501c037c54539946d86474580249b553d70229c7ec7143f5
render_recovery: []
---
*We're out of the office celebrating Thanksgiving here in the States, so we're not able to bring you new articles today. Rather than just leave you with crackling static (which we're pretty sure is what happens if we stop putting articles up), we welcome you to enjoy last week's column. It's worth a re-read, especially if you missed the big announcement about the future of Latest Developments at the end of the article.*

*We'll be back with all-new articles on Monday November 28. See you then!*

 

*This article originally ran Friday, November 18.*

 

*Innistrad* is a graveyard set at its mechanical heart. A quick [Gatherer](https://web.archive.org/web/20111125000000/http://gatherer.wizards.com/Pages/Default.aspx) search reveals that 69 of *Innistrad*'s 249 cards that aren't basic lands have "graveyard" in the text box, and only 27 of those have the flashback mechanic. Another 17 contain the word "dies" and 9 contain "died," and until only recently both of those categories would have showed up in the "graveyard" search. That is quite a lot of cards.

As developers, we know that the graveyard is a dangerous place to mine for design space. There are several reasons for this, and most of them came up in some way or another during *Innistrad* development. I'll run through some of them today as I go down the list of cards that raised them.

![](https://i.ormos.uk/e7/5b/e75bef7e2d25d1b756bf770f0e9ffa505948bc8a6ae391530f54d18b0ba3af79.jpg)

A long time ago, in a galaxy far, far away, [Arc-Slogger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arc-Slogger) was printed. At the time, it was a pretty powerful card; it was a key piece of two different *Mirrodin* Block Constructed decks, one of which ported well into Standard for the next year. A big body that came with what were essentially three free [Shock](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)s was more than strong enough for Constructed. Despite this, it seemed like only tournament players wanted to own the card. Most other people were too allergic to spending undrawn cards in their deck, and [Arc-Slogger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arc-Slogger) was one of the most hated cards in *Mirrodin* according to consumer research.

For years, we have avoided incremental self-milling as a theme both at common and on tournament-strength cards. [Armored Skaab](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armored+Skaab) and [Deranged Assistant](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deranged+Assistant) represent a bit of an exception to that. Both of those cards are critical pieces to nonwhite blue decks in *Innistrad* Limited, and yet the majority of **Magic**-playing humans likely consider [Armored Skaab](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armored+Skaab) to be strictly worse than [Horned Turtle](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horned+Turtle).

Why did we do self-milling this time if we don't normally do it? There was a nice confluence of factors. Our idea for the constructed-out-of-corpses blue zombies all but required easy ways to fill your graveyard, the other four colors in the set were pretty straightforward, and cards that make you a little uncomfortable felt right in a horror-themed set. I'm glad we did them, as the blue decks that mill themselves are an absurd blast for me and other Spikes I know to play, but this represents an exception. I'm also comfortable with blue being the one color that goes this direction, as the kind of people who gravitate toward fiddly and weird decks like those also tend to like blue.

![](https://i.ormos.uk/36/21/36216489db2ec62e9b18b6a6ea41771d45d178b450fdfd1fb81de7f0849987a9.jpg)

I don't remember when this card was added to the file—it was fairly late—but I do remember that it was an attempt to give flashback to creatures. I also remember the first time it really did its thing in a Sealed Deck playtest. I had it in a pretty slow mill-myself deck, and although I hadn't seen anyone else play it yet, I felt like this was the deck for it. The ensuing ridiculous mess of strips of paper as I tried to represent the many different copies of things I had in play caused us some consternation. Large numbers of [Phantasmal Image](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Image)s and [Phyrexian Metamorph](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Metamorph)s are sometimes difficult to keep track of, but that requires drawing many of them in one game. Huge amounts of token clones coming from one card was more of a problem.

Three things saved the card. First, it worked fine on **Magic Online**, where the program creates helpful and fully-texted tokens for you. Second, the card wasn't causing any problems in the Future Future League, so we weren't concerned about seeing all those strips of paper at top tournament tables. Third, art had already been commissioned, and no one could come up with something better for the art we had. That was enough that we decided to let the card do its thing.

![](https://i.ormos.uk/e4/08/e4087095005511a842f47fb69120e08b8ddf49311addf03325e687b7c949f5de.jpg)

During design, Mark often challenged us to find horror tropes that were not black. One that I stumbled upon was the ghostly ancestor who stuck around to help, but was still kind of creepy. The card I designed to that concept became [Dearly Departed](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dearly+Departed). However, my version of the card had it giving +1/+1 counters to every creature you control. What happened?

The long and short of it is that cards that annihilate -1/-1 counters do unfortunately recursive things with [Kitchen Finks](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks) and [Murderous Redcap](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap). For example, there is a Modern deck that uses [Birthing Pod](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birthing+Pod) to assemble [Viscera Seer](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Seer), [Kitchen Finks](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks), and [Melira, Sylvok Outcast](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Melira%2C+Sylvok+Outcast) to gain infinite life. [Dearly Departed](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dearly+Departed) would have been another such card, and Ken Nagle warned us that it would become a key piece of annoying Commander combinations.

My original solution to the problem was to build in some condition under which the card would exile itself, but Erik's more elegant idea was to make it only grant its bonus to Humans. That preserved the always-around feel and conveniently dodged every persist card. Thanks, Erik!

![](https://i.ormos.uk/9b/01/9b01e2033b144842bf0a292c49c0a4bf3c73a6a7bfe106a8558327a2a81fa4cb.jpg)

We still occasionally get complaints about how often we print [Cancel](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel). We like simple and basic effects that we think we have found the right cost for, and [Cancel](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) is not that far off of being a Constructed card anyway. We were more than happy to play the full amount of [Dissipate](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dissipate)s in our Future Future League decks, and the same seems to be true in the real world. There were also plenty of [Stoic Rebuttal](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoic+Rebuttal)s in decks that had very few artifacts last season.

One of our current theories about building fun Constructed environments is that keeping most things at a power level where you can think about playing them, but don't automatically have to, creates variation in a format over time. As long as strong players are willing to play the weaker versions of an effect, we're likely to keep making them that way.

![](https://i.ormos.uk/73/cc/73cc39b4ac3ec7d450c5e3ab97b44e3d36380e9b1d3aba8499cd27587ce04b55.jpg)

[Gravedigger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravedigger) has an abysmal appeal-to-actual-power-level ratio for many people. Who wants to play a four-mana 2/2 that you don't even want to cast on turn four a lot of the time? Strong players know that it's very good, but they also discover that it can be a grindy card that makes for long games and inevitable victories that take a long time to execute. The worst possible situation with [Gravedigger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravedigger) is, of course, a second [Gravedigger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravedigger), which can lead to infinite recursion.

In *Innistrad* Design, Richard Garfield came up with the idea of returning random cards from one's graveyard to one's hand. That lets us make [Gravedigger](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravedigger)-like cards cost less because they're weaker, and also reduces the likelihood of infinite recursion. While this was a fine idea, I'm not sure it plays out that randomly in practice. Two Saturdays ago, I drafted a blue-black Zombie deck with two [Makeshift Mauler](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mauler)s, a [Skaab Goliath](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skaab+Goliath), and a [Corpse Lunge](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corpse+Lunge), and there were very few circumstances when I could not sculpt exactly which Zombie I would get back. I was fine with that, of course, since it meant that my [Grimgrin, Corpse-Born](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grimgrin%2C+Corpse-Born) got to make several encore performances.

I have seen several clever and high-minded Design attempts to fix problems morph into minor hoops for players to jump through to achieve the thing Design was trying to avoid. This instance was extra-weird for me because I was subverting myself. I still don't know if I was supposed to feel guilty or not.

![](https://i.ormos.uk/30/16/3016c2d232f227cb84837e826eebae742f28265ac65102176dc1a0fb5bf1fd7d.jpg)

This card is similar to [Back from the Brink](https://web.archive.org/web/20111125000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Back+from+the+Brink) in that it is a long-game-grinding, gradual-advantage-building card. Graveyard-themed cards seem especially conducive to making this kind of card, and I don't love that. This, however, is my favorite of the *Innistrad* cards in that category. My least favorite thing is when my opponent and I have to keep playing when the course of the game is obvious, and this card minimizes that by naturally including a quadratic growth rate. This card starts off slow, but when I have six 6/6 Oozes out, the game ends quickly. That is also a pretty fun way for a game to end, as slow and grinding game endings go.

![](https://i.ormos.uk/85/a5/85a5ac614dd6b05e1ef2be5a36bd066b14da4128769eb92f965fc5f1bc682d5c.jpg)

I had no idea what to make of this card when it was added to the Design file. I had no idea what to make of it when we finalized the Development file. I still have no idea what to make of it.

As we've mentioned, Richard Garfield worked on the design of *Innistrad*. His instincts for what makes an enjoyable game environment were a joy to be around and key to building the set's structure. His individual card designs, however, often leaned wacky. This is, of course, one of those cards. Because of how strange his cards usually were, we couldn't keep all of them in the file, or the set would have had too large a fraction of really strange cards. This is one of the ones that made the cut.

I'm not sure any of us understand exactly what to do with this. Maybe you do?

![](https://i.ormos.uk/d5/d1/d5d1fed6d74222566ba54a3b46ba8b16805a49e597d32447dbff45d70114edad.jpg)

### Moving On

Graveyard sets seem to be rife with cards that move other cards from one zone to another. While I am not a card, I have also recently experienced a zone change.

Before I worked for Wizards, my gaming experience was almost exclusively from card games. During the past three years, my horizons have expanded into several other genres, including hobby board games and the occasional miniatures game. In particular, though, I have fallen in love with tabletop roleplaying games. I've now flown to several conventions in the past year to play them in the same way that I used to do to play **Magic**; I just got back from one this past Sunday, and that weekend I had as much fun as I used to as a player at a Pro Tour, if not more.

I was recently given the opportunity to move over to **Dungeons & Dragons** R&D. While the decision about whether or not to do so took some soul-searching, it felt right at the time, and it still does. It's going to be strange for a bit, but this way I'll be working on the kind of thing that I care most about.

![](https://i.ormos.uk/93/45/9345bed3ab7251e01fa807fda1376b509caefe20a2563e7832916967501f665e.jpg)

It's been an honor and a joy to be your Latest Developments columnist for nearly three years, but it's time for me to move on. I'll be leaving you and the column in the capable hands of developer Zac Hill. I'll have a little bit more to say the Friday after Thanksgiving, but that will be the last you hear from me for a while.

I would not be the person I am if I had not run into **Magic** in 1997. My fourteen years of **Magic** have taught me about life, hard work, game design, and how to have fun in ways that I don't think I could have replicated with anything else. I hope that one day you can look back and say the same.

 

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>What do you think of Standard with <i>Innistrad</i>?</b></th>&#10;		</tr></thead><tbody><tr><td>I love it!</td>&#10;			<td>2065</td>&#10;			<td>24.8%</td>&#10;		</tr><tr><td>I like it.</td>&#10;			<td>2729</td>&#10;			<td>32.8%</td>&#10;		</tr><tr><td>I don't mind it.</td>&#10;			<td>1077</td>&#10;			<td>13.0%</td>&#10;		</tr><tr><td>I don't like it.</td>&#10;			<td>385</td>&#10;			<td>4.6%</td>&#10;		</tr><tr><td>I hate it!</td>&#10;			<td>187</td>&#10;			<td>2.2%</td>&#10;		</tr><tr><td>I haven't played Standard with Innistrad.</td>&#10;			<td>1872</td>&#10;			<td>22.5%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>8315</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>