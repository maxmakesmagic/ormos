---
id: 41kvfvq7
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/07-29-the-magic-2012-multiverse-dump-part-1
title: The Magic 2012 Multiverse Dump, Part 1
published: '2011-07-29'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    lang_detected: en
    capture_id: 727282
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    captured_at: '2022-06-29 19:20:39+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    lang_detected: en
    capture_id: 727282
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    captured_at: '2022-06-29 19:20:39+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    lang_detected: en
    capture_id: 727282
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    captured_at: '2022-06-29 19:20:39+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    lang_detected: en
    capture_id: 727282
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
    captured_at: '2022-06-29 19:20:39+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 41kvfvq7
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
  lang: en
  template: drupal
  captured_at: '2022-06-29 19:20:39+00'
  capture_id: 727282
  wayback_url: https://web.archive.org/web/20220629192039id_/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
- document_id: 41kvfvq7
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/153
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/153
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:36:51+00'
  capture_id: 613405
  wayback_url: https://web.archive.org/web/20130706053651id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/153
- document_id: 41kvfvq7
  url: http://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-29
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-29
  lang: en
  template: drupal
  captured_at: '2016-07-31 04:23:01+00'
  capture_id: 727285
  wayback_url: https://web.archive.org/web/20160731042301id_/http://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-29
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 41kvfvq7
  capture_id: 727282
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
  wayback_url: https://web.archive.org/web/20220629192039id_/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-1-2011-07-28
  captured_at: '2022-06-29 19:20:39+00'
  template: drupal
  sha256: ede1b2c5df328ba5cec8e5cf097be3800008026e0b3c29cce09d9c6e5e5f6661
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
It's been a while since I've done a Multiverse article. Conveniently, it's also been a while since I knew a Multiverse file as well as I know the file for ***Magic** 2012*, as I was the set's lead developer. Let's do this.

For those of you who haven't been around for a while, Multiverse is the database we use to build **Magic** sets. While much of it is administrative and used to handle things like art credits, collector numbers, and so on, we also use it to control card texts, and it has space for us to use to communicate with each other. Everything you see in monospace in this article came directly from internal communications that took place during ***Magic** 2012* design and development.

Here's your cast of characters for today.

> AF: Aaron Forsythe, Director of **Magic** Ramp;D and ***Magic** 2012* design team member  
>  DB: Doug Beyer, ***Magic** 2012* design team member  
>  Del: Del Laugel, **Magic** senior editor  
>  DH: Dave Humpherys, ***Magic** 2012* development team member  
>  KD: Kelly Digges, ***Magic** 2012* development team member  
>  KEN: Ken Nagle, ***Magic** 2012* design team member  
>  MJ: Mons Johnson, **Magic** playtester  
>  MR: Mark Rosewater, **Magic** head designer  
>  MT: Mike Turian, ***Magic** 2012* development team member  
>  PAS: Peter Schaefer, ***Magic** 201*2 development team member  
>  Tabak: Matt Tabak, **Magic** editor  
>  TML: Tom LaPille, ***Magic** 2012* lead developer

