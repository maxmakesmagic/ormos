
---
[Link to Wayback Machine](https://web.archive.org/web/20160727164114/http://magic.wizards.com/en/articles/archive/magic-digital/emrakul-runnings-2016-07-27)

[_metadata_:author]:- "Alli Medwin"
[_metadata_:description]:- "Allie talks through the hard work that went into bringing Eldritch Moon to life on Magic Online."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1048571"
[_metadata_:publish_date]:- "2016-07-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Emrakul Runnings"
[_metadata_:wayback_capture_timestamp]:- "2016-07-27 16:41:14"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160727164114id_/http://magic.wizards.com/en/articles/archive/magic-digital/emrakul-runnings-2016-07-27"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/magic-digital/emrakul-runnings-2016-07-27"
---


Emrakul Runnings
================



 Posted in **Magic Digital**
 on July 27, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Alli_Medwin_large.jpg)
By Alli Medwin











Hey everyone! I'm Alli Medwin from the *Magic Online* design team. Every set, I get to discuss with you folks a portion of what went into making this set into a reality on *Magic Online*. Some sets there's not much to talk about. *Oath of the Gatewatch* development cycles, for example, were almost entirely devoted to the mana system rewrite. This set is the opposite: I've got a lot of great things to talk about. I'm also going to discuss some of the high-level philosophy of *Magic Online* design, plus walk through an *Eldritch Moon* card's creation story from initial inception to final digital implementation.


A Nuclear Melddown
==================


For *Magic Online*, the most challenging mechanic in the set was meld, and the others weren't even close. It's not just that the rules are a little weird and changed a few times, even up to the point when we were doing initial work on the set. It's not just that the UX for meld was something brand new (more on that in a bit). Mostly, meld was challenging because it broke one of the atomic assumptions about *Magic*: that each card is a distinct object.


Before *Eldritch Moon*, one of the safest assumptions that was made about *Magic* was that objects were never made up of multiple cards. Sure, silver-bordered *Magic* has played around with that idea in both *Un-* sets—[S.N.O.T.](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=S.N.O.T.) in *Unhinged* and B.F.M. in *Unglued*—but since we don't typically make card titles with so many periods, it seemed safe.


Revisiting this assumption meant modifying some very low-level components of the game server that at first caused everything to break. Creatures entering the battlefield caused two enters-the-battlefield triggers to go onto the stack. Creatures leaving the battlefield caused two leaves-the-battlefield triggers, too. Over time, most of the bugs were fixed, leaving only a few remaining. You can check out the [Known Issues List](http://magic.wizards.com/node/389091) for those.


Minor bugs aside, we took the opportunity to make things just a little bit easier to play with meld cards. The first and most noticeable thing you'll see is that, when you zoom in on any of the three card faces involved in a meld pair anywhere in the client, you'll get to see all of them. Much like zooming in on a double-faced card will give you both faces, you'll be able to see all three faces of a meld pair even when you're drafting, with the order determined by which of the three you're zooming in on. Especially early in the Draft season, when people are still learning all the cards, having ready access to both halves plus the payoff meld card at all times is really useful.


The one thing we weren't able to deliver on was making double-size meld creatures. It's one of the flashier, more awesome things to do in paper (seriously, if you haven't yet, try it in your next [local game store](http://locator.wizards.com) draft), but the cost of implementing that display was far more than we could have afforded, even if we did nothing else, because it would have required us to completely rewrite the way cards are displayed on the battlefield. Instead, when you meld two cards together you'll see a single normal-size card with a slightly different crop of the art to accommodate the different aspect ratio.


Single Card Stories: Soul Separator
===================================


I don't think I'm terribly unique in saying this: as a teenager and young adult who was heavily invested in *Magic*, I spent a lot of time designing my own *Magic* cards. I dreamed of the day that I would finally get to make cards for real. With *Eldritch Moon*, I can finally say that a *Magic* card I designed has been printed: [Soul Separator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Separator).


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul+Separator)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Separator)
Let me set the stage. It's early 2015, and we've just released *Dragons of Tarkir*. I'm on the design team for *Commander (2016 Edition)*, and lead designer Ethan Fleischer lays out a solution to a problem we've been working on. It requires us to make some new cards to fill in some structure, so he hands us all a homework assignment. But I'm excited, so after work that day, I stay late to tinker with the assignment.


At the same time, I'm thinking a lot about the details of tokens. I'd just finished doing some work on the token inventory for *Magic Online*'s *Magic Origins* release and was getting my homework out of the way early. We had a token problem with *Origins* that we ended up resolving in a way that in retrospect wasn't optimal: rather than implement both Thopter tokens, we just took one of them and had all *Origins* cards make that specific token. I ended up chatting with some of the cardset software developers for a while about tokens, then about the homework assignment I had. The conversation went from multiple cards making the same token to a single card making multiple tokens.


I had a thought strike me, and I stopped listening to the devs long enough to furiously type out the text of a creature with a complicated tap ability. The first thought I had was pretty evocative: a necromancer that could exile a creature card from the graveyard to return both the body and soul, but not together. The body would be a Zombie the exact same size as the creature and the soul would be a Spirit with all its abilities. These are the words I typed:


