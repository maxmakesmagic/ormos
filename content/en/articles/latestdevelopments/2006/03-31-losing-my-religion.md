---
id: w2dn9y92
kind: article
lang: en
path: /en/articles/latestdevelopments/2006/03-31-losing-my-religion
title: Losing My Religion
published: '2006-03-31'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    lang_detected: en
    capture_id: 726762
    url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    captured_at: '2022-08-19 03:08:38+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    lang_detected: en
    capture_id: 726762
    url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    captured_at: '2022-08-19 03:08:38+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    lang_detected: en
    capture_id: 726762
    url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    captured_at: '2022-08-19 03:08:38+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    lang_detected: en
    capture_id: 726762
    url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
    captured_at: '2022-08-19 03:08:38+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: w2dn9y92
  url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
  lang: en
  template: drupal
  captured_at: '2022-08-19 03:08:38+00'
  capture_id: 726762
  wayback_url: https://web.archive.org/web/20220819030838id_/https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
- document_id: w2dn9y92
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af112&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af112
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:28:49+00'
  capture_id: 253002
  wayback_url: https://web.archive.org/web/20090604152849id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af112&print=true
- document_id: w2dn9y92
  url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31
  page_key: magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31
  lang: en
  template: drupal
  captured_at: '2022-05-25 04:17:38+00'
  capture_id: 726761
  wayback_url: https://web.archive.org/web/20220525041738id_/https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31
- document_id: w2dn9y92
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af112
  page_key: wizards.com/default.asp?x=mtgcom/daily/af112
  lang: en
  template: classic_asp
  captured_at: '2008-03-24 14:56:13+00'
  capture_id: 1926042
  wayback_url: https://web.archive.org/web/20080324145613id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af112
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w2dn9y92
  capture_id: 726762
  url: https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
  wayback_url: https://web.archive.org/web/20220819030838id_/https://magic.wizards.com/en/articles/archive/latest-developments/losing-my-religion-2006-03-31-0
  captured_at: '2022-08-19 03:08:38+00'
  template: drupal
  sha256: d9cfd00c76500564773f1c69e537c5133fedee6c69651892b851b12160df7ed5
