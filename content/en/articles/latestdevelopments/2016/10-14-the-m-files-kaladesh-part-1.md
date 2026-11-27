---
id: z3ndx8ww
kind: article
lang: en
path: /en/articles/latestdevelopments/2016/10-14-the-m-files-kaladesh-part-1
title: 'The M-Files: Kaladesh, Part 1'
published: '2016-10-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    lang_detected: en
    capture_id: 727040
    url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    captured_at: '2017-03-25 21:39:27+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    lang_detected: en
    capture_id: 727040
    url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    captured_at: '2017-03-25 21:39:27+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    lang_detected: en
    capture_id: 727040
    url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    captured_at: '2017-03-25 21:39:27+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    lang_detected: en
    capture_id: 727040
    url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
    captured_at: '2017-03-25 21:39:27+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: z3ndx8ww
  url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
  lang: en
  template: drupal
  captured_at: '2017-03-25 21:39:27+00'
  capture_id: 727040
  wayback_url: https://web.archive.org/web/20170325213927id_/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: z3ndx8ww
  capture_id: 727040
  url: http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
  wayback_url: https://web.archive.org/web/20170325213927id_/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-kaladesh-part-1-2016-10-14
  captured_at: '2017-03-25 21:39:27+00'
  template: drupal
  sha256: 9b7f7e3845eb7c4333676b7b84d377886833f4e084350bbf5ff49d6eb9ede713
render_recovery: []
---
![](http://media.wizards.com/2016/images/daily/Mfiles2016.jpg)

It's time once again to return to the M-Files! Frequent readers of this column will know that Multiverse is our internal database, used to track *Magic* cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights on the design and development processes, as well as a few laughs. You'll find both here.

If you'd like to have a face to put with each name, click below to review our cast of commenters:

## Click to Reveal

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke, development co-lead for *Kaladesh*

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_markrosewater.jpg)**MR**—Mark Rosewater, design co-lead for *Kaladesh*

![](http://media.wizards.com/2015/images/daily/authorpic_shawnmain.jpg)**SM**—Shawn Main, design co-lead for *Kaladesh*

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_samstoddard.jpg)

**SPS**—Sam Stoddard, developer. That's-a me!

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_davehumphreys.jpg)**DH**—Dave Humpherys, developer

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_matttabak.jpg)**TABAK**—Matt Tabak, editor

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_markglobus.jpg)**MJG**—Mark Globus, product architect

![](http://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_monsjohnson.jpg)**MJJ**—Mons Johnson, designer for *Duel Masters*

![](http://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_adamprosak.jpg)**AP**—Adam Prosak, developer

![](http://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_jamessooy.jpg)**JS**—James Sooy, UX designer

![](http://media.wizards.com/2015/images/daily/authorpic_JackieLee.jpg)**JL**—Jackie Lee, designer

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_aaronforsythe.jpg)**AF**—Aaron Forsythe, The Big Boss Man (senior director)

![](http://media.wizards.com/2015/images/daily/Bryan_Hawley.jpg)**BrH**—Bryan Hawley, developer

![](http://media.wizards.com/2015/images/daily/authorpic_YoniSkolnik.jpg)**YS**—Yoni Skolnik, developer

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_gavinverhey.jpg)**GSV**—Gavin Verhey, designer

![](http://media.wizards.com/2016/images/daily/mfiles_melissa-detora.jpg)**MDT**—Melissa DeTora, playtester

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_kennagle.jpg)**KEN**—Ken Nagle, editor

![](http://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_dellaugel.jpg)**DEL**—Del Laugel, editor

![](http://media.wizards.com/images/magic/daily/authorpics/authorpic_timaten.jpg)**TJA**—Tim Aten, editor (former)

![](http://media.wizards.com/2016/images/daily/Jules_Robbins.jpg)**JDR**—Jules Robins, designer

With that out of the way, let's get to the cards:

**Tasseled Dromedary**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tasseled+Dromedary)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tasseled+Dromedary)

ID: 2W 3/2 -> W 0/4.  
 ID: W 0/4 -> 3W 1/6.  
 SPS: *He's so fluffy!*  
 ID: 3W 1/6 -> W 0/4. As originally concepted.

I have a secret to admit: sometimes I plant things in here to pull up a year later, just in case nobody else put anything amusing in the file. Fortunately, there is some good stuff in the *Kaladesh* M-Files, but I am leaving this one here because it amuses me.

* * *

**Ninth Bridge Patrol**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ninth+Bridge+Patrol)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ninth+Bridge+Patrol)

ID: 1W 1/1 -> 2W 2/2 to differentiate from [Unruly Mob](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unruly+Mob), which is common in *SOI*.  
 ID: 2W 2/2 -> 1W 1/1 and uncommon -> common.

So, yes, technically [Ninth Bridge Patrol](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ninth+Bridge+Patrol) is just an all-upside version of [Unruly Mob](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unruly+Mob), which appeared two sets earlier, but we needed to leave ourselves some room for this kind of thing. This is certainly the kind of card we wanted in the set—one that could get better as you did the white-blue thing of bouncing your own creatures to get their enters-the-battlefield effects again—and forcing it to be at a different mana cost than [Unruly Mob](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unruly+Mob) wasn't worth the changes.

* * *

**Gearshift Ace**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gearshift+Ace)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gearshift+Ace)

SM: Now two-drop, now vigilance.  
 SM: Now three-drop, now first strike.  
 ID: 2W 2/2 -> 1W 2/1.

This was a design created pretty early in design. The three comments above were left over a year apart from one another. Once we had Vehicles and crew in the set, having Pilots that helped crew Vehicles was an obvious and interesting way to go. It certainly helps to separate Vehicles from Equipment even more.

* * *

**Servo Exhibition**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Servo+Exhibition)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Servo+Exhibition)

