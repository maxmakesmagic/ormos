---
id: jg8w5a4z
kind: article
lang: en
path: /en/articles/feature/2010/01-28-january-2010-update-bulletin-5
title: January 2010 Update Bulletin
published: '2010-01-28'
column_slug: feature
column: Feature
authors:
- slug: markgottlieb
  name: Mark Gottlieb
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/75b
    lang_detected: en
    capture_id: 173398
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
    captured_at: '2012-04-16 18:29:04+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/75b
    lang_detected: en
    capture_id: 173398
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
    captured_at: '2012-04-16 18:29:04+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/75b
    lang_detected: en
    capture_id: 173398
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
    captured_at: '2012-04-16 18:29:04+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/75b
    lang_detected: en
    capture_id: 173398
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
    captured_at: '2012-04-16 18:29:04+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: jg8w5a4z
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/feature/75b
  lang: en
  template: aspx
  captured_at: '2012-04-16 18:29:04+00'
  capture_id: 173398
  wayback_url: https://web.archive.org/web/20120416182904id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jg8w5a4z
  capture_id: 173398
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
  wayback_url: https://web.archive.org/web/20120416182904id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/75b&page=2
  captured_at: '2012-04-16 18:29:04+00'
  template: aspx
  sha256: 668638a470bcba3078242c996c4f2bf8294e969ead59e53bd5a672dfd87438b7
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Backdraft
  - Bend or Break
  - Camouflage
  - Carpet of Flowers
  - Cave Tiger
  - Elvish Berserker
  - Pygmy Troll
  - Rabid Wolverines
  - Retaliation
  - Viashino Weaponsmith
  - Dark Depths
  - Sakashima the Impostor
  - Defensive Formation
  - Firestorm Phoenix
  - Brainstorm
  - Grim Reminder
  - Infernal Medusa
  - Lifeline
  - Day of Judgment
  - Lord of Tresserhorn
  - Mercadia's Downfall
  - Oath of Druids
  - Dragon Fangs
  - Darksteel Colossus
  - Power Sink
  - Ring of Renewal
  - Sneak Attack
  - Soul Echo
  - Sporogenesis
  - Sulfuric Vapors
  - Lightning Bolt
  - Pyroclasm
  - Tanglewalker
  - Victimize
  occurrences: 56
---
### Functional Oracle Changes

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>What is Oracle?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <p>&#10;                    <b>Magic</b> is a game made up of over 10,000 interchangeable pieces—the cards. Over the years, we've felt the need to update the wordings of older cards, whether because we've introduced a new keyword, or a card was printed with a mistake, or we have a clearer wording for what a card does, etc. Rather than sneak into your room at night and change your cards with a magic marker, we keep a database of the &quot;modern wordings&quot; (what the cards would say if we printed them today) of every tournament-legal card ever printed. These wordings are considered the official wordings of the cards, and accurately reflect their functions.</p>&#10;                  <p>You can access a card's Oracle wording by looking it up in <a href="https://web.archive.org/web/20100128000000/http://gatherer.wizards.com/pages/default.aspx">Gatherer</a>.</p>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

 **Backdraft**  
 The printed wording of Backdraft reads strongly like you cast it after the sorcery it's looking for has already resolved, while the Oracle wording can be cast only while that sorcery is still on the stack (and, thus, hasn't resolved yet). So let's try a wacky wording that attempts to mimic the (egads) *Legends* functionality.

*New wording*  
 Choose a player who cast one or more sorcery spells this turn. Backdraft deals damage to that player equal to half the damage dealt by one of those sorcery spells this turn, rounded down.

 **Bend or Break**  
 This is a functional change if you look at what the card says compared its new wording. But since the card has never actually been played using a strict interpretation of its printed wording, we're not really changing its functionality. We're just bringing it in line with what it's obviously supposed to do.

This is the only divvy card that affects multiple players at once. By a strict reading of its printed wording, the opponent doing the choosing in each case has to be an opponent of the spell's controller, not an opponent of whichever player is getting a pile chosen. The wording also (by strict reading) says that a player doing the choosing can choose any pile, not just a pile controlled by the intended player. We all know what it means, but that's not good enough for a pedantic guy like me. What it means has got to match what it says. Which leads (sadly? humorously?) to this:

*New wording*  
 Each player separates all lands he or she controls into two piles. For each player, one of his or her piles is chosen by one of his or her opponents of his or her choice. Destroy all lands in the chosen piles. Tap all lands in the other piles.

 **Camouflage**  
 Two changes with Camouflage. First, this should affect only your attacking creatures. That's how it was printed, but its Oracle wording let you cast it during another player's turn to affect his or her attack. You probably wouldn't want to mess with your own ability to block, but the fact is you shouldn't even have the option—and, more importantly, you certainly shouldn't be able to cast it during a multiplayer game to mess with two of your opponents. That's just not what the card does.

The other change also relates to multiplayer. The card's wording assumed that there's only one defending player and that all attacking creatures are going that player's way. It needed a better wording for multiplayer. And when I say "better," I mean "ridiculous and awful, but properly functional, at least."

*New wording*  
 Cast Camouflage only during your declare attackers step.  
 This turn, instead of declaring blockers, each defending player chooses any number of creatures he or she controls and divides them into a number of piles equal to the number of attacking creatures for whom that player is the defending player. Assign each pile to a different one of those attacking creatures at random. Each creature that can block the creature its pile is assigned to does so. *(Piles can be empty.)*

 **Carpet of Flowers**  
 As printed, this card added mana to your mana pool "during your main phase." This is something called a "phase ability," which could be used once during the stated phase. At the time of the *Sixth Edition* rules changes, all phase abilities were changed to triggered abilities that triggered "at the beginning of" the stated phase, and that's what happened to Carpet of Flowers too.

But another change happened at the same time. Before *Sixth Edition*, each turn just had one main phase, not two. (Combat was something that happened in the middle of that one main phase.) Now that each turn had two main phases, Carpet of Flowers went a little wonky. Originally, you could get the mana after combat, if you wanted. Then you couldn't, because it was changed to give you the mana at the beginning of your precombat main phase. Just reading the printed card is confusing, since the phrase "your main phase" doesn't make sense anymore. We're giving the card a new template that triggers during each of your main phases, but that you can effectively use only once per turn. Now you can get that mana after combat if you want.

*New wording*  
 At the beginning of each of your main phases, if you haven't added mana to your mana pool with Carpet of Flowers this turn, you may add up to X mana of any one color to your mana pool, where X is the number of Islands target opponent controls.

 **Cave Tiger and friends**  
 Three *Exodus* cards and three *Urza's Saga* cards were printed with the wording "Whenever a creature blocks it, \[this creature\] gets +1/+1 until end of turn" (or a close variant of that ability). Their Oracle wordings became "Whenever \[this creature\] becomes blocked, it gets +1/+1 until end of turn for each creature blocking it." I believe this is functionally different. As I read the original card, it should trigger once per creature declared as a blocker for it. Each of those triggers will resolve individually, even if a blocking creature that caused one of them to trigger has left the battlefield by then. By contrast, the Oracle wording triggers just once, and counts the number of blocking creatures when it resolves. Elvish Berserker has been left alone, since it was printed in both *Ninth Edition* and *Tenth Edition* with the new wording. But the other five cards haven't been reprinted, so they're going back to their original functionalities.

*New Cave Tiger wording*  
 Whenever Cave Tiger becomes blocked by a creature, Cave Tiger gets +1/+1 until end of turn.

*New Pygmy Troll wording*  
 Whenever Pygmy Troll becomes blocked by a creature, Pygmy Troll gets +1/+1 until end of turn.  
 {oG}: Regenerate Pygmy Troll.

*New Rabid Wolverines wording*  
 Whenever Rabid Wolverines becomes blocked by a creature, Rabid Wolverines gets +1/+1 until end of turn.

*New Retaliation wording*  
 Creatures you control have "Whenever this creature becomes blocked by a creature, this creature gets +1/+1 until end of turn." 

