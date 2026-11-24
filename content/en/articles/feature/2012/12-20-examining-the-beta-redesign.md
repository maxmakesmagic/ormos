---
id: 3v205sdt
kind: article
lang: en
path: /en/articles/feature/2012/12-20-examining-the-beta-redesign
title: Examining the Beta Redesign
published: '2012-12-20'
column_slug: feature
column: Feature
authors:
- slug: dave-marsee-59e39a5d
  name: Dave Marsee
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    lang_detected: en
    capture_id: 599622
    url: https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    captured_at: '2022-10-03 08:01:13+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    lang_detected: en
    capture_id: 599622
    url: https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    captured_at: '2022-10-03 08:01:13+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    lang_detected: en
    capture_id: 599622
    url: https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
    captured_at: '2022-10-03 08:01:13+00'
    rule: drupal.div_author
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/226d
    lang_detected: en
    capture_id: 593111
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/226d
    captured_at: '2014-02-18 20:44:19+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 3v205sdt
  url: https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
  page_key: magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
  lang: en
  template: drupal
  captured_at: '2022-10-03 08:01:13+00'
  capture_id: 599622
  wayback_url: https://web.archive.org/web/20221003080113id_/https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
- document_id: 3v205sdt
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/226d
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/226d
  lang: en
  template: aspx
  captured_at: '2014-02-18 20:44:19+00'
  capture_id: 593111
  wayback_url: https://web.archive.org/web/20140218204419id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/226d
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3v205sdt
  capture_id: 599622
  url: https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
  wayback_url: https://web.archive.org/web/20221003080113id_/https://magic.wizards.com/en/articles/archive/examining-beta-redesign-2012-12-20
  captured_at: '2022-10-03 08:01:13+00'
  template: drupal
  sha256: fd3c3fb2e361b00b62c38dad33c72ea0662b7a16b0a5077201e849ce560a1c39
render_recovery: []
---
Hi there! My name's Dave Marsee, the user experience (or "UX") designer for the **Magic Online** Beta Client. This project has been a labor of love ever since I joined the **Magic Online** design team two years ago. Being a UX designer means my job is to make sure that you, the players, are having the best possible experience while playing.

