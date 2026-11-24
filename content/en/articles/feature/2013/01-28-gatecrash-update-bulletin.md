---
id: b2sw9zkb
kind: article
lang: en
path: /en/articles/feature/2013/01-28-gatecrash-update-bulletin
title: Gatecrash Update Bulletin
published: '2013-01-28'
column_slug: feature
column: Feature
authors:
- slug: matt-tabak-25905907
  name: Matt Tabak
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/231d
    lang_detected: en
    capture_id: 172449
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
    captured_at: '2013-02-01 08:49:40+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/231d
    lang_detected: en
    capture_id: 172449
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
    captured_at: '2013-02-01 08:49:40+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/231d
    lang_detected: en
    capture_id: 172449
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
    captured_at: '2013-02-01 08:49:40+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/231d
    lang_detected: en
    capture_id: 172449
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
    captured_at: '2013-02-01 08:49:40+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: b2sw9zkb
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/231d
  lang: en
  template: aspx
  captured_at: '2013-02-01 08:49:40+00'
  capture_id: 172449
  wayback_url: https://web.archive.org/web/20130201084940id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: b2sw9zkb
  capture_id: 172449
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
  wayback_url: https://web.archive.org/web/20130201084940id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=2
  captured_at: '2013-02-01 08:49:40+00'
  template: aspx
  sha256: 01dc6907c437a1c244bc0bf0eb23583b028288d3a022d2d265e3d51df2c62f61
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Gifts Ungiven
  - Intuition
  - Everbark Shaman
  - Far Wanderings
  - Kodama's Reach
  - Natural Balance
  - Primal Growth
  - Rites of Spring
  - Auriok Steelshaper
  - Howlpack Alpha
  - Immerwolf
  - Lovisa Coldeyes
  - Pallid Mycoderm
  - Cruel Fate
  - Darksteel Ingot
  - Hypersonic Dragon
  - Ink-Treader Nephilim
  - Common Bond
  - Vanish into Memory
  occurrences: 28
---
### Oracle Changes

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>What is Oracle?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <p>&#10;                    <b>Magic</b> is a game made up of more than 12,000 interchangeable pieces—the cards. Over the years, we've felt the need to update the wordings of older cards, whether because we've introduced a new keyword, or a card was printed with a mistake, or we have a clearer wording for what a card does, etc. Rather than sneak into your room at night and change your cards with a magic marker, we keep a database of the &quot;modern wordings&quot; (what the cards would say if we printed them today) of every tournament-legal card ever printed. These wordings are considered the official wordings of the cards, and accurately reflect their functions. </p>&#10;                  <p> You can access a card's Oracle wording by looking it up in <a href="https://web.archive.org/web/20130128000000/http://gatherer.wizards.com/pages/default.aspx">Gatherer</a>. </p>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

### New template: Searching for multiple cards with a specific quality (nonfunctional)

There's a rule that says if you're searching a library for cards with a specific quality, you don't have to find those cards, even if they're present in the library. Many players and judges call this the "fail to find" rule. For example, if you were searching your library for a creature card, but there were none in your library, without that rule a judge would have to confirm that you couldn't find what you were looking for. 

The problem is that with some cards not finding what you're looking for can actually be an advantage. Take Gifts Ungiven. A popular way to use this card is to just find two cards, not the full four. Because the card has you searching for cards with different names, the "specific quality" mentioned above, this is perfectly legal. Those two cards end up in your graveyard, but this isn't so much a drawback for Reanimator decks and the like. But it's easy to see that some players who don't know the rule would think this was suspect. So we're adding a helpful, non-functional "up to" on these cards, so even if you don't know the rule, the card's text will lead you to the right conclusion. 

Note that if you're instructed to search for some number of cards, with no specific qualities stated, you are required to find that number of cards if possible, so cards like Intuition are unaffected by this update. 

### Affected Cards:

> Everbark Shaman  
>  Far Wanderings  
>  Gifts Ungiven  
>  Kodama's Reach  
>  Natural Balance  
>  Primal Growth  
>  Rites of Spring

