---
id: k18d2mqy
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/07-23-architecting-archenemy
title: Architecting Archenemy
published: '2010-07-23'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    lang_detected: en
    capture_id: 718039
    url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    captured_at: '2022-08-10 14:57:48+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    lang_detected: en
    capture_id: 718039
    url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    captured_at: '2022-08-10 14:57:48+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    lang_detected: en
    capture_id: 718039
    url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    captured_at: '2022-08-10 14:57:48+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    lang_detected: en
    capture_id: 718039
    url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
    captured_at: '2022-08-10 14:57:48+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: k18d2mqy
  url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
  page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
  lang: en
  template: drupal
  captured_at: '2022-08-10 14:57:48+00'
  capture_id: 718039
  wayback_url: https://web.archive.org/web/20220810145748id_/https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22
- document_id: k18d2mqy
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/100
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/100
  lang: en
  template: aspx
  captured_at: '2013-07-07 05:43:59+00'
  capture_id: 612689
  wayback_url: https://web.archive.org/web/20130707054359id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/100
- document_id: k18d2mqy
  url: https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-23
  page_key: magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-23
  lang: en
  template: drupal
  captured_at: '2022-05-24 23:03:06+00'
  capture_id: 718040
  wayback_url: https://web.archive.org/web/20220524230306id_/https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-23
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: k18d2mqy
  capture_id: 612689
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/100
  wayback_url: https://web.archive.org/web/20130707054359id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/100
  captured_at: '2013-07-07 05:43:59+00'
  template: aspx
  sha256: 18c0af90904f4f59ba9106202b482c43fedabae7f3c988da219e679d8bd3215f
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Stormtide Leviathan
  - Grave Titan
  - Primeval Titan
  - Baneslayer Angel
  - Time Reversal
  - Gaea's Revenge
  - Demon of Death's Gate
  - Sun Titan
  - Platinum Angel
  - Jace Beleren
  - Garruk Wildspeaker
  - Inferno Titan
  - Chandra Nalaar
  - Ajani Goldmane
  - Frost Titan
  - Liliana Vess
  - Jace's Erasure
  - Jace's Ingenuity
  - Liliana's Caress
  - Liliana's Specter
  - Chandra's Outrage
  - Chandra's Spitfire
  - Garruk's Companion
  - Garruk's Packleader
  - Ajani's Mantra
  - Ajani's Pridemate
  occurrences: 26
---
Welcome to the end of Multiplayer Week. I do not often play multiplayer, and amusingly, I wrote a multiplayer development [column](/en/articles/latestdevelopments/2009/09-04-developing-for-multiplayer) a year ago for [*Planechase*](https://web.archive.org/web/20130704094451/http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/planechase/productinfo) Week. If that's what you're looking for today, you might want to check that out. Rather than do that again, I'll be talking about [*Archenemy*](https://web.archive.org/web/20131220141302/http://www.wizards.com/Magic/TCG/ProductArticle.aspx?x=mtg/tcg/archenemy/productinfo) today, as I never quite got the chance to do that the way I wanted to before ***Magic** 2011* came out.

As is tradition, let's meet the team ...

### The Team

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg) **Tom LaPille:** That's me! *Archenemy* was the first paper product I led; my previous leads were **Magic Online** sets—*Masters Edition III* and the upcoming *Masters Edition IV*, which you'll see later this year. Also, as Aaron [mentioned](/en/articles/feature/2010/06-28-magic-2011-has-big-shoes-to-fill) earlier on this site, I'm currently leading a little project with the code name "M12." I'm not the biggest fan of Free-For-All multiplayer because I don't enjoy politics, but I do love the team interaction that Two-Headed Giant brings. That made this the perfect mulitplayer product for me to lead, and I had a blast doing it.

