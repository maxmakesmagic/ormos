---
id: de44skb6
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/12-18-origins-of-a-vorthos
title: Origins of a Vorthos
published: '2015-12-18'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    lang_detected: en
    capture_id: 729421
    url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    captured_at: '2016-03-25 08:39:02+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    lang_detected: en
    capture_id: 729421
    url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    captured_at: '2016-03-25 08:39:02+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    lang_detected: en
    capture_id: 729421
    url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    captured_at: '2016-03-25 08:39:02+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    lang_detected: en
    capture_id: 729421
    url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
    captured_at: '2016-03-25 08:39:02+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: de44skb6
  url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
  page_key: magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
  lang: en
  template: drupal
  captured_at: '2016-03-25 08:39:02+00'
  capture_id: 729421
  wayback_url: https://web.archive.org/web/20160325083902id_/http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: de44skb6
  capture_id: 729421
  url: http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
  wayback_url: https://web.archive.org/web/20160325083902id_/http://magic.wizards.com/en/articles/archive/latest-developments/origins-vorthos-2015-12-18
  captured_at: '2016-03-25 08:39:02+00'
  template: drupal
  sha256: 669dbfaf915bf93f1627e89c4c4012cc6f3288049bb71b2b7b8fdf9425bb9546
render_recovery: []
---
*With the end of the year nearly upon us, we're taking two weeks to revisit the best articles from DailyMTG in 2015. If you didn't catch some of these the first time around, do yourself a favor and read on. Then, join us back on December 28 as* Oath of the Gatewatch *previews get underway in earnest!*

*Happy Holidays!*

* * *

It's Vorthos Week on DailyMTG, so I'm going to talk about the importance of flavor to development, in terms of both card names and card designs.

Out of all the developers, I am probably the biggest Vorthos. While I won't say I have the same kind of encyclopedic knowledge of the *Ice Age* storyline as Ethan Fleischer, I definitely know a good amount of the story. I have read many of the novels, followed complex storylines on cards, and memorized most of Jaya Ballard's flavor text. It was part of what got me into the game as a child, and part of what kept me going as an adult. I may not have quite understood what being a Planeswalker actually meant when I started playing, but I did get an idea of all the awesome creatures I could summon—and I was able to pick a few of my favorites to include in my decks, even if they weren't the strongest cards. [Leviathan](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leviathan), I'm looking at you.

While many people may have been able to play *Magic* if it was all vanilla cards named "Creature48480" with just numbers and no art, I couldn't have done it. I needed that basis of fantasy to get over the hump of learning the rules, understanding what abilities did, and absorbing all of the (at the time) hundreds of cards that were out there. I even ended up reading *One Thousand and One Nights* as a way to better understand all of the *Arabian Nights* cards that I was definitely not cool enough to own. But, I could tell you who [Ali from Cairo](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ali+from+Cairo) was, what the [Diamond Valley](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diamond+Valley) had to do with Sinbad, and why [Shahrazad](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shahrazad) started a subgame. That kind of connection drew me in even further, and pretty much got me hooked on *Magic* for life.

When I am working on a set, I try to have enough flavor in it that I can impress the next young developer, who is just getting into the game and is looking not just for footholds to understand why things work, but a deeper lore to bring them in. Flavor may not be the primary goal of development, but it is certainly not something that we ignore.

# Importance of Flavor

Flavor is important for development. I know that you may think of us as just people looking to tweak numbers, but we are also all about tweaking the play experience. Often that means finding ways to ensure flavorful cards do what you think they should do and are generally fun. We could create "Pay your taxes" as a top-down design that took two hours to resolve and ended up charging you four hundred dollars, but unless we are working on an Azorious card, it's probably better to stick with designs that are actually fun to cast.

Let's take [Flight](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=25510), for example. It's an old card, and depending on which version of it you have, it could depict anything from a weird lady who appears to be standing on the ground to a very awkward zebra. I prefer the zebra version, but that's neither here nor there—what is important is the card as a package makes sense. If you cast [Flight](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=25510) on your [Craw Wurm](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craw+Wurm) and attack an opponent, even without a ton of rules knowledge, things would make sense. It makes sense to people that creatures with flying can't be blocked by creatures on the ground. In some sense, flying is the best keyword we have because of how intuitive and easy it is.

