---
id: 6yk6w879
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/12-25-the-yang-of-timmy
title: The Yang of Timmy
published: '2009-12-25'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    lang_detected: en
    capture_id: 736338
    url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    captured_at: '2022-08-13 22:47:03+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    lang_detected: en
    capture_id: 736338
    url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    captured_at: '2022-08-13 22:47:03+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    lang_detected: en
    capture_id: 736338
    url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    captured_at: '2022-08-13 22:47:03+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    lang_detected: en
    capture_id: 736338
    url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
    captured_at: '2022-08-13 22:47:03+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 6yk6w879
  url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
  lang: en
  template: drupal
  captured_at: '2022-08-13 22:47:03+00'
  capture_id: 736338
  wayback_url: https://web.archive.org/web/20220813224703id_/https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-14
- document_id: 6yk6w879
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/70
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/70
  lang: en
  template: aspx
  captured_at: '2013-07-06 17:28:29+00'
  capture_id: 623508
  wayback_url: https://web.archive.org/web/20130706172829id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/70
- document_id: 6yk6w879
  url: https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25
  lang: en
  template: drupal
  captured_at: '2022-08-08 21:54:10+00'
  capture_id: 736340
  wayback_url: https://web.archive.org/web/20220808215410id_/https://magic.wizards.com/en/articles/archive/latest-developments/yang-timmy-2009-12-25
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 6yk6w879
  capture_id: 623508
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/70
  wayback_url: https://web.archive.org/web/20130706172829id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/70
  captured_at: '2013-07-06 17:28:29+00'
  template: aspx
  sha256: fc283bdcd3bdde92607b8f0a2cba52669d1f1c51bbb412e1387a121805255d85
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Progenitus
  - Congregate
  - Hit // Run
  - Faerie Macabre
  - Cryptic Command
  - Millstone
  - Glimpse the Unthinkable
  - Haunting Echoes
  - Noble Benefactor
  - Lobotomy
  occurrences: 20
---
*Many **Magic** players have an image of Timmy as an excitable person who loves enormous creatures. While those people fall into the Timmy category, not all Timmies look like that. Timmies want their games to take them on emotional rides, but not all Timmies want the same ride, and some Timmies even want to engineer an unpleasant ride to take their opponents on. "The Yang of Timmy" talks about "griefers," which is a word many gaming communities use to describe exactly that kind of player.* 

* * *

*This article originally ran on March 13, 2009.* 

* * *

By this point in Timmy Week, Timmy himself needs little introduction. Mark Rosewater talked about [designing for Timmy](/en/articles/makingmagic/2009/03-09-designing-for-timmy) on Monday and Kelly set out [a manifesto for Timmy](/en/articles/seriousfun/2009/03-10-the-timmy-manifesto) on Tuesday. You might think that now you know everything there is to know about Timmy, but he also has a dark side that no one else this week has been willing to expose. Today I'll talk about how we develop for the four subtypes of Timmies that Kelly talked about on Tuesday, then I'll talk about a different and more sinister kind of Timmy that you might not have thought of as a Timmy before.

### Power Gamers

I don't think I can top Kelly's description of power gamers from his Tuesday article: "Power gamers are all about huge plays and giant monsters. They want the biggest, the dumbest, the craziest, and the coolest. They want dragons. They want Ultimatums. They want three planeswalker ultimates to go off in one turn." **Magic** developers are very good at identifying power level, and we have detailed metrics that we use to evaluate card power both in Limited and Constructed. However, it's much more difficult to measure how much raw excitement cards create.

