---
id: 9ew9q0pj
kind: article
lang: en
path: /en/articles/latestdevelopments/2005/06-17-the-cost-of-arcane
title: The Cost of Arcane
published: '2005-06-17'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    lang_detected: en
    capture_id: 719946
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    captured_at: '2022-08-18 14:20:55+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    lang_detected: en
    capture_id: 719946
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    captured_at: '2022-08-18 14:20:55+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    lang_detected: en
    capture_id: 719946
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    captured_at: '2022-08-18 14:20:55+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    lang_detected: en
    capture_id: 719946
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
    captured_at: '2022-08-18 14:20:55+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 9ew9q0pj
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
  lang: en
  template: drupal
  captured_at: '2022-08-18 14:20:55+00'
  capture_id: 719946
  wayback_url: https://web.archive.org/web/20220818142055id_/https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
- document_id: 9ew9q0pj
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af71&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af71
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:44:56+00'
  capture_id: 253329
  wayback_url: https://web.archive.org/web/20090604154456id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af71&print=true
- document_id: 9ew9q0pj
  url: http://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17
  page_key: magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17
  lang: en
  template: drupal
  captured_at: '2016-03-26 03:25:56+00'
  capture_id: 719941
  wayback_url: https://web.archive.org/web/20160326032556id_/http://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17
- document_id: 9ew9q0pj
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af71
  page_key: wizards.com/default.asp?x=mtgcom/daily/af71
  lang: en
  template: classic_asp
  captured_at: '2008-03-24 15:06:11+00'
  capture_id: 1929433
  wayback_url: https://web.archive.org/web/20080324150611id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af71
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9ew9q0pj
  capture_id: 719946
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
  wayback_url: https://web.archive.org/web/20220818142055id_/https://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17-0
  captured_at: '2022-08-18 14:20:55+00'
  template: drupal
  sha256: b9524ff9004c9cc8a8a44613c0a5f6253e8bf5b2d9be42c5f4d3fd874c5313e9
render_recovery: []
---
Arcane spells have their own dirty little secret. I know most of you buy lots and lots of cards from us, or at least pay attention to them all, but there is a significant portion of the **Magic**-playing audience that experiences new sets a few packs or a few cards at a time. Some of them only spend $10-$20 on each new set, some of them acquire singles just by poking around in commons bins, and most of them don't read the Internet regularly. So let's say you're one of those people. You open your three packs and you see these cards:

Now, without any context, what do you think of these cards? One is [Boomerang](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boomerang), but a sorcery. One is [Fallow Earth](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fallow+Earth), but one mana more. And the last is [Demolish](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demolish), but double red. All have the subtype “Arcane,” but that doesn't appear to mean anything!

That's the dirty little secret—having Arcane on a card's typeline isn't “free,” yet the benefits of it aren't readily apparent. That's not a great place to be in from a design and development standpoint.

Of course, sometimes the original spell is enough “below the curve” that we were able to tack on Arcane essentially for free—[Demystify](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demystify), [Fugue](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fugue), and [Mind Rot](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) are now [Quiet Purity](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quiet+Purity), [Three Tragedies](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Three+Tragedies), and [Waking Nightmare](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waking+Nightmare). That serves to hide the initial problem, but that problem is still evident. Brandon Bozzi of the creative team once told me a story of a discussion he had with his **Magic**-playing friends from back home in New Jersey that they couldn't for the life of them figure out why in the world we made [Reach through Mists](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists). What good is a card that does nothing else but draw another card?!

Of course, most of you know by now that [Reach through Mists](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists) can (a) help summon forth [The Unspeakable](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Unspeakable), (b) be a splice outlet for cards like [Glacial Ray](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Ray) and [Dampen Thought](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dampen+Thought), and (c) trigger “spiritcraft” abilities like those on [Teller of Tales](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teller+of+Tales) and [Thief of Hope](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thief+of+Hope). But none of that is obvious when you open your pack.

### Parasitism, Good and Bad

 

![Auriok Glaivemaster](https://i.ormos.uk/9a/b9/9ab99da09f4eb87f985af6e51169ba6471f2d2afec503936a4ee24d8615b2976.jpg)

We throw the term “parasitism” around in R&D a lot. To us it means: “when a card's value is solely dependent on other cards in the same set or block.” In other words, cards that are parasitic have little or no use when mixed with cards from throughout **Magic's** past, but are key components to some larger puzzle in the block in which they were printed. Some parasitic cards, like *Darksteel's* [Auriok Glaivemaster](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Glaivemaster), are obviously so, as they call out the name of the card type or mechanic they need to work with. Others, like *Odyssey's* [Tireless Tribe](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tireless+Tribe), just look really bad until you start seeing potential interactions with flashback, madness, and threshold.

There's gray area as well. [Sosuke's Summons](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sosuke%27s+Summons), for instance, needs Snakes to work well, and there have been a handful of Snakes printed prior to this block. So at least you could in theory build a deck that used it without overloading on Kamigawa cards. But the *best* way to make the card work involves lots and lots of cards from *Champions* and *Betrayers*. Cards with “affinity for artifacts” are the same way. Sure, [Frogmite](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frogmite) only costs 3 when you have a [Bronze Horse](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bronze+Horse) in play, but the obvious way to use the card is with tons of artifact lands. Are those cards really considered parasitic? Technically I guess not, but they sure feel like it.

