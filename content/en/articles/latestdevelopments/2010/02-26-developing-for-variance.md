---
id: h58d47rc
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/02-26-developing-for-variance
title: Developing for Variance
published: '2010-02-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    lang_detected: en
    capture_id: 721093
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    captured_at: '2022-10-03 22:17:37+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    lang_detected: en
    capture_id: 721093
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    captured_at: '2022-10-03 22:17:37+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    lang_detected: en
    capture_id: 721093
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    captured_at: '2022-10-03 22:17:37+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    lang_detected: en
    capture_id: 721093
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
    captured_at: '2022-10-03 22:17:37+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: h58d47rc
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
  lang: en
  template: drupal
  captured_at: '2022-10-03 22:17:37+00'
  capture_id: 721093
  wayback_url: https://web.archive.org/web/20221003221737id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-25
- document_id: h58d47rc
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/79
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/79
  lang: en
  template: aspx
  captured_at: '2013-07-02 14:12:31+00'
  capture_id: 623595
  wayback_url: https://web.archive.org/web/20130702141231id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/79
- document_id: h58d47rc
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-26
  lang: en
  template: drupal
  captured_at: '2022-07-01 23:39:09+00'
  capture_id: 721095
  wayback_url: https://web.archive.org/web/20220701233909id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-variance-2010-02-26
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: h58d47rc
  capture_id: 623595
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/79
  wayback_url: https://web.archive.org/web/20130702141231id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/79
  captured_at: '2013-07-02 14:12:31+00'
  template: aspx
  sha256: 44798fe0f56997518fd2efc18fbcc1513851f881ed65fee35f4740bc54ed3050
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Runeclaw Bear
  - Baloth Woodcrasher
  - Turntimber Basilisk
  - Roil Elemental
  - Hagra Crocodile
  - Hedron Rover
  - Calcite Snapper
  - Gnarlid Pack
  - Enclave Elite
  - Skitter of Lizards
  - Quag Vampires
  - Apex Hawks
  - Jace, the Mind Sculptor
  - Sage Owl
  - Sensei's Divining Top
  occurrences: 20
---
W*orldwake* contains five common creatures with multikicker.

  