![](http://media.wizards.com/2015/images/daily/cardart_VIE_Flight.jpg)

[Flight](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=25510) | Art by [Jerry Tiritilli](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Jerry+Tiritilli%22%5d)

[Flight](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flight) has another huge advantage to it—the name. It may not come off as the most flavorful ([Spectral Flight](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Flight) and [Phantom Wings](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Wings) both sound much better), but it has the advantage of being resonant. It's nice to have a mix of cards in our sets that are very specific ([Nissa's Revelation](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Revelation), [Abbot of Keral Keep](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Abbot+of+Keral+Keep)) along with ones that have generic and resonant names ([Throwing Knife](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Throwing+Knife), [Claustrophobia](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Claustrophobia)). This lets people focus on the flavor for cards that are important, but also allows some of the background cards to exist in a way that makes games play well. If we had to rename [Claustrophobia](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Claustrophobia) each time we put it in a set, we would quickly run out of good words to use and tax people's memory more than necessary. We would much rather leave that brain space for the cards that are important to the story.

Now, *Magic* has been around for over 20 years, and we've used a lot of super iconic names. Many—such as [Reincarnation](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reincarnation), [Subdue](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Subdue), and [Teleport](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teleport)—are pretty forgettable cards from sets like *Legends*. Nowadays, we at least try to guard some of the best names and use them on cards that we'll want to reprint on a semi-regular basis. The aforementioned [Claustrophobia](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Claustrophobia) is a good example of a card that was originally printed in *Innistrad*, has since been reprinted twice—in *Magic 2014* and in *Magic Origins*—and will likely be printed again in the future. It is a nice, simple effect with a resonant name that can exist anywhere.

# Flavor Wins

Development rarely (but sometimes) goes in with the plan to try and make things in the set make sense flavorfully. [Godsend](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Godsend) and [Deicide](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deicide), for example, are very intentionally able to kill [the god version of Xenagos](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=378528). We would like to at least try to avoid things like Gerrard's card being unable to kill Tsabo's card—despite the fact that [Gerrard Capashen](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard+Capashen) is far smaller and [Tsabo Tavoc](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tsabo+Tavoc) has protection from Legends—because he is able to defeat her in the story. The design team is often using the cards in the final design file to tell a story. Development must ensure that those cards tell the story on the page, as well as make them play well and tell the same story in games.

A few weeks ago, I talked about trying to get our characters correct with regard to how we make legendary cards. We also try to portray the world as a whole in a cohesive and sensible manner. Take [Nissa, Vastwood Seer](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%2C+Vastwood+Seer) in *Origins*, for example. She is a legendary creature that searches up a Forest. So does [her Pilgrimage](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398593), which can put one Forest into play and one (or two) more into your hand. And when you hit seven Forests on the battlefield, Nissa transforms. Was that decision made for balance reasons? Well, partly, but I also chose that number for her trigger because of another card in the set—the card that actually shows Nissa's Spark moment:

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa%27s+Revelation)](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Revelation)

