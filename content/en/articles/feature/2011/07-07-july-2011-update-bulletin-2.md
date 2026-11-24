---
id: 9c46j2mh
kind: article
lang: en
path: /en/articles/feature/2011/07-07-july-2011-update-bulletin-2
title: July 2011 Update Bulletin
published: '2011-07-07'
column_slug: feature
column: Feature
authors:
- slug: matt-tabak-25905907
  name: Matt Tabak
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/150b
    lang_detected: en
    capture_id: 172378
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
    captured_at: '2011-08-11 10:56:37+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/150b
    lang_detected: en
    capture_id: 172378
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
    captured_at: '2011-08-11 10:56:37+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/150b
    lang_detected: en
    capture_id: 172378
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
    captured_at: '2011-08-11 10:56:37+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/150b
    lang_detected: en
    capture_id: 172378
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
    captured_at: '2011-08-11 10:56:37+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 9c46j2mh
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/150b
  lang: en
  template: aspx
  captured_at: '2011-08-11 10:56:37+00'
  capture_id: 172378
  wayback_url: https://web.archive.org/web/20110811105637id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9c46j2mh
  capture_id: 172378
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
  wayback_url: https://web.archive.org/web/20110811105637id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=2
  captured_at: '2011-08-11 10:56:37+00'
  template: aspx
  sha256: bdf2aa13728d05e303dd37c3ff01ef4c5f42d9b01d6e0ebc774f5dd0ae8b04ec
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Heartwood Dryad
  - Wall of Diffusion
  - Ætherflame Wall
  - Æther Web
  - Tithe
  - Land Tax
  - Knight of the White Orchid
  - Rally the Horde
  - Priest of Yawgmoth
  - Sacrifice
  - Soldevi Adnate
  - Viridian Joiner
  - Sleight of Mind
  occurrences: 31
---
### Functional Oracle Changes

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;                 <b>What is Oracle?</b></td>&#10;            <td> </td>&#10;            <td>&#10;              <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;            </td>&#10;          </tr>&#10;          <tr>&#10;            <td colspan="3">&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                    <p>&#10;                      <b>Magic</b> is a game made up of over 11,000 interchangeable pieces—the cards. Over the years, we've felt the need to update the wordings of older cards, whether because we've introduced a new keyword, or a card was printed with a mistake, or we have a clearer wording for what a card does, etc. Rather than sneak into your room at night and change your cards with a magic marker, we keep a database of the &quot;modern wordings&quot; (what the cards would say if we printed them today) of every tournament-legal card ever printed. These wordings are considered the official wordings of the cards, and accurately reflect their functions.</p>&#10;                    <br>&#10;                    <p>You can access a card's Oracle wording by looking it up in <a href="https://web.archive.org/web/20110707000000/http://gatherer.wizards.com/Pages/Default.aspx">Gatherer</a>.</p>&#10;                    <br>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

 **Heartwood Dryad and Wall of Diffusion**  
 These two *Tempest* cards were built to walk between worlds, able to block both creatures with shadow and those without. *Time Spiral* came along and brought us Ætherflame Wall and Æther Web, complete with a fancy new "as though" template. The two *Tempest* cards adopted this new template, and all was well.

Unfortunately, that introduced a small functional change to the two *Tempest* cards. If Ætherflame Wall gains shadow, it becomes unable to block any attacking creature. If the attacker has shadow, you treat it as though it doesn't, and now Ætherflame Wall can't block it (as it has shadow). If the attacker doesn't have shadow, Ætherflame Wall can't block it (yep, still has shadow). The same is true for any creature enchanted by Æther Web. This functionality was intended and explained in the *Time Spiral* FAQ.

But the *Tempest* cards shouldn't have been saddled with that drawback. The printed wording on each clearly states it's able to block creatures with shadow regardless of its own current shadowiness. So, we've altered their wordings to undo that change.

*New Heartwood Dryad wording:*  
 Heartwood Dryad can block creatures with shadow as though Heartwood Dryad had shadow.

*New Wall of Diffusion wording:*  
 Defender *(This creature can't attack.)*  
 Wall of Diffusion can block creatures with shadow as though Wall of Diffusion had shadow.

 **Tithe**  
 The printed card targets an opponent. Somewhere along the way, this fact was... Ignored? Forgotten? I don't know. But we're restoring it. Also, most cards that ask you to compare lands controlled used the format "if \[someone\] controls more \[something\] than you." Tithe went about this the other way, saying "if you control fewer lands than an opponent." Now it'll use the same template that cards like Land Tax and Knight of the White Orchid do.

*New Tithe wording:*  
 Search your library for a Plains card. If target opponent controls more lands than you, you may search your library for an additional Plains card. Reveal those cards and put them into your hand. Then shuffle your library.

 **Rally the Horde**  
 This one isn't a functional change, per se, but it turns out this card may not have really, um... worked before. This card instructed you to exile the top three cards of your library and then look at the "last card exiled." But the three cards are exiled at the same time, so there isn't a "last card." There were several options to fix this, but this new wording did the best job of unambiguously pointing at the right card, even if there were two or fewer cards left in your library.

*New Rally the Horde wording:*  
 Exile the top card of your library. Exile the top card of your library. Exile the top card of your library. If the last card exiled isn't a land, repeat this process until the last card exiled is a land. Put a 1/1 red Warrior creature token onto the battlefield for each nonland card exiled this way.

 **Priest of Yawgmoth, Sacrifice, Soldevi Adnate, Viridian Joiner**  
 These cards all add "an amount of" some color of mana to your mana pool. Early cards spelled it out using the color word. For example, Sacrifice's printed wording referred to "a number of black mana." More recently, Viridian Joiner was printed with a template that added "an amount of ![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)" to your mana pool.

In almost all cases, "black mana" and "![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)" are equivalent. The one time they're not? When cards like Sleight of Mind are involved. We previously decided that under modern templating guidelines, we wouldn't allow the interaction between Sleight of Mind and descriptions of colored mana. But these four cards were kind of all over the map. Soldevi Adnate's Oracle wording even went the other way, using "black mana" even though it used the mana symbol as printed. We're going forward following Viridian Joiner's lead.

In addition, I rearranged some words so they all use similar templates.

*New Priest of Yawgmoth wording:*  
 {oT}, Sacrifice an artifact: Add to your mana pool an amount of {oB} equal to the sacrificed artifact's converted mana cost.

*New Sacrifice wording:*  
 As an additional cost to cast Sacrifice, sacrifice a creature.  
 Add to your mana pool an amount of {oB} equal to the sacrificed creature's converted mana cost.

*New Soldevi Adnate wording:*  
 {oT}, Sacrifice a black or artifact creature: Add to your mana pool an amount of {oB} equal to the sacrificed creature's converted mana cost.

*New Viridian Joiner wording:*  
 {oT}: Add to your mana pool an amount of {oG} equal to Viridian Joiner's power.

> *   [Introduction](https://web.archive.org/web/20110707000000/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/150b&page=1)
> *   Functional Oracle Changes
> *   [Nonfunctional Oracle Changes](/en/articles/feature/2011/07-07-july-2011-update-bulletin)
> *   [Comprehensive Rulebook Changes](/en/articles/feature/2011/07-07-july-2011-update-bulletin-5)