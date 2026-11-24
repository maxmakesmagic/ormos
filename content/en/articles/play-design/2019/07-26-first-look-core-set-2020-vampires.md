---
id: xdgf2ttr
kind: article
lang: en
path: /en/articles/play-design/2019/07-26-first-look-core-set-2020-vampires
title: 'First Look: Core Set 2020 Vampires'
published: '2019-07-26'
column_slug: play-design
column: Play Design
authors:
- slug: andrew-brown-f7ed0296
  name: Andrew Brown
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    lang_detected: en
    capture_id: 1133863
    url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    captured_at: '2020-11-07 23:02:08+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    lang_detected: en
    capture_id: 1133863
    url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    captured_at: '2020-11-07 23:02:08+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    lang_detected: en
    capture_id: 1133863
    url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    captured_at: '2020-11-07 23:02:08+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    lang_detected: en
    capture_id: 1133863
    url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
    captured_at: '2020-11-07 23:02:08+00'
    rule: url.article_section
sources:
- document_id: xdgf2ttr
  url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
  page_key: magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
  lang: en
  template: drupal
  captured_at: '2020-11-07 23:02:08+00'
  capture_id: 1133863
  wayback_url: https://web.archive.org/web/20201107230208id_/https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: xdgf2ttr
  capture_id: 1133863
  url: https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
  wayback_url: https://web.archive.org/web/20201107230208id_/https://magic.wizards.com/en/articles/archive/play-design/first-look-core-set-2020-vampires-2019-07-26
  captured_at: '2020-11-07 23:02:08+00'
  template: drupal
  sha256: 23239635fac02f369aaeafeccc9d2e63885f2374a11c7187c591501d129f1aab
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 5
---
Welcome to First Look! This is a repeating column every quarterly release (similar to the M-Files) where Play Design will share decklists and their thought processes from the [Future Future League](/en/articles/play-design/2017/07-07-designing-hour-of-devastation-cards-to-meet-ffl-goals) focus period of the most recent set. The FFL focus period is the three months during set design where we handle most of the competitive balance tweaks to the card file.

Today, I'll be going in depth in how we got to the printed versions of [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion) and [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord), and going through our attempts to make Vampires a fun and competitive deck.

# Eighth-Set Standard Perils

*Core Set 2020* being the eighth set introduced into the Standard environment provides some interesting challenges for us. The more cards in the environment, generally the higher the power level and more opportunities for combos and synergies. It's tough to make generically powerful cards in the eighth set, as for them to hit Standard they must beat out a lot of competition. This makes it harder for the set after it to add fun and strong cards as the environment shrinks because of rotation. Competing for deck slots in a five-set environment is very different than in an eight-set environment.

One strategy we use to get around this is make cards that synergize with the cards from previous years. One of the most successful examples of this was the Blue-Red Thopters deck from *Magic Origins*. *Magic Origins* introduced cards such as [Chief of the Foundry](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chief+of+the+Foundry), [Pia and Kiran Nalaar](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pia+and+Kiran+Nalaar), and [Whirler Rogue](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whirler+Rogue) to combine with [Ornithopter](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter), [Ensoul Artifact](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ensoul+Artifact), and [Springleaf Drum](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springleaf+Drum). Blue-Red Thopters was an explosive deck that took the metagame by storm on release but fluctuated up and down in popularity once players figured out how to adapt to it. (My testing team for Pro Tour *Magic Origins* had the Blue-Red Thopters deck, but I still played Blue-Black Control . . . many regrets.)

# Vamping Up the Vampires

With that in mind, we set out with the goal of making Vampires a fun and exciting deck for Standard. Given the set space in M20, we had two card slots to work with to accomplish that goal. The final cards that we ended up on were [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord) and [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion).

One of the first things we did was look at the existing pool of Vampire cards and identify holes or problems with their baseline strategy. The two problems we felt most necessary to address were that too much power was locked up in high converted mana cost creatures and that there weren't any powerful mana sinks. [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord) allows the top of the curve to get into play ahead of schedule, and [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion) is a meaningful mana sink for the later game.

# The Beginnings of the Knight of the Ebon Legion

The initial goal for this design was to be an aggressively slanted card that specifically synergized with [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard). Our first design started out at this:

2B  
 Creature — Vampire Knight  
 At the beginning of your end step, if a player lost 4 or more life this turn, put a +1/+1 counter on each creature you control.  
 3/2

