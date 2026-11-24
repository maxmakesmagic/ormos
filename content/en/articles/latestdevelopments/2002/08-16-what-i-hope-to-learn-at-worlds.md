---
id: dmszz2rj
kind: article
lang: en
path: /en/articles/latestdevelopments/2002/08-16-what-i-hope-to-learn-at-worlds
title: What I Hope to Learn at Worlds
published: '2002-08-16'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    lang_detected: en
    capture_id: 735906
    url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    captured_at: '2022-01-18 18:01:34+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    lang_detected: en
    capture_id: 735906
    url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    captured_at: '2022-01-18 18:01:34+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    lang_detected: en
    capture_id: 735906
    url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    captured_at: '2022-01-18 18:01:34+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    lang_detected: en
    capture_id: 735906
    url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
    captured_at: '2022-01-18 18:01:34+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - mgvjsbbn
sources:
- document_id: dmszz2rj
  url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
  lang: en
  template: drupal
  captured_at: '2022-01-18 18:01:34+00'
  capture_id: 735906
  wayback_url: https://web.archive.org/web/20220118180134id_/https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
- document_id: mgvjsbbn
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb33
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb33
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:26:02+00'
  capture_id: 805246
  wayback_url: https://web.archive.org/web/20090604152602id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb33
- document_id: mgvjsbbn
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb33,,de
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb33
  lang: en
  template: classic_asp
  captured_at: '2005-03-02 23:31:33+00'
  capture_id: 1989049
  wayback_url: https://web.archive.org/web/20050302233133id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb33,,de
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: dmszz2rj
  capture_id: 735906
  url: https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
  wayback_url: https://web.archive.org/web/20220118180134id_/https://magic.wizards.com/en/articles/archive/latest-developments/what-i-hope-learn-worlds-2002-08-16
  captured_at: '2022-01-18 18:01:34+00'
  template: drupal
  sha256: bb07ef8fb8afe9e800bac595ca0eb253a175d6f7bca80158136792e3801e32c3
render_recovery: []
---
I'm away in Sydney, Australia, right now at the ninth annual **Magic: The Gathering** World Championships. I thought it might be interesting to talk about why I'm here and what I hope to learn--sort of a developer's-eye view of the event.

### An Autobiographical Digression

