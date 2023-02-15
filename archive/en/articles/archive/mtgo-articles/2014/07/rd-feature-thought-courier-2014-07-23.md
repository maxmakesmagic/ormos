
---
[Link to Wayback Machine](https://web.archive.org/web/20150304131827/http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-thought-courier-2014-07-23)

[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "252566"
[_metadata_:publish_date]:- "2014-07-23"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "R&D Feature: Thought Courier"
[_metadata_:wayback_capture_timestamp]:- "2015-03-04 13:18:27"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150304131827id_/http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-thought-courier-2014-07-23"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-thought-courier-2014-07-23"
---


R&D Feature: Thought Courier
============================



 Posted in **Magic Online**
 on July 23, 2014 










![](https://web.archive.org/web/20141030155949im_/http://www.wizards.com/mtg/images/digital/magiconline/NEWSITE_MTGO_Logo_reduced.png)

[Download *****Magic Online*****](http://magic.wizards.com/en/content/download) 
  


Welcome back everyone! Previously in this space, Jon Loucks brought you the latest news and gossip from the front lines of *Magic Online* design. Now that he’s moved on, I’ll be doing the same: giving you some insight into the collective mind of the *Magic Online* design team.


The last few months have been very exciting. Within R&D, we moved some team members over to the digital design team: I moved from the editing team to be the dedicated editor for *Magic Online*, and Tom LaPille moved over from the development team to work on card set implementations. Now, we’re both focused completely on *Magic Online*, and I’m very excited to be working to make one of my favorite games of all time even better.


The most recent kind of “better,” of course, is the release of *Magic 2015* online. This set introduces a bunch of really awesome things, not all of which are readily apparent, so today we’ll walk through some of what you’ll be seeing with this set and the latest updates to the client.


Speaking of updates to the client, it’s worth noting that *Magic 2015* is the first set built and released on only the new client. As a result, since we won’t be building for two clients anymore, we’ll be able to get more done, focused as we are now on delivering new releases for just one client. This is definitely one of the best things to happen to *Magic Online* in a while. For more on this, check out [Chris Kiritz’s article](http://magic.wizards.com/en/articles/archive/magic-online-new-beginnings-2014-07-16), or [Worth Wollpert’s article](http://magic.wizards.com/en/articles/archive/magic-online-v3-date-and-new-client-update-2014-07-01).



Show and Tell

In addition to the numerous surveys we’ve run, the *Magic Online* team reads Twitter, Reddit, and a bunch of other social media regularly. It’s important for us to know what’s important to our customers, after all. One thing that has struck me is that there are a lot of features in *Magic Online*—some unique to the new client—that never see any discussion. Maybe it’s because everyone just knows these things, but *I* didn’t always know these things. I’d have appreciated someone telling me that, say, holding the M key while clicking a dual land for mana will automatically select a color, saving me a click when I’m paying a generic mana cost. Or that pressing F7 will put all of my [Soul Warden](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Warden) triggers on the stack at the same time.


For the last few weeks, we’ve been putting out [short daily articles](http://magic.wizards.com/en/articles/archive/getting-to-know-your-magic-online-client) on how to make good use of the client, and there’s also now an in-game comprehensive help manual. Click Help in the navigation bar and just about every topic in *Magic Online* is covered. Each section walks through using the client step by step, from interacting with your collection and building a deck to usage tips in a duel.


If there are features that you feel still aren’t fully explained, definitely let us know.



Read the ~~Bones~~ Cards




|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |


You may have noticed that reminder and flavor text aren’t showing up on cards without zooming in anymore. We took a look at the various ways people used that text, and in almost every case, when a player wanted to read it, they weren’t benefiting from the way we were displaying it on the battlefield.


People use reminder text as a way to understand a new (or new-to-them) mechanic, and while that text does a lot of heavy lifting in explanations, it doesn’t add much to the experienced player who knows how the mechanic works. Experienced players generally turned off reminder text anyway, because they typically know how their cards work. For those players who benefit from reading reminder text, having a necessarily abbreviated version of that text show up on the battlefield isn’t as useful as it was trying to be.


Additionally, *Magic* is a complicated game. Text showing up on cards in a complex board state when that text isn’t helping you understand what’s going on is far more liable to confuse than clarify. It turns out that having the [Bronze Sable](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bronze+Sable)s and [Centaur Courser](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Centaur+Courser)s showing a blank text box can help make processing board states just a little easier.


Now, this text isn’t gone. All of that italic text still shows up when you zoom in on a card or look at it in the Preview Pane. It’s still there, still easy to get to, and you can still read flavor text while waiting for your opponent to make a decision. It just won’t show up when it’s not helpful anymore.


So why did we move from offering an option to not offering an option? This is a large philosophical design question, but it’s one that players often ask. In short, options are great when you have multiple modes with each serving a different need. Unfortunately, both the “always show reminder text” and “never show reminder text” were failing to serve the needs of the audiences they were trying to serve. This balanced approach, we feel, will be able to meet everyone’s needs better than either of the old options ever could.



A Token of My Appreciation

Now that we’re freed from developing for two clients, we’re able to devote resources to improve the way that the game looks and feels. One of the things that I’m excited we were able to clean up early in this process is the presentation of tokens.


Tokens come in two broad categories of frames: with and without text boxes. On printed tokens, choosing a frame is easy: [Elspeth’s Soldier tokens](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=373649) don’t need it, but [Garruk’s black Beast tokens](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=383251) with their deathtouch ability certainly do.


In general, *Magic Online* has kept to the printed cards as much as possible. No matter what happened to the card, you’d always see Elspeth’s Soldiers without a rules text box in the frame. The advantage here is obvious: we want to keep to the printed game as much as possible. That’s the game’s greatest strength, after all: *Magic Online* is *Magic*, just online.


It’s important for *Magic Online* to show off the current state of an object, though. After all, we take advantage of the fact that this is a digital game by putting blue text on objects to provide clarity. Tokens deserve the same treatment as cards.


Previously, we reconciled that by maintaining the frame for tokens without rules text boxes, but adding a transparent white rectangle to act as a rules text box. It worked, but it made the text hard to read, and it made the art harder to see.


This is the same Wolf token, in the same game state. The right is the zoom view. This is obviously not ideal.





|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |


Now, though, we’ve developed the technology to dynamically change the token frame as needed. When a Soldier token gains an ability, it’ll have a rules text box the same as though it were printed with one. It won’t match printed cards, of course, but the visual will be much cleaner on the digital battlefield.


For a behind-the-scenes exclusive, take a look at this mogg. When I was putting together the pitch for this token frame dynamism, I had one of our graphic designers whip up an example of what it would look like. This guy acted as the proof of concept, and I can’t tell if he’s angry, excited, or both.





|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |


And now that it’s all implemented: a Soldier token from M15, both with and without rules text.





|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |



Indulge Me, If You Will

If you’ll indulge me a moment, I’d like to show off one of my favorite *Magic 2015* cards, because it shows how we’re trying to speed up gameplay and prevent unnecessary clicks.


![](http://www.wizards.com/mtg/images/digital/magiconline/card_IndulgentTormentor_resized.jpg)
It’s the black Prerelease card in the upcoming *Magic 2015* Prerelease events online, so we knew this card is going to see a lot of play. When this Demon’s trigger resolves, it presents your opponent with three options: sacrifice a creature, pay 3 life, or allow you to draw a card.


Under the old system, we would have presented three buttons—one for each of those options. If the opponent clicks on the sacrifice option, the opponent clicks again on the creature to sacrifice. This works, but there’s no reason to ask a player to click twice to get an effect if we can avoid it.


So here’s how it works instead: there are two buttons, and we highlight the creatures you can sacrifice. If your opponent wants you to get the card: one click. If your opponent pays life: one click. If your opponent sacrifices a creature: one click.


Ultimately, we think that this is a faster and smoother experience. What do you think?



Grasp of Phantoms

Worth talked about this in [a previous article](http://magic.wizards.com/en/articles/archive/magic-online-v3-date-and-new-client-update-2014-07-01), but just as a reminder: as a thank you for playing, we're granting Phantom Points and one each of the *Magic 2015* Prerelease items to every account that’s logged in at least once between April 2008 and the July 23 downtime. If you haven’t already used them on the Holiday Cube, you can use them to join a non-phantom Prerelease event for free.


I’m hoping to see a lot of you playing! It’ll be a great time, and I can’t wait to hear about everyone’s Prerelease stories.


Allison Medwin  









