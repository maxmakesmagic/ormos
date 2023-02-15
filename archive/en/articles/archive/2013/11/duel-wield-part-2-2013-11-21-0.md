
---
[Link to Wayback Machine](https://web.archive.org/web/20210503084440/https://magic.wizards.com/en/articles/archive/duel-wield-part-2-2013-11-21-0)

[_metadata_:author]:- "Jon Loucks"
[_metadata_:description]:- "Download Magic Online I outlined Magic Online's key-bound shortcuts earlier this week in Part 1 of this article. In Part 2, I will explore other handy tricks that can make the duel scene faster and easier to use. Duel Scene Shortcuts Have a pile of Plains you want to tap for mana? Or maybe you want to attack with an entire stack of tokens? In the Wide Beta Client, if you right"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "688546"
[_metadata_:publish_date]:- "2013-11-21"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duel Wield, Part 2"
[_metadata_:wayback_capture_timestamp]:- "2021-05-03 08:44:40"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210503084440id_/https://magic.wizards.com/en/articles/archive/duel-wield-part-2-2013-11-21-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/duel-wield-part-2-2013-11-21-0"
---


Duel Wield, Part 2
==================



 Posted in **Feature**
 on November 21, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_jonloucks.jpg)
By Jon Loucks




 Jonathon Loucks is a digital designer in Wizards R&D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the Limited Resources podcast. Now he works on the many facets of Magic Online.
 








![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/logo-mtgo-trim.jpg)[Download **Magic Online**](https://accounts.onlinegaming.wizards.com/)

  
I outlined **Magic Online**'s key-bound shortcuts earlier this week in [Part 1 of this article](/en/articles/archive/duel-wield-part-1-2013-11-18-0). In Part 2, I will explore other handy tricks that can make the duel scene faster and easier to use.


Duel Scene Shortcuts
--------------------


Have a pile of [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) you want to tap for mana? Or maybe you want to attack with an entire stack of tokens? In the Wide Beta Client, if you right click on a stack of active cards, you'll get an option to perform the same action with all of them. It's much faster than clicking on each one individually.



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_plains.png)
What if you just want to attack with ALL of your available attackers? Right click on the battlefield and select the "attack with all creatures" option. This is a great way to speed up alpha strikes.



What if you just want to attack with ALL of your available attackers? Right click on the battlefield and select the "attack with all creatures" option.
There are ways to speed up activated and triggered abilities. Take a look at the context menu for the triggered ability from [Bident of Thassa](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bident+of+Thassa):



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_bident_triggeryield.png)
There are four options here. Let's look at the first two: "Always yield to…" and "Yield to…until end of turn." These set up auto-yields for all triggers from that permanent for the rest of the game. This is a great way to make sure you never have to wait for that [Essence Warden](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Warden) trigger again. However, this doesn't affect future copies of that same permanent. If your opponent bounces your Bident and you cast it again, **Magic Online**  treats it like a new permanent, and you'll have to set up the new yields again. This makes auto-yielding sometimes difficult to set up for permanents that are entering and leaving the battlefield a lot.


If you auto-yield to [Bident of Thassa](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bident+of+Thassa), it will still ask you if you want to use the ability, since it's a "may" ability. That's where the other two options come in, "Always yes…" and "Always no…." If you tell it to both auto-yield and always-yes to your Bident trigger, then you'll never have to click through it on your own again that game. Just like the auto-yield settings, the "Always yes…" settings are stuck to that permanent.


Hitting F3 will also clear all auto-yield stops.
Once you've set an auto-yield this way, right clicking on the ability again will provide options to remove that stop. Hitting F3 will also clear all auto-yield stops.


In the future, I could see the value of a way to make yield settings sticky for all instances of a card. However, the yield design space is a fairly messy one, and it becomes hard for the player to manage. I'm not sure where yields may go in the future, but there is always room for improvement.



Duel Options
------------


[Top](#top)

Take a look at the bar of buttons on the lower right of the duel scene:



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_optionsbutton.png)
The arrow image takes you back to the event details screen. From there, you can click "Return to game" to get back to the duel. Think of it like two sides of a sheet of paper. On one side, you've got the event details. On the other side, there's the game. While this paradigm helps players keep track of games and events, it hasn't been as intuitive as we'd hoped. I could see this being a place we improve in the future.


The chat bubble does what you would think: it brings up the chat. Either it opens the chat if you've closed it, or brings it to the front if it's minimized or behind the current window.


The gear button gets you to a slew of options for the duel scene. (The top half of this menu can also be brought up by right-clicking on the battlefield.)



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_optionslist.png)
A few of these options also have corresponding hotkeys:



 


* Undo (Ctrl+Z)
* Turn Off Auto-Yields (F3)
* Yield until End-of-Turn (F6)
* Stack Abilities Automatically (F7)
* No Possible Play: Yield All (F8)

I'm hoping that, in the future, we can actually get the corresponding hotkeys listed next to their matching options, and align the naming conventions between the duel scene and the input options.


There's also the "Concede Game" option. As you probably guess, it concedes the game (with a confirmation step in between). People coming over to the Wide Beta Client from the current client may notice that there's no "Concede Match" option. Instead, the player leaves the match or event by closing the window (again, after a confirmation step). We've noticed that this is a pain point for Wide Beta users, so we're looking at how we can improve the match and tournament dropping flow.


Display Settings  
**"Show Preview Pane":** Here the player can create or close the preview pane window. In the current client, there's an "always open" card preview built into the duel scene. In the Wide Beta Client, this has been broken out to a card preview window to make more room in the duel scene.


