
---
[Link to Wayback Machine](https://web.archive.org/web/20160624151556/http://magic.wizards.com/en/articles/archive/latest-developments/mrakul-files-developing-emrakul-2016-06-24)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Sam walks through the steps it took to develop Emrakul into the vexing enigma she is today."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1031286"
[_metadata_:publish_date]:- "2016-06-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "M’rakul Files: Developing Emrakul"
[_metadata_:wayback_capture_timestamp]:- "2016-06-24 15:15:56"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160624151556id_/http://magic.wizards.com/en/articles/archive/latest-developments/mrakul-files-developing-emrakul-2016-06-24"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/mrakul-files-developing-emrakul-2016-06-24"
---


M’rakul Files: Developing Emrakul
=================================



 Posted in **Latest Developments**
 on June 24, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






![](https://media.wizards.com/2016/images/daily/Mrakulfiles2016.jpg)


What's this? Something strange has happened to the M-Files!


Frequent readers of this column will know that Multiverse is our internal database, used to track *Magic* cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights on the design and development processes, as well as a few laughs. You'll find both here.


If you'd like to have a face to put with each name, click below to review our cast of commenters:




Click to reveal
---------------






![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_kennagle.jpg)**KEN**—Ken Nagle, *Eldritch Moon* lead designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_samstoddard.jpg)**SPS**—Sam Stoddard, that's-a me!


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—Erik Lauer, head developer


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_dellaugel.jpg)**DEL**—Del Laugel, editor


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_monsjohnson.jpg)**MJJ**—Mons Johnson, *Duel Masters* developer


