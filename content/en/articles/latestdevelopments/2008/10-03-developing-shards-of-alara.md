---
id: jw591we9
kind: article
lang: en
path: /en/articles/latestdevelopments/2008/10-03-developing-shards-of-alara
title: Developing Shards of Alara
published: '2008-10-03'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: billstark
  name: Bill Stark
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    lang_detected: en
    capture_id: 721019
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    captured_at: '2022-09-29 23:58:31+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    lang_detected: en
    capture_id: 721019
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    captured_at: '2022-09-29 23:58:31+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    lang_detected: en
    capture_id: 721019
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    captured_at: '2022-09-29 23:58:31+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    lang_detected: en
    capture_id: 721019
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
    captured_at: '2022-09-29 23:58:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: jw591we9
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
  lang: en
  template: drupal
  captured_at: '2022-09-29 23:58:31+00'
  capture_id: 721019
  wayback_url: https://web.archive.org/web/20220929235831id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-02
- document_id: jw591we9
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/6
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/6
  lang: en
  template: aspx
  captured_at: '2013-07-01 21:52:59+00'
  capture_id: 623402
  wayback_url: https://web.archive.org/web/20130701215259id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/6
- document_id: jw591we9
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03
  lang: en
  template: drupal
  captured_at: '2022-08-16 14:17:46+00'
  capture_id: 721024
  wayback_url: https://web.archive.org/web/20220816141746id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-shards-alara-2008-10-03
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: jw591we9
  capture_id: 623402
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/6
  wayback_url: https://web.archive.org/web/20130701215259id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/6
  captured_at: '2013-07-01 21:52:59+00'
  template: aspx
  sha256: 605e539133deb3c156e8b9125a683c0a82d36dcb1051c73ceca75f31e50dd905
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Salvage Titan
  - Incinerate
  - Resounding Thunder
  - Battlegrace Angel
  - Rafiq of the Many
  - Kresh the Bloodbraided
  - Altar of Dementia
  - Ooze Garden
  - Goblin Bombardment
  - Mons's Goblin Raiders
  - Murderous Redcap
  - Nantuko Husk
  - Kitchen Finks
  - Soul
  - Essence Warden
  - Spike Feeder
  - Knight of Meadowgrain
  - Goldenglow Moth
  - Ajani Vengeant
  - Elspeth, Knight-Errant
  - Empyrial Archangel
  - Godsire
  - Hellkite Overlord
  - Lich's Mirror
  - Mayael the Anima
  - Prince of Thralls
  - Sarkhan Vol
  - Sedris, the Traitor King
  - Sharuum the Hegemon
  - Sphinx Sovereign
  - Tezzeret the Seeker
  occurrences: 51
---
*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on Magic development. Enjoy!  
 –Kelly Digges, **magicthegathering.com** editor* 

 ![Edge_of_Autumn](https://i.ormos.uk/48/09/48091084d0aee85bc02c2e04e92eff2b7e54b7900d90437f1386f87fc412cb06.jpg)

Autumn. There is perhaps no season that so accurately evokes a feeling of change. The weather is turning, the leaves are falling. The political world is in upheaval, and professional sports rotate from baseball to football. And of course, most importantly, there's a brand new **Magic** set!

Today we're going to take a look at some of the stories that came from Development during the process of testing, tweaking, and finishing the set *Shards of Alara*. Before we get to that, however, it's important to re-examine the differences between the design and development teams and the roles they play in creating a **Magic** set. How are they separate?

Consider this scenario: your boss has told you she needs you to brainstorm up some ideas for Project Y. You sit down with pen and paper, uninhibited. No restrictions, no rules, no nothing—just coming up with as many ideas as you possibly can. If some of them aren't perfect? No worries, that will get worked out later. Your responsibility is simply coming up with the starting points for everything. Ideas, ideas, ideas.

Got that mental picture in your head? Great. That's (approximately) design.

Now it's time for the second scenario. It's a week later. The bevy of ideas you came up with have had a chance to brew, and it's time to re-examine them. Project Y now has some parameters. The product has to be a certain size, say, or evoke a specific feel. It has to fit the rules and regulations of the market it's being sold in. It's up to you to re-work the ideas you came up with while completely uninhibited into a final product. Some ideas will be thrown out; some new ones will be added. Some of the brainstorms will be edited to increase their potential; some will be edited to decrease it. Now you're entering the world of **Magic** Development.

We don't just make the game you love; we make the game you love better. How do we do that? So glad you asked...

### Salvage Titan

 ![Salvage Titan](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Salvage%20Titan&options=) 

No doubt fans of artifacts have been immediately drawn to Salvage Titan, particularly as it applies to Extended versions of Affinity. It's certainly an exciting and powerful card, and it made it through development receiving simultaneous powering up *and* down. Here's where we started:

> Salvage Titan 4BB  
>  Artifact Creature  
>  Trample.  
>  You may sacrifice three artifacts instead of paying Salvage Titan's casting cost.  
>  Remove three artifacts in your graveyard from the game: Return Salvage Titan from your graveyard to play.  
>  6/3

Pretty over the top, huh? Not only did the Titan start out with trample, but its return-from-graveyard ability actually put the card straight into play. No need to come up with ![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif) or three more artifacts to be sacrificed; just a 6/3 coming at 'ya. Oof.

It didn't take long for the developers to wrangle the Titan into decks that merited changing the card's stats. Putting the 6/3 back into play from the graveyard was very powerful, and it hurt the flavor of the card. By making Salvage Titan return to a player's hand, the player gets to fill their graveyard with more artifacts, which they can later use to salvage the card should it wind up getting killed. This took care of power level concerns while simultaneously adding free flavor at no charge.

The final change to reduce power was dropping trample from the Titan's abilities. It was determined that such a large monster able to be played so quickly was a bit over the top when it virtually guaranteed punching some amount of damage through. That said, the powering down merited a small improvement in toughness; Salvage Titan might not be able to get through for as much without trample, but it would also be harder to kill via Incinerate or Resounding Thunder at 6/4.

The end result? A fun, artifact-friendly behemoth that's challenging but not over-the-top broken.

### Rafiq of the Many

 ![Rafiq of the Many](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Rafiq%20of%20the%20Many&options=) 

When Mark Rosewater announced the introduction of mythic rares to the world this past summer, the development team had already pushed out the first set of the new breed of cards. The directive for them had been clear: they were to be powerful, important story tellers but not necessarily Constructed auto-includes. In an effort to get the very first class right, a lot of effort went into tinkering with their power levels, shifting some up while others were shifted down. Rafiq was a member of the group who became more powerful.

There's no doubt Rafiq has a commanding on-field presence now. Not only does he provide a 3/3 body, but his abilities function as a pseudo-haste effect, giving a creature already in play +1/+1 and doubling their power. When Rafiq hits the board, the rest of the table sits up and takes note; trouble could soon be headed in their direction.

But what if Rafiq cost ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) instead of the much friendlier ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)? What if the bonus he provided your creatures was different? Or what if, as he was originally presented, he was:

