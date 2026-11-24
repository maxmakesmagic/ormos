---
id: ngb2wyvc
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/01-22-the-second-landfall
title: The Second Landfall
published: '2010-01-22'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    lang_detected: en
    capture_id: 731518
    url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    captured_at: '2022-06-26 10:55:57+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    lang_detected: en
    capture_id: 731518
    url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    captured_at: '2022-06-26 10:55:57+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    lang_detected: en
    capture_id: 731518
    url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    captured_at: '2022-06-26 10:55:57+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    lang_detected: en
    capture_id: 731518
    url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
    captured_at: '2022-06-26 10:55:57+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ngb2wyvc
  url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
  page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
  lang: en
  template: drupal
  captured_at: '2022-06-26 10:55:57+00'
  capture_id: 731518
  wayback_url: https://web.archive.org/web/20220626105557id_/https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-22
- document_id: ngb2wyvc
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/74
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/74
  lang: en
  template: aspx
  captured_at: '2013-07-07 17:20:39+00'
  capture_id: 623546
  wayback_url: https://web.archive.org/web/20130707172039id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/74
- document_id: ngb2wyvc
  url: https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-21
  lang: en
  template: drupal
  captured_at: '2022-01-17 10:00:23+00'
  capture_id: 731507
  wayback_url: https://web.archive.org/web/20220117100023id_/https://magic.wizards.com/en/articles/archive/latest-developments/second-landfall-2010-01-21
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: ngb2wyvc
  capture_id: 623546
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/74
  wayback_url: https://web.archive.org/web/20130707172039id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/74
  captured_at: '2013-07-07 17:20:39+00'
  template: aspx
  sha256: cb09f6678476a1b60c8da8db7ed93dad60c3a96d84bb25e7dd64651d8d25334b
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Harrow
  - Scalding Tarn
  - Pyroclasm
  - Day of Judgment
  - Phytohydra
  - Vulturous Zombie
  - Vigean Hydropon
  occurrences: 7
---
When we print a mechanic for the first time, we like to do simple implementations of it. The biggest reason is that it takes time for players to get comfortable with a new mechanic. Starting out with complicated cards using a mechanic gives a player no time to internalize how the mechanic works, and makes it hard for them to process everything. There is also a secret reason that we like to start simple. **Magic**'s designers and developers are also human, and need time to get comfortable with unfamiliar new cards. Therefore, starting out simple serves the same purpose for us: we get to know the basics of the mechanic well, which lets us design and develop more correctly.

Take, for example, the cycle of landfall creatures in *Zendikar*.

