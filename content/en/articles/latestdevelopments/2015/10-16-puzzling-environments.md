---
id: ww863a7r
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/10-16-puzzling-environments
title: Puzzling Environments
published: '2015-10-16'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    lang_detected: en
    capture_id: 730069
    url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    captured_at: '2016-05-04 15:34:13+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    lang_detected: en
    capture_id: 730069
    url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    captured_at: '2016-05-04 15:34:13+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    lang_detected: en
    capture_id: 730069
    url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    captured_at: '2016-05-04 15:34:13+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    lang_detected: en
    capture_id: 730069
    url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
    captured_at: '2016-05-04 15:34:13+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ww863a7r
  url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
  lang: en
  template: drupal
  captured_at: '2016-05-04 15:34:13+00'
  capture_id: 730069
  wayback_url: https://web.archive.org/web/20160504153413id_/http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ww863a7r
  capture_id: 730069
  url: http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
  wayback_url: https://web.archive.org/web/20160504153413id_/http://magic.wizards.com/en/articles/archive/latest-developments/puzzling-environments-2015-10-16
  captured_at: '2016-05-04 15:34:13+00'
  template: drupal
  sha256: ace224c2629a90d2f309616a488148633f2691674c0399a214d92ee7952f8ce3
render_recovery: []
---
Today on Latest Developments, I am going to give you a bit of insight into how we create our environments. We shape them in such a way that they are interesting for the competitors at the Pro Tour and fun for viewers to watch—while also trying to ensure that the formats are not solved after the Pro Tour.

# Standard Diversity

Look at Pro Tour *Magic Origins*. This was a format that, only a few weeks before, people felt was dominated by [Siege Rhino](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino) and [Dig Through Time](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dig+Through+Time). And although both of those strategies saw a lot of play and were very popular, the top two decks at the Pro Tour were a mono-red aggressive deck and a blue-red artifact aggro deck that wasn't on many people's radar before the Pro Tour. Still, despite what the Top 8 looked like, the pros mostly agreed on what the top deck was—the green-white aggro deck that Brian Kibler played, which hadn't made it particularly close to the Top 8. So, many pros decided to run that deck at the next Grand Prix—a GP that was ultimately won by a blue-red [Sphinx's Tutelage](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Tutelage) deck. Just like everyone was expecting.

I think if I had to classify what the "best deck" was for the majority of the last year of Standard, it was certainly Abzan—but that doesn't mean that it was as dominant as a deck like Caw-Blade or Jund was in its heyday. While the deck may have been one of the most popular, it had its foils—like Green-White Company and Red-Green Devotion. Although there probably was a best deck, the metagame was by no means solved. Week after week and event after event, new decks would show up and different decks would win events. This kind of metagame churn with new decks popping up constantly is the heart and soul of what separates Standard from the other major Constructed environments. While both Legacy and Modern showed similar trends when they were early in their life, and occasionally after a banning or a particularly impactful new set, this kind of upheaval is not the norm for either format.