*Old wording:*  
 Same as the new wording, minus the "up to." 

*New wording:*  
 Same as the old wording, plus the "up to." 

See Gatherer for specific wordings. Man, Update Bulletins after the changes go live are fun! 

  

* * *

  

### New template: Abilities that care about creatures with at least one of multiple creature types (nonfunctional)

Some cards have abilities that give a bonus to a creature if it has at least one of multiple listed creature types. Take Auriok Steelshaper. The "and/or" construction can be confusing. What if the creature is both a Soldier and a Knight? Does it get the bonus twice? It was unclear. We came up with a new template that hopefully will make this unambiguous. 

### Affected cards:

### Auriok Steelshaper

*Old wording:*  
 Equip costs you pay cost {o1} less. As long as Auriok Steelshaper is equipped, Soldier and/or Knight creatures you control get +1/+1. 

*New wording:*  
 Equip costs you pay cost {o1} less.  
 As long as Auriok Steelshaper is equipped, each creature you control that's a Soldier or a Knight gets +1/+1. 

### Howlpack Alpha

*Old wording:*  
 Other Werewolf and Wolf creatures you control get +1/+1. At the beginning of your end step, put a 2/2 green Wolf creature token onto the battlefield. At the beginning of each upkeep, if a player cast two or more spells last turn, transform Howlpack Alpha. 

*New wording:*  
 Each other creature you control that's a Werewolf or a Wolf gets +1/+1.  
 At the beginning of your end step, put a 2/2 green Wolf creature token onto the battlefield.  
 At the beginning of each upkeep, if a player cast two or more spells last turn, transform Howlpack Alpha 

### Immerwolf

*Old wording:*  
 Intimidate *(This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)* Other Wolf and Werewolf creatures you control get +1/+1. Non-Human Werewolves you control can't transform. 

*New wording:*  
 Intimidate *(This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)*  
 Each other creature you control that's a Wolf or a Werewolf gets +1/+1.  
 Non-Human Werewolves you control can't transform. 

### Lovisa Coldeyes

Well, Lovisa was a bit weird. In fact, she probably deserves her own section. See below. 

### Pallid Mycoderm

*Old wording:*  
 At the beginning of your upkeep, put a spore counter on Pallid Mycoderm. Remove three spore counters from Pallid Mycoderm: Put a 1/1 green Saproling creature token onto the battlefield. Sacrifice a Saproling: Fungus and/or Saproling creatures you control get +1/+1 until end of turn. 

*New wording:*  
 At the beginning of your upkeep, put a spore counter on Pallid Mycoderm.  
 Remove three spore counters from Pallid Mycoderm: Put a 1/1 green Saproling creature token onto the battlefield.  
 Sacrifice a Saproling: Each creature you control that's a Fungus or a Saproling gets +1/+1 until end of turn. 

  

* * *

  

### Lovisa Coldeyes (functional)

Originally printed in *Coldsnap*, Lovisa united the Barbarian, Warrior, and Berserker tribes into a massive frenzy of beatdown. She was a Human Lord, but we've since eliminated Lord as a supported creature type. At the time, it felt weird for her to be a Human with no class (you know what I mean), so she was given an appropriate job: Barbarian. But wait a minute, she gave bonuses to Barbarians, and she wasn't meant to give herself a bonus without some help, so she needed new rules text. So then she affected other Barbarians, Warriors, and Berserkers. Well, with the new template concerning multiple creature types, this got even more awkward. 

A few options were debated, but we ultimately decided to just return her as close as possible to her original printing. Lord was a lost cause, but we've become increasingly comfortable with Creature – Human, and that felt like the best way to go. By the way, check out her flavor text. She crushes contraptions! What's not to love? 

*Old type line:*  
 Creature – Human Barbarian 

*Old wording:*  
 Warrior, Berserker, and/or other Barbarian creatures get +2/+2 and have haste. 

*New type line:*  
 Creature – Human 

*New wording:*  
 Each creature that's a Barbarian, a Warrior, or a Berserker gets +2/+2 and has haste. 

  

