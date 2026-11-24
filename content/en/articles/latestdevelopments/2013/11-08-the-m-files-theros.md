---
id: e3trbnzp
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/11-08-the-m-files-theros
title: 'The M Files: Theros'
published: '2013-11-08'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    lang_detected: en
    capture_id: 727236
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    captured_at: '2022-09-26 02:25:32+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    lang_detected: en
    capture_id: 727236
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    captured_at: '2022-09-26 02:25:32+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    lang_detected: en
    capture_id: 727236
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    captured_at: '2022-09-26 02:25:32+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    lang_detected: en
    capture_id: 727236
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
    captured_at: '2022-09-26 02:25:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: e3trbnzp
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
  lang: en
  template: drupal
  captured_at: '2022-09-26 02:25:32+00'
  capture_id: 727236
  wayback_url: https://web.archive.org/web/20220926022532id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
- document_id: e3trbnzp
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/272
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/272
  lang: en
  template: aspx
  captured_at: '2014-02-18 22:35:05+00'
  capture_id: 620663
  wayback_url: https://web.archive.org/web/20140218223505id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/272
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: e3trbnzp
  capture_id: 727236
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
  wayback_url: https://web.archive.org/web/20220926022532id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-08
  captured_at: '2022-09-26 02:25:32+00'
  template: drupal
  sha256: e15399c3331fb97bda4016c03cf8a96e01d505ff07a277af0b5fb71087a78640
render_recovery: []
---
*Beginning with this article, Sam's series where he explores Multiverse comments will be known as the M Files. Look for the M Files image in the future if you're a fan of this popular series!*

Mike McArtor, copy editor of DailyMTG

