---
id: mq6xdnav
kind: article
lang: en
path: /en/articles/feature/2013/01-07-developing-gatecrash
title: Developing Gatecrash
published: '2013-01-07'
column_slug: feature
column: Feature
authors:
- slug: dave-humpherys-4a7b522e
  name: Dave Humpherys
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    lang_detected: en
    capture_id: 619100
    url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    captured_at: '2022-10-04 21:17:27+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    lang_detected: en
    capture_id: 619100
    url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    captured_at: '2022-10-04 21:17:27+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    lang_detected: en
    capture_id: 619100
    url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    captured_at: '2022-10-04 21:17:27+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    lang_detected: en
    capture_id: 619100
    url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
    captured_at: '2022-10-04 21:17:27+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: mq6xdnav
  url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
  page_key: magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
  lang: en
  template: drupal
  captured_at: '2022-10-04 21:17:27+00'
  capture_id: 619100
  wayback_url: https://web.archive.org/web/20221004211727id_/https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
- document_id: mq6xdnav
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/229
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/229
  lang: en
  template: aspx
  captured_at: '2013-06-29 23:29:11+00'
  capture_id: 593245
  wayback_url: https://web.archive.org/web/20130629232911id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/229
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mq6xdnav
  capture_id: 619100
  url: https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
  wayback_url: https://web.archive.org/web/20221004211727id_/https://magic.wizards.com/en/articles/archive/feature/developing-gatecrash-2013-01-07
  captured_at: '2022-10-04 21:17:27+00'
  template: drupal
  sha256: 428882effcf8a6b4d984d1c3f98b5526a27ce07c607b4b7fdc1c4d52ce402f33