![](https://media.wizards.com/2015/images/daily/authorpic_shawnmain.jpg)**SM**—Shawn Main, designer


![](https://media.wizards.com/2015/images/daily/Bryan_Hawley.jpg)**BrH**—Bryan Hawley, developer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_matttabak.jpg)**TABAK**—Matt Tabak, rules manager


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_gavinverhey.jpg)**GSV**—Gavin Verhey, Beyond the Basics columnist and designer


![](https://media.wizards.com/2016/images/daily/Jules_Robbins.jpg)**JDR**—Jules Robins, design intern


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_timaten.jpg)**TJA**—Tim Aten, *Shadows* lead editor






The original idea behind the *Shadows over Innistrad* block came from an off-site where different people within *Magic* R&D pitched ideas for formats, products, design principles, and worlds. Adam Lee pitched the idea of an Innistrad where Emrakul had corrupted things. A sort of cosmic-horror version of the world. It was a huge hit, and one that quickly made its way into our lineup of future world plans.


When working on the *Shadows over Innistrad* world, it was decided that we would spend the first set trying to discover the mystery of what was driving Innistrad insane, and then the second one with the reveal that Emrakul was behind it the whole time. That put a lot of pressure to create a version of Emrakul that was amazing, but different from the first one. The first version Ken Nagle, the set's lead designer, put into his *Eldritch Moon* design file looked like this:


Emrakul, the Promised End  

{13}  

Legendary Creature - Eldrazi  

13/13  

When you cast CARDNAME, exile all nonland permanents your opponents control.  

Flying, trample  

You may cast nonland cards exiled by CARDNAME by spending mana as though it were mana of any color to cast those cards.


Making a 13/13 for thirteen mana was basically a requirement. We needed to find a way to make the card impactful, without it being about reanimating or sneaking it into play like the first one. There was just no way we were going to top [Emrakul, the Aeons Torn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emrakul%2C+the+Aeons+Torn)'s "over-the-topness." The best we could aim for was to top it in playability in "fair" decks, and to make it cool in a way other than the "the game just ends" sense that the original Emrakul showed.


KEN: Might be too much like an Ulamog card (eating, though it's trying to be brainwashing), but trying to put most of the power in the cast trigger.


KEN: Now more ridiculous and hurts nonbasics, hoping it's a trump in the control mirror where you can get to thirteen mana, but maybe Ulamog or Kozilek already is that.


KEN: Cleaned up some text.


KEN: A thirteen-mana card is a blank in all our Limited playtests. Trying a cost reduction.


Ken wasn't wrong here. While this version of Emrakul was more impressive on some level than an Ulamog card, it felt like a souped-up version, rather than its own thing. It also wasn't doing what Emrakul was known for doing—warping physiology. We also had one other big question: both *Rise of the Eldrazi* and *Battle for Zendikar* were built around casting huge creatures with converted mana costs of 10 and higher—*Shadows over Innistrad* wasn't. That meant we needed to find some way to actually cast her. During design, Ben Hayes came up with a novel idea that played with the idea of delirum in the block, counting card types but letting you go beyond four.


Emrakul, Mother of Aberration  

Legendary Creature - Eldrazi  

13/13  

CARDNAME costs 1 less to cast for each different card type among cards in your graveyard. (Card types are artifact, enchantment, creature, land, instant, sorcery, planeswalker, and tribal.)  

Flying, incurable (This can't be exiled or returned to its owner's hand.)  

When you cast CARDNAME, gain control of target permanent.


KEN: Better cast trigger to test the upper limit. Steals two things.


KEN: Instead of two things, now can steal a permanent of each type (since it already lists the card types in reminder text).


KEN: New incurable.


Emrakul, Mother of Aberration  

Legendary Creature - Eldrazi  

13/13  

CARDNAME costs 1 less to cast for each card type in your graveyard. (Card types are artifact, enchantment, creature, land, instant, sorcery, planeswalker, and tribal.)  

When you cast CARDNAME, for each permanent type, gain control of target permanent of that type.  

Flying, incurable (This can't be exiled, returned to its owner's hand, or put into a library from the battlefield.)


Incurable was an early idea for a mechanic that could be a different kind of protection on creatures. Kind of like indestructible, for the opposite kind of spells. Very powerful with an [Upheaval](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Upheaval), rather than a [Wrath of God](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God). It was interesting, but a very hard mechanic to implement in the middle of a block. After all, the power would be largely based on the kinds of removal in *Shadows over Innistrad*, which was still very far from being completed. In the end, we abandoned the idea, but I wouldn't be surprised to see it or something like it someday.


SPS: Except for incurable, I love this.


KEN: Had this cast against me in Sealed and it felt social media-worthy. I still won but just barely.


KEN: Now tramples because my Spider and Spirit tokens let me survive against this. Emrakul has a legacy to uphold and needs to be the scariest thing in the Multiverse to fight against.


KEN: Cut incurable


EVL: Usually we let you get your cards back if you kill the thing that took them. Is that a bad story fit?


KEN: Then it's 1-for-1 against Murder. A better fix is she steals one thing. Ulamog and Kozilek offer 3-for-1s or better, and Emrakul is supposed to be "scarier."


DEL: "Up to one target" so that the ability can go on the stack if a permanent type is missing from the battlefield?


It was around this time that I took over the file, as the set moved from design to development. While the card was serviceable and I loved the cost-reduction mechanic, I didn't like the trigger very much. One of the things we do in development is run mini teams, where each member of the development team runs a small team with different people from around R&D and tries to improve the set. For *Eldritch Moon*, Melissa DeTora ran a mini team focusing on ensuring we'd be happy to have more card designs from the file see play in Constructed.


SPS: New version from the MDT miniteam.


SPS: trying without hexproof


The new version looked like this—much closer to the final version.


Emrakul, The Promised End  

{13}  

Legendary Creature - Eldrazi  

13/13  

CARDNAME costs one less to cast for each card type in your graveyard.  

When you cast CARDNAME, you control target opponent during his or her next turn. After that turn, that opponent takes an extra turn.  

Flying


The idea of a [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver) was great. Emrakul was, after all, controlling the minds of a ton of the denizens of Innistrad—so why should the Planeswalkers be immune? Getting another turn after that meant that it wasn't a surefire death sentence like [Emrakul, the Aeons Torn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emrakul%2C+the+Aeons+Torn)'s cast trigger in *Rise of the Eldrazi*. There was a lot of counterplay here, but it was very fun. You often won when you cast Emrakul, but not every time. That was important.


MJJ: Cold to sweepers/edicts, this might want something extra.


SM: Love the [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver) plus extra turn.


KEN: Does it want "you control target opponent until the end of that opponent's next turn. After that turn, that player takes an extra turn." This way she hits the table while you are controlling your opponent and she'll survive instant kill spells and edicts for at least a turn, like [Dragonlord Dromoka](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragonlord+Dromoka). She also lets you attack that turn for upside. Other [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver)s aren't active while you are attacking.


That was a fascinating suggestion from Ken. We hadn't really thought of something like that. It was a very novel line of text, so I decided to put it into the set.


Emrakul, The Promised End  

{13}  

Legendary Creature - Eldrazi  

13/13  

CARDNAME costs {1} less to cast for each card type among cards in your graveyard.  

When you cast CARDNAME, gain control of target opponent until the end of that player's next turn. After that turn, that player takes an extra turn.  

Flying, Trample


SPS: taking KEN's suggestion - now until the end of that player's next turn.


BrH: Having Emrakul die to [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) seems wrong to me. I'd like a protection ability here.


TABAK: I believe that [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) may be headed...elsewhere.


KEN: This was pretty fair in Future Future League compared to Ulamog. You get to run their best guy into the 13/13 which is flavorful, but it often won't save you against go-wide aggro. Maybe the control/combo matchups make up for it.


TABAK: Flashing this in during an opponent's upkeep is really good. You control them for like three weeks.


EVL: Should this be along the lines "until that player's next end of turn"?


GSV: Awesome. Worthy of the Emrakul name.


This version was very popular, and powerful—but it had a number of problems. The first was digital, where it was going to be a ton of work to implement. It turns out that switching control in the middle of a turn is a lot harder than switching control for an entire turn. If that were the whole problem, though, we would've kept it. The largest problem with the card was discovered when two decks playing it faced each other in the FFL. While the effect itself was brain-melty, when you cast the card and the opponent had one in their hand, all of a sudden we ended up with nested-control turns. It was just more than was really reasonable.


JDR: If we go with one of the alternatives that doesn't grant immediate control, can we make it clearer what the end result is? Something like, "When you cast Emrakul, target opponent takes an extra turn after this one. You control that player during that turn."


![](https://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_Z2nLZiWA1l.png)


Emrakul, The Promised End  

{13}  

Legendary Creature - Eldrazi  

13/13  

Emrakul, the Promised End costs {o1} less to cast for each card type among cards in your graveyard.  

When you cast Emrakul, you gain control of target opponent during that player's next turn. After that turn, that player takes an extra turn.  

Flying, trample, protection from instants


TJA: Now just a regular [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver). Also protection from instants.


KEN: Can still be [Cancel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel)ed despite protection from instants. :(


In the end, we felt that this card was plenty strong but also made for an overall more satisfying play experience. We added protection from instants so that it wouldn't die to [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade). We wanted a card that was worthy of the Emrakul name, but also one that wasn't as overpowered as the first one, and that you could actually cast in decks—not just cheat onto the battlefield. In the end, I am very happy with how she turned out, and I hope you all are too.


That's it for this week. I hope you are as excited for *Eldritch Moon* as I am for you to see it. Next week, I'll be back with a new preview card, as the season will be in full swing.  
  

Until next time,


Sam ([@samstod](http://www.twitter.com/samstod))