When Bill Rose offered me a job in Wizards R&D, I made one request before I accepted. I told him I wanted to stay in touch with the Pro Tour circuit. I knew they were hiring me in large part because they wanted developers who knew how to play at the highest level. (They needed high-quality "[Spikes](https://web.archive.org/web/20020816000000/https://magic.wizards.com/en/node/614566)" and that's what I was.) So it seemed natural that I should continue going to Pro Tour events just so that I could stay up to date on the latest deckbuilding technology. The fact that I'm a huge fan of the game and that I would get to spend those weekends hanging out with all my friends had nothing to do with it. (Yeah, that's the ticket.) Anyway, Bill agreed to send me at least to the U.S. Pro Tour events, and that was good enough for me--I accepted the job.

<table><tbody><tr><td><br><i>Randy Takes notes on a Pro TOur match between Brian Hacker and Scott Johns.</i></td>&#10;		</tr></tbody></table>

Once I got to Wizards I quickly found an even better way to get to all the Pro Tour events: *Sideboard* website (and magazine) reporting. Jeff Donais asked me if I was interested in writing reports for Pro Tour and Grand Prix events. He offered to send me to all the Pro Tours (even the international ones) and to however many Grand Prix I wanted to go to in exchange for a mere sixteen hours of slave labor each day of each event. I agreed immediately, and if you plow through *Sideboard* archives, you'll see a crazy number of Feature Match reports penned by yours truly--I'm told I hold the record. Since then, I've picked up an additional gig: I'm the play-by-play guy for Sunday Top 8 broadcasts. (This "distraction," along with growing responsibilities at work, makes it harder for me to find time for Grand Prix coverage. So Josh Bennett has started closing the gap on my Feature Match writing mark.)

Anyway, none of this explains why I should care about the Pro Tour circuit from a professional stance, but I've gotten a bunch of emails asking me how I got my job in R&D, so I figured a small autobiographical digression wasn't wholly inappropriate.

### The Real Reasons

When R&D begins developing a **Magic** set, we juggle quite a few goals. We know the game has many audiences (Timmy-Johnny-Spike is one reasonable audience breakdown), so we try to make sure that sets will be well-received by each. Of course "well-received" is, in itself, a juggling act because the set has to be good enough to be intriguing to players, but not so good that the environment becomes ridiculous.

<table><tbody><tr><td><br><i>Randy, and other pro players and Wizards employees, will often 'gunsling' against local players at big events.</i></td>&#10;		</tr></tbody></table>

A large chunk of **Magic** players can be usefully categorized as Spikes, or tournament-caliber players. Tournament players are significantly outnumbered by "casual" **Magic** players, but they do tend to spend more money (per person) than do casual players. (If you look at the total amount of money spent by each crowd, by the way, tournament players are still outweighed by casual players, but not by as much.) Thus, R&D cares a lot about appeasing tournament players, but not so much that we want to sacrifice anything about the game that makes it appealing to our other audiences.

Tournament players can be tough to take care of because once a set is released, players put in untold hours trying to break it. We in R&D simply don't have the resources to spend that much time playtesting each set, and if something broken does sneak through it can really mess up an environment. Most casual players won't hesitate to add "house rules" that ban whatever cards or strategies they don't enjoy, but for tournament play the pressure is squarely on R&D.

After releasing about a dozen cards (all in the Urza block) that were worthy of DCI banning, Wizards knew they needed more help taking care of Spike--so they looked to the Pro Tour. I was hired shortly after *Mercadian Masques* released, and Mike Donais came on board at about the same time. Within the next year or so, three other developers with Pro Tour experience were hired: Worth Wollpert, Brian Schneider, and Elaine Chase. I've always looked at it as just changing teams: I used to try to break cards after they came out; now I try to break them a year earlier. The only real difference is that I used to get rewarded with tournament prizes and a modicum of Internet fame. Now when I break a card, all that happens is that my toys get taken away (because the card gets changed).

Anyway, because Wizards hired me in part because of my Pro Tour experience, it's important to me to try to keep my skills as sharp as possible. That's one of the reasons I go to Pro Tour events. By watching pros play, I'm reminded of the best strategies and I get to learn any new ones. There's also no better way to learn which deck types are defining a Constructed environment than to talk to the top deckbuilders about the subject. It's also interesting to grade R&D's ability to manipulate the environment and predict what the good cards will be. Worlds, for example, will be my first big chance to see *Judgment* in action. I've read my fair share of Internet articles, but nothing teaches me more about the raw card power levels than watching the pros draft or watching a Pro Tour metagame take shape.

<table><tbody><tr><td><br><i>Two of the many cards that Randy will have his eye on at Worlds.</i></td>&#10;		</tr></tbody></table>

A lot of this is probably pretty obvious, but the interesting perspective that's important to keep in mind is that all these issues really apply to only one of our several audiences. I go to Pro Tours to remind myself how to take care of Spike, and the data I collect really speaks only to power-level issues. But there's a lot more to **Magic** than just Spike. Pro Tours don't teach me much about which cards are fun; Spikes just think winning is fun, and they'll play whatever they think will help them win one more round. Pro Tours also don't teach much about what's cool and/or just plain fun to think about.

All in all, the Pro Tour is a useful tool for me as a **Magic** developer. It's only one tool among many, but it does help me keep my own play skills sharp, and it helps increase my understanding of why some cards are better than others.

In particular, here are a few metagame issues I'll be keeping my eye on in Sydney:

*   Which *Judgment* cards are getting the most play?
*   Did we screw up when we trimmed that third mana off of [Quiet Speculation](https://web.archive.org/web/20020816000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quiet+Speculation)?
*   What are the best colors and cards in full *Odyssey* Block Booster Draft?
*   How interesting is the off-kilter color distribution of *Torment* and *Judgment* in draft?
*   Has the Standard metagame been able to react to [Upheaval](https://web.archive.org/web/20020816000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Upheaval)?
*   Are the [Cunning Wish](https://web.archive.org/web/20020816000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Cunning%2BWish) as interesting as we thought they would be?

And, of course, there are strictly fan concerns:

*   Will the U.S. national team rise to the challenge posed by Germany and the Netherlands?
*   Can Kai Budde become the first two-time world champion?
*   Which budding star will bust out and make a run at the title?
*   Who will qualify for the **Magic** Invitational?

(God, I love this game . . . and my job.)

If you want to check out things for yourself, visit [**sideboard.com**](https://web.archive.org/web/20020816000000/https://magic.wizards.com/en/articles/archive/event-coverage/3rd4th-place-playoff-rob-nadebaum-vs-daniel-clifton-2015-07-22) for live coverage of all five days of competition.

Here are the results of my last poll:

<table><thead><tr><th colspan="3"><b>How many colors do you like to play in your decks?</b></th>&#10;		</tr></thead><tbody><tr><td>One</td>&#10;			<td>1036</td>&#10;			<td>13.7%</td>&#10;		</tr><tr><td>Two</td>&#10;			<td>3956</td>&#10;			<td>52.4%</td>&#10;		</tr><tr><td>Three</td>&#10;			<td>1532</td>&#10;			<td>20.3%</td>&#10;		</tr><tr><td>Four</td>&#10;			<td>335</td>&#10;			<td>4.4%</td>&#10;		</tr><tr><td>Five</td>&#10;			<td>694</td>&#10;			<td>9.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7553</b></td>&#10;			<td><b>100%</b></td>&#10;		</tr></tbody></table>

"Two" was the overwhelming favorite, chosen by over half the respondents.

  
*Randy may be reached at latestdevelopments@wizards.com.*