![](http://media.wizards.com/2015/images/daily/pjqXqoHKCM_icon.jpg)

[Scatter to the Winds](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scatter+to+the+Winds) | Art by [Raymond Swanland](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Raymond+Swanland%22%5d)

The secret to *Magic* is that there is no perfect metagame. While Modern and Legacy are often quite diverse metagames, they are also frequently pretty static. The top decks from a year ago are not that far off from the top decks today. That's because there are just not enough cards entering the formats (in comparison to their size) to make meaningful changes at a rate that would keep them from being basically unsolvable. We could print a lot of super powerful cards that would move the needle every set, but that would have huge repercussions for Standard, and I think change one of the things that people like about the non-rotating formats—which is that a person can choose a deck and play it for weeks, months, or even years.

# Finding Balance

If we were only interested in creating a metagame that was balanced, we could do it by making sure that three to five decks were just much stronger than the rest and letting those be the metagame. While there would be advantages to that in terms of balance, that is not the kind of experience that we are hoping to create with Standard, and it's also not the kind of gameplay we believe our fans enjoy. One of the cool things about Legacy and Modern is the sheer number of decks that are viable due to the combination of a huge card pool and the banned lists. Standard's card pool is by its very nature smaller, and we would rather not have a Standard banned list if we can avoid it. For that reason, removing all of the elements of innovation and discovery isn't worth perfect balance.

At the same time, just making a format diverse isn't actually that useful. In the old days of *Magic*'s Standard, the formats looked very diverse but were often very unbalanced. While there were a lot of decks that could work at lower levels of competition, once you put the top level of pros on the quest, what players were "supposed to do" would quickly become obvious. Because of this, we spent years not running Standard Pro Tours (we only ran two between 1996 and 2008). Frequently, Standard did break and the metagame was clearly centered around only one or two decks. This separation of Standard from the Pro Tour and PTQ scene meant that a huge amount of the event coverage and competitive articles didn't touch the format that most people were playing at their local game stores. Moving Standard to the forefront had some risks, but I think it has been a huge boon to *Magic* overall.

In order to ensure there was a mix of both diversity and balance in our Standard metagame, we used a very different strategy in how we looked at Standard and what we expected out of our sets. Instead of pushing each set to make the block format very powerful—and assuming that between it and the core set, Standard would be fun—we have moved to trying to integrate things much more holistically. If you look at the olden days, block strategies were often totally different from each other, and often actually played against each other. This meant that if one block was a little weaker than the previous one, it might not shift the needle much at all, as we saw with *Champions of Kamigawa*. *Champions* would be, by today's standards, a pretty strong Standard set. But it just didn't compare in power to *Mirrodin*, and it didn't do much with the strategies in that block. Because of the huge focus on making sure that block was as strong as it could be, the Affinity deck just didn't need any cards from outside of *Mirrodin* block in order to work. Things were incredibly stagnant. We definitely seed cards in now, like the fetch lands in *Khans*, which we can use to make sure that decks from a new block have footholds to make them strong enough to impact Standard. But we aren't relying solely on cards from the new set to make the seeds work. We can, if we choose, print cards in a subsequent set to replace the cards that left, but that's something we can only do with a ton more knowledge to prevent us from making a block monster.

![](http://media.wizards.com/2015/images/daily/cardart_FRF_Mastery-of-the-Unseen.jpg)

[Mastery of the Unseen](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=391878) | Art by [Daniel Ljunggren](https://web.archive.org/web/20151016000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Daniel+Ljunggren%22%5d)

# Creating a Puzzle

Rock-Paper-Scissors is not a very diverse game, but it is very balanced. If you were to run a large tournament, you would find that each choice would win pretty close to 33%. While that may seem like the ideal situation, there is also not really anything fun or new happening. The RPS metagame is solved. If that was a *Magic* metagame with three decks that won in those percentages against each other, it would be very boring—with the random pairings mattering more than anything else. It's pretty hard to try and make a good deck choice when put under those kind of parameters. Instead, what we strive for more with *Magic* are diverse environments, with enough complexity that it is very hard to totally solve the metagame. Our goal isn't to make an unsolvable metagame; that is basically impossible. Instead, we want to make sure there is enough variation and flex in the metagame that the amount of time it takes (on average) for the community to solve the metagame is longer than that particular metagame exists. So, for *Battle for Zendikar* Standard, ideally it would take players longer than until February to solve the format, at which point *Oath of the Gatewatch* will come out. *Oath* will then add enough new variations that the amount of time it will take to solve the format will be increased by a great enough measure that it will remain a puzzle until Tears is released, at which point both *Khans* and *Fate Reforged* rotate out.

A ton of the deep work the Future Future League does serves to create a diverse metagame. While I occasionally see some very harsh comments directed at us for missing a card in our FFL testing, or believing that a deck would be good when instead it was bad, it is important that we miss on things. We spent much less time working with the final version of the set than the public does. In fact, we never played *BFZ*-alone Standard with the final versions of the *BFZ* cards. Instead, we finalized *BFZ* while working on *Oath of the Gatewatch* to make sure that environment wasn't getting blocked by any cards in *BFZ*. It's just much harder to actually settle down on which decks are the strongest when we are constantly changing cards. Our goal is to create the right cards to allow for a wide variety of archetypes that all work and in our testing are of similar power levels. We then let this loose on the world, and see what they create. Often it is what we were expecting, but sometimes it is things that we didn't. We then use that real-world data to impact next year's sets and make sure that those sets have the tools needed to keep Standard diverse.

That's it for this week. Join me next week on Latest Developments when I talk about the devoid mechanic and how colorlessness was developed in *Battle for Zendikar*.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))