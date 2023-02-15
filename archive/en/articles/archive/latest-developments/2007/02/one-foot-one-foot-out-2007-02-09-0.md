
---
[Link to Wayback Machine](https://web.archive.org/web/20190304153728/https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "Hello!Planar Chaos lead developer Devin Low here, leaping at the chance to talk about some Planar Chaos development techniques while Aaron is out of the office. The development team knew going in that making the alternate color pie work would not be easy."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "612376"
[_metadata_:publish_date]:- "2007-02-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "One Foot In, One Foot Out"
[_metadata_:wayback_capture_timestamp]:- "2019-03-04 15:37:28"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20190304153728id_/https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/one-foot-one-foot-out-2007-02-09-0"
---


One Foot In, One Foot Out
=========================



 Posted in **Latest Developments**
 on February 9, 2007 






![](https://web.archive.org/web/20190304153736im_/https://magic.wizards.com/sites/mtg/files/styles/auth_small/public/images/person/authorpic_DevinLow.jpg?itok=6mfVM74z)
By Devin Low











Hello!*Planar Chaos* lead developer Devin Low here, leaping at the chance to talk about some *Planar Chaos* development techniques while Aaron is out of the office. The development team knew going in that making the alternate color pie work would not be easy. We could set all the structure and color rules we wanted, but we knew the set would only be loved by the public if the color shifts "felt right." But how can you possibly make white counterspells and blue discard spells "feel right?" Fortunately, the design team discovered a technique to do just that: 


>  *To make a classic mechanic feel right in a new color, combine it with a dose of what you're used to in that color, creating a card that is part groundbreaking and part familiar.*

The development team loved the tactic, upheld it, and even deployed it on a couple more cards. The result is a group of cards that have one foot in Magic's classic color pie and one foot in the *Planar Chaos* alternate color pie – the best of both worlds. I'll focus first on how we applied this to white counterspells and blue discard spells and then take a quick spin exploring how we used the technique across the other colors.

### Something Old, Something New

![Rewind](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rewind)We planned *Planar Chaos* very carefully, and when a major mechanic switches colors in the set, it always does so with at least three cards. Green flying? Three cards. Black tapping target creature? Three cards. Red bouncing enemy creatures? Three cards. That three-card-minimum helps ensure that specific mechanics move to specific places, and it's not just mass hysteria with every color doing everything. So when the design team pitched moving counterspells into white, we knew that it would have to be at least 3 cards. If you just picked a few random counterspells to move into white, you might end up with white [Rewind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind), white [Spelljack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spelljack), and white [Prohibit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prohibit). If you think about opening those spells in a *Planar Chaos* pack, it would feel totally wrong. Why? Because each of those isn't just a counterspell, it's a very non-white-feeling counterspell. [Rewind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind) untaps 4 lands – not white at all.

[Spelljack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spelljack) lets you steal your opponent's spell and hurl back at her – not white at all. 

[Prohibit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prohibit) hates small spells – not white at all.

So what makes the white counterspells we did pick feel white?

**[Rebuff the Wicked](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set1.jpg)

The actual card [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) would be a jarring card to print in *Planar Chaos* White. There's nothing white about it. But [Rebuff the Wicked](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked) both plays into the white theme of "Protect my guys" and plays almost exactly like the common staple [Shelter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shelter).If you cast [Rebuff the Wicked](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked), it "feels right" because you're doing something white always does. You're just using traditionally blue tools to do it.

**[Dawn Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dawn+Charm)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set2.jpg)

Just as [Rebuff the Wicked](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebuff+the+Wicked) replicates white's ability to protect its creatures, white's second counterspell embodies white's ability to protect itself. Just compare to the similar answer to burn spells and discard effects: [Gilded Light](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gilded+Light). Put another way, [Dawn Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dawn+Charm) is an instant [Ivory Mask](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Mask), giving a nice white feel to cushion the otherwise bizarre impact of a white [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell).

**[Mana Tithe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Tithe)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set3.jpg)

