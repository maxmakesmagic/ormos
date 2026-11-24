---
id: ra8rebp9
kind: article
lang: en
path: /en/articles/latestdevelopments/2007/02-09-one-foot-in-one-foot-out
title: One Foot In, One Foot Out
published: '2007-02-09'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: devinlow
  name: Devin Low
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    lang_detected: en
    capture_id: 729368
    url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    captured_at: '2022-01-24 23:20:25+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    lang_detected: en
    capture_id: 729368
    url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    captured_at: '2022-01-24 23:20:25+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    lang_detected: en
    capture_id: 729368
    url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    captured_at: '2022-01-24 23:20:25+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    lang_detected: en
    capture_id: 729368
    url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
    captured_at: '2022-01-24 23:20:25+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ra8rebp9
  url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
  lang: en
  template: drupal
  captured_at: '2022-01-24 23:20:25+00'
  capture_id: 729368
  wayback_url: https://web.archive.org/web/20220124232025id_/https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
- document_id: ra8rebp9
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af157&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af157
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:44:06+00'
  capture_id: 253114
  wayback_url: https://web.archive.org/web/20090604154406id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af157&print=true
- document_id: ra8rebp9
  url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09
  lang: en
  template: drupal
  captured_at: '2021-11-30 20:58:59+00'
  capture_id: 729366
  wayback_url: https://web.archive.org/web/20211130205859id_/https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09
- document_id: ra8rebp9
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af157&=RSS-MTGCOM
  page_key: wizards.com/default.asp?=RSS-MTGCOM&x=mtgcom/daily/af157
  lang: en
  template: classic_asp
  captured_at: '2007-03-02 01:56:56+00'
  capture_id: 1260901
  wayback_url: https://web.archive.org/web/20070302015656id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af157&=RSS-MTGCOM
- document_id: ra8rebp9
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af157
  page_key: wizards.com/default.asp?x=mtgcom/daily/af157
  lang: en
  template: classic_asp
  captured_at: '2008-03-24 14:59:26+00'
  capture_id: 1926589
  wayback_url: https://web.archive.org/web/20080324145926id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af157
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ra8rebp9
  capture_id: 729368
  url: https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
  wayback_url: https://web.archive.org/web/20220124232025id_/https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0
  captured_at: '2022-01-24 23:20:25+00'
  template: drupal
  sha256: b0377fe2cb1b955354e728bf3396d27cc9ea6e5a4837035543bc5a33bc340b4b
render_recovery: []
---
Hello!*Planar Chaos* lead developer Devin Low here, leaping at the chance to talk about some *Planar Chaos* development techniques while Aaron is out of the office. The development team knew going in that making the alternate color pie work would not be easy. We could set all the structure and color rules we wanted, but we knew the set would only be loved by the public if the color shifts "felt right." But how can you possibly make white counterspells and blue discard spells "feel right?" Fortunately, the design team discovered a technique to do just that: 

>  *To make a classic mechanic feel right in a new color, combine it with a dose of what you're used to in that color, creating a card that is part groundbreaking and part familiar.*

The development team loved the tactic, upheld it, and even deployed it on a couple more cards. The result is a group of cards that have one foot in Magic's classic color pie and one foot in the *Planar Chaos* alternate color pie – the best of both worlds. I'll focus first on how we applied this to white counterspells and blue discard spells and then take a quick spin exploring how we used the technique across the other colors.

### Something Old, Something New

