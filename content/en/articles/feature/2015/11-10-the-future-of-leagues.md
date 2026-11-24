---
id: hgfm21sz
kind: article
lang: en
path: /en/articles/feature/2015/11-10-the-future-of-leagues
title: The Future of Leagues
published: '2015-11-10'
column_slug: feature
column: Feature
authors:
- slug: chris-kiritz-55019ce1
  name: Chris Kiritz
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    lang_detected: en
    capture_id: 628095
    url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    captured_at: '2016-05-19 17:32:47+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    lang_detected: en
    capture_id: 628095
    url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    captured_at: '2016-05-19 17:32:47+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    lang_detected: en
    capture_id: 628095
    url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    captured_at: '2016-05-19 17:32:47+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    lang_detected: en
    capture_id: 628095
    url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
    captured_at: '2016-05-19 17:32:47+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: hgfm21sz
  url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
  page_key: magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
  lang: en
  template: drupal
  captured_at: '2016-05-19 17:32:47+00'
  capture_id: 628095
  wayback_url: https://web.archive.org/web/20160519173247id_/http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: hgfm21sz
  capture_id: 628095
  url: http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
  wayback_url: https://web.archive.org/web/20160519173247id_/http://magic.wizards.com/en/articles/archive/feature/future-leagues-2015-11-10
  captured_at: '2016-05-19 17:32:47+00'
  template: drupal
  sha256: bb026cd2c518a3e6d9190ec9c98b43def5670e71831888c25f4b1366610278d4
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:MagicOnlineFeedback@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - via email
  occurrences: 1
---
Greetings, *Magic Online* players, and happy *Magic Online* Takeover Week!

I'm Chris Kiritz, Digital Product Manager for *Magic Online*, and my job is to ensure that new features and projects are as awesome as can be before we ship them. Most recently, I was on the team that delivered Constructed Leagues (as well as the internal tool that helps manage them).

[![](http://media.wizards.com/2015/images/daily/Download_MTGO-Button_WOL.png)](https://web.archive.org/web/20151110000000/http://magic.wizards.com/node/823031)

Today I want to check in on those Constructed Leagues, and then talk little about what the future holds for *Magic Online*, including the status of Sealed Deck Leagues. (Spoiler alert: They're coming in 2016.) Let's get to it.

# Constructed Leagues Have Landed

Leagues are designed to allow players to play competitive *Magic* in a way that fits into a busy lifestyle. Whether you're a student with classes and homework, a parent with a job and family, a professional *Magic* player, or anywhere in between, you can battle in a Constructed League whenever you have time for a match.

If you're unfamiliar with Leagues, they are essentially tournaments with a series of linked matches that you can play over the course of several days, or even weeks, without needing to carve three or four consecutive hours out of a busy day. When you're done, you earn prizes based on your wins and can then rejoin the League and start over. Our initial release included support for Standard Leagues, but we've now added Modern Leagues and are continuing to evaluate the viability of other formats, such as Pauper.

As [Worth mentioned yesterday](/en/articles/feature/2015/11-09-magic-online-in-2015a-look-back), we're very happy with how Leagues are performing. Thousands of people have played in our Standard and Modern Leagues (most playing several rounds), accounting for hundreds of thousands of matches. In fact, one of the things that surprised us the most was how fast players played through a League; most players take no more than a day or two to finish.

The Leagues structure also means that more players have been able to experience competitive *Magic* than ever before. While the majority of League players have previously played in tournaments, close to ten percent of those who joined a League were playing in a Constructed event for the first time. This means we've been able to create an event that better serves the needs of players who were unable to participate previously. Very exciting!

As for the technical side, Leagues have been very solid with no major issues. On the back end, the delivery of Leagues included new tools for our Game Support team to help players who encounter problems with their League, including the ability to simply nullify problem matches. This nullification makes it as though the match never happened for the player who encountered a problem and lets them continue their League course without having to start over.

Even with the initial success of Constructed Leagues, we still have room to grow. To this end, we're exploring additional ways to expand our offerings, including looking at additional Constructed formats and League structures, evaluating matchmaking, and, of course, delivering Sealed Deck Leagues.

![](http://media.wizards.com/2015/images/daily/cardart_BFZ_Kor-Castigator.jpg)

[Kor Castigator](https://web.archive.org/web/20151110000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kor+Castigator) | Art by [Greg Opalinksi](https://web.archive.org/web/20151110000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Greg+Opalinski%22%5D)

# Sealed Deck Leagues on the Horizon

When we started the Leagues project, our plan was to deliver traditional Sealed Deck Leagues first. Constructed already had some pretty flexible ways to play on your own schedule, and we really wanted to provide a similar experience for Limited players. As I mentioned in [my previous article](/en/articles/magiconline/2015/08-17-magic-online-leagues-update), however, we ran into some challenges along the way, so we changed direction and decided to release the Leagues infrastructure along with Constructed Leagues as a steppingstone toward that Sealed Deck League goal. With the successful launch of Constructed Leagues, I'm happy to announce our noses are now to the grindstone on Sealed Deck Leagues.

We're currently planning two Sealed Deck League releases next year. The first will deliver the deck-building functionality and allow players to play in a structure that is similar to what is currently available for Constructed. In this format, you'll battle for a set number of matches with the same deck until your League course ends. Similar to the Constructed Leagues, when your course is over you can join the League again, build a new deck, and continue battling. In this first iteration, however, you will not be adding any additional product to your deck over the course of the League and will be playing all your matches with the same deck.

The second delivery will expand the Sealed Deck League to separate the available matches into stages and will be more like the longer Leagues experiences longtime *Magic Online* players may be more familiar with. Each stage will run a set number of matches, each pairing you with an opponent who is in the same stage. At the end of each stage, you'll have the option to add a booster to your League deck and evolve it before continuing your course and dueling players in the next stage.

While we are not ready to announce the release dates yet, we expect both versions to be available before mid-2016. If you can't wait until next year, we'll be running at least two closed beta tests for Sealed Deck leagues before the end of the year. This is your chance to check out the League features, give us feedback on your experience, and see if you can break things. If you want to be considered for participation in those Leagues, [apply to become a Beta tester today](http://wizards.custhelp.com/app/answers/detail/a_id/2265/).

# …and Beyond

In addition to the awesomeness of Leagues, we're working on some more under-the-hood improvements to the client, which we expect to ship early next year. These changes are primarily behind-the-scenes to help our development and QA teams be more efficient, but the changes will also improve general stability and performance in *Magic Online* while making future fixes and updates run more smoothly.

As for the rest of 2016, we're not ready to announce additional plans—but we have some cool content updates in the works and are exploring more ways to improve the general experience and make playing *Magic Online* awesome. As [Worth mentioned yesterday](/en/articles/feature/2015/11-09-magic-online-in-2015a-look-back), he'll have more info on our 2016 plans in an upcoming article.

It's been a busy year, and I can't wait until Sealed Deck Leagues are available for all. As always, feel free to let us know what you think via email, on Twitter (using either [@ckiritz](http://www.twitter.com/ckiritz) or [@Magic\_Online](http://www.twitter.com/MagicOnline)), or on the [*Magic Online* Tumblr](http://wizardsmtgo.tumblr.com/). Also, if you haven't taken our [Satisfaction Survey](http://www.surveygizmo.com/s3/2410924/18a8ae107cad) yet, please do. This is another outlet for you to tell us how we've done this year. Make your voice heard.

Thanks for being awesome, passionate fans and remember to have fun!

Chris Kiritz

Digital Product Manager

*Magic: The Gathering*