"Mana taxing" has been part of White's color pie for ages. Recent highlights include [Grand Arbiter Augustin IV](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grand+Arbiter+Augustin+IV), the techy [Suppression Field](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Suppression+Field), and the moving of [Propaganda](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Propaganda) into white as Ghostly Prison. But white mana taxing goes all the way back to the obscure [Glowrider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glowrider), the powerful Aura of Silence, and even *The Dark*'s Brainwash. White's version of [Force Spike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike) is basically an instant variant Aura of Silence. "Your spell costs one more mana. Oh, hadn't I mentioned that? Oh, you don't have any more mana to pay?"

What's that they say about death and taxes?

### Something Borrowed, Something Blue

Printing [Stupor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stupor) in blue would be utterly bizarre. What would blue be doing with this random-discard spell? Instead, the blue discard spells have one foot in classic blue to give that comforting familiarity, even as the other foot's in the *Planar Chaos* alternate color pie of blue discard effects.

**[Wistful Thinking](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wistful+Thinking)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set4.jpg)

Blue has had card drawing/filtering spells like [Compulsive Research](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), [Careful Study](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Study), and [Merfolk Looter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter) for years. Some, like [Compulsive Research](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), let you target another player to help an ally or deck an opponent. It's amazing how changing just the numbers and the targeting on [Sift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift) transforms it from a card-filtering spell into a discard spell that often plays more like [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot). Because you're used to blue getting "draw and discard" effects, it still feels blue. Want to see [Wistful Thinking](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wistful+Thinking) do something that [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) can't? Just combine it with [Megrim](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Megrim).

**[Dismal Failure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set5.jpg)

Tacking "discard a card" at the end of a vanilla spell seems like it would have to feel black, the color of [Ravenous Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ravenous+Rats) and [Cackling Fiend](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cackling+Fiend). But [Dismal Failure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure) is such a beautiful mirror of [Dismiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss) that it feels totally natural. Black Knight wouldn't normally get away with being a black two-mana 2/2 with two awesome abilities, but his symmetrical mirroring of [White Knight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=White+Knight) makes it seem perfectly natural. [Call of the Herd](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Call%2Bof%2Bthe%2BHerd)ed "Evil [Dismiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss)" during development and given its clever real name by the flavor text crew, [Dismal Failure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismal+Failure) is [Dismiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss)'s Black Knight.

**[Venarian Glimmer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venarian+Glimmer)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set6.jpg)

This is one is awfully subtle. Once the observant figure it out, they tend to appreciate it. A blue coercion sounds like a stretch... maybe you can justify it by saying it combines blue telepathy with black discard? Sketchy. Things snap into focus when you hear its playtest name: "Proactive [Spell Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Blast)" It's basically "[Spell Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Blast) target spell... in your hand!" Having one foot in a well-known blue effect definitely helps this spell feel right.

### Highlight Reel

There isn't room to list every *Planar Chaos* card that used this technique. Let me quickly run you through some highlights from each color. If you look, you'll find a few more on your own.

**[Sunlance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set7.jpg)

Before [Time Spiral](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Spiral) Block, if you asked players what cards they expected to see printed in white, I very much doubt anyone would say "A white burn spell that deals 3 to a creature for one mana!" White weenie decks have been splashing mountains for red burn spells ever since "PT Jank" decks tore up Grand Prix on the back of [Soltari Priest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Priest), all the way to today, with Boros Deck Wins living up to its name on the back of, well, [Soltari Priest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Priest). So what makes this white creature-kill spell and its friends [Saltblast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltblast) and [Serra's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra%27s+Boon) feel at home in white? All these cards hearken back to older spells like Holy Light, [Exile](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exile), [Blinding Light](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Light), and [Crackdown](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crackdown). [Sunlance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance) follows in their footsteps... in a much more powerful way.

When the design team was searching for ways to do "Destroy target nonwhite creature" in *Planar Chaos* white, they looked to see what nostalgic spells they could tweak to get what they wanted. White [Dark Banishing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) would be the simplest, but it just didn't "feel right." Instead the designers went back to a color-shifted [Strafe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strafe) as [Sunlance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunlance), a tweaked [Phyrexian Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Boon) as [Serra's Boon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra%27s+Boon), and a nonwhite-clause [Desert Twister](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desert+Twister) as [Saltblast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltblast).

