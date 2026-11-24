---
id: wdachdvv
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/05-08-getting-to-know-cascade
title: Getting to Know Cascade
published: '2009-05-08'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    lang_detected: en
    capture_id: 722767
    url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    captured_at: '2022-08-19 22:35:19+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    lang_detected: en
    capture_id: 722767
    url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    captured_at: '2022-08-19 22:35:19+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    lang_detected: en
    capture_id: 722767
    url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    captured_at: '2022-08-19 22:35:19+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    lang_detected: en
    capture_id: 722767
    url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
    captured_at: '2022-08-19 22:35:19+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: wdachdvv
  url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
  page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
  lang: en
  template: drupal
  captured_at: '2022-08-19 22:35:19+00'
  capture_id: 722767
  wayback_url: https://web.archive.org/web/20220819223519id_/https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-07
- document_id: wdachdvv
  url: http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/37
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/37
  lang: en
  template: aspx
  captured_at: '2014-03-13 01:38:37+00'
  capture_id: 620943
  wayback_url: https://web.archive.org/web/20140313013837id_/http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/37
- document_id: wdachdvv
  url: https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08
  page_key: magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08
  lang: en
  template: drupal
  captured_at: '2021-12-09 04:18:01+00'
  capture_id: 722798
  wayback_url: https://web.archive.org/web/20211209041801id_/https://magic.wizards.com/en/articles/archive/latest-developments/getting-know-cascade-2009-05-08
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: wdachdvv
  capture_id: 620943
  url: http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/37
  wayback_url: https://web.archive.org/web/20140313013837id_/http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/37
  captured_at: '2014-03-13 01:38:37+00'
  template: aspx
  sha256: 2f2ea2dcc5be5fdafae5baf71f335487a196a29ad78645dbed85dc790978b8f9
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Force of Will
  - Contagion
  - Unmask
  - Time Spiral
  - Frantic Search
  - Priest of Gix
  - Mind's Desire
  - Spellweaver Helix
  - Magma Jet
  - Shock
  - Mind Rot
  - Tel-Jilad Justice
  - Oxidize
  - Lose Hope
  - Stand Firm
  - Serum Visions
  - Ardent Plea
  - Enigma Sphinx
  - Demonic Dread
  - Violent Outburst
  - Terminate
  - Esper Stormblade
  - Enlisted Wurm
  - Maelstrom Nexus
  - Zuran Orb
  - Ancestral Vision
  - Eureka
  - Hypergenesis
  - Captured Sunlight
  - Oblivion Ring
  - Kitchen Finks
  - Loxodon Hierarch
  - Bituminous Blast
  - Aven Mimeomancer
  - Blitz Hellion
  - Cloven Casting
  - Dauntless Escort
  - Deathbringer Thoctar
  - Fight to the Death
  - Filigree Angel
  - Finest Hour
  - Glory of Warfare
  - Identity Crisis
  - Knight of New Alara
  - Knotvine Paladin
  - Lavalanche
  - Lich Lord of Unx
  - Lightning Reaver
  - Madrush Cyclops
  - Maelstrom Pulse
  - Mayael's Aria
  - Meddling Mage
  - Mycoid Shepherd
  - Necromancer's Covenant
  - Nemesis of Reason
  - Predatory Advantage
  - Retaliator Griffin
  - Sages of the Anima
  - Soulquake
  - Sovereigns of Lost Alara
  - Spellbound Dragon
  - Spellbreaker Behemoth
  - Thought Hemorrhage
  - Time Sieve
  - Unscythe, Killer of Kings
  - Vedalken Heretic
  - Wargate
  occurrences: 95
---
Cascade is a mechanic that produces free spells, and that is an element of **Magic** that developers must treat carefully. There were a number of things that could have gone wrong with cascade, but we were able to get the mechanic to a place that was both safe and fun. I'll talk about our journey to understand cascade as a mechanic overall, then discuss one of the questions we had to answer about how we were going to use it.