![](https://i.ormos.uk/ce/2c/ce2c01f6b41d58dd99064dcf0866c5ffb9b2a4af28307f6c38e3584127b77248.jpg) **Scott Larabee:** Scott manages the **Magic** tournament system from the ground up. Among other things, that means being at every Pro Tour, at which it's never difficult to find him playing EDH after hours with judges. Scott is building quite a resume of multiplayer product teams, as he also worked on the *Planechase* development team. His work on both products was awesome, and not that I'd know anything about this sort of thing, but I'd be surprised if he didn't end up on another multiplayer product team in the near future.

![](https://i.ormos.uk/55/c1/55c15279e289f2a4f448f07024ec45a6a6749744d19701e7536c7c0341c8de91.jpg) **Lee Sharpe:** Lee once worked on programming **Magic Online**, and has since moved on to a data analysis role. You can also often find him at conventions running the **Magic Online** live series tournaments. Lee demonstrated his passion for multiplayer when he disappeared into a cave one weekend and singlehandedly coded the Commander format for **Magic Online**. Lee also has been part of the team that does **Magic** rules and templating for several years, and that experience helped us navigate the rules issues that we ran into.

![](https://i.ormos.uk/f0/72/f0720a9292c2c5be800aefded8bf71f579f2ec9657cc13c67ac053bb5e76dfa6.jpg) **Andy Smith:** Andy is the scheduling guru who makes sure that everything at Wizards happens on time. He's somewhat soft-spoken and his role in the company is not one that most people think about regularly, but he's essential to getting you your **Magic** cards on time. He also loves to play **Magic** of any kind, multiplayer or not, and we learned a bunch from the several times he took early versions of *Archenemy* to his play groups inside Wizards.

![](https://i.ormos.uk/2b/09/2b094d288b20f58968d51834eb02b2ed1381ae876700918a5c14f07004174e55.jpg) **Mike Turian:** Mike has led several sets: *Future Sight*, *Morningtide*, *Worldwake*, and now *Scars of Mirrodin*. He also led *Planechase*, last year's multiplayer product. He's also in the Pro Tour hall of fame, and is one of the greatest Limited players to have ever touched a **Magic** card. Mike's expertise was invaluable, as he is both very good at **Magic** and experienced at doing all the things that I was about to do on my first paper product lead.

### The Rules

We don't normally get to craft rules when we make a **Magic** set. However, that is something that comes with the territory when you're dealing with entirely new card types and game structures. There were some questions that needed answers.

One category of questions had to do with the multiplayer mechanics that were independent of the schemes. We knew that we wanted turns to alternate between the archenemy and a team that took Two-Headed-Giant-style simultaneous turns. The design team handed off a starting life total system for the archenemy that scaled with the number of players, but it was a little bit more complicated than I wanted. We eventually chose to fix the archenemy's life total at 40 to simplify things. This also let us send the message that if you're having trouble beating the archenemy, you should find more friends.

![](http://media.wizards.com/images/magic/daily/ld/ld100_rules.jpg) 

  

The other category of questions had to do with the schemes. One question was when the archenemy would scheme. *Archenemy* lead designer Ken Nagle handed off the product with schemes happening at the beginning of the archenemy's upkeep, which didn't quite work the way we wanted. First, this often led to having to make decisions before you knew what card you would draw for the turn, which was tricky. Sometimes that decision even involved deciding how much mana to pay, which was an especially annoying thing to do before drawing a card. The other problem is that players are used to untapping, drawing a card, *then* doing interesting things. Getting them to insert an extra step in between those two actions was tough; what often happened was people would scheme after their draw because they just forgot to do it beforehand. We got to solve both of those problems by having the scheme happen at the beginning of the archenemy's main phase.

### The Words

Another unique problem to this product was that we had oversized cards of a new type, and we needed to name them. Matt Tabak was the editor and rules manager for this product, so this task would be his responsibility. We called them "boss cards" for quite a while, but that's not exactly something we can print.

The first clue as to what we should do for these came when Creative lead Brady Dommermuth concepted the first five boss cards with names like "Say Hello to My Little Friend," "Your Fate is Thrice Sealed," and "Your Puny Minds Cannot Comprehend." These set the Creative tone for the product, and inspired Matt to look for a card type name that had the same flavor. The tentative name he settled on was "scheme," and it basically stuck from the beginning. There was some vacillation in the beginning between "ongoing" and "enduring" to describe the schemes that don't go away forever. I don't recall why he chose "ongoing"; I can guess in hindsight that it was because it doesn't imply the length of the duration through which it lasts, but I'm not sure.

![](http://media.wizards.com/images/magic/daily/ld/ld100_2Schemes.jpg) 

  

That wasn't the last of our problems, though. We also needed rules words to describe the act of playing a scheme card and what happens when an ongoing scheme is done. Matt continued his quest for flavorful words, and found "setting a scheme into motion." You can see from the printed scheme cards that this one stuck. He also found "thwart" for the game action of ending a scheme. We were all excited about the Scooby-Doo-esque vibe that "thwart" gave us, so we put it on cards and did some playtesting.

It was then that we discovered two problems. First, when an ongoing scheme is good for the archenemy, it feels weird to read "thwart this scheme" on it. One does not wish to thwart one's own schemes, but that's exactly what the card would command you to do. Our next try was the passive voice "This scheme is thwarted." We found the passive voice to be a little distasteful, and there were also several schemes that then read "thwart this scheme and \[do something terrible to the players\]." That's silly, because the scheme wasn't actually thwarted at all.

![](http://media.wizards.com/images/magic/daily/ld/ld100_abadon.jpg) 

  

We solved these two problems separately. First, we switched from "thwart" to "abandon" to avoid passive voice. Second, I cut all the schemes on which thwarting or abandonment was not unambiguously good for the players. That gave us cards that read both cool and sensibly.

### The Schemes

![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme01a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme01b.jpg)

This is one of the most powerful schemes we made. Extra turns are really good no matter what is going on, but are especially good when you have a whole team of hungry heroes ready to take advantage of the slightest "shields-down" moment. The design version of this card however, did not have the second sentence on it, which made it even more sick. In fact, it was so sick that it was better than every other scheme, because it gave you another scheme next turn. It's okay to have good cards, but it's not interesting when one card is better than every other card. Rather than make this strictly better than every other scheme, we took away the scheme on your extra turn.

  
 ![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme02a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme02b.jpg)

Both Aaron Forsythe and Ken Nagle love putting their opponents in untenable positions and watching them squirm. Midway through *Archenemy* development, Aaron pitched the idea for "hot-seat" schemes that would force one player to make a decision for the whole team about what sort of bad thing happens. I pitched this to Ken, and Ken liked it so much that he asked to put one such scheme in each deck. In addition to those four schemes, we liked the hot-seat technology so much that we put it on other schemes. For example, Nature Demands an Offering once asked the archenemy's opponents to collectively make a decision about what permanents to lose. That was hard to do under the **Magic** rules, so instead we put the decision to a player of the archenemy's choice.

I'm glad we chose to run with Aaron's suggestion. One of my favorite things to do in *Archenemy* is point one of the hot-seat schemes at people who are not team players. Mike Turian and Ken Nagle, for example, can both be counted on to choose "others" whether or not it's better for the team. Exploiting things like that is one of the best ways for an archenemy to get an edge!

  
 ![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme03a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld100_scheme03b.jpg)

One of the cool things about developing products designed by Ken Nagle is that he often does a strange sort of development before he gives it to you. Ken understood that one of the ways that *Archenemy* goes wrong is for one of the players to have a spell-based combination deck that you aren't prepared to interact with. To help protect against that, he made this card, which seriously punishes an opponent for not playing along and having creatures. It's still good against creatures, of course, but it's far worse for someone who has no creatures to feed to this scheme.

### Correction

I stated two weeks ago that Stormtide Leviathan was designed by Greg Marques. This was incorrect; it was actually designed by **Magic Online** architect Ryan Dhuse. My apologies to both of them for the mistake.

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> What is your favorite <i><b>Magic</b> 2011</i> mythic rare? </b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Grave Titan</a>&#10;    </td>&#10;    <td>1778</td>&#10;    <td>21.40%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Primeval Titan</a>&#10;    </td>&#10;    <td>1209</td>&#10;    <td>14.50%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Baneslayer Angel</a>&#10;    </td>&#10;    <td>1049</td>&#10;    <td>12.60%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Time Reversal</a>&#10;    </td>&#10;    <td>655</td>&#10;    <td>7.90%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Gaea's Revenge</a>&#10;    </td>&#10;    <td>598</td>&#10;    <td>7.20%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Demon of Death's Gate</a>&#10;    </td>&#10;    <td>590</td>&#10;    <td>7.10%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I'm not particularly fond of any of them</td>&#10;    <td>578</td>&#10;    <td>6.90%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Sun Titan</a>&#10;    </td>&#10;    <td>523</td>&#10;    <td>6.30%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Platinum Angel</a>&#10;    </td>&#10;    <td>243</td>&#10;    <td>2.90%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Jace Beleren</a>&#10;    </td>&#10;    <td>236</td>&#10;    <td>2.80%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Garruk Wildspeaker</a>&#10;    </td>&#10;    <td>219</td>&#10;    <td>2.60%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Inferno Titan</a>&#10;    </td>&#10;    <td>194</td>&#10;    <td>2.30%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Chandra Nalaar</a>&#10;    </td>&#10;    <td>128</td>&#10;    <td>1.50%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Ajani Goldmane</a>&#10;    </td>&#10;    <td>123</td>&#10;    <td>1.50%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Frost Titan</a>&#10;    </td>&#10;    <td>104</td>&#10;    <td>1.20%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <a>Liliana Vess</a>&#10;    </td>&#10;    <td>96</td>&#10;    <td>1.20%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>8323</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

### This Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                 <b>Which pair of planeswalker cards is your favorite?</b></td>&#10;                <td> </td>&#10;                <td>&#10;                  <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                </td>&#10;              </tr>&#10;              <tr>&#10;                <td colspan="3">&#10;                  <table>&#10;                    <tbody><tr>&#10;                      <td>&#10;                        <div id="pollmtg_daily_ld_100_poll1">&#10;                          <div>&#10;                            &#10;                            &#10;                            <a>Jace's Erasure</a> and <a>Jace's Ingenuity</a>.<br><a>Liliana's Caress</a> and <a>Liliana's Specter</a>.<br><a>Chandra's Outrage</a> and <a>Chandra's Spitfire</a>.<br><a>Garruk's Companion</a> and <a>Garruk's Packleader</a>.<br><a>Ajani's Mantra</a> and <a>Ajani's Pridemate</a>.<br>I do not like the Planeswalker signature spells.<br>I'm not sure.<br></div>&#10;                          <div>&#10;                            &#10;                          </div>&#10;                          <div></div>&#10;                        </div>&#10;                      </td>&#10;                    </tr>&#10;                  </tbody></table>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

* * *

[![](https://i.ormos.uk/16/db/16dbe0ac881e02a455caf551c7488edc692e5d8c3ea4a7254bdaa6679a535bd9.jpg)](https://web.archive.org/web/20130704153147/http://www.wizards.com/magic/digital/magiconline.aspx)