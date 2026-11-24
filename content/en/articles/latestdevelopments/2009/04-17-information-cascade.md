---
id: 2chz0v61
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/04-17-information-cascade
title: Information Cascade
published: '2009-04-17'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    lang_detected: en
    capture_id: 723229
    url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    captured_at: '2022-05-17 11:51:34+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    lang_detected: en
    capture_id: 723229
    url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    captured_at: '2022-05-17 11:51:34+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    lang_detected: en
    capture_id: 723229
    url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    captured_at: '2022-05-17 11:51:34+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    lang_detected: en
    capture_id: 723229
    url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
    captured_at: '2022-05-17 11:51:34+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 2chz0v61
  url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
  page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
  lang: en
  template: drupal
  captured_at: '2022-05-17 11:51:34+00'
  capture_id: 723229
  wayback_url: https://web.archive.org/web/20220517115134id_/https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-17
- document_id: 2chz0v61
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/34
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/34
  lang: en
  template: aspx
  captured_at: '2013-07-02 02:20:48+00'
  capture_id: 620916
  wayback_url: https://web.archive.org/web/20130702022048id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/34
- document_id: 2chz0v61
  url: https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-15
  page_key: magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-15
  lang: en
  template: drupal
  captured_at: '2021-12-01 01:34:06+00'
  capture_id: 723216
  wayback_url: https://web.archive.org/web/20211201013406id_/https://magic.wizards.com/en/articles/archive/latest-developments/information-cascade-2009-04-15
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 2chz0v61
  capture_id: 620916
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/34
  wayback_url: https://web.archive.org/web/20130702022048id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/34
  captured_at: '2013-07-02 02:20:48+00'
  template: aspx
  sha256: 53c63505901e9c161a418738140b16032db32430e34364a72e74d7dfedd68be5
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Etherium Sculptor
  - Sharuum the Hegemon
  occurrences: 5
---
Today I have the privilege of introducing *Alara Reborn*'s new mechanic. It's called cascade, and it's spectacularly fun. You may have already seen it on Bituminous Blast from the [Visual Spoiler](https://web.archive.org/web/20130702140852/https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/alarareborn/spoiler).