After some playtesting, we found that even though it accomplished the above stated goals, it was too snowball-y on the play and should be changed. As a three-drop, it was also pushing out cards we wanted to play such as [Mavren Fein, Dusk Apostle](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mavren+Fein%2C+Dusk+Apostle) and [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord). With those findings in mind, we tried this next:

B  
 Creature — Vampire Knight  
 2B: [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion) gets +3/+3 and gains menace until end of turn.  
 At the beginning of your end step, if a player lost 4 or more life this turn, put a +1/+1 counter on [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion) and you gain 2 life.  
 1/1

Playtesting of this version yielded more positive results. We enjoyed the interaction with [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard) being more toned down and loved the addition of a mana sink in the deck. In the environment, we were finding that [Goblin Chainwhirler](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Chainwhirler) was too brutal against the deck and menace wasn't the right keyword on an instant-speed activation. With that in mind, we added a point of toughness, changed menace to deathtouch, then took off the life gain as a balance compensation. Then after playing with those changes, we were happy to give it our final Play Design stamp of approval.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Knight+of+the+Ebon+Legion)](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion)

# Starting on Sorin, Imperious Bloodlord

Sorin was a tough one, it took us a lot of iterations and number tweaking to end up at his final set of abilities. It was nearly like pulling fangs . . . anyways. Here's the first version we tried:

3B  
 +2: Up to one target creature you control gains deathtouch and lifelink until end of turn. If it's a Vampire, put a +1/+1 counter on it.  
 -2: You may put a Vampire creature card from your hand onto the battlefield.  
 -7: You get an emblem with "Whenever you gain life, each opponent loses that much life."  
 4

We learned a lot from testing this version of Sorin. We enjoyed the play pattern on the plus ability making combat interesting and the -2 getting expensive Vampires into play. The main problem with this design was that once you chose an ability, you were likely locked into using the same ability again. -2ing would make [Champion of Dusk](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Champion+of+Dusk) draw into more Sorins and Vampires, which would encourage a -2 on the next turn and then playing a new Sorin. Once the +2 ability was used, building to the ultimate was too often more powerful than using the -2. Those play-pattern issues also made the card feel and play less like a planeswalker. With those findings in mind, we changed the design to three mana and looked for a different ability other than an ultimate. That got us to this:

2B  
 +1: Up to one target creature you control gains deathtouch and lifelink until end of turn. If it's a Vampire, put a +1/+1 counter on it.  
 ???????????????????  
 -3: You may put a Vampire creature card from your hand onto the battlefield.  
 4

When looking for a new ability, we asked ourselves "What angle can we give Vampires that Mono-White Aggro doesn't have?" Mono-White Aggro's weakness is generally closing when the opponent has stabilized the board. We opted for something that could close out the game if the opponent was at a low enough life total, and ended up with [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord)'s second plus ability, "+1: You may sacrifice a Vampire. When you do, [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord) deals 3 damage to any target and you gain 3 life."

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sorin%2C+Imperious+Bloodlord)](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord)

To wrap things up on the Vampires, here is one of the many configurations of Vampires that we tried out to test [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Ebon+Legion) and [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Imperious+Bloodlord):

#### Abro's Toolbox Sorin

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (4)

4 [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BImperious%5D+%5BBloodlord%5D) 

##### Creature (24)

2 [Forerunner of the Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForerunner%5D+%5Bof%5D+%5Bthe%5D+%5BLegion%5D) 4 [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdanto%5D+%5BVanguard%5D) 1 [Mavren Fein, Dusk Apostle](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMavren%5D+%5BFein,%5D+%5BDusk%5D+%5BApostle%5D) 4 [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnight%5D+%5Bof%5D+%5Bthe%5D+%5BEbon%5D+%5BLegion%5D) 4 [Champion of Dusk](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChampion%5D+%5Bof%5D+%5BDusk%5D) 4 [Legion Lieutenant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLieutenant%5D) 2 [Cruel Celebrant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCruel%5D+%5BCelebrant%5D) 2 [Pitiless Pontiff](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPitiless%5D+%5BPontiff%5D) 1 [Vona, Butcher of Magan](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVona,%5D+%5BButcher%5D+%5Bof%5D+%5BMagan%5D) 

##### Enchantment (7)

