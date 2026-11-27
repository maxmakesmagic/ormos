---
id: b9n5102h
kind: article
lang: en
path: /en/articles/latestdevelopments/2006/04-14-clouds-in-the-forecast
title: Clouds in the Forecast
published: '2006-04-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    lang_detected: en
    capture_id: 719677
    url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    captured_at: '2022-07-03 00:39:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    lang_detected: en
    capture_id: 719677
    url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    captured_at: '2022-07-03 00:39:58+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    lang_detected: en
    capture_id: 719677
    url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    captured_at: '2022-07-03 00:39:58+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    lang_detected: en
    capture_id: 719677
    url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
    captured_at: '2022-07-03 00:39:58+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: b9n5102h
  url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
  lang: en
  template: drupal
  captured_at: '2022-07-03 00:39:58+00'
  capture_id: 719677
  wayback_url: https://web.archive.org/web/20220703003958id_/https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14-0
- document_id: b9n5102h
  url: https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14
  lang: en
  template: drupal
  captured_at: '2022-05-25 12:10:44+00'
  capture_id: 719673
  wayback_url: https://web.archive.org/web/20220525121044id_/https://magic.wizards.com/en/articles/archive/latest-developments/clouds-forecast-2006-04-14
- document_id: b9n5102h
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af114
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af114
  lang: en
  template: aspx
  captured_at: '2013-07-07 02:16:38+00'
  capture_id: 778017
  wayback_url: https://web.archive.org/web/20130707021638id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af114
- document_id: b9n5102h
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af114
  page_key: wizards.com/default.asp?x=mtgcom/daily/af114
  lang: en
  template: classic_asp
  captured_at: '2008-04-28 20:05:07+00'
  capture_id: 1926059
  wayback_url: https://web.archive.org/web/20080428200507id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af114
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: b9n5102h
  capture_id: 778017
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af114
  wayback_url: https://web.archive.org/web/20130707021638id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af114
  captured_at: '2013-07-07 02:16:38+00'
  template: aspx
  sha256: 805ad6c890cf2877b831c8ce5775471ee5b43ae3d80b119355e68fd4642b0ef1
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Stalking Stones
  - Capsize
  - Boomerang
  - Awakening
  occurrences: 10
---
We are now entering a period of extreme awkwardness for me. You see, I write the development articles here on **magicthegathering.com**. I'm a decent fit for this role because I usually do some amount of development and/or playtesting of every set we make, and if I wasn't part of a particular development conversation, I usually get the full download from Randy Buehler or Brian Schneider or Devin Low so that I can regurgitate the important bits here.

But for *Dissension*, I was the lead designer—the role you all usually associate with Mark Rosewater. (In fact, Mark did more development on this set than I did. Go figure.) I made and/or supervised the making of most of the cards in the set, and then handed them off to the development team to do what they pleased. To my great relief, Matt Place and the other developers did their best to adhere to what we laid down in design, deviating only where necessary.

For the next couple of months, I'll be doing my best to play the developer role, although my viewpoints will probably be a bit stilted towards those of design.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <img src="https://i.ormos.uk/30/fc/30fcd9226ce07641ece264db8e3e3cd7cc4016165c0bd436772c6f3d45d757e4.jpg">&#10;      <br>&#10;      <i>Brian Schneider, Matt Place, and Aaron Forsythe at PT Honolulu.</i>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

So who developed the set? This was Matt Place's first team lead as a developer. I put him on the spot on the day I handed the set over, asking him, “Are you ready to tell me I made my cards wrong?” He made some great improvements to the set, and I was very happy with his willingness to ask my opinion on various approaches he and his team were thinking about taking. Brian Schneider, **Magic's** lead developer, was on the team as well to keep Matt on the straight-and-narrow. Brian tends to be on most (not quite all) development teams these days, and the well-balanced state of today's Standard environment is testament to how good Brian is at his job. 

Mark Rosewater was the design rep to the team—he's actually done more development work than most people realize. Mark is a great addition to dev teams as his design skills let him come up with innovative solutions quickly. The fourth member of the team was Steve Warner, making his debut on **Magic** teams. Steve worked for years here in Customer Service where he accumulated a great deal of understanding of not only the rules and intricacies of just about every game we make, but also the ins-and-outs of our players through the filter of the questions and concerns they voiced to him via email or over the phone. When a full-time playtesting position opened here in R&D, we snapped up Steve, and he has been a valuable contributor to many other games as well as **Magic**.

### And Now for Something Completely Different…

Enough with the intros… let's see a card!

