---
id: gna26acm
kind: article
lang: en
path: /en/articles/feature/2009/01-29-january-2009-update-bulletin-5
title: January 2009 Update Bulletin
published: '2009-01-29'
column_slug: feature
column: Feature
authors:
- slug: markgottlieb
  name: Mark Gottlieb
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/23c
    lang_detected: en
    capture_id: 172459
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
    captured_at: '2012-04-18 00:33:45+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/23c
    lang_detected: en
    capture_id: 172459
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
    captured_at: '2012-04-18 00:33:45+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/23c
    lang_detected: en
    capture_id: 172459
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
    captured_at: '2012-04-18 00:33:45+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/23c
    lang_detected: en
    capture_id: 172459
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
    captured_at: '2012-04-18 00:33:45+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: gna26acm
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/23c
  lang: en
  template: aspx
  captured_at: '2012-04-18 00:33:45+00'
  capture_id: 172459
  wayback_url: https://web.archive.org/web/20120418003345id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gna26acm
  capture_id: 172459
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
  wayback_url: https://web.archive.org/web/20120418003345id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/23c&page=2
  captured_at: '2012-04-18 00:33:45+00'
  template: aspx
  sha256: 057bca0d08499f3374446662ca8e7cd7167700cbdbad23e39cca9f2bc5ae8074
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Balance
  - Restore Balance
  - Eye for an Eye
  - Freyalise's Winds
  - Temporal Distortion
  - Gilded Drake
  - Stifle
  - Guardian Beast
  - White Ward
  - Pyramids
  - Rebound
  - Silver Wyvern
  - Seeds of Strength
  - Torchling
  - Shaman en -Kor
  - Sorrow's Path
  - City of Brass
  - Tainted Specter
  - Temporal Aperture
  - Unstable Shapeshifter
  occurrences: 46
---
### Functional Oracle Changes

 **Balance**  
 Balance's current Oracle wording seems to have you sacrifice lands in stages, one after the other, until you reach the required number. But the printed card doesn't imply that. When Restore Balance was printed in *Time Spiral*, it used a more succinct, more accurate template for this ability that clearly has all land sacrifices happen simultaneously. (And creature sacrifices, and discards.) Balance is being changed to use that template too.

*New Oracle text:*  
 Each player chooses a number of lands he or she controls equal to the number of lands controlled by the player who controls the fewest, then sacrifices the rest. Players discard cards and sacrifice creatures the same way.

 **Eye for an Eye**  
 This card's timing has always been kind of fuzzy. Did you have to wait until you've been dealt damage to play it? The *Arabian Nights*, *Revised*, and *Fourth Edition* printings say yes ... but they also say that you ignore damage prevention effects that have affected the original damage. That implies a weird little time bubble. The *Fifth Edition* wording is even stranger, as it allows you to play Eye for an Eye only when you've been *assigned* damage. The current Oracle wording only adds to the strangeness. It's clearly useful only after damage has been dealt, but it counts the sum total of damage dealt to you by a single source over the course of the turn—even if it was dealt in multiple instances—which isn't how any of the printed wordings worked.

And then there's the flavor. The card is designed to exact revenge for damage dealt to you, but if that damage is enough to cause you to lose the game, you won't be able to play Eye for an Eye. And isn't that the most important time to play it? The *Fifth Edition* wording of the card promotes the concept of simultaneous damage, before the Oracle wording veers away. Can we achieve that? This is a bit of an experiment, but I'm willing to give it a shot ....

*New Oracle text:*  
 The next time a source of your choice would deal damage to you this turn, instead that source deals that much damage to you and Eye for an Eye deals that much damage to that source's controller.

 **Freyalise's Winds**  
 In the last Oracle update, I changed this card from a bad Oracle wording that spliced multiple abilities onto permanents into a card that matches Temporal Distortion. It was pointed out that it shouldn't really match Temporal Distortion. A replacement effect would be truer to the printed card than Temporal Distortion's static ability and triggered ability. 

*New Oracle text:*  
 Whenever a permanent becomes tapped, put a wind counter on it.  
 If a permanent with a wind counter on it would untap during its controller's untap step, remove all wind counters from it instead.

 **Gilded Drake**  
 Here's what's going on with this crazy card:

1) When Gilded Drake comes into play, its ability triggers. You must target a creature an opponent controls. If you can't choose a legal target, any other ability simply wouldn't go on the stack. In this case, however, you must sacrifice Gilded Drake.  
 2) As the triggered ability resolves, the game checks to see if its target is still legal. If it isn't, any other ability would be countered and nothing would happen. In this case, however, you must sacrifice Gilded Drake.  
 3) If the target is still legal, you exchange control of that creature and Gilded Drake. Or you can choose to sacrifice Gilded Drake.

Part 1 (and the latter half of part 3) are currently being achieved by a modal wording. If there are no legal targets, you can't choose the mode with a target in it, so you have to choose to sacrifice Gilded Drake. I think the same thing can be more simply achieved by a "choose up to one" targeting restriction. Right now, Gilded Drake says to sacrifice it in two different ways; with the new wording, it just says it once.

Part 2 is currently being achieved with the bizarre and unprecedented line "This ability can't be countered." The intent of this line is that the ability can't be countered *by the game rules* for having no legal targets. Unfortunately, it's also covering effects of spells and abilities like Stifle. Stifle should be able to counter Gilded Drake's ability.

*New Oracle text:*  
 Flying  
 When Gilded Drake comes into play, exchange control of Gilded Drake and up to one target creature an opponent controls. If you don't make an exchange, sacrifice Gilded Drake. This ability can't be countered except by spells and abilities. *(This effect doesn't end at end of turn.)*

 **Guardian Beast**  
 As printed, Guardian Beast could prevent your noncreature artifacts from being *further* enchanted, but it wouldn't affect Auras already on those artifacts. Its current Oracle wording says that noncreature artifacts you control can't be enchanted, which means Auras on those artifacts would fall off. I'm adding a line to the template that's borrowed (and modified) from cards like White Ward.

*New Oracle text:*  
 As long as Guardian Beast is untapped, noncreature artifacts you control can't be enchanted, they're indestructible, and other players can't gain control of them. This effect doesn't remove Auras already attached to those artifacts.

 **Pyramids**  
 As printed, Pyramids prevented a land from being destroyed. It currently regenerates that land, but it shouldn't, because the printed wording wouldn't cause that land to become tapped. There was a proposal on one of the boards for "The next time target land would be destroyed this turn, instead it isn't." That doesn't work because if that land is also a creature, and the reason it would be destroyed is because it's been dealt lethal damage, "instead it isn't" doesn't clear the damage off the land and it'll immediately be destroyed again as a state-based effect. But the following should work.

Also, as printed, Pyramids had a single ability. It was broken up in Oracle to two separate abilities just for ease of use. You choose which ability you're using at the time you play one of them. If it were modal, you'd choose which mode you're using at the time you play the ability. The difference is negligible. But modal activated abilities do exist, so we might as well stay as true to the printed card as possible.

*New Oracle text:*  
 {2}: Choose one — Destroy target Aura attached to a land; or the next time target land would be destroyed this turn, remove all damage from it instead.

 **Rebound & Silver Wyvern**  
 The printed wordings of these cards' abilities lets them affect spells like Seeds of Strength, which have multiple targets that all target the same thing. The Oracle wording (which predates Seeds of Strength) does not. The target-changing ability seen on Torchling (which can affect Seeds of Strength) is actually quite similar to the printed wordings of these cards, so it's being implemented here.

*New Silver Wyvern Oracle text:*  
 Flying  
 {U}: Change the target of target spell or ability that targets only Silver Wyvern. The new target must be a creature.

*New Rebound Oracle text:*  
 Change the target of target spell that targets only a player. The new target must be a player.

 **Shaman *en*-Kor**  
 A damage prevention or redirection effect usually says "source of your choice" when the source of the applicable damage is locked in at the time the effect is created, and just "source" if it determines the source when applicable damage is dealt. This is a case of the former, but the Oracle text doesn't say "of your choice." It's being brought in line with the standard modern-day template for its printed wording.

*New Oracle text:*  
 {0}: The next 1 damage that would be dealt to Shaman *en-*Kor this turn is dealt to target creature you control instead.  
 {1W}: The next time a source of your choice would deal damage to target creature this turn, that damage is dealt to Shaman *en-*Kor instead. 

 **Sorrow's Path**  
 As printed, Sorrow's Path had a fascinating line break. It looked like this:

> {T}: Exchange two of opponent's  
>  blocking creatures. This exchange  
>  may not cause an illegal block.  
>  Sorrow's Path does 2 damage to  
>  you and 2 damage to each creature  
>  you control whenever it is tapped.

Was that one ability or two? Sorrow's Path predated half-line spaces between abilities, so when looking at the actual card, there was no way to tell whether this was all a single activated ability or the first three lines were an activated ability and the last three lines were a separate triggered ability. Players at the time commonly interpreted the card as having two abilities, both because the second ability parsed better that way, and because that interpretation made the card not completely useless. (Mark Rosewater, for one, liked to give it to his opponent somehow and then force it to become tapped.)

In Oracle, however, it's all one ability. This is supported by the original typesetting file for the card ... but that doesn't necessarily signify that it was two abilities. City of Brass's two abilities were fused into a single paragraph in its *Arabian Nights* printing, but they were interpreted as two separate abilities, and the card was reprinted with correct line breaks in *Chronicles*.

There's no smoking gun here, but this is a case where the Oracle wording should reflect the reality of how players actually played the card, especially when their interpretation is entirely justified by the printed wording.

*New Oracle text:*  
 {T}: Choose two target blocking creatures an opponent controls. If each of those creatures could block all creatures that the other is blocking, remove both of them from combat. Each one then blocks all creatures the other was blocking.  
 Whenever Sorrow's Path becomes tapped, it deals 2 damage to you and each creature you control.

 **Tainted Specter**  
 Tainted Specter's Oracle wording currently has a player put a card from her or her hand into the graveyard without using the word "discard." It shouldn't.

*New Oracle text:*  
 Flying  
 {1BB}, {T}: Target player discards a card unless he or she puts a card from his or her hand on top of his or her library. If that player discards a card this way, Tainted Specter deals 1 damage to each creature and each player. Play this ability only any time you could play a sorcery.

 **Temporal Aperture**  
 When its ability resolved, it momentarily revealed the top card of your library. It then immediately stopped revealing it, but required you to keep track of it while it's face down on top of your library, and even to play it while it was face down. This was weird, but didn't bother anyone. However, there's a rules tweak in this update regarding keeping track of cards in your library that makes that functionality untenable. Temporal Aperture will now specify that the card it reveals stays revealed.

*New Oracle text:*  
 {5}, {T}: Shuffle your library and reveal the top card. Until end of turn, as long as that card remains on top of your library, play with the top card of your library revealed and you may play that card without paying its mana cost. *(If it has X in its mana cost, X is 0.)*

 **Unstable Shapeshifter**  
 Unstable Shapeshifter's ability will trigger when Unstable Shapeshifter itself comes into play. It will become a copy of itself and keep its ability, meaning it will have two versions of that ability. The next time a creature comes into play, both versions of this ability will trigger. First one will resolve, causing it to become a copy of the new creature and retain its ability, then the other will resolve, causing the exact same thing to happen. It'll then be down to one copy of its ability, and will work as you'd expect. Having it trigger on itself is unnecessary, confusing, and really just seems to be an oversight. It certainly doesn't serve any greater purpose, so this card is getting errata to not do that.

*New Oracle text:*  
 Whenever another creature comes into play, Unstable Shapeshifter becomes a copy of that creature and gains this ability.

[Introduction](/en/articles/feature/2009/01-29-january-2009-update-bulletin-3)  
 [Functional Oracle Changes](/en/articles/feature/2009/01-29-january-2009-update-bulletin-5)  
 [Übertemplating Oracle Changes](/en/articles/feature/2009/01-29-january-2009-update-bulletin-2)  
 [Other Nonfunctional Oracle Changes](/en/articles/feature/2009/01-29-january-2009-update-bulletin)  
 [Comprehensive Rules Changes](/en/articles/feature/2009/01-29-january-2009-update-bulletin-6)