3 [Conclave Tribunal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConclave%5D+%5BTribunal%5D) 4 [Legion's Landing](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLanding%5D) 

##### Land (25)

4 [Godless Shrine](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 4 [Isolated Chapel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsolated%5D+%5BChapel%5D) 4 [Temple of Silence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 6 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 7 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### White (14)

2 [Forerunner of the Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForerunner%5D+%5Bof%5D+%5Bthe%5D+%5BLegion%5D) 4 [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdanto%5D+%5BVanguard%5D) 3 [Conclave Tribunal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConclave%5D+%5BTribunal%5D) 1 [Mavren Fein, Dusk Apostle](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMavren%5D+%5BFein,%5D+%5BDusk%5D+%5BApostle%5D) 4 [Legion's Landing](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLanding%5D) 

##### Black (12)

4 [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnight%5D+%5Bof%5D+%5Bthe%5D+%5BEbon%5D+%5BLegion%5D) 4 [Champion of Dusk](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChampion%5D+%5Bof%5D+%5BDusk%5D) 4 [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BImperious%5D+%5BBloodlord%5D) 

##### Multi colored (9)

4 [Legion Lieutenant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLieutenant%5D) 2 [Cruel Celebrant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCruel%5D+%5BCelebrant%5D) 2 [Pitiless Pontiff](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPitiless%5D+%5BPontiff%5D) 1 [Vona, Butcher of Magan](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVona,%5D+%5BButcher%5D+%5Bof%5D+%5BMagan%5D) 

##### Colorless (25)

4 [Godless Shrine](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 4 [Isolated Chapel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsolated%5D+%5BChapel%5D) 4 [Temple of Silence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 6 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 7 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### 1 (8)

4 [Legion's Landing](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLanding%5D) 4 [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnight%5D+%5Bof%5D+%5Bthe%5D+%5BEbon%5D+%5BLegion%5D) 

##### 2 (12)

4 [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdanto%5D+%5BVanguard%5D) 4 [Legion Lieutenant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLieutenant%5D) 2 [Cruel Celebrant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCruel%5D+%5BCelebrant%5D) 2 [Pitiless Pontiff](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPitiless%5D+%5BPontiff%5D) 

##### 3 (7)

2 [Forerunner of the Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForerunner%5D+%5Bof%5D+%5Bthe%5D+%5BLegion%5D) 1 [Mavren Fein, Dusk Apostle](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMavren%5D+%5BFein,%5D+%5BDusk%5D+%5BApostle%5D) 4 [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BImperious%5D+%5BBloodlord%5D) 

##### 4 (3)

3 [Conclave Tribunal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConclave%5D+%5BTribunal%5D) 

##### 5 (5)

4 [Champion of Dusk](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChampion%5D+%5Bof%5D+%5BDusk%5D) 1 [Vona, Butcher of Magan](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVona,%5D+%5BButcher%5D+%5Bof%5D+%5BMagan%5D) 

35 Cards 

##### Common (13)

6 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 7 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

##### Uncommon (17)

2 [Forerunner of the Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForerunner%5D+%5Bof%5D+%5Bthe%5D+%5BLegion%5D) 4 [Adanto Vanguard](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdanto%5D+%5BVanguard%5D) 3 [Conclave Tribunal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConclave%5D+%5BTribunal%5D) 4 [Legion Lieutenant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLieutenant%5D) 2 [Cruel Celebrant](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCruel%5D+%5BCelebrant%5D) 2 [Pitiless Pontiff](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPitiless%5D+%5BPontiff%5D) 

##### Rare (25)

1 [Mavren Fein, Dusk Apostle](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMavren%5D+%5BFein,%5D+%5BDusk%5D+%5BApostle%5D) 4 [Legion's Landing](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLegion%5D+%5BLanding%5D) 4 [Knight of the Ebon Legion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKnight%5D+%5Bof%5D+%5Bthe%5D+%5BEbon%5D+%5BLegion%5D) 4 [Champion of Dusk](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChampion%5D+%5Bof%5D+%5BDusk%5D) 4 [Godless Shrine](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 4 [Isolated Chapel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsolated%5D+%5BChapel%5D) 4 [Temple of Silence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 

##### Mythic (5)

4 [Sorin, Imperious Bloodlord](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BImperious%5D+%5BBloodlord%5D) 1 [Vona, Butcher of Magan](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVona,%5D+%5BButcher%5D+%5Bof%5D+%5BMagan%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forerunner+of+the+Legion)

[Deal Another Hand](https://web.archive.org/web/20190726000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Champion+of+Dusk)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Legion+Lieutenant)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Godless+Shrine)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Silence)

a:17:{i:0;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Forerunner of the Legion";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Adanto Vanguard";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Conclave Tribunal";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Mavren Fein, Dusk Apostle";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Legion's Landing";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Knight of the Ebon Legion";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Champion of Dusk";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:26:"Sorin, Imperious Bloodlord";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Legion Lieutenant";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cruel Celebrant";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Pitiless Pontiff";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Vona, Butcher of Magan";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Godless Shrine";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Isolated Chapel";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Temple of Silence";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}} 

I wanted to write about all the iterations that it took to get the Vampires deck to a fun and competitive level. But that goal conflicts with the original goal of this article which is to post decklists that we built during the making of M20. To compensate, here are my favorite decks that fall more into the "brew" category.

#### Michael Majors's Sai Forge

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (8)

4 [Renowned Weaponsmith](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRenowned%5D+%5BWeaponsmith%5D) 4 [Sai, Master Thopterist](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSai,%5D+%5BMaster%5D+%5BThopterist%5D) 

##### Artifact (26)

2 [Bolas's Citadel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBolas%5D+%5BCitadel%5D) 4 [Orazca Relic](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrazca%5D+%5BRelic%5D) 4 [Navigator's Compass](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNavigator%5D+%5BCompass%5D) 3 [Manifold Key](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManifold%5D+%5BKey%5D) 3 [Fountain of Renewal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFountain%5D+%5Bof%5D+%5BRenewal%5D) 4 [Mystic Forge](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BForge%5D) 4 [Gilded Lotus](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 2 [Mox Amber](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BAmber%5D) 

##### Enchantment (4)

4 [Gift of Paradise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGift%5D+%5Bof%5D+%5BParadise%5D) 

##### Land (22)

4 [Zhalfirin Void](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZhalfirin%5D+%5BVoid%5D) 4 [Temple of Mystery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMystery%5D) 2 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Breeding Pool](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 4 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Forest](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 

60 Cards 

##### Blue (8)

4 [Renowned Weaponsmith](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRenowned%5D+%5BWeaponsmith%5D) 4 [Sai, Master Thopterist](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSai,%5D+%5BMaster%5D+%5BThopterist%5D) 

##### Black (2)

2 [Bolas's Citadel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBolas%5D+%5BCitadel%5D) 

##### Green (4)

4 [Gift of Paradise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGift%5D+%5Bof%5D+%5BParadise%5D) 

##### Colorless (46)

4 [Orazca Relic](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrazca%5D+%5BRelic%5D) 4 [Navigator's Compass](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNavigator%5D+%5BCompass%5D) 3 [Manifold Key](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManifold%5D+%5BKey%5D) 3 [Fountain of Renewal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFountain%5D+%5Bof%5D+%5BRenewal%5D) 4 [Mystic Forge](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BForge%5D) 4 [Gilded Lotus](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 2 [Mox Amber](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BAmber%5D) 4 [Zhalfirin Void](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZhalfirin%5D+%5BVoid%5D) 4 [Temple of Mystery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMystery%5D) 2 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Breeding Pool](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 4 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Forest](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 

60 Cards 

##### 1 (10)

4 [Navigator's Compass](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNavigator%5D+%5BCompass%5D) 3 [Manifold Key](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManifold%5D+%5BKey%5D) 3 [Fountain of Renewal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFountain%5D+%5Bof%5D+%5BRenewal%5D) 

##### 2 (4)

4 [Renowned Weaponsmith](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRenowned%5D+%5BWeaponsmith%5D) 

##### 3 (12)

4 [Sai, Master Thopterist](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSai,%5D+%5BMaster%5D+%5BThopterist%5D) 4 [Gift of Paradise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGift%5D+%5Bof%5D+%5BParadise%5D) 4 [Orazca Relic](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrazca%5D+%5BRelic%5D) 

##### 4 (4)

4 [Mystic Forge](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BForge%5D) 

##### 5 (4)

4 [Gilded Lotus](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 

##### 6 (2)

2 [Bolas's Citadel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBolas%5D+%5BCitadel%5D) 

36 Cards 

##### Common (20)

4 [Gift of Paradise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGift%5D+%5Bof%5D+%5BParadise%5D) 4 [Orazca Relic](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrazca%5D+%5BRelic%5D) 4 [Navigator's Compass](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNavigator%5D+%5BCompass%5D) 4 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Forest](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 

##### Uncommon (14)

4 [Renowned Weaponsmith](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRenowned%5D+%5BWeaponsmith%5D) 3 [Manifold Key](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BManifold%5D+%5BKey%5D) 3 [Fountain of Renewal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFountain%5D+%5Bof%5D+%5BRenewal%5D) 4 [Zhalfirin Void](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZhalfirin%5D+%5BVoid%5D) 

##### Rare (24)

4 [Sai, Master Thopterist](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSai,%5D+%5BMaster%5D+%5BThopterist%5D) 2 [Bolas's Citadel](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBolas%5D+%5BCitadel%5D) 4 [Mystic Forge](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystic%5D+%5BForge%5D) 4 [Gilded Lotus](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGilded%5D+%5BLotus%5D) 4 [Temple of Mystery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMystery%5D) 2 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Breeding Pool](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 

##### Mythic (2)

2 [Mox Amber](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMox%5D+%5BAmber%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Renowned+Weaponsmith)

[Deal Another Hand](https://web.archive.org/web/20190726000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gilded+Lotus)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mystic+Forge)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Watery+Grave)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Orazca+Relic)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fountain+of+Renewal)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Navigator%27s+Compass)

a:18:{i:0;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Renowned Weaponsmith";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Sai, Master Thopterist";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Bolas's Citadel";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Gift of Paradise";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Orazca Relic";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Navigator's Compass";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Manifold Key";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Fountain of Renewal";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Mystic Forge";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Gilded Lotus";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mox Amber";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Zhalfirin Void";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Temple of Mystery";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Watery Grave";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Breeding Pool";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}}} 

#### Michael Majors's Red-White Bag

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (7)

3 [Cavalier of Flame](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BFlame%5D) 4 [Arclight Phoenix](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArclight%5D+%5BPhoenix%5D) 

##### Sorcery (11)

4 [Crash Through](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrash%5D+%5BThrough%5D) 3 [Cathartic Reunion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCathartic%5D+%5BReunion%5D) 2 [Finale of Promise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFinale%5D+%5Bof%5D+%5BPromise%5D) 2 [Deafening Clarion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeafening%5D+%5BClarion%5D) 

##### Instant (13)

3 [Jaya's Greeting](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaya%5D+%5BGreeting%5D) 4 [Lightning Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BStrike%5D) 4 [Heartwarming Redemption](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeartwarming%5D+%5BRedemption%5D) 2 [Justice Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJustice%5D+%5BStrike%5D) 

##### Artifact (4)

4 [Bag of Holding](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBag%5D+%5Bof%5D+%5BHolding%5D) 

##### Land (25)

2 [Cryptic Caves](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCaves%5D) 4 [Sacred Foundry](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 2 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Clifftop Retreat](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClifftop%5D+%5BRetreat%5D) 9 [Mountain](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Temple of Triumph](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 

60 Cards 

##### Red (23)

4 [Crash Through](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrash%5D+%5BThrough%5D) 3 [Jaya's Greeting](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaya%5D+%5BGreeting%5D) 4 [Lightning Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BStrike%5D) 3 [Cathartic Reunion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCathartic%5D+%5BReunion%5D) 3 [Cavalier of Flame](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BFlame%5D) 4 [Arclight Phoenix](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArclight%5D+%5BPhoenix%5D) 2 [Finale of Promise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFinale%5D+%5Bof%5D+%5BPromise%5D) 

##### Multi colored (8)

4 [Heartwarming Redemption](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeartwarming%5D+%5BRedemption%5D) 2 [Justice Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJustice%5D+%5BStrike%5D) 2 [Deafening Clarion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeafening%5D+%5BClarion%5D) 

##### Colorless (29)

4 [Bag of Holding](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBag%5D+%5Bof%5D+%5BHolding%5D) 2 [Cryptic Caves](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCaves%5D) 4 [Sacred Foundry](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 2 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Clifftop Retreat](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClifftop%5D+%5BRetreat%5D) 9 [Mountain](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Temple of Triumph](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 

60 Cards 

##### 1 (8)

4 [Crash Through](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrash%5D+%5BThrough%5D) 4 [Bag of Holding](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBag%5D+%5Bof%5D+%5BHolding%5D) 

##### 2 (14)

3 [Jaya's Greeting](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaya%5D+%5BGreeting%5D) 4 [Lightning Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BStrike%5D) 3 [Cathartic Reunion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCathartic%5D+%5BReunion%5D) 2 [Finale of Promise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFinale%5D+%5Bof%5D+%5BPromise%5D) 2 [Justice Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJustice%5D+%5BStrike%5D) 

##### 3 (2)

2 [Deafening Clarion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeafening%5D+%5BClarion%5D) 

##### 4 (8)

4 [Arclight Phoenix](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArclight%5D+%5BPhoenix%5D) 4 [Heartwarming Redemption](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeartwarming%5D+%5BRedemption%5D) 

##### 5 (3)

3 [Cavalier of Flame](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BFlame%5D) 

35 Cards 

##### Common (25)

4 [Crash Through](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrash%5D+%5BThrough%5D) 3 [Jaya's Greeting](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaya%5D+%5BGreeting%5D) 4 [Lightning Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BStrike%5D) 3 [Cathartic Reunion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCathartic%5D+%5BReunion%5D) 2 [Plains](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 9 [Mountain](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

##### Uncommon (8)

4 [Heartwarming Redemption](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeartwarming%5D+%5BRedemption%5D) 2 [Justice Strike](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJustice%5D+%5BStrike%5D) 2 [Cryptic Caves](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCaves%5D) 

##### Rare (18)

2 [Deafening Clarion](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeafening%5D+%5BClarion%5D) 4 [Bag of Holding](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBag%5D+%5Bof%5D+%5BHolding%5D) 4 [Sacred Foundry](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 4 [Clifftop Retreat](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClifftop%5D+%5BRetreat%5D) 4 [Temple of Triumph](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 

##### Mythic (9)

3 [Cavalier of Flame](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BFlame%5D) 4 [Arclight Phoenix](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArclight%5D+%5BPhoenix%5D) 2 [Finale of Promise](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFinale%5D+%5Bof%5D+%5BPromise%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crash+Through)

[Deal Another Hand](https://web.archive.org/web/20190726000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Deafening+Clarion)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Triumph)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sacred+Foundry)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Jaya%27s+Greeting)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clifftop+Retreat)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crash+Through)

a:17:{i:0;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Crash Through";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Jaya's Greeting";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Lightning Strike";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Cathartic Reunion";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Cavalier of Flame";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Arclight Phoenix";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Finale of Promise";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Heartwarming Redemption";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Justice Strike";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Deafening Clarion";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bag of Holding";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Cryptic Caves";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sacred Foundry";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Clifftop Retreat";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Temple of Triumph";s:22:"field\_card\_image\_front";a:0:{}}}} 

#### Abro's Scapeshift Aggro

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (24)

4 [Kitesail Freebooter](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKitesail%5D+%5BFreebooter%5D) 2 [Ravenous Chupacabra](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BChupacabra%5D) 4 [Dread Shade](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BShade%5D) 4 [Graveyard Marshal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGraveyard%5D+%5BMarshal%5D) 3 [Isareth the Awakener](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsareth%5D+%5Bthe%5D+%5BAwakener%5D) 4 [Dread Presence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BPresence%5D) 3 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 

##### Sorcery (4)

4 [Scapeshift](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScapeshift%5D) 

##### Instant (5)

3 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 2 [Vraska's Contempt](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVraska%5D+%5BContempt%5D) 

##### Enchantment (2)

2 [Arguel's Blood Fast](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArguel%5D+%5BBlood%5D+%5BFast%5D) 

##### Land (25)

4 [Temple of Malady](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalady%5D) 4 [Woodland Cemetery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BCemetery%5D) 4 [Overgrown Tomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOvergrown%5D+%5BTomb%5D) 13 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### Black (31)

3 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 4 [Kitesail Freebooter](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKitesail%5D+%5BFreebooter%5D) 2 [Ravenous Chupacabra](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BChupacabra%5D) 4 [Dread Shade](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BShade%5D) 4 [Graveyard Marshal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGraveyard%5D+%5BMarshal%5D) 3 [Isareth the Awakener](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsareth%5D+%5Bthe%5D+%5BAwakener%5D) 4 [Dread Presence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BPresence%5D) 2 [Vraska's Contempt](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVraska%5D+%5BContempt%5D) 2 [Arguel's Blood Fast](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArguel%5D+%5BBlood%5D+%5BFast%5D) 3 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 

##### Green (4)

4 [Scapeshift](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScapeshift%5D) 

##### Colorless (25)

4 [Temple of Malady](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalady%5D) 4 [Woodland Cemetery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BCemetery%5D) 4 [Overgrown Tomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOvergrown%5D+%5BTomb%5D) 13 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### 1 (3)

3 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 

##### 2 (10)

4 [Kitesail Freebooter](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKitesail%5D+%5BFreebooter%5D) 4 [Graveyard Marshal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGraveyard%5D+%5BMarshal%5D) 2 [Arguel's Blood Fast](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArguel%5D+%5BBlood%5D+%5BFast%5D) 

##### 3 (7)

4 [Dread Shade](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BShade%5D) 3 [Isareth the Awakener](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsareth%5D+%5Bthe%5D+%5BAwakener%5D) 

##### 4 (12)

2 [Ravenous Chupacabra](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BChupacabra%5D) 4 [Dread Presence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BPresence%5D) 2 [Vraska's Contempt](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVraska%5D+%5BContempt%5D) 4 [Scapeshift](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScapeshift%5D) 

##### 5 (3)

3 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 

35 Cards 

##### Common (13)

13 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

##### Uncommon (9)

3 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 4 [Kitesail Freebooter](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKitesail%5D+%5BFreebooter%5D) 2 [Ravenous Chupacabra](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BChupacabra%5D) 

##### Rare (31)

4 [Dread Shade](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BShade%5D) 4 [Graveyard Marshal](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGraveyard%5D+%5BMarshal%5D) 3 [Isareth the Awakener](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsareth%5D+%5Bthe%5D+%5BAwakener%5D) 4 [Dread Presence](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDread%5D+%5BPresence%5D) 2 [Vraska's Contempt](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVraska%5D+%5BContempt%5D) 2 [Arguel's Blood Fast](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArguel%5D+%5BBlood%5D+%5BFast%5D) 4 [Temple of Malady](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalady%5D) 4 [Woodland Cemetery](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWoodland%5D+%5BCemetery%5D) 4 [Overgrown Tomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOvergrown%5D+%5BTomb%5D) 

##### Mythic (7)

3 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 4 [Scapeshift](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScapeshift%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Disfigure)

[Deal Another Hand](https://web.archive.org/web/20190726000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dread+Shade)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Overgrown+Tomb)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dread+Presence)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scapeshift)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ravenous+Chupacabra)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Graveyard+Marshal)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kitesail+Freebooter)

a:15:{i:0;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Disfigure";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Kitesail Freebooter";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Ravenous Chupacabra";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Dread Shade";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Graveyard Marshal";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Isareth the Awakener";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Dread Presence";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Vraska's Contempt";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Arguel's Blood Fast";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Cavalier of Night";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Scapeshift";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Temple of Malady";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Woodland Cemetery";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Overgrown Tomb";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"13";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}} 

#### Abro's Loopy Reanimator

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (18)

2 [Scholar of the Ages](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScholar%5D+%5Bof%5D+%5Bthe%5D+%5BAges%5D) 3 [Gorging Vulture](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGorging%5D+%5BVulture%5D) 4 [Yarok's Fenlurker](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYarok%5D+%5BFenlurker%5D) 3 [Vilis, Broker of Blood](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVilis,%5D+%5BBroker%5D+%5Bof%5D+%5BBlood%5D) 2 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 4 [Tomebound Lich](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTomebound%5D+%5BLich%5D) 

##### Sorcery (12)

4 [Chart a Course](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChart%5D+%5Ba%5D+%5BCourse%5D) 2 [Blood for Bones](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5Bfor%5D+%5BBones%5D) 2 [Enter the God-Eternals](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnter%5D+%5Bthe%5D+%5BGod-Eternals%5D) 4 [Connive // Concoct](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConnive%5D+%5B&%5D+%5BConcoct%5D) 

##### Instant (5)

1 [Blink of an Eye](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlink%5D+%5Bof%5D+%5Ban%5D+%5BEye%5D) 2 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 2 [Tyrant's Scorn](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTyrant%5D+%5BScorn%5D) 

##### Land (25)

4 [Dismal Backwater](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BBackwater%5D) 4 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Drowned Catacomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BCatacomb%5D) 3 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 10 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### Blue (7)

1 [Blink of an Eye](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlink%5D+%5Bof%5D+%5Ban%5D+%5BEye%5D) 2 [Scholar of the Ages](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScholar%5D+%5Bof%5D+%5Bthe%5D+%5BAges%5D) 4 [Chart a Course](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChart%5D+%5Ba%5D+%5BCourse%5D) 

##### Black (16)

3 [Gorging Vulture](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGorging%5D+%5BVulture%5D) 2 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 4 [Yarok's Fenlurker](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYarok%5D+%5BFenlurker%5D) 2 [Blood for Bones](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5Bfor%5D+%5BBones%5D) 3 [Vilis, Broker of Blood](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVilis,%5D+%5BBroker%5D+%5Bof%5D+%5BBlood%5D) 2 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 

##### Multi colored (12)

4 [Tomebound Lich](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTomebound%5D+%5BLich%5D) 2 [Tyrant's Scorn](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTyrant%5D+%5BScorn%5D) 2 [Enter the God-Eternals](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnter%5D+%5Bthe%5D+%5BGod-Eternals%5D) 4 [Connive // Concoct](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConnive%5D+%5B&%5D+%5BConcoct%5D) 

##### Colorless (25)

4 [Dismal Backwater](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BBackwater%5D) 4 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Drowned Catacomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BCatacomb%5D) 3 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 10 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### 1 (2)

2 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 

##### 2 (11)

1 [Blink of an Eye](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlink%5D+%5Bof%5D+%5Ban%5D+%5BEye%5D) 4 [Chart a Course](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChart%5D+%5Ba%5D+%5BCourse%5D) 4 [Yarok's Fenlurker](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYarok%5D+%5BFenlurker%5D) 2 [Tyrant's Scorn](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTyrant%5D+%5BScorn%5D) 

##### 3 (7)

3 [Gorging Vulture](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGorging%5D+%5BVulture%5D) 4 [Tomebound Lich](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTomebound%5D+%5BLich%5D) 

##### 4 (2)

2 [Blood for Bones](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5Bfor%5D+%5BBones%5D) 

##### 5 (8)

2 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 2 [Enter the God-Eternals](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnter%5D+%5Bthe%5D+%5BGod-Eternals%5D) 4 [Connive // Concoct](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConnive%5D+%5B&%5D+%5BConcoct%5D) 

##### 7 (2)

2 [Scholar of the Ages](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScholar%5D+%5Bof%5D+%5Bthe%5D+%5BAges%5D) 

##### 8 (3)

3 [Vilis, Broker of Blood](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVilis,%5D+%5BBroker%5D+%5Bof%5D+%5BBlood%5D) 

35 Cards 

##### Common (21)

1 [Blink of an Eye](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlink%5D+%5Bof%5D+%5Ban%5D+%5BEye%5D) 3 [Gorging Vulture](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGorging%5D+%5BVulture%5D) 4 [Dismal Backwater](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BBackwater%5D) 3 [Island](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 10 [Swamp](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

##### Uncommon (20)

2 [Scholar of the Ages](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScholar%5D+%5Bof%5D+%5Bthe%5D+%5BAges%5D) 4 [Chart a Course](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChart%5D+%5Ba%5D+%5BCourse%5D) 2 [Disfigure](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 4 [Yarok's Fenlurker](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYarok%5D+%5BFenlurker%5D) 2 [Blood for Bones](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5Bfor%5D+%5BBones%5D) 4 [Tomebound Lich](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTomebound%5D+%5BLich%5D) 2 [Tyrant's Scorn](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTyrant%5D+%5BScorn%5D) 

##### Rare (17)

3 [Vilis, Broker of Blood](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVilis,%5D+%5BBroker%5D+%5Bof%5D+%5BBlood%5D) 2 [Enter the God-Eternals](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnter%5D+%5Bthe%5D+%5BGod-Eternals%5D) 4 [Connive // Concoct](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BConnive%5D+%5B&%5D+%5BConcoct%5D) 4 [Watery Grave](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Drowned Catacomb](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BCatacomb%5D) 

##### Mythic (2)

2 [Cavalier of Night](https://web.archive.org/web/20190726000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCavalier%5D+%5Bof%5D+%5BNight%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blink+of+an+Eye)

[Deal Another Hand](https://web.archive.org/web/20190726000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Connive+%2F%2F+Concoct)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vilis%2C+Broker+of+Blood)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dismal+Backwater)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gorging+Vulture)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Connive+%2F%2F+Concoct)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chart+a+Course)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dismal+Backwater)

a:18:{i:0;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Blink of an Eye";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Scholar of the Ages";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Chart a Course";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Gorging Vulture";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Disfigure";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Yarok's Fenlurker";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Blood for Bones";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Vilis, Broker of Blood";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Cavalier of Night";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Tomebound Lich";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Tyrant's Scorn";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Enter the God-Eternals";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Connive // Concoct";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Dismal Backwater";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Watery Grave";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Drowned Catacomb";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"10";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}} 

I'll be back once *Throne of Eldraine* rolls around to share some of my favorite Future Future League decks from the ELD FFL focus period. In the meantime, I'll be at most West Coast (best coast) *Magic* events. Come say hi!

—Abro  
[@Murk\_Lurker](http://www.twitter.com/Murk_Lurker)