![](https://i.ormos.uk/29/c3/29c3fcf51c4c21c2cbd6b2a1f5af433feb95d8018a6eb6926d70484fa982c915.jpg) 

  

Once one makes the decision to use landfall as a major mechanic in one's set, it makes a lot of sense to have a cycle of common creatures that use it. However, there are lots of ways to implement such a cycle. You could decide that each of the creatures gains some keyword ability on landfall, and end up with a loose cycle whose cards are not obviously related to each other. The simplest version, however, was to have each card in the cycle receive the same bonus. Those versions are simpler for us to work with while we begin to understand the mechanic, and often end up being easier for players to hold in their heads as well.

*Zendikar* lead designer Mark Rosewater and lead developer Henry Stern both understood this. When the set was handed from design to development, each of the landfall creatures got +1/+1 upon landfall. After some playtesting, Henry thought that this wasn't enough of a bonus that players would want to build Constructed decks with them. He and his team adjusted their numbers so that the bonus was +2/+2, but he still had the discipline to keep the bonus the same across all five of them.

Another example of this is the expeditions.

![](https://i.ormos.uk/a5/e2/a5e200848349f0d04c559486a20a50022a5d6d3f76f06c3c190d54f5fbc9cda1.jpg) 

  

I was part of the mini-design team that created the initial versions of the quests that are in *Zendikar*. However, we didn't make any of these cards. We designed rare and uncommon quests that were wacky, wonky, and dripping with flavor. Most of the rare quests are our designs, and a few of the uncommon ones are as well. However, the common quests did not come from us. They were created by the development team, who wanted simple, accessible versions of quests that would both help players understand what the quest mechanic was doing and help them understand how quests work.

The common quests and common landfall creatures allowed us to get a very firm handle on how the landfall mechanic works, and prepared us for what was to come.

![](https://i.ormos.uk/be/26/be2615fd533ea55fd2af81ac26af31a19f2aa977acd2758b127187a4bb78dee5.jpg) 

  

Now, on to Worldwake. It shouldn't surprise you that we still did some simple landfall cards in Worldwake. For now, though, we're doing our best to show you the coolest stuff, so I don't have any simple landfall cards to show you. However, I can show you this simple card that interacts well with landfall, which **Magic** developer Mike Turian spoiled on [his Twitter feed](http://twitter.com/mturian) two days ago.

![Explore](https://i.ormos.uk/c2/83/c2838ffa8f73978fa64652906b66b8748bc1f4792a4e7903810449df652cbd03.jpg "Explore") 

  

(Aside: I'll also be spoiling a card on [my own Twitter feed](http://twitter.com/tomlapille) sometime Friday morning. Perhaps you should be ready!)

We did some slightly weird stuff in *Worldwake*. For example, we have expanded landfall to non-permanents. Have a look at Mysteries of the Deep.

![Mysteries of the Deep](https://i.ormos.uk/c4/0a/c40ad51d9dc41c98fa61b0b37625b85a7568da7b50011e8e3d38e6bfefb79b69.jpg "Mysteries of the Deep") 

  

This card and its friends require a little bit more mind space than, say, the common creatures I started this article with. With one of those creatures sitting on the battlefield, you know that you need to care about when you play a land. However, now that some instants have landfall, you'll sometimes need to be able to go back in time to remember whether or not you've played a land. Now that you've played with *Zendikar* for a while, we're confident that you'll be able to do that.

![](https://i.ormos.uk/bd/3c/bd3c8d75a671b337052f52276886f08735f12202cbaead7c10fbe6bdec2ff368.jpg) 

  

The need to do this will not come up so much with Mysteries of the Deep, which you'll normally cast in your main phase after playing a land, or in your opponent's end step, either obviously not having played a land or having sacrificed a fetch land immediately beforehand. However, there are landfall instants similar to Mysteries of the Deep that are potent combat tricks. I will warn you now: if you are playing in the *Worldwake* Prerelease and your opponent makes a point of playing a land before attacking you, watch out!

Another place we went with landfall in *Worldwake* is creatures with tap abilities that untap upon landfall. Here's one of those.

![Tideforce Elemental](https://i.ormos.uk/02/de/02defe1865f7895e33cb58e862722c0dc5578942621c14d9c2047abe3402d78b.jpg "Tideforce Elemental") 

  

This card's effect isn't complicated, nor does it have the potential for causing memory issues. However, it creates tricky situations in gameplay, as I learned recently while playing Limited with the first bunch of physical *Worldwake* product that arrived inside R&D. My opponent and I were in a complicated race; he had three creatures of varying sizes out, while I had a Tideforce Elemental and two other creatures of different sizes. After my draw step, I had both a Harrow and a Scalding Tarn in my hand.

None of these cards are individually that complicated, but the overall board state was quite a puzzle for me to figure out. Do I just tap my opponent's creatures now, and attack for damage? Do I wait for his turn, and tap multiple creatures before his attack step? Do I attack now, then wait until after he attacks to untap my tapped creatures and ambush his attackers? I enjoyed figuring out what I was supposed to do in this situation, but I was glad that I had experience with landfall to draw from while I was doing it.

Speaking of slightly wonky cards with landfall, you may also get to meet the fabled Convertible Turtle at the *Worldwake* Prerelease. It's a Mark Rosewater pet card, so it shouldn't surprise you to hear that it's a little wacky!

We also used our newfound understanding of landfall to make some completely over-the-top cards. Here's Admonition Angel.

![Admonition Angel](https://i.ormos.uk/18/4c/184cb217ca2f7b408254913b2b7d69955c4935bcef719f8863014b7c20909171.jpg "Admonition Angel") 

  

This card featured very prominently in our testing of *Zendikar* / *Worldwake* Constructed. I will not claim that it is not powerful, because that would be a lie. However, we are confident that it is safe to print. Perhaps you will open one at your *Worldwake* Prerelease and exile a bunch of your opponents' permanents. Hopefully none of your opponents will do that to you.

![](https://i.ormos.uk/4c/ff/4cffaecab239ef02c3eaac5df10dab3cbc76e167ca592bc09ee655f1a2707df8.jpg) 

  

Now, let's talk about my preview card, which is another over-the-top landfall card. *Worldwake* is about lands coming alive. Because of this, we wanted to make some kind of "land lord"- a creature with a landfall ability that made your lands better. Here's the text box from the first version we made.

> Lands you control are 1/1 creatures that are still lands.  
>   
>  Landfall — Whenever a land enters the battlefield under your control, put a +1/+1 counter on each land you control.

This card immediately captured our imagination with the story it tells. First, your lands all become creatures. Then, when you play another land, all of your lands grow. As I observed,

> TML 2/17/2009: This is a lot of dice/beads running around.

However, our experiences with him were tons of fun despite that. There's a sort of meta-Timmy excitement that happens when you realize that you've already put twenty-four beads on your lands, you don't have any more within arm's reach, and you actually need more. This happened a couple of times, which caused us to pull out the **Magic** R&D equivalent of the big gun:

![](https://i.ormos.uk/fa/0f/fa0f32b6d74d8702aa7bf62cf585f530d3fadff09ce1fc2666179015e611f507.jpg) 

  

However, we also realized a depressing phenomenon. These comments come from Ken Nagle, Mike Turian, me, Ken, and Alexis Janson respectively.

> KEN 3/13/2009: This guy and Ambush Commander read like "Please Wrath of God my team and lands away." I don't think I've seen an Ambush Commander in play outside of Elves VS Goblins. Kinda wish this did what a Hopscotch plane did, Landfall - turn land into a 5/5 permanently, plains vigilance, forest trample, etc.  
>  MT 3/16: Maybe we should make waking up the lands activated, so it has less of that feel.  
>  TML 3/18/2009: I had fun playing this dude in limited today. I don't know how to solve the KEN problem, which I do agree is annoying, but he was seriously insanely fun.  
>  AJ 3/19: I would recommend a no-mana sacrifice ability to help solve the wrath-your-lands problem, although three abilities is a lot of text. Ambush commander sort of had that but you had to keep 1G up.  
>  sw 3/24: Agreed, although this guy does read fun!

A bunch of Standard playtesting with this card caused us to be very unhappy with this card's game play. Any time any of us built a deck with it, we got hit with Pyroclasms and Day of Judgments, a fate that we did not wish on anyone in the real world. It's nice when a card reads so exciting to us that we go off and build decks with it, but it's quite bad when we are shown so quickly that what we did was a terrible idea. We pride ourselves on making a game that remains fun over time, so we decided to go back to the drawing board rather than release an exciting card that would let people down so quickly.

![](https://i.ormos.uk/cf/fe/cffe0ca3a58210ef15040ac332e96bb29d773a63242d11da0c01d7b974b7e53d.jpg) 

  

I don't recall who had the idea for the final version of Avenger of Zendikar. I can, however, backsolve the likely inspiration. In each set, we have a limited number of token types, and one of the tokens we were already planning to include in *Worldwake* was a 0/1 Plant token. (We all fell in love with the first card that produced it. If you look around the **Magic** internet today, you might find it!) Rather than make lands into creatures, Avenger of Zendikar might simply make one creature token for each land, and then be a lord for that creature type. The best token available for this job was the Plant, so suddenly we had a Plant lord.

Here's the completed Avenger of Zendikar.

![Avenger of Zendikar](https://i.ormos.uk/9d/82/9d825f220dc5a17d6bf77633daa901fedfc7431f3e65ec31c4cc7a700fd345a3.jpg "Avenger of Zendikar") 

  

This card works just fine as a card on its own in any **Magic** deck, but it will go crazy in a deck equipped to put lots of lands into play quickly. That will make you even more Plants when you first play the Avenger, and it will also let you grow your Plants faster. If you're feeling tribal, you can also build a Plant deck around this guy. Plants like Phytohydra and Vulturous Zombie already deal in +1/+1 counters, and you can also use Avenger of Zendikar to keep your Vigean Hydropon going on and on. *Worldwake* even has a couple of new plants to work with!

We hope to see you at the *Worldwake* Prerelease next Saturday. Many lands will fall, and many things will happen when they do. And, if you're lucky, perhaps you'll get to put a lot of +1/+1 counters on a lot of Plants.

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>What do you think of Jace, the Mind Sculptor?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>It's awesome!</td>&#10;    <td>4328</td>&#10;    <td>48.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>It's good.</td>&#10;    <td>2852</td>&#10;    <td>31.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>It's okay.</td>&#10;    <td>1323</td>&#10;    <td>14.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>It's bad.</td>&#10;    <td>216</td>&#10;    <td>2.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>It's terrible!</td>&#10;    <td>250</td>&#10;    <td>2.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>8969</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Soon you'll get your chance to play with Jace, the Mind Sculptor for the first time. My suspicion is that after spending some time with this new Jace on your team, or having to face down an opponent who recruited him, you might join the group of people that voted for "awesome."

### This Week's Polls

In which of the following types of **Magic** events have you participated in the past three months?

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Have you participated in a Grand Prix event in the last three months?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_74_poll1">&#10;                            <div>&#10;                              &#10;                              Yes<br>No<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Have you participated in a Pro Tour Qualifier event in the last three months?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_74_poll2">&#10;                            <div>&#10;                              &#10;                              Yes<br>No<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Have you participated in a Friday Night Magic event in the last three months?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_74_poll3">&#10;                            <div>&#10;                              &#10;                              Yes<br>No<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Have you participated in a paper sanctioned event not covered by the previous three polls in the last three months?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_74_poll4">&#10;                            <div>&#10;                              &#10;                              Yes<br>No<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

* * *

[![](https://i.ormos.uk/a9/4d/a94d970addf8a06940d62e6102b659280c5c0d1f6887810c418e59702b7861c0.jpg)](https://web.archive.org/web/20130620141938/http://www.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/worldwake)