![](https://i.ormos.uk/88/3a/883aeec3638a8f16702de476ac22553405201ce0dd632bc512d58e466d2631b4.jpg) 

  

To get a picture of how exciting cards are, we use a tool that we uncreatively call "the rare poll." Early in each set's development, we send employees from all over the company a poll that asks them to rate all the rares and mythic rares in that set on a scale from 1 to 10. That data gives us a much better picture of what cards tickle people's inner Timmy. When a card that we thought would be exciting does well on the poll, we protect it. When such a card does poorly instead, we tweak it to make it more appealing to that audience.

![](https://i.ormos.uk/87/e8/87e8520f811f86ae270c414efde55b37937074804a62e7f67a38036976edc74e.jpg)

One card that benefited from the rare poll is Progenitus. There was a point in *Conflux* development where some people thought that it should not be a 10/10. The card was already insane enough, they argued, because of the line "protection from everything," and did not need to kill in two hits. *Conflux* lead developer Mike Turian knew that the card was a top 10 finisher in the rare poll and knew that the card had very little danger of being a power level problem for tournament **Magic**, so he let it go as a 10/10 to make sure that it read as the most ridiculous possible card.

### Social Gamers

Social gamers are people who use **Magic** mainly as a social outlet. They tend to play multiplayer formats that involve lots of people and their primary goal is for everyone to have fun. It's hard for us to develop for social gamers, largely because they are perfectly willing to develop for themselves by making house rules banning particular things. You might find a group of social gamers who despise time-consuming search effects, mass land destruction, or Congregate, and just outright ban the offending card or cards. Those players do a better job of developing for themselves than we ever could.

The biggest thing that we do as developers for social gamers is to give cards extra functionality in multiplayer when we can do that without making the card more complicated than we would like. For example, Hit // Run gained the ability to key off of a teammate's creatures, Faerie Macabre lets you remove one card each from two different graveyards, and Cryptic Command taps creatures controlled by all your opponents. Another example of a card that gained from this is Silence from [***Magic** 2010*](/en/articles/feature/2009/02-23-recapturing-the-magic-with-magic-2010), which stops all your opponents from playing spells.

![](https://i.ormos.uk/31/c1/31c194083233ea140dc817cd31eac0bed04e895f9da85bf49d6d2663f4825a4f.jpg) 

  

### Diversity Gamers

Diversity gamers are players who want **Magic** to be a new experience every time they play it. They need constant change to stay interested. We serve diversity gamers by making sure that **Magic** offers plenty of different things to do. We try to make each set pull players in different directions, so over time diversity gamers will naturally experience many different things. They will also find that each set's different themes can be taken in different directions. For example, some of the Merfolk in *Lorwyn* and *Morningtide* gave players tools to mill their opponent with, but they also supported a simpler beatdown merfolk deck. This allows players who value diversity to build different kinds of decks within the same block theme.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Drowner of Secrets" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Drowner%20of%20Secrets&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Streambed Aquitects" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Streambed%20Aquitects&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

### Adrenalin Gamers

Adrenalin gamers are people who enjoy tense situations that have very high variance. It's lots of fun for them to wait in suspense while they find out whether or not something awesome happened. We develop for adrenalin gamers by making sure that we protect exciting cards that produce those kinds of games. One great example of this category of card is Capricious Efreet from ***Magic** 2010*, which Aaron Forsythe previewed when he [announced that set](/en/articles/feature/2009/02-23-recapturing-the-magic-with-magic-2010). At one point its text box looked like this:

> At the beginning of your upkeep, choose target permanent you control and up to two target permanents you don't control. Destroy one of them at random.

**Magic** designer and ***Magic** 2010* development team member Greg Marques noticed that the obvious use of this card is to target one of your own lands and two of your opponent's nonlands. Most of the time you'll kill one of your opponent's permanents, and some of the time you'll kill your own land. Greg complained that this was hardly a moment of tension at all, and that the card wasn't very fun for this kind of Timmy because there was no real way anything could go wrong. We added "nonland" to the card to increase the tension, and Greg and other adrenalin Timmies like him became much happier.

![](https://i.ormos.uk/c3/6a/c36af9f4ace0843def0fe2b16028f8f9dc1a63f1da97c87e262207b0c4e98cd0.jpg) 

  

That's all I have to say about the kinds of Timmies you've met so far this week. Now it's time to introduce you to a kind of Timmy that you may not have thought of as a Timmy before.

### Griefer Timmies

![](https://i.ormos.uk/f5/7a/f57add1ba1cf4cd9a5c2247f76b13bca2ced8269ad8814d6fdebb0953ec7e79a.jpg)

Just like other Timmies, "griefers"—a term that comes from online games—are looking to experience something. Unlike other Timmies, however, the experience that the griefers want is the experience of their opponents squirming in misery. They are at their very happiest when their opponents are miserable. Griefers cackle with glee when they hit your best card with a Millstone, and they feel deeply cheated when an opponent who has no permanents concedes even though the griefer has no plans to actually win anytime soon. His goal is to make you sad, and he gets a kick out of your sadness.

One classic griefer strategy is land destruction. The dream there is that the opponent will be stuck staring wistfully at a hand full of cards that he can't play. Another strategy that griefer Timmies I grew up with loved was counterspells. Some Magic players use counterspells to stop threats that they can't deal with otherwise, but griefer Timmy is excited about counterspells because he can use them to stop every card his opopnent ever plays in an entire game. Timmy doesn't play eight counterspells; he plays plays twenty-eight of them. The joy of those strategies isn't that they are powerful or lead to winning the game. It is only that the opponent can't do what he wants to, and a sad opponent makes for a happy griefer.

![](https://i.ormos.uk/28/97/28977d1cfd48eaaba44457e97ad0be994e999aea2eaa4171ee5bc394efe975dc.jpg) 

  

We are not afraid to print individual cards for griefer Timmy. Two classic examples of these cards are Glimpse the Unthinkable and Haunting Echoes. Griefer Timmy loves milling because everyone gets to see the fun and exciting cards that his opponent won't play this game, and ten cards milled for only two mana is awesome. Haunting Echoes is somewhat similar in that it gives griefer Timmy the chance to take away his opponent's cards in a very public way. However, a player whose graveyard is full when they get hit by a Haunting Echoes must play the rest of the game with a deck largely devoid of action spells, which is demoralizing and annoying. That's exactly what griefer Timmy wants out of a card.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Glimpse the Unthinkable" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Glimpse%20the%20Unthinkable&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Haunting Echoes" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Haunting%20Echoes&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

Griefer Timmy doesn't need his cards to be powerful as long as they are sufficiently annoying. One classic combination that griefer Timmy loves is Noble Benefactor and Lobotomy. Everyone is happy when Noble Benefactor lets everyone get their favorite card, but griefer Timmy isn't interested in getting an awesome card of his own. Instead, he wants you to tell him what your favorite card in your deck is, then rip that card out of your deck entirely with Lobotomy. This is a lot of work to go through for something that isn't particularly powerful, but griefer Timmy is happy to do it as long as it makes you sad.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Noble Benefactor" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Noble%20Benefactor&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Lobotomy" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Lobotomy&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

In some ways, from our perspective the ideal card for griefer Timmy is one that he thinks annoys his opponents a lot but actually doesn't annoy them too much. Those cards allow griefer Timmy to be happy because he gets to mess with other people, but don't hurt other players' experiences excessively. On the other hand, it is important for griefer Timmy that he feels like his efforts reward him with his opponents' misery, so we have to make sure that he does manage to annoy his opponents some of the time.

![](https://i.ormos.uk/db/6b/db6b4628c8a640c3d9a865de285f79d1a57b7db231860e25e3b8fe9f4a1c2c38.jpg)

Sometimes people who work on **Magic** fight to kill cards that enable griefing. Extremely annoying cards sometimes don't survive, but other times those people's efforts are thwarted because we want to make griefer Timmies happy too. One instance of this from ***Magic** 2010* is Silence, another one of the cards that Aaron Forsythe previewed in his announcement. Former Building on a Budget author and R&D member Nate Heiss argued that the card was a very bad thing to print because it was both miserable and powerful in tournament constructed, and he built tons decks that included it. He would then play them against various people to try to prove his point.

Nate's decks tended to include a bunch of little creatures, some removal spells, and Silences. He would curve out with some creatures and then Silence his opponent during upkeep when he thought his opponent might cast a spell. He would then try to convince his opponents that they were annoyed, but mostly they would just draw their card, play a land, and then wait a turn to play their spells. Sometimes, his opponents even had the audacity to respond to his Silences with instant removal spells, in which case the Silence didn't hurt them very much at all. Other times, both Nate and his opponent would create a creature stall, and when he drew a Silence in that situation he was effectively down a card. 

In the end, Nate's efforts did not stop the card, and ironically convinced the ***Magic** 2010* development team that the card was a great idea to print. He showed us that Silence wasn't going to be too powerful when used merely to grief people and that Silence would make people who enjoyed griefing very excited. Nate never really came around to this view, but the card made it out the door intact. 

This story is beautiful to me because even though Nate was griefing us relentlessly, he wasn't doing it because he enjoyed it. Instead, he was doing it because he thought it was his responsibility to keep everyone else from doing it. In the process, however, he became exactly the thing that he hated. When the **Magic** web team heard this story, they dubbed Nate "the Rorschach of griefing," which is hilarious and awesome.

![](https://i.ormos.uk/21/72/2172ac391b73717f53ace4e1ee5152c0ecd80be4e4e462b6c32dfe9ce3620b63.jpg) 

  

Even though griefer Timmy's goal is to make you sad, there is an effective way to deal with him. Simply refuse to be sad in the face of his tricks, and you will deny him his fun. Even more devastating, you can beat him while ignoring his efforts to annoy you. A griefer Timmy who neither wins the game nor makes his opponent miserable is a very sad griefer Timmy indeed. However, be very careful when you do this. If you enjoy a griefer Timmy's misery too much, you will become intimately familiar with the fun that a griefer Timmy can have and you might be tempted to become one yourself!

We've come to the end of Timmy week. If you are a Timmy, be proud of the big creatures and swingy moments you love. If not, be respectful of them now that you know what makes Timmy tick, and we'll have weeks devoted to your psychographic later this year.

### Last Week's Polls

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>How many Pro Tour Qualifier tournaments have you played in?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>0</td>&#10;    <td>2446</td>&#10;    <td>57.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>1</td>&#10;    <td>479</td>&#10;    <td>11.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>2 or 3</td>&#10;    <td>471</td>&#10;    <td>11.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>4, 5, or 6</td>&#10;    <td>276</td>&#10;    <td>6.5%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>7, 8, 9, or 10</td>&#10;    <td>157</td>&#10;    <td>3.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>11 or more</td>&#10;    <td>419</td>&#10;    <td>9.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>4248</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

My intention for this poll was only to learn how many of my readers have actually played in [Pro Tour Qualifier](/en/articles/event-coverage/undated/magic-the-gathering-pro-tour-qualifiers-2) tournaments. I understand that competitive **Magic** is not for everyone. I also knew that last week I would be talking about the Pro Tour, so it seemed appropriate to ask how much of my audience had tried to qualify for one.

I was glad to see that people who had played in qualifiers seemed to do a good job of figuring out whether the qualifier scene was for them. The majority of players who had played in a qualifier either stopped after three or less or had continued on to play seven or more. We try to have diverse organized play offerings so that every player can find something they enjoy, and these results suggest that players who decided that qualifiers weren't fun for them found other arenas to play in rather than soldiering on in a world they didn't like. We couldn't be happier about that, and all we want for you is that you are having fun with **Magic** however you choose to play it.

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>Did you follow the coverage of last weekend’s Pro Tour in Kyoto?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>I only read the text coverage.</td>&#10;    <td>1772</td>&#10;    <td>41.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I read the text coverage and watched the live webcast.</td>&#10;    <td>1348</td>&#10;    <td>31.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I didn't follow the coverage at all.</td>&#10;    <td>925</td>&#10;    <td>21.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I only watched the live webcast.</td>&#10;    <td>212</td>&#10;    <td>5.0%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>4257</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

I'm happy to see that many of you did watch at least some of the live webcast of [Pro Tour–Kyoto](/en/events/2009/ptkyo09/nassif-the-greater-power). I enjoy watching **Magic**, and there were some great games of **Magic** played on camera two weekends ago. In particular, [the Finals match](/en/events/2009/ptkyo09/finals-controlling-the-giant-2) between Luis Scott-Vargas and Gabriel Nassif will go down in history as one of the great Pro Tour Finals matches and I fully expect both of them to one day be in the Pro Tour Hall of Fame. I recently found out that I'll be attending [Pro Tour–Honolulu](/en/articles/event-coverage/undated/pro-tour) as part of the coverage team, and I hope to be able to watch some **Magic** that good in person!

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>How many multicolored cards do you think are in <i>Alara Reborn</i>?<br>      (The set contains 145 cards.)</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_70_poll1">&#10;                            <div>&#10;                              &#10;                              0<br>1<br>2-25<br>26-50<br>51-100<br>101-144<br>145<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>