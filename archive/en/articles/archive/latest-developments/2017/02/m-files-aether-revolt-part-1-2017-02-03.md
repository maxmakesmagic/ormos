
---
[Link to Wayback Machine](https://web.archive.org/web/20170203171554/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-aether-revolt-part-1-2017-02-03)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Sam begins his series of card-by-card development stories for Aether Revolt."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1123021"
[_metadata_:publish_date]:- "2017-02-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "M-Files: Aether Revolt, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2017-02-03 17:15:54"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170203171554id_/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-aether-revolt-part-1-2017-02-03"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/m-files-aether-revolt-part-1-2017-02-03"
---


M-Files: Aether Revolt, Part 1
==============================



 Posted in **Latest Developments**
 on February 3, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






![](https://media.wizards.com/2016/images/daily/Mfiles2016.jpg)


It's time once again to return to the M-Files! Frequent readers of this column will know that Drake (formerly called "Multiverse") is our internal database, used to track *Magic* cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Drake and leaving comments. Looking back on the file a year later provides insights on the design and development processes, as well as a few laughs. You'll find both here.


If you'd like to have a face to put with each name, click below to review our cast of commenters:




Click to reveal
---------------






![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_mago.jpg)**MAGO**—Mark Gottlieb, lead designer for *Aether Revolt*


![](https://media.wizards.com/2017/images/daily/authorpic_benhayes.jpg)**BH**—Ben Hayes, lead developer for *Aether Revolt*


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_kennagle.jpg)**KEN**—Ken Nagle, designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_timaten.jpg)**TJA**—Tim Aten, former editor and seven-day *Jeopardy!* champion


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_dellaugel.jpg)**DEL**—Del Laugel, editor


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_samstoddard.jpg)**SPS**—That's-a me!


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_markglobus.jpg)**MJG**—Mark Globus, product architect


![](https://media.wizards.com/2016/images/daily/Jules_Robbins.jpg)**JDR**—Jules Robins, designer


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—Erik Lauer, head developer


![](https://media.wizards.com/2015/images/daily/authorpic_ethanfleisher.jpg)**EEF**—Ethan Fleisher, designer


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_adamprosak.jpg)**AP**—Adam Prosak, developer


![](https://media.wizards.com/2016/images/daily/mfiles_melissa-detora.jpg)**MDT** - Melissa DeTora, playtester


![](https://media.wizards.com/2017/images/daily/authorpic_scottvanessen.jpg)**SVE**—Scott Van Essen, *Duel Masters* designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke, developer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_matttabak.jpg)**TABAK**—Matt Tabak, editor


![](https://media.wizards.com/2015/images/daily/Bryan_Hawley.jpg)**BRH**—Bryan Hawley, developer






  

With that out of the way, let's get to the cards!


**Audacious Infiltrator**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Audacious+Infiltrator)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Audacious+Infiltrator)
KEN: I've been pretty happy with this line of text on a 3/1 in token-and-4/4-Vehicle world.


EEF: Agreed. My general concern with a 1W 3/1 is that it will trade down with a token. This feels good to me.


Due to the higher-than-average number of 1/1 tokens in *Kaladesh* block, we had real problems getting 1-toughness creatures without any evasion to be strong enough in Limited. Lines of text like this one let is easily get past those Servos, and have some splash damage against other artifact-heavy decks.




---

**Inspiring Roar**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Inspiring+Roar)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspiring+Roar)
MAGO: Common spell in which Ajani helps his comrades. This could also be 1W, "Put a +1/+1 counter on up to two target creatures you control," or the like. Affecting the team seems more appropriate to the player experience level than "up to two targets."


One thing we have attempted to do in sets recently is to find places to get our Planeswalker characters onto cards at the highest frequency possible. That means finding commons that can do something a particular character would do. In this set, Mark Gottlieb, the set's lead designer, created a card early on that could highlight Ajani.




---

**Countless Gears Renegade**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Countless+Gears+Renegade)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Countless+Gears+Renegade)
EEF: This looks like a lot of value for a common. Too much, to be honest.


TJA: Though achieving revolt status isn't a given, a 3/2 and two 1/1s for four mana doesn't feel common to me.


