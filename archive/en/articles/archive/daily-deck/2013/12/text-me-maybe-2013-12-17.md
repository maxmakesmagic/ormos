
---
[Link to Wayback Machine](https://web.archive.org/web/20210503084445/https://magic.wizards.com/en/articles/archive/daily-deck/text-me-maybe-2013-12-17)

[_metadata_:author]:- "Jon Loucks"
[_metadata_:description]:- "Welcome to Magic Online Week! I'm going to use this chance to talk about one of our most powerful design tools in the duel scene: blue text. I've touched on it in articles in the past, but today we're going to dive in head first. Style Matters Over the last few years, Ramp;D has continually taken a more active role in the design of Magic Online. As part of that effort, I put"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "203751"
[_metadata_:path_date]:- "2013-12-17"
[_metadata_:publish_date]:- "2013-12-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Text Me Maybe"
[_metadata_:wayback_capture_timestamp]:- "2021-05-03 08:44:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210503084445id_/https://magic.wizards.com/en/articles/archive/daily-deck/text-me-maybe-2013-12-17"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/daily-deck/text-me-maybe-2013-12-17"
---


Text Me Maybe
=============



 Posted in **Daily Deck**
 on December 19, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_jonloucks.jpg)
By Jon Loucks




 Jonathon Loucks is a digital designer in Wizards R&D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the Limited Resources podcast. Now he works on the many facets of Magic Online.
 






Welcome to **Magic Online** Week! I'm going to use this chance to talk about one of our most powerful design tools in the duel scene: blue text. I've touched on it in articles in the past, but today we're going to dive in head first. 

Style Matters
 Over the last few years, Ramp;D has continually taken a more active role in the design of **Magic Online**. As part of that effort, I put together the **Magic Online** Card Text Style Guide. This document serves as a target to design to when implementing new card sets, improving old cards, and creating new duel scene features. In the past, our approach to card text style was inconsistent. This document will help the design team and the cardset team (the people who code the cards) get on the same page. 

[At the beginning of a previous article](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/other/09292013/loucks) I talked about the philosophy of this document, so you may want to check that out. 

When I say "card text style" I'm talking about the way our card text is presented. Different styles communicate when new information is added to a card, when information changes, when an ability is lost, the current state of a card, etc. It's also agreed upon that the text on a card does not need to represent literally 100% of the information about that card—we still have tools at our disposal such as the game log, context menus, and tooltips.

**Disclaimer:** Now that this document exists, **Magic Online** can start to move in that direction. It's not going to happen overnight, but over time we should be moving closer to this target. Also, things are bound to change as they get implemented and we learn more about **Magic Online** and its needs. Consider this article a sneak peek into what the designers are thinking, but not necessarily a promise of things to come. 

The first thing this document does is break our text into four consistent styles:

* **Black** text shows the oracle text of a card, like in face-to-face **Magic**.
* ***Black italics***shows the reminder text and flavor text of a card, also like face-to-face **Magic**.
* **Blue**text shows that something has changed or has been added, or otherwise communicates important information about the state of a card.
* **Gray (semi-transparent)**text indicates oracle text that has been disabled/removed.

 You may have seen red strikethrough text on cards before. While it has been removed in some places (such as the type line of a God or creature with bestow), it may still be present in other areas. In the long run, red strikethrough text should be replaced by gray semi-transparent text. 

Outside the Box
Most of the card text style guide talks about text inside the rules box, but there are a few areas outside of the box that matter.

 If the name of a card changes, the new name would be shown in blue text since it doesn't match the printed text. For example, [Clone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone). 

  
 The only time we would change the mana cost of a card is with an X spell on the stack. I could see a future where a [Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra) on the stack with an X of five shows "![](https://web.archive.org/web/20170413132456im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)", with the "5" in a blue font color within the colorless mana symbol. 

  
Power and toughness is an area where we currently don't do any styling in the Wide Beta client. I'd like to move to a world where the power/toughness is shown in a blue font color whenever it's different from the printed power/toughness. Similarly, if a creature card is no longer a creature, making the P/T gray would also help communicate this change. For example, here's an early prototype from one of our cardset developers:

![](https://media.wizards.com/images/magic/daily/features/feat278g_levelers.jpg)  
 It's much easier to tell which level a [level-up creature](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;text=+%5Blevel%5D+%5Bup%5D) is currently on when the non-levels are in gray text. It's also easier to see that the creature on the left (with a +1/+1 counter on it) has a power/toughness that is different than its printed power/toughness. 

 Lastly, the type line is another place we want to communicate text changes. [I talked about the impact this had on Gods and bestow cards in a previous article.](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/other/09292013/loucks) For example, here's [Heliod, God of the Sun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heliod%2C+God+of+the+Sun) in the Wide Beta client when he's not a creature: 

![](https://media.wizards.com/images/magic/daily/features/feat278g_heliod.jpg)  
Rules Box Rules Rule
 Once we get inside the actual text box of a **Magic** card, there's a lot going on. Any time a card gains an ability, we want to show it in the rules box in blue text. Defining exactly how that appears isn't entirely straightforward. 

First, the text needs to be sorted intelligently. Currently, almost all blue text is listed on one line, separated by commas:

![](https://media.wizards.com/images/magic/daily/features/feat278g_abilitybluetext.jpg)  
This tends to work for the current level of blue text in the game, but as we start representing more and more abilities in blue text, such as gained activated abilities, it becomes trickier. Here's the defined order:

1. **Summoning sick:** This is a line that would only be shown on a right-click context menu. I'm not sure exactly how it would be worded (since "summoning sick" isn't an official term), but it's often important to know which permanents of yours haven't been under your control since the beginning of the turn. For example, if you're going to [Koth of the Hammer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Koth+of+the+Hammer) one of your Mountains, you need to know which one you just played. Creatures have the summoning sickness "swirl" but we need to communicate this verbally on noncreature permanents.
2. **Counters:** Another line that would only appear in the right-click context menu. It simply lists the number and types of each counter on the card. While it's rare that a permanent will have a doom counter next to a dream counter, it's currently difficult to tell the difference between the two on the Wide Beta client.
3. **Keywords, simple static abilities, etc.:** This is where the bulk of the information you're used to seeing in blue text would be shown. It includes keywords (like "flying") and simple static abilities (like "can't be blocked by red creatures"), each separated by a comma.
4. **Complex static abilities:** Since paragraph #3 is a stack of abilities separated by commas, abilities that actually have a comma in them need to be split out into their own paragraphs. (For example: "When this creature becomes the target of a spell or ability, sacrifice it.")
5. **Activated abilities:** Lastly, all gained activated abilities are listed. If you enchant a creature with [Dragon Mantle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Mantle), this is where "![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif): This creature gets +1/+0 until end of turn" would appear. This would be new functionality that the Wide Beta client doesn't currently do.

 If you put it all together, here's a crazy example of how an [Advocate of the Beast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Advocate+of+the+Beast)'s text box might look if it gained a lot of abilities: 


>  X is 9, amplify 3, attacks each turn if able, can't block, echo ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), first strike, flying  
>  When this creature becomes the target of a spell or ability, sacrifice it.  
> ![](https://web.archive.org/web/20170424152623im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/tap.gif): This creature deals 1 damage to target creature or player.  
>  At the beginning of your end step, put a +1/+1 counter on target Beast creature you control. 
> 
> 

Ample Examples
 While the **Magic Online** Card Text Style Guide gives general direction on how to approach card text, it's also stuffed full of specific examples. **Magic** is full of a lot of unique abilities that need individual attention. Let's check out a few of them. 

  
When a permanent changes color, we change the frame along with it. This is great at communicating the color of a permanent that is one or two colors. However, once a card is at three or more colors you can't tell exactly which colors it is by the frame alone. Blue text to the rescue! In the future, you may see a card that says "CARDNAME is white, blue, red, and green," or even "CARDNAME is all colors."

  
 Card text style isn't just for permanents. Spells often have different modes that need to be communicated while they're on the stack. If you cast a spell from your graveyard with flashback, it should say "cast with flashback." Or if you evoke a [Mulldrifter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mulldrifter), it could say "Evoked" while it's on the stack. Maybe an [Everflowing Chalice](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Everflowing+Chalice) says "kicked three times." 

![](https://media.wizards.com/images/magic/daily/features/feat278g_bluepithingneedle.jpg)  
 I'll admit it, sometimes I can be really nit-picky. What [Pithing Needle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle)'s blue text should *really* say is, "The named card is [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault)." It especially doesn't want a colon, since blue text is treated like rules text, and colons always mean activated abilities. It's all about increasing consistency over time. 

  
 One of our goals with Cube releases is to improve a handful of old mechanics with each release. Echo is a mechanic that's on my list. Currently, there's no way to tell if the echo cost of a card has already been paid or not—it's up to the player's memory. This can especially catch players off guard if they [Control Magic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Control+Magic) a creature with echo, and then get stuck with the echo cost. I could see blue text in the future with something like "Echo not yet paid." It's more of a piece of helpful information than an ability, but I think it still has a place in the blue text. 

  
 The last example I want to talk about is an exciting new design space we've been exploring with the cardset team: in-line blue text. Imagine if [Electrickery](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Electrickery)'s rules text changed while it was on the stack if it was cast with overload. It could literally make the replacement that overload calls for. I've even got a mockup! 

![](https://media.wizards.com/images/magic/daily/features/feat278g_electrickeryblue.jpg)  
 This type of design excites me because it opens up a lot of possibilities. We could display the value of X in-line. Or imagine a [Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) that sacrificed a 2-power creature with the rules text "[Fling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling) deals damage equal to the sacrifice creature's power (2) to target creature or player." Maybe a card with devotion to green shows it as "devotion to green (#)" in all zones. It's a new world to explore, so I can't make any promises as to where it will lead, but I'm enjoying the possibilities. 

What Are You Loucksing At?
Thanks for taking a walk through blue text with me today! I find this stuff interesting. Done correctly, this is a feature that the player hopefully never has to think about—it should be intuitive. Getting there, however, can be a journey. As usual, here's a disclaimer on the designs I talk about in this article:

The above ideas are not necessarily a promise of things to come. Instead, they serve to illustrate the design direction the team is working toward. We're always trying new ideas, iterating on them, and reprioritizing the things we implement. Consider this a behind-the-scenes look into that process, not a preview of the end result. And as I've said before, any feature we implement means another feature that we don't implement. It's all about priority.

As always, I encourage you to send me feedback via email, Twitter, or the message boards.

Thanks for reading,  
—Jon

![](https://web.archive.org/web/20150711050253im_/http://archive.wizards.com/mtg/images/widgets/storelocator/SmallStoreLocator_Background_Left.png)![](https://web.archive.org/web/20150711005846im_/http://archive.wizards.com/mtg/images/widgets/storelocator/EN_SmallStoreLocatorGOText.png)[![](https://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Details_Static.png)](https://archive.wizards.com/Magic/Magazine/Article.aspx?x=events/magic/fnm)[![](https://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_Info_Static.png)](http://archive.wizards.com/Magic/tcg/products.aspx?x=mtg/tcg/products/theros)[![](https://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_FNM_CIG_Static.png)](http://gatherer.wizards.com/Pages/Search/Default.aspx?set=%5B%20Theros%20%5D)  
  
  
![](https://media.wizards.com/images/magic/daily/footers/slice1.jpg)![](https://media.wizards.com/images/magic/daily/footers/slice2.jpg)![Jon Loucks](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_jonloucks.jpg) **Jon Loucks**[@JonLoucks](https://twitter.com/jonloucks)[Email Jon](/company/emailtoauthor.asp?author=Jon%20Loucksamp;amp;headline=%5BText%20Me%20Maybe%5D "Click to send email to the author.") | [Author Archive](/Magic/Magazine/Archive.aspx?author=Jon%20Loucks)[Uncharted Realms Archive](/Magic/Magazine/Archive.aspx?tag=Uncharted%20Realmsamp;description=Uncharted%20Realms) |  
 Jonathon Loucks is a digital designer in Wizards Ramp;D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the [Limited Resources](http://lrcast.com/) podcast. Now he works on the many facets of **Magic Online**. 