![](https://i.ormos.uk/ad/33/ad33883be37807be41c1466920b627595373fa37ad25963b24afcba39bacb278.jpg) 

There, my friends, is the Azorius keyword in all its glory—forecast. How does it work? From the forthcoming *Dissension* FAQ:

> Forecast is an activated ability you can play only from your hand. Only cards from the Azorius guild (white, blue, or white-blue) have forecast.
> 
> The official rules for the forecast ability are as follows:
> 
> 502.53. Forecast
> 
> 502.53a A forecast ability is a special kind of activated ability that can be played only from a player's hand. It's written "Forecast — \[Activated ability\]."
> 
> 502.53b A forecast ability may be played only during its controller's upkeep step and only once each turn. The controller of the forecast ability reveals the card with that ability from his or her hand as the ability is played. That player plays with that card revealed in his or her hand until the upkeep step ends or until it leaves the player's hand, whichever comes first.
> 
> \* Playing a forecast ability doesn't cause the card it's on to leave its owner's hand.
> 
> \* Unless the card the forecast ability is on leaves its owner's hand, that card remains continuously revealed from the time the ability is announced until that upkeep step ends.
> 
> \* When a card that's been revealed to play a forecast ability leaves its owner's hand, it stops being revealed. If that happens before the forecast ability resolves, it will resolve as normal.
> 
> \* A player may play the forecast ability of any number of cards during his or her upkeep. However, the forecast ability of any card in that player's hand may be played a maximum of once during that upkeep.
> 
> \* If a player plays a card's forecast ability, then that card leaves that player's hand, then that card is returned to that player's hand, all during the same upkeep, the card is considered a new object. The player may play that card's forecast ability again during that upkeep.

In simpler terms, each forecast card has an ability you can play once per turn during your upkeep by revealing it from your hand and paying a cost. It's like each card has its own buyback spell built right in!

### The Ability That Almost Wasn't

![](https://i.ormos.uk/40/50/40505198c443702126d37a42eb1d19fd6e7a5294bd499883434a787159a6dee0.jpg)

Design really liked forecast (initially called “brainwave”) because it really fit the Azorius model of “action through inaction”—in other words, the White/Blue guild could affect the game without actually spending any of its cards. We can all envision the stereotypical White-Blue control player sitting smugly behind a full grip, and that's the feel we wanted to capture with the mechanic.

We didn't want to make things too easy, however. If there's one thing narrow-minded control players don't want to do, it's commit. Ideally they'll never tap a mana on their own turns, instead staying reactive and doing everything at the last minute. I can remember playing against some of Randy Buehler's more famous Blue decks from back in the day, and he could actually win without ever tapping a land for mana on his own turn; he just countered everything and then eventually activated Stalking Stones and won.

Yuck.

While we were fully willing to give Azorius good tools to play the control role, no one working on the set (either in design or development) had any desire to return to the days of “Draw-Go” style **Magic**. So if you want to forecast something, you'll have to commit some of your mana on your own turn. Now each decision is crucial, and better players will learn when the right time to forecast something is and when it's better to hold back.

Even with all these constraints (which were all set up in design), development still had huge concerns about the mechanic. It had two big problems—one, it basically couldn't be stopped short of discard (you can't counterspell a forecast effect), and two, if they're too powerful, they lead to repetitive games wherein nothing either player draws matters much as one player will simply forecast over and over again until the game ends.

The card developers liked pointing to as evidence against forecast was Capsize, which was a buyback Boomerang from *Tempest*. Capsize was a powerful card that elicits strong emotions of both love and hate from our players.

![](https://i.ormos.uk/61/7f/617fa4c43fd01851f7eddb206b21e7896c88a75714699eef7b9d309c4a487f1b.jpg)

People that like powerful effects, annoying their opponents, and winning, all love Capsize. Once the Capsize player hits six mana, assuming he's winning, it's pretty clear how the game is going to play out. Bounce your thing. Bounce your thing. Bounce your thing. Great.

People that are just playing the game for fun really don't like cards like Capsize, and tend to avoid them. I've been on both sides of that fence—playing in *Tempest* block PTQs, where the goal was to win, I had no problem putting Awakening into play and removing my opponent's entire board from the table. But in fun games in my apartment, my roommates and I usually cajoled each other until we took the Capsizes out of our decks.

As you can imagine, the development team didn't want a set full of Capsizes, especially uncounterable ones. The team even went so far as to ask us if we had any other White/Blue mechanics in reserve. Rosewater leapt to defend forecast, based almost solely on how well it tied into the flavor of the Azorius. I defended it is well, claiming that balancing the cards such that they were useful and fun to play without being oppressive and dominant wasn't as hard as it seemed.

In the end we reached a compromise, making forecast the smallest mechanic in the block (a mere nine cards). But that handful of cards really shows off the breadth of the mechanic.

As for the card I previewed specifically—I love Pride of the Clouds. Not only can it be the win condition in a slow control deck—imagine a Vitu-Ghazi that makes fliers and isn't actually in play—but it is a sick turn-two play in a deck full of fliers. Hooray for cards that fill more than one role!

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> Which <i>Dissension</i> guild are you most looking forward to?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Simic</td>&#10;    <td>6139</td>&#10;    <td>36.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Rakdos</td>&#10;    <td>5843</td>&#10;    <td>34.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Azorius</td>&#10;    <td>4910</td>&#10;    <td>29.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>16892</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

My personal favorite? Rakdos! I enjoy reckless play, and it's nice to have cards that allow that to be a good strategy.

### This Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>Have you played with <i>Visions</i> on <i><b>Magic</b> Online</i>?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtgcom_Forsythe_2006Apr14_visions">&#10;                    <div>&#10;                      &#10;                      Yes<br>Not yet<br>I don't play Online<br></div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>