![](http://media.wizards.com/images/magic/daily/ld/ld153_card01a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld153_card01b.jpg)

***Magic** 2012* lead designer Mark Globus created an aura subtheme in ***Magic** 2012*. He was also bored with [Holy Strength](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) and [Unholy Strength](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength), and his design handoff included a more powerful and splashy pair of cards to replace them. The design handoff version of this card, though, gained you only 1 life when it entered the battlefield, to mirror [Dark Favor](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor)'s 1 life loss, and gave a bonus of +1/+4 to mirror [Dark Favor](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor)'s +4/+1. Power is stronger than toughness, so I thought this card needed a little more juice.

> TML 4/14/2010: We want these cards to be better. Four life instead of one!  
>  KD 4/23: Much more appealing, both power-wise and aesthetically.  
>  MR 7/06/10: If you care about aesthetics, the life should be the combination of the power and toughness.  
>  AF 7/19: I didn't realize aesthetics had such well-defined answers.  
>  KEN 8/2/2010: This card is 3.4 milliHelens beautiful.  
>  TML 8/3/2010: Excellent choice of unit. Also, now less good.

[Dark Favor](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Favor) proved too good at +4/+1, so I moved it to +3/+1 instead. [Divine Favor](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Favor) had to change to match it, so it went back down to +1/+3 and 3 life, where we printed it.

![](http://media.wizards.com/images/magic/daily/ld/ld153_darkFavor.jpg)  
![](http://media.wizards.com/images/magic/daily/ld/ld153_card02a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld153_card02b.jpg)

[Grand Abolisher](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grand+Abolisher)'s intent was never in question. However, its actual words changed quite a bit. Here's where it started:

> During your turn, your opponents can't cast spells or activate abilities.

This is pretty weird for **Magic**, though, as it would keep you from even tapping your lands for mana. We normally get around this by excluding "mana abilities," which according to the rules means "nontargeted abilities that add mana to your mana pool." To match up with precedent, I changed it to this:

> During your turn, your opponents can't cast spells or activate abilities that aren't mana abilities.

Then, I found myself wondering something.

> TML 6/16/2010: Is there any good reason to exclude mana abilities from this? Is someone casting [Fade Away](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fade+Away) or something? Some people think "mana abilities" are any abilities that cost mana, which makes this card read worse to them.

I'm not a big fan of forcing people to look up the comprehensive rules, nor am I a fan of questions with bizarre answers. For example, have a look at these two cards:

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Talisman"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Pristine+Talisman"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Immolating+Souleater"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Immolating+Souleater"></a></div></div></td></tr></tbody></table>

One of these two cards has a mana ability. Do you know which one? I ran a straw poll among less-experienced **Magic** players in the building, and many of them either got it wrong or told me they had no idea.

Del Laugel, our crack senior editor, was ready with an astute and terrifying answer.

> Del 9/3: Shutting off mana abilities means that we'll need to consider this card when templating all future cards with buyout clauses ([Shrouded Serpent](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shrouded+Serpent)), triggered abilities that have mana stuck in for dev reasons ([Azorius Æthermage](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+%C3%86thermage)), and triggered abilities that behave like do-this-once activated abilities ([Electropotence](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Electropotence)). I'm not saying the card can't stay as it is; I'm just saying that it will receive a lot of attention during templating if it's handed off like this.

Attention from the templating team is a little scary, as it means that your cards are liable to change under your feet. In classic **Magic** developer tradition, I just changed my card to dodge the issue instead. It now turns off mana artifacts, but leaves lands—the most likely source of mana—alone.

![](http://media.wizards.com/images/magic/daily/ld/ld153_card03a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld153_card03b.jpg)

[Phantasmal Bear](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Bear) started out life the same way it was printed.

> DB 3/8/2010: Don't poke the bear!  
>  KD 4/6: In the old days this would've cost 1U. The old days sucked.  
>  PAS 4/12: Love this theme.

While the Bear was cute, I was interested in doing a little more color pie pushing. Each Illusion creature in the file was designed to match a non-Illusion creature elsewhere in the file; what if one of the illusions was a version of a card that blue didn't normally get? I saw [Youthful Knight](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) in white and got an interesting idea.

![](http://wizards.com//mtg/images/daily/ld/ld153_mortallity2.jpg)  

> TML 4/14/2010: Was U 2/2. Trying crazier U 2/1 first strike for more color bleeding.

This caused some consternation. What was I doing with a blue first-striker? Why did it win in combat against everything? What is going on here? There was some amount of unhappiness about this, but a larger amount of bewilderment.

Eventually, though, [Youthful Knight](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) made its way out of the set on its own, which made this particular Illusion Knight look particularly out of place. I changed it back to the Bear, and everyone was happy.

> TML 5/14/2010: Back to bear. No one cared that it was a knight, and [Youthful Knight](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Youthful+Knight) is gone.

Well, almost everyone. Some people still had issues, but I just pretended to not know what they were talking about.

> MJ 6/10: strange that blue gets a 2 power 1 drop, but green doesn't.  
>  TML 6/16/2010: What two power one drop? I don't see anything... :)

![](http://media.wizards.com/images/magic/daily/ld/ld153_card04a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld153_card04b.jpg)

[Chasm Drake](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chasm+Drake), to you, likely looks like just another **Magic** card. When I look at it, I groan a little inside, as it was the common in the set that I struggled the most with.

***Magic** 2012* lead designer Mark Globus was interested in including fantasy tropes that took more than one card into the set. You can see that theme in cards like the Empires artifacts and the pairing of [Arachnus Spinner](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arachnus+Spinner) and [Arachnus Web](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arachnus+Web). One card that didn't make it was an artifact, flavored to be a magic lamp, that interacted with Djinn creatures. I fell in love with this idea, and made a common Djinn, a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) 3/3 flier, to support it. I was rather proud of the mechanic I came up with, which despite being reasonable for common still did a reasonable job of getting Djinn flavor across. Then, I discovered that we don't make common Djinns.

> TML 4/14/2010: Knight is already a bloodthirst enabler, and we need a real flying creature. Was [Zephyr Sprite](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zephyr+Sprite). Made a good flyer and a djinn for the Lamp.  
>  TML 4/14/2010: Note that creative is not in love with djinns. We should figure out how much we like the lamp.  
>  EVL 5/2: Fun  
>  TML 5/3/2010: This won't be a djinn, but it can maybe stay this. I like this!  
>  Del 6/1: Should this card wait for the Djinn set to come rather than become "smart pudgy bird" or "baby sphinx"?

I decided that the answer to Del's question was yes—this mechanic worked well enough on a common Djinn that it could wait for a time when it could be one—and looked for a new card. I struggled for a few weeks to find an ability for a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) 3/3 flier until Erik suggested that I look for underplayed color combinations in Limited. This showed me that green-blue was not being played as much as the others. We engineered [Chasm Drake](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chasm+Drake) to be good friends with [Vastwood Gorger](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vastwood+Gorger), the lamp became [Quicksilver Amulet](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quicksilver+Amulet), and the rest is history.

> TML 6/4/2010: This ability will change. I don't know what to.  
>  TML 6/11/2010: New line of text. Would like a drake here.

Dave Humpherys later pointed out that this card could swoop onto an opponent's side of the board and take out an illusion, which is an unfortunate interaction.

> DH 8/13: Add 'you control' to save the bears (illusions).  
>  TML 8/17/2010: Bears saved.

This being **Magic** Ramp;D, though, we couldn't stop without one final snarky comment.

> Tabak 11/30: I just want to go on record as hating the Bears, but I'll let this go.

![](http://media.wizards.com/images/magic/daily/ld/ld153_card05a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld153_card05b.jpg)

Three Ramp;D members disagree.

> MT 3/8: Still think this guy could be busted.  
>  KEN 3/9/2010: I didn't enjoy this card the first time.  
>  DB 3/10/2010: The perfect top-down Skeleton.

Three Ramp;D members disagree.

![](https://i.ormos.uk/bd/2d/bd2d5ace8b8f9c9ceb613cef8f1ed759f8cf99bbe030e868ae714ca00ce86d95.jpg)  

Okay, I'm out of time. There's more where this came from, though, so I'll be back to it later this summer.

Last Week's Polls

<table><tbody><tr><td colspan="3"><b> Are you happy that the Titans are in <i>Magic 2012</i>? </b></td></tr><tr><td>Yes</td><td>631</td><td>54.6%</td></tr><tr><td>No</td><td>381</td><td>33.0%</td></tr><tr><td>I have no opinion.</td><td>144</td><td>12.5%</td></tr><tr><td><b>Total</b></td><td><b>1156</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

<table><tbody><tr><td colspan="3"><b> Are you happy that <a href="https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Fortress">Glacial Fortress</a> and friends are in <i><b>Magic</b> 2012</i>?</b></td></tr><tr><td>Yes</td><td>851</td><td>68.2%</td></tr><tr><td>No</td><td>280</td><td>22.4%</td></tr><tr><td>I have no opinion.</td><td>117</td><td>9.4%</td></tr><tr><td><b>Total</b></td><td><b>1248</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

This Week's Poll

**Which Ramp;D member do you agree with most about [Reassembling Skeleton](https://web.archive.org/web/20110729000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reassembling+Skeleton)?**Mike Turian: Still think this guy could be busted.Ken Nagle: I didn't enjoy this card the first time.Doug Beyer: The perfect top-down Skeleton.

  

* * *

![](http://wizards.com//mtg/images/daily/features/M12_ArticleFooter_MTGO_top_ver1.jpg)[![](http://wizards.com//mtg/images/daily/features/M12_ArticleFooter_MTGO_button_Static.jpg)](https://web.archive.org/web/20110729000000/http://archive.wizards.com/magic/Digital/MagicOnline.aspx)![](http://wizards.com//mtg/images/daily/features/M12_ArticleFooter_MTGO_BottomRight_ver1.jpg)