*New Viashino Weaponsmith wording*  
 Whenever Viashino Weaponsmith becomes blocked by a creature, Viashino Weaponsmith gets +2/+2 until end of turn.

 **Dark Depths**  
 The Marit Lage token that this card creates is inherently legendary, is inherently black, and inherently has flying, because all of those are characteristics. If you copy the token with Sakashima the Impostor, for example, Sakashima will gain those characteristics too. However, being indestructible isn't a characteristic; it's just something true about the token. That Sakashima will not be indestructible. This is wildly counterintuitive, especially since the Marit Lage tokens we printed to go along with Dark Depths say "This creature is indestructible" right on them! The determination is that this functionality loophole is an unintended oversight, and it's being corrected.

*New wording*  
 Dark Depths enters the battlefield with ten ice counters on it.  
 {o3}: Remove an ice counter from Dark Depths.  
 When Dark Depths has no ice counters on it, sacrifice it. If you do, put a legendary 20/20 black Avatar creature token with flying and "This creature is indestructible" named Marit Lage onto the battlefield.

 **Defensive Formation**  
 Two changes here. One is small: the wording used the word "instead," but it doesn't create a replacement effect, so that's being revised. The other change is substantial. As printed, Defensive Formation let you choose how creatures attacking you deal combat damage. What does that mean under the M10 rules? After some discussion, we decided that this card should work the way banding works now. In the case of double blocks, it lets you ignore damage assignment order and divide the incoming damage however you like.

*New wording*  
 Rather than the attacking player, you assign the combat damage of each creature attacking you. You can divide that creature's combat damage among any of the creatures blocking it.

 **Firestorm Phoenix**  
 This card was odd, in that it creates an unverifiable situation involving hidden information. If the Phoenix dies, it returns to its owner's hand but can't be cast again that turn. But that player can still cast a different Firestorm Phoenix from his or her hand. If that player casts a Phoenix and claims it's a different one, there's no way for the other players in the game to verify whether it is or isn't. That's just not the sort of thing we allow, so the card is changing to get a "reveal" clause. This could impact the card negatively; for example, if that player casts Brainstorm, the other players will now know whether Firestorm Phoenix winds up on top of the player's library or not (which is info they wouldn't previously have had). But on the whole, we felt that it was a necessary change.

*New wording*  
 Flying  
 If Firestorm Phoenix would be put into a graveyard from the battlefield, return Firestorm Phoenix to its owner's hand instead. Until that player's next turn, that player plays with that card revealed in his or her hand and can't play it.

 **Grim Reminder**  
 In practical terms, this isn't a functional change, but in technical terms it could be seen as one, so it's getting listed here. This card said "Search your library for a nonland card and reveal it \[...\] Then shuffle the revealed card back into your library." If you search your library, you don't actually have to find a card in this case. (The search parameters list a characteristic of the card you're looking for. In order to avoid unverifiability issues—claiming that you don't have such a card in your library can't be confirmed by your opponents since they can't see the contents of your library—you can always just "fail to find.") If you don't find a card, however, then you obviously can't reveal it, and thus can't shuffle it back into your library. That means you'd search your library without shuffling it, and that's completely out of bounds; we never allow that to happen. So of course you have to shuffle, but it's a matter of wording the card to actually accomplish that.

Luckily, the card you search for and reveal never actually leaves your library. So changing that last sentence to just "Then shuffle your library" covers all cases.

*New wording*  
 Search your library for a nonland card and reveal it. Each opponent who cast a card this turn with the same name as that card loses 6 life. Then shuffle your library.  
 {oBoB}: Return Grim Reminder from your graveyard to your hand. Activate this ability only during your upkeep. 

 **Infernal Medusa**  
 According to the printed text, the non-Wall stipulation is supposed to apply only to the situation in which Infernal Medusa is attacking, not when it's blocking. Walls don't often attack, so Infernal Medusa isn't often going to block one, and I can see why the Oracle change would have been made to shorten the text. But it's still a functional change that shouldn't be there, so it's being taken out.