ID: Common -> uncommon to reduce as-played of tokens.

We talk a lot about as-fan, but less about as-played. The idea is, not surprisingly, to think about things on the table as opposed to just in the boosters for Draft. One of the issues we were running into with *Kaladesh* at many times was that there were just too many tokens running around. With fabricate adding so many, we didn't need a strong common like this to add to the problem. By cutting it, we were hoping to make things like large creatures without trample to be more viable in Limited.

* * *

**Trusty Companion**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trusty+Companion)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trusty+Companion)

ID: New card from mini team.  
 DH: Looks relatively strong, or at least I'm surprised it could block alone.  
 DH: Also funny the back-up plan for this Hyena is to get in a Vehicle.  
 ID: Uncommon -> common, 3/3 vigilance -> 3/2.

Having "can't attack or block alone" on the card was close to the right power level, but not how white does things. Once it could block alone, it became a bit too strong as a wall, especially since it had vigilance. We ultimately moved it back to uncommon and made it more of a Vehicle enabler than a go-wide powerhouse.

* * *

**Wispweaver Angel**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wispweaver+Angel)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wispweaver+Angel)

SPS: I assume two of these and some random other combo card isn't a problem. Probably should keep it at five-plus mana, though.  
 TABAK: The developers of [Restoration Angel](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Restoration+Angel) felt differently.

Over time, we have certainly become less gun-shy about expensive combos between cards that combo with extra copies of themselves or just two five-plus-mana cards together that go infinite. *Kaladesh* is all about becoming an inventor, so if you have a three-card combo with some expensive cards, we're probably doing the right things.

* * *

**Refurbish**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Refurbish)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Refurbish)

MJG: We haven't made this card before? Seems like a perfect fit!  
 ID: We did [Argivian Restoration](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Argivian+Restoration) long ago, but this effect is now white. I really like the simple version here.  
 DH: Future Future League (FFL) meeting. Please test.  
 MJJ: I am dubious about having this card and Gearhulks. I worry that the best deck is just the intersection rather than the individual decks that the various Gearhulks may spawn.  
 ID: We can always go to five mana on this if we need to. Four mana to reanimate a six-ish mana creature doesn't seem unreasonable to me though.

Time will tell. We usually don't like making huge risks on the graveyard in non-graveyard sets, but this felt the right kind of card to do it with. Even if people are filling up their graveyard and returning something, if it is an artifact, they are probably doing something Johnny-ish that will feel more *Kaladesh*-y than *Innistrad*-y.

* * *

**Toolcraft Exemplar**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Toolcraft+Exemplar)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Toolcraft+Exemplar)

