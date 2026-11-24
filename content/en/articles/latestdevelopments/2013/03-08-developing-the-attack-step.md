---
id: b5dmjb4f
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/03-08-developing-the-attack-step
title: Developing the Attack Step
published: '2013-03-08'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    lang_detected: en
    capture_id: 720597
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    captured_at: '2022-05-17 11:09:23+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    lang_detected: en
    capture_id: 720597
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    captured_at: '2022-05-17 11:09:23+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    lang_detected: en
    capture_id: 720597
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    captured_at: '2022-05-17 11:09:23+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    lang_detected: en
    capture_id: 720597
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
    captured_at: '2022-05-17 11:09:23+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: b5dmjb4f
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
  lang: en
  template: drupal
  captured_at: '2022-05-17 11:09:23+00'
  capture_id: 720597
  wayback_url: https://web.archive.org/web/20220517110923id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-08
- document_id: b5dmjb4f
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/237&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/237
  lang: en
  template: aspx
  captured_at: '2013-07-02 01:44:27+00'
  capture_id: 231404
  wayback_url: https://web.archive.org/web/20130702014427id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/237&print=true
- document_id: b5dmjb4f
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05
  lang: en
  template: drupal
  captured_at: '2022-01-21 12:51:36+00'
  capture_id: 720590
  wayback_url: https://web.archive.org/web/20220121125136id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-attack-step-2013-03-05
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: b5dmjb4f
  capture_id: 231404
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/237&print=true
  wayback_url: https://web.archive.org/web/20130702014427id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/237&print=true
  captured_at: '2013-07-02 01:44:27+00'
  template: aspx
  sha256: 41ba448da9dead0d62b6e187fbb879406071c93da56cb1d3c0a52fcc4ef8fe43
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Grizzly Bears
  - Hill Giant
  - Pillarfield Ox
  - Catacomb Slug
  - Horned Turtle
  - Elusive Krasis
  - Scorchwalker
  - Slaughterhorn
  - Ember Beast
  - Smite
  - Ætherize
  - Zhur-Taa Swine
  - Ghor-Clan Rampager
  - Thragtusk
  - Boros Reckoner
  - Restoration Angel
  - Azorius Charm
  - Searing Spear
  - Fencing Ace
  occurrences: 29
---
It's Gruul Week, and where would we be if that didn't mean talking about one of the most basic interactions in **Magic**: attacking and blocking. I briefly considered writing a long string of incoherent words and drawing crude diagrams, but the guild letter hit that note hard, and like all good writers, I fear retribution from my up-to-now benevolent editors for attempting to shirk my duties. So, instead, I'll be discussing some of the intricacies of the attack step, with a special eye on how it impacted the development of Gruul. 

