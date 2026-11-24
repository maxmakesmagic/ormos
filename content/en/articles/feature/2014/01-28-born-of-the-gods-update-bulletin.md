---
id: 8na6q9t4
kind: article
lang: en
path: /en/articles/feature/2014/01-28-born-of-the-gods-update-bulletin
title: Born of the Gods Update Bulletin
published: '2014-01-28'
column_slug: feature
column: Feature
authors:
- slug: matt-tabak-25905907
  name: Matt Tabak
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/284b
    lang_detected: en
    capture_id: 172309
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
    captured_at: '2014-05-11 05:30:53+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/284b
    lang_detected: en
    capture_id: 172309
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
    captured_at: '2014-05-11 05:30:53+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/284b
    lang_detected: en
    capture_id: 172309
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
    captured_at: '2014-05-11 05:30:53+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/284b
    lang_detected: en
    capture_id: 172309
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
    captured_at: '2014-05-11 05:30:53+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 8na6q9t4
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/284b
  lang: en
  template: aspx
  captured_at: '2014-05-11 05:30:53+00'
  capture_id: 172309
  wayback_url: https://web.archive.org/web/20140511053053id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 8na6q9t4
  capture_id: 172309
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
  wayback_url: https://web.archive.org/web/20140511053053id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/284b&page=2&print=true
  captured_at: '2014-05-11 05:30:53+00'
  template: aspx
  sha256: d1799eaf96580f4686aba3ac1aaaf64197b3748ad5b0cfa32bd020111bf26341
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Blind Fury
  - Blood Frenzy
  - Bloodletter Quill
  - Burning of Xinye
  - Cloudstone Curio
  - Creeping Renaissance
  - Goblin Warchief
  - Opal Palace
  - Psychic Battle
  occurrences: 21
---
### Oracle Changes

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>What is Oracle?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <p>&#10;                    <b>&#10;                      <b>Magic</b>&#10;                    </b> is a game made up of more than 13,000 interchangeable pieces—the cards. Over the years, we've felt the need to update the wordings of older cards, whether because we've introduced a new keyword, or a card was printed with a mistake, or we have a clearer wording for what a card does, etc. Rather than sneak into your room at night and change your cards with a magic marker, we keep a database of the &quot;modern wordings&quot; (what the cards would say if we printed them today) of every tournament-legal card ever printed. These wordings are considered the official wordings of the cards, and accurately reflect their functions. </p>&#10;                  <p> You can access a card's Oracle wording by looking it up in <a href="https://web.archive.org/web/20140128000000/http://gatherer.wizards.com/pages/default.aspx">Gatherer</a>. </p>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

### Blind Fury (functional)

Before *Mirage* was released on **Magic Online**, Blind Fury was given a restriction to when you could cast it, specifically before the combat damage step. This was to prevent you from putting combat damage on the stack and then casting Blind Fury in response, before combat damage resolved. If you did this, the fact that creatures lost trample wouldn't matter as combat damage had already been potentially assigned to players from blocked creatures with trample. You would still get the bonus of all combat damage assigned to creatures being doubled. Basically, the rules structure of pre-*M10* allowed you to evade the clearly intended drawback of Blind Fury, something the rules structure when *Mirage* was first printed didn't allow. 

However, now that combat damage no longer uses the stack, this timing restriction is unnecessary. If you cast Blind Fury before the combat damage step, the spell will work as intended. If you cast it during or after the combat damage step, basically nothing will happen (except possibly if there are multiple combats, but even then you get what you expect). So, we're removing the timing restriction. 

As a side note, a few other cards, such as Blood Frenzy, were given similar restrictions so you couldn't evade their intended drawbacks, but because of the nature of their effects, removing those restrictions would essentially create different cards. This is something we're not interested in, so those cards are being left alone. 

*Old wording:* 

Cast Blind Fury only before the combat damage step.  
 All creatures lose trample until end of turn. If a creature would deal combat damage to a creature this turn, it deals double that damage to that creature instead.

*New wording:* 

All creatures lose trample until end of turn. If a creature would deal combat damage to a creature this turn, it deals double that damage to that creature instead.

  

* * *

  

### Bloodletter Quill (nonfunctional)

It's standard to always specify who is losing life. This card was missing a "you."

*Old wording:* 

![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif) , ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif), Put a blood counter on Bloodletter Quill: Draw a card, then lose 1 life for each blood counter on Bloodletter Quill.  
![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif): Remove a blood counter from Bloodletter Quill. 

*New wording:* 