It can be hard to get cards to the right power level for Limited. We like to push mechanics to some extent, and we can have cards that are balanced enough for Limited but are just too swingy to be the best common in a color. For a long time, this was a 3W 3/2 that made two 1/1s with revolt, but that was just too much. It was well below the bar without revolt, and above it with it. Instead of moving the card to uncommon, we found a better spot where we could be happy with the card not being too swingy.




---

**Caught in the Brights**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Caught+in+the+Brights)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caught+in+the+Brights)
*(Was "When a Vehicle enters the battlefield under your control, exile enchanted creature.")*


MAGO: New last ability that calls out Vehicles.


SPS: wut?


MAGO: Changed trigger from ETB to attack. Now works with a Vehicle you already had, so it eliminates a sequencing issue.


MJG: Weird card.


JDR: Flavor makes more sense to me as destruction.


EVL: Nice top-down design.


EEF: This card isn't very strong, but it's really fun when you get it to work. I love it.


This was a cute card from the start, and one that we protected in development. I believe that it's important that when we find charming designs like this, we do our best to keep them around.




---

**Felidar Guardian**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Felidar+Guardian)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Felidar+Guardian)
TJA: Two of these (or one plus a [Clone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone) effect) go infinite. Is that problematic?


DEL: Arbitrarily large, but at least they wouldn't draw the game.


Technically, infinite is different than an arbitrary large number. Three [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring)s with no other nonland permanents actually do go infinite, and the game ends in a draw. This combo lets you repeat it over and over again. Tim made this comment, but we weren't that worried about two copies of this creating an infinite number of ETB triggers. You'd need a third card to go infinite. We did miss the interaction with Saheeli, however, and that has led to some . . . interesting decks in Standard. While we were pushing for more combo decks in Standard with *Aether Revolt*, this is not the kind of deck we would intentionally take a risk with. In hindsight, [Felidar Guardian](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Felidar+Guardian) definitely should've said "creature or artifact." [Pro Tour *Aether Revolt*](http://magic.wizards.com/en/events/coverage/ptaer) is this weekend, and we'll be watching to see how these decks do.




---

**Metallic Rebuke**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Metallic+Rebuke)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metallic+Rebuke)
BH: [Cancel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) > [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak).


EEF: It amuses me that this mechanic does nothing with Moxen and artifact lands.


AP: I'm sure Moxen and artifact lands are doing fine without the help of new mechanics.


Early in *Aether Revolt* development, we talked about including affinity for artifacts but ended up pulling it back to artifact convoke. Ethan is our resident Vintage fan, so having an incredibly powerful artifact-based mechanic that didn't break the world in Vintage was amusing to him.




---

**Trophy Mage**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trophy+Mage)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trophy+Mage)
SPS: "Search your cube for a non-[Batterskull](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Batterskull) Equipment . . ."


MAGO: Continuation of the super-cycle. One to go!


ID: Nice one. High chance it's too strong, though. Converted mana cost 1 and converted mana cost 6-plus are quite restrictive. This one lets you get the artifacts you actually want to get. Worth testing, though.


MDT: I agree with ID that this is likely too strong although I love continuing the cycle.


GSV: I don't know that this needs to stay "2 or 3" (it could be just CMC 2), but I definitely like preserving this if possible. Fun, inventive, and will put a smile on some players' faces.


JDR: Have we charted out names for the rest of this cycle? We don't want to end up with the only fitting names being something bigger than an existing member that tutors for a higher CMC.


DEL: Too early to be thinking about real card names, but dev lead could mention during toplining.


BH: All parties are acting with awareness of this card's pedigree.


Originally, this searched for a card with converted mana cost 2 or 3, which felt like way too much value. Ben's plan the entire time was to start off with those two numbers and see which was more fun for Standard and Limited, which ended up being three. Mark Gottlieb's comment about "one to go" was referencing that since we have "1 or less," "2 or 3," and "6 or more," we only needed to do a tutor for converted mana costs of 4 and 5. With the change, we opened up even more room for *T*-something Mages that get new numbers for artifacts! Who knows how many years it'll take to get to the next one, but I'm sure we will continue the tradition until we get them all. We just may need to invent a new word that starts with *T* that fits in with [Trophy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trophy+Mage), [Treasure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treasure+Mage), and [Trinket](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinket+Mage).




---

**Wind-Kin Raiders**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wind-Kin+Raiders)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind-Kin+Raiders)
BH: New artifact convoke flier.


EEF: It's like a little [Broodstar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Broodstar)!


BH: Was 4/4.


