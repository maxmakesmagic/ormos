---
id: 4ygnwfvr
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/03-25-skeletons-in-r-amp-ds-closet-part-2
title: Skeletons in R&amp;D's Closet, Part 2
published: '2011-03-25'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    lang_detected: en
    capture_id: 734642
    url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    captured_at: '2016-07-25 14:03:07+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    lang_detected: en
    capture_id: 734642
    url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    captured_at: '2016-07-25 14:03:07+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    lang_detected: en
    capture_id: 734642
    url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    captured_at: '2016-07-25 14:03:07+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    lang_detected: en
    capture_id: 734642
    url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
    captured_at: '2016-07-25 14:03:07+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 4ygnwfvr
  url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
  lang: en
  template: drupal
  captured_at: '2016-07-25 14:03:07+00'
  capture_id: 734642
  wayback_url: https://web.archive.org/web/20160725140307id_/http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 4ygnwfvr
  capture_id: 734642
  url: http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
  wayback_url: https://web.archive.org/web/20160725140307id_/http://magic.wizards.com/en/articles/archive/latest-developments/skeletons-rds-closet-part-2-2011-03-25
  captured_at: '2016-07-25 14:03:07+00'
  template: drupal
  sha256: 5bd5223dde1452b5adf015221d52795185059d44f65ac86cfbc46532f35b637e
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 1
---
A little over seven years ago, then-Latest Developments author Aaron Forsythe wrote an article entitled [Skeletons in R&D's Closet](/en/articles/latestdevelopments/2004/02-20-skeletons-in-r-ds-closet). In it, he shared Multiverse comments that developers left on some of **Magic**'s most famously broken cards: [Survival of the Fittest](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest), [Oath of Druids](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oath+of+Druids), [Tolarian Academy](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy), [Yawgmoth's Will](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Will), and others. Here's how he ended that article:

> Of course, nobody's perfect. I'm sure ten years from now a new group of developers will look back at some of the cards we've made in recent years and say, "What were they thinking?!" I just hope they don't write an article about it.

Aaron wrote this fourteen days after *Darksteel*'s release date.

It's Mirrodin Week.

Let's do this.

![](https://i.ormos.uk/ac/e8/ace8b498cf79b662248fa67df62b0b16253ba769363dd00468517aae6f8559ea.jpg)

We'll start with an appetizer. [Thirst for Knowledge](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge) is hardly the least offensive of the cards in this article. Despite that, it saw heavy play through all of its lifetime in Standard and Extended, and was powerful enough in Vintage thanks to the Moxes that the DCI chose to restrict it when [Mana Drain](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) decks were a dominating force. Let's see what R&D said about it before it was printed. One note: In this example and throughout the article, I've changed the initials of those involved to D1, D2, etc. to protect their identities. I still work with some of these people, after all…

> D1 9/9: make an instant?  
>  D2 (9/11/02): This card was originally an instant but was changed to a sorcery since it is at times a card drawing card.

An astute development comment!

> D3 9/12 It is actually a really good card drawing card with the artifact lands.  
>  D4 9/14 Agreed, this is card drawing, not filtering

I'm glad they figured that out, at least.

> D5 9/16: team prefers at common (was uc ... briefly)

I can't imagine drafting with this as a common. By that, I mean that I can imagine drafting blue over and over if this was a common.

> D4 9/27 test me

Compared to the rest of the cards here, this one probably seemed just fine.

![](https://i.ormos.uk/ab/54/ab54fa4aa7f5b53f9a04e668c65face0268e55e00c2309e9cbcc7b17934a9541.jpg)

[Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) was one of two key cards that fuelled the artifact attack deck that dominated Standard soon after *Darksteel* released, which was popularly called "Affinity" even though the most powerful cards in the deck lacked that keyword. When you can play 45 artifacts in a 60-card deck and a bunch of ways to sacrifice artifacts at will, this card was frequently a one-mana double [Lava Axe](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe).

R&D likes pondering hypothetical questions. One of them is what single **Magic** card we would go back in time to remove from **Magic** forever. [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) is the third most common answer from developers. (The other two will appear later.)

Let's see what the *Mirrodin* developers have to say for themselves.

> D1 10/15: new card, needed a cheap creature and thought it would be cute to mirror the new white soul warden

Cute?

> D2 10/17 push

Really?

> D1 11/26: trimming a mana to mirror white change

Oh no.

I am certain that the aesthetic benefit of mirroring [Leonin Elder](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Elder) and [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) at one mana weren't worth the players we lost to the deck this change spawned.

![](https://i.ormos.uk/f8/2d/f82d577e2360d3efbc52fca002154e2d9f9cb101eacdb4046a92d4977eae596c.jpg)

We now have found our first card with the actual affinity ability. How much discussion was there about this creature, which is potentially a zero-mana 2/2?

> D1 10/18: new card, teams wants enough potentially free guys to motivate people to build a deck around them

Mission accomplished!

![](https://i.ormos.uk/96/28/9628457d89e5a9bce6982b5ab32ef2a906fbfac53e3e8f1fe7e73a2b6ebb084d.jpg)

> D1 9/14 I think the fact that this guy \*could\* cost 0 mana is Johnnyriffic.  
>  D2 9/22: going back up to 8-mana  
>  D1 10/17 push  
>  D2 10/18: trimming a mana to push, but moving to UC because he was already good in Limited  
>  D2 11/27: moving down to common so artifact creatures and affinity are better  
>  D2 1/2: we should test some more and see exactly where the level of artifact creatures is

1) This card's potential cost of zero is also as Spikeriffic as it gets.  
 2) The level of artifact creatures is high.

Let's pause for a moment to appreciate how difficult affinity is to deal with as a developer. We have learned that cards that are powerful but read poorly are a great recipe for getting bad initial buzz about a set. We have also learned that keyword mechanics that are much stronger than they look create cards that read poorly. Affinity is one such mechanic, so the developers were under some awkward pressure to find exactly the right balance between appropriate card power and cards that are appealing to read. That's not a great spot to be in, and I don't envy their position.

![](https://i.ormos.uk/66/f4/66f4a36aa2baadca7e015a47e9fc6af16a57475a04e830fcf60c28d1a3cb98c0.jpg)

[Goblin Charbelcher](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Charbelcher) looks like a cute and goofy card. In reality, it's a little bit of a monster, enabling Extended combination decks that won on turn two or three at [Pro Tour New Orleans](/en/articles/event-coverage/2003/11-02-live-coverage-of-2003-pro-tour-new-orleans) in 2003 by casting [Mana Severance](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Severance). You can also win on turn one or two in Legacy and Vintage by playing one or zero lands in your deck thanks to those formats' copious fast mana. There is exactly one comment on the card. Let's have a look:

> D1 11/15: new card from design submissions

I have more sympathy for this card than any other in this article, as it's hard to test cards like this. It even did some things in Standard that were kind of cool. Still, we do our best these days not to create cards that can make Eternal formats even more high-variance than they naturally are. I'm not sure whether we'd let this one go today.

![](https://i.ormos.uk/0b/0e/0b0e4623e69f476cc2ad72ca801694fc0039330cbea56e4fe21b48a7fc13025f.jpg)

And now, we come to the artifact lands. These interact very powerfully with affinity cards, for which they serve as lands that make two mana. These also interact powerfully with cards like [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcbound+Ravager), [Atog](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog), and [Thirst for Knowledge](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge) that require artifacts as food. Normally, the requirement that one play enough lands to cast one's spells would keep one from playing too many artifacts, but with artifact lands in the mix the sky was the limit. Ravager Affinity decks, for example, commonly played 45 artifacts. This made [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcbound+Ravager) and [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) much more powerful. The artifact lands eventually found themselves on the Standard banned list, a fate shared by few other cards.

![](https://i.ormos.uk/4f/e8/4fe8bc76f82d4c1bd27c8882a6904bf95683648492d11b473a73c1f9a88a75af.jpg)

The following is the entirety of the Multiverse comments all five lands.

> D1 9/16: These still confuse me in many various ways.

Good...

> D2 11/13: These will be in land frames with the same colored text boxes that our other mono-colored nonbasic lands get

Ah, that clears everything up.

![](https://i.ormos.uk/cd/5a/cd5a47c962c40563f77631bf2b89b20487ed22d9744062a05e53999028f5ab42.jpg)

Here's the second most common answer to the "What card would you use a time machine to remove from **Magic**" question. This card is not my answer, but I think it's a reasonable one, as it's bad news for a format when a colorless card is this powerful. Regional Championships in 2004 were dominated by three different decks: Ravager Affinity with [Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp), Goblins with [Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp), and an Elf-based [Tooth and Nail](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail) deck with [Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp). Fewer than one fifth of the people who qualified for Nationals that year at Regionals did so *without* a set of [Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp)s in their main deck. [Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp) soon found itself banned from Standard and Extended, and it was also decided that the card was too powerful for Legacy. Let's see what the developers had to say about it.

> D1 2/11: Ick. Didn't this used to be 'when equipped creature is put into a g.y., draw 2?' I liked that way, way better.  
>  D2 2/17: i too liked it better the old way.  
>  D3 2/26 team agrees that sac me theme isn't working out, switching back  
>  D3 4/30 should/could this be better?  
>  D3 5/2 fiddled with numbers to make it better, also swapped rarities with whispersilk cloak.  
>  D2 6/27: this thing has to be good in some bizarre deck.

...as well as many normal decks.

![](https://i.ormos.uk/cc/9c/cc9cd05e93cec610a17c0be9c75ce484cf1a9f547e6c233fd0d9aa09ee90295a.jpg)

> D1 2/10 Lowered CC to o1 and changed to "your" upkeep (think multiplayer)  
>  D2 2/11: The kids will like this.

So will Merfolk, Goblins, [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcbound+Ravager)s, and Extended banned lists.

Here's a card that is deceptively powerful. Mana is one of **Magic**'s core resources. Cards that give you lots of fast mana are often broken. Normally, those cards enable spell-based quick kills. The developers likely thought that this card was safe, as the fast mana it provides you can only be used to play creatures, which are harmless. As it turns out, that's not quite true. This was a key piece of the most powerful versions of Ravager Affinity, even though those decks didn't often advance [Aether Vial](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Aether%2BVial) past two. Goblin decks did a better job of using it to its full potential, often bringing it all the way to five mana to enable free [Siege-Gang Commander](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang+Commander)s. The card is still played in Legacy with Goblins and Merfolk, and it's powerful enough that it was banned in Extended before [Pro Tour Los Angeles](/en/articles/event-coverage/undated/a-starring-role-for-antoine-ruel-2) in 2005.

![](https://i.ormos.uk/6e/5c/6e5c8555d90ed753cd4a0b1e7734bbefd399f1504379d182948ab0d3c0f1d9bd.jpg)

And now, the winner. This is the most common answer we have to the time machine question. It's the star of the Ravager Affinity deck that ran roughshod across Standard for a year, hand in hand with so many other cards in this article. As you can see, the card was popular with developers, but this was before a significant change was made to the card. (Note that "chimera" was the playtest name for modular.)

> D1 3/4: this guy is the bitchin' chimera.  
>  T2? fringe?  
>  D1 4/8: this guy is the chimeric nuts. i love this guy...  
>  D2 4/19: Make that 2 votes for this guy being awesome...probably my favorite card in the set now..

Drumroll, please...

> D3 7/28: R&D changed mana cost from 3 to 2 just after handoff to Typesetting (7/9).

This may be the single most costly Multiverse comment ever made.

![](https://i.ormos.uk/bd/fc/bdfcad4ad40c4e5e060a1db5d3afc9e6f69677977b8385f26eeb24cdfc937148.jpg)

I mentioned [Trinisphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinisphere) last week as a card whose impact on Vintage we should have thought about. Winning the die roll and casting [Trinisphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinisphere) on turn one with [Mishra's Workshop](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) can really screw up a game of **Magic**. Someone on the receiving end of that can't cast their Moxes or anything until turn three, and by that point they are likely stuck underneath a [Tangle Wire](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tangle+Wire), sacrificing permanents to a [Smokestack](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokestack), or getting beaten down by a [Juggernaut](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Juggernaut). That is not a recipe for good **Magic**. [Trinisphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinisphere) has done some noble anti-combo work in formats like Extended and Legacy, but I think that wasn't worth the cost to Vintage when we could have just made a different anti-combo card instead.

> D1 2/11: I like D2's orignal intent for this card, which was to hose people who build competitive decks so my fatty deck would have a better chance. I say drop the cost so Timmy can have his revenge on Spike.  
>  D3 2/20: this card seems dumb. It's something like "flip a coin and if you win you have a [Nether Void](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nether+Void)" but the people who don't like coin flips don't like [Nether Void](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nether+Void) so no one is happy and people subjected to it are miserable.

The first comment here makes me sad. The second comment here makes me happy. Unfortunately, the first comment seems to have won this fight.

![](https://i.ormos.uk/bc/05/bc056d6568f357724e53133cf317a858402e22d38dc067ea9bf5bcc9e41409eb.jpg)

[Skullclamp](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp) was banned before the *Mirrodin* Block Constructed Pro Tour Qualifier season. Despite that, Affinity was still easily the best deck in the format, largely because of this card. No longer able to draw a million cards to find a [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault), instead Affinity decks had to settle for giving creatures +11/+0 for three mana. Let's see what R&D had to say about that.

> D1 (3/11/03): New equipment.  
>  D1 (3/13/03): Changed from +2/-2 to +3/-1. Added black rider.  
>  D1 (3/17/03): Changed equip from 1 to 2.  
>  D1 (3/27/03): Changed to CD.  
>  D1 (4/10/03): I changed these from CD activations to CC and moved from common to rare.

All right, sure.

> D2 7/3: Took off, "Equipped creature gets +3/-1," and have CQI'd... need this to be interesting.

Interesting? What do you have in mind?

> D2 7/16: changed, added nim ability... should be decent in limited.

What about Constructed?

> D2 8/13: changed activation to 1.

Really. Are you sure that's a good idea?

Some of you may not have been around for the heyday of all of these cards. I was nearly the state champion of Ohio in 2004, and the deck I played to that 2nd-place finish was a good example of the sort of deck that people were playing at the time.

#### Tom LaPille's Affinity

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (25)

4 [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisciple%5D+%5Bof%5D+%5Bthe%5D+%5BVault%5D) 4 [Arcbound Worker](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BWorker%5D) 4 [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BRavager%5D) 3 [Atog](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAtog%5D) 2 [Myr Retriever](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BRetriever%5D) 4 [Frogmite](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrogmite%5D) 4 [Myr Enforcer](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BEnforcer%5D) 

##### Sorcery (4)

4 [Thoughtcast](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtcast%5D) 

##### Artifact (26)

4 [Seat of the Synod](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeat%5D+%5Bof%5D+%5Bthe%5D+%5BSynod%5D) 4 [Tree of Tales](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BTales%5D) 4 [Vault of Whispers](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVault%5D+%5Bof%5D+%5BWhispers%5D) 3 [Great Furnace](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreat%5D+%5BFurnace%5D) 4 [Æther Vial](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BVial%5D) 4 [Chromatic Sphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChromatic%5D+%5BSphere%5D) 3 [Cranial Plating](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BPlating%5D) 

##### Land (5)

4 [Blinkmoth Nexus](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlinkmoth%5D+%5BNexus%5D) 1 [Glimmervoid](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlimmervoid%5D) 

60 Cards 

##### Sideboard (15)

1 [Glimmervoid](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlimmervoid%5D) 1 [Myr Retriever](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BRetriever%5D) 2 [Terror](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 3 [Moriok Rigger](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BRigger%5D) 4 [Oxidize](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidize%5D) 4 [Electrostatic Bolt](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrostatic%5D+%5BBolt%5D) 

##### Blue (4)

4 [Thoughtcast](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtcast%5D) 

##### Black (9)

4 [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisciple%5D+%5Bof%5D+%5Bthe%5D+%5BVault%5D) 2 [Terror](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 3 [Moriok Rigger](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BRigger%5D) 

##### Red (7)

3 [Atog](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAtog%5D) 4 [Electrostatic Bolt](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrostatic%5D+%5BBolt%5D) 

##### Green (4)

4 [Oxidize](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidize%5D) 

##### Colorless (51)

4 [Blinkmoth Nexus](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlinkmoth%5D+%5BNexus%5D) 2 [Glimmervoid](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlimmervoid%5D) 4 [Seat of the Synod](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeat%5D+%5Bof%5D+%5Bthe%5D+%5BSynod%5D) 4 [Tree of Tales](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BTales%5D) 4 [Vault of Whispers](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVault%5D+%5Bof%5D+%5BWhispers%5D) 3 [Great Furnace](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreat%5D+%5BFurnace%5D) 4 [Arcbound Worker](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BWorker%5D) 4 [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BRavager%5D) 3 [Myr Retriever](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BRetriever%5D) 4 [Frogmite](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrogmite%5D) 4 [Myr Enforcer](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BEnforcer%5D) 4 [Æther Vial](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BVial%5D) 4 [Chromatic Sphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChromatic%5D+%5BSphere%5D) 3 [Cranial Plating](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BPlating%5D) 

75 Cards 

##### 1 (24)

4 [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisciple%5D+%5Bof%5D+%5Bthe%5D+%5BVault%5D) 4 [Arcbound Worker](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BWorker%5D) 4 [Æther Vial](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BVial%5D) 4 [Chromatic Sphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChromatic%5D+%5BSphere%5D) 4 [Oxidize](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidize%5D) 4 [Electrostatic Bolt](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrostatic%5D+%5BBolt%5D) 

##### 2 (15)

4 [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BRavager%5D) 3 [Atog](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAtog%5D) 3 [Myr Retriever](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BRetriever%5D) 3 [Cranial Plating](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BPlating%5D) 2 [Terror](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 

##### 3 (3)

3 [Moriok Rigger](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BRigger%5D) 

##### 4 (4)

4 [Frogmite](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrogmite%5D) 

##### 5 (4)

4 [Thoughtcast](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtcast%5D) 

##### 7 (4)

4 [Myr Enforcer](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BEnforcer%5D) 

54 Cards 

##### Common (45)

4 [Seat of the Synod](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeat%5D+%5Bof%5D+%5Bthe%5D+%5BSynod%5D) 4 [Tree of Tales](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BTales%5D) 4 [Vault of Whispers](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVault%5D+%5Bof%5D+%5BWhispers%5D) 3 [Great Furnace](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreat%5D+%5BFurnace%5D) 4 [Disciple of the Vault](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisciple%5D+%5Bof%5D+%5Bthe%5D+%5BVault%5D) 4 [Arcbound Worker](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BWorker%5D) 4 [Frogmite](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrogmite%5D) 4 [Myr Enforcer](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BEnforcer%5D) 4 [Chromatic Sphere](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChromatic%5D+%5BSphere%5D) 4 [Thoughtcast](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtcast%5D) 2 [Terror](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 4 [Electrostatic Bolt](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElectrostatic%5D+%5BBolt%5D) 

##### Uncommon (13)

3 [Atog](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAtog%5D) 3 [Myr Retriever](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMyr%5D+%5BRetriever%5D) 3 [Cranial Plating](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BPlating%5D) 4 [Oxidize](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidize%5D) 

##### Rare (13)

4 [Blinkmoth Nexus](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlinkmoth%5D+%5BNexus%5D) 2 [Glimmervoid](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlimmervoid%5D) 4 [Arcbound Ravager](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArcbound%5D+%5BRavager%5D) 3 [Moriok Rigger](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BRigger%5D) 

##### Mythic (4)

4 [Æther Vial](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BVial%5D) 

75 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blinkmoth+Nexus)

[Deal Another Hand](https://web.archive.org/web/20110325000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seat+of+the+Synod)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Atog)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%C3%86ther+Vial)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Frogmite)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Great+Furnace)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thoughtcast)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tree+of+Tales)

 

A full 38 of the 60 maindeck cards were mentioned in this article, which is about famously powerful **Magic** cards. I am pleased with 18-year-old Tom's ability to choose decks.

![](https://i.ormos.uk/1b/95/1b95177dcc7bae8b0736852269afa7d5737eae26a9e6f8aba0ec85021055f64f.jpg)

Here's another card I consider regrettable, although not cataclysmically so. This card, when combined with [Strip Mine](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strip+Mine) or more commonly [Wasteland](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wasteland), has the ability to ruin perfectly good Eternal games. This happens with great regularity in Vintage and **Magic Online** Classic, in which one can use the aforementioned [Mishra's Workshop](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) to cast a [Crucible of Worlds](https://web.archive.org/web/20110325000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crucible+of+Worlds) very quickly. Let's see what comments there are.

> D1 7/16: testing at 2.  
>  D1 8/13: team concerned about power level, testing at 3.

There are some mitigating factors on this card. It was the winner of a contest that was accurately named [You Make the Card](/en/articles/feature/2003/11-18-you-make-the-card-2-wrap-up). Because the public built the card from the ground up, the developers likely wanted to avoid making the card unplayable. Unfortunately, it had very little impact in Standard and has done unfortunate things in other competitive formats.

Hrm. I got to the end of *Mirrodin*, but I'll let you in on a secret: none of the above comments were actually from Aaron. That hardly seems fair. Hold on a moment.

![](https://i.ormos.uk/8e/7a/8e7afbf8eb7c4ee38f91506ada71f541153c5a9c7f20eb1835e541b5254a45bd.jpg)

> AF 10/24: A good tempting bad card.

Well, that was fun. I sure hope I never get skewered in an article like this one seven years from now, though. That would just be embarrassing.

### Last Week's Poll

<table><tbody><tr><td colspan="3"><b>How many times have you drafted in the past month, either in paper or online? </b></td>&#10;		</tr><tr><td>0</td>&#10;			<td>2097</td>&#10;			<td>38.6%</td>&#10;		</tr><tr><td>1</td>&#10;			<td>918</td>&#10;			<td>16.9%</td>&#10;		</tr><tr><td>2</td>&#10;			<td>734</td>&#10;			<td>13.5%</td>&#10;		</tr><tr><td>3</td>&#10;			<td>407</td>&#10;			<td>7.5%</td>&#10;		</tr><tr><td>4</td>&#10;			<td>373</td>&#10;			<td>6.9%</td>&#10;		</tr><tr><td>5-9</td>&#10;			<td>483</td>&#10;			<td>8.9%</td>&#10;		</tr><tr><td>10-19</td>&#10;			<td>248</td>&#10;			<td>4.6%</td>&#10;		</tr><tr><td>20+</td>&#10;			<td>176</td>&#10;			<td>3.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>5436</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

  
  