She couldn't exactly cast that spell and find Emrakul in the Teeth of Akoum if she didn't have seven mana, could she? Now, as happy as I was to have those line up, part of it was by accident and part of it was intentional. While the card [Nissa's Revelation](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Revelation) was designed to hit the story moment, the size of the effect dictated something in the seven-mana range anyway. Had the gameplay proven to be much better with either Nissa or the Revelation at different numbers, then we would've put them there. But I was happy with how those numbers worked out, so we kept it.

A lot of our other various flavor wins come through general playtesting of the set. Early playtesting isn't usually terribly useful for this, as the cards often have silly or useless names. For example, if a card starts out as "[Inspiration](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inspiration)" in a development file and we decide we want a different card-draw spell that isn't a reprint in the same slot, we might call it "NotInspiration" so that people know that it's a different card. Other playtest names, like "Ulamog is So Hot!" for burn spells, are cute—but they're clearly not going to make the final card. Once creative has done their pass and started actually naming things, that is when development goes to work. If a card is concepted as a part of the story and something about it doesn't fit, it's often development who will notice the mismatch and talk to creative. For example, while working on *Origins*, we were playing with [Chandra's Ignition](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%27s+Ignition) and realized something weird. Although it represented Chandra's spark moment, it didn't actually flip her because the spell did the damage. It wasn't a huge change to make the creature deal the damage (which had the side effect of being better with things like lifelink and deathtouch), but it went a long way to making something people could discover as a flavor win at a later time. Little changes like these aren't the most important parts of making each set, but they do go a long way to getting the set to the final level of polish.

# Flavor Fails

While *Magic* has a lot of flavor wins, we are also aware of its flavor fails. [Gerrard Capashen](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard+Capashen) can't actually kill [Tsabo Tavoc](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tsabo+Tavoc). A [Fire Elemental](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fire+Elemental) can be [roasted](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=394667) to death. A [Soulless One](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soulless+One) can have its [soul reaved](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398591), and an [Aquamoeba](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aquamoeba) can be [dehydrated](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=129521) without dying. These things happen, and most people don't think too deeply about them. Not everything is going to make sense, and that is okay.

![](http://media.wizards.com/2015/images/daily/Nope-Nope-Nope.png)

*Nope, nope, nope, nope*

*Magic* is a game first, and while getting the flavor of the cards right is important most of the time, we definitely understand that there are times where that isn't practical. I can put [Lightning Greaves](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Greaves), [Swiftfoot Boots](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swiftfoot+Boots), and a pair of [Fleetfeather Sandals](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fleetfeather+Sandals) (in the right order) on a [Killer Whale](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Killer+Whale). It doesn't make sense, and it doesn't have to. While a photographer once caught [a picture of a Golden Eagle with a knife](http://i.dailymail.co.uk/i/pix/2012/05/10/article-0-1304EA9E000005DC-378_964x711.jpg), I don't think that most [Squadron Hawk](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk)s actually have the strength to hold up both a [Sword of Feast and Famine](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sword+of+Feast+and+Famine) and a [Batterskull](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Batterskull). That's just a lot of weight. Limiting Equipment to humanoids would put way more pressure than would be reasonable on creative and development to balance Limited—in addition to fostering conversations about how a Dog could definitely hold THIS warhammer in his mouth, even if he couldn't carry a shield. And what about the Naga? They are humanoids, in that they could carry swords, but they wouldn't be able to equip boots. This kind of granularity is fine for some games, but not for *Magic*.

There also individual weirdo things, like how [Emrakul, the Aeons Torn](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emrakul%2C+the+Aeons+Torn) can be blocked by a Thopter token. I mean, the titan eats a ton of the world whenever it moves, but is stopped dead in its tracks by a Thopter. Meanwhile, a lowly [Charging Badger](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charging+Badger) can keep moving with a little encouragement. And Emrakul is even killed by a [Fetid Imp](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fetid+Imp). While that doesn't make any sense in the context of the story of the game, we choose the abilities on creatures for their gameplay interactions, and hope that all the work that we do to keep as much of the flavor working as possible forgives the inevitable parts that don't make sense.

I also think these moments have their charm to them. It's a little fourth-wall breaking, but that's okay. I know that when I first started playing *Magic*, I enjoyed the idea of putting a [Holy Strength](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) on a [Demonic Hordes](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Hordes). Not that I should've been attacking with it, but it was a fun thing to do. Or putting both [Unholy Strength](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength) and [Holy Strength](https://web.archive.org/web/20151218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) on the same creature, and arguing that they should nullify each other. It was this kind of recognition of flavor fails that helped get me deeper into the game as a whole, and ultimately pushed me to where I am today.

That's it for this week. Join me next week, when *Battle for Zendikar* spoilers start in earnest! I've got a pretty nice one for you.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))