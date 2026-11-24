---
id: 0m2v89ak
kind: article
lang: en
path: /en/articles/feature/2013/05-01-crafting-the-maze
title: Crafting the Maze
published: '2013-05-01'
column_slug: feature
column: Feature
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    lang_detected: en
    capture_id: 272700
    url: https://magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    captured_at: '2022-10-05 22:44:42+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    lang_detected: en
    capture_id: 272700
    url: https://magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    captured_at: '2022-10-05 22:44:42+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    lang_detected: en
    capture_id: 272700
    url: https://magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
    captured_at: '2022-10-05 22:44:42+00'
    rule: drupal.div_author
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/245b
    lang_detected: en
    capture_id: 219126
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/245b&print=true
    captured_at: '2013-07-06 03:34:54+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 0m2v89ak
  url: https://magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
  page_key: magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
  lang: en
  template: drupal
  captured_at: '2022-10-05 22:44:42+00'
  capture_id: 272700
  wayback_url: https://web.archive.org/web/20221005224442id_/https://magic.wizards.com/en/articles/archive/crafting-maze-2013-05-01
- document_id: 0m2v89ak
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/245b&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/245b
  lang: en
  template: aspx
  captured_at: '2013-07-06 03:34:54+00'
  capture_id: 219126
  wayback_url: https://web.archive.org/web/20130706033454id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/245b&print=true
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: 0m2v89ak
  capture_id: 219126
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/245b&print=true
  wayback_url: https://web.archive.org/web/20130706033454id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/245b&print=true
  captured_at: '2013-07-06 03:34:54+00'
  template: aspx
  sha256: eb1ca9f66e7f4921121345c44902e6c6fda2948a85b89fc88c9d6b7bd527ee2b
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Cyclopean Giant
  - Plated Pegasus
  - Glass Asp
  - Cyclopean Mummy
  - Cyclopean Tomb
  - Lightning Helix
  - Putrefy
  - Selesnya Evangel
  - Sabertooth Alley Cat
  - Street Savvy
  - Convolute
  - Snapcaster Mage
  - Sphinx's Revelation
  - Ral Zarek
  occurrences: 25
---
Hey, y'all!

  
  

It's been a while since I've graced the pages of the good ol' DailyMTG.com, but as the lead developer of *Dragon's Maze* they decided to let me climb back up onto the podium for a little bit and talk about the set. 

The first set I worked on was *Rise of the Eldrazi*, and the last was "Huey," which (despite my having been out of the Wizarding world for a while now) still won't come out for another year and a half or so. Point being I've had my paws on a number of **Magic** sets, and yet *Dragon's Maze* had maybe the most unique demands of any set I've ever seen. 

