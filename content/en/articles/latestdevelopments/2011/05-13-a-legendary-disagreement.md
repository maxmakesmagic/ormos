---
id: 25ja80f1
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/05-13-a-legendary-disagreement
title: A Legendary Disagreement
published: '2011-05-13'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    lang_detected: en
    capture_id: 726527
    url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    captured_at: '2022-09-30 06:02:30+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    lang_detected: en
    capture_id: 726527
    url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    captured_at: '2022-09-30 06:02:30+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    lang_detected: en
    capture_id: 726527
    url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    captured_at: '2022-09-30 06:02:30+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    lang_detected: en
    capture_id: 726527
    url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
    captured_at: '2022-09-30 06:02:30+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 25ja80f1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
  lang: en
  template: drupal
  captured_at: '2022-09-30 06:02:30+00'
  capture_id: 726527
  wayback_url: https://web.archive.org/web/20220930060230id_/https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-13
- document_id: 25ja80f1
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/142
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/142
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:31:34+00'
  capture_id: 613219
  wayback_url: https://web.archive.org/web/20130706053134id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/142
- document_id: 25ja80f1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-12
  page_key: magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-12
  lang: en
  template: drupal
  captured_at: '2021-10-25 00:03:39+00'
  capture_id: 726519
  wayback_url: https://web.archive.org/web/20211025000339id_/https://magic.wizards.com/en/articles/archive/latest-developments/legendary-disagreement-2011-05-12
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 25ja80f1
  capture_id: 613219
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/142
  wayback_url: https://web.archive.org/web/20130706053134id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/142
  captured_at: '2013-07-06 05:31:34+00'
  template: aspx
  sha256: 16f2221d8dc3a44c6e6b220c51517810ca2b1d8bb0c5f54c012a294ef0615d67
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Isamaru, Hound of Konda
  - Plains
  - Isamaru
  - Darksteel Forge
  - Mycosynth Lattice
  - Doom Blade
  - Leatherback Baloth
  - Umezawa's Jitte
  - Meloku the Clouded Mirror
  - Melira, Sylvok Outcast
  - Green Sun's Zenith
  - Jace, the Mind Sculptor
  - Jace Beleren
  - Accumulated Knowledge
  - Koth of the Hammer
  - Garruk Wildspeaker
  - Elesh Norn, Grand Cenobite
  - Jin-Gitaxias, Core Augur
  - Sheoldred, Whispering One
  - Urabrask the Hidden
  - Vorinclex, Voice of Hunger
  occurrences: 24
---
Earlier this week, Mark Rosewater [wrote about](/en/articles/makingmagic/2011/05-09-the-issue-is-legenwait-for-itdary) the rules for legendary permanents, explaining that **Magic** R&D was unhappy with them. Although we often present ourselves on this website as a monolithic entity, that perception is far from accurate. **Magic** R&D is a group of intelligent humans with strong opinions. As you might expect, we don't often agree on anything. Any time you read that "**Magic** R&D thinks \[whatever\]," there's probably at least one person who disagrees with it.

In this case, I am one such person.

I will not claim to speak for anyone else. However, I'm a **Magic** developer, and I like the current legendary permanent rule.

For the benefit of those who haven't been around for a while, I'll recap the previous and current incarnations of the legend rule. Let's suppose I control an Isamaru, Hound of Konda. You tap a Plains and cast your own copy of Isamaru. Under the previous "legend rule," the game would see that there were multiple Legends with the same name in play and that your copy was more recent than mine, so it would put your copy into the graveyard and leave mine in play. Under the current "legend rule," the game sees that there are two legendary permanents on the battlefield with the same name, then puts them both into the graveyard.

