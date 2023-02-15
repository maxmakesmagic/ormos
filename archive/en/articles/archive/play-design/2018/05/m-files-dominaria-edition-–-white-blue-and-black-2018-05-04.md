
---
[Link to Wayback Machine](https://web.archive.org/web/20180504152829/https://magic.wizards.com/en/articles/archive/play-design/m-files-dominaria-edition-%E2%80%93-white-blue-and-black-2018-05-04)

[_metadata_:author]:- "Dan Musser"
[_metadata_:description]:- "Look behind the scenes and see how some of the most exciting cards in Dominaria came to be."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1284871"
[_metadata_:publish_date]:- "2018-05-04"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The M-Files: Dominaria Edition – White, Blue, and Black"
[_metadata_:wayback_capture_timestamp]:- "2018-05-04 15:28:29"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20180504152829id_/https://magic.wizards.com/en/articles/archive/play-design/m-files-dominaria-edition-%E2%80%93-white-blue-and-black-2018-05-04"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/play-design/m-files-dominaria-edition-%E2%80%93-white-blue-and-black-2018-05-04"
---


The M-Files: Dominaria Edition – White, Blue, and Black
=======================================================



 Posted in **Play Design**
 on May 4, 2018 






![](https://web.archive.org/web/20180504152851im_/https://magic.wizards.com/sites/mtg/files/styles/auth_small/public/images/person/authorpic_Dan-Musser.jpg?itok=5s5WOAJD)
By Dan Musser




 A former tournament grinder from Ohio, Dan is currently part of the Play Design team within Magic R&D. 






![](https://media.wizards.com/2016/images/daily/Mfiles2016.jpg)


Welcome to the M-Files, *Dominaria* edition! Now, you might be asking yourself, "What on earth is an M-File?" Honestly, when I first read this article series penned by Melissa DeTora, I just assumed that the M was her first initial. I didn't really assume she was just naming an article series after herself, but it wasn't obvious where the name came from. It turns out, the program we used to use to store all of the mystical data about current, future, and past *Magic: The Gathering* cards was dubbed the Multiverse. Since the beginning of the series, we've switched to a different program called Drake. I wonder if that means the name of this series should also be changed? The D-Files. Hmm, D and M are both my initials. We'll see  . . . 


Oh, right, I am quite new here and might need a small introduction. My name is Dan Musser, and I joined the Play Design team in 2017 after traveling the world playing this beautiful game for years. I hail from Ohio, where I started playing *Magic* during *Stronghold*. Modern is my favorite format, Thought-Knot Seer is my favorite card, and green is my favorite color. Also, cats rule!


But enough about me. Let's dive right in and take a look at some of the design and development commentary on some *Dominaria* card files from about a year ago.


For brevity, names have been initialed. Click below to meet the commenters.




Click to Reveal
---------------






![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_davehumphreys.jpg) **DGH**—Dave Humpherys, lead set designer.


![](https://media.wizards.com/2015/images/daily/authorpic_ethanfleisher.jpg) **EEF**—Ethan Fleischer, lead exploratory designer


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_kellydigges.jpg) **KD**—Kelly Digges, lead writer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_aaronforsythe.jpg) **AF**—Aaron Forsythe, senior director of R&D


![](https://media.wizards.com/2015/images/daily/Bryan_Hawley.jpg)**Bryan**—Bryan Hawley, play designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_kennagle.jpg)**KEN**—Ken Nagle, set designer


![](https://media.wizards.com/2016/images/daily/authorpic_Eli-Shiffrin.jpg)**Eli**—Eli Shiffrin, set designer and rules manager


![](https://media.wizards.com/2016/images/daily/mfiles_alli_medwin.jpg)**Alli**—Alli Medwin, *Magic Online* editor


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_matttabak.jpg)**Tabak**—Matt Tabak, senior editor


![](https://media.wizards.com/2016/images/daily/mfiles_melissa-detora.jpg)**MDT**—Melissa DeTora, play designer


![](https://media.wizards.com/2016/images/daily/mfiles_glenn-jones.jpg)**GJ**—Glenn Jones, set designer and editor


![](https://media.wizards.com/2017/images/daily/authorpic_andrewbrown.jpg)**ABro**—Andrew Brown, play designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_dougbeyer.jpg)**DougB**—Doug Beyer, creative lead


![](https://media.wizards.com/2016/images/daily/Jules_Robbins.jpg)**JDR**—Jules Robins, designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke, Play Design lead


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—Erik Lauer, co–lead set designer


![](https://media.wizards.com/2015/images/daily/authorpic_YoniSkolnik.jpg)**YS**—Yoni Skolnik, set designer


![](https://media.wizards.com/images/magic/daily/authorpics/authorpic_markglobus.jpg)**MJG**—Mark Globus, product architect


![](https://media.wizards.com/2018/images/daily/authorpicM_Dan-Musser.jpg)**DMus**—Dan Musser, play designer


![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_monsjohnson.jpg)**MJJ**—Mons Johnson, *Duel Masters* lead developer


![](https://media.wizards.com/2017/images/daily/authorpic_natmoes.jpg)**NKM**—Nat Moes, editor






**Tragic Poet**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tragic+Poet)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tragic+Poet)
DGH: Tragic Poet seems like a very good reprint given Sagas flavor with name, from Dominaria set, etc.


DGH: Reprint Urza's Legacy.


EEF: I love this reprint.


KD: Very flavorful and charming.


AF: "Ohh, tell us about Nicol Bolas again!" "Hmmm  . . .   okay." (dies)


KD: She works herself to death writing her magnum opus. Sad!


Bryan: Really cool reprint with Sagas in the set.


Talk about a perfect reprint! Originally from a Dominaria set? Check. Interacts with a major set mechanic? Check. I hope she returns the Saga The Eldest Reborn so she can come back and see how her magnum opus was received.




---

**Dub**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dub)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dub)
DGH: New from Ethan.


DGH: Changed instant to Aura.


KEN: 1W? :)


Eli: What is the cost "to dub" a creature? Two-dub.


Bryan: Extremely resonant. Love it.


DGH: I miss the name "Dub" here.


Alli: Also miss "Dub." It's elegant, simple, and not likely to be used elsewhere. This feels like it could be just top-down from that name.


Eli: Also loving "Dub."


Tabak: With that mana cost? "To Dub" I'd buy.


All right, there is a bit of R&D shorthand going on here, so let's break it down. When we reference mana costs on cards, we speak the number of the colorless part of the cost followed by the letter(s) form the colored part of the cost. The letter W is quite a mouthful to say, which leads us to shortening it even further, to simply "dub." Playtest names are usually cute and generally get their meaning across; however, they often get changed to something more creatively resonant. Dub costing 2W was such a perfect balance of wit, flavor, and simple elegance that it made it all the way to print without having to break from the original design.




---

**Seal Away**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seal+Away)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seal+Away)
DGH: Journey to Nowhere variant, cares about creatures up to 4 power.


DGH: Up to 4 power at color pie request.


MDT: I found this to be weak in FFL so far.


DGH: Might want to change to exile target tapped/attacking creature as long as in play.


EEF: FFL meeting: 1W Flash, exile a tapped creature an opponent controls until CARDNAME leaves the battlefield?


GJ: Changed.


Pro Tour *Hour of Devastation* took place around the same time that Seal Away was going through its paces in FFL. Hazoret the Fervent was the all-star of that Pro Tour, and we had a removal spell that wasn't quite pulling its weight. These factors combined brought forth a new addition to the Play Design process. We can now add targeted cards later down the line to keep certain other cards or strategies in check.




---

**Benalish Marshal**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Benalish+Marshal)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Marshal)
DGH: New card from Standard mini-teams.


ABro: Glorious.


Another example of the new processes. With the expansion of the Play Design team over the last year, we have been able to run focused "mini-teams." This is when portions of R&D split off into small groups, each with a set of specific goals. Here, a team was built to brainstorm and design a bunch of standard power level cards. This takes some of the weight off of the Set Design team and allows Play Design to really flex its creative muscles. Also, Andrew Brown coming in with the pun.




---

**Healing Grace**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Healing+Grace)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Healing+Grace)
DGH: Changed to effectively choose both.


DougB: Creatively I really like associating dmg prevention with life gain like this, FWIW. The resonant "laying on hands" art for prevention effects is an odd match mechanically, since damage isn't really healed.


GJ: Dave: Should this be able to protect planeswalkers?


DGH: No, not unless clean words.


Tabak: I think "creature, planeswalker, or player" is fairly clean. If it's not, I have bad news about burn spells. :)


GJ: The words would be exactly as Tabak suggests, so I think it's easy to do; just wasn't within the prescribed scope of cards I'd automatically update.


DGH: Okay, changed to those words.


ABro: Thanks to Play Design we can make stronger cards. Alpha power creep, yw.


Talk about power creeping on Healing Salve! Interestingly, Healing Grace here was being developed around the same time we decided to do away with the planeswalker redirection rule and let direct damage spells target planeswalkers instead. To further power creep Healing Salve, Glenn wanted this to be able to prevent damage to planeswalkers as well. It turned out the words would end up cleaner than anyone expected  . . .   Sorry, Healing Salve (#notsorry).




---

**Tolarian Scholar**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tolarian+Scholar)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Scholar)
DGH: Moved down to 3 mana.