![](https://i.ormos.uk/93/c6/93c64b99747e3cb38fa2373655d3e0e6878e030ded087c52a0b54fa11b1d0be3.jpg) 

  

**Magic** developers are probably most closely associated with the kind of player who enjoys long control games or tight tempo races, but there are more than a few of us who like to let the beast out every once in a while and get a good smashing on. For the last several years, we have worked to move the major action of the game more onto the battlefield and out of players' hands, and that means making the interactions on the battlefield more meaningful. Planeswalkers being attackable, for one example, have created a greater necessity for most decks to have some kind of creature offense available to them, and that pushes more interaction on the battlefield. 

I believe that moving the action to the battlefield shouldn't be associated with dumbing down the game, however. It is the task of development to create a fun and dynamic and robust game where players are able to interact meaningfully with not just their hands, but on the battlefield as well. I think it is important to note the disassociation of the concepts of simplicity and strategically deep game play. One of the things [New World Order](/en/articles/makingmagic/2011/12-05-new-world-order) strives for is to make the game more simple at the most basic level, but to also increase the overall strategic depth of the game. I believe we have done this by harnessing many of the tools **Magic** already had available to it, but doing so in a more thoughtful way than we once did. 

![](https://i.ormos.uk/97/ca/97ca0238686fd72a793374ea07e405255b109ee97d0a3fddf4e84e25924979a7.jpg) 

  

### A Beautiful Asymmetry

One of the most fruitful things [Richard Garfield](https://web.archive.org/web/20130602205428/http://www.wizards.com/magic/magazine/archive.aspx?author=richard%20garfield) built into the original version of **Magic** was different values for power and toughness (and not just power when attacking and power when defending). While it seems obvious now, it certainly wasn't a guarantee to be in the game. Plenty of games pre- and post- **Magic** used one stat for combat. The direction **Magic** went certainly adds some complexity but also a lot of interesting game play. It also lets development make a lot of small tweaks to get cards to the right power levels and to make playing the game more interesting. 

To give an example, let's say we are just playing with creatures with square stats. You have out two 2/2 vanillas, and I have out a 4/4 vanilla. You can't attack me, and I am able to attack and trade my creature for both of your creatures (if you want to make the trade). Now let's look at options for making these creatures non-square. Moving even one of the 2/2s into a 2/3 all of a sudden turns the trade unprofitable for me—my much-larger creature now only trades for one of yours. If my creature was a 3/5, however, I can now freely attack through both of your creatures, assuming there are no combat tricks. Turning my creature into a 4/3 doesn't change its power in the first example, but now it will trade with a 3/1, if you have it. Development makes sure to populate a set with a fruitful number of different power and toughness combinations to ensure that even without a single instant, we can create a good deal of variation, and decisions, in game play. It also lets us tweak the individual strength of creatures by increasing or reducing their stats to trend toward them dying more often from combat, surviving more often from combat, or being better at trading with other creatures in combat.

When a **Magic** set is turned over from design to development, design generally has the common creatures pretty well balanced on an individual scale for Limited, but it tends to bias away from the simple interactions I discussed above and focus more on whatever the main theme of the set is. That's good, though. Design sets out to create a bold and new vision of what Limited and Constructed should play like, and it is up to development to both make that vision a reality and to figure out how to make that line up with what is expected out of a finished **Magic** set. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Grizzly Bears" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Grizzly%20Bears&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hill Giant" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hill%20Giant&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Development's first job is to really put the set through its paces in Limited and create an environment full of dynamic interaction, and a lot of that work goes into the seemingly unexciting work of spreading out power and toughness in a way that gives as much game play as possible. If all of the powerful creatures in a set were simply Grizzly Bears or Hill Giants with abilities, **Magic** would become stale very quickly. Making sure the powerful creatures appear at various sizes and various spots on the mana curve alone helps to make a more dynamic environment, with more interesting combat decisions. One of the things, at least for Limited, that development does is figure out ways to reduce the word count in the set and add interaction with important power-and-toughness-combination creatures. Design files are rarely full of vanilla cards like Pillarfield Ox, Catacomb Slug, or Horned Turtle, but they are part of the glue that really holds Limited together. Development tries to figure out when and where these are needed and adds them to the set, generally filling in much-needed gaps in a color's curve. 

![](https://i.ormos.uk/8c/c9/8cc97f712646bce8eb56d03f21c56f50872f8187282255458df969dc28950711.jpg) 

  

### The Tricks of the Trade

*Gatecrash* is a study in power/toughness asymmetry in **Magic**. Two of the mechanics in the set—bloodrush and evolve—rely heavily on the game play that asymmetrical stats bring up. It was interesting to watch people come around to how powerful Elusive Krasis was in the evolve deck, not just because it was unblockable, but because at 0/4 it is both likely to evolve all of your other creatures and to be evolved by almost all of your future creatures. The evolve deck also pushes you away from playing a lot of the same creatures and toward a greater variety of power and toughness so evolve happens more frequently. 

This isn't Simic Week, though, so let's get back to the guild at hand—Gruul. And what does Gruul like to do? Gruul smash! 

![](https://i.ormos.uk/84/48/8448bd64f6debe80eb493feb21edea2c4bd23ed737642d033d980dc830d3c2f3.jpg) 

  

Gruul wants its creatures to ABA. A—always. B—be. A—attacking. Always be attacking. If you aren't attacking, you are losing. If you aren't attacking, your opponent is getting a foothold. If you aren't attacking, you can't crush your opponents underneath your feet. You attack, or you hit the bricks. But, uh, anyway, getting back to the subject at hand, one of the keys to making Gruul work was to make sure that attacking with Gruul was the easier decision and blocking was the harder one. It's what bloodrush excels at doing.

![](https://i.ormos.uk/ec/72/ec72168412120bec46f7a671b32227396f1faea4fb7ce4fe3bcaf6f436a92430.jpg) 

  

Bloodrush creatures on the whole have different power and toughness to make blocking decisions more difficult and to better tweak their usefulness as creatures on the battlefield or combat tricks in the hand. If your opponent knew he or she was always playing around +2/+2 or +3/+3, he or she could more easily make optimal decisions on how to block, but Bloodrush was developed to not make those decisions easy. Scorchwalker is perhaps the poster child for this duality. It is rare that a 5/1 for four has much usefulness on the battlefield, or that a +5/+1 combat trick for three would be a particularly high pick, but the combination of the two on the same card really gets things going. Because all of the bloodrush creatures are playable in either form, your opponent has to at least respect all of them when you attack with your Slaughterhorn and Ember Beast. Some are intended to more heavily punish blocking with multiple creatures, some are better at punishing you for blocking with one large creature, and others punish for not blocking at all. The mechanic highlights Gruul as the guild of straightforwardness in attacking, while at the same time creating interesting game-play interactions with the other guilds. 

### Dynamic Defense

Gruul is all about attacking, but we've put in more than a few ways to prevent it from dominating the format—after all, that wouldn't be very interesting. The impulsivity and aggressiveness of Gruul is it greatest strength, but is also what gives its opponents the best opening to defeat it. While the Gruul may be able to dodge counterspells, any removal in response to a creature being bloodrushed is devastating, and we made sure to place a few pieces that are more specifically geared toward the Gruul menace. The first, and most obvious in Limited, is Smite. You could almost say it is perfectly placed to counter bloodrush (interesting, that). While Smite is a generally powerful Limited card in a vacuum, it is the density of combat tricks in *Gatecrash* and their importance to the Gruul strategy that really pushes it over the edge here. The key weakness of Gruul is that it will rely on combat tricks, not just larger creatures, to win in combat, so removal in response to bloodrush will get you a two-for-one. Without any strong card-drawing or evasion to make up for the loss in tempo, Gruul will have a harder time than other colors coming back from that. 

![](https://i.ormos.uk/a3/91/a3913995220d80e1595202819bf156db7832c0d9c2494ffd6182b64bbabb8013.jpg) 

  

The second card is Ætherize. Although it is an uncommon, and won't show up as much as Smite, it has the benefit of not only negating blocked attackers, but unblocked creatures as well. Whenever a blue player presents the Gruul player with the perfect opportunity for a Scorchwalker or Zhur-Taa Swine to end the game, the Gruul player will have to weigh taking his or her shot at it, and how far behind an Ætherize will put the player. 

In Constructed, Bloodrush cards like Ghor-Clan Rampager excel at giving decks super-efficient answers to powerful blockers like Thragtusk, Boros Reckoner, and Restoration Angel, but it is similarly weak to cards like Azorius Charm or, often, just Searing Spear. One thing we enjoy is creating cards that both are trumps and have trumps to different strategies and cards. It is one of the things that keeps Standard moving as a format and, hopefully, keeps it new and interesting for players week after week. 

### Looking Forward

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Fencing Ace" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Fencing%20Ace&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Faerie Impostor" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Faerie%20Impostor&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Bloodrush works wonderfully in the confines of *Gatecrash* Limited, but it is destined for larger things than just that. When *Dragon's Maze* comes out, we hope you will find even more fun interactions with bloodrush in Limited, combining it with familiar cards in *Return to Ravnica*. It could be bloodrushing a Fencing Ace on turn three with Scorchwalker to take a more-than-healthy chunk out of your opponent's life total, or using Faerie Imposter to return a Slaughterhorn that has outlived his usefulness on the battlefield and is ready to assist in combat from your hand. And all of that is without even touching the goodies that *Dragon's Maze* adds to the mix. As much as I am enjoying *Gatecrash* Limited, I'm looking forward to everyone being able to enjoy the full block as well. 

![](https://i.ormos.uk/ae/c0/aec0e7691a77d43b24d9d7b3d09e4801440738bc4e4b6c6bf72bf0cb7f24962c.jpg) 

![](https://i.ormos.uk/d2/e7/d2e71f791c65cdf2356ac3e6081d4ccdf9e2a1f59666204e5204fd80e7c308d9.jpg) [![](https://i.ormos.uk/26/95/2695b2bb507d5fe24582ed4d128fa225368e26fa88c9de28501f29fc109b7b3d.jpg)](/en/events/2011/league-facts/avacyn-restored-league) ![](https://i.ormos.uk/2c/02/2c02ec1873bd94d38416e3306848241b26b0ab4734d2bbe37aefdde35e8e9518.jpg) [![](https://i.ormos.uk/ee/bb/eebb6c15c343bd8da6d69decf1b3523b9e3fa4402a2523b9743d22f4d82025b4.jpg)](https://web.archive.org/web/20130629155253/http://www.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/gatecrash)  
  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130308000000/https://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[Developing%20the%20Attack%20Step]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130308000000/http://staging.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130903232710/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 