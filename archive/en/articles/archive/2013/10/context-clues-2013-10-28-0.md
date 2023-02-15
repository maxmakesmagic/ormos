
---
[Link to Wayback Machine](https://web.archive.org/web/20220520225415/https://magic.wizards.com/en/articles/archive/context-clues-2013-10-28-0)

[_metadata_:author]:- "Jon Loucks"
[_metadata_:description]:- "Download Magic Online Last month I wrote about implementing Theros on Magic Online. This month I return with another insight into Magic Online design. There's a lot that goes on behind the scenes of Magic Online, and I like being able to illuminate a little of that process for you, readers. It's good to be back! In today's article, I'm going to talk about context menus, the"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "688361"
[_metadata_:publish_date]:- "2013-10-28"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Context Clues"
[_metadata_:wayback_capture_timestamp]:- "2022-05-20 22:54:15"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220520225415id_/https://magic.wizards.com/en/articles/archive/context-clues-2013-10-28-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/context-clues-2013-10-28-0"
---


Context Clues
=============



 Posted in **Feature**
 on October 28, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_jonloucks.jpg)
By Jon Loucks




 Jonathon Loucks is a digital designer in Wizards R&D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the Limited Resources podcast. Now he works on the many facets of Magic Online.
 








![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/logo-mtgo-trim.jpg)


[Download ****Magic Online****](https://accounts.onlinegaming.wizards.com/)


Last month I wrote about implementing *Theros*  on **Magic Online**. This month I return with another insight into **Magic Online**  design. There's a lot that goes on behind the scenes of **Magic Online**, and I like being able to illuminate a little of that process for you, readers. It's good to be back!

In today's article, I'm going to talk about context menus, the subject of my most recent design document. I'm also going to talk about the future of context menus, at least as much as I can; it's important to note that in future design much can change, and sometimes concepts and plans are set aside because more important ones come along. Part of what I want to demonstrate is that the design of digital features often extends far beyond what is finally represented on screen.


Let's start at the beginning…


Context Menus and You!
----------------------


When you click on a card in the duel scene, a menu often appears. (The duel scene is what we call the window where you actually play **Magic**.) It's called a "context menu" because the menu changes based on the context of the click, like the mouse button, location, game state, etc.


There are a few different types of context menus, and each requires its own tailored treatment. I'm going to walk through the various types of context menus used in **Magic Online**  today and talk about their purpose and design. Most context menus a player uses are spawned from clicking on a card, but there are other types of context menus I'll touch on.


Left-click: Action
------------------


A left mouse click is how a player takes action on a card. Sometimes this happens immediately, without the need of a context menu.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/xenegos_contextmenu.png)
Here are a few examples:


* A player left-clicks a land in their hand to play it.
* A player left-clicks on [Lightning Strike](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Strike) to begin casting it, then chooses a target with a left-click, and then left-clicks on their lands to pay the cost.
* While a player is declaring attackers, they left-click on a creature to move it into the red zone, and then left-click it again to move it out of the red zone.
* While a [Mind Rot](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) is resolving, the player left-clicks on a card in their hand to discard it.

Sometimes a card will have multiple actions it can take. In that case, a context menu is created with the list of available actions for that card. From there, the player can left-click on an option in the context menu to use it. Examples:


* A player left-clicks on [Reaper of the Wilds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+of+the+Wilds), and then left-clicks either "![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_black_color.png): Reaper of the Wilds gains deathtouch until end of turn," or "![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_colorless_1.png)![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_green_color.png): [Reaper of the Wilds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+of+the+Wilds) gains hexproof until end of turn."
* A player left-clicks on a Planeswalker, then left-clicks on the ability they want to use.
* A player left-clicks on a [Thassa's Emissary](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%27s+Emissary) in their hand, and then left-clicks on either "cast" or "bestow."

There's a little more detail to it than that, which I'll get to later in the article. For now, that serves as a good overview.


Right-click: Investigate
------------------------


A right-click is how a player investigates a card. [In my last article](/en/articles/archive/putting-rd-theros-2013-09-30-0), I talked about levels of information. Top-level information, the most important information, is shown on the battlefield. Not all information can be shown on the battlefield, so second-level information is placed one right-click away. When a player right-clicks on a card, the full oracle text of the card is presented in simple text, along with gained blue text, such as [Coordinated Assault](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coordinated+Assault) giving first strike, and the same list of actions that a left-click creates.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/fleecemane_contextmenu.png)
If you want to know information about a card, a right-click should get you there. This is usually true, but there are still a few areas where we can better meet this goal. I'll be talking through a few of these areas today.


Activated Abilities
-------------------