I love this game. I play **Magic** just about every day—if not with my kids around the kitchen table, then on the iPad edition of **Duels of the Planeswalkers** 2013, in internal Wizards of the Coast leagues (tied for 2nd in *Return to Ravnica*), or in the weekly learn-to-play classes I teach here in the building. I even went 2–1 in the [Community Cup](https://web.archive.org/web/20121220000000/https://magic.wizards.com/en/events/coverage/community-team-learns-sorrow-defeat), beating the great Conley Woods! (GG, CW.) We live and breathe this stuff.

![](https://i.ormos.uk/b7/2b/b72b0643ecefb018db3844c0552cac05f45974db859af3ba5edf40ab807949bb.jpg)

My job entails many different aspects: I talk with the R&D design team to nail down how the game and mechanics should be played. I talk with the business team to make sure players can join the tournaments they want to. I talk with the dev team to work out how we can accomplish this with our technological constraints. I talk with players to see how our solutions work for them. And then, I make a lot of documents to capture these needs and expectations.

### Making Hard Choices

![](https://i.ormos.uk/bb/47/bb4790f7cfc0cc814843381fccf7993e728e5be2d5a9ebe9c2ff30a489776bdd.jpg)

One of my favorite memories is from 1988. I bought an NES with birthday money, and it came with a game that changed my life: *Super Mario Bros.* In that game, I learned about interacting with software with multiple input methods: a directional pad and two buttons. As I read the instruction manual and looked at the start screen—wondering who drew those pixels and who wrote "2 PLAYER GAME"—I knew that this was what I wanted to do with my life.

Since then, I've designed for start-ups, computer companies, and many e-commerce sites. I've usability-tested with people from a wide range of backgrounds. I've researched and played hundreds and hundreds of different games.

While this is my dream job, it's also one of my most challenging. With an e-commerce site, so much of the hard work is already done for you. There is very little re-invention on an online store.

But **Magic Online** is a whole other beast. Nothing is taken for granted. We know we are making some great improvements, but some choices aren't so easy, which is why we debate—a lot. In the early months, it was easy to design something we all agreed with, but most choices come with a list of pros and cons. And every choice is going to meet the needs of some portion of our players... and probably bother some others. So we always come back to a few philosophical questions when making a tough decision:

1.  What are the goals we are trying to meet? What problems are we trying to solve?
2.  What are the benefits of each option? What are the drawbacks?
3.  Which choice will be preferred by the largest number of our players?

It isn't until after we have asked all of these questions that we reach a decision.

### History

A few of you have tried out our work in progress, the **Magic Online** Beta Client. The story of the Beta starts with the launch of the current client (aka "V3"). V3 is built on a structure that is very difficult to modify. Even the smallest changes or additions are a significant cost to our development team. Early in 2009, a new version was already being planned. In addition to changing the underlying structure of the program, the team saw some opportunities for improving the user experience.

I was tapped to join the team halfway through its development. A few prototypes were already being user-tested. However, **Magic Online** is a complex program. It quickly became apparent that our users would have demands we just hadn't designed yet.

Today, I'll be talking about three scenes we've made changes to in the Beta version, and speak a bit as to why we made these choices. They are: Collection/Deck Editor, Play Lobby, and Drafts/Tournaments.

### Goals

Our top priority is to make **Magic Online** the most fun, complete, and best way to play competitive **Magic**. To do this, I've worked with some of the brightest minds in the game. There are many excellent people who make this program a success... and without whom we would not be as far as we are. Some names you may recognize include [Ryan Spain](https://web.archive.org/web/20130913040206/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Spain), [Alexis Janson](https://web.archive.org/web/20130520111221/http://www.wizards.com/magic/magazine/archive.aspx?author=alexis%20janson), Graeme Hopkins, and [Chris Kiritz](https://web.archive.org/web/20130626041609/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Chris%20Kiritz), but there are many more who work behind the scenes. We meet together every day to discuss, debate, and design each detail to make **Magic Online** the best it can be.

Paper **Magic** and **Magic Online** have a lot of similarities in the way you interact with your cards, but also a lot of differences. In **Magic Online**, players don't have to shuffle their decks manually, combat damage is assigned automatically, card rules text is always up-to-date, there's always someone to draft with, and your collection doesn't take up any room in your closet. But even though your closet space is free when using **Magic Online**, your collection may still be massive. We are aware of collections that have hundreds of thousands of cards in them. How can a player easily find the cards he or she wants to see?

### Collection

In V3, your collection is broken up into two screens: Collection and Deck Editor. There are a few things about these scenes that are less effective. First, there are two different interfaces that can serve largely the same purpose. Second, the filters care a lot about the technical truth of a card, but don't consider the process of deck building. Third, it's difficult to discover possible cards that might go well in your deck. Fourth, a significant percentage of players either don't know the filters exist or don't know how to use them well.

[![](https://i.ormos.uk/ac/5d/ac5d355932ff949a8bb8f12aedb058efd6274d23ecbe930e81525cb8a3a81c10.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_v3collection_large.jpg)

*Click to expand*

 

 

 

[![](https://i.ormos.uk/b8/f0/b8f0306ffd91da2f322bec545a22e3f1f52e66f96433069093130af5b3adf991.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_v3_deckeditor_large.jpg)

*Click to expand*

 

We set a number of goals to solve some of these problems in the Beta, including: (1) consolidate scenes whenever it made sense for the user—we've done this by making the collection scene be where players create and edit their decks; (2) make the filters more recognizable to a broader audience— these filters are clearly identified, and players can easily peruse them to find just the card they want; and (3) create a new grouping logic for colors and other metadata.

 

 

[![](http://media.wizards.com/images/magic/daily/features/feat226d_wireframe_collection_small.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_wireframe_collection_large.jpg)

*Click to expand*

 

 

 

[![](https://i.ormos.uk/af/d6/afd6193a30a5202f028e59548eac4dc414e2d0771dd7ec18562adf3aeab85a92.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_wireframe_deckeditor_large.jpg)

*Click to expand*

 

 

 

[![](https://i.ormos.uk/dd/e7/dde72fa9de3fa2c8ba5dc8efc4b874591c4a032bf6d6ffb38e6a9d38dc5eb988.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_shiney_collection_large.jpg)

*Click to expand*

 

Here's how color grouping logic works: When you select colors (let's say green and white), your results are grouped into areas of relevance.

 

The first group is cards you can actively use in your green-white deck... cards whose mana costs are green OR white, green AND white, hybrid mana that includes green or white, or colorless cards that care about green or white.

The second group is for perusing after you've explored the first one. These are cards that are castable in a green-white deck but aren't necessarily green or white. Here, you'll find colorless or other cards you may find useful.

The third group contains cards that are technically the colors you've selected and also require additional colors you haven't selected.

The reasoning behind this philosophical shift is because the main-use case for **Magic Online**'s Collection scene is that of deck building. And when you select a color, you are doing so for the purpose of putting cards that care about that color in a deck. So, we expand (or promote) the cards that may matter to your search to help you discover cards you may not have considered before.

There are many more changes to the Collection scene, including the ways players manage their decks, set aside parts of their collection for trading, and change the ways their cards are displayed. Be on the lookout for further improvements in the coming months. With these changes, we believe the Beta Client will be a much better experience for the majority of players.

### Play Lobby

A super-important scene in **Magic Online** is the Play Lobby. In V3, there are a few areas we felt could use some improvement. (1) We separate play into many different rooms—each invisible to the others—which decreases the amount of events in each room but also hides possible opportunities for play. (2) V3 doesn't have the capacity to explain all the features of a given event, so we are forced to display event details on our website. (3) Finding and joining a game in a Casual room is frustrating (my biggest pet peeve of all)—it feels like a skill game of "click the moving row correctly, then hunt down the right deck before someone else does." I don't know about you, but that is not my favorite kind of game.

![](https://i.ormos.uk/a9/15/a915ffefbc885ff22e2a66d561729eb8e118972ec297579b9877d6f67ec8504e.jpg)

 

In the beta version, we have tried to solve these problems in a few ways.

 

 

[![](https://i.ormos.uk/ec/2c/ec2c112f74bf6a24a21a9f0d151c2c4f9c3160707ca7a0b35e202c3a75534a63.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_play_lobby_large.jpg)

*Click to expand*

 

First, every game, match, draft queue, tournament, etc., is all accessible in a single scene! No longer do you have to navigate from room to room to see what is available to be played. The filters you saw in the Collection scene are here again in the Play Lobby, so we hope you'll find yourself at home here.

 

Second, each match or event has a details page that displays important data, including entry requirement options, standings, a clock, and important information about the event as a whole. As time goes by, we will be able to enhance this details screen with even more relevant information.

Third, our design is such so that you can find the game you want with a minimum of clicks. For Constructed Open Play, it's as easy as selecting your deck and clicking the big "Next Game" button. You'll either be automatically joined to an already-created game that fits your deck's format or you'll host a new game, ready for another player to join you!

### Drafting

The best part of playing **Magic** (in my humble opinion) is drafting. I don't have as many opportunities to have a full draft as I would like, as a father of three kids, but I do so whenever I can. Over the Thanksgiving holiday, I was lucky enough to have a full pod of relatives over, so we partook in a *Return to Ravnica* draft. I am not too proud to say that I took all five [Auger Spree](https://web.archive.org/web/20121220000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auger+Spree) cards that was passed to me and 3–0ed. (Better luck next time, family! Remember to take removal higher!)

We on the **Magic Online** Beta team feel very strongly about drafting and want to make it the best experience possible. To accomplish this goal, we went over the entire draft experience with a fine-toothed comb and have made some great improvements—some of which you've already seen, and some that are still in the works.

In V3, there is some room to improve. For example, (1) every card you pick goes right into your deck—but we know that only about twenty-three of your picks will make it into the final deck; (2) the method of growing/shrinking cards in this scene isn't immediately obvious; (3) V3 assumes you want to build your deck, like a LEGO creation, one card at a time—but our research showed that many players don't build that way; (4) the Duel scene can become a maze of arrows and duplicate ghost cards—very disorienting for a person who just began playing.

 

[![](https://i.ormos.uk/d9/98/d998d0828726c298afba9cacbbb90dafa6181f1f021740fee4bf11f4fe388599.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_v3draftscreen_large.jpg)

*Click to expand*

 

We have made some changes to alleviate these problems.

 

First, you can now pre-nominate cards to be in your sideboard. These cards remain in your sideboard after all your choices are made.

 

[![](https://i.ormos.uk/ee/2a/ee2a83d9b3146eef1cede84aada53336c9cf39822e50e784b9e4de46c1a6f769.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_shineydraft_large.jpg)

*Click to expand*

 

Second, you can also organize creatures and noncreatures in separate rows, filter out cards from your sideboard (this is especially useful in Sealed), or hide cards altogether. This allows players to build decks like granite sculptures, chipping away until their decks reveal themselves. Regardless of your preferred method, you can do both in the Bata Client. While this scene still has a few tweaks ahead of it, we believe we're on the right track to a great deck-building scene.

 

 

[![](https://i.ormos.uk/c8/2a/c82a96aa1c3fafb4c469f916f93206a0fdaa238630a9484336f8beedba144e42.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_v3draftbuild_large.jpg)

*Click to expand*

 

 

 

[![](https://i.ormos.uk/81/eb/81ebb52b56b1004e2f720359c135998d2437b4d78bf6fd0049f42623474117fc.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_shiney_draftbuild_large.jpg)

*Click to expand*

 

The Duel scene has gone over some of the most extensive changes in **Magic Online**. We have tried to build it with the following goals in mind: To keep the "duplicate ghosting" of cards to a minimum, to communicate combat attacking and blocking with proximity for ease-of-understanding, to make it easy for players to click on cards the way they expect them to, and to generally get out of the players' way. We still have a ways to go to get it the way we want it, but I believe that by the time we're done, the Duel scene will be the crown jewel of the Beta Client.

 

 

[![](https://i.ormos.uk/7f/62/7f6266be264f44348777d8e9cb16f1c5d844e9a48ed2521f50fb8c9837bdd077.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_v3_duelscene_large.jpg)

*Click to expand*

 

 

 

[![](https://i.ormos.uk/fa/03/fa03d0cadb6a731736943c1b6cf00a233ce08ddfbdf68efa5d374933624b2a82.jpg)](http://media.wizards.com/images/magic/daily/features/feat226d_shiney_duelscene_large.jpg)

*Click to expand*

### And Finally...

I can guarantee that as you try the beta version of **Magic Online**, you will find some changes. Some of these changes will feel foreign to you and some will be familiar. Many of you have shared your concerns with us on our [feedback page](http://www.surveygizmo.com/s3/1028055/Magic-Online-Wide-Beta-Feedback-Form). I read this feedback, so my hope is twofold:

1.  If we've made a change you don't like, that you can see or understand that this change is intended to be the best choice for the **Magic** community as a whole—but also, it is subject to change if it turns out that our first attempt was wrong-headed.
2.  That you understand that this software still isn't complete—that some features are waiting in the wings as we deal with the priorities shared by all of you.

This work in progress is one that I have great faith in. I'm really proud of this program, and when we're done, I hope it'll be something you'll feel comfortable sharing with your friends. In the meantime, I want to invite you to give the [Beta Client](/en/articles/feature/2011/10-17-download-magic-online) a try. Let us know what you think.

All the best,

Dave Marsee

 