---
id: tbr424fh
kind: article
lang: en
path: /en/articles/latestdevelopments/2017/05-19-developing-cycles
title: Developing Cycles
published: '2017-05-19'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    lang_detected: en
    capture_id: 720684
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    captured_at: '2017-08-09 11:19:36+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    lang_detected: en
    capture_id: 720684
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    captured_at: '2017-08-09 11:19:36+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    lang_detected: en
    capture_id: 720684
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    captured_at: '2017-08-09 11:19:36+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    lang_detected: en
    capture_id: 720684
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
    captured_at: '2017-08-09 11:19:36+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: tbr424fh
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
  lang: en
  template: drupal
  captured_at: '2017-08-09 11:19:36+00'
  capture_id: 720684
  wayback_url: https://web.archive.org/web/20170809111936id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: tbr424fh
  capture_id: 720684
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
  wayback_url: https://web.archive.org/web/20170809111936id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-cycles-2017-05-19
  captured_at: '2017-08-09 11:19:36+00'
  template: drupal
  sha256: d1e8d1a89ae34bfffa2acc12b2e50910b044efc36e31c616fbcf77a897b52d8f
render_recovery: []
---
Hello, and welcome to another week of Latest Developments! I talked a bit about cycling in my article previewing the cycling lands in *Amonkhet*, but there is a lot more to talk about with the mechanic. The lands were one thing, and while they are exciting and all, we had a lot more cards to put into the set. Those cards were a lot harder to balance than just the lands, and today on Latest Developments, I'm going to give you some insights into what we were thinking about when developing those cards.

Cycling is one of the best mechanics we have. We can put small costs on cards and make them have good card flow, we can put middle-of-the-road costs and allow people some interesting decisions, or we can put higher mana costs and allow for cycling triggers. It's just incredibly versatile. The mechanic is funny in that it is probably a little too versatile to be an evergreen mechanic. We try to put some kind of card-flow mechanic in most sets, but there is a limit to how many of those you can have, and I think having cycling plus another one would likely allow for too much card flow. When choosing an evergreen mechanic for card flow, we ended up with scry, which has done a good job of letting us ensure there is some card flow in sets that don't have any explicit card-flow mechanics, but not being so strong that you feel like you don't need another.

# Costing Cycling

One of the harder parts of making cycling cards is figuring out how to actually cost them. In some sense, *Urza's Saga* had the easier job of just costing the cycling at 2 and figuring out what to put it on. While that could work, it's not really what we were looking to do. We want to have more knobs than just adding one mana to a card like [Shatter](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter) and ending up with [Scrap](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrap).

When figuring out how to cost a card with cycling, there are a few things we look at:

*   How strong the card is without cycling
*   How frequently you will cycle the card
*   Opportunity cost of adding the card to your deck (if it didn't cycle)
*   Any metagame reasons the card might want to be a bit more aggressively costed

This isn't an exhaustive list but more of a few general guidelines for the kinds of things we think about. There are a lot more reasons like this, like Limited pointing, that also end up coming up in discussions. But, these kinds of rubrics help us decide how much more we end up wanting to charge for the card on the main effect and how much for the cycling cost. Of course, we don't just need to make the front card cost more; we have other options like making it more narrow. For example, [Naturalize](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) is a card that sees Standard sideboard play, so when we go to create a version of it that cycles in *Amonkhet*, we have a few options—we could make it cost 2G or we could change the effect a bit. We ended up making it only hit artifacts, which gave us the ability to charge only G to cycle it. [Sweltering Suns](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sweltering+Suns) is another example—[Anger of the Gods](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger+of+the+Gods) was a totally reasonable card in *Theros-*era Standard, and 1RR deal 3 alone would probably be just strong enough to see Standard play. Still, we have some room on the card to improve. Then we think about the points we talk about above:

**1) How strong is the card without cycling?**

Strong enough to see Standard play.

**2) How frequently will it be cycled?**

Very matchup dependent. Not a lot against fast matchups, where it is at its most useful, but frequently against control, where you have a lot of time to do it.

**3) Opportunity cost of adding the card to your deck (if it didn't cycle).**

Medium. Assuming you aren't an aggressive deck, this will be useful against almost anything else in the metagame. You probably don't want to draw it against a combo deck or another control deck, but chances are you would run a few without cycling, at least in sideboards.

**4) Metagame reasons the card might want to be a bit more aggressively costed.**

