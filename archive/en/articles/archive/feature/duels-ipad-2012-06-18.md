
---
[Link to Wayback Machine](https://web.archive.org/web/20181030215205/https://magic.wizards.com/en/articles/archive/feature/duels-ipad-2012-06-18)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/duels-ipad-2012-06-18"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20181030215205id_/https://magic.wizards.com/en/articles/archive/feature/duels-ipad-2012-06-18"
[_metadata_:wayback_capture_timestamp]:- "2018-10-30 21:52:05+00:00"
[_metadata_:description]:- "Hello! I'm Max McCall, digital designer in Magic R&D. Last week, I wrote about how Duels of the Planeswalkers 2013 was my first project at Wizards, and how excited I am that it's hitting shelves this week. Today, I want to focus specifically on the development of Duels for the iPad. We ran into a unique series of challenges in bringing Duels onto the tablet."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Duels on iPad
=============



 Posted in **Feature**
 on June 18, 2012 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Max McCall











Hello! I'm Max McCall, digital designer in **Magic** R&D. Last week, I wrote about how [**Duels of the Planeswalkers** 2013 was my first project at Wizards](/en/node/681551), and how excited I am that it's hitting shelves this week. Today, I want to focus specifically on the development of **Duels** for the iPad. We ran into a unique series of challenges in bringing **Duels** onto the tablet.

**Duels of the Planeswalkers** has a play pattern that's great for gaming on the go. There are hours and hours of game play in **Duels**, but all of the game play is broken up into very discrete ten-minute chunks. Which means it's easy to play a single duel or Encounter while you have a bit of downtime.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature200_ps3.jpg)*Screenshot of Duels of the Planeswalkers 2013 for Playstation 3*

We had good reasons for making earlier franchises of **Duels** for console and PC instead of for iPad and other tablets. Bigger screens on your TV and PC show off **Magic**'s art to its greatest advantage, and we were excited to use the XBox LIVE, PlayStation, and Steam platforms to enable easy multiplayer play with friends. When we were making **Duels** 2012*,* the iPad had only just debuted, and it wouldn't be any fun to buy **Duels** on your iPad and not have anyone to play with.

Fortunately, tablet gaming has been growing steadily in the last couple of years, so we were very excited to marry the fun of **Duels** with the convenience of a tablet like the iPad.

Unfortunately, porting **Duels** over to a tablet isn't as easy as changing a few lines of code and calling it a day. The process of bringing **Duels** onto the iPad was a very interesting one, and I want to peel back the curtain a bit to give y'all some insights.

### Press Here to Continue

The interface between a player and a game is one of the hardest and most subtle aspects of game design. If it's done right, no one ever notices that the user interface designer was there. If the UI is done wrong, the game can be unplayable. It's very important that the player be able to, you know, play the game. That means having the controls be responsive and having commands work in the way a player expects.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature200_xbox.jpg)*Screenshot of Duels of the Planeswalkers 2013 for XBox 360*

On the console and PC versions of **Duels**, the UI is simple and clean. There are buttons to play cards, zoom in on cards, pass priority, and pause the game. Outside the game, scrolling through carousel menus is quick and easy, and we hope you'll never select an option and be surprised by what happens next.

On an iPad, there's only one button. It's the entire screen.

Well, that's awkward.

We briefly considered a total redesign and new implementation of **Duels** UI for iPad, but ultimately we decided against it. It's important to us that you can have the same great **Duels** experience on every platform, and we didn't want **Duels** on iPad to feel alien to veteran **Duels** players.

So we dove in. It turns out there are a lot of ways in which a touchscreen provides a similar UI experience to a PC user with a mouse. Touchscreens allow for a lot of precision and don't force you to drag a mouse back and forth across the screen, which is super nice. However, with a mouse, you can be exceptionally precise with your clicks, even in a very small space. Touchscreens, on the other hand, can be frustrating if you have clumsy fingers.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature200_pc.jpg)*Screenshot of Duels of the Planeswalkers 2013 for PC*

I have clumsy fingers, so I was exceptionally sensitive to this problem. The "stop timer" button is very important in **Duels** if you want to respond to your opponent, but I was having a hard time hitting it in time in our early iPad builds. We ended up fixing the problem by expanding the "hit area" you can tap to click a button and spacing them out slightly wider so you wouldn't tap the wrong one. In particular, the hit area for the stop timer button is now about the size of a bus. Hurray!

Having a one-size-fits-all button caused some other issues as well. How do you call up the main menu while you're in a game if there's no escape key? We were using a two-fingered tap system, which was functional but occasionally caused unintentional pauses. More importantly, though, it wasn't intuitive. No one who picked up an iPad and began playing knew how the pause button worked.

Now, there's a truism in game design that good game design is intuitive. You don't want to surprise your players with things they don't expect. In fact, that truism is even more important in interface design—if you can't access the main menu, you won't be able to find the help and options screen that has the information you need!

This is one example where we ended up making a small departure from the console style to add some unintrusive menu options to the in-game display. We made a couple of other nods to traditional tablet UI as well. For example, we avoided using a double-tap on the iPad where possible, because the usual tablet experience uses a one-touch select. In much the same way that it's important for **Duels** on iPad to match **Duels** on Steam and XBox, it's important for **Duels** on iPad to match other iPad apps in terms of traditional iPad UI.

### Look At Me Now

The layout of **Duels** is wide open and expansive, with plenty of room on the battlefield for all of your permanents as well as a red zone for creatures to brawl in. However, iPad screens are just under ten inches diagonally.

So our early builds were a little cramped. We scaled everything down to fit, but that led to a new problem: the cards were too small! It's easy to miss the forest for the trees if you look at a problem long enough, and in our zealousness to preserve the battlefield we wanted, we'd made the cards themselves just a bit too small.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature200_ipad.jpg)*Screenshot of Duels of the Planeswalkers 2013 for iPad*

The fix was simple: just make the cards bigger. But the size issue alerted us to a new question: How should we handle zooming? We'd been using a system that let the player "pinch" the screen to zoom in on cards, but, as with the pause, we weren't sure how intuitive that would be for players, so we added double-tap functionality to enable zooming as well.

Zooming was particularly important to us because of some issues that had arisen in our stress-testing. On first-generation iPads, we were experiencing some performance problems in four-player games when the battlefield filled with dozens of permanents. We were able to alleviate those problems but our solution was to not render text on cards in play. Not rendering that text doesn't have any impact on game play—it was too small to read, and we had wanted to include it to make **Duels** feel more like paper **Magic**—but without that text it was important to us that zooming in and viewing cards was as easy as possible.

We put a lot of effort into the look and feel of zooming and playing cards because of how important it is for the mechanical act of dragging cards around the screen be as smooth as possible. Mental energy shouldn't be expended figuring out how to play your spells—**Magic** is complicated enough as it is. We put a lot of fine-tuning into how cards should be selected and played, and we're super happy with the results.

### Putting It All Together

And that was that! After all of this tweaking and tuning and iteration, we're very excited to release **Duels** into the wild on the iPad. It's the platform I personally played **Duels** 2013 on the most—it got me through some boring meetings—and I hope you'll enjoy it as much as I have.

Max McCall ([@M\_McCall](https://twitter.com/#!/m_mccall) on Twitter)

  

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/banners/D13_ArticleFooterBanner_PRE.jpg)[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/banners/SteamOnlyButton_Static.png)](http://store.steampowered.com/app/97330)






