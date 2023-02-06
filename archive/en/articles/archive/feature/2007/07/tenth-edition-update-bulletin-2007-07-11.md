
---
[Link to Wayback Machine](https://web.archive.org/web/20170116181505/http://magic.wizards.com/en/articles/archive/feature/tenth-edition-update-bulletin-2007-07-11)

[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/tenth-edition-update-bulletin-2007-07-11"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170116181505id_/http://magic.wizards.com/en/articles/archive/feature/tenth-edition-update-bulletin-2007-07-11"
[_metadata_:wayback_capture_timestamp]:- "2017-01-16 18:15:05+00:00"
[_metadata_:description]:- "What is Oracle?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2007-07-11"
---


*Tenth Edition* Update Bulletin
===============================



 Posted in **Feature**
 on July 11, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/generic-avatar-150_240.png)
By Mark L. Gottlieb













|  |
| --- |
| **What is Oracle?**
**Magic** is a game made up of over 9,000 interchangeable pieces—the cards. Over the years, we've felt the need to update the wordings of older cards, whether because we've introduced a new keyword, or a card was printed with a mistake, or we have a clearer wording for what a card does, etc. Rather than sneak into your room at night and change your cards with a magic marker, we keep a database of the "modern wordings" (what the cards would say if we printed them today) of every tournament-legal card ever printed. These wordings are considered the official wordings of the cards, and accurately reflect their functions.
You can access a card's Oracle wording by looking it up in Gatherer.
**What are the Comprehensive Rules?**
**Magic** is complicated. No, really. When you have over 9,000 interchangeable game pieces, you get some freaky interactions. The Comprehensive Rules cover everything the game has ever come up with, from basic game play structure, to every keyword ever, to entire pages dedicated to single bizarre cards (hello, [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver)!) The Comprehensive Rules are, well, comprehensive... but they're also obtuse, unfriendly, and looooong. They're not intended to be a player resource—they're a judge resource, a rules guru resource, and a place to store definitive answers. In fact, I recommend never reading them. For a much friendlier rulebook that is intended to be a player resource, check out the [*Tenth Edition* Basic Rulebook (2MB PDF)](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/rules/MagicRulebook_10E_EN.pdf). It doesn't have sections about phasing or subgames... but you'll never miss them. |

The release of each new **Magic** set comes packaged with two updates to the **Magic** infrastructure: an update to the Comprehensive Rules, and an update to the Oracle card database.This coincides with set releases for a simple reason: The new cards cause us to change these things anyway! The new cards (or, in the case of a Core Set, the updated cards) are incorporated into Oracle, and the Comp Rules get revised to handle new keywords, new card types, new bizarre cards, and so on. As long as we're monkeying with Oracle and the Comp Rules for new business, we might as well take care of some old business at the same time.

Recent updates have been a surprise—you'd find out that we changed the functionality of [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) or [Great Whale](/en/articles/archive/latest-developments/power-level-errata-b-gone-2006-07-14-0) on the day that it actually happened. This was seen as a bad policy. So now we're giving you a bit of a heads-up. This document details the notable changes that will be implemented when *Tenth Edition* is released on Friday, July 13. (There are some other minor updates to wording or formatting that are not detailed here.)

### Oracle Changes

**[Phyrexian Dreadnought](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Dreadnought)**  
The Dreadnought was printed with a comes-into-play ability. You could play it, pop [Pandemonium](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pandemonium) for 12, and then sacrifice it. Or, y'know, do some broken things instead. It got power-level errata to say that unless you sacrificed 12 power worth of creatures first, it never came into play at all. As part of our recent effort to eliminate power-level errata, we're reverting the Dreadnought to its printed functionality.

**[Natural Selection](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Natural+Selection)**  
As printed, this says to look at the top three cards of "any player's library." Typically, when a spell affects a single player of your choice, that means that it targets that player. We believe that this intends to target a player, but it's a sloppy Alpha template (like [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall)). We're changing it so that it targets a player.

**[Cruel Deceiver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Deceiver), [Venomous Fangs](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venomous+Fangs)**  
 When new keywords lifelink, reach, and shroud premiered in *Future Sight*, they were deemed "evergreen" (for use in all sets) as opposed to block-specific, and all relevant cards were updated in Oracle. The same thing did not happen to deathtouch because only two cards in history would have gotten it. But it will be an evergreen keyword, so it should get the same treatment.

**[Land Cap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Land+Cap), [Lava Tubes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Tubes), [River Delta](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+Delta), [Timberline Ridge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Timberline+Ridge), [Veldt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Veldt)**  
 These are the *Ice Age* depletion lands. As printed, they go through an uncomfortable process: When you tap one for mana, you put a depletion counter on it. It won't untap during your untap step if it has a depletion counter on it. Then you remove the depletion counter during your upkeep.

Someone very clever who preceded me found a much simpler way to implement what was going on: When you tapped one for mana, it wouldn't untap during your next untap step. That takes one third of the space to say... and it's the same thing, right?

Well, no, it's not the same thing. What if you have something that removes counters, like [Power Conduit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Power+Conduit) or [Chisei, Heart of Oceans](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chisei%2C+Heart+of+Oceans)? This was an unfounded functional change, and we're reverting these cards back to their printed functionality.

![Imagecrafter](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Imagecrafter)**[Imagecrafter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imagecrafter), [Standardize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Standardize), [Mistform Mutant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistform+Mutant)**  
 As printed, these cards told you to choose a creature type other than Legend or Wall. This was back when Legend was a creature type (now legendary is a supertype), and Walls couldn't attack (now creatures with defender can't attack, and all printed Walls happen to have defender).Once the two creature types with special rules stopped having special rules (and/or being creature types), these three cards were changed in Oracle to let you choose any creature type. But why? The printed cards still tell you that you can't choose Legend or Wall. It's now impossible to choose Legend, so that's a non-issue. But as long as the cards say not to choose Wall, we should go along with that. It doesn't mean much; it just makes the printed cards closer to true.