ID: New ability. Was "Whenever [Toolcraft Exemplar](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Toolcraft+Exemplar) becomes tapped, if you control an artifact, put a +1/+1 counter on [Toolcraft Exemplar](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Toolcraft+Exemplar)."  
 ID: +2/+2 -> +2/+1

The original version of this was a W 1/1 that got a +1/+1 counter whenever it tapped, if you controlled an artifact. It was very good if you had a Vehicle, since it could crew it at end of turn, and attack as a 3/3 the first time it had the chance. While this did a good job of promoting the artifact aggro decks, it also did it a bit too well. It was very snowball-y, and if you ever managed to cast two on the first two turns followed by something like a [Thraben Inspector](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thraben+Inspector), you were probably going to only lose to a board sweeper. The printed version is generally more powerful if you don't have Vehicles in your deck, at least for the first attack, but doesn't go so far up in power that your opponent can't block with a Gearhulk on turn six.

* * *

**Fumigate**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fumigate)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fumigate)

AP: FFL suggests 2WW "Exile all creatures with converted mana cost 2 or less. Gain 1 life per creature exiled in this way." Or just converted mana cost 3 or less without life gain.  
 ID: Trying new text, pending creative approval.  
 JS: Is this supposed to be hitting double-faced cards and meld creatures?  
 MR: A lot of different restrictions on white kill spells. Might want to line a few of them up.  
 ID: Yes JS, we like to have answers to the previous block. Aiming the rate at metagame/sideboard.  
 SM: This looks like a black-aligned card. Why is white punishing small creatures? This looks like a color pie violation.  
 JL: I agree that white shouldn't be killing two-drops and [Last Breath](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Breath) was a mistake. Could deal 2 damage to each attacking/blocking creature?  
 ID: Continuous quality improvement'd for color pie.  
 ID: Moving to a simpler wrath as a placeholder. Likely to change in FFL.  
 BrH: OooOoo.  
 JL: Is there any way this could gain you a flat amount of life? Keying off creatures killed feels like black schadenfreude.

Originally, this was a mass [Last Breath](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Breath) that gained the caster life. Except, as design pointed out many times, it was not really in color pie. It is something we have done a lot in the past, but have identified as a mistake going forward. At the same time, we have struggled a bit with getting our five-mana Wraths to be appealing to people. They see Standard play, but some of that is because of how strong they are, not about how appealing they are. This version of the card was exciting enough for people that they would want to build decks to play [Fumigate](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fumigate), rather than going to the strongest five-mana Wrath in the format.

* * *

**Aether Tradewinds**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Aether+Tradewinds)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aether+Tradewinds)

SM: Everyone's favorite! White-blue gating.  
 SM: Peel -> Tradewinds.  
 AF: Such flavor.

Some percentage of reprints have names that work (Aether) and some percentage work well with the set mechanically (white-blue is a self-bounce deck). When they come together, there is a high chance the card just makes the final set.

* * *

**Saheeli's Artistry**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Saheeli%27s+Artistry)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saheeli%27s+Artistry)

BrH: Can confirm—this card is fun.  
 JDR: I adore this card.  
 DH: I assume it's intentional you can double-copy artifact creatures? Where's my [Precursor Golem](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Precursor+Golem) (if that even works) or [Wurmcoil Engine](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wurmcoil+Engine)? In other news, surprised I can't find "Put two token copies of a creature onto battlefield" on a card before...not including flashback, retrace, cipher, etc.  
 ID: Modal-ified, and now the creature copy is an artifact by creative request.  
 YS: This seems most powerful *against* Gearhulks. Is that reasonable?  
 AF: It seems pretty insane *with* them, to be fair.

True enough on both counts. All that said, I would be surprised if this is the card that keeps people from playing Gearhulks, but it is a very interesting answer to them if they are as ubiquitous as [the Titans](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&name=+%5bTitan%5d&set=%7C%5b%22Magic%202011%22%5d%7C%5b%22Magic%202012%22%5d) were in *Magic 2011* and *Magic 2012* Standard.

* * *

**Tezzeret's Ambition**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tezzeret%27s+Ambition)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tezzeret%27s+Ambition)