JDR: Wizards that are just about attacking and blocking are still super strange to me. I imagine there are limited implications.


DGH: Note makes sense. We are in tough spot where what makes this card Limited playable is that it has the hidden text "This counts as a Wizard," something we do for vanillas at times.


In *Magic* terms, a "vanilla" creature is one with a text box that is blank except for flavor text. Tolarian Scholar appears to be a vanilla creature, but since one of the Limited themes is "Wizards matter," this scholar here is more than meets the eye. What kind of vanilla should that be called?




---

**Arcane Flight**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arcane+Flight)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcane+Flight)
DGH: Going for something simple.


EEF: Simple and appealing.


DGH: Combo with vanilla legend.


ABro: P1P1 Yargle, P2P1 thiiiisssssss.


It doesn't get much simpler than this. Sorry, Flight, you'll have to take a back seat to your arcane cousin. There's nothing quite like enchanting your beloved house cat with some glowing wings and letting them zip across the skies. Also, tossing this on a Yargle, Glutton of Urbog is some serious business! Ten ya.




---

**In Bolas's Clutches**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=In+Bolas%27s+Clutches)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=In+Bolas%27s+Clutches)
DGH: New design that seemed fun in theme.


DGH: Sounds like this might want to show Liliana, which then works better.


DGH: Added legendary.