*New wording*  
 Whenever Infernal Medusa blocks a creature, destroy that creature at end of combat.  
 Whenever Infernal Medusa becomes blocked by a non-Wall creature, destroy that creature at end of combat.

 **Lifeline**  
 This card has, as far as I'm concerned, the worst printed wording of all time. It makes no sense. It defies logic, parsing, common decency, and the space-time continuum. Let's start with what it says:

> Whenever a creature is put into a graveyard and a creature is in play, return that creature from your graveyard to play at end of turn.

It's not at all clear what this card should do. When should it check when the other creature is in play? Should it affect everyone (it triggers whenever a creature is put into a graveyard), or just you (it says to return it from "your graveyard")? If the former, whose control should the creatures return under? The card is so ambiguous that any answers can be justified. Previous judgments had been that Lifeline affects everyone, and that each card is returned to the battlefield under its owner's control, and we were satisfied keeping those decisions intact. But we changed the answer to the first question.

The rules state that when dealing with a leaves-the-battlefield trigger, you check the game state just before the trigger event to see what's going on. That means that if Lifeline is on the battlefield and someone casts Day of Judgment, the just-before-Day of Judgment game state allows Creature A to see that Creature B is on the battlefield, and Creature B sees that Creature A is on the battlefield, and all the other creatures can see both Creatures A and B ... basically, all creatures serve as lifelines for all other creatures, even though they all die at the same time. The old Oracle wording let all those creatures return.

This didn't seem right, and it didn't seem intuitive. The new wording checks whether another creature is on the battlefield both at the time the ability triggers and at the time the ability resolves. Another creature has to actually live to allow the dead creature to return to the battlefield later.

*New wording*  
 Whenever a creature is put into a graveyard from the battlefield, if another creature is on the battlefield, return the first card to the battlefield under its owner's control at the beginning of the next end step.

 **Lord of Tresserhorn**  
 As printed, the enters-the-battlefield ability targeted an opponent. We're restoring that functionality. That means that if the triggered ability fails to resolve for having no legal targets, you won't have to pay life or sacrifice creatures.

*New wording*  
 When Lord of Tresserhorn enters the battlefield, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards.  
 {oB}: Regenerate Lord of Tresserhorn.

 **Mercadia's Downfall**  
 This card said "Attacking creatures get +X/+0 until end of turn, where X is the number of nonbasic lands defending player controls." Since a spell returns a single value for X, this doesn't really work in a multiplayer game in which creatures are attacking different opponents. It's treating the attacking creatures collectively, when it needs to treat each attacking creature/defending player relationship individually.

*New wording*  
 Each attacking creature gets +1/+0 until end of turn for each nonbasic land defending player controls.

 **Oath of Druids**  
 As printed, the last sentence has one instance of the word "puts," meaning all the putting is a single simultaneous action. This means that revealing Dragon Fangs and Darksteel Colossus would get the Colossus to trigger the Fangs, since the Colossus is put onto the battlefield at the same time the Fangs are put into the graveyard. However, when this card was updated a couple of months ago, the ability was changed to have two instances of the word "puts." This makes putting the creature card onto the battlefield come before putting the other cards into the graveyard. That was an unintentional change, and it's being corrected.

*New wording*  
 At the beginning of each player's upkeep, that player chooses target player who controls more creatures than he or she does and is his or her opponent. The first player may reveal cards from his or her library until he or she reveals a creature card. If he or she does, that player puts that card onto the battlefield and all other cards revealed this way into his or her graveyard.

 **Power Sink**  
 As printed, Power Sink said to tap all mana-producing lands. The Oracle wording says to tap all lands. It's a marginal difference, but we can get it back to what it says it does.

*New wording*  
 Counter target spell unless its controller pays {oX}. If he or she doesn't, that player taps all lands with mana abilities he or she controls and empties his or her mana pool.

 **Ring of Renewal**  
 As printed, this card's activated ability had both the discard and the card draws in its effect. This drifted in Oracle so that the discard became part of the ability's cost. There doesn't seem to be any justification for this. If the printed wording said to discard a card "to" draw two cards, we'd interpret that nowadays as a cost. But it doesn't. If you activate this ability with an empty hand, you should just draw two cards as a result.