* * *

  

### Cruel Fate (nonfunctional)

An errant comma was removed. 

*Old wording:*  
 Look at the top five cards of target opponent's library. Put one of those cards into that player's graveyard, and the rest on top of his or her library in any order. 

*New wording:*  
 Look at the top five cards of target opponent's library. Put one of those cards into that player's graveyard and the rest on top of his or her library in any order. 

  

* * *

  

### Darksteel Ingot (nonfunctional)

There are several versions of the indestructible reminder text, and somehow Darksteel Ingot ended up with the wrong version. Our current policy says not to mention how damage may or may not affect an indestructible permanent that isn't a creature. The indestructible reminder text policy has evolved over the years, and this probably isn't the only card that could use an update. However, it's the most glaring, so it gets a fix this time around. 

*Old wording:*  
 Darksteel Ingot is indestructible. *("Destroy" effects and lethal damage don't destroy it.)* {oT}: Add one mana of any color to your mana pool. 

*New wording:*  
 Darksteel Ingot is indestructible. *(Effects that say "destroy" don't destroy it.)*  
 {oT}: Add one mana of any color to your mana pool. 

  

* * *

  

### Hypersonic Dragon (nonfunctional)

If an ability affects when you cast a spell or from what zone you can cast it from, it should refer to the "card," as it has to apply before you start the casting process. If an ability affects the cost to cast a spell, it should say "spell," as it applies once the card is already on the stack (and thus, a spell). Hypersonic Dragon inadvertently fell on the wrong side of the line. 

*Old wording:*  
 Flying, haste  
 You may cast sorcery spells as though they had flash. *(You may cast them any time you could cast an instant.)*

*New wording:*  
 Flying, haste  
 You may cast sorcery cards as though they had flash. *(You may cast them any time you could cast an instant.)*

  

* * *

  

### Ink-Treader Nephilim (functional… maybe? Who knows how it worked before?)

Rule 114.8 talks about three specific templates we use when we need to check what a spell or ability is targeting. And I mean specific. There are quotes and everything. Ink-Treader Nephilim had a unique template that didn't conform to any of them, so it wasn't entirely clear how it was supposed to behave if it wasn't on the battlefield when its triggered ability tried to resolve. With the new template, the answer is clear. If Ink-Treader Nephilim isn't on the battlefield when its triggered ability tries to resolve, no copies of the spell will be created. 

This is only tangentially relevant to this change, but here's a fun Ink-Treader Nephilim fact: Ink-Treader Nephilim can be targeted by an instant or sorcery spell multiple times, as long as it's the only target, and the spell will be copied. Common Bond is a great choice, and it's even in the Nephilim's colors! 

*Old wording:*  
 Whenever a player casts an instant or sorcery spell, if Ink-Treader Nephilim is the only target of that spell, copy the spell for each other creature that spell could target. Each copy targets a different one of those creatures. 

*New wording:*  
 Whenever a player casts an instant or sorcery spell, if that spell targets only Ink-Treader Nephilim, copy the spell for each other creature that spell could target. Each copy targets a different one of those creatures. 

  

* * *

  

### Vanish into Memory (nonfunctional)

The "its" in the last sentence was too ambiguous. The closest antecedent is "card," which could mistakenly point you to the card in exile. You're supposed to discard cards equal to the new creature's toughness when the delayed triggered ability resolves, and hopefully this new template is a tad clearer. 

*Old wording:*  
 Exile target creature. You draw cards equal to that creature's power. At the beginning of your next upkeep, return that card to the battlefield under its owner's control. If you do, discard cards equal to its toughness. 

*New wording:*  
 Exile target creature. You draw cards equal to that creature's power. At the beginning of your next upkeep, return that card to the battlefield under its owner's control. If you do, discard cards equal to that creature's toughness. 

  

* * *

  

> *   [Introduction](https://web.archive.org/web/20130128000000/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/231d&page=1)
> *   Oracle Changes
> *   [Comprehensive Rulebook Changes](/en/articles/feature/2013/01-28-gatecrash-update-bulletin-2)