render_recovery: []
---
![Orzhova, the Church of Deals](https://i.ormos.uk/5b/e0/5be0b22afb2778a0c957cda1d99402135ff2a279b31ec1d6a67fdc38552b2795.jpg)

The sinister Orzhov—a guild of many things. *Guildpact's* design team saw the guild through a lens of gothic religion, and filled it with such trappings: bats, spirits, and the keyword haunt. The creative team had fleshed out the Syndicate as a kind of oligarchy where money was king and religion was little more than a façade. And of course, the head of design *and* the creative team, Mark Rosewater, had his own vision of how the guild should play out mechanically—the so-called “bleeder” strategy, wherein the Orzhov player takes control of the game and slowly drains the opponent's resources.

It was up to development to make sure that all shone through somehow, and that it all came together in a way that made sense from a flavor and feel standpoint as well as a deckbuilding standpoint.

### What Came Before

As a player, I simply adored the *Apocalypse* set. The splashy cards all felt very powerful, drafting with it was fun as hell, and it gave people something they hadn't had in a reasonable quantity ever—enemy-colored cards.

![Spectral Lynx](https://i.ormos.uk/f2/fe/f2feaac81270a5122424eba69de5d2a61336dc30077c5a81b0682a80c0180194.jpg)

But as a designer and developer now, I can see problems in the *Apocalypse* execution. The set was too small and each color pair too unfocused to really give anything its own distinct feel. I can remember working on Black/White decks for Standard and Block Constructed at that time, and struggling mightily to make anything cohesive. Most of the commons and uncommons weren't good enough to consider, and the rares were all over the board. [Spectral Lynx](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Lynx) was a cheap beater. [Desolation Angel](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desolation+Angel) was an expensive finisher. [Vindicate](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vindicate) was a wonderful utility spell, and [Death Grasp](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Grasp) was a great [Drain Life](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life), but what kind of deck uses all of those cards? [Drain Life](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life) and [Armageddon](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armageddon) are hardly a combo. Black/White decks had to invariably include a third color (usually Dromar's Blue) to compete.

Given more knowledge and a lot more cards to work with here in *Guildpact*, we were able to simultaneously focus and diversify what Black/White was about.

We chose to focus heavily on the “bleeder” feel, and that was the theme we wanted to be evident to someone reading a card list or opening packs. [Ghost Council of Orzhova](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghost+Council+of+Orzhova) drains for a point. [Agent of Masks](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+Masks) drains for a point, as does the Church of Deals, and [Mourning Thrull](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mourning+Thrull) does so as well. [Pillory of the Sleepless](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillory+of+the+Sleepless) plinks away relentlessly, and cards like [Souls of the Faultless](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Souls+of+the+Faultless) and [Hissing Miasma](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hissing+Miasma) punish the opponent for trying to win. [Blind Hunter](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blind+Hunter) and [Shrieking Grotesque](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shrieking+Grotesque) nab resources from the opponent, and then start chipping away on the offensive.

We certainly gave “bleeding” all the tools it could want to have decks built around it, but the funny thing was that we didn't want that to be what all Orzhov decks did. Not only was being bled to death a very unfun way to lose, but we were unsure that the most vicious bleeder decks would be able to finish tournament rounds in time. So we set out to diversify what Black/White could do.

Instead of making tons of new cards—which we couldn't do, there simply wasn't room—we tried to let Orzhov cards work well with existing powerful White and Black strategies. Cheap cards like [Plagued Rusalka](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plagued+Rusalka) and [Castigate](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Castigate) complement [Dark Confidant](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Confidant). Cards that get better with other creatures, like Teysa and the Ghost Council, make *Kamigawa's* horde of good two-mana guys more appealing. [Shrieking Grotesque](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shrieking+Grotesque) and [Cry of Contrition](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cry+of+Contrition) give redundancy to a discard strategy headlined by [Hypnotic Specter](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hypnotic+Specter) and [Ravenous Rats](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ravenous+Rats). Big finishers like [Angel of Despair](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel+of+Despair) and [Debtors' Knell](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Debtors%27+Knell) make decks that use [Wrath of God](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) and [Faith's Fetters](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faith%27s+Fetters) a lot happier. Utility like [Mortify](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify) and [Orzhov Pontiff](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orzhov+Pontiff) supplement just about any strategy. And who could forget Ghost Dad? Our inclusion of Spirits in the guild was no accident, although were weren't certain what the end result would be.

As *Guildpact* was being discussed on the Internet during the first few days after the Prerelease, one poster made a comment along the lines of, “Orzhov feels really weak, like there's no deck there that makes any sense to build.” Thankfully that sentiment has not borne itself out. When someone plays a first-turn [Godless Shrine](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Godless+Shrine) against you, who knows what creepiness awaits? Whatever it is, be assured that it is powerful.

### The Haunting

![Belfry Spirit](https://i.ormos.uk/dd/71/dd714c59930488625e16f6c5a413e6f7f6d2179c72559bbeeaa50452d6be7737.jpg)

Haunt is one of the more difficult mechanics to understand that we've ever made. Developing it was no picnic, either.

The problems in parsing the mechanic lie in the fact that it is essentially a three-step process. One thing happens when the creature is played, another when it dies, and another when the haunted creature dies. Considering most of our keywords are there to shorthand *one-step* processes, the complexity of haunt should be evident.

Like most developers, I am of the mind that complexity with little or no benefit is actively bad. But I do believe that we need to continually (a) widen the scope of what the game can do and (b) challenge our players with new and interesting ways of playing. Bloodthirst and replicate are relatively simple mechanics (at least on the surface), which gave us a bit of room to try something more complicated. The end result of doing a mechanic like this (or at least I hope the end result is something like this) is that players appreciate the game itself more for being that much more fleshed-out and wide in scope and presenting interesting game situations and deckbuilding challenges to puzzle through, even if they aren't huge fans of the mechanic itself.

Plus, there are people that actually are fans of the mechanic - also very crucial.

We tried many different variations on haunt; here are a few of the more notable ones:

*   **When THIS goes to the graveyard, haunt target creature you control**. Initially you could only haunt your own creatures. This decision was made to keep the board from getting confusing (you're haunting my guy, I'm haunting your guy, we're both haunting Steve's guy, etc.), but development quickly changed it to any creature. A good change.
*   **When THIS goes to the graveyard from anywhere, haunt target creature. When the haunted creature dies, play this card for free**. This was, in effect, the simplest version, but also the most absurdly powerful. If the haunt card was countered, discarded, or put into the graveyard with dredge, the haunt triggered. It was way too good, so we had to settle on the different reminder text for haunt spells (*When this spell is put into a graveyard after resolving…*) and creatures (*When this card is put into a graveyard from play…*). This version also meant that cards could haunt and rehaunt over and over as long as creatures were in play.
*   **When the haunted creature dies, you may pay \[cost\] to \[do X\]**. We tried tacking a cost onto the haunt ability, but it was too much information to process and actually made it play worse, as you had to keep mana untapped at all times in anticipation of the haunted creature dying.
*   **When THIS comes into play, \[do X\]. When the haunted creature dies, \[do Y\]**. There was a short period time when some haunt cards did different things at different times. [Absolver Thrull](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Absolver+Thrull), for instance, regrew an enchantment when it came into play and destroyed one with its haunt ability. As if things weren't confusing enough!

It took a long time, but we managed to get the ability down to a couple lines of reminder text and working in a way that is balanced.

### Multiverse Notes

In closing, here are some of the comments from the development of Orzhov cards lifted from out Multiverse database.

**[Mortify](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify)** was in jeopardy for a short period of time for being too close to [Putrefy](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy). Later on we agreed that that similarity was a good thing, not a bad one.

> AF 10/12: We aren't using this?  
>  DAL 10/15: I like it, but I wouldn't want to make Putrefy (1BG Terminate/Oxidize) look really cookie-cutterish b/c we make this one too. That's probably no big deal.  
>  AF 12/20: Putrefy has anti-regen clause. Should this?  
>  DAL 1/10: Yes.  
>  MP 2/4: This could remove from game, very useful against reclaim[](#footnote)/phoenix angel[](#footnote).  
>  HS 3/28 Add "no regen" clause? add life gain? add anything?  
>  bs 4/5: this card is excellent where it is.

**[Belfry Spirit](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Belfry+Spirit)** began life as a Black sorcery with haunt that made two Bat tokens. Development wanted to keep White as the primary source of flying tokens, so they made it into a White creature. For a while it was cheaper and made only one token, but that wasn't cool enough.

> DAL 12/4: I can see the ALT precon now: "THIRST OF THE BATS!"  
>  MJ 12/14: Wouldn't you choose to haunt the bats you just put into play?  
>  AF 12/20: Yes. You figured it out.  
>  HS 3/23 yes, white bats.  
>  AF 3/28: What would this cost if the ability made 2 1/1's? 5 mana? Uncommon?  
>  bs 3/31: whatever token type this should be commissioned in wave 2 (create a record if it isn't there already)  
>  BD 4/12/05: As per discussions w/HS, this white creature makes black Bat tokens.  
>  AF 4/12: Awesome change.  
>  DAL 4/18: Can he be "Bat Spirit" so you can sac him with Batman[](#footnote) and in bizarre Bat tribal decks? Outside of Kamigawa, you can have dual-type spirits.  
>  HS 4/28 Team decides this is the more interesting card (compared to shrieking griffin[](#footnote)) and this is now 3 mana HS Moved Griffin to 3 mana, this guy now gives 2 bats, and cost 5, changed rarity to uncommon  
>  Del 6/15: Dev changes from 3WW to 2WW  
>  Del 6/12: Dev changes back.

![Cry of Contrition](https://i.ormos.uk/ea/ce/eaceacdb1bfe56ef2055db33ede6079aa110ebc67174b6e59f656f38427cdd22.jpg)

**[Cry of Contrition](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cry+of+Contrition)** didn't change much, but it did generate a bunch of discussion.

> bs 1/7: discard 2 might be a better idea.  
>  DAL 1/10: It is discard 2... eventually. I like the current level - it's the Skull Fracture (Flashback Discard 1) of the set.  
>  MT 3/15: Saying it is like Skull Fracture isn't going to sell me on it. Weird that it is so cheap.  
>  bs 4/5: this card seemed good in testing. haunt is very easy to pull off in constructed... as there are a number of creatures decks like to sacrifice anyway.  
>  AF 4/6: Is this the haunt effect we want to be good? Neither exciting nor fun.  
>  NH 4/16: I think there are only 3 spells with haunt...might it be worthwhile to have them all become creatures for consistency and rules simplicity?  
>  HS 4/15 I disagree with Nate from the future, and I disagree with Aaron as well. I have found this to be interesting just because it works differently than 90% of our discard cards, and there is the hope that you can get to use the haunt effect as an instant later. That said, I am concerned about power level.  
>  AF 4/18: Block planning issue... We should be able to do good discard in the RB guild.  
>  bs 4/25: this isn't broken. it seems worse than blanche[](#footnote).  
>  bs 5/2: block discard isn't very good in general. it's this card and blanche. delete should come prepared.

**[Seize the Soul](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seize+the+Soul)** was an uncommon at first, and didn't have haunt.

> DAL 4/22: Should not step on the toes of Putrefy and Wilt[](#footnote). Should say "nonblack"...."nonwhite" would actually be a cool choice here too, since it makes a white token.  
>  bs 4/25: i'm fine with either of dl's suggestions.  
>  HS 4/28 added both! (and lowered cost)  
>  AF 5/3: While I like this, I feel that by putting "nonblack nonwhite" we are making this a guild card, but it doesn't fit the mold for what gets a watermark. We could (a) give it one anyway, (b) change it back, (c) give it haunt, or (d) do nothing. I don't like (d).  
>  MT 5/10: If we gave it haunt would it be able to haunt the 1/1. That would be cool.  
>  bs 5/12: design says that this should get a guild symbol.  
>  bs 5/13: given haunt, love.  
>  DAL 5/16: Weird that the BW guild makes 1/1 flying Bat tokens and 1/1 flying Spirit tokens...art probably means this can't make a bat....  
>  MJ 5/17: this is going to be the absolute house outside of Ravnica. Destroy 2 creatures & chump a third in an opponent's attack.  
>  HS 6/2 Has this been seeing much(any?) play?  
>  Del 6/3: No room for reminder text on this card. Any chance it could be bumped up to rare?  
>  BB 6/3: would this be cooler if it made white-black spirit tokens?  
>  Del 6/3: Adding "and black" x 2 would mean that the text needs to go 1/2 pt. below min rather than 1/4 below. :(  
>  MLG 6/8: Devin mentioned this earlier... Has there ever been a set that contained two token creatures with identical stats, color, and abilities, but different types?  
>  HS 6/10 changed to rare  
>  Del 6/13: About the token thing -- no, at least not from INV forward. Token creature types are usually kept constant within the block to cut down on art costs. At this point, the art seems to lock us into having both Pegasus[](#footnote) and Spirit.

![Agent of Masks](https://i.ormos.uk/eb/62/eb62075c46aa781ab6fc972ee4f74950653d2e4b1366d7053779db408f5b4de8.jpg)

**[Agent of Masks](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+Masks)** was a common 1/1 for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) in design, and was called “Goth Sniper.” He got bigger and moved to uncommon.

> AF 12/20: This guy was common, and could go back if the bleeder thing needs more support.  
>  MR (12/21/04): This guy (along with Mummy's Wrap[](#footnote)) are the two gold cards that best define W/B. I agree that this could be moved to common if we need the W/B stronger in limited.  
>  HS 3/31 raised Cc and p/t to separate from other w/b guild cards  
>  Del 4/4: Could make better in multiplayer as "each opponent loses 1 life. You gain life equal to the life lost this way."  
>  HS 4/28 team likes del's suggestion

Believe it or not, the **Ghost Council** didn't wow everyone at first, even when it didn't cost any mana to use its ability!

> HS 12/16 This is the guild leader? I was expecting something a bit more exciting. Maybe change his ability to triggering every turn? Maybe a 2 life swap instead of 1.  
>  AF 12/20: The exciting thing about this guild leader is that he might be playable.  
>  DAL 1/10: Looks pretty exciting to me.  
>  bs 1/13: creative confirms that this meets what the guild is trying to do (and that this is reasonable for the guild leader).  
>  MT 3/22: Why no flying?  
>  HS 3/29 it needs flying?  
>  DAL 4/7: Good card  
>  NH 5/9: This guy makes me happy, but sometimes I wonder if he would feel more black/white with a lower power higher toughness?  
>  Del 6/29: Dev adds o1 to the activation cost -- which also adds a line to the card. Cutting the flavor text: “Hand over your tithe, breather.”

: dredge  
: [Firemane Angel](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firemane+Angel)  
: [Skeletal Vampire](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Vampire)  
: [Shrieking Grotesque](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shrieking+Grotesque)  
: [Castigate](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Castigate)  
: [Mortify](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify)  
: [Storm Herd](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Storm+Herd)  
: [Pillory of the Sleepless](https://web.archive.org/web/20060331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillory+of+the+Sleepless)