![](https://i.ormos.uk/b5/69/b56930fc690389f4a31ddc6cc2f9f6adab6bb27f573708aea3383f83e7fa39fc.jpg)

It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here.

But first, the cast of characters:

![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg)

**DH**—[Dave Humphreys](https://web.archive.org/web/20140509102202/http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
**Magic** development manager

![](https://i.ormos.uk/71/7e/717ec8ea013fe26416594283aa203c8c086fe7db5bfeb02641f7c432994f20bb.jpg)

**EEF**—[Ethan Fleischer](https://web.archive.org/web/20140412002643/http://www.wizards.com/magic/magazine/archive.aspx?author=ethan%20fleischer)  
**Magic** designer and [resident Greek-history expert](/en/articles/makingmagic/2013/09-02-an-even-handed-tale)

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

**EVL**—[Erik Lauer](https://web.archive.org/web/20140223104405/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Erik%20Lauer)  
 lead developer of *Theros*

![](https://i.ormos.uk/82/2b/822b917034ff4543ec86ea9e0a479c80f7232f507471856a098422ca9b0c809b.jpg)

**ID**—Ian Duke  
**Magic** developer

![](https://i.ormos.uk/e0/0c/e00c2900e4532fed44efdbc0223f486ee1518c0cf594bb289867319eeda0f043.jpg)

**KD**—[Kelly Digges](https://web.archive.org/web/20140327064203/http://www.wizards.com/magic/magazine/archive.aspx?author=kelly%20digges)  
 lead editor of *Theros*

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg)

**KEN**—[Ken Nagle](https://web.archive.org/web/20140327225845/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle)  
**Magic** designer

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

**Max**—[Max McCall](https://web.archive.org/web/20140508203101/http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  
**Magic** digital developer

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg)

**MJG**—MJG: [Mark Globus](https://web.archive.org/web/20130706022422/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Globus)  
**Magic** senior producer

![](https://i.ormos.uk/f8/3c/f83cde49f5aa4cfb338e0e4a5b8d96af7fe22d2b20b7986681c70bc77fe6cc38.jpg)

**MJ**—Mons Johnson  
**Duel Masters**/**Kaijudo** developer and **Magic** playtester

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg)

**MR**—[Mark Rosewater](https://web.archive.org/web/20140501120753/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater)  
 lead designer of *Theros*

![](https://i.ormos.uk/f8/3b/f83b7c2d164a18a665378b13e7adec05a979b390fc07e360fae3fdfa6f560cab.jpg)

**SM**—[Shawn Main](https://web.archive.org/web/20131126162723/http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main)  
**Magic** designer

![](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg)

**SPS**—[Sam Stoddard](https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  
 That's a-me

![](https://i.ormos.uk/47/08/47081b2fb575627719501cd2b19c0a3c18f386ccd401dc3aa65b271d35cb6db2.jpg)

**SW**—Steve Warner  
**Duel Masters**/**Kaijudo** and **Magic** playtester

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

**TML**—[Tom LaPille](https://web.archive.org/web/20140508201555/http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** developer

![](https://i.ormos.uk/98/ff/98ff84c36158a8091193fe55e8d3028e6e766bb343fd8e5051e08a78fcb62548.jpg)

**ZH**—[Zac Hill](https://web.archive.org/web/20140530202858/http://www.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill)  
 Former **Magic** developer, current **Magic** talking head

Now that we have that out of the way, onto the files:

![Unknown Shores](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unknown+Shores)

EVL 6/18: 5 color fixing.  
 EVL 9/14: Replaces [Evolving Wilds](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds).  
 SPS 9/21: I like this change. Splashing is a path to take, not a basically free decision.  
 TML 10/15/2012: Replaced with functional reprint of [Shimmering Grotto](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shimmering+Grotto).  
 SPS 11/1/12: Yay functionally reprinted lands.

The first version of this card was [Evolving Wilds](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds), which worked, but the slightly higher gold numbers in *Theros*, and so many of the bestow creatures only requiring a single colored mana, led to a lot of splashing. Just coming out of *Return to Ravnica* block, it seemed that it would be better to try and nudge people toward two-color decks. We started this out as [Terminal Moraine](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminal+Moraine), which eventually became the functional reprint of [Shimmering Grotto](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shimmering+Grotto) you can see today.

The important thing to note is that we didn't want to keep people from splashing in Limited, especially in Sealed, but to just make sure there was a reasonable cost involved. Ideally, splashing is usually incorrect, but can be correct in certain circumstances.

![Opaline Unicorn](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Opaline+Unicorn)

DH 10/11: I like where this is at. I'd been refusing to play it but have been reconsidering as people put it to decent use against me.  
 EVL 11/21: Added a toughness.  
 DH 11/26: A bit too similar to Living Caryatid for my tastes in the same set. Would rather see this as a 1/1 or some other means of differentiation in function.  
 EVL 11/26: OK, 1/2.  
 SPS 11/29: Putting that horn to good use.

This card started as a 0/1, and earned a lot of ire (most of it probably undeserved), because it looked so bad. It still served a purpose in Limited, but many people weren't playing it even when they probably should have. Improving it a bit helped out on that front and got people to start putting it in their decks when they had a lot of monsters or expensive bestows.

![Witches' Eye](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Witches%27+Eye)

EVL 8/29: From Romans. Sorry Ken!  
 KEN 8/29/2012: ;( my eyeball

Sometimes, as the development of a set moves on, we find that we have cards we don't like and we need to cut them. One of the easiest ways to fill a hole is to see if another, later set in the same block has a card that you could use. In this case, we stole the card from Ken's file for *Born of the Gods*. Sorry, Ken, but luckily the eye got put to good use!

[Flamespeaker Adept](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamespeaker+Adept)

![Flamespeaker Adept](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flamespeaker+Adept)

EVL 8/3: For the UR Scry deck.  
 SPS 8/30: This is cool  
 SM 8/30: So amusing. Glad he has Ken's eyeball to help him now.

We try to make each color pair in Limited "do" something; blue-red is the spells-matter color pair, but also it focuses on scry. When we do this, we usually put in some kind of build-around uncommon that isn't very strong if you aren't doing "the thing," but gets stronger when you do—as way to reward people in different color pairs. [Nemesis of Mortals](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nemesis+of+Mortals), for example, does this for green-black. Moving [Witches' Eye](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Witches%27+Eye) to *Theros* gave the blue-red deck another great way to trigger [Flamespeaker Adept](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamespeaker+Adept).

![Centaur Battlemaster](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Centaur+Battlemaster)

DH 7/20: Feels a lot like a monster.  
 TML 7/20/2012: In this card's defense, I felt very heroic when I actually pulled it off.

Hulk Smash!

![Pheres-Band Centaurs](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pheres-Band+Centaurs)

(was a 2/7)

ZH 7/20: FILL OUT THAT SPREADSHEET! ;)  
 Max 8/30: This card looks black or white to me, not green.  
 EVL 9/3: Is 3/7 more green?  
 Max 9/6: Yes :)

Erik Lauer has, for the past several years, been attempting to make sure there is a vanilla of each power and toughness combination of 1–6 in **Magic**. He completed this is *Return to Ravnica* with [Catacomb Slug](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Catacomb+Slug), but has since moved on to making sure that 1–7 also have vanillas.

![Mistcutter Hydra](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mistcutter+Hydra)

Oh, the long and crazy history of [Mistcutter Hydra](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra).

EEF 8/17/11: New card.

The card began as a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 12/12 with "cannot attack unless you control at least twelve permanents" as a nod to Hercules. Creative was unhappy with the largest creature in *Theros* being a human, and so it became a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) Hydra with that text.

ID 8/30: Not in love with this, seems like it would be a frustrating experience to try to turn this on.  
 DH 9/4: Like it in green better with ramp, fight, and possibly tokens.  
 Mago 9/11: Strange that both rare/mythic rare green Hydras cost 2GG  
 MJ 9/13: better to not turn it on, just play [Disciple of Bolas](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+Bolas)...  
 TML 10/15/2012: Now 3G for Johnny.  
 EVL 12/6: New design to attack control decks.

The card then changed to something to better fight the [Sphinx's Revelation](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) decks we were seeing in the real world, as well as the white-blue control decks in our [FFL](/en/articles/latestdevelopments/2013/08-16-days-of-future-future-part-2) with Elspeth, and create a creature that was not killable by [Detention Sphere](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detention+Sphere).

Twelve-Headed Hydra  
 3GG  
 Trample  
 You may cast CARDNAME from your graveyard or exile. Whenever an opponent draws a card, put a +1/+1 counter on CARDNAME.  
 5/5  
 MJ 12/14: Testing shows this to be too powerful as is, imo. Might be ok as a 4/4.  
 EVL 12/18: removed some text, but now can't be countered and protection from blue.  
 EVL 12/31: New text.

It was in between this time that we created the cycle of "protection from \[color\]" creatures, and that changed what we needed from this card.

The card then changed to:

[Mistcutter Hydra](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Haste, protection from blue  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 If an opponent has five or more cards in hand, you may cast CARDNAME from your graveyard.  
 0/0  
  
 MR 1/03/13: Card feels very inelegant. I know it's serving a development purpose but I wonder if it can be made a little less Frankenstein looking.

Besides just looking weird, one problem with being able to cast a Hydra from your graveyard meant that death or "enters the battlefield" triggers suddenly became live on just paying ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). That was not okay.

EVL 1/10: New text.  
  
[Mistcutter Hydra](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Trample, haste, protection from blue  
 CARDNAME can't be countered.  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 Remove two +1/+1 counters from CARDNAME: Regenerate CARDNAME.  
 0/0  
  
 Sw 1/14: I feel like this is a bit over what we would normally give a card. I could see this at XGG, or even XG if it didn't have haste. I don't think it's breaking much (besides blue) now, just a bit over.  
 EVL 1/15: Removed regenerate text.  
 Max 1/23: I think we will be unhappy with how powerful this is against next year's blue decks.  
 KD 1/28: Loses trample, now can't be blocked by small creatures.

The card with trample and haste was powerful enough that many of our green decks were playing it main, which is not where we wanted this card. We wanted it to be something that could be main deck if the format was skewed toward blue, but would be more of a sideboard card, so we took that ability off. We were still worried about green decks not having a good answer to Elspeth, so the card morphed into:

[Mistcutter Hydra](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Haste, protection from blue  
 CARDNAME can't be countered.  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 CARDNAME can't be blocked by creatures with power 1 or less.  
 0/0  
  
 KD 3/28: Per Erik, cut pseudo-trample: [Mistcutter Hydra](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra) can't be blocked by creatures with power 1 or less.

Very late in development, Nylea's abilities changed and granted trample to all creatures. This was the exact change we needed to give green decks a way to beat an Elspeth, so we were able to take off the last super-wonky words from the card, and end up in a more sensible place.

![Triton Tactics](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Triton+Tactics)

ID 12/10: This is super underwhelming compared to the others in the cycle. Should this give some extra bonus, like hexproof, or frosting creatures they block this turn?  
 EVL 12/12: Great idea.  
 KD 3/18: Template update: Now with [Joven's Ferrets](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven%27s+Ferrets) technology so it locks things down whether you play it before or after blockers.

It's not often that the editors need to go to *Homelands* to find templates. [Joven's Ferrets](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven%27s+Ferrets) provided the wording we needed but never answered the question of why [Joven](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven) was into Ferrets.

![Anger of the Gods](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Anger+of+the+Gods)

EVL 9/7: Changed to anti-regenerate due to [Lotleth Troll](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotleth+Troll).  
 KEN 9/10/2012: [Lotleth Troll](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotleth+Troll) must go big or go home!!  
 MJG 9/11/12: This is the second red card with the anti-regen clause. Seems like one too many.  
 TML 10/29/2012: Used to be anti-regen. Now exiles.  
 ID 11/12: I like that this answers [Voice of Resurgence](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voice+of+Resurgence) effectively. Provides a good tension between red and white sweepers.

It's not every day we get to create powerful red sweepers, but one of the things we have tried to do is give red some additional midrange options and keep it from being just a beatdown color. We had already seen Chandra in ***Magic** 2014* working great as a top-end card in red aggro, or as a card drawer in the red-based midrange decks. We also knew that devotion is a risky mechanic that can snowball, so making sure that multiple colors have options for sweepers would keep the format in a place where it could evolve. [Anger of the Gods](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger+of+the+Gods) was in the right place to solve all of those issues.

![Cavalry Pegasus](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cavalry+Pegasus)

EVL 9/21: New ability to avoid looking like a heroic trigger.  
 EVL 11/21: Changed to a 2HG template!  
 EVL 1/2: Trigger free!  
 ID 1/8/13: Downside to trigger free is that if someone advances to declare blockers and doesn't realize a human has flying, there's no backing up. I can see myself doing this and getting frustrated.  
 EVL 1/9: Good point Ian. I think this is worth trying.  
 TML 2/6/2013: I prefer these being triggers now. I think this and power/toughness granting things should be the same, and anything that grants toughness needs to be a trigger until eot or things can just die out of nowhere.  
 KD 2/7: Now a trigger. Because it's an attack trigger, I dropped "you control" for 2HG.

The original version of this card gave flying to one target Human when you attacked.

One piece of early feedback we got on *Theros* was that playtesters were sometimes confused when their triggers on creatures didn't trigger heroic. We briefly tried out heroic working that way, but the cards were impossible to balance, considering a card like [Civic Saber](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Civic+Saber) turned [Labyrinth Champion](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Labyrinth+Champion) into a machine gun, and there were already several Equipment in the set.

Instead, what we did was to try and remove as many instances of creatures that could target your own creatures as we could, at least at lower rarities. There are still some, but most of them are there because the game play was just better to be able to target your own guys. We also tried a version of him that didn't trigger, which had some rules benefits, but which could create some huge blowouts if it was killed during combat. We opted to go with the current version instead.

![Fanatic of Mogis](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fanatic+of+Mogis)

EEF 5/24/12: 5R 2/3 -> 2R 3/1. Common -> uncommon.  
 EVL 11/21: Added a mana and a toughness.  
 DH 11/26: Can this be a 4/2 ? As uncommon I'd rather this not be completely trumped by the 2/4 Devotion Drainer in black.  
 EVL 11/26: OK, 4/2 if creative approves.

Devotion was a hard mechanic to get right, and we quickly found that a lot of cards with devotion were stronger than we were expecting. For [Fanatic of Mogis](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis), this was mostly due to the powerful ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) cards like [Burning-Tree Emissary](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning-Tree+Emissary), [Ash Zealot](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ash+Zealot), and [Boros Reckoner](https://web.archive.org/web/20131108000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner). Moving the cost on this to four mana meant that you could no longer curve out at one- two- three-drop and have your opponent at 8 life (or less) the beginning of his or her fourth turn. Upping the cost gave the opponent much more of an opportunity to interact with the board before Fanatic hit the table.

That's it for this edition of the M Files.

Until next time,  
 Sam ([@samstod](https://twitter.com/@samstod))