ID: New card. [Jace's Ingenuity](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%27s+Ingenuity) variant.  
 ID: Was "Draw four then discard two unless you discard an artifact." Now simple draw three. Uncommon -> common.  
 SPS: This makes me a little sad, but it looks correct for common.  
 BrH: 4U to at least make the comparison less obvious?  
 ID: Now discard a card unless you control an artifact.

This card tried to be five-mana straight-up draw three at common, which was about the right power level, theoretically, but more impactful and less directional than we would have liked. Moving from 3UU to 4U helped to separate the cards, and moving to discarding unless you controlled an artifact at least made it less powerful in any old deck. Not that having an artifact is very hard in *Kaladesh* Limited, but it requires some work.

* * *

**Paradoxical Outcome**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Paradoxical+Outcome)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paradoxical+Outcome)

ID: Creature -> instant. Too many creatures bouncing things.  
 GSV: I have found this pretty unwieldy at this mana cost so far, at least for Limited. Could it be 2U?  
 ID: Sure, let's try 2U.  
 ID: 2U -> 3U

[Paradoxical Outcome](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paradoxical+Outcome) is kind of the poster child for cards that are awesome if they are a little weak and lame if they are really powerful. At 3U, we found this card to be awesome in an [Aetherflux Reservoir](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aetherflux+Reservoir) deck, but at 2U it made the deck more powerful than we wanted. We are wrong a lot about cards, so we tend to try to make a lot of Johnny-ish combo decks to be tier 2. [Sphinx's Tutelage](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Tutelage) and the Cat Pact deck both hit this mark in the last year or so. If we make several tier 1 combo decks, and we are wrong, we usually do not find the formats end up very fun—but having a few tier 2 combos that end up being tier 1 (but barely) tends to be pretty fun. Time will tell which way we missed with this deck.

* * *

**Morbid Curiosity**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Morbid+Curiosity)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Curiosity)

YS: I never play [Altar's Reap](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Altar%27s+Reap), and I think being a sorcery is worse than being able to sacrifice artifacts. Can this be an instant for a strictly better?  
 ID: Sorcery -> instant.  
 ID: 1B instant sac creature or artifact to draw two -> 2B sorcery and draw, same converted mana cost. Common -> uncommon.  
 AP: [Metalwork Colossus](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metalwork+Colossus) says "Hello."

[Altar's Reap](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Altar%27s+Reap) is a card we make frequently that never does much. We rejiggered this version of it to be strong enough that it might do interesting things. We'll look to see how this goes, and maybe look at some other interesting variants in the future.

* * *

**Lost Legacy**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lost+Legacy)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lost+Legacy)

ID: New card. [Memoricide](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide) variant.  
 MDT: [Memoricide](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide) variants are pretty unappealing, and this one is worse.  
 ID: I think this is better at doing what [Memoricide](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide) is "supposed" to do, and less good at getting incidental card advantage by [Cabal Therapy](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Therapy)-ing your opponent.  
 MDT: But it's only card advantage if you get two cards from the hand! Most of the time this is card disadvantage. This version is now always pure card advantage for the opponent. The people who hate this effect will find this card appalling. Those who like it will find it unappealing. My two cents.

I get Melissa's concern with this—[Memoricide](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide) is not the kind of card that she likes, but there are many people who do like this effect. We also knew, as we were working on *Eldritch Moon*, how important [Infinite Obliteration](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infinite+Obliteration) was against the Eldrazi decks. This card gave a new version of it that had other implications since you can hit noncreatures, but it still dodges artifacts to not totally negate new Johnny decks in *Kaladesh*.

* * *

**Noxious Gearhulk**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Noxious+Gearhulk)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noxious+Gearhulk)

KEN: Once in a while you'd want to kill your own guy for the life gain, but you can't.  
 ID: Good point. Do we want "another," "opponent controls," or "may" here? I guess let's try "may" for now.  
 DEL: The current "you may" and "an opponent controls" feels off. If there isn't a specific reason to have both, pick one?  
 AF: Ian's comment makes me think removing "opponent" is the desired choice right now. That sounds cooler to me.  
 ID: Okay, I went with "you may" and "another."  
 SPS: With Emrakul in the format, I am glad that this can't kill itself.