render_recovery: []
---
Before I run through a brief introduction of the cast that brought you *Gatecrash* from the development side of things, let me note that there was a ton of work in the planning of this set within a greater context. [Zac Hill](https://web.archive.org/web/20140530202858/http://www.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill) and [Mark Globus](https://web.archive.org/web/20130706022422/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Globus) worked on setting up an Architecture team that went into full force for the sets in this block. They helped answer many questions that wouldn't otherwise have been explored by the time a set typically entered development. They also answered questions that would tie this set into sets and blocks, past and future, in ways we hadn't prioritized to the same extent with sets before this block. 

Similarly, by the nature of the block structure, I owe a lot to the work done on *Return to Ravnica*. [Erik Lauer](https://web.archive.org/web/20140430170951/http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer) and [Ken Nagle](https://web.archive.org/web/20130107000000/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Kenneth%20nagle), along with the Architecture team and the design and development teams, worked out many of the starting points for what would also create the framework for *Gatecrash*. How good and prevalent should the color-fixing be? How should card power be distributed between monocolored and multicolored cards for the best Limited play? Questions like these took a lot of time to solve and I had the benefit of their earlier conclusions in leading my team through a similar process. It left us in a great position from which to explore what *Gatecrash* should be. 

On that note, here's the *Gatecrash* development team: 

![](https://i.ormos.uk/d7/0f/d70f8dade26e853cb0ce60e3db54b835ed336e8f69ebd69fede2ccbafbc530b3.jpg)  

**Dave Humpherys (lead)** 

Resident cloning expert. I've been immersing myself in development, becoming the most frequent development team member in the last while. *Gatecrash* marked my six development team of the last seven sets. In atypical fashion for the development lead of a set, I was also on the *Gatecrash* design team. 

**Mark Globus** 

All-around awesome guy. And did I mention? My boss. Mark is a senior producer for **Magic** and has been around since the first [Great Designer Search](https://web.archive.org/web/20130107000000/https://magic.wizards.com/en/articles/archive/great-designer-search-2006-10-31). Mark led ***Magic** 2012* design and also led development of **Magic**: The Gathering Commander. He fills in as we need him and appears on one or two design or development teams each year. Mark brought wisdom to what was a relatively fresh development team and challenged us on the big picture items. 

**Zac Hill** 

Zac led ***Magic** 2013* development, and before too long you will see the work he put into leading *Dragon's Maze* development. Zac was a great ally in discussing designs, especially within the overall structure of the block. I also picked his brain for insights on what he'd newly learned in leading the development of sets. 

**Max McCall** 

This is [Max](https://web.archive.org/web/20131126163305/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Max%20McCall)'s second development team, quickly following up on ***Magic** 2013*. Max spends much of his time working on the digital side of **Magic** R&D, especially with *Duels of the Planeswalkers*. He's also been an integral part of Cube for **Magic Online** by leading its development. Max has a reputation for finding some imbalance early on in draft format and then continuing to lean on it until he's trounced us enough times to realize we need to adjust. 

**Mark Purvis** 

[Mark](https://web.archive.org/web/20130701024606/https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Purvis) is the senior brand manager for **Magic**. Besides filling up our quota of Marks on *Gatecrash* teams, he was in charge of making sure we had perspective from outside our R&D pit. I was excited to have Mark on the team, since I'd worked with him a lot over the years and seen him enthusiastically help in combining R&D's and Brand's visions together to bring new products and experiences to life. It helped, too, that he's an avid player himself, and has been on past design and development teams, like ***Magic** 2013* design and *Scars of Mirrodin* development. Mark was quick to let me know whenever a card wasn't Timmy enough for him. 

**Gavin Verhey** 

You likely know [Gavin](https://web.archive.org/web/20130630084544/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Gavin%20Verhey) from his ReConstructed column on this site. Gavin also spends a good amount of time working on Kaijudo. This was Gavin's first **Magic** development team. This meant he had a lot of new ideas he was eagerly waiting to share, so I grabbed a great many of them for cards in this set. Gavin brought a great deal of excitement to the team and a fondness for finding all the angles to take in playing Dimir. 

![](https://i.ormos.uk/dc/1f/dc1f36d2390d6554009c3c30e63d6771a017168c03523f5fdd58dee1ccd26263.jpg)

Art by [Clint Cearley](https://web.archive.org/web/20130107000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Clint%20Cearley%22%5D) 

### Mechanical Gears

As we made the transition from design to development, we'd already gone through many playtests with evolve and battalion, which had existed largely unchanged since early in design. They each polled well within the company and were a good fit for the guilds. In development, we still had our work cut out for us with a couple of fledgling mechanics and making sure the guild cards and their mechanics worked well not only for the guild itself, but also with neighboring guilds, even those in *Return to Ravnica*. It was time to get a bunch of parts moving together well. 

Bloodrush was the next mechanic to solidify in the design process. We toyed with a couple of variations that were more all-upside, but these versions subsequently cost more mana and weren't fulfilling the aggressive-minded role we wanted. I was a big proponent of bloodrush, since it fit in so nicely with the two adjacent color pairs. It could provide a remedy and stabilizing agent for the most frequent feel-bad of both evolve and battalion—simply not drawing enough creatures—which goes hand in hand with not having enough creatures in your deck in the first place. There'd typically be a concern that a deck full of creatures can lead to some messy stalemates and for not the most exciting game play. Fortunately, bloodrush helps out in both of those regards.

Simic decks can pack extra bloodrush creatures where they might otherwise use pump spells. To create a diversity of pump effects, we also were already inclined to use a bunch of varied and big stats for bloodrush, which was a good fit for what Simic would want from creatures entering the battlefield. For the Boros deck, bloodrush creatures are an even better fit. White and red creatures most often want a helping hand in getting through other, bigger creatures, and pump spells are great here. Needless to say, so is having a pump "spell" that can also substitute as that third creature you need to set up your battalion.

<table><tbody><tr><td>&#10;						<img src="https://i.ormos.uk/27/72/2772e57acb9c6581ebf5b4057fc716728caaef3617f55f5296d79c91223384dc.jpg"></td>&#10;					<td>&#10;						<img src="https://i.ormos.uk/86/9e/869e831f11f534cc55b32edd6978f28af55a90eb0cd6976177556c683e92aec7.jpg"></td>&#10;				</tr></tbody></table>

While each guild was given options for both aggressive- and defensive-minded strategies, [as we'd worked toward in *Return to Ravnica*](https://web.archive.org/web/20130107000000/https://magic.wizards.com/en/node/645536), the bloodrush creatures admittedly fit best into the more offensively minded strategies. As our next mechanic also directly incentivizes attacking, bolstering defensive strategies in the set further was among the areas in which we especially looked to fortify strategies as development proceeded. 

Next up was cipher. Cipher was very appealing to those we first exposed it to. It was like rebound that kept going and going. This was a big change in direction within the set. The original Dimir mechanic was all about milling. While we held on to many of those card designs (without keywords), we didn't feel it was going to do the work it needed as the central guild mechanic. This was particularly true as we started to think intra-guild, including those we'd see more of with *Dragon's Maze*. While synergies need not just be about the primary guild mechanic, the overload/mill/unleash triad, for example, created a seemingly humorous pairing of objectives. Mill opened up some fun with scavenge but didn't otherwise do enough work for us with the other guilds. 

As such, Dimir has a clearly defined secondary strategy of milling. But the milling isn't all about entirely depleting a library; there's an exploration of the many ways in which making progress on that axis can lead to improved play from your other cards. Cipher is more flexible in its application and can have good roles in either aggressive or more controlling strategies. Cipher isn't as natural a fit with evolve since, in many cases, you are looking to build up a fortress of creatures, but we looked to make sure there were both worthy early evolve creatures like Cloudfin Raptor that could quickly become targets for cipher, assuming you could evolve it at least once. Meanwhile, we looked for early cipher cards, like Hands of Binding, that could help you buy the time to build up. 

<table><tbody><tr><td>&#10;						<img src="https://i.ormos.uk/06/54/065438b8146a92c10e286b43375e90d13569336bba9f4d2ec0170b87246062c7.jpg"></td>&#10;					<td>&#10;						<img src="https://i.ormos.uk/bd/ef/bdef866fbead42c7a6128d39905e767ff5a2b06b16303c7df1e2b01125a9fd4c.jpg"></td>&#10;				</tr></tbody></table>

Cipher figured to be the hardest mechanic to balance, but I'll get to more on that later as I introduce my preview card. It turns out that our implementation of cipher worked well with the final mechanic we settled on, extort, because you can keep casting the spells with cipher and thus can keep triggering extort. Both mechanics could come together well in a variety of deck types.

In leading a mini-team to brainstorm ideas for an Orzhov mechanic, I had a number of items on my wish list for the group. Extort really delivered on all of them, and I'm glad [Shawn Main](https://web.archive.org/web/20131126162723/http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main) came up with the idea. As the last piece of the mechanics puzzle, I really wanted a mana-sink to provide more to do in games that progressed to later turns, like scavenge was doing for *Return to Ravnica*, since the set could use something in this regard. A bleeder-style mechanic was high on the desirable list as well for the guild, and this mechanic tied in perfectly to that. As we were already at three attacking-related keywords, I also wanted to steer clear of that. Extort wasn't the most impressive on a first read, and it was a tad odd thematically in mono-white, but otherwise I quickly started liking it more and more. It was doing really cool stuff for both aggressive and defensive decks as soon as we gave it a try. In terms of pairing up with guilds sharing a color, as I mentioned, it was convenient how it also worked well with cipher. 

In terms of connecting the final gear within the set to Boros, extort was also exciting, since it gave them some reach, removing those last pesky points of life from an opponent. And since it mostly appears on creatures, extort provided yet more flexibility in reaching a "full" battalion.

This put us in a good place to focus on how we best play up the synergies between the guilds and fill in holes.

### Crash and Burn

At the outset, we were interested in moving the Limited format a tad faster than *Return to Ravnica*, in part setting up a contrast between what we expected to be a slower format and what we predicted to be typical of more color-hungry decks likely to follow in *Dragon's Maze*. 

We had to be careful, though, in that we had so many offense-minded mechanics, and ones that could potentially lead to some snowballing of early advantages. This meant that we needed to make sure there were enough ways to break apart early leads and to also embrace the mechanics encouraging you to build up. There are a number of cards, especially removal, that are very deliberately poised better for players on their heels. There are also a number of ways to only temporarily or surprisingly achieve the critical mass of battalion or the opportunity to get an encoded creature through, as opposed to keeping these situations entirely stable.

![](https://i.ormos.uk/a1/70/a17040f6a71464b16a587c6ff39d18c85a4dd9398bf6d3dca087572707642ba6.jpg)

Consuming Abberation | Art by [Karl Kopinski](https://web.archive.org/web/20130107000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Karl%20Kopinski%22%5D) 

Cipher was particularly challenging, and scary, with regard to swingy-ness. In our own internal [New World Order](https://web.archive.org/web/20130107000000/https://magic.wizards.com/en/node/654416) document summarizing how to best tackle complexity we have a list of "Red Flags." These are kinds of cards that cause problems with one or more of our primary goals within New World Order.

What is the first entry on this list?

"Repeatable effects"

The notes in this section for repeatable effects are to make sure that on-board complexity is kept in check and to make sure we protect "fun." Given that we'd be using this mechanic at common, this meant we had to take particular care not to, for example, create something that would become a repeatable "kill" or create hard-to-deal-with permanents. It also meant we could create other effects that would spiral out of control and bog down the battlefield. We had to be careful that it wasn't too easy to curve into nasty card advantage engines or other seemingly insurmountable advantages that didn't require other work or other mana investments.

We created some hoops to jump through, even if small ones, in setting up mini combos with cipher for Limited. Meanwhile, in Standard, as our public was quick to note, we needed to test out many initial card designs with decks highlighting [Invisible Stalker](https://web.archive.org/web/20130107000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Invisible+Stalker). These decks became the real testing ground for what we could and could not do with cipher. 

On that note, let's look at one of the things we decided we could do with cipher.

But first, think about your favorite creature. Ideally a non-legendary one. Any guesses where I'm going with this?

See the card here. 

>> Click to Show

![](https://i.ormos.uk/bf/41/bf41dad26c1acd0ca6d7dd463b03f8e3339265aac506307fc8bdcde1464cc962.jpg)  

Wouldn't you like to have more and more of those creatures... potentially an endless supply of them? Even at a hefty six mana, which demands a lot of power for competitive Constructed, Stolen Identity can make a big impact, and its ability to clone opposing creatures provides plenty of opportunities to make great use of it. Let's say your opponent plays [Thundermaw Hellkite](https://web.archive.org/web/20130107000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite). Now you can have your own hasty Dragon. Encode Stolen Identity onto it, and then on the same turn make another Dragon (or any other creature or artifact that might be on the board). 

Copying, cloning, stealing. I have a soft spot for cards with these effects. You will see a few of these cards in *Gatecrash*. Perhaps more than you'd typically expect, but we had the guilds here where they make a lot of sense. While cloning was something I'd have been more happy to emphasize in Simic, it was a very good mechanical fit for a blue cipher rare, and our creative team found the right Dimir concept to fit for it. Lazav was also already bolstering the copying aspect of the guild. Fortunately, there were still several ways to play up wacky science tropes, like cloning, on other Simic cards; Biovisionary, for example, could have lofty goals with employing this very preview card. 

I hope you are enjoying the preview so far!

Thanks for reading,  
 Dave Humpherys