Let's compare the way that activated abilities are shown in the current client to the Wide Beta Client.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/morphling.png)
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/morphling_betaclient.png)
The current client context menu of abilities is a lot busier than the beta client version. Long abilities, and long lists of abilities, take up a lot more space in the current client. For example, [Primal Command](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Command)'s ability text in the current client can't even completely fit on most screens!


However, there are good things about the current client's abilities lists that can still be carried over. For example, the lists have a pretty clear mouseover state, while the beta client is still a little too subtle. Similarly, the current client clearly communicates the break in clickable areas, and there's no dead space in between the options. The beta client could be better on that front.


With these ideas in mind, James Sooy created a mockup of what the beta client context menu *could* look like:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/cityofbrass_example.jpg)
A quick disclaimer: This is a *very* early mockup. James made this in an afternoon after a design discussion, and literally handed it to me a few days before I wrote this article. There are certainly more iterations to come, but I love the direction we're heading in. Also, yes, that's not technically what City of Brass does, but that doesn't really matter in early mockups.


You can see a few improvements that mirror some of the good things about the current client, namely the clear mouseover state. There's also a line separating the abilities, though in a much less intrusive way than the current client.


There are a few other improvements you might notice, the big one being the bulleted list of options. Compare that to the current way we show a list of options:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/abandonedoutpost.png)
See how the activation cost is repeated for each color option? That's incredibly redundant. With the bulleted list, we can better communicate a single activation cost with multiple options. Not only does this really clean up mana abilities, but we can also apply this technology to modal activated abilities (abilities where the player chooses a mode), like Bow of Nylea, showing each option under the same cost header.


There's another area where we're not entirely consistent. Maybe you can see it in this picture:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/horizoncanopy.png)
What if I add a [Riftstone Portal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftstone+Portal) to my graveyard?



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_riftstoneportal.png)
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/horizoncanopy_riftstoneportal.png)

 

Ahh! As you can see, the first two mana abilities, which are [Horizon Canopy](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horizon+Canopy) abilities, show no activated ability cost, and according to [Horizon Canopy](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horizon+Canopy)'s text, tapping it for mana costs an additional 1 life. So those first two could potentially kill you if your life total is low! That's another improvement you can see in James's mockup—the life cost of the ability is shown.


Similarly, check out [Karplusan Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Forest):


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/karplusanforest.png)
As far as the context menu is concerned, it looks like there's no difference between the three abilities. While they all have the same activation cost, the ![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_red_color.png) and ![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_green_color.png) mana abilities have the additional effect of dealing 1 damage to you—we should tell you! This all speaks to another goal of activated abilities in context menus: Show the full text of the costs and abilities.


Not only does this mean showing the full cost and effect, but it also means removing abbreviations from the context menu. The current client didn't have as much space on the screen to show ability text with the bulky presentation, so abbreviations helped keep abilities contained. However, we have confidence in the beta client's ability to present full ability text, without abbreviations. This will lead to a much cleaner and consistent presentation, with less guesswork needed from the player.


For example, here is an image I printed out and pinned to my desk to constantly remind myself of the terrors of inconsistency:


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/pingcrazy.png)](http://www.wizards.com/mtg/images/digital/magiconline/pingcrazy.png)
That said, there are two areas where abbreviations can be useful. The first is mana abilities. Adding mana to your mana pool is such a frequent occurrence that we can abbreviate "Add [color symbol(s)] to your mana pool" as "Add [color symbol(s)." Second, abilities where the player chooses a mode (which we call modal abilities) can lose some of their "and/or" text and punctuation, and be presented as a full ability. For example, [Bow of Nylea](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bow+of+Nylea) could be written as:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_colorless_1.png)![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_green_color.png), ![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mana_tap.png): Choose one—
* Put a +1/+1 counter on target creature.
* [Bow of Nylea](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bow+of+Nylea) deals 2 damage to target creature with flying.
* You gain 3 life.
* Put up to four target cards from your graveyard on the bottom of your library in any order.

There's one more thing I want to talk about from James's mockup. Did you notice that the last two abilities were a little faded? That's an effort to show abilities that aren't able to be activated right now. For example, let's take a look at Bow of Nylea again:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/bowofnylea.png)
Remember what I was saying earlier about the context menu showing all information about a card? Some of the Bow's abilities are missing here! When a card has an activated ability that can't be activated (usually due to a lack of targets) it currently isn't shown on the context menu at all. This can be deceiving, especially when the card is being granted an ability by something else, like a [Lightning Prowess](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Prowess). Instead, we want to show the full list of abilities that a card has, even the ones that can't be activated—those would be shown grayed-out and sorted to the bottom of the ability list.


To Menu, or Not to Menu?
------------------------