![](https://i.ormos.uk/6f/13/6f1328b70b4cb5da235b422251c6cb01c52a00a7d61b9f9fcd523358a2720a20.jpg) 

  

**Magic** cards that skirt the mana system must be balanced very carefully. Force of Will, Contagion, and Unmask ask for cards in your hand rather than mana, and all three of these cards have been Constructed superstars. Cards like Time Spiral, Frantic Search, and Priest of Gix that gave players their mana back after they resolved enabled degenerate decks during Urza block. Mind's Desire is a great example of a card that uses free spell mechanics in a way that mostly didn't break **Magic** while still being powerful, but achieving this requires careful tuning to not create a monster like Time Spiral. On the other hand, a card like Spellweaver Helix offers lots of fun potential, but is not powerful in ways that tournament **Magic** players are likely to appreciate. Balancing cards that allow free spells so that they are both powerful and fun is a challenge that **Magic** developers have struggled with.

Cascade is a mechanic that produces free spells. It is also an exciting new mechanic that *Alara Reborn* needed to show off. We knew that we needed to be able to make cascade card that were powerful, fun, and balanced, so we spent some time early in *Alara Reborn* development thinking about the mechanic as a whole so that we would be able to cost cards that used the mechanic correctly.

![](https://i.ormos.uk/07/33/07336adedecaeca299cd6f25b307a7fd31443d93d5cef15e0121c2e826278bb2.jpg) 

  

An interesting exercise when thinking about a mechanic is to think in the abstract about how much mana it costs to add that mechanic to a card. Having a vague but reasonable answer for this question helps us cost simple cards that use that mechanic. For example, one might compare Magma Jet to Shock, Fill With Fright to Mind Rot, and Tel-Jilad Justice to Oxidize, and conclude that "scry 2" costs exactly ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) to add to a card. However, this gets messier when one is confronted with cards like Lose Hope, Stand Firm, or Serum Visions. How much does "Draw a card" cost, and how much does "Scry 2" cost? Honestly, I don't have a good answer for that question, and I'm sure the *Fifth Dawn* developers didn't either. 

![](https://i.ormos.uk/4b/98/4b98a5a27376db54f0f842736357c477a25e0bdcf485f6f60844646a83e72232.jpg)

It is even more challenging to think about the mana cost of mechanics that change value depending on the card that they are attached to. One great example of such a mechanic is trample. A French vanilla 1/1 creature with trample does not get much out of the trample ability. On the other hand, a French vanilla 7/7 with trample is a very powerful creature. Cascade, on the other hand, scales with the converted mana cost of a card and not with the power of a creature. That variability makes thinking about its value tricky, but spending time thinking about the question is still useful.

We discovered two different ways to think about the value of cascade. The first is based on variance. When you cast a spell with cascade, you're going to get a randomly produced card from your deck. The cost of the cascade spell determines how many of the cards in your deck you can hit. Ardent Plea's cascade trigger may find only a few of the cards in your deck, while Enigma Sphinx could easily be the most expensive card you have chosen to play and therefore give you no control over which of the rest of your cards you find. **Magic** players are very smart, and we knew that some players would sculpt their decks to make their inexpensive cascade spells hit exactly what they wanted every time. This made cascade more powerful on low-cost cards.

The other way is to think about mana production. You always get a free card when you cast a spell that has cascade. Because you get to cast that new card for free, the cascade spell also generates mana, and the amount of mana generated is exactly the converted mana cost of the new spell. Therefore, a great way to think about how much mana the cascade spell is generating is the average mana cost of the card you cascade into. Casting an Ardent Plea in a deck with few one-mana spells is very likely to find you a two-mana spell, and therefore the cascade trigger has produced two mana for you. That's very different from casting Enigma Sphinx, which will hit almost all of the rest of the cards in your deck. You might hit a six-mana spell, a four-mana spell, or a one-mana spell, so the expected ratio of the cascade card's converted mana cost to the amount of mana effectively produced by the cascade trigger is much lower. Because of this, cascade represents a large fraction of a cheap cascade spell's power, while a more expensive cascade spell gets a smaller fraction of its power from cascade. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Ardent Plea" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Ardent%20Plea&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Enigma Sphinx" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Enigma%20Sphinx&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

You can see the result of our discussions from looking at the cascade spells organized by mana cost. Ardent Plea, Demonic Dread, and Violent Outburst all grant fairly minor effects, but are still very strong cards because they consistently cascade into Terminates, Esper Stormblades, and other powerful two mana cards. On the other hand, Enlisted Wurm and Enigma Sphinx get to have sizable bodies because they aren't consistently producing free five- or six-mana cards from cascade.

You might also notice that there are no two-mana cascade spells. This is not an accident. Imagine for a moment that the following card exists.

![](https://i.ormos.uk/e0/01/e001a5594c80449c3d23d5120b31f4d7b5ed6d0cd05a303aa591939e226a272b.jpg) 

  

If this card existed, you could play only one unique card that costs one mana in your deck. This would change the action of cascade from a fun source of crazy randomness into a bizarrely mechanical tutoring effect. You would reveal cards from the top of your library, but you would play the spell that you knew all along you were going to play. The randomness would only come from the different amounts of information you granted your opponents. 

We really felt this effect in a Future Future Elder Dragon Highlander game that we played with *Alara Reborn* cards, in which Alexis Janson got a Maelstrom Nexus in play. A few people were capable of killing it, but we all wanted to see the card in action. Alexis started with a one-mana spell next turn. As it turns out, she had only three zero-mana spells in her deck. We encouraged her to just search her deck for the three cards and pick one of them at random, but she chose to do her duty as a member of the *Alara Reborn* development team and do exactly what the card said. It took her about a minute and a half to produce a Zuran Orb and do the required shuffling, and that showed us the annoying potential of low-cost cascade cards.

 ![Maelstrom Nexus](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Maelstrom%20Nexus&options=) 

  

Another reason that Waterfall is not a card is that thanks to *Time Spiral*, **Magic** now has some very powerful spells that have converted mana cost of zero. A card like Waterfall would have allowed players to abuse those spells very easily. For example, one could put four copies of Ancestral Vision into a deck along with four Waterfalls and no spells that cost one mana. This means that Waterfall would always lead to drawing three cards, which is quite a deal for the low cost of ![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif). Amusingly, that's not the most dangerous of the *Time Spiral* spells without mana costs. Eureka's effect allows a player with the right cards in hand to win the game on the spot, and thanks to Hypergenesis a player with access to Waterfall would have a guaranteed Eureka for only two mana. The combination of the potential craziness with zero-cost spells and the mechanical annoyance kept us from making two-mana cascade spells.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Eureka" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Eureka&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hypergenesis" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hypergenesis&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

After plenty of play, we felt comfortable with making three-mana cascade spells. We knew that the potential for the Hypergenesis deck still existed, but we also felt that the cost of including no one- or two-mana spells in one's deck was high enough that nothing would go wrong. On the other hand, that is hardly an insurmountable barrier, and plenty of players seem excited about the possibility of converting Demonic Dread, Ardent Plea, and Violent Outburst into the two-, one-, or zero-mana spell of their choice. We expect that this will turn out to be a fun thing to do, but also that it won't be ruinously powerful.

![](https://i.ormos.uk/b2/5d/b25dda1daf8d7fe4c37599de81c5faa3c93c0c39d8885cbc0272a79240362cea.jpg) 

  

One question we had to answer about how to use cascade was how many instants we wanted to give cascade to. *Alara Reborn* lead developer Matt Place kept a careful eye on how many instants had cascade. He understood how crushing it can be to have cards come out of nowhere and punish you for attacking. If too many instants had cascade, players might be ambushed by cascade cards after they attack one too many times and decide that attacking into open mana is just wrong. It's not very fun when it's never right to attack, so Matt wanted to make sure that this did not become the case due to excessive amounts of instants with cascade. On the other hand, it wouldn't be very interesting if there were no instants with cascade at all, because then you would be safe all the time. Matt's goal was to find a happy medium, and put cascade on instants only where it made sense to do so.

Captured Sunlight was one card that Matt had his eyes on. It entered development exactly as printed except that it was an instant and it only gained 3 life. Mike Turian noticed how brutal it was in Limited when someone attacked into a surprise creature from a Captured Sunlight, and proceeded to build a board control deck that used Captured Sunlight to cascade into Oblivion Rings and Kitchen Finks. Captured Sunlight felt like a less powerful Loxodon Hierarch, but the surprise factor made for very painful situations. *Alara Reborn* lead developer Matt Place knew that gaining life at instant speed was fun, but he also knew that excessive amounts of unfun surprises might be too painful. He decided that life-gain spells played fine as sorceries, and changed Captured Sunlight to a sorcery that gained 4 life instead of an instant that gained 3. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Captured Sunlight" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Captured%20Sunlight&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Bituminous Blast" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Bituminous%20Blast&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

This change caused people to wonder a little bit about why Bituminous Blast was an instant. This card was often more painful a surprise than Captured Sunlight because its main effect was (and is) excellent at instant speed. Why did it get to be an instant when Captured Sunlight didn't? Matt's answer was that there was a much larger amount of extra fun gained from making a removal spell an instant. Life-gain spells work fine as sorceries; Bituminous Blast would not. Personally, I also found the removal spell to be much less onerous because it costs five mana. When I attack into five open mana and get surprised, it's hard for me to get angry. I'm glad that Bituminous Blast is an instant.

 ![Violent Outburst](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Violent%20Outburst&options=) 

  

The only other instant with cascade is Violent Outburst. There was a suggestion that this card change to a sorcery and grant creatures haste as well as +1/+0. However, we enjoyed the card as an instant trick enough that this idea never gained momentum, so we left it as it was.

Cascade is an extremely fun mechanic. Its potential frightened us early in *Alara Reborn* development, but we did the work to make it both exciting and balanced. We're proud of the cascade cards we printed, and we hope you are enjoying them!

### Last week's poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>Are you attending, or have you attended, an <i>Alara Reborn</i> Launch Party this weekend?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes</td>&#10;    <td>1354</td>&#10;    <td>40.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>No</td>&#10;    <td>2017</td>&#10;    <td>59.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>3371</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

I'm excited by how many respondents attended the Launch Parties. They're a great way to get your hands on the new cards and meet other **Magic** players near you, and I hope everyone who went had fun. [Alara Reborn prerelease events](/en/articles/uncategorised/2009/05-06-alara-reborn-magic-online-prerelease) begin on Friday, May 15, and the set releases on **Magic Online** on May 18. If you didn't attend a Prerelease or Launch Party, or you just didn't get to play enough with *Alara Reborn* at those events, the **Magic Online** release events are your chance to get your fill!

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>What is your favorite (non-mythic) rare in <i>Alara Reborn</i>?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_37_poll1">&#10;                            <div>&#10;                              &#10;                              &#10;                              <a>Aven Mimeomancer</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Blitz Hellion</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Cloven Casting</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Dauntless Escort</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Deathbringer Thoctar</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Enigma Sphinx</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Fight to the Death</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Filigree Angel</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Finest Hour</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Glory of Warfare</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Identity Crisis</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Knight of New Alara</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Knotvine Paladin</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Lavalanche</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Lich Lord of Unx</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Lightning Reaver</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Madrush Cyclops</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Maelstrom Pulse</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Mayael's Aria</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Meddling Mage</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Mycoid Shepherd</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Necromancer's Covenant</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Nemesis of Reason</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Predatory Advantage</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Retaliator Griffin</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sages of the Anima</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Soulquake</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Sovereigns of Lost Alara</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Spellbound Dragon</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Spellbreaker Behemoth</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Thought Hemorrhage</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Time Sieve</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Unscythe, Killer of Kings</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Vedalken Heretic</a>&#10;                              <br>&#10;                              &#10;                              &#10;                              <a>Wargate</a>&#10;                              <br>&#10;                              &#10;                              &#10;                            </div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

* * *

[![](https://i.ormos.uk/d8/0f/d80f168e004fb630459268795525d14888a5a8845afca568f833e16fa762c9a8.jpg)](https://web.archive.org/web/20130809020704/http://www.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/alarareborn)