![](https://i.ormos.uk/13/16/1316400a07b31cc35524c6f763ce377180e98718985da30de1081624cb222ecf.jpg) 

  

One thing Mark didn't mention was that the rules for legendary permanents with the same name and planeswalkers with the same subtype are nearly identical, so almost anything that can be said about legendary permanents can also be said about planeswalkers. I like both rules, and I'll discuss them together.

![](https://i.ormos.uk/30/d3/30d35a37f6d6679b4d939339e439280454e20ebf1f835f4ca3d2d6b30c405dea.jpg) 

  

As I said before, there are many things I like about these rules, so I'm reluctant to change them. If you want me to support Mark's case, your new suggested rule should keep as many of the positive attributes I list here as possible.

**The legendary permanent and planeswalker uniqueness rules work the same.** 

Simple rules offer tons of benefits to games. Players can only keep so many things in their heads at once, and there's no sense adding complexity to a game in rules governing rare corner cases that won't add a lot of fun value to the game overall.

Planeswalkers and legendary permanents aren't the same things, but they feel very similar from a standpoint of flavor and player expectations. Therefore, it's great that they both work the same, as that saves explanation time and gainless complexity.

**The legendary permanent and planeswalker rules are interactive.** 

Mark made the claim that the current legendary rules do not allow for interaction. It may be true that they preclude interaction between cards, but they do force players to interact with each other.

![](https://i.ormos.uk/87/5b/875b03536411bd75556d5505d72bef561110fd6ae4aba5d766f9bd5306e89ce7.png) 

  

In **Magic**, some card interactions are positive, like Darksteel Forge combined with Mycosynth Lattice. Others are destructive, like when Doom Blade kills a Leatherback Baloth. While positive interaction is good, there can only be so much positive interaction on the table before the board gets too complicated to process. The legend rule is a source of destructive interaction, and I have no problem with that. I'm not tied to these rules causing destructive interactions, but I like that they cause some kind of interaction between players.

**Legendary permanents and planeswalkers need answers too.** 

Many legendary permanents are very powerful cards. Developers like it when there are answers to powerful cards, and from my perspective, a card being its own solution is one of the more elegant ways to provide answers.

Many legendary permanents are very powerful cards. Kamigawa block was full of them, and after having played several high-level Kamigawa Block Constructed tournaments, I am confident that I would have had much less fun if all the legendary cards in those sets had not annihilated each other. In particular, I can't imagine enjoying a game of **Magic** while both players controlled their own copies of Umezawa's Jitte or Meloku the Clouded Mirror.

![](https://i.ormos.uk/77/be/77be075b7ef2c27a68a89d15d951b1697ea7ce37f068f459c3a5ed8c741eef84.jpg) 

  

This kind of effect continues to crop up and do good things. Yet another of them cropped up during *Scars of Mirrodin* Block Constructed playtesting, when Melira, Sylvok Outcast became important in sideboarded games between Mono-Green Infect decks. While posturing battles between Green Sun's Zenith and Melira weren't the most fun **Magic** we had ever played, it was far better than having the first person to stick a Melira win, or allowing a Melira on both sides of the table.

![](https://i.ormos.uk/52/68/5268cb734437bd02e0eb9ea8a0f64a5707d13d14cfc2164f0feeb98e2eb57aa5.png) 

  

**The rules don't punish you for playing your planeswalker or legendary permanent first.** 

My favorite thing about the current legendary permanent and planeswalker uniqueness rules is that they incentivize you to play your legendary permanent before your opponent plays a copy of the same card. If your legendary creature comes down second, you get none of the value that the card could give you from being on the battlefield. If you were first, though, you are advantaged. If the card in question has no abilities, you get to have the strategic initiative, which is always good. If it has an activated ability, has haste, or has some other way to take advantage of it other than attack and block, you often get value out of your card, while your opponent doesn't. This is even more extreme in the case of planeswalkers, when you are sure to get at least one activation out of your copy before your opponent can cast one of his or her own.

Although Jace, the Mind Sculptor is more powerful than we intended, the planeswalker rule has done interesting things to the construction of blue decks. At three mana, Jace Beleren comes down before Jace, the Mind Sculptor does. Therefore, many decks that want to win Jace fights have supplemented their Mind Sculptors with Belerens. This had the dual effect of giving compelling options to people who want to win Jace fights and making decks that try to win those fights worse against extremely aggressive decks that can win before card advantage from Jace matters too much. That's a healthy kind of metagame cycle, and I was glad to see it happen.

![](https://i.ormos.uk/e4/56/e4562c109df3bca4eb9688b0c3adab4169649f72ba04840befc370d4a2f28b74.jpg) 

  

I read someone pitch the idea that a new legendary permanent could destroy every other instance of that card in play. That idea fails this test. If we both have four copies of Umezawa's Jitte in our deck, under that rule the correct play may be for neither of us to play a copy of it first, as keeping one in play may be the only thing that matters. This kind of effect has existed before in Accumulated Knowledge mirror matches, and it is no fun at all. Usually, whoever blinks and does something first loses, and that is not the right lesson for **Magic** to teach.

Playing your cards as soon as you can is more fun than waiting, and it's better when the more fun thing is correct more often. Any replacement rule needs to preserve the general correctness of playing out your legendary cards first.

**There are plausible flavor explanations.** 

**Magic** is a game built around high fantasy. While there are elements of the game, such as mulliganing, that have no basis in flavor, the great majority of the rules are consistent with the game's creative conceits.

![](https://i.ormos.uk/a0/ff/a0ffe8827510db0e8d095ca565830461a83cbe8ebbd6f1a3fb38d8bf8d9d11de.jpg) 

  

Planeswalker and legendary permanent cards represent unique things in the multiverse. There's only one Koth of the Hammer, and there's only one Umezawa's Jitte. It would be fourth-wall-breaking to allow both players to control their own copy of either at the same time. Therefore, the rules must prevent this. They must also figure out what to do when this is in danger of happening.

The previous version of the legend rule simply put the most recent one into the graveyard, which makes fine flavor sense. Under that model, it's impossible to summon a legend from the æther while said legend is standing right over there.

The new model, however, also has reasonable explanations. My favorite explanation for legendary creatures is that the spell reaches into the æther looking for the creature; if it can't find it, it reaches further out to find it, but it can only pull it back so far. The end effect is to leave the creature somewhere in limbo. My favorite explanation for planeswalkers is simpler. The price in mana that I must pay to get Garruk Wildspeaker to hang out with me is set, but that same price is enough to get him to leave me in the lurch. Garruk is a pragmatic guy; if my opponent pays him off, then he's happy to get out of there.

![](https://i.ormos.uk/8a/ef/8aefea45501ed2374f4fbc5dc215c3120d1328bc6a02fa6afc7328624ce89443.jpg) 

  

I have heard other plausible flavor explanations of what happens when legendary permanents and planeswalkers annihilate each other. I didn't mind any of them. These are my favorite, but if you don't like them, I'm guessing you can come up with ones you like better. Whatever new rule you propose needs to be equally explainable with flavor.

* * *

  

While both Design and Development want **Magic** to be as awesome as possible, they often have different priorities. Sometimes, we don't get along, and compromises must be made. If the current legendary permanent and planeswalker rules were the result of a compromise, it's a compromise I'm glad we made. As always, I am happy to consider alternatives, but not if they sacrifice too many of the positive aspects I've listed here.

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> Are you attending, or have you attended, a <i>New Phyrexia</i> Prerelease event this weekend?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, at a local store.</td>&#10;    <td>952</td>&#10;    <td>54.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, at a large regional prerelease.</td>&#10;    <td>143</td>&#10;    <td>8.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, both kinds.</td>&#10;    <td>48</td>&#10;    <td>2.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>No.</td>&#10;    <td>592</td>&#10;    <td>34.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>1735</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### This Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>Which of the five Praetors is your favorite?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtg_daily_ld_142_poll1">&#10;                    <div>&#10;                      &#10;                      &#10;                      <a>Elesh Norn, Grand Cenobite</a>&#10;                      <br>&#10;                      &#10;                      &#10;                      <a>Jin-Gitaxias, Core Augur</a>&#10;                      <br>&#10;                      &#10;                      &#10;                      <a>Sheoldred, Whispering One</a>&#10;                      <br>&#10;                      &#10;                      &#10;                      <a>Urabrask the Hidden</a>&#10;                      <br>&#10;                      &#10;                      &#10;                      <a>Vorinclex, Voice of Hunger</a>&#10;                      <br>&#10;                      &#10;                      &#10;                    </div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>