We can also improve consistency on when a context menu appears, which will also serve to protect players from accidental clicks. I'll give you a few examples.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_torchfiend.png)
Right now, if you control a [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend) but there's no artifact to target, a left-click doesn't do anything. Once an artifact is on the battlefield, the [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend) gains a thin pinline border (indicating that it's clickable) and clicking on it starts to activate the ability. The prompt box simply says "Choose target artifact."


If we were to implement features like the ones above, here's how [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend) could work. If you control a [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend) and there's no artifact to target, it still doesn't have a clickable pinline. However, left-clicking on it would still bring up a context menu with [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend)'s ability, but that ability would just be grayed-out. Once an artifact is on the battlefield, [Torch Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torch+Fiend) gains the clickable pinline. However, instead of just starting to activate the ability, left-clicking here would bring up the context menu. This requires a second click from the player to start activating the ability, but it's a much clearer process to the user. It's a little jarring to click on a permanent and then be told to select a target, especially if you click on a card with multiple abilities, only one of which is available.


There's one exception to this "always context menu" rule: casting a spell. Technically, every card in a player's hand has a "cast" option. (Or a "play" option, if it's a land.) You can see this option if you right-click on a card. However, clicking on a card in your hand to cast it happens so often, and there's no need for us to make players click twice, once on the card, and once on the "cast" option. Clicking on a card in hand and jumping straight to casting is a fairly natural process, so there's no need to add a second step in there. This is a case where we keep current functionality.


To go one level deeper, there's still an exception to that exception, which **Magic Online**  already uses: zero-mana spells. If you start casting a 0-mana spell, like [Accorder's Shield](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accorder%27s+Shield), you'll be presented with the cast option. This is to prevent players from accidentally casting a spell, since there's no intermediate cost payment step to alert them that they've started to cast a spell.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/accordersshield.png)
The Full Card Monty
-------------------


I mentioned that a right-click context menu should give the player all information about a card. Here's an image of where we're at right now:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/polukranos_example.png)
Let's dissect this context menu, including information it could display in the future.


**Card title:** Fairly self-explanatory.


**Mana cost:** Also fairly self-explanatory. I could see a far-future feature where altered costs are reflected here, in addition to the original cost, but that's just a nugget of a design idea that hasn't been mined yet.


**Type line:** [In my last article](/en/articles/archive/putting-rd-theros-2013-09-30-0), I talked about how we changed the type line display slightly with the release of *Theros*  Gods, replacing the glaring red strikethrough with gray text, which you'll also see reflected on the context menu.


**Counters:** Here's something that isn't currently being reflected in the context menu. It can be hard to tell the difference between types of counters on permanents. It's rare that a permanent has more than one counter type on it (especially with +1/+1 and -1/-1 counters eating each other) but it can happen. An easy way to communicate counters on permanents is with the context menu, listing exact type and number of each counter in blue text.


**Rules Text:** The full rules text of the card, including blue text. This is a good place to note if the permanent is "summoning sick," which can help in those situations where you're not sure which land to animate with something like [Koth of the Hammer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Koth+of+the+Hammer).


**Power / Toughness:** Not only do we want to show the creature's current power and toughness, but we should be showing the creature's original power and toughness as well. This is in line with a design rule that I outlined in a previous article: don't hide oracle text. One way to present this is to show the current power and toughness in blue, and the original power and toughness next to it in parenthetical gray text.


Some cards have multiple "forms" they can be in. For example, check out the context menu for a double-faced card:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/huntmaster_example.png)
Here, we list the entire additional forms of cards, separated by a horizontal line. These would cover the same information as the current form of the card, though only present the oracle text—no blue text necessary here. Here's a full list of the additional forms that would want this treatment:



* The front side of a face down card, like a morph.
* The other side of an *Innistrad*  double-faced card.
* The other side of a *Kamigawa*  flip card.
* The original version of a card that is currently a copy of a different card, like [Clone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone).
* The other levels of a *Rise of the Eldrazi*  level-up card.

We currently treat each of these a little differently. Going forward, we could increase our consistency by making sure each of these forms is represented completely. For example, you'll see a few pieces of information missing from the context menu of a morph:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/morph_example.png)
Lastly, at the bottom of the right-click context menu you'll find that card's full list of activated abilities.


Loucks, Stock, and Two Smoking Barrels
I've rambled on about context menus long enough for one day. There are a few context menus on non-cards, like abilities on the stack or the battlefield itself, but I'll leave those for another article.


I want to reiterate a disclaimer for this article. The above ideas are not necessarily a promise of things to come. Instead, they serve to illustrate the design direction the team is working towards. We're always trying new ideas, iterating on them, and re-prioritizing the things we implement. Consider this a behind-the-scenes look into that process, not a preview of the end result. And as I've said before, any feature we implement means another feature that we don't implement. It's all about priority.


As always, I encourage you to send me feedback via the email link below, or to [@JonLoucks on Twitter](http://twitter.com/@JonLoucks).


Thanks for reading, and may you appreciate the value of context.


-Jon



 
 






