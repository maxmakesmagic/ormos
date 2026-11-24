---
id: n3w1xf43
kind: article
lang: en
path: /en/articles/makingmagic/2013/03-13-the-beta-goes-on
title: The Beta Goes On
published: '2013-03-13'
column_slug: makingmagic
column: Making Magic
authors:
- slug: ryan-spain-a32db4e3
  name: Ryan Spain
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    lang_detected: en
    capture_id: 212190
    url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    captured_at: '2024-05-18 03:46:31+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    lang_detected: en
    capture_id: 212190
    url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    captured_at: '2024-05-18 03:46:31+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    lang_detected: en
    capture_id: 212190
    url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    captured_at: '2024-05-18 03:46:31+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    lang_detected: en
    capture_id: 212190
    url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
    captured_at: '2024-05-18 03:46:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: n3w1xf43
  url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
  page_key: magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:46:31+00'
  capture_id: 212190
  wayback_url: https://web.archive.org/web/20240518034631id_/https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
- document_id: n3w1xf43
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/238c
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/238c
  lang: en
  template: aspx
  captured_at: '2014-02-17 18:40:04+00'
  capture_id: 594745
  wayback_url: https://web.archive.org/web/20140217184004id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/238c
- document_id: n3w1xf43
  url: https://magic.wizards.com/en/articles/archive/making-magic/beta-goes-2013-03-13
  page_key: magic.wizards.com/en/articles/archive/making-magic/beta-goes-2013-03-13
  lang: en
  template: drupal
  captured_at: '2022-01-24 02:48:09+00'
  capture_id: 867301
  wayback_url: https://web.archive.org/web/20220124024809id_/https://magic.wizards.com/en/articles/archive/making-magic/beta-goes-2013-03-13
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: n3w1xf43
  capture_id: 212190
  url: https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
  wayback_url: https://web.archive.org/web/20240518034631id_/https://magic.wizards.com/en/news/making-magic/beta-goes-2013-03-13
  captured_at: '2024-05-18 03:46:31+00'
  template: contentful
  sha256: a2d62b821974b3054b380d17dd7cf53da44da26ef0386a61b801cd2293ed5451