Emrakul is not a weak *Magic* card, and we have spent some time in the upcoming sets thinking about how she interacts with cards and making sure cards like this have some amount of play against her.

* * *

**Cathartic Reunion**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cathartic+Reunion)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cathartic+Reunion)

SM: Too much [Tormenting Voice](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormenting+Voice), trying new numbers, instant?  
 ID: 3R -> 2R.  
 KEN: Could this (in addition or instead) add red mana to your mana pool? I'm not sure what "Chandra and Pia hug and cry" would do mechanically, but I can imagine lots of red mana happening.  
 ID: 2R -> 1R. Hoping that's still reasonable.  
 ID: Instant -> sorcery, just forgot to change it.

We put [Tormenting Voice](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormenting+Voice) in a lot of sets because it is sort of the "perfect" red card in a similar way that [Inspired Charge](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspired+Charge) is "perfect" for white. It's a simple effect that adds a lot to Limited. This was an attempt to find another variant we could use, but also one that may have more of an impact in Constructed. Also, as interesting as Ken's suggestion is, I don't know how much room [Cathartic Reunion](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cathartic+Reunion) has in older formats to be any stronger. The only thing more terrifying than giving Dredge the ability to discard two Gravetrolls and draw three cards might be giving it the mana to immediately cast another one or even flashback a [Faithless Looting](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faithless+Looting).

* * *

**Start Your Engines**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Start+Your+Engines)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Start+Your+Engines)

ID: New card.  
 TJA: This card is gas.  
 TJA: But seriously folks, that first ability is a really sweet effect.

The joke practically makes itself.

* * *

**Skyship Stalker**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Skyship+Stalker)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skyship+Stalker)

TJA: Is this better or worse than [Furnace Whelp](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Whelp)?  
 SPS: [Dwarven Warriors](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dwarven+Warriors) says uncertain.

The march of progress.

* * *

**Take Down**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Take+Down)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Take+Down)

ID: Instant -> sorcery but added a mode.  
 TAB: Missing "[Take Down](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Take+Down) deals 2 damage to some of the creatures with flying."

Look, man, not every card can do *everything*.

* * *

**Commencement of Festivities**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Commencement+of+Festivities)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Commencement+of+Festivities)

TJA: After reading the previous card (+1/+1 counter, energy), I wonder about the proliferation of random cookies. (Continuing to read, there's also "destroy an artifact, gain life" and "[Rampant Growth](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth), get energy.")  
 JDR: Agreed. The set is already really heavy on them, so I'd love to cut the ones that aren't needed to support a theme.

One of the challenges of making a set is trying to make enough cards that feel "new"

without cluttering the set up with a lot of random text that doesn't go anywhere. We don't want to trick players, especially in Limited, into thinking that there is a deck you can draft because we are giving you a reward, but it was just there to make a card look and feel new. There isn't a ton of need to wow people with exciting lines of text on a Fog variant, so it left here.

* * *

**Arborback Stomper**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arborback+Stomper)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arborback+Stomper)

ID: New card for A+.  
 BrH: Welcome back, [Thragtusk](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thragtusk). We missed you!  
 MJJ: Since he lost his 3/3, he prefers the name "Thrag."  
 ID: "You can just carry one spear...you'll probably be fine." —Rakgom, Kaladeshi Hunter

One thing we attempted to do with *Kaladesh* was to print more really appealing uncommons that were powerful by themselves without a ton of context. Simple cards that look exciting—cards like this, [Aerial Responder](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aerial+Responder), and [Essence Extraction](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Extraction). For newer or returning players, it's very nice to have cards that don't need a ton of context to be awesome.

* * *

**Blossoming Defense**

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blossoming+Defense)](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blossoming+Defense)

ID: New card, more generous [Ranger's Guile](https://web.archive.org/web/20161014000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ranger%27s+Guile).  
 DH: Wow, this is big jump on a Limited card I already like. Not sure how else to do this as an uncommon, but surprised...  
 KEN: Possibly for Modern Green-Blue Infect.

We don't playtest for Modern, but that's not to say we can't see a good thing when it's in front of us.

* * *

That's it for this week. *Kaladesh* has many artifacts, so I'll be back next week to talk about gold cards, artifacts, and lands.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))