**[Saltfield Recluse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltfield+Recluse)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set8.jpg)

After years of appearing very rarely on cards, -X/-0 (or "shrink") has finally settled down in blue's color pie with recent cards like [Bewilder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bewilder), [Meishin, the Mind Cage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meishin%2C+the+Mind+Cage), and [Oboro Envoy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oboro+Envoy). [Saltfield Recluse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saltfield+Recluse) "feels right" in white despite using a blue ability because it's doing something so clearly white in philosophy – protecting you and your creatures – and doing so in such a white way, with a little creature's free tap ability. Extra points if you recognized its numerical homage to classic powerful *Urza's Saga* draft common [Sanctum Custodian](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctum+Custodian).

**[Body Double](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Body+Double)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set9.jpg)

This one is pretty straightforward. How do you justify moving [Zombify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) into blue? By making the [Zombify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) effect actually a [Clone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone) effect. With playtest name "Death Clone," we'd actually tried to put this card into earlier Magic sets in straight blue. *Planar Chaos*' color-shifting theme gave it the perfect home, as a blue card with one foot in blue and one foot in black.

**[Magus of the Coffers](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magus+of+the+Coffers)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set10.jpg)

A creature that taps to produce mana is the most iconic green color pie ability of all time, and almost zero nongreen creatures have ever had it. (Thank you, [Sisters of the Flame](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sisters+of+the+Flame).) But this card feels so right in black that hardly anyone even thinks of it as a color-shifted card at all. No one notices that it's mechanically closer to Rofellos than to any black creature.

**[Molten Firebird](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Molten+Firebird)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set11.jpg)

If this card were a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 2/2 Spirit with the same abilities, it would seem ludicrously non-red, even in *Planar Chaos*. White, black, and green all contain mechanics and philosophies that deal with bringing the dead back to life or reincarnation, but red really doesn't at all – in "regular red" *or* "*Planar Chaos* red." Flying is also almost absent from both regular red and *Planar Chaos* red. So what is a flying reincarnator doing in red, either in *Planar Chaos* red or regular red? Why would we move Ivory Gargoyle here instead of to black? The flavor is the key. Phoenixes are such an iconic fantasy monster, and their abilities fit our game so well, that we love to express them mechanically as Magic cards. The fantasy flavor of Phoenixes is tightly so tied to fire, and fire is tied so tightly to Magic's red, that we've long made creatures like [Shard Phoenix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shard+Phoenix) and Bogardan Phoenix red cards, even though their reincarnation and flying abilities otherwise have nothing to do with red mechanically. As both a reincarnator and a flier and a 2/2, Ivory Gargoyle's mechanics are the perfect fit to a red phoenix. The fact that red already has the [Jokulhaups](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jokulhaups) effects that made Ivory Gargoyle powerful is just gravy.

**[Utopia Vow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Vow)**

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af157_set12.jpg)

Monogreen removal? The concept sounds weird at first, but most players find this card very natural as soon as they see it cast. The reason is that in gameplay it feels less like "Pacify your man," and more like "Turn your guy into a Bird of Paradise." What color should make things into [Utopia Tree](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Utopia+Tree)s? Green, of course.

So that's the story of how many color-shifted *Planar Chaos* cards were made to "feel right" by keeping one foot in the old color pie even as they stuck an exploratory foot into *Planar Chaos*' alternate color pie. Come back next week when Aaron returns from tromping his actual feet across a bunch of actual pies. (Yeah, he's twisted like that.)

![Serra Sphinx](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Serra+Sphinx)