![](https://media.wizards.com/2016/images/daily/MD20160727_Necromancer.jpg)


The card was adorable. Everyone loved it. It went into the file—but it didn't stay there long. Ken Nagle, also on the team, decided that he wanted it for his set "Fears," which would later get the name *Eldritch Moon*.


"Fears" toyed with the card as it was, as a creature, but ultimately it didn't have room for that kind of necromancer. It didn't fit Gisa, Geralf, or Liliana—but the card worked for the trope of the mad scientist's lab all the same. It became an artifact named [Soul Separator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Separator), the name it would keep through the rest of the set's design and development.


Because it's my job, my mind immediately went to how this would look in digital *Magic*: you'd see the Spirit token copy and the Zombie token. Blue text would tell you each token's power and toughness. The token copy would have blue text "flying," and the type plaque would have additional blue text indicating that it's a Spirit and a token. There are a lot of details, but you can tell what's going on. This is obviously the soul of a [Primal Druid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Druid):


![](https://media.wizards.com/2016/images/daily/MD20160727_Druid.png)


Turns out, though, that making tokens *that* complicated gets *really* complicated when you're doing it every turn. See, the first artifact version of [Soul Separator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Separator) could be used every turn, generating a ton of tokens very quickly. At least, it's complicated when you don't have a game server making (and maintaining) the tokens so clear. When you're playing with physical cards, it's not hard to remember that the dime is [Primal Druid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Druid)'s Spirit and the face-down Soldier token is its body. But when you need to remember those *plus* that this other face-down token is [Heron's Grace Champion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heron%27s+Grace+Champion)'s body and the fourth is the Champion's Spirit, *and* track several other different tokens on your opponent's side of the board, it rapidly becomes a headache. For the sake of the face-to-face version of *Magic*, [Soul Separator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Separator) just couldn't complicate the board that much, and it was changed so that it sacrificed itself. If you want to abuse it, now you need to put some work into doing so.


I've talked a lot in previous articles about the relationship between the design and development teams, digital R&D, and the cardset software developers. These relationships are incredibly important because they keep us all aware of our collective limitations. It's good to push boundaries regularly: it's how we got colorless mana costs, it's how we got double-faced cards, it's how we got [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver) and [Fortune's Favor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fortune%27s+Favor) and the planeswalker card type. The biggest risk to *Magic* is not taking risks, after all.


*Magic* isn't just a digital game and it isn't just a face-to-face game. It's *both*. It's a complex game to create and takes a lot of people working together. The marriage of the two ways to play is part of the special sauce that makes this game so great. When software developers raise an issue with a card or mechanic being costly to code, that's an issue for the whole game. When the paper designers and developers raise the issue of a card having a nightmarish tracking problem—even though it's trivial for digital *Magic*—it's an issue for the whole game.


Boy...That Escalated Quickly
============================


There are times when the right solution involves crafting something new, and there are times when the right solution is already in your toolbox, just waiting for some minor tweaks. Meld required the former. Emerge was the perfect candidate for the latter. Escalate was somewhere between the two, and it didn't help that it was really two different mechanics, one of which already existed.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Collective+Effort)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Effort)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Borrowed+Malevolence)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Borrowed+Malevolence)
The two-mode escalate cards are effectively entwine cards, so we knew we didn't want to reinvent the wheel on this one. Entwine is presented like a normal two-mode modal spell, with a line at the bottom labeled "Entwine," which is comprehensible shorthand for "do both these things." The same can work for two-mode escalate cards, like this:


![](https://media.wizards.com/2016/images/daily/MD20160727_Escalate.jpg)


The three-mode, seven-option escalate cards are a different beast altogether. One possible implementation would be to treat it like a [Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=397793), presenting all the legal options in the menu used to cast the card. The problem is, casting [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command) looks like this:


![](https://media.wizards.com/2016/images/daily/MD20160727_Cryptic.jpg)


I'm a professional editor well-accustomed to lots of words, and I'm the woman who dreamed up one of the wordiest cards in the set. That [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command) menu is not something I want to inflict on *myself* in the middle of an intense game, let alone players who want to play the game more than read the cards.


The other interface that makes sense here is a variant of the [Confluence](http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&name=+%5bConfluence%5d&set=+%5b%22Commander%202015%22%5d) dialog box. I discussed this in [my design article on the *Legendary Cube*](http://magic.wizards.com/en/articles/archive/feature/worthy-legend-2015-11-10), but for a refresher, here's how it works: once you've clicked the card in your hand to cast it, a dialog box appears, allowing you to choose how many times you want to use each mode. It looks something like this:


![](https://media.wizards.com/2016/images/daily/MD20160727_Confluence.jpg)


The problem is that it's pretty click-intensive. If you're going to cast [Collective Brutality](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Brutality) for all three modes regularly, you want that process clear and concise. Using this dialog box to cast a spell for all three modes requires six clicks: one to open the menu, a second to open the escalate dialog box, three more to choose each of the three modes, then a sixth click on the Cast button. Then, if there's a targeting step or three, that's even more clicks. That's just too many clicks.


The Confluence dialog box opens to help players make choices in a straightforward way. This makes a lot of sense if you're casting a Confluence, or if you're casting a three-mode escalate spell with two modes. But when you're casting an escalate spell with all three modes, there aren't any of those choices to make. And it's precisely that lack of choices that opens up an opportunity to streamline the process.


If you want to cast an escalate card for three modes, there's another option on the initial menu allowing you to cast it without opening the dialog box at all. If you want to cast a three-mode escalate card with only two modes, you'll need to use the dialog box, but that's because you have choices to make: which of the three modes are you going to use?


![](https://media.wizards.com/2016/images/daily/MD20160727_Escalate02.jpg)


The goal, of course, is to make sure that when you're playing these cards, especially a three-mode escalate card with all three modes, you can have an excuse to say "[Boy...that escalated quickly.](https://www.youtube.com/watch?v=FONN-0uoTHI)"


Emerge-nt Gameplay
==================


Emerge is a new riff on an old mechanic. *Kamigawa* block's offering mechanic was very, very similar. Offering required the sacrifice of a creature of a specific type, but that sacrifice similarly reduced the mana cost of the offering creature. Fortunately, when we were planning *Oath of the Gatewatch* and its enormous mana system rewrite, we already knew that emerge was coming; it helps that the *Magic Online* design team sits about 20 feet from *Eldritch Moon* lead designer Ken Nagle's desk. For the past few years now, we've had regular check-ins with the cardset development team, so we're always aware of what's coming.


That advance planning turned out to be very helpful with emerge, and as part of the *Oath* work, we laid the foundation for emerge, saving us a healthy amount of time when it came time to work on *Eldritch Moon*.


The Process of Getting Unique Art for *MTGO* Promos
===================================================


I don't normally preview promo cards in this article, but this one is important for a bunch of reasons.


![](https://media.wizards.com/2016/images/daily/MD20160727_Doomsday.png)


One: well, it's [Doomsday](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doomsday). Legacy and Vintage players, I hope you guys enjoy this Q3 MOCS promo. I'll admit that I'm more interested in Marit Lage than [Laboratory Maniac](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Laboratory+Maniac) as my Legacy win condition of choice, but this is still a very exciting version of a very exciting card that we know is in pretty short supply.


Two: it's new art. And not new art in the way that *Magic Online* normally uses. Normally we just pick up alternative art promos. Sometimes we pick them up even if they're canceled, like the [Sunscorch Regent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunscorch+Regent) promo from June 2015. But until now, we haven't commissioned our own art and created our own promos. Starting now, we're no longer completely tied to the promotional cards that the paper teams want to create; we can be more responsive to the specific needs that *Magic Online* has with our card selection.


Three: the art is fantastic. That's subjective, I'll admit. So instead I'll let the card concept and art speak for themselves.



![Doomsday"](https://media.wizards.com/2016/images/daily/cardart_PRM_Doomsday.jpg)[Doomsday](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doomsday) (Promo) | Art by [Joseph Meehan](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Joseph+Meehan%22%5d)
Setting: Not setting-specific


Intention: This represents a spell that is a powerful last-ditch effort that will either unleash something incredibly dark and powerful (and win the game) or, if it fails, will kill the caster.


Location: Inside a long abandoned cathedral devoted to dark magics.


Action: An opulently dressed dark mage has fallen to his knees in desperation (we are likely see him from behind). His arms are raised theatrically overhead as he invokes a powerful summoning ritual as a last-ditch effort. As the room around him begins to violently crumble, a large rift has opened in the mosaic floor in front of the priest and sinister purple light issues up from the pit. We see the head and shoulders of a vague but massive demonic shape within the up-lit haze over the pit. The priest is so lost in the ritual that he is oblivious to the danger around him.


Focus: The scene


Mood: "I will have my way even at the cost of the world!"


And who knows what promos may lie undiscovered in the future?



![](https://media.wizards.com/2016/images/daily/c4rd4r7_-WdRA7R62sC.jpg)Art by Grzegorz Rutkowski
That's No Moon...
=================


*Eldritch Moon* brings a few other, smaller changes to *Magic Online* as well. Players may now view their sideboards during a match by right-clicking on the battlefield and choosing "View Sideboard." If you're instructed to sacrifice something but can't because you don't control it—which might happen with two of this set's Equipment—the game log will tell you that you're unable to sacrifice permanents you don't control. We've made some minor iterations on targeting comments. Things like that.


It was a lot of work, but the set turned out pretty sweet. I can't wait to play it with all of you!


As always, if you want to contact the digital design team with feedback, we're available on social media. I've got [my Tumblr](http://www.trulyaliem.tumblr.com) talking about digital *Magic* in general and *Magic Online* in particular, and there's also [the Official *Magic Online* Tumblr](http://www.wizardsmtgo.tumblr.com), which is staffed by Events Manager Lee Sharpe and Game Designer Rob Schuster. Both sites have open "ask me anything!" links, so if you have something to say or a question for us, we'd love to hear from you.


Until next time, when I'll have some new inventions to show you all!







