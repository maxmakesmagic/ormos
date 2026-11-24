---
id: vm37nkd4
kind: article
lang: en
path: /en/articles/latestdevelopments/2016/02-26-learning-from-the-two-block-world
title: Learning from the Two-Block World
published: '2016-02-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    lang_detected: en
    capture_id: 723489
    url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    captured_at: '2016-08-29 02:45:53+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    lang_detected: en
    capture_id: 723489
    url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    captured_at: '2016-08-29 02:45:53+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    lang_detected: en
    capture_id: 723489
    url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    captured_at: '2016-08-29 02:45:53+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    lang_detected: en
    capture_id: 723489
    url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
    captured_at: '2016-08-29 02:45:53+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: vm37nkd4
  url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
  lang: en
  template: drupal
  captured_at: '2016-08-29 02:45:53+00'
  capture_id: 723489
  wayback_url: https://web.archive.org/web/20160829024553id_/http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vm37nkd4
  capture_id: 723489
  url: http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
  wayback_url: https://web.archive.org/web/20160829024553id_/http://magic.wizards.com/en/articles/archive/latest-developments/learning-two-block-world-2016-02-26
  captured_at: '2016-08-29 02:45:53+00'
  template: drupal
  sha256: 91850df91b61f2b8d37d82d9d0b81a0e57b1bb42caedc008811f1d83e3d8074b