When working on *Amonkhet*, we had a lot of strong aggressive decks like the Zombie deck, white Human decks, and even some artifact aggro decks. We wanted to make sure that our slower decks had some counterplay. White had [Fumigate](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fumigate) and black had a lot of strong point removal, so that left red open for a nice sweeper.

After all that, 3 was the cost we settled on. This is a card where almost all the strength is in the main card and the cycling is a bit of added reward.

Let's look at another card, [Censor](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Censor).

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Censor)](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Censor)

**1) How strong is the card without cycling?**

Very weak. We had this card before with [Stymied Hopes](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stymied+Hopes), but it also had scry 1, and that card saw basically no play in Constructed and only a bit in Limited.

**2) How frequently will it be cycled?**

Very frequently. This is an easy card to play around after turn five or so, and your opponent will frequently do it by accident just by playing lands before their spells and not curving out perfectly.

**3) Opportunity cost of adding the card to your deck (if it didn't cycle)**

High. If you don't cast it very early, it is very likely you are going to have a hard time getting much usefulness out of it.

**4)Metagame reasons the card might want to be a bit more aggressively costed**

No major ones. Cards like [Spell Pierce](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Pierce), [Disdainful Stroke](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disdainful+Stroke), or the like have important parts in the metagame, but there isn't a huge need for this exact card. If we were trying to push hard on the metagame in some way, we would likely make the card stronger and more narrow, which would make the cycling card more relevant.

In the end, we ended up on U for cycling [Censor](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Censor) because the card is so weak on its own, but is really interesting with cycling at U. I'm really happy with where the card is—it does a particularly good job of allowing the blue control decks to have nice answers in the early-mid game while giving it a higher chance of not missing land drops. So, it's a great way to keep yourself from losing to a turn four Gideon or [Aetherworks Marvel](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aetherworks+Marvel), without also giving you a dominant late game. That's a nice card.

Each individual cycling card had a ton of discussions for making sure the costs were correct. In the end, one mana to draw a card isn't exactly something that is super weak, so we didn't put too many cards with that cost.

![Shefet Monitor](http://media.wizards.com/2017/images/daily/cardart_AKH_Shefet-Monitor.jpg)

[Shefet Monitor](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shefet+Monitor) | Art by [Viktor Titov](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5bViktor%5d+%5bTitov%5d)

# Cycling Rewards

The most powerful cycling rewards in *Magic* both came out of *Onslaught*—[Astral Slide](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide) and [Lightning Rift](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift). Beyond those having the major downside of looking at either player cycling (which is in the realm of *Ice Age*'s strange insistence to have a ton of snow-covered land hate, but almost no reasonable snow-covered land rewards), they are also just incredibly strong rewards. As a whole, when we have rewards that strong, we like to have some kind of mana payment attached; it just helps out our ability to make cards with cycling have more reasonable costs. [Drake Haven](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drake+Haven) is an example of a card that we could've decided to make without a mana cost involved, but we would then have had to have balanced the rest of the cycling cards around it. It may have been more interesting for Cube or Modern, but we'd rather not balance everything to be strong enough in those formats.

We knew we wanted cycling rewards in *Amonkhet*, but we also didn't want people to fill their deck full of cycling cards they would have little-to-no use for just to get those rewards. I think we hit a pretty good spot—the deck that gets closest to that is the [New Perspectives](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=New+Perspectives) deck, which still casts most of its cycling cards.

*Onslaught* was doing something very new with cycling—believe it or not, it was the first time we actually reused a non-evergreen mechanic in a new block in *Magic*. We managed to get a pretty good run there with just new things, but as the total amount of design space gets smaller, reusing the really strong keywords is a great option. As a result, it went out of its way to reward people for cycling cards. In fact, [Astral Slide](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide) and [Lightning Rift](https://web.archive.org/web/20170519000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift) were the cards that convinced people to actually go ahead and reuse a mechanic, which was a good strategy at that point, but I think the exciting parts of cycling here really should be the cards with the mechanic. We want people to be excited about more of the cards in the set than how a few reward cards interact with previous years.

That's it for this week. Join me next week when I answer some mail-bag questions.

Until next time,

Sam ([@samstod](https://twitter.com/samstod))