When talking about adding affinity to *Aether Revolt*, we decided that the most-fun affinity card in original *Mirrodin* block was [Broodstar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Broodstar), when just *Mirrodin* was out. That was a cute and fun deck that was strong, but didn't break the format—unlike the Affinity deck that followed with *Darksteel*.




---

**Baral, Chief of Compliance**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Baral%2C+Chief+of+Compliance)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baral%2C+Chief+of+Compliance)
EEF: This Baral guy looks like a huge jerk. Oh, he's supposed to be? Good.


Flavor win!




---

**Quicksmith Spy**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Quicksmith+Spy)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quicksmith+Spy)
BH: Trying a Grixis-color cycle of one-off metalbonders at rare.


DEL: Current text doesn't make sense. What's this meant to do?


DEL: Got it. Templated.


Another mechanic we attempted in the set was ''metalbond," which was a lot like soulbond except it gave an activated ability. It was an interesting idea, but it didn't fit with what we were trying to do in the set. Still, it's very frequent that failed mechanics make one or two good cards.




---

**Disallow**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Disallow)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disallow)
EEF: I like this. Is it expensive enough that people won't counter fetch land activations with it in Modern?


SVE: This the kind of card we should be spending our "Awesome Impactful Single-Word Name" capital on.


ID: Nice. Should this have a reprint-able name?


BH: I believe Ari has a plan that allows this to have a simple and reprintable name.


This is definitely something we think about as we near the end of work on a set—making sure that rares that seem like things we might want to reprint later get names that will make them easy to reprint. It was good that [Thoughtseize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize) was called that and not "Oona's Spite" or something; that would've prevented us from printing it in *Theros*, especially as it was so strong that we wouldn't have printed a functional reprint.




---

**Whir of Invention**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Whir+of+Invention)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whir+of+Invention)
BH: Revolt not in blue now, new artifact convoke card. I hope it's not broken.


EEF: What could possibly go wrong?


Famous last words, etc. I actually think this card is probably fine in Standard, and while there are definitely things that make it strong in Modern, at least the triple-blue cost adds some challenge to it.




---

**Fatal Push**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fatal+Push)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fatal+Push)
BH: Now a revolt removal spell. Modern maybe?


MDT: This is sweet. Modern/Legacy-playable. Not too sure the revolt matters here though.


KEN: I'm going to hear lots of "Delver got pushed" in coverage voice-over, huh?


Another card where Ben went out of his way to make sure it had an easy and evocative name because of how strong it is in non-rotating formats.




---

**Fourth Bridge Prowler**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fourth+Bridge+Prowler)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fourth+Bridge+Prowler)
BH: 1B > B


BRH: I see you've lost some weight, [Blister Beetle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blister+Beetle).


It's been working out.




---

**Frontline Rebel**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Frontline+Rebel)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frontline+Rebel)
EEF: I really like this lenticular design. (How it combines with Vehicles.)


TABAK: "CARDNAME attacks or drives each combat if able."


BH: Was 1R 3/2


AP: Wow, 2R 3/3 with "upside." The upside being that I'm more likely to make the correct play by attacking.


The running joke, which started with Mike Turian, is that "must attack" is upside text, since you should always be attacking—and now you can't forget!




---

**Ravenous Intruder**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ravenous+Intruder)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ravenous+Intruder)
BH: Was passive +1/+0 per artifact, trying [Atog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog) functional reprint.


[Atog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog) was a very lovable card, and while the creative didn't fit on this world, we did manage to get most of what people loved about the card into Standard.




---

**Ragavan**


![](https://media.wizards.com/2016/c1lRLirbrl_AER/en_rzqBW60kOg.png)


BH: Changed from Monkey Pirate to just Monkey.


I wanted to leave you with this one—and what almost was. There was real-life discussion in our offices on whether a Monkey has the cognitive faculties to decide to be a Pirate. I argued that Monkeys are, by their very nature, pretty close to Pirates; they naturally steal, swear, and sing sea shanties. But it wasn't enough, and Ragavan was relegated to being jobless forever.




---

That's it for this week. I hope you all enjoy watching [Pro Tour *Aether Revolt*](http://magic.wizards.com/en/events/coverage/ptaer). I'll be back next week to finish up the *Aether Revolt* M-Files with Part 2.


Until next time,


Sam ([@samstod](http://www.twitter.com/samstod))