*New wording*  
 {o5}, {oT}: Discard a card at random, then draw two cards.

 **Sneak Attack**  
 As printed, the creature you sneak onto the battlefield gains haste forever. Most of the time, this doesn't matter, because the creature is sacrificed at the beginning of the next end step, so the Oracle wording changed to grant that creature haste just until the end of the turn. But it could matter if the creature changes control before the end step, and thus dodges the sacrifice.

*New wording*  
 {oR}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.

 **Soul Echo**  
 Like Lord of Tresserhorn, this was printed with a targeted ability that has become untargeted. We're restoring the printed functionality. Now, if the triggered ability fails to resolve for having no legal targets, Soul Echo won't be sacrificed when it has no counters on it ... at least not until your next turn begins, anyway.

*New wording*  
 Soul Echo enters the battlefield with X echo counters on it.  
 You don't lose the game for having 0 or less life.  
 At the beginning of your upkeep, sacrifice Soul Echo if there are no echo counters on it. Otherwise, target opponent may choose that for each 1 damage that would be dealt to you until your next upkeep, you remove an echo counter from Soul Echo instead.

 **Sporogenesis**  
 The printed wording of the second ability triggered only when a creature with a fungus counter is put into a graveyard. The Oracle wording had changed so it triggered whenever any creature is put into a graveyard. Practically, it makes no difference, since those extra triggers won't produce any Saprolings. But it really shouldn't trigger at all in those cases.

*New wording*  
 At the beginning of your upkeep, you may put a fungus counter on target nontoken creature.  
 Whenever a creature with a fungus counter on it is put into a graveyard from the battlefield, put a 1/1 green Saproling creature token onto the battlefield for each fungus counter on that creature.  
 When Sporogenesis leaves the battlefield, remove all fungus counters from all creatures.

 **Sulfuric Vapors**  
 Tricky card. As printed, it said "Whenever a red spell deals damage, it instead deals that amount of damage plus 1." It's quite clear what that means with respect to Lightning Bolt. But what does it mean with respect to Pyroclasm while there are three creatures on the battlefield? Pyroclasm would deal 2 damage to Creature A, 2 to Creature B, and 2 to Creature C, for a total of 6 damage. Does Sulfuric Vapors change the effect so it instead deals 7 damage (since that's 6 + 1), and if so, where does that extra damage go? Or does it change Pyroclasm's effect so it deals 3 damage (2 + 1) to Creature A, 3 to Creature B, and 3 to Creature C? Clearly, based on the Oracle wording, that's how it was ruled. OK.

The reason Sulfuric Vapors is garnering attention now is due to planeswalkers. Since the printed wording of this card didn't reference a damage recipient, it should work with regard to *any* damage recipient. That used to mean "creature or player," but now it means "permanent or player."

*New wording*  
 If a red spell would deal damage to a permanent or player, it deals that much damage plus 1 to that permanent or player instead.

 **Tanglewalker**  
 Like Mercadia's Downfall, this should treat each attacking creature/defending player relationship in a multiplayer game individually.

*New wording*  
 Each creature you control is unblockable as long as defending player controls an artifact land.

 **Victimize**  
 As printed, sacrificing a creature was part of the spell's effect. This changed in Oracle to be an additional cost. It shouldn't be. (If the printed wording said to sacrifice a creature "to" return the targeted creatures to the battlefield, that would be a different matter. But it doesn't.)

*New wording*  
 Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield tapped.

*   [Introduction](/en/articles/feature/2010/01-28-january-2010-update-bulletin-4)
*   [Functional Oracle Changes](/en/articles/feature/2010/01-28-january-2010-update-bulletin-5)
*   [Nonfunctional Oracle Changes](/en/articles/feature/2010/01-28-january-2010-update-bulletin-6)
*   [Comprehensive Rulebook Changes](/en/articles/feature/2010/01-28-january-2010-update-bulletin-3)
*   [Mark's Exploding Brain](/en/articles/feature/2010/01-28-january-2010-update-bulletin-2)