> Rafiq of the Many 2WUG  
>  Legendary Creature  
>  Heroic – Whenever a creature you control attacks alone, it gets +1/+1 and double strike until end of turn.  
>  3/3

His impact on a game of **Magic** would have been reduced. Testing revealed some of these weaknesses and quickly inspired changes, while also cleaning up the ability that would eventually become exalted. Originally exalted was simply an ability word for any bonus applied to a lone attacking creature. As testing progressed, however, it soon became apparent that constantly having to check all the bonuses applied to your creature from a plethora of different sources was confusing; why not make "heroic" a single bonus that was universal so it was quick to recognize and more enjoyable to play?

That enabled us to make the ability more fun and easier to understand, but dropped Rafiq in power level too much. How could we have a strong heroic (by then called exalted) creature from Bant that stood out from the rest? The fix came by compromise: finding a way to keep the cool extra exalted abilities on some of the cards that had them while still universalizing exalted overall. So Rafiq was keyworded with exalted, then gained the additional bonus of providing double strike to a lone attacker. You can see this work on other cards such as Battlegrace Angel.

 ![Battlegrace Angel](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Battlegrace%20Angel&options=) 

How about the final version? After much discussion, Rafiq of the Many made it to the masses in his present form. No word yet on how popular he'll be as an [Elder Dragon Highlander / Commander](https://web.archive.org/web/20130518210852/https://www.wizards.com/magic/tcg/article.aspx?x=magic/rules/edh) general, but it seems safe to bet you'll soon see him during many such games.

### Kresh the Bloodbraided

 ![Kresh the Bloodbraided](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Kresh%20the%20Bloodbraided&options=) 

While Rafiq was one of the mythic rares that saw an increase in power level, some of the mythic rares were so strong they had to be taken down a peg or two during testing. Kresh the Bloodbraided, one of the representatives from Jund, was just such a card.

As he sits now, Kresh is very flavorful and sufficiently powerful. He plays nice with the Jund mechanic of devour, quickly growing unmanageable by benefiting from what the denizens of Jund do best. His 3/3 body isn't oversized at five mana but can quickly grow disproportionate. And of course he even takes a stab at appealing to Johnnys everywhere; how will *you* build around Kresh? Altar of Dementia? Ooze Garden? Goblin Bombardment? The options are tantalizing.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Ooze Garden" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Ooze%20Garden&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Altar of Dementia" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Altar%20of%20Dementia&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

When Development first got hold of Kresh, however, things were a different story. Here's what his first stats looked like: 

> Kresh the Bloodbraided 2BRG  
>  Legendary Creature  
>  Carnage – Whenever a creature goes to the graveyard from play, put a +1/+1 counter on each creature you control.  
>  4/4

It didn't take long for Development to do unfair things with *that*. Mons Johnson (of Mons's Goblin Raiders fame) managed a combo involving Kresh, Murderous Redcap, and Nantuko Husk that could easily "go infinite" and sucked a lot of fun out of games. Persist creatures in general were very good with Kresh, and it soon became apparent that even at five mana, having no activation cost made it much too simple to use Kresh as an engine to do degenerate things; not really what we had in mind when designing the Jund legendary mythic rare.