render_recovery: []
---
About eighteen months ago now, [Mark Rosewater's article "Metamorphosis"](/en/articles/makingmagic/2014/08-25-metamorphosis) came out, detailing the new block structure and why we were doing it. While it may have seemed like an amazingly long time in the future when the article came out, we are rapidly approaching the date that *Khans of Tarkir* and *Fate Reforged* will rotate out of Standard and we get our first spring rotation. I for one am very excited.

Even though this will be the first time that you all get to experience this rotation, internally, we have already experienced it twice now. While I can't make a solid evaluation of how it is working in the real world, I can give you some ideas of how we have been viewing it internally, and what kinds of things we have learned from the new block scheme and rotation.

# Change Is Hard

It may not come as a shock to you that it is just as easy for us to get stuck in our ways as it is for you to do the same in whatever endeavors you are working on. When things are working well, which I would say they are for *Magic*, it's easy to just keep on trucking and using that as evidence that you are doing everything right. Sure, we had been struggling with third sets for about as long as we had been making *Magic*, but we also hadn't made any changes up until this point—outside of some experimentation (with mixed results) in *Lorwyn*/*Shadowmoor* block.

The biggest challenge to this was taking the first step and actually doing it. It required a lot of work immediately from the story and art teams (who were now being signed up for two worlds per year) and the design team (who had to speed up their exploratory design process and rework what our seven-year plan was for worlds). Development's role on this started at a similar time, but took a lot longer to see fruition. It required a lot of theorycrafting on our part to try and get everything to work in the new rotation scheme, but it was well over a year before we would even get to playtest the format eternally. Fortunately, we made some important decisions like switching *Khans* to being the first set that would rotate in eighteen months instead of *Battle for Zendikar*, because *Khans* was not planned under this model. In the original plan, *Battle for Zendikar* would've been a three-set block, which would have put the fetch lands in Standard for that entire year. We knew we wanted that overlap, but we also knew that we probably didn't want it for the whole year if we intended to go to Innistrad next. All of these led up to what is probably the most exciting spring expansion in recent memory—something I am personally really excited about.

The more we get into developing two-block worlds, the more we realize that we have to reevaluate how we do all of our processes, and that we need to update many of them. The increased rate of rotation adds in some really interesting possibilities for two-card combo overlaps or mechanical overlaps in Standard, when pushed for the right period of time. We would have never allowed battle lands and fetch lands to overlap in the old model, where it would've been for a full year. Now, that experiment seems to have turned out less well than I, at least, would've hoped for Standard, but I believe that we have learned some things from it and it will lead to better Standard environments in the future. I think it's important to realize that we are looking at how to make sure that *Magic* will be as good as possible in 20 years from now, and that means running experiments like this from time to time. Data is important.

![Comparative Analysis art](http://media.wizards.com/2016/images/daily/cardart_OGW_Comparative-Analysis.jpg)

[Comparative Analysis](https://web.archive.org/web/20160226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Comparative+Analysis) | Art by [Willian Murai](https://web.archive.org/web/20160226000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Willian+Murai%22%5d)

# Known Unknowns

In just over a month, *Shadows over Innistrad* will come out, which means a lot of things for us. First off, it is a really sweet *Magic* set. Awesome, love that—but we've released a ton of them before. It also means that we get to see how well our planning plays out in the real world. This is the first real test of the two-block model, where we are attempting to release a spring set that has the same level of impact that the fall set previously did. One thing this means is that we are rotating Standard—something we haven't ever really done at this point in the year.

Going into this, we knew a lot about what to expect from making sets for the past two decades. We were able to work out on paper the major challenges ahead of us—readjusting to a world without core sets, figuring out how to overlap themes between all three blocks in Standard, and finding ways to change Limited to be more interesting. We also knew that we were going to miss some things. Luckily, we managed to catch many of those things before they became problems. For instance, we had to do some shuffling in the seven-year plan to accommodate block themes and make sure we would be in a spot where each block had the best possible chance to succeed. Even though we managed to catch several individual things, we know that there will be things we missed, and it's up to us to react to those in the best way possible as quickly as possible.

Probably the hardest part about moving to the two-block model for development is trying to sculpt Standard without all the tools that we had in the previous world. It was much easier to say, "Next year is about enchantments, so let's make sure to not print a [Tranquility](https://web.archive.org/web/20160226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tranquility) effect in *Return to Ravnica* block," or "Next year is about artifacts, let's not print anything that hates on them too much in *Zendikar* block."

# Finding the Dividing Line

*Battle for Zendikar*/*Oath of the Gatewatch* is far from the first time we have mechanically separated two sets in a block, but it is one of the starkest differences. The reason behind this was that *Battle* was all about Ulamog, while *Oath* was all about Kozilek. While I think it allowed for some really cool cards and a very interesting Limited format, I think it also ended up stranding too many themes from the first set. If you liked ingest or landfall, there is just not going to be much for you in *Oath*. The upside is that we get to push the mechanics that don't appear in the second set harder in the first. The downside is that we don't generally get to fill them out all the way. In the old model, we might have had the third set deviate this far, and be drafted alone like *Rise of the Eldrazi* or *Avacyn Restored*, but we wouldn't have done this in the second set.

After working on *Oath*, we knew that this dividing line of how to make the first set and the second would require a big change in how we thought about blocks. We can (and should) shift some mechanics around, but how much of a mechanic's potential do we use in the first set versus the second? If we don't give you enough in the first, you might end up thinking the mechanic is lame and not caring about it in the second. If we give you too much, then the second set may not feel new enough.

One of the biggest questions ahead of us for the two-block model is how to divide the sets up. While it ended up being pretty straightforward for *Battle for Zendikar* block, we are not going to make every block in this way. The way that *Shadows over Innistrad* and *Eldritch Moon* play out will be different than how *Battle for Zendikar* and *Oath of the Gatewatch* played out, because of things we learned from *Oath* and *Battle*. Lock and Stock will likely take a lot of the things we learned from the two previous blocks and iterate, as will Barrel and Laughs. It may take us a few reps, but I believe that as we move further down the two-block model, we will have a better idea of all the tools in our arsenal for making sets feel different from each other.

I will say that the change of the draft structure to *Oath*-*Oath*-*Battle* instead of *Oath*-*Battle*-*Battle* was a huge step forward. As I mentioned in an earlier article, we discussed making this change with *Fate Reforged*, but found that the format wasn't up to our standards, so we kept it as *Fate*-*Khans*-*Khans*. The change of adding *Oath* to the environment has, I believe, been great for Limited. People had been asking for it for some time, and we had even discussed it as early as when *Born of the Gods* was released, but it seemed very strange in the three-set-block model. The new structure was the perfect place for it, and I think it has done and will continue to do good work.

That's it for this week. Join me next week on Latest Developments, when I talk about how we try to power balance the top commons in Limited.

Until next week,

Sam ([@samstod](https://twitter.com/samstod))