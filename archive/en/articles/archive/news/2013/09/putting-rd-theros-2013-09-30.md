
---
[Link to Wayback Machine](https://web.archive.org/web/20211206064117/https://magic.wizards.com/en/articles/archive/news/putting-rd-theros-2013-09-30)

[_metadata_:description]:- "Hello my friends! My name is Jonathon Loucks, and I'm a digital designer here in Wizards R&D. I love telling stories about my job, and that's exactly what I get to do today! I'm going to give you a behind-the-scenes look into how Theros got onto Magic Online. But first, I wanted to introduce you to the digital R&D team, which has grown quite a bit over the last few years. Led"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "118666"
[_metadata_:path_date]:- "2013-09-30"
[_metadata_:publish_date]:- "2013-12-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Putting the R&D in Theros"
[_metadata_:wayback_capture_timestamp]:- "2021-12-06 06:41:17"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211206064117id_/https://magic.wizards.com/en/articles/archive/news/putting-rd-theros-2013-09-30"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/news/putting-rd-theros-2013-09-30"
---


Putting the R&D in Theros
=========================



 Posted in **News**
 on December 8, 2013 










Hello my friends! My name is Jonathon Loucks, and I'm a digital designer here in Wizards R&D. I love telling stories about my job, and that's exactly what I get to do today! I'm going to give you a behind-the-scenes look into how *Theros*  got onto **Magic Online**.


But first, I wanted to introduce you to the digital R&D team, which has grown quite a bit over the last few years. Led by Ken Troop, we're the team that now owns the design of **Magic Online**. In addition to digital R&D tasks, we're also a part of greater **Magic** R&D, meaning that we still get to keep our fingers on the pulse of **Magic** and participate in set design, development, and testing. Here are the team members:


* Ryan Spain is the principal R&D designer for **Magic Online**, though you may also recognize him as my predecessor on Limited Resources.
* Dave Marsee is a powerhouse of a UI/UX designer, and he also has a passion for teaching new players. He sacrifices his Tuesday lunches to run internal learn-to-play-**Magic**  sessions.
* Max McCall is a designer for **Magic Online**  working primarily on live features and digital-only product offerings. I first met him when we were in the same dorm building for freshman year of college.
* James Sooy is a UI/UX designer with a strong history working on digital TCGs. We started at Wizards on the same day, and his shoes are usually better than mine.

 


And then there's me! I work with the rest of the team on larger **Magic Online**  design visions, but my own day-to-day tends to focus on set releases. Sometime around *Dragon's Maze*, R&D started to take a more active role in the implementation of **Magic** sets onto **Magic Online**. This way, we can make sure every individual card works in the best way possible. In addition to specifying exactly how each new mechanic should look and work in the UI, I comb through the entire set, card-by-card, looking for any hang-ups or improvements we can make.


Today, I'm going to take you through pieces of that journey for *Theros*, sharing with you some of my best stories. If you want a peek into the world of digital design for **Magic**, this article is for you. Enjoy!


A Philosophical Foundation
The first thing I want to share with you is my philosophy on how we handle information in a game of **Magic Online**. This is plucked right out of a document I recently shared with the team:


 



In a face-to-face game of **Magic**, the players have to track changing information themselves. Because each player has to be in agreement with the game state, either player can ask a question about known information and both players must be able to come to an answer. (Or, in a tournament, a judge might provide the answer.)


On **Magic Online**, this agreement between players is not only unnecessary, but impossible. Instead, **Magic Online**  serves as that agreement. In the same way that the players must be able to come to an agreement in real life, the player must be able to ask **Magic Online**  a question about the game state and get a reliable answer.



 


Essentially, anybody should be able to walk up to either side of a **Magic Online**  game and be able to discern everything about the current game state. We're not all of the way there yet, and we may never reach 100%, but we're pretty close. With R&D's increased involvement on **Magic Online**  via the digital design team, **Magic Online**  is getting even closer every day. This philosophy serves as the foundation to any duel scene features I design.


Now that you know where I'm coming from, let's dive into the stories!


A Non-creature Creature
You used to have to do a lot of work to make a creature not a creature. I'm talking Soul Sculptor level of work. Then *Theros*  comes along with its Gods and bestow cards, and suddenly there are non-creature creatures everywhere! In face-to-face **Magic**  we rely on players' memories and context to know the modes of cards. Luckily we can go further on **Magic Online**  and actually change the face of cards to help our players.


First off, we've got to do something about the type line. In the past, whenever a card lost a super-type (like creature) or a sub-type (like Goblin) that word was shown struck-through in red font. The design team isn't really a big fan of that treatment, and *Theros*  gave us just the excuse to change it. Now you'll see lost types in a kinder gray font.





|  |  |
| --- | --- |
| 
 Celestial Archon
 in Magic | 
 Celestial Archon
 as an Aura
 in Magic Online |


Next, we had to make sure the bestow cards gained blue text to communicate that they now have "enchant creature." We use blue text in **Magic Online**  to communicate when a card gains abilities or something has changed. I've been spending a lot of time lately defining and improving our blue text standards, and this is one of those areas that we made sure got the blue-text treatment.


The first implementation of Gods and bestow creatures showed them with no power and toughness while they weren't creatures. The power and toughness box was just gone. This conveyed what mode your card was in, but violated one of our fundamental tenants: Don't hide oracle text. Players should be able to tell what the base stats of a card are no matter which mode the card is currently in. Sometimes, this information is stored in a card's context menu (which you see by right-clicking on a card), but in this case it wasn't even showing up there.


So we turned the power and toughness box back on for all modes. It's easy to tell when a bestow card is an aura because it's attached to a permanent. For the Gods, we made sure that they appear in the back, non-creature row when they're not creatures, so you'll see them slide up to the creature row once you reach the proper devotion.


![](https://media.wizards.com/legacy/mtg/images/digital/magiconline/img_god_enchantment_battlefield_650.png)
I should note that the design team spends most of their time working in the Wide Beta Client for **Magic Online** ([download Wide Beta Client](http://mtgoclientdepot.onlinegaming.wizards.com/setup.exe)). That's our new and future client, so that's what we design for. Sometimes we run into issues where the Wide Beta Client doesn't match the current client, and this is one of those moments. In the Wide Beta Client, you'll see the power and toughness on Gods and bestow cards when they're not creatures. In the current client, however, you won't. That's the "joy" of maintaining two clients simultaneously. We're hoping to address this for the current client soon so that it more closely matches the Wide Beta Client functionality.


![](https://media.wizards.com/legacy/mtg/images/digital/magiconline/img_monstrous.png)
You're a Monster
Rawr! I love monstrosity. It wasn't an especially tricky mechanic to implement, but there was some discussion on if and how we should show that a creature is in a monstrous state. Ultimately we decided on adding the word "monstrous" to the creature in blue text, and I smile every time I see it. It's just another example of us trying to make the game state as clear as possible to the player.


To Exile and Back Again
There are a few cases in **Magic Online**  where we show exiled cards on the battlefield instead of in the exile zone. Oblivion Ring is probably the most famous case of this treatment. It's the most intuitive method of showing the association between Oblivion Ring and the exiled card, though sometimes the implementation isn't entirely straightforward.


It's one thing to exile a single card. Angel of Serenity ups the stakes a little bit with three cards. But Ashiok, Nightmare Weaver? This Planeswalker exiles like crazy! In some control matchups, especially with the new legend rule, it's not crazy to think that Ashiok would have a double-digit number of exiled cards. Do we really want to show that many exiled cards on the battlefield?


We kicked around a few ideas. Do we show all the cards? None of the cards? Some of the cards? I liked the idea of showing only the exiled creatures under Ashiok, since those are the ones Ashiok cares about once they're exiled. However, this would be the first instance of splitting cards exiled by the same source into two different places, so we wanted to make sure it was worth breaking convention.


![](https://media.wizards.com/legacy/mtg/images/digital/magiconline/ashiok_exile.png)
Sometimes I'll poll "the Pit," which is what we call the area where designers work and congregate, with **Magic Online**  design questions--this was one of those times. Talking to the *Theros*  development team (the card developers, not the programmers who are also called developers at times) validated the "show some" approach. Apparently, while testing Ashiok, that's how people naturally played; they would put the exiled creature cards under Ashiok, and put the rest off to the side. I think it's a big win when we can align digital mechanics with how people intuitively play with the cards.


A Turn for the Better
![](https://media.wizards.com/images/magic/tcg/products/ths/obasdfkjw8324lz/8x2vHVs5J2Y_EN_LR.jpg)
Behold!


Medomai the Ageless cares about something that no other card has cared about before: whether or not you're in an extra turn. The rules technically know if a player is in an extra turn (as opposed to a normal turn), so to adhere to the philosophy I outlined earlier, that the player must be able to ask **Magic Online**  a question about the game state and get a reliable answer, we should surface this information to the players. Medomai is the perfect excuse to do this now.


There are a few different places that we can surface information to the player during a duel on **Magic Online**. The most obvious place is on the main duel screen itself. However, not all information is worthy of this placement. There just isn't room for everything. Adhering to the philosophy does not mean that all information is available at a glance--just that it's available somewhere in the game. Since most players know whether or not they're in an extra turn just by playing the game, and since that particular information isn't always relevant, we're safe putting this information a level deeper.


Information about individual cards that doesn't deserve to be top-level is often put on a context menu, the menu you get when you right-click on a card. It's true that Medomai cares about extra turns, but whether or not it's an extra turn is global data that doesn't belong on a specific card. Luckily, Medomai gains the blue text "can't attack" during extra turns, which is a pretty clear indicator of the game state if you just care about Medomai. So the context menu isn't quite the right place.


![](https://media.wizards.com/legacy/mtg/images/digital/magiconline/img_chatlog.png)Luckily, we've got a good place to put second-level global game information: the game log. Something you'll notice about the Wide Beta Client is that the chat is split into two sections: the game log on the top, and the chat log on the bottom.


Separating game chat from game information makes it a lot easier to digest each piece on its own. We stick relevant game actions into the chat log, including stuff that doesn't get surfaced in the duel scene. For example, if a player casts Burst Lightning with kicker, the game log will say "[playername] casts Burst Lightning (with kicker) targeting [target]."


We already announce in the game log when players begin their turn. With *Theros*, you'll also notice that when a player takes an extra turn, that is noted as well. You'll see "Turn #: [playername] - Extra Turn" in the game log. It's an admittedly small improvement, but it's all about meeting the philosophy that I outlined earlier. Today it's an extra turn indicator to help Medomai, and tomorrow it's adding the storm count to support an entire mechanic.


Sins of the Past
One of my goals in writing up the set spec (that's what we call the document that outlines how the cards should be implemented) is to make sure we pick up any loose ends from previous sets. Sometimes we run out of time and can't get everything in for a set release that we wanted. Sometimes a bug makes it through. Sometimes we designers just
![](https://media.wizards.com/images/magic/tcg/products/dgm/tiwoirwiixix/rtdk3u41zz_EN.jpg)
missed something and don't see how a card can best be implemented until we actually play with it online. Sometimes the feedback of players will lead us to an improvement. Things will inevitably be missed, and now we have a system in place to catch the things that slipped through: We put it in the set spec for the next set.
This time around, we picked up Progenitor Mimic from *Dragon's Maze*. We realized that the copy wasn't getting any blue text, but it was clearly gaining an ability that should be represented. With the release of *Theros*  on **Magic Online**, you'll now see blue text on a Progenitor Mimic that's a copy of something.


There are other instances of clones gaining abilities, such as Phantasmal Image. We'd like to add blue text to those eventually as well, but they're not as high of a priority. Part of this past-cleanup effort accepts that we can't fix everything, but we should put extra effort in to polish our most recent releases. I hope that this effort continues to raise the bar for **Magic Online**  sets, even after their release dates!


Heroes and Hydras
The set spec also has to cover any branded-play requests. For *Theros* , that means following the Hero's Path. The other week [I wrote about how the Hero's Path works](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/266a) on **Magic Online**  (for information on events in the **Magic Online**  Hero's Path, check out the articles on [*Theros*  Prerelease and Release Events](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/other/09162013) and the [Face the Hydra Challenge](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/other/09232013)). If you're familiar with the Hero's Path in face-to-face **Magic**, then you'll notice some difference with how it works on **Magic Online**. Figuring out exactly how the Hero's Path would work on **Magic Online**  was a multi-discipline effort between the digital designers, the **Magic online**  programmers, business, and the path's original designer, Dave Guskin.


![](https://media.wizards.com/legacy/mtg/images/digital/magiconline/herospath_white_theprotector.jpg)
The first step was seeing how closely we could stick to the original Hero Card designs. Luckily, we could leverage the existing avatar technology on **Magic Online**, though most of the Hero Cards would do something no other Avatar has done before: tap! The Hero Cards look great on the Wide Beta Client, but you can tell that they're not quite optimized for the current client. They work, but they're partially outside the command zone window while tapped. We felt like this was acceptable since they functionally worked, and we were able to preserve the one-to-one match between the paper and **Magic online**  Hero Cards.


Then we had to figure out exactly how to get the avatars to the players. This isn't as simple as face-to-face **Magic**  where we can just put the Hero Card in your Prerelease box. Instead, once you're done with a Prerelease event, you'll be granted your Hero Card along with the rest of the cards in your pool.


![](http://archive.wizards.com/mtg/images/digital/magiconline/avatar_THS_hydra.jpg)
Lastly, there was the challenge of creating a [Hydra experience](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/other/09232013). We certainly couldn't replicate the unique in-store experience of the Face the Hydra Challenge Deck, so we had to get a little creative. We still wanted players to battle a Hydra, but we had no way of running an event that paired everybody against a hydra of some kind. So we created a tournament where players earned the right to face the mighty Hydra in a separate event, piloted by none other than Wizards R&D! If enough heroes defeat the Hydra, then we give rewards out to the entire community. I wish you the best of luck in defeating the Hydra--you'll need it.


Stop Loucks and Listen
Thus ends our foray into the implementation of *Theros*  on **Magic Online**. I hope you enjoyed this glimpse into our day-to-day, and I look forward to sharing even more stories about how we made playing **Magic Online**  even better. I encourage you to send me feedback on this article or **Magic Online**  via Twitter ([@JonLoucks](http://twitter.com/jonloucks)) or email (linked below).


Thanks for reading, and enjoy *Theros*!