**"Keep the 'Red Zone' always open":** The Wide Beta Client uses a red zone to communicate combat. When combat starts, the center of the battlefield expands into the red zone, and attackers move into it. This is also where blockers visually align with the creatures they're blocking, which is not something that the current client does. In an effort to create more vertical space, the red zone naturally opens in combat and closes outside of combat. However, the battlefield movement can be disorienting for some players, so we've included an option to keep the red zone always open, even outside of combat.


Above your hand is the phase ladder. This communicates which phase of the game you're in, as well as your current stop settings.
**"Show Phase Ladder":** You may notice that vertical space is especially important in the duel scene. That's why we've included an option to hide the phase ladder, which is the horizontal bar above the player's hand that indicates the current turn phase, and where your stops are set. Once they've got their stops figured out, some players just use the prompt box to tell which phase of the turn they're in so they can hide the phase ladder.


**"Enable Animations":** The Wide Beta Client places more weight on system performance, some of which comes from a larger number of animations compared to the current client. However, if users are looking to improve their performance, they can turn animations off in the options menu.


**"Auto-Size Cards":** Lastly, you can switch from auto-sized cards to manual sizing, and adjust the grid splitter in the options menu.



It's Just a Phase
-----------------


[Top](#top)

Above your hand is the phase ladder. This communicates which phase of the game you're in, as well as your current stop settings.



**The phase ladder:**


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_phaseladder.png)
You don't always need priority in every step of the game, so players set their "stops" to customize which steps they get priority. There are a few ways to adjust this. First, you can go to the Accounts scene and then In-Duel Settings page, where you can change your steps and learn more about each step.


However, sometimes you'll want to tweak your stops on-the-fly based on the game state. On the phase ladder, there are little triangles by each step that you can check or uncheck. The top triangles correspond to the stops you have set on your opponent's turn, and the bottom triangles correspond to your own turn. You can also right click on each step, and you'll get a context menu that lets you adjust the stops.


While I'm talking about phases, I should also mention that the battlefield indicates whose turn it is. On your turn, your battlefield will be lit up and have a yellow outline. On your opponent's turn, your opponent's battlefield is lit up. Similarly, the prompt box colors change based on whether or not you have priority, or if there's an action that you need to take. These are important visual cues, and we're always looking to get them just right.



Zones and Grid Splitters
------------------------


[Top](#top)

Each player, each format, and each deck puts different strains on the duel scene. It's hard to meet all needs and preferences with a single layout. Luckily the duel scene has a few sliders we call "grid splitters" that you can adjust to give space to whatever needs it. Any split between zones with five dots in the middle can be dragged to resize those zones. Double-clicking on a grid splitter often snaps it in or out.


The left grid splitter can be used to shrink or expand the left zone. This is particularly useful when you need to expand the graveyard to see its contents.


Many players aren't aware of the grid splitter above the phase ladder. This can be used to grow and shrink the hand size.
Many players aren't aware of the grid splitter above the phase ladder. This can be used to grow and shrink the hand size. However, if you keep dragging the grid splitter down, eventually your hand starts to disappear "below the fold" of the window. A lot of players can get by with just the names or art of their cards showing, so dragging the hand down like this creates a lot more valuable battlefield space. We had a feature where cards in your hand expanded on mouseover so that you could keep your hand shrunk, but easily bring up the cards to read them. We weren't able to get this feature polished enough to meet our quality standards, but I'm hoping we can revisit and polish it enough for a future release.


**Magic Online zones**  
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/01_zones_open.png)
The right side of the battlefield stores a few zones: revealed cards, exile, effects, and the command zone (if you're in a game of Commander). Clicking on the zone headers expands the zones vertically, and dragging the grid splitter expands them horizontally.


A few notes on these zones while we're here.


The revealed zone can be especially useful at tracking known information, instead of having to take physical notes yourself. You can also remove cards from the revealed zone by clicking an X in the card's corner. However, this zone doesn't work for all effects. For example, if you [Thoughtseize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize) your opponent, you technically "look" at your opponent's hand, but the cards don't go to the "revealed" zone. I'm hoping in the future we can get cards that you look at added to the revealed zone, maybe with some sort of indicator as to which zone they were revealed from.


The effects zone used to be named the "shields" zone, since it was almost primarily used to track damage prevention shields. However, we've started to take more advantage of this zone with current set implementation, and I'm hoping we can continue down that path with future sets. For example, this is a great place to store delayed triggers like the one [Triton Tactics](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triton+Tactics) creates.


The command zone stores a player's commander (as well as avatars for other formats). Although the number of times a commander has been played is tracked while it's in the command zone, that information is lost once it's on the battlefield. In terms of improving the commander experience, the design team is looking for ways to use the command zone to continue to track this information.


Lastly, some players have asked for zones that can be "popped out" of the sidebar. (The same request has been made for the graveyard as well.) This speaks to the point I made earlier about the duel scene having to bend to meet the needs of a lot of different players and decks, and the design team is looking at ways to serve this need in the future.



Duel You Feel Loucksy?
----------------------


[Top](#top)

Phew, that's a lot of words on the duel scene! It's arguably our most important scene, and it's a complicated one, but I tried to capture as much as I could. In the modern world of software design, the features are constantly evolving, and things that are true now will certainly be different in the next one/five/twenty years.


As usual, I want to add a disclaimer about the comments I make about the future of **Magic Online**  design. The above ideas are not necessarily a promise of things to come. Instead, they serve to illustrate the design direction the team is working toward. We're always trying new ideas, iterating on them, and re-prioritizing the things we implement. Consider this a behind-the-scenes look into that process, not a preview of the end result. And as I've said before, any feature we implement means another feature that we don't implement. It's all about priority.


I really appreciate the chances I've had to talk design with you, so thanks for reading.


Now, go duel somebody!


-Jon




 
 