![](https://i.ormos.uk/f2/87/f2878acc867a71d6fa0bdca6b39b6962319e0ae4e1729d73becf8d34713d1c59.jpg) 

  

As with all **Magic** cards, the shining façade of the final product belies the massive amount of effort that went into producing it. Today I'll share with you the journey of the cascade mechanic, and then show you a card that was built specifically to show it off.

Before that, though, I'll introduce the *Alara Reborn* development team!

![Matt Place](https://i.ormos.uk/ea/a3/eaa36db8b94a55ec752ca93412586ac318b349d51a69f2f46c61d00f9c6668ab.jpg "Matt Place")

**Matt Place** (lead) – Matt is a former Pro Tour winner and full-time **Magic** developer. Matt also led the development of two other multicolor-themed sets, *Dissension* and *Eventide*, and that made him uniquely qualified to solve the problems that an exclusively multicolored set posed. I learned a lot from watching him work within the restrictions that were placed on him to create a fun set.

![Dave Guskin](https://i.ormos.uk/db/7a/db7a1461380a9b1b1a818e73c45395d72f8612ab206ac03a18ba077cb013bd23.jpg "Dave Guskin")

**Dave Guskin** – Dave is a full-time web developer at Wizards. He is the driving force behind the [new version](/en/articles/feature/2009/04-16-the-new-gatherer) of the [Gatherer](https://web.archive.org/web/20090417000000/http://gatherer.wizards.com/) card database and he was also instrumental in the creation of the [Totally Normal Draft Viewer](https://web.archive.org/web/20100123005110/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/activity/158). Dave spends part of his time in **Magic** R&D helping us with Limited playtests and playing Constructed in the FFL, and he occasionally he serves on set development teams. 

![Alexis Janson](https://i.ormos.uk/ee/e0/eee0d44326785d6cab5488c0c4ad1ad943d8c6ff2b26281945c039e7527772dc.jpg "Alexis Janson")

**Alexis Janson** – Alexis was the winner of the Great Designer Search. Her full-time job now has her working on **Magic Online**, but she continues to help out on both design teams and development teams. Her design credits include *Morningtide*, *Eventide*, *Shards of Alara*, and *Alara Reborn*, and she also was a member of the *Shadowmoor* development team.

![Erik Lauer](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg "Erik Lauer")

**Erik Lauer** – Erik once had a reputation as one of the **Magic** Pro Tour's best deck-builders, and now he uses those same skills to make sure that **Magic** is fun for all players no matter how much effort they put into trying to win. Midway through *Alara Reborn* development, however, Erik began his role as the lead developer of ***Magic** 2010* and became too busy to continue working on *Alara Reborn*. He left the team and was replaced by ....

![Mike Turian](https://i.ormos.uk/2b/09/2b094d288b20f58968d51834eb02b2ed1381ae876700918a5c14f07004174e55.jpg "Mike Turian")

**Mike Turian** – Mike is both a member of the **Magic** Pro Tour Hall of Fame and an experienced **Magic** developer. His lead developer credits include *Future Sight*, *Morningtide*, and *Conflux*, and that experience meant that Mike had no trouble seamlessly jumping onto the *Alara Reborn* team.

  

### Cascade's Journey

Now that you know the team, let's talk about cascade!

The first version of cascade came from Mark Gottlieb. Its playtest name was "spin," and it originally had a number attached to it that was equal to the converted mana cost of the spell it was on. The ability looked like this:

> Spin N (When you play this spell, find the first nonland card in your library that costs N or less. You may play it instead of CARDNAME. Shuffle your library.)

 ![Spin_into_Myth](https://i.ormos.uk/a1/2c/a12c3dc8406e984406e7f5955e5e3fb3aa7f67c72105e52cc493a08dd941f1a9.jpg)

This mechanic created tension for the player by showing what was behind door number two and asked if the player wanted that instead of what they had cast. When you cast a spin spell, you might end up playing it, but you might also take the buyout option. 

There were several problems with this mechanic. One was that cards with spin needed to have costs that took into account the increase in power that the spin mechanic gave them. This meant that the effect of a spin card that cost four mana was usually worse than the effect of a four mana card that didn't have spin, so if you hit a four mana card with the spin, you were likely to just play the new card instead. This made the cards feel more like mystery buttons than well-defined spells.

Mike Turian did not enjoy the tension that the mechanic created. He was looking for a fun and variable experience when he cast a spell with spin, and instead was presented with a thought-provoking decision when the mechanic resolved. He suggested that cascade allow you to get both spells instead of just one. That would make the mechanic all-upside, and it would also keep the game from pausing while someone made a decision. The teams decided to try that version, and they liked it.

> Spin N (When you play this, find the first nonland card in your library that costs N or less. **You may play it for free.** Shuffle your library.)

There was now a new problem. If the nonland cards in your deck all had spin and had the same converted mana cost, playing only one of them would eventually result in every spell in your deck being cast. Something less extreme but similar would happen if all the nonland cards in your deck that cost three mana had spin, and no other cards in your deck cost less than four. In that case, you would get all the spells that cost three for free. We didn't like that this felt very deterministic and tutor-like, so the team changed the spin ability to only trigger when a spin card was played from your hand.

> Spin N (When you play this **from your hand**, find the first nonland card in your library that costs N or less. You may play it for free. Shuffle your library.)

 ![Fatespinner](https://i.ormos.uk/92/1d/921d4e184719ebfd4ffa0c454de864efab5ea071687f6338406363c0b543b633.jpg)

The "play from your hand" clause solves the problem of spinning into another spin card. However, many people argued that this was not a problem at all. In fact, spinning into another spin card sounded like an incredibly fun thing to do. Many ways to enable this were discussed, but the simplest was to allow the mechanic to only see cards that cost less than the cost of the spell. This had various benefits. One was that it allowed for the dream of enormous spell chains. The second is that it made the template much shorter when written rigorously. It allowed us to delete "from your hand," and it also allowed us to simply say "less" rather than "less than or equal to." Finally, it made the mechanic work cleanly without requiring us to attach a number to it. This was the next version.

> Spin (When you play this from your hand, find the first nonland card in your library **that costs less than this card.** You may play that card for free. Shuffle your library.)

Spin now provided big dreams. A lucky player could play a 7-cost spin spell, spin into a 6-cost spin spell, spin into a 5-cost spin spell, and so on, until the process stopped with a two-mana spell. It stopped at two because Alara Reborn's hook kept it from containing any one mana spells, and therefore a two-mana spin spell in a deck full of *Alara Reborn* cards would simply reveal its caster's library to its opponent before forcing it to be shuffled. The cheapest cards in *Alara Reborn* that have cascade cost three mana, but the possible spell chain that went all the way from 7 to 2 was still very exciting.

The mechanic passed through the hands of some editors, and then the designers handed the following templated version off to development.

> Spin (When you play this spell, **reveal cards from your library until you reveal a nonland card with a lesser converted mana cost. You may play it without paying its mana cost. Then** shuffle your library.)

Ken Nagle had fallen in love with the dream of big spell chains and was one of the people who advocated for this version of the mechanic. Once spin had been changed to accommodate the dream of spinning through every possible mana cost, Ken built a deck and tried to live it. I don't know if he ever managed to chain spells all the way from 7 to 2, but I do remember at least one chain of spin cards he produced that was four cards long. His deck produced tons of dramatic and fun moments and was a source of constant amusement for Ken's opponents and all who watched his games.

About this time, the creative team dubbed the mechanic "cascade," and **Magic** editors began to cut words away from its reminder text. The file contained the following version of cascade for a long time.

> **Cascade** (When you play this spell, reveal cards from the top of your library until you reveal a nonland card **that costs less**. You may play it without paying its mana cost. Then, shuffle your library.)

 ![Temporal_Cascade](https://i.ormos.uk/f0/04/f004b18fd71fe9ed2f2ca167b1db3119c8548fb3543274240b7ae69971f63dd3.jpg)

Near the end of development, many playtesters complained that cascade forced them to shuffle their library. The physical process of resolving a cascade trigger was extremely fun, but needing to shuffle every time was too annoying. Lead developer Matt Place took sympathy on them. The templating team was unhappy about adding words to an already wordy mechanic, but they solved the problem by removing the cards from the game rather than revealing them, then putting them on the bottom of the library. 

The last question to be answered was in what order the removed cards go on the bottom of your library. If the player who resolved the spin was allowed to choose the order, a player who had nothing left in his deck to spin into would end up stacking his entire deck. We didn't like this, so we went with the slightly bizarre option of randomizing only the revealed cards. This is still a little bit of shuffling, but it isn't nearly as bad as randomizing the whole deck.

Here's the final version. 

> Cascade *(When you play this spell, remove cards from the top of your library from the game until you remove a nonland card that costs less. You may play it without paying its mana cost. Put the removed cards on the bottom in a random order.)*

Of course, we didn't just design and develop a mechanic. We also created cards to put it on, and we tried to use some of those cards to truly show it off. In some ways, the best part of cascade is the fun of discovering what unknown card you get for free. Because of this, the *Alara Reborn* design team decided to make a creature with cascade that could be cast multiple times. Here's what they came up with.

![](https://i.ormos.uk/e9/db/e9db3b6d4fdf076d7831462698aa2c83881d1c7fd52b33258f0155f146de6f7c.jpg) 

  

This card was designed when someone jokingly said that the only thing better than casting a cascade spell was casting a cascade spell multiple times. Someone immediately had the idea to put cascade on a creature that went back to your hand somehow. It seemed too annoying to have the creature immediately go back to a player's hand when it died, so instead they went with the slightly strange "third from the top" clause.

Having cascade on a seven-mana spell creates awesome moments in game play. When you play Engima Sphinx in an Esper deck, you could end up with something as small as an Etherium Sculptor, but you might also end up with something as enormously awesome as Sharuum the Hegemon. It is a mystery!

![](https://i.ormos.uk/ee/80/ee80e9252f307b8d57adc3c28c52ce415fb15e95c977d700da06b48c81c5f906.jpg) 

  

However, if your deck has cascade cards of all the mana costs from 7 down to 3, you could very well end up with a completely ridiculous chain like this one.

![](https://i.ormos.uk/62/23/622328f1c27d0366898a3b0eee5afb317094e7beca523fe839bccbf15f39c531.jpg) 

  

I have had a blast playing with cascade, and I can't wait for everyone else to be able to share that fun. Your first chance to play with *Alara Reborn* will come at the *Alara Reborn* Prerelease, which is April 25 and 26. Those events will be happening at local stores all over the world, so find one and I promise you'll have tons of fun playing with all the new multicolored cards!

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>Do you follow @<a href="https://web.archive.org/web/20090417000000/http://ww2.wizards.com/Site/LeavingWizards.aspx?url=http://twitter.com/dailymtg&amp;origin=">dailymtg</a> on Twitter?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>No. I know what Twitter is but don't have an account.</td>&#10;    <td>4560</td>&#10;    <td>60.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>No. I don't know what Twitter is.</td>&#10;    <td>2006</td>&#10;    <td>26.5%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes</td>&#10;    <td>552</td>&#10;    <td>7.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>No. I have a Twitter account and don't follow @dailymtg.</td>&#10;    <td>450</td>&#10;    <td>5.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>7568</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Twitter is a social networking site that lets people share what they are up to in real time. Through the @[dailymtg](https://web.archive.org/web/20090417000000/http://ww2.wizards.com/Site/LeavingWizards.aspx?url=http://twitter.com/dailymtg&origin=) Twitter feed, Kelly Digges and Monty Ashley post fun tidbits about day-to-day life inside **Magic** R&D. Sometimes we use it for other things. For example, people who follow the @dailymtg twitter feed received a special bonus preview card last Friday.

![](https://i.ormos.uk/1d/08/1d08e5804eefd138de2264de8078378b9db3c9805c13f921e72a97870323e23b.jpg) 

  

We promised that we would give another preview card over Twitter if we hit 2000 followers. We did, and then we previewed this.

![](https://i.ormos.uk/c3/d2/c3d2c5105456147e606d7186d0f6de1556a9c5907abc6c72ff82cfee71f80391.jpg) 

  

We know that not everyone saw those on Twitter, and some may not have seen them at all before now. You can make sure you don't miss any cards by checking the [Visual Spoiler](https://web.archive.org/web/20130702140852/https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/alarareborn/spoiler). Every card we preview anywhere—such as the preview card in today's [The Week That Was](/en/articles/buildingonabudget/2009/04-16-post-fixing)—will find its way there!

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>What is your favorite preview card so far?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_34_poll1">&#10;                            <div>&#10;                              &#10;                              Terminate<br>Unscythe, Killer of Kings<br>Spellbound Dragon<br>Nemesis of Reason<br>Jund Hackblade<br>Knight of New Alara<br>Soulquake<br>Thought Hemorrhage<br>Sages of the Anima<br>Aven Mimeomancer<br>Bituminous Blast<br>Marisis's Twinclaws<br>Pale Recluse<br>Ethercaste Knight<br>Sphinx of the Steel Wind<br>Blitz Hellion<br>Defiler of Souls<br>Jenara, Asura of War<br>Lavalanche<br>Dragon Broodmother<br>Time Seive<br>Thraximundar<br>The five Borderposts<br>Maelstrom Pulse<br>Qasali Pridemage<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

* * *

[![](https://i.ormos.uk/09/52/09521b3acbfe3dd0349682e9a886a132926be02dd748d9e6e7f23a8a883d6f8f.jpg)](/en/articles/event-coverage/undated/magic-the-gathering-prereleases-3)