Naturally, stats started morphing. The 4/4 was dropped to 3/3, but that didn't really address the fact Kresh's abilities were being abused. His "carnage" ability (which eventually lost its status as an ability word) changed from giving *all* of your creatures +1/+1 to giving Kresh himself the bonus. A mere +1/+1 from a creature dying wasn't quite strong enough, however, so things went back the other way. Now Kresh himself gets large fast based on what happens on the board, but without being unfun. And, like Rafiq, you can count on Kresh showing up at the EDH table in the near future!

### Cradle of Vitality

 ![Cradle of Vitality](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Cradle%20of%20Vitality&options=) 

For our last example in this installment, we're going to look at an excellent example of an unassuming card at print that started at much more powerful than it was intended to be. We know it today as a neat way to improve decks focused on lifegain, and possibly a way of interacting with persist creatures (did someone say Kitchen Finks?). Things weren't always this way, and here's how it looked when it was brought to development:

> Cradle of Vitality 2W  
>  Enchantment  
>  Whenever you gain life, you may pay X, where X is less than or equal to the amount of life you gained. If you do, put X 1/1 white Spirit creature tokens with flying into play.

This, as many developers noted, was a cool combo with cards like Soul or Essence Warden. It didn't fit the flavor we were looking for, though, and the 1/1 Spirits soon became +1/+1 counters:

> Cradle of Vitality 2W  
>  Enchantment  
>  Whenever you gain life, you may put that many +1/+1 counters on target creature.

Aaron Forsythe quickly pointed out that not having an activation cost for this version was problematic. What happened when someone resolved Cradle in addition to Spike Feeder? A two card combo that left you with an arbitrarily large amount of life and an arbitrarily large Spike Feeder? Something that powerful shouldn't be so easily accomplished for so little effort, and that's before considering the implications of an easily achieved "impervious" Kitchen Finks.

Upping the initial cost from ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif) to ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif) made the card a bit more balanced, but Greg Marques demonstrated the card still wasn't where it needed to be one afternoon during Future Future League testing. The deck he used for the deed? It revolved around efficient life-gain creatures like Kitchen Finks, Knight of Meadowgrain, and...Goldenglow Moth. It may not sound like much, but it's a rough world when Goldenglow Moth morphs from an innocuous 0/1 into a 4/5 flier that just netted your opponent 4 life before munching your biggest attacker—and did all of it for free.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Goldenglow Moth" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Goldenglow%20Moth&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Kitchen Finks" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Kitchen%20Finks&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

Ultimately the card was revised to the version we see today, ready for fun and the ingenuity of the public's deck builders, but safe from the shenanigans that might have been wrought had the crafty minds of the development team not caught it before seeing print.

### Conclusions

That's a look at some of the interesting stories from Development during the process that brought you *Shards of Alara*. Just like the second stage of the Project Y example, we added some ideas, cut some, increased the power of a few, and decreased the power of a few others. Between the two of us (design and development) we're very excited the world finally gets to see what we've been working so hard on. Here's to enjoying *Shards of Alara*!

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>Which set will you miss most when Standard rotates?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <i>Time Spiral</i>&#10;    </td>&#10;    <td>3023</td>&#10;    <td>32.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <i>Planar Chaos</i>&#10;    </td>&#10;    <td>1550</td>&#10;    <td>16.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <i>Future Sight</i>&#10;    </td>&#10;    <td>1479</td>&#10;    <td>15.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I don't play Standard</td>&#10;    <td>1448</td>&#10;    <td>15.5%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <i>Coldsnap</i>&#10;    </td>&#10;    <td>981</td>&#10;    <td>10.5%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>None of the above</td>&#10;    <td>539</td>&#10;    <td>5.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>What is Standard?</td>&#10;    <td>320</td>&#10;    <td>3.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>9340</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

With *Time Spiral*—including its 121 "timeshifted" cards—making up close to half the cards rotating out of Standard, it's not surprising to see it at the top of the list.

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Which mythic rare are you looking forward to getting the most?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtgcom_ld6_poll1">&#10;                            <div>&#10;                              &#10;                              &#10;                              <a>Ajani Vengeant</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Elspeth, Knight-Errant</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Empyrial Archangel</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Godsire</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Hellkite Overlord</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Kresh the Bloodbraided</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Lich's Mirror</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Mayael the Anima</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Prince of Thralls</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Rafiq of the Many</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sarkhan Vol</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sedris, the Traitor King</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sharuum the Hegemon</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sphinx Sovereign</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Tezzeret the Seeker</a>&#10;                              <br>&#10;                              &#10;                              &#10;                            </div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

* * *

*Shards of Alara* Launch Parties are this weekend, October 3-5, at stores worldwide, and you won’t want to miss them. Get your chance to buy *Shards of Alara* cards as soon as they go on sale, play the new set with your friends, and get a foil, alternate-art Ajani Vengeant promo card!