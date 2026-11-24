---
id: j0g73s00
kind: article
lang: en
path: /en/articles/latestdevelopments/2003/09-26-post-development-digest
title: Post-Development Digest
published: '2003-09-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    lang_detected: en
    capture_id: 729731
    url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    captured_at: '2022-01-24 16:27:31+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    lang_detected: en
    capture_id: 729731
    url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    captured_at: '2022-01-24 16:27:31+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    lang_detected: en
    capture_id: 729731
    url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    captured_at: '2022-01-24 16:27:31+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    lang_detected: en
    capture_id: 729731
    url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
    captured_at: '2022-01-24 16:27:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: j0g73s00
  url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
  lang: en
  template: drupal
  captured_at: '2022-01-24 16:27:31+00'
  capture_id: 729731
  wayback_url: https://web.archive.org/web/20220124162731id_/https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
- document_id: j0g73s00
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb90
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb90
  lang: en
  template: aspx
  captured_at: '2014-05-24 20:58:25+00'
  capture_id: 805483
  wayback_url: https://web.archive.org/web/20140524205825id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb90
- document_id: j0g73s00
  url: https://magic.wizards.com/en/articles/archive/post-development-digest-2003-09-26
  page_key: magic.wizards.com/en/articles/archive/post-development-digest-2003-09-26
  lang: en
  template: drupal
  captured_at: '2021-04-29 03:51:30+00'
  capture_id: 1141456
  wayback_url: https://web.archive.org/web/20210429035130id_/https://magic.wizards.com/en/articles/archive/post-development-digest-2003-09-26
- document_id: j0g73s00
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb90,,ja
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb90
  lang: en
  template: classic_asp
  captured_at: '2004-08-15 19:16:43+00'
  capture_id: 1993390
  wayback_url: https://web.archive.org/web/20040815191643id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb90,,ja
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: j0g73s00
  capture_id: 729731
  url: https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
  wayback_url: https://web.archive.org/web/20220124162731id_/https://magic.wizards.com/en/articles/archive/latest-developments/post-development-digest-2003-09-26
  captured_at: '2022-01-24 16:27:31+00'
  template: drupal
  sha256: a083ea58911aba3c0ab9505a4ec77169cd43480660134f61fc13aac52566cadf
render_recovery: []
---
## Stories from the Making of Mirrodin

As I was trying to figure out what to write my column about this week, I was reviewing the *Mirrodin* file and reminding myself of interesting anecdotes from our development work last fall and winter. I kept accumulating stories that I thought would be fun to tell, but none of them seemed worthy of an entire article. Here, therefore, are three completely unconnected tales from the trenches of *Mirrodin* development.

### How Many Thumbs Do Goblins Have, Anyway?

Legends are some of the coolest **Magic** cards we produce. Normally our legends are creatures that are so powerful that they are one of a kind. Whether they are characters from the novels or other unique creatures from the world, they are always big and splashy. However, this is yet another one of our "rules" that we broke in *Mirrodin*. *Mirrodin* has a card that we turned into a legend mostly just because we couldn't figure out what would happen if there were two of them in play at the same time:

![](http://archive.wizards.com/global/images/mtgcom_daily_rb90_pic1_en.jpg)

Don't get me wrong, it makes perfect sense for [Krark's Thumb](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krark%27s+Thumb) to be a legend. After all, there's only one Krark and he only had two thumbs. When our creative team was handed this card mechanic, they even suggested to the development team that we turn it into a legend so their "Krark's Thumb" concept would be stronger. The development team initially decided not to make that change because the card didn't seem special enough to be worthy of legendary status and we also thought it would be kind of cool to have people design coin-flip decks that wanted to get multiples copies of this card into play. Our creative guys were ok with that, reasoning that there could be hundreds of goblins running around all of whom thought they were the proud owner of Krark's lucky thumb, but in fact none of them had the real deal.

Enter the templating team. As the templating team carefully navigates a new card set through the rules minefield, R&D frequently plays the role of Furt. We walk right up to what the rules experts know is the most suspicious-looking bump and prod it with our pointy sticks. BOOM! And that's what happened with Krark's Thumb. The Dev team had initially worded the card as "Whenever you flip a coin, flip an additional coin," which, as a triggered ability, kicked in too late to actually do anything. But what we really cared about was making sure players would know what to do if there were two of these in play at the same time. Obviously there were two basic options: either you got to flip three coins, because the second Thumb added one additional coin to your overall "flip," or you got to flip four coins, because each of your two flips got replaced with a flip plus an additional flip. The Dev Team preferred that you get three coins, not four, when you had two Thumbs in play, but we would have been willing to give up on that goal if the only really good wording gave people four coins. The tricky bit was making the card both unambiguous and compatible with the **Magic** rules system.

All kinds of somewhat obscure rules issues kept cropping up to cause problems for all of our elegant wordings (which either "went infinite" or did nothing at all), and all of our rules-tight wordings seemed clunky and hard to parse. After banging our heads against this problem for quite a while, I remembered that the creative team kind of preferred that this card be a legend anyway, so I proposed that we make it a legendary artifact and then there could never be two of them in play at the same time anyway. Thus we no longer needed to solve that particular puzzle. It does make the coin-flip deck a bit less consistent, but with cards like [Fiery Gambit](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Gambit) running around that's probably actually a good thing.

