---
id: 4rv5w7ne
kind: article
lang: en
path: /en/articles/makingmagic/2013/05-27-developing-masters
title: Developing Masters
published: '2013-05-27'
column_slug: makingmagic
column: Making Magic
authors:
- slug: eriklauer
  name: Erik Lauer
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    lang_detected: en
    capture_id: 214888
    url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    captured_at: '2024-05-18 03:44:42+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    lang_detected: en
    capture_id: 214888
    url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    captured_at: '2024-05-18 03:44:42+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    lang_detected: en
    capture_id: 214888
    url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    captured_at: '2024-05-18 03:44:42+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    lang_detected: en
    capture_id: 214888
    url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
    captured_at: '2024-05-18 03:44:42+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 4rv5w7ne
  url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
  page_key: magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:44:42+00'
  capture_id: 214888
  wayback_url: https://web.archive.org/web/20240518034442id_/https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
- document_id: 4rv5w7ne
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/249
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/249
  lang: en
  template: aspx
  captured_at: '2014-04-10 09:27:05+00'
  capture_id: 595625
  wayback_url: https://web.archive.org/web/20140410092705id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/249
- document_id: 4rv5w7ne
  url: https://magic.wizards.com/en/articles/archive/making-magic/developing-masters-2013-05-27
  page_key: magic.wizards.com/en/articles/archive/making-magic/developing-masters-2013-05-27
  lang: en
  template: drupal
  captured_at: '2022-10-05 21:53:25+00'
  capture_id: 875796
  wayback_url: https://web.archive.org/web/20221005215325id_/https://magic.wizards.com/en/articles/archive/making-magic/developing-masters-2013-05-27
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 4rv5w7ne
  capture_id: 214888
  url: https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
  wayback_url: https://web.archive.org/web/20240518034442id_/https://magic.wizards.com/en/news/making-magic/developing-masters-2013-05-27
  captured_at: '2024-05-18 03:44:42+00'
  template: contentful
  sha256: e4b3000cf4f0b400027153f6024f529685be0cdb71dc4bd8f9aaa1cd9aaf211f