![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif) , ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif), Put a blood counter on Bloodletter Quill: Draw a card, then you lose 1 life for each blood counter on Bloodletter Quill.  
![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif): Remove a blood counter from Bloodletter Quill. 

  

* * *

  

### Burning of Xinye (functional, but a reversal)

In the *Innistrad* update, I updated this card in an effort to clarify who was doing what and when. Unfortunately, I accidentally introduced a functional change with respect to lands with indestructible. Ah, the frivolity of youth. Um... let's just go back to the last wording. \*waves hands\* Nothing to see here. 

*Old wording:* 

Choose four lands you control and destroy those lands. Then target opponent chooses four lands he or she controls. Destroy those lands. Then Burning of Xinye deals 4 damage to each creature. 

*New (and yet old) wording:* 

You destroy four lands you control, then target opponent destroys four lands he or she controls. Then Burning of Xinye deals 4 damage to each creature. 

  

* * *

  

### Cloudstone Curio (functional)

Back in 2007, the text of this card changed from "permanent type" to "card type." "Permanent type" was described at the time as an obsolete term. However, the term stuck around in the rules. When it came time to template *Innistrad*, we dug the term out of the mothballs to use on Creeping Renaissance. Given that it's a valid term, we should put it back on Cloudstone Curio to undo the functional change. 

What functional change? Well, cards can share a card type without sharing a permanent type thanks to the ongoing bounty of wonderfulness that is tribal. A Tribal Enchantment – Goblin and a Tribal Artifact – Soldier Equipment share a card type (tribal) and could previously be affected by Cloudstone Curio. But they don't share a permanent type (tribal isn't one), and now they won't be. 

*Old wording:* 

Whenever a nonartifact permanent enters the battlefield under your control, you may return another permanent you control that shares a card type with it to its owner's hand.

*New wording:* 

Whenever a nonartifact permanent enters the battlefield under your control, you may return another permanent you control that shares a permanent type with it to its owner's hand.

  

* * *

  

### Goblin Warchief (functional)

Goblin Warchief, originally printed in *Scourge*, also joined his brethren in the very first *Duel Decks: Elves vs. Goblins*. At that time, its creature types were updated to Goblin Warrior. Not only is he called a Warchief, but he's in a very war-like posture. And check out that stick! Unfortunately, this change was accidentally left out of Oracle and lost to time. Well, time's up, because I noticed. I'll just make that Oracle update now, I suppose. 

*Old creature types:* 

Goblin

*New creature types:* 

Goblin Warrior

  

* * *

  

### Opal Palace (nonfunctional)

This *Commander* (2013 Edition) card was missing an "additional." That word is helpful but not necessary, so this isn't a functional change. 

*Old wording:* 

![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif) : Add ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) to your mana pool.  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Add to your mana pool one mana of any color in your commander's color identity. If you spend this mana to cast your commander, it enters the battlefield with a number of +1/+1 counters on it equal to the number of times it's been cast from the command zone this game. 

*New wording:* 

![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif) : Add ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) to your mana pool.  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Add to your mana pool one mana of any color in your commander's color identity. If you spend this mana to cast your commander, it enters the battlefield with a number of additional +1/+1 counters on it equal to the number of times it's been cast from the command zone this game. 

  

* * *

  

### Psychic Battle (functional)

The last line of Psychic Battle's old wording was added quickly after the card was released to prevent immediately drawing the game every time. Given that you choose new targets when you change them, Psychic Battle's ability would just trigger itself, over and over and over again. Although the added line took care of the problem for one Psychic Battle, two or more Psychic Battles would still draw the game by causing each other to trigger *ad infinitum*. This was a templating oversight at the time, which we can now button up. 

*Old wording:* 

Whenever a player chooses one or more targets, each player reveals the top card of his or her library. The player who reveals the card with the highest converted mana cost may change the target or targets. If two or more cards are tied for highest cost, the target or targets remain unchanged. Changing targets this way doesn't trigger this ability.

*New wording:* 

Whenever a player chooses one or more targets, each player reveals the top card of his or her library. The player who reveals the card with the highest converted mana cost may change the target or targets. If two or more cards are tied for highest cost, the target or targets remain unchanged. Changing targets this way doesn't trigger abilities of permanents named Psychic Battle. 

> *   [Introduction](/en/articles/feature/2014/01-28-born-of-the-gods-update-bulletin-2)
> *   Oracle Changes
> *   [Comprehensive Rulebook Changes](/en/articles/feature/2014/01-28-born-of-the-gods-update-bulletin-3)