ABro: Awesome that this triggers historic.


I always thought Bolas was capable of clutching many things. Historic describes legendaries, artifacts, and Sagas. Here, we get a non-Saga enchantment that gets to be historic as well. Adding Liliana to the art gave us a delightful peek at a truly awesome story moment  . . .   for Nicol Bolas.




---

**Naban, Dean of Iteration**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Naban%2C+Dean+of+Iteration)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naban%2C+Dean+of+Iteration)
DGH: New from Andrew B. Fits pretty well with what's going on in set, lots of Wizards do have ETBs here. Somewhat weird words. Will excite people with Snapcaster.


DGH: Could use some opinions on this card. Is this too narrow? Is it cool if enough Wizards here have ETBs? Is it weird given Panharmincon is around another 6 months?


Eli: It inspires me to find Wizards with cool ETBs to build a deck around. It's pretty narrow, but narrow in an encouraging way that reminds me of when I was a new player discovering new ways to think about building decks.


Eli: Does anything break with Arcane Adaptation from XLN teaching all of your creatures Wizardly ways?


ID: Nothing that wouldn't already break with Panharmonicon.


Nice one, Andrew! Wizardharmonicon. If you put enough Wizards together in a room, sometimes magic just  . . .   happens. Wizards developing cards for other Wizards. Could this be Wizardception?




---

**Zahid, Djinn of the Lamp**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Zahid%2C+Djinn+of+the+Lamp)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zahid%2C+Djinn+of+the+Lamp)
EEF: New card by Ethan Fleischer.


EVL: Nice!


Eli: Some Lamp Djinns emerge from Vehicles. They have the easy life.


YS: Awesome!


DGH: Does this card want there to be a lamp in the set?


MJG: Cool concept, though I agree that a lamp doing this could be cooler.


DGH: Added legendary.


DGH: Should this be noncreature artifact?


Eli: Thoughts on tapping a creature and an artifact plus 2U for the cost? The creature has to rub the artifact.


DGH: Going to Eli's suggestion


ID: Strong with Pirates that make Treasure. FFL also liked 3U and 5/6.