![Rewind](https://i.ormos.uk/be/77/be777270b287bd4b044fbfa6f5800040f5f242449fb7fb85cf6c2aa5e711bb16.jpg)

We planned *Planar Chaos* very carefully, and when a major mechanic switches colors in the set, it always does so with at least three cards. Green flying? Three cards. Black tapping target creature? Three cards. Red bouncing enemy creatures? Three cards. That three-card-minimum helps ensure that specific mechanics move to specific places, and it's not just mass hysteria with every color doing everything. So when the design team pitched moving counterspells into white, we knew that it would have to be at least 3 cards. If you just picked a few random counterspells to move into white, you might end up with white [Rewind](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind), white [Spelljack](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spelljack), and white [Prohibit](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prohibit). If you think about opening those spells in a *Planar Chaos* pack, it would feel totally wrong. Why? Because each of those isn't just a counterspell, it's a very non-white-feeling counterspell.

[Rewind](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind) untaps 4 lands – not white at all.

[Spelljack](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spelljack) lets you steal your opponent's spell and hurl back at her – not white at all. 

[Prohibit](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prohibit) hates small spells – not white at all.

So what makes the white counterspells we did pick feel white?

**[Rebuff the Wicked](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked)**

![](https://i.ormos.uk/d8/17/d817a3b1d3f40f19d39558f1c29a8afdbd0a14eb566b715b8fbdd45aa85972f5.jpg)

The actual card [Counterspell](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) would be a jarring card to print in *Planar Chaos* White. There's nothing white about it. But [Rebuff the Wicked](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked) both plays into the white theme of "Protect my guys" and plays almost exactly like the common staple [Shelter](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shelter).If you cast [Rebuff the Wicked](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked), it "feels right" because you're doing something white always does. You're just using traditionally blue tools to do it.

**[Dawn Charm](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dawn+Charm)**

![](https://i.ormos.uk/24/4a/244ab211b4cd2ba25fc153fea3089e07b8a9c9511793c158549434f728878028.jpg)

Just as [Rebuff the Wicked](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked) replicates white's ability to protect its creatures, white's second counterspell embodies white's ability to protect itself. Just compare to the similar answer to burn spells and discard effects: [Gilded Light](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilded+Light). Put another way, [Dawn Charm](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dawn+Charm) is an instant [Ivory Mask](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Mask), giving a nice white feel to cushion the otherwise bizarre impact of a white [Counterspell](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell).

**[Mana Tithe](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Tithe)**

![](https://i.ormos.uk/78/fc/78fca02aa23ec291cf03b54911e9981b45b4cb7bd5fe5ef4a57c707f6055de26.jpg)

"Mana taxing" has been part of White's color pie for ages. Recent highlights include [Grand Arbiter Augustin IV](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grand+Arbiter+Augustin+IV), the techy [Suppression Field](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Suppression+Field), and the moving of [Propaganda](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Propaganda) into white as Ghostly Prison. But white mana taxing goes all the way back to the obscure [Glowrider](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glowrider), the powerful Aura of Silence, and even *The Dark*'s Brainwash. White's version of [Force Spike](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike) is basically an instant variant Aura of Silence. "Your spell costs one more mana. Oh, hadn't I mentioned that? Oh, you don't have any more mana to pay?"

What's that they say about death and taxes?

### Something Borrowed, Something Blue

Printing [Stupor](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stupor) in blue would be utterly bizarre. What would blue be doing with this random-discard spell? Instead, the blue discard spells have one foot in classic blue to give that comforting familiarity, even as the other foot's in the *Planar Chaos* alternate color pie of blue discard effects.

**[Wistful Thinking](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wistful+Thinking)**

![](https://i.ormos.uk/52/a6/52a6e551cd476fb29ed165147ef69a0d045bdd818950412a5b5200b27ae5fc21.jpg)

Blue has had card drawing/filtering spells like [Compulsive Research](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), [Careful Study](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Study), and [Merfolk Looter](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter) for years. Some, like [Compulsive Research](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), let you target another player to help an ally or deck an opponent. It's amazing how changing just the numbers and the targeting on [Sift](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift) transforms it from a card-filtering spell into a discard spell that often plays more like [Mind Rot](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot). Because you're used to blue getting "draw and discard" effects, it still feels blue. Want to see [Wistful Thinking](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wistful+Thinking) do something that [Mind Rot](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) can't? Just combine it with [Megrim](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Megrim).

**[Dismal Failure](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure)**

![](https://i.ormos.uk/c3/12/c3125835f283061ebbefe0cf2b39c135d807e463847fdc12b77f57610dc7b76f.jpg)

Tacking "discard a card" at the end of a vanilla spell seems like it would have to feel black, the color of [Ravenous Rats](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ravenous+Rats) and [Cackling Fiend](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cackling+Fiend). But [Dismal Failure](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure) is such a beautiful mirror of [Dismiss](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss) that it feels totally natural. Black Knight wouldn't normally get away with being a black two-mana 2/2 with two awesome abilities, but his symmetrical mirroring of [White Knight](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=White+Knight) makes it seem perfectly natural. [Call of the Herd](https://web.archive.org/web/20070209000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Call%2Bof%2Bthe%2BHerd)ed "Evil [Dismiss](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss)" during development and given its clever real name by the flavor text crew, [Dismal Failure](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure) is [Dismiss](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss)'s Black Knight.

**[Venarian Glimmer](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venarian+Glimmer)**

![](https://i.ormos.uk/29/fb/29fbd5789791f254711117f5befc8a85b111e95e707cf6e6644da2e9ad96d1f4.jpg)

This is one is awfully subtle. Once the observant figure it out, they tend to appreciate it. A blue coercion sounds like a stretch... maybe you can justify it by saying it combines blue telepathy with black discard? Sketchy. Things snap into focus when you hear its playtest name: "Proactive [Spell Blast](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Blast)" It's basically "[Spell Blast](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Blast) target spell... in your hand!" Having one foot in a well-known blue effect definitely helps this spell feel right.

### Highlight Reel

There isn't room to list every *Planar Chaos* card that used this technique. Let me quickly run you through some highlights from each color. If you look, you'll find a few more on your own.

**[Sunlance](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance)**

![](https://i.ormos.uk/38/c5/38c5e684f960cdf42a11efa4c89d27fa381e5a70b5e674922d7df56fc519138f.jpg)

Before [Time Spiral](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Spiral) Block, if you asked players what cards they expected to see printed in white, I very much doubt anyone would say "A white burn spell that deals 3 to a creature for one mana!" White weenie decks have been splashing mountains for red burn spells ever since "PT Jank" decks tore up Grand Prix on the back of [Soltari Priest](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Priest), all the way to today, with Boros Deck Wins living up to its name on the back of, well, [Soltari Priest](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Priest). So what makes this white creature-kill spell and its friends [Saltblast](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltblast) and [Serra's Boon](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra%27s+Boon) feel at home in white? All these cards hearken back to older spells like Holy Light, [Exile](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exile), [Blinding Light](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Light), and [Crackdown](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crackdown). [Sunlance](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance) follows in their footsteps... in a much more powerful way.

When the design team was searching for ways to do "Destroy target nonwhite creature" in *Planar Chaos* white, they looked to see what nostalgic spells they could tweak to get what they wanted. White [Dark Banishing](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) would be the simplest, but it just didn't "feel right." Instead the designers went back to a color-shifted [Strafe](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strafe) as [Sunlance](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance), a tweaked [Phyrexian Boon](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Boon) as [Serra's Boon](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra%27s+Boon), and a nonwhite-clause [Desert Twister](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+Twister) as [Saltblast](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltblast).

**[Saltfield Recluse](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltfield+Recluse)**

![](https://i.ormos.uk/e2/c2/e2c21891077658ac55860d9f32ce46f2f3271cdac0ecad9775bfbfdf3d78ea7d.jpg)

After years of appearing very rarely on cards, -X/-0 (or "shrink") has finally settled down in blue's color pie with recent cards like [Bewilder](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bewilder), [Meishin, the Mind Cage](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meishin%2C+the+Mind+Cage), and [Oboro Envoy](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oboro+Envoy). [Saltfield Recluse](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltfield+Recluse) "feels right" in white despite using a blue ability because it's doing something so clearly white in philosophy – protecting you and your creatures – and doing so in such a white way, with a little creature's free tap ability. Extra points if you recognized its numerical homage to classic powerful *Urza's Saga* draft common [Sanctum Custodian](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctum+Custodian).

**[Body Double](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Body+Double)**

![](https://i.ormos.uk/fe/c8/fec863a19bdf1bbcc3851d384a0dd260d2ad648d7ca904054cc21d16efb16810.jpg)

This one is pretty straightforward. How do you justify moving [Zombify](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) into blue? By making the [Zombify](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) effect actually a [Clone](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone) effect. With playtest name "Death Clone," we'd actually tried to put this card into earlier Magic sets in straight blue. *Planar Chaos*' color-shifting theme gave it the perfect home, as a blue card with one foot in blue and one foot in black.

**[Magus of the Coffers](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magus+of+the+Coffers)**

![](https://i.ormos.uk/11/1d/111d62df18a44b8a5fee8a7762903d7a0aabef032133f497132e522c4da26206.jpg)

A creature that taps to produce mana is the most iconic green color pie ability of all time, and almost zero nongreen creatures have ever had it. (Thank you, [Sisters of the Flame](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sisters+of+the+Flame).) But this card feels so right in black that hardly anyone even thinks of it as a color-shifted card at all. No one notices that it's mechanically closer to Rofellos than to any black creature.

**[Molten Firebird](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Molten+Firebird)**

![](https://i.ormos.uk/a3/71/a37190ec9d0dae36e65482857555100640bf1d2471068cb6ca6eda92ffa9466b.jpg)

If this card were a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 2/2 Spirit with the same abilities, it would seem ludicrously non-red, even in *Planar Chaos*. White, black, and green all contain mechanics and philosophies that deal with bringing the dead back to life or reincarnation, but red really doesn't at all – in "regular red" *or* "*Planar Chaos* red." Flying is also almost absent from both regular red and *Planar Chaos* red. So what is a flying reincarnator doing in red, either in *Planar Chaos* red or regular red? Why would we move Ivory Gargoyle here instead of to black? The flavor is the key. Phoenixes are such an iconic fantasy monster, and their abilities fit our game so well, that we love to express them mechanically as Magic cards. The fantasy flavor of Phoenixes is tightly so tied to fire, and fire is tied so tightly to Magic's red, that we've long made creatures like [Shard Phoenix](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shard+Phoenix) and Bogardan Phoenix red cards, even though their reincarnation and flying abilities otherwise have nothing to do with red mechanically. As both a reincarnator and a flier and a 2/2, Ivory Gargoyle's mechanics are the perfect fit to a red phoenix. The fact that red already has the [Jokulhaups](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jokulhaups) effects that made Ivory Gargoyle powerful is just gravy.

**[Utopia Vow](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow)**

![](https://i.ormos.uk/c8/fc/c8fc8bfa2ec4f5109458eac0609e5d610c277b0cd8c7eaddbb37f5f42b7c21e9.jpg)

Monogreen removal? The concept sounds weird at first, but most players find this card very natural as soon as they see it cast. The reason is that in gameplay it feels less like "Pacify your man," and more like "Turn your guy into a Bird of Paradise." What color should make things into [Utopia Tree](https://web.archive.org/web/20070209000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Tree)s? Green, of course.

So that's the story of how many color-shifted *Planar Chaos* cards were made to "feel right" by keeping one foot in the old color pie even as they stuck an exploratory foot into *Planar Chaos*' alternate color pie. Come back next week when Aaron returns from tromping his actual feet across a bunch of actual pies. (Yeah, he's twisted like that.)

![Serra Sphinx](https://i.ormos.uk/47/97/4797cc990fb8c9c5f2bcf5a04d86be5ca251c2db7703c4341f4afba890539907.jpg)