### Where Are the Multilands?

![Talisman of Progress](https://i.ormos.uk/ed/16/ed16f0a4275a7def790b756673cc34627efcd80f1ae8e37f3fba7a8ec4343e46.jpg)

I read a lot of speculation on message boards about what lands *Mirrodin* would contribute to the world. Most of these threads pointed back to my article ["Tending the Land"](/en/articles/feature/2002/08-02-tending-the-land) where I promised that every block would have a cycle of multilands that would help make two-color decks more viable. Well, most of you have probably already noticed that *Mirrodin* doesn't technically have a cycle of multilands, but what it does have are the "painstones":

Only time will tell if the Talismans are as effective at promoting multicolor decks as a good cycle of lands. They probably aren't as powerful as the *Onslaught* fetch lands (like [Wooded Foothills](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wooded+Foothills)), but I think they are better than the *Odyssey* filter lands (like [Mossfire Valley](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mossfire+Valley)). They should be plenty good enough to get the job done in *Mirrodin* Block Constructed, and I think they will be relevant to Standard and other constructed formats.

In any case, I still believe everything I wrote about lands last year; I just think of artifact mana as accomplishing the same task as nonbasic lands.

### The Birth of Robo-Jens

The Talismans weren't the only example in *Mirrodin* of cards turning into artifacts simply to fit into the environment a little better. Jens Thoren's Invitational card made a very similar transition.

![](http://archive.wizards.com/global/images/mtgcom_daily_rb90_pic2_en.jpg)

When Jens won the **Magic** Invitational and earned the right to design his own **Magic** card, he submitted "Forestfolk," which was essentially the same card we wound up printing, except it cost ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) to play (and the "draw a card" ability triggered whenever it left play instead of just when it went to the graveyard). We knew right away that we didn't want to have any "gold" cards in *Mirrodin* (and we also thought the card wouldn't be very exciting if you had to have both blue and green mana before you could play your mana-fixing card) so we turned it into a monogreen card as soon as we put it into the set. We were also concerned that four mana total was a pretty steep price to pay for a mana-fixer, so our initial testing was done with a version that cost ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) and gave you a 2/1 creature.

Our initial ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), 2/1 version of this card lasted about a day. Once we started playing with Jens's card we realized how good it was and how Jens had been right all along -- it really did need to cost four -- and so we tested it at ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), 2/2 for a while.

One of the things I have always thought was cool about Invitational cards is the way in which R&D has managed to stay true to the spirit of the initial submission, but at the same time integrate them into the upcoming block. Darwin Kastle's [Avalanche Riders](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Avalanche+Riders), for example, gained echo. Chris Pikula's [Meddling Mage](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage) turned into a multicolored card. Kai Budde's [Voidmage Prodigy](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voidmage+Prodigy) turned into a "tribal" card. Wouldn't it be cool, I argued to the *Mirrodin* development team, if Jens's card were an artifact creature? We decided to try it out with a cost of ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif) and it worked out so well that we never went back. It was so good that for a while we were testing it as a four-mana 2/1, but in the end we decided to leave the power and toughness right where Jens submitted them.

Solemn Simulacrum may not look super-powerful, but trust me, once you start playing with it you'll see that rolling all those abilities onto one card is actually quite a saucy combination. While it's not the splashiest card we've ever made, it's extremely efficient. Essentially, it's card advantage incarnate and while that may not turn Timmy on, the Spikes of the world are going to see a lot of Jens's face over the next few years.

(By the way, the [slate for this season's Invitational](https://web.archive.org/web/20030926000000/http://archive.wizards.com/default.asp?x=sideboard/news/20030919b) was recently announced over on Sideboard.com. The date for the event hasn't been chosen yet, but those are the sixteen players who will be duking it out on ***Magic** Online* to see who gets the right to make his own card.)

### This Week's Poll:

**What do you think of Aaron Forsythe's move from the Web team into R&D?** How dare you guys steal Aaron away from us?!Good for him! And good luck to him.Ask me again once I see how good his replacement is.Who?

### Last Week's Poll:

<table><thead><tr><th colspan="3"><b>Are you glad we reprinted <a href="https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triskelion">Triskelion</a>?</b></th>&#10;		</tr></thead><tbody><tr><td>Yes – It's nice to see old favorites like Trike come back.</td>&#10;			<td>9055</td>&#10;			<td>82.1%</td>&#10;		</tr><tr><td>No – I like some reprints, but Triskelion is not cool.</td>&#10;			<td>1430</td>&#10;			<td>13.0%</td>&#10;		</tr><tr><td>No – Every card in expert level sets should be brand new.</td>&#10;			<td>538</td>&#10;			<td>4.9%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>11023</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

My favorite email from last week: "Anyone who doesn't think [Triskelion](https://web.archive.org/web/20030926000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triskelion) is cool should get a punch in the face."

*Randy may be reached at latestdevelopments@wizards.com.*