There's a lot of good that comes from making parasitic cards. Limited formats (sealed deck and draft) feel different from one another when their main themes are lineal, which often implies some level of parasitism. The *Odyssey* UG threshold draft deck feels and plays different from the *Onslaught* WB Cleric deck, the *Mirrodin* UB affinity deck, and the *Kamigawa* UR splice deck. We want different game play from year to year, and one way to accomplish that is by making one zone or card type matter more, and then printing linear (sometimes parasitic) cards that focus on that zone or type.

Block Constructed (and, to an extent, Standard) varies in the same way. Sometimes the block is slow and plodding and filled with giant spells, like the current one, and sometimes it's really fast, like *Odyssey* and *Mirrodin*. And even then, the slow decks feel different than one another—Astral Slide decks and Gifts Ungiven decks are completely separate animals.

The downside of parasitism is what I was talking about in the introduction. If you aren't drafting or playing Standard or Block, the cards can be kind of “meh.” But why?

### Incurring the Cost

Looking just at the *Kamigawa* Arcane stuff, enfranchised players should be able to see that when the ball gets rolling, it gets rolling well. I can play [Reach through Mists](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists) with a [Glacial Ray](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Ray) spliced onto it which triggers my [Soilshaper](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soilshaper) and my [Elder Pine of Jukai](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elder+Pine+of+Jukai). Not unheard of in limited games. So for basically no real cost other than a few mana—the Ray is still in my hand, and I've drawn a card to replace the Reach—I have done 2 damage to something, animated a land, and potentially netted up to three extra cards from Mr. Jukai.

These abilities cannot all be given away for free—the cost for such potential power has to be incurred somewhere. Sometimes the creatures with spiritcraft have to cost a little more, sometimes splice cards have to cost a little more, and sometimes the normal run-of-the-mill Arcane cards incur the cost. We mix it up on purpose, so that one category of cards isn't “all above the curve” whereas the other is “all bad.”

These abilities cannot all be given away for free—the cost for such potential power has to be incurred somewhere.

So when Arcane ends up costing some fraction of a mana, some fraction of the Arcane cards end up costing a mana more than what you might expect. That's where [Uproot](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Uproot), [First Volley](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Volley), and other similar cards come in. Yes, they unfortunately look bad on the surface, but as you dig deeper into the set we can only hope you understand why.

### Brand New Effects

Of course, my favorite way of hiding the cost of being Arcane is by making cards with abilities that haven't existed before so that no direct comparison is available. Look at cards like [Petals of Insight](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Petals+of+Insight), [Cranial Extraction](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cranial+Extraction), and [Rending Vines](https://web.archive.org/web/20050617000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rending+Vines). Which of those, if any, costs more to play simply because it's Arcane? (Hint: not Extraction.) The answer is well hidden, since in theory these cards could have these costs even if they weren't Arcane—who's to know?

Unfortunately we can't reinvent the wheel every time. Every block needs enchantment removal, simple discard, pump spells, land destruction and the like. Some of them got tweaked a little from previously released versions, some were given splice, and some were simply made Arcane.

And the funny thing is, even though some of them cost more than you're used to, it's often worth it… as long as you're playing the right deck.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>How do you feel about the number of new cards released each year?</b></th>&#10;		</tr></thead><tbody><tr><td>We release about the right number of new cards per year.</td>&#10;			<td>6787</td>&#10;			<td>50.3%</td>&#10;		</tr><tr><td>We release too many new cards per year.</td>&#10;			<td>3047</td>&#10;			<td>22.6%</td>&#10;		</tr><tr><td>We release too few new cards per year.</td>&#10;			<td>2511</td>&#10;			<td>18.6%</td>&#10;		</tr><tr><td>We release WAY too many new cards per year.</td>&#10;			<td>1156</td>&#10;			<td>8.6%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>13501</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

Every so often we revisit how many cards we're making and if that is meeting players' needs. It looks like the people that think we make too many cards are in the minority, but a sizeable minority at that. Good to know.