render_recovery: []
---
*Modern Masters* was designed by [Max McCall](https://web.archive.org/web/20140508203101/http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall) and [Aaron Forsythe](https://web.archive.org/web/20140509102153/http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe). Generally, the design team comes up with the vision and the initial set. The development team polishes the set, while preserving design's vision.

![](https://i.ormos.uk/21/8f/218f61a6e3ba99db16ed28fef3b8c62fb5b154cc60515d9cf700c4ffe1451a95.jpg)

The biggest decision of the *Modern Masters* design team was to make the set support the Modern format. Beyond that, the set would have many Constructed cards, but it would need to be structured like other **Magic** sets and not simply be a shopping list of Constructed cards. Also, design chose the size of the set, that it was all reprints using cards from *Eighth Edition* to *Alara Reborn*, and that it should be fun to draft.

The set design handed off was well crafted and, in fact, already reached all design's goals. While there is always room for improvement, I think the set was already acceptable, so the development team started to meet to discuss the set.

The development team for *Modern Masters* was:

### Erik Lauer (lead)

![](https://i.ormos.uk/be/ec/beec6372a2b1b12ea74ab13a7cf553dba29dcabacfeb204ccf1028cd4265a17d.jpg)  
 

I have led several development teams, most recently *Innistrad* and *Return to Ravnica*. *Modern Masters* fit snugly in my schedule between *Return to Ravnica* and the upcoming *Theros* set.

### Shawn Main

![](https://i.ormos.uk/eb/ae/ebae62185d584a8cb9676c094754527525f460b1c185922dd117366600e97642.jpg)  
 

[Shawn](https://web.archive.org/web/20131126162723/http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main) is a designer who came to R&D via the [Great Designer Search 2](/en/articles/feature/2011/03-07-the-great-designer-search-2). Most development teams have a designer on them, in part to keep a broader skill set on the team. Shawn was on both the *Return to Ravnica* and *Theros* teams.

### Ryan Spain

![](https://i.ormos.uk/52/f8/52f849ee4eb04b0c64a89a6de33ed194d1636d46d2f7b87b82f76feea180d29d.jpg)  
 

[Ryan](https://web.archive.org/web/20130913040206/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Spain) is a digital designer who spends a lot of his time working on **Magic Online**. Before Ryan worked here, he was part of a **Magic** drafting podcast called [Limited Resources](http://lrcast.com/).

All three of us love to draft, and in different ways: I was a tournament drafter, Ryan was primarily a **Magic Online** drafter, and Shawn was a casual drafter. We decided the area we could most improve from the design was the drafting experience.

The design team had picked draft themes from various blocks. Some of those themes led to weaker draft decks, so the designers tried their best to give those themes the strongest cards possible. However, there was still a fair amount of imbalance. Since we couldn't make new cards or recost the existing cards, there wasn't much we could do to make those decks stronger. We decided to explore new themes.

I wanted to use themes we were less likely to use in a Standard-legal set, since the Modern metagame has a lot of competitive decks that don't behave like typical Standard competitive decks. While draft decks aren't Constructed decks, I thought the Draft environment should reflect that difference. Ryan was very interested, but he stressed we should make sure the draft decks do something different than the same draft decks from their original blocks. Shawn thought we should be willing to bend some of the normal design rules, especially rarity, to make this all work.

We made a big grid of every draft deck we enjoyed from each block in the *Modern Masters* range and which colors those decks used. We wanted to use themes from each block, spread the themes over a lot of color pairs, and use themes that had powerful Constructed cards. We chose mechanics such as [affinity](https://web.archive.org/web/20130527000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+%5Baffinity%5D&format=+%5B%22Modern%22%5D), [dredge](https://web.archive.org/web/20130527000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+%5Bdredge%5D&format=+%5B%22Modern%22%5D), and [storm](https://web.archive.org/web/20130527000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+%5Bstorm%5D&format=+%5B%22Modern%22%5D), but we also chose some themes that were more unusual—adding Giants to that crazy mix made it even stranger. Then we had to find a way to weave it all together. I like having synergies and cross-synergies, but I don't like a Draft format being all about the designed themes. There needs to be strong cards you can draft that don't have a synergistic reward, or at least not with the designed themes. A lot of the fun is discovery, but a lot is also brewing and creating your own draft strategies. Finally, we went back to the designers. Max came to all the drafts, he saw what we were doing, and he conquered. Then he left some great feedback.

Dredge is a curious mechanic. Some members of R&D love it for its uniqueness, while others are not fond of dredge at all. [Mark Rosewater](https://web.archive.org/web/20140501120753/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater) designed it as the Golgari mechanic for Ravnica, but it was about getting to draw the same card repeatedly and not milling yourself. Brian Schneider was the lead developer of Ravnica, and he came up with making it a "self-milling" deck. He added the idea that different dredge cards would mill you for different amounts. That gave the deck a unique game play: as you dredged, you would mill other dredge cards into your graveyard, giving you more options on future turns. However, as you did this, you would run low on card in your library, giving a fair amount of tension.

Constructed dredge decks don't just dredge into more dredge cards. They have a lot of cards that work while in your graveyard. We decided that when you draft a dredge deck in *Modern Masters*, that should be an option. To make this work, we picked another graveyard mechanic: [retrace](https://web.archive.org/web/20130527000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+%5Bretrace%5D&format=+%5B%22Modern%22%5D). As you dredge cards, your retrace cards end up in your graveyard, giving you even more options.

Let's look at four of the cards you might play in a *Modern Masters* dredge deck.

### Life from the Loam

![](https://i.ormos.uk/2a/4a/2a4a8065f3c3c294b17bc3cb5c1bd59a15c57dc07d2773020401899d30d4d415.jpg)

Bronson Magnan won [Grand Prix Lincoln](https://web.archive.org/web/20130527000000/https://magic.wizards.com/en/events/coverage/bronson-magnan-grand-prix-lincoln-champion) playing a dredge deck with [Life from the Loam](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Life+from+the+Loam). Since *Modern Masters* was created with the Constructed format in mind, we wanted to include it. If you are lucky enough to draft this rare card, know it is a great fit, as it both dredges and provides a lot of land to repeatedly use your retrace cards.

### Stinkweed Imp

![](https://i.ormos.uk/02/f4/02f4b3a971cc3e9290057158a045ccd20b3d42bc4966cb0d90a592c40e621517.jpg)

In order for a self-mill deck to work, you need cards that are going to mill a lot of your library. [Stinkweed Imp](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp) is common and has the highest dredge value of any Modern-legal card. It isn't spectacular on the battlefield, but it flies and can destroy almost any creature that it blocks. And when [Stinkweed Imp](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp) dies it goes to your graveyard, giving you another opportunity to dredge. A dredge deck needs time to set up, and for three mana, [Stinkweed Imp](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp) makes a good blocker.

### Worm Harvest

![](https://i.ormos.uk/b3/fd/b3fd23a69a96db58b0a07a917a6e7b329f6cd0cf0034e9acbc1acedd003768c2.jpg)

Dredging into retrace cards needs a big reward card to compete with the other decks you can draft. [Worm Harvest](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worm+Harvest) seemed like the obvious choice, but it was not doing enough. Shawn made a convincing argument that we should change the rarity on this card to make the draft deck work.

### Masked Admirers

![](https://i.ormos.uk/4c/19/4c19da9d6f765025215d6946504ddd75a2df647bf85e1b12cc805ec6c14ef716.jpg)

I wanted a card that worked with dredge but was strong on its own. [Masked Admirers](https://web.archive.org/web/20130527000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masked+Admirers) does just that. You find it in your graveyard after you dredge and get it back when you cast another creature card. Also, every time it enters the battlefield, you can replace your normal draw with a dredge. Again, to better support the dredge deck, we changed the rarity from rare to uncommon.

When we held our drafts, the participants had a lot of fun. Aaron made another big call and decided the set was ready for a Grand Prix. You can see *Modern Masters* in play June 21–23, at [Grand Prix Las Vegas](/en/events/2013/lasvegas13/grand-prix-las-vegas-event-information).

I hope you have a chance to draft *Modern Masters*, either with physical cards or on [**Magic Online**](https://web.archive.org/web/20140424154230/http://www.wizards.com/magic/digital/magiconline.aspx?) .

Cheers,  
Erik