![](https://i.ormos.uk/7c/28/7c281b55b2212546e2f7e248079df0c77139d43b614e03dc303d1ab62a67c4bf.jpg) 

  

This is Multikicker Week, and today I will tell you the story of these five cards. However, like any good development story, it is not short, involves lots of playtesting and spirited debate, and requires a little background. If you're ready, let's hop in the time machine and go back to the middle of *Zendikar* development ....

![](https://i.ormos.uk/c5/a7/c5a78fd4c10e9b2bad9ac5a4ac0ec75a99e228334e0c9ed25031a4ceec05ad75.jpg) While we were working on *Zendikar*, **Magic** developers discovered two quirks about the *Zendikar* Limited format. The first, and this is an observation that many players have made since the set released, is that it is extremely fast. The set is full of creatures with landfall triggered abilities. Unless you're doing something special, you can only put a land onto the battlefield on your own turn, so all these creatures are stronger on attack than on defense. The set is also full of Allies, and just like lands, in most situations you are playing Allies on your own turn. Once again, Allies encourage you to attack, not defend, as so many of their triggers are only active on your turn.

As we got used to how many of *Zendikar*'s creatures were stronger on the attack than on defense, we adjusted our drafting to match. Our decks kept getting more and more aggressive. We eschewed six-mana fatties for two-mana 2/1s, and after discovering how strong two-mana creatures were in this world, we started picking them higher and higher. We were self-aware about this, of course, and often wondered to ourselves whether this was a good thing or not. Eventually, however, we decided to embrace it. The Limited format immediately preceding *Zendikar* was ***Magic** 2010*, which was on the slower end of the range of speeds we like Limited formats to be. We know that change is what keeps **Magic** fresh. The change of speed from ***Magic** 2010* to *Zendikar* was jarring, but it would certainly keep you on your toes.

Although a Limited format being fast isn't automatically a problem, we discovered a second quirk of *Zendikar* Limited that we did consider to be problematic. That quirk was that it was very difficult to come back from behind. Often, a Limited game progresses to a point where neither player has cards in hand, and both are playing off the top of their libraries. Usually, when this happens one player is in a worse position than the other. In other Limited formats, one of the most important ways such a player could come back was for the other player to draw a string of "blanks," or cards that didn't do anything in the situation. If the opponent draws blanks for a few turns while you draw "live" cards, or cards that do relevant things, you'll be back in the game in no time.

Although a few nonland cards can be blanks, like Runeclaw Bear on a board full of huge creatures, the largest category of midgame blanks in most formats is lands. *Zendikar*, however, is not most formats. It's not uncommon in a midgame stall to want to draw a land in exactly those situations where in any other format you'd be hoping for a spell. Perhaps a land would let you pump your Baloth Woodcrasher, use your Turntimber Basilisk to take out your opponent's second-best creature, and use your Roil Elemental to steal the best one. Most situations aren't this dramatic, but merely giving a Hagra Crocodile +2/+2 can be the difference between doing nothing and making a strong attack. Of course, the alternative to drawing a land is drawing a spell, which is also a fine thing to draw on a stalled board—such a strong alternative, in fact, that it's exactly what you hope for in any other Limited format!

![](https://i.ormos.uk/9e/94/9e94c7c2c514aa100725c8e150e7d18d3f15d7d86b5e42d9fea50d44600f1f71.jpg) 

  

We've just established that in *Zendikar*, both spells and lands are live draws in midgame stalls. You will note, of course, that every card in your deck is either a spell or a land, so nearly any card drawn in the midgame contributes to a player's board position. How delicious, then, to be the player who is ahead on board. When there are few blanks to draw in either library, the variance in power of draws is very low, and that's exactly what the player who is ahead on board wants. If the game continues in the way it has gone so far, that player will win, and because of the lowered variance that the landfall mechanic provides, a player who pulls ahead is much more likely to stay in the lead.

Because of this, the development team was a little unhappy with the variance-reducing effect landfall had on *Zendikar* Limited games. Just like you, we want **Magic** to be a game of skill, but there is already plenty of skill in **Magic** already. (If you don't believe this, try playing against a player who is much, much weaker or much, much stronger than the players you normally play against. The difference in your win rate should be jarring.) We love dramatic come-from-behind victories, and we value that **Magic** allows them to happen. Mechanics that reduce variance in game play risk keeping them from happening often enough.

![](https://i.ormos.uk/b9/39/b9393aa785646f08a29a7084be7959fde2781c1b1d24a05a9ea276f0c978a535.jpg) 

  

We had these two quirks in mind when we started working on *Worldwake*. As I said before, we saw *Zendikar*'s speed not as a problem, but as a natural part of the evolution of **Magic** over time. However, going by the same logic that led us to believe *Zendikar* could be that fast, *Worldwake* had to change the speed some. Because *Zendikar* was near the fastest we are willing to make a format, the natural thing to do with *Worldwake* was to pull the speed back a little bit. Because drafts use two packs of *Zendikar* and one pack of *Worldwake*, we couldn't change the speed too much, but we wanted to slow it down a little bit.

Because we were less happy with the other quirk, we decided to try to change it. This being the second set in the *Zendikar* block, we didn't have the option of rejecting landfall and Allies as mechanics. However, we could choose to be more careful about how we used them in order to build more comeback potential into Limited games, and that's exactly what we did.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hedron Rover" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hedron%20Rover&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Calcite Snapper" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Calcite%20Snapper&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

These conclusions affected everything we did in *Worldwake* development. One place you can see the results of these decisions is in the common landfall creatures that *Worldwake* has to offer. While five commons in *Zendikar* have landfall triggers that give them +2/+2, only Hedron Rover in *Worldwake* receives that bonus on landfall. Calcite Snapper is the only other creature in *Worldwake* whose power and toughness change upon landfall; I don't think anyone would call that card a poor blocker, as a 1/4 with shroud is no jokes. The other landfall creatures gain things like vigilance and flying, which encourage you to attack but give you plenty of power and toughness to use on defense.

I don't have time to talk about all of the ways we addressed this, but I wanted to give you a glimpse of how those goals changed our thinking. This is, however, an article about the five common multikicker creatures, so let's move on to them.

Mark Rosewater invented multikicker during *Zendikar* design, but it was decided that it would be put off to *Worldwake*. As we got closer to the beginning of *Worldwake*'s development, we had those two quirks of *Zendikar* Limited in mind. Once again, we liked multikicker as a mechanic, but we made the unhappy discovery that it also reduced the variance in draws. 

![](https://i.ormos.uk/51/a1/51a1751dc76397dbaf5dc70867470ca9632d652e908265052c221dcd4e830f86.jpg) 

  

Take Gnarlid Pack, for example. Because of how fast *Zendikar* Limited is even after *Worldwake*, we thought it was usually correct to just play it on turn two as a 2/2 if it was our only two-mana creature. However, if it were a Runeclaw Bear, we might end up drawing it on turn twelve when a 2/2 creature wasn't a big deal. Thanks to multikicker, Gnarlid Pack doesn't have that problem. If you draw it on turn twelve, you can just play it as a 5/5 or 6/6. No matter when in the game you draw it, it's quite good for you. This reduces variance in exactly the way that landfall does. With fewer ways for cards to come up in the wrong order, it's hard for someone to come back from a poor position.

Except for Enclave Elite, each of the common multikicker creatures left design exactly as they are, with only one difference: the multikicker cost was ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif). Fellow developer Erik Lauer was the first to point out how potentially dangerous their variance-reducing qualities were, and when I realized how strong they were, I started agitating for change. I liked Skitter of Lizards and Quag Vampires as they were, but Apex Hawks and Gnarlid Pack grated on me; they were both cards that were rather strong in the *Zendikar* / *Worldwake* format before any abilities were added to them, and the multikicker ability just put them way over the top.

I talked so much about this that *Worldwake* lead designer Ken Nagle, in his infinite griefing powers, chose to make each of their playtest names friendly pokes at me. We have physical copies of two of them:

![](https://i.ormos.uk/33/9d/339d5a288ccc3d8e3f669009450612988f28b19183b72eb7983e34dde6b1e31a.jpg) 

  

The other three were Tom Foolery, Ginger Folk, and White Board Menace, the last a reference to the whiteboard I joke about having used to order my job at Wizards from the universe—a great story that could perhaps be an article one day.

My annoyance at these creatures never really went away. Although my fellow developers agreed with my statements about them, they weren't sure what to do about it, and *Worldwake* lead developer Mike Turian was wary of my proposals because many of them would have made that cycle much less appealing as a whole. I eventually chose to fight for making the green one start at ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 3/3. Mark Rosewater, however, hated that idea; he thought players would feel better about casting a ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 3/3 if they had gotten to pay the multikicker cost, which is clearly what you were supposed to do with the card in the first place. 

![](https://i.ormos.uk/04/e3/04e3a40ed988b0387b9c1ec56fb635fdce162ea0c71d98aac11d5102638ededb.jpg) 

  

The story has a happy ending, however, as Mike offhandedly suggested during one meeting that we change the multikicker cost on these cards from ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif) to "1C"—R&D slang for one generic mana and one colored mana of the appropriate color. As soon as he suggested it, I knew we had found what we were looking for. The cards would read almost as excitingly, but they would be less consistently powerful in the late game because you might have drawn the wrong mix of lands to kick them with all of your mana. It was clear after one playtest that this change returned a significant amount of comeback potential to *Zendikar*-*Worldwake* Limited, and we settled on 1C for the multikicker costs of those creatures.

**Magic** development is a complex puzzle. To do it well, we have to take in and weigh lots of information, including playtest data, past experiences, and opinions from non-developers. Every card has a story, and the story of these five cards should show you just how detailed those stories can be. We put tons of effort into each **Magic** card, though, and we have a blast while we make them. We hope you're having fun with them too!

**Last Week's Poll** 

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> What is your favorite <i>Worldwake</i> mythic rare card? </b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Jace, the Mind Sculptor</td>&#10;    <td>2388</td>&#10;    <td>28.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Abyssal Persecutor</td>&#10;    <td>1378</td>&#10;    <td>16.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Dragonmaster Outcast</td>&#10;    <td>854</td>&#10;    <td>10.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Omnath, Locus of Mana</td>&#10;    <td>846</td>&#10;    <td>10.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Admonition Angel</td>&#10;    <td>569</td>&#10;    <td>6.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Wrexial, the Risen Deep</td>&#10;    <td>551</td>&#10;    <td>6.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Novablast Wurm</td>&#10;    <td>521</td>&#10;    <td>6.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Eye of Ugin</td>&#10;    <td>482</td>&#10;    <td>5.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Comet Storm</td>&#10;    <td>350</td>&#10;    <td>4.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Avenger of Zendikar</td>&#10;    <td>319</td>&#10;    <td>3.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>8258</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

My answer to this poll is Jace, the Mind Sculptor. While fiddling around with the top of one's library is not what every **Magic** player loves, there is a subset of players that adores cards like Sage Owl and Sensei's Divining Top. I am one of those players, and I love using Jace to sculpt games over many turns.

**This Week's Poll** 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                 <b>What do you think of Standard with <i>Worldwake</i>?</b></td>&#10;                <td> </td>&#10;                <td>&#10;                  <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                </td>&#10;              </tr>&#10;              <tr>&#10;                <td colspan="3">&#10;                  <table>&#10;                    <tbody><tr>&#10;                      <td>&#10;                        <div id="pollmtg_daily_ld_79_poll1">&#10;                          <div>&#10;                            &#10;                            It's awesome!<br>It's good.<br>It's okay.<br>It's bad.<br>It's terrible!<br>I haven't played Standard since <i>Worldwake</i> released.<br></div>&#10;                          <div>&#10;                            &#10;                          </div>&#10;                          <div></div>&#10;                        </div>&#10;                      </td>&#10;                    </tr>&#10;                  </tbody></table>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

* * *

[![](https://i.ormos.uk/5e/32/5e3290dee782c9ac8ca5a482206365d0efc643773751b5072579572723f1f8d4.jpg)](/en/events/2009/gameday-facts/world-wide-game-day)