[![](https://i.ormos.uk/33/a2/33a216be73cac4d75845e4b19ded1105ccfce96c36b2849c10d8023eeb551f90.jpg)](https://web.archive.org/web/20130501000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=126281) 

  

Back in the day, Wizards of the Coast made a block called *Time Spiral*. I was a PTQ/Pro Tour regular at that point and still look back on that era fondly, with an astounding Draft environment and maybe the most fun Block Constructed qualifier format I had ever played. Yet the block was hugely unpopular among the vast majority of players, selling poorly across the board, and we at Wizards learned a lot of lessons in the aftermath. 

The biggest problem was simply this: busting open a pack was *incomprehensible*. Everything did everything. There were what seemed like fifty zillion keywords on every card, many of which had nothing whatsoever to do with one another, and unless you had been playing **Magic** (like I had) long enough to get all the references and in-jokes, the set put up a brick wall in front of you and said, "Nah, dawg, this ain't for you." 

It's tempting, of course, to say, "Well, not everything can be for new players—what about the loyal fan base that's been with you forever?" There's some merit to that. But I'm not sure the set even succeeded along that axis, really. *Innistrad* proved you can create some truly great game play without having to use fifteen million words to do it. Meanwhile, cards like Cyclopean Giant, Plated Pegasus, and Glass Asp certainly contained references that I *got*, but I wasn't really sure why it was cool that I was *getting* them. "Ooh—two Cyclopean Mummys stapled together inside a Cyclopean Tomb! I remember now! What's better than three sucky cards? *One* sucky card that's a combination of all three!" 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Cyclopean Mummy" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Cyclopean%20Mummy&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Cyclopean Tomb" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Cyclopean%20Tomb&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Anyway, the point of all of this was that we became cautious about jamming sets full of too much *stuff*. Yet the very structure of *Dragon's Maze* dictated that it wanted to be full of *stuff*. Ten guilds in one set—that meant ten keywords and ten color combinations from Day One, to say nothing of anything new we might want to add. We were treading on very dangerous territory from the get-go, and we had to be careful. 

There was upside, though. We knew *Return to Ravnica* and *Gatecrash* had the potential to be two of the most awesome sets of all time. Doing *Dragon's Maze* right would mean adding to that awesomeness while tying the two sets together in an unprecedented way. As awesome as original *Ravnica* block was, it had a couple major flaws, the biggest of which was that once you were done, you were done. Like Golgari? Well, sorry, you're not getting any more in *Dissension*. Being able to provide that closure while maintaining the core of what made the original *Ravnica* block great gave us the potential to create what could be the best block in all of **Magic** history. 

No pressure.

Trouble was, what did *Dragon's Maze* want to *be*? It was, after all, its own set, smushed together at the end of a heretofore unheard-of back-to-back two-large-set block. It had to allocate its one-hundred-fifty-six cards to ten different guilds, while leaving enough room for its standalone cards to shine as well. It couldn't feel like an afterthought, an obligatory release to occupy a slot on the schedule. But neither could it be some kind of magnum opus, a grandiose conclusion to a paradigm-setting block—that wasn't its role. What was there to do? 

Eventually, we realized that the set didn't want to go in a whole 'nother direction from its predecessors, as many third-sets do. It wanted to take what you liked about *Return to Ravnica* and *Gatecrash* and give you more of it, while also tying the two sets together in a way that neither set could do individually. It wanted to be "more of the same kind of awesome." For Constructed, the goal was to provide new cards. For Limited, the goal was to provide new *perspectives*, to provide lenses with which to view *Gatecrash* cards in the light of *Return to Ravnica* and vice versa. 

And maybe, just maybe, it could have a few "twists" of its own.

With that in mind, [Alexis](https://web.archive.org/web/20130706042207/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Alexis%20Janson) and her team headed boldly into design. 

### Turn On, Tune In, and Cut Out

I know for a fact that at every step of the design process, Alexis and her team were wholly conscious of the dangers of complexity creep. She spent tons of time tightening up the set, creating a series of cycles and slots that gave the set symmetry, unity, and cohesion. She played the set with *Return to Ravnica* and *Gatecrash* and took great strides to ensure the cards made sense with one another. She did everything she could to make sure every word on every card was pulling its weight. 

Still, it was a labyrinth, a jungle of half-formed possibility. A lot was there, obviously—but, through the branches, it was impossible to see. So we started taking a hatchet to things.

First casualty: the ten Cluestones. Originally, each Cluestone sacrificed for a different effect. Then, they entered the battlefield for a different effect. Then, they went back to sacrificing. Alexis didn't want the set to be bogged down by cycles containing ten of the same card—and rightly so! Unfortunately, keeping these separated was just too confusing. "Oh—is that particular black Cluestone the one with the drain effect or the kill effect or the double raise dead?" Thinking about them was a nightmare, especially under the rules of [New World Order](/en/articles/makingmagic/2011/12-05-new-world-order). Moreover, balancing the ten of them was hard, and we kept having people bring up the fact that their guild was getting the shaft. In the end, we decided that for simplicity's and elegance's sake we wanted to go with the good, clean, straightforward, universally playable designs you see right now. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Selesnya Cluestone" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Selesnya%20Cluestone&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Dimir Cluestone" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Dimir%20Cluestone&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Then: gold cards. I talked already about the problems with *Time Spiral*, but I have yet to bring up the problems with *Alara Reborn*—another one of my favorite-ever sets. In both cases, opening a booster pack was just utterly incomprehensible for most people, but for *Alara Reborn* the reason was entirely different. Unlike *Time Spiral*, you didn't even get to the point of reading the cards. It was just this sea of gold, a weird [combinatorics](http://en.wikipedia.org/wiki/Combinatorics) problem you had to think about before you could even get to the point of putting cards in decks. It was way too weird, and since then we've been conscious—even for multicolored sets—about how many gold cards go into packs. I did a *lot* of work as a part of architecture (an R&D team focused on maintaining the cohesion between sets and blocks) mapping out the distribution of multicolored cards across *Return to Ravnica* block, basing my numbers off original *Ravnica* block and taking into account both (a) the new allocation of guilds and (b) the new number of total cards in the set. 

Ravnica, it turns out, didn't actually contain that many gold cards on a per-pack basis. While I remember things like Lightning Helix and Putrefy and Selesnya Evangel, there were also a whole lot of Sabertooth Alley Cats and Street Savvys and Convolutes and other monocolored pieces of what was largely "filler." *Dragon's Maze* had three gold cards per guild at common in the handoff. This doesn't sound like much, but it resulted in each pack containing around nine gold cards in total. We were cognizant of the lessons of *Alara Reborn*, so we reduced that number to just over five by cutting our gold cycle down to one per guild. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Lightning Helix" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Lightning%20Helix&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Sabertooth Alley Cat" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Sabertooth%20Alley%20Cat&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Still, our playtesters were bewildered. A breakthrough came when [Mark Globus](https://web.archive.org/web/20130706022422/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Globus) sat my team down and asked, "Okay—what is the set about?" We settled upon two—okay, two and a half—things. The first was multicolored cards. After all, that's what's super-cool about the block. The guild model is totally amazing, but a lot of the reason it's amazing is that it gives structure to the abstract concept of multicolored creatures, which are themselves cool because of the abstract concept of the color pie. The second was the whole Gate thing, which is taking center-stage in *Dragon's Maze* booster packs (check out the awesome panorama-like [new Gate art](/en/articles/arcana/2013/04-17-zoomed-guildgates)) and cements the story of the entire block together with, well, the actual maze. The idea, then, was to embrace a [Rosewaterian](https://web.archive.org/web/20130701165759/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater) maxim—"If it's not at common, it's not what your set is about"—and create some common cycles that tied the set together. These became the [Gatekeepers](https://web.archive.org/web/20130501000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Dragon%27s+Maze%22]&name=+[Gatekeeper]) and the [Maze creatures](https://web.archive.org/web/20130501000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Dragon%27s+Maze%22]&name=+[Maze]&type=+[%22Creature%22]), which also served the "half" a goal very nicely: slowing the set down. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Opal Lake Gatekeepers" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Opal%20Lake%20Gatekeepers&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Maze Rusher" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Maze%20Rusher&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

See, both *Return to Ravnica* and *Gatecrash* Limited were relatively fast formats in playtesting, by design. This was because we knew that drafting the sets in concert with one another would shake up mana bases substantially. Whenever you "hiccup" on mana, it's just less likely that you're deploying threats quickly, so we figured the Draft environment post- *Dragon's Maze* would be relatively slow. This meant that in order for that transition to seem meaningful, we wanted to start the format out pretty fast—creating a "change in feel" from *Return to Ravnica* to *Gatecrash* because of the five new guilds, and a change from *Gatecrash* to *Dragon's Maze* because the format would slow down dramatically. Putting in a cycle of (a) four-mana 2/4s and (b) powerful six-mana commons would further encourage that change in tempo for the better. 

### Tweaks on a Leash

These changes, plus the normal processes of development, allowed us to get the set into shape for intensive playtesting. This led us to realize that the Limited environment, after getting its skeleton together, really needed some focus. The thing is, a lot of gold environment trend toward "good-stuff" decks that just aren't very fun to play. You cast your powerful cards over and over again until your opponent dies. What this means is that after you recognize the pick order, you don't find yourself having a lot of fun in Draft.

Our solution was twofold: first, we'd concentrate a lot of the multicolored cards' power in a cycle of "Lieutenants" at uncommon, or powerful creatures whose abilities lend themselves to certain styles of play. This meant that to maximize your most powerful options in Draft, you'd have to pursue a strategy with direction rather than just take context-independently powerful cards. Afterwards, we "curved out" the most powerful cards in every guild across the block and made sure our most powerful cards occupied different slots along the mana curve. This ensured that you'd be able to draft both aggressive and controlling decks without having to sacrifice card quality. Then, if certain aggressive strategies lacked playables along certain spots of the curve in certain densities, we tweaked *Dragon's Maze* cards to fill in those holes. The goal was to slow down the environment as a whole while providing enough tools for the aggressive decks to function. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Blaze Commando" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Blaze%20Commando&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Korozda Gorgon" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Korozda%20Gorgon&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

After this point—plus a lot of micromanaging of individual designs—we felt pretty good about Limited. In fact, the way I am describing it, it sounds like a huge percentage of early development was devoted to Booster Draft. That's because it was. As a point of fact, we also spent a huge amount of time trying to get the Prerelease format right, but solving the problems with Draft helped to solve that format as well. In general, Limited playtesting also drives progress for Sealed Deck, Booster Battle Packs, and Casual Constructed, assuming you're thinking about how the game will play out given that a player opens N number of booster packs. If you think actively about it, you can anticipate the consequences of your tweaks and changes with a pretty solid degree of accuracy.

This led us to the bulk of our Constructed testing. In general, you want to work on the commons and uncommons you expect to be relevant Constructed players first, because you can't tweak those without substantially shaking up Limited. Fortunately, it's usually pretty easy to tell how viable lower-rarity effects are going to be in Constructed, since they tend to produce the kind of interactions you've seen before. The one exception to this was Lightning Helix, which I fought for *stridently* to remain in the set, but proved to be overpowered in concert with Snapcaster Mage and Sphinx's Revelation. 

Alas.

[![](https://i.ormos.uk/42/5c/425cdbe7d26f3cb19c9f90716223ce16d6ca17111d25c6ec34bacd88f97c32d3.jpg)](https://web.archive.org/web/20130501000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=369081) 

  

Normally, when it comes to Constructed testing, we simply move the set into the [FFL](/en/articles/feature/2011/10-17-greetings-from-the-future-future) and let the playtesters start grinding. With this set, though, it was important to me that it was actually meeting the goal of giving you more of what you like from *Return to Ravnica* and *Gatecrash*. That is, if *Dragon's Maze* cards were going into decks, but they weren't going into the decks enabled by *Return to Ravnica* cards, the set wasn't living up to its vision. So I conscripted numerous people both on and off the team to go about designing guild-based decks from *Return to Ravnica* and *Gatecrash*. Then, I asked them which cards (if any) they wanted to play from *Dragon's Maze*, and whether they would fit nicely into those decks. I deliberately costed *Dragon's Maze* cards to fill in holes in mana curves left by the existing *Return to Ravnica*-block designs and tried to make sure no guilds were left out. We tested these decks extensively, tested Block Constructed, and only then moved forward into Standard—with an eye toward enabling the cards that were players in the guild-based Casual Constructed decks. 

The single card we probably spent the most time on was our Planeswalker, Ral Zarek. He went through probably eight different redesigns and at least three different costs. The issue kept being that he lacked "personality"—that, as a true member of the Izzet League, he really needed to feel Izzet and not just blue-red. So the versions that just drew cards and dealt damage felt kind of "meh" to a lot of people. Eventually, we drew inspiration from the "stormy" feel of his **Duels of the Planeswalkers** deck and settled on a design we felt was kind of quirky, kind of off the wall, but was still powerful and appealing and had the potential for massive, massive upside. We're pleased with the result. 

### Smoothing the Edges

From there, it was just a matter of marginal variations. Editing happened, which changed some things. Originally, the ten legends were sprinkled through the set at both rare and mythic rare, but [Doug Beyer](https://web.archive.org/web/20130625063128/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer) from the creative team felt strongly that they should all be present at rare. This resulted in some late redesigns. Then, of course, was templating, where a lot of my carelessness with regards to how many "you may"s and "up to"s and "target player"s and "target opponent"s was laid bare for all the world to see. 

And then I left, and sometime after that the set left, and after enough time has managed to fly here we all are now sitting around opening the cards in booster packs!

It's been almost six months since I left the vaunted walls of Wizards. I'd be lying if I said I didn't spend a lot of time missing it, even as I love what I'm doing here in New York. The love every member of R&D pours into the game is palpable, tangible, and it manifests itself inside a set like *Dragon's Maze* as much as any other. I've talked a lot about what I've done with *Dragon's Maze*, but I don't want to undermine for a second the tremendous effort and insight of every member of both the design and development teams. They make **Magic** what it is—and some of us simply get to be lucky enough to take the credit. 

I hope you enjoy *Dragon's Maze*. I'm eager to hear your stories, and I'm eager for you to share the memories the set has helped you create. Please, let me know. 

Zac

![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueBegin_Top.jpg) ![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueBegin_LeftOfButton_01.jpg) [![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueBegin_Button_01_Static.jpg)](/en/events/2011/league-facts/avacyn-restored-league) ![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueBegin_RightOfButton_01.jpg) [![](http://media.wizards.com/images/magic/daily/footers/DGM/EN_DGM_ArticleFooter_LeagueBegin_Bottom_Static.jpg)](https://web.archive.org/web/20130710043245/http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/dragonsmaze/productinfo) 

  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)

 

![Zac Hill](https://i.ormos.uk/2d/72/2d72b81445c4e8a88d9f4fe8b3bced02d1310c1683426ad71415285f6c9629c4.jpg "Zac Hill")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Zac Hill</b>&#10;        <br>&#10;        <a href="https://twitter.com/zdch">@zdch</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130501000000/http://www.wizards.com/company/emailtoauthor.asp?author=Zac%20Hill&amp;amp;headline=[Crafting%20the%20Maze]">Email Zac</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20130523185550/http://www.wizards.com/magic/magazine/archive.aspx?author=zac%20hill">Author Archive</a>&#10;        <br>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for *Dragon's Maze*. His articles have appeared in The *Huffington Post*, *The Believer*, and on [StarCityGames.com](http://www.starcitygames.com/). Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 

 