**[Voidstone Gargoyle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voidstone+Gargoyle)**  
[Pithing Needle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle) is getting a new template in *Tenth Edition* that's both shorter *and* more comprehensive. (Yes, we're geniuses.) [Voidstone Gargoyle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voidstone+Gargoyle) has much the same ability, so it's getting updated to the same wording. This does involve a functional change, but the only time it's relevant is if someone wants to play the activated ability of a *copy* of [Lightning Storm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Storm) on the stack, and [Lightning Storm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Storm) is the named card. (After the update, you won't be able to play the ability.)

**[Norritt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Norritt)**  
[Norritt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Norritt) is getting a functional change—it's changing from not functional to functional! Its current Oracle wording has a paradox that makes the card broken: There's a play restriction that's dependant on knowing what the target of the ability is. You can't choose the target until after you start playing the ability... but you can't start playing the ability until after you know what the target is. It's getting fixed.

***Tenth Edition* Creature Types**  
 If I counted correctly, 39 *Tenth Edition* cards are getting their creature types updated, in accordance with the current race-class creature type policy. The tricky thing is that I can't tell you what they are, because this document is intended to educate and elucidate, not to spoil 39 *Tenth Edition* cards. Here's what I can tell you, so you'll be less surprised when it happens:




* All artifact creatures in *Tenth Edition* that previously had no creature types... are getting some creature types!
* All legendary creatures in *Tenth Edition* that previously had no creature types... are getting some creature types! (Such cards had the creature type "Legend" when they were originally printed.)
* All lands and artifacts in *Tenth Edition* with abilities that turn themselves into creatures will have creature types while animated.
* 16 creatures in *Tenth Edition* are getting the race "Human" added to their type line, with no other changes.
* The subtype "Lord" is being phased out. All creatures in this set that previously appeared with "Lord" in their type lines will no longer be Lords.

There are some other changes (a creature is gaining the Metathran race, a creature with Nomad in its name is gaining the Nomad subtype, and so on), but that covers the bulk of it.

### Comprehensive Rules Changes

**Rule 101.4a, Rule 600.5**  
 The multiplayer mulligan rules are changing. Now all multiplayer formats will employ the "free" mulligan that Two-Headed Giant does: Your first mulligan is to another hand of seven cards. Your second mulligan drops you to six cards, and so on.

![Gemstone Caverns](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gemstone+Caverns)**Rule 101.5**  
 There's now a clear section describing when to put cards such as [Gemstone Caverns](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gemstone+Caverns) and the *Guildpact* Leylines into play before the game begins.**Rule 104.6**  
 The section on symbols now has a rule that covers the card type symbols that appear in the upper left corner of the "timeshifted" *Future Sight* cards.

**Rule 212.6b**  
 The rule about when you can play a land got a minor clarification so it's true in Two-Headed Giant.

**Rule 216.2**  
 The rule says that tokens aren't cards. It was expanded to cover [the tokens in *Tenth Edition* booster packs](/en/articles/archive/tenth-editions-tips-tricks-tokens-2007-06-18), not just the ones from the *Unglued* set.

**Rule 217.5a**  
 This rule talks about placement of cards in the in-play zone. It basically says to keep your stuff in front of you, except for Auras attached to your opponent's permanents. The language was loosened up since Auras that get attached to weirder stuff (your opponent, a card in your opponent's graveyard) have started to appear.

**Rule 310.4, Rule 413.2i**  
 We know what happens to a spell on the stack when it finishes resolving—it's put into play (if it's a permanent spell) or its owner's graveyard (if it's an instant or sorcery). But no rules covered what happened to an ability on the stack or to combat damage on the stack. These rules now specify that these two objects cease to exist after they resolve. They don't go to any other zones.

**Rule 503.10**  
 This rule now specifies who the owner of a copy of a spell is. It's the player who controlled the spell or ability that created the copy.

![Shahrazad](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shahrazad)**Rule 506**  
 This rule covers subgames. According to the current rules, when a subgame is finished, all the cards in the subgame are shuffled back into the respective main game libraries... except cards removed from the game in the subgame. Those cards stay removed from the game. That means that if you suspend a card in the subgame and the subgame ends, the card remains suspended and ticks down until you get to play it for free in the main game. Or, at least, that's what some people believe. Others have been questioning whether it's supposed to work this way, still others wondered if it worked the other way (suspend in the main game, play in the subgame), and this has been an active topic among rules gurus recently.In my opinion, the suspend interaction violates the spirit of the subgame. The subgame is a completely separate, isolated **Magic** game, and cards aren't supposed to cross the boundaries from one game to the other (unless you use a Wish, which is explicitly getting something from *outside* the game you're in). This is a loophole caused by increased use of the (increasingly inaccurately named) removed-from-the-game zone. The nice thing about being the **Magic** Rules Manager is that my opinions have a funny way of becoming the truth, and this section has been rewritten to stop those shenanigans, and hopefully to be clearer overall. (For obvious reasons, no one had paid much attention to this section in a while. The only cards that create subgames are [Shahrazad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shahrazad) and [Enter the Dungeon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enter+the+Dungeon).)