KD: 5/6 has upside for the Moti callback.


DGH: Going to 3U and 5/6 then if that's on the table.


DGH: Don't have to tap creature as part of cost (again).


The flavor of Zahid, Djinn of the Lamp is extraordinary. I was sad when I first read that we took away the cost that you had to tap a creature in order to activate this. It seemed so fitting for the creature to rub the artifact to get the Djinn out. The reason that was removed was twofold. From a gameplay perspective, it wasn't strong enough, and why would you actually need a creature to rub the lamp? You are a Planeswalker! You pay 3U and YOU rub the lamp  . . .   I hope Mahamoti Djinn isn't too upset.




---

**Windgrace Acolyte**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Windgrace+Acolyte)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windgrace+Acolyte)
ABro: Flying cat warrior? Is creature typing correct/possible?


Eli: Concept checks out, it's a cat riding a dinosaur.


ABro: Okay I know nothing.


DMus: Are you ABro or ASno?


In Andrew's defense, neither Cats nor Warriors are normally depicted flying through the air. Unless they get enchanted with Arcane Flight, of course. While his question might seem silly, we do visit a lot of worlds, and maybe on some of them cats DO fly. Here we just have a Cat riding a dinosaur, obviously.




---

**Fungal Infection**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fungal+Infection)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fungal+Infection)
EEF: I really like this card.


GJ: Charming.


Alli: This didn't take long to grow on me. Big fan.


KEN: Deathspore Thallid's best impression of Blister Beetle.


MJJ: This seems quite nice vs mono-red.


Simple. Powerful. Charming. Soon it'll grow on you, too. Play Design loves having answers in place for powerful cards, and this is one of the cleanest answers to a turn-one Llanowar Elves.




---

**Final Parting**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Final+Parting)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Final+Parting)
DGH: New design. Callback toward Demonic Tutor and Buried Alive. Jarad's Orders that can hit noncreatures.


KD: This is really cool.


EEF: Very cool design.


DGH: Gets Liliana + reanimation target. Might be better than we think.


DGH: Does this need to exile itself?


NKM: I will get Yawgmoth's Will and Tendrils. (I think this is strong but fine.)


Nat is our resident Vintage aficionado, and having someone like him in R&D is valuable to the process of creating *Magic* cards for everyone. The last time we stapled Demonic Tutor and Dark Ritual together, it had a huge effect on Eternal formats. Will Final Parting have the same impact?




---

**Josu Vess, Lich Knight**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Josu+Vess%2C+Lich+Knight)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Josu+Vess%2C+Lich+Knight)
YS: I like this a lot!


MJG: Cool, but 12 mana is a lot.


Alli: I've had this guy in my deck in multiple playtests in different archetypes, and not once have I come even close to kicking it. Agree with MJG that 12 is too much.


YS: I'd still like this at 10 mana total.


DGH: Will move down to 11 mana for now.


DGH: Cut a mana off the kicker.


DGH: Added Zombie to token type based on rare poll feedback.


MJJ: Now that's a text box.


DougB: Rad.


DGH: 4/4 -> 4/5.


ABro: Can't have its glory brought. Sorry Glorybringer.


Josu here is another example of us making a change based on what is happening in real-world competitive *Magic*. With Glorybringer seeing significant play, we wanted to make sure you didn't curve Josu right into your opponent's Dragon and get a case of the feel-bads. Adding a point of toughness was a more flavorful change than making this into a Dragon. Will you live the dream of kicking this for the full 20 power worth of creatures?




---

**Yargle, Glutton of Urborg**


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Yargle%2C+Glutton+of+Urborg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yargle%2C+Glutton+of+Urborg)
DGH: Legendary Vanilla


KEN: Secret game text "This deals commander damage".


Alli: Another one to check off the P/T matrix!


GJ: So, Human Insect Frog Spirit?


Another secret non-vanilla creature, as Ken points out. Yargle here is the first creature with this specific power and toughness combination. The story of how a lowly Frog became a legend and eventually the mascot of all of Dominaria is an awe-inspiring tale.




---

Looks like that is all we have time for today. Come back next week when we finish with red, green, multicolor, artifacts, and lands!


See you then,


Dan Musser


[@daniis7](https://twitter.com/@daniis7)