render_recovery: []
---
After the **Magic Online** downtime on Wednesday, March 13, a new version of the **Magic Online** Beta client [will be available to download](/en/articles/feature/2011/10-17-download-magic-online). For all the articles I've written about progress on the beta client, I've never had a longer list of changes and improvements to draw from. The full list of fixes, new features, and changes can be found in this [thread](https://web.archive.org/web/20130313000000/http://community.wizards.com/go/thread/view/75846/29466403/Wide_Beta_Changelist), but I'll use my time with you today to give you a look at a few of the most prominent updates in this build with a little tour.

![](https://i.ormos.uk/06/6f/066f8f10ad8a5ed52ac883d1542af3e643183d9f559da946d1e790c917d73b0e.jpg)

### Promo Codes

If you missed [Chris Kiritz's article](/en/articles/makingmagic/2013/03-07-magic-online-program-update-2012-mocs-champs-gp-trials-promo-codes-and-more) on some of the great things coming up for **Magic Online**, you might not have heard about a cool new feature launching with the March 13 build: the **Magic Online** Promo Code program! Through this program, we will be able to create codes that players can redeem through the **Magic Online** Store, but only in the Beta Client. There's even a free code you can redeem after the March 13 downtime in Chris's article, but I'm going to make you find it over there...

### Dial M for Mana

**Magic**'s depth and rich history are part of what make it such a compelling game, but it is also one of the things that makes **Magic Online** design a challenge. In general, with video-game design you want to help players control their experience intuitively, with as few button presses and interactions with the user interface (UI) as possible. The depth of **Magic** constantly pushes against that philosophy when implementing mechanics and features, though. **Magic Online** asks a lot of seemingly obvious questions ("Would you like to gain that life?"), but we have to because there are always edge cases to consider ("No, I have cards with the fateful hour mechanic.").

We try to incorporate opt-in shortcuts to expedite game play where we can, but in the world of "advanced options," more is not always better—every additional option carries with it a complexity cost. We have to pick our spots, finding opt-in shortcuts that are worth both the development and the complexity costs. In the latest build of the beta client, we have added one of my favorite shortcuts since the "always yes" and "always no" options on "you may" triggered abilities: "fast mana."

There are a lot of permanents in **Magic** that tap for multiple colors of mana, but a lot of the time, you don't need a specific color, you just need mana. We can't presume to know when that is, but we can let you tell the client when you don't care. Now, if you hold down the "M" key when you left-click a permanent with multiple tap abilities that include a mana ability, the game will automatically activate the first mana option instead of bringing up a context menu (that list of potential options to choose from on cards with multiple abilities). In a dual-land-heavy environment like *Return to Ravnica* block, this feature is a great time-saver, and it works on nonlands like the Keyrunes of *Return to Ravnica* and creatures like [Birds of Paradise](https://web.archive.org/web/20130313000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) and [Devoted Druid](https://web.archive.org/web/20130313000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devoted+Druid). This shortcut is bindable in the settings as well, so you can set it to something other than "M" if you wish.

![](https://i.ormos.uk/84/7c/847c332707e4577c83282af035b2c06bd44e3ef98bc29c96da93779ad3410118.jpg)

Speaking of context menus: we also made a change to the way context menus function with tooltips that some players will appreciate. Tooltips can be found throughout the client by right-clicking whenever you see a question mark in the cursor, and they are also found above the context menus on cards. These in-game tooltips show the full rules text of the card, which can be helpful when you need that information quickly. For an experienced player who doesn't need this info, though, getting the full rules text whenever a card had a context menu could be more distracting than helpful. Now, the tooltip only appears when you right-click on a card to activate its ability, and left clicking only shows the context menu.

![](https://i.ormos.uk/f4/88/f488aa15c33d62e1e0961fe21e93d6619bb7bb8222618c8634831c35853ffa0c.jpg)

### Getting Thin

Space is at a premium on the battlefield and throughout the client. One of our technical artists, Brian Price, has spent a lot of time lately going over the client and reclaiming space where we can through the restyling of certain UI elements. The biggest improvements on this front will be more apparent in the build after this one, but Brian has already made an important tweak to the UI styling by thinning the "grid splitters" throughout the UI. The grid splitters are the borders between areas of a scene that you find throughout the client, and they were taking up too much valuable screen real estate previously.

![](https://i.ormos.uk/d0/dc/d0dcf20c2acbf578798dac46eba738addc8b12e3bfa5299a5a489009d5422af0.jpg)

I'm excited by the difference Brian's changes are making to the overall feel of the client, and there is more to come in the next build.

### Limited Deck Building

In Limited deck building, we have reclaimed a lot of space by doing away with the large panel containing the "Add Lands" and "Submit" button and moving those buttons elsewhere in the UI. This move recaptures a full column of space in the deck pane:

![](https://i.ormos.uk/b3/2c/b32c07acaaae7ec5aee76ef45b9d3fec515ccf92e98926bbfe39413ae6e698b1.jpg)

A drawback of this space reclamation is that the buttons for adding lands and submitting a deck don't stand out as much as they did before. We will be improving on this in an upcoming build, but in the meantime the increased space for viewing your deck and sideboard were too important not to reclaim.

One V3 feature near and dear to my heart that had not yet made it onto the Beta Client is the ability to save and load different versions of a Limited deck during deck building and sideboarding. It's finally here! If you right-click in an empty space in your main deck, you can choose the "Save as" option to save out different builds of your sealed or draft deck, and then load them during sideboarding. In an improvement over the V3 method, the Beta Client will only show you decks that match the contents of your Limited card pool, so you don't have to sift through non-matching decks.

![](https://i.ormos.uk/ae/97/ae97031a434a3617b35bd4b9245032e45c2bc481e4a5c51e38aa97ed60f5d207.jpg)

### Collection

We made a lot of small fixes to the Collection scene in this build. While it's not exactly the most exciting thing to say, "Some things that were broken are now fixed," instead of introducing you to a cool new feature, the fixes in the Collection scene collectively make me very happy. They represent the meat and potatoes of progress in software development—the iteration, refinement, and polish of the complex system your team has built.

The most annoying collection bug that was fixed in this build is probably the one where removing a card from your deck with certain filters applied to the collection would cause the collection to refresh. If you are a longtime Beta Client user, this is an annoyance you will be happy to be rid of. If you are new to the Beta Client, I'm happy you'll never experience it. We also now have a confirmation dialog for opening product, which was another frustration point for anyone who accidentally clicked the "open product" button that appears over boosters and other sealed product.

![](https://i.ormos.uk/13/92/13923c2f812a65568b10bd24d1b7b61d6b475031b441c578bb231cae681f949d.jpg)

Regular beta users may want to browse the Collection portion of the changelist to see other welcome fixes to the Collection scene, but the takeaway here is that we are continuing to improve and fix bugs in the client in lots of little ways that collectively adds up to a significant improvement to the experience.

### Trade

While the recent improvements to Collection reflect the effort to get from functional to polished, there are still areas of the client that we have been moving from nonfunctional to functional, and Trade is one such area. The good news is, Trade has reached and passed "functional" status with this build, and we are currently polishing up the flow of trades, reducing the clicks, increasing the clarity, and generally taking it from "functional" to "good" for the next build.

### Chat

In addition to lots of the small fixes seen throughout the changelist, chat has benefited from a couple of nice features and some improved styling. One improvement is that the composition field in the chat window will now expand automatically as your message gets longer instead of having to manually adjust the size of that field. In addition, the chat module was one of the greatest beneficiaries of the restyling effort to reclaim space by thinning the grid splitters, and is emblematic of the impact of the effects of this restyling throughout the client. Look at this before and after:

![](https://i.ormos.uk/95/d6/95d681dfcb2bc71e1cce93ddcd64b219d82750c26ab397700a5b6b4ceed2a270.jpg)

It is vastly improved, and that is just the beginning of what Brian has in store for the next update to the client!

### Commander & Multiplayer

Multiplayer **Magic**—Commander in particular—is another area of the Beta Client that had frankly been sitting in the "nonfunctional" pile with Trade for a long while. You could technically start a multiplayer Commander match, but from there, things got pretty weird. Commanders appeared to begin play on the battlefield despite technically being in the Command Zone, and lots of other issues interfered with the smooth completion of the game's most popular casual format.

We've implemented a Command Zone and generally improved the multiplayer experience quite a bit in this build. I hope some of you diehard Commander players will give it a shot and share some feedback with us. It's not perfect yet, but like trading, it is now functional and heading toward "good."

### The Tip of the Iceberg

I'm butting up against my word count, and I feel like I've left out dozens of great improvements and fixes in the latest build of the Beta Client. I do hope you will check out the changelist for the goodies I didn't cover in this article or, even better, download the client after the downtime on March 13 and check it out firsthand. After you do, make sure you fill out this [survey](http://www.surveygizmo.com/s3/1187782/MTGO-Wide-Beta-Survey-March-13-2013) and tell us how we are doing.

As always, your feedback is important to us. After you fill out the survey, you can also share your thoughts in the [forums](https://web.archive.org/web/20130313000000/http://community.wizards.com/go/forum/view/75846/135046/magic_online_general), fill out this feedback [form](http://www.surveygizmo.com/s3/1028055/Magic-Online-Wide-Beta-Feedback-Form), or just [contact me on Twitter](https://twitter.com/RyanSpain). Until the next new build, good luck and have fun!