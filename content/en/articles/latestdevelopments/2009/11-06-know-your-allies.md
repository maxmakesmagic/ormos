---
id: yvjqq4ym
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/11-06-know-your-allies
title: Know Your Allies
published: '2009-11-06'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    lang_detected: en
    capture_id: 723395
    url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    captured_at: '2022-05-24 03:57:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    lang_detected: en
    capture_id: 723395
    url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    captured_at: '2022-05-24 03:57:58+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    lang_detected: en
    capture_id: 723395
    url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    captured_at: '2022-05-24 03:57:58+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    lang_detected: en
    capture_id: 723395
    url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
    captured_at: '2022-05-24 03:57:58+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: yvjqq4ym
  url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
  page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
  lang: en
  template: drupal
  captured_at: '2022-05-24 03:57:58+00'
  capture_id: 723395
  wayback_url: https://web.archive.org/web/20220524035758id_/https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06
- document_id: yvjqq4ym
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/63
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/63
  lang: en
  template: aspx
  captured_at: '2013-07-07 07:36:49+00'
  capture_id: 623436
  wayback_url: https://web.archive.org/web/20130707073649id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/63
- document_id: yvjqq4ym
  url: https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-05
  page_key: magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-05
  lang: en
  template: drupal
  captured_at: '2021-12-08 01:40:32+00'
  capture_id: 723391
  wayback_url: https://web.archive.org/web/20211208014032id_/https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-05
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: yvjqq4ym
  capture_id: 623436
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/63
  wayback_url: https://web.archive.org/web/20130707073649id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/63
  captured_at: '2013-07-07 07:36:49+00'
  template: aspx
  sha256: 6462f3823392aac9e50aca081b6d393db1af19ba8711a0f79a7ea26bc7f70f91
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Krovikan Mist
  - Sound the Call
  - Oran-Rief Survivalist
  - Umara Raptor
  - Grizzly Bears
  - Wind Drake
  - Nimana Sell-Sword
  - Hagra Diabolist
  - Murasa Pyromancer
  - Stonework Puma
  - Tajuru Archer
  - Tuktuk Grunts
  - Kazuul Warlord
  - Turntimber Ranger
  - Makindi Shieldmate
  occurrences: 32
---
Welcome to the end of Ally Week! Today, I'll be telling the story of the overall development of the Allies, and then I'll tell the stories of a few Allies in particular.

### The Allies Developers Tell

I'd like you to put on your **Magic** developer hat and ponder a question for a moment. How far below the power curve should an Ally be in a Limited deck that has no other Allies?

![](https://i.ormos.uk/0d/ac/0dac2a41b09cb67b49733d320d85bc3d33862263d0b8b2a0d2839a43cfdb4bb1.jpg) 

  

Before you go running in horror, let me explain. Allies are a linear mechanic; the more Allies you have in your deck, the better they all are. If each Ally alone were as powerful as a normal card, everyone would take them very high in drafts, and you would never have the chance to accumulate lots of them to make an awesome-feeling deck. However, if they were all worse than normal cards, few people would think to draft an Ally deck to begin with. What to do?

We've done a linear mechanic with similar consequences for Limited before. Do you remember where?

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Krovikan Mist" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Krovikan%20Mist&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Sound the Call" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Sound%20the%20Call&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Yes, that's right! We did it in *Coldsnap*. *Coldsnap* had a number of commons like this that scaled in power based on the number of them you had in your deck. A single Krovikan Mist is a two mana 1/1 flyer, and a lone Wolf from a Sound the Call is a three mana 2/2; neither of these are anything to write home about. However, *Coldsnap* was a small set that was drafted as though it were a big set, so it was very possible to collect large numbers of either of these cards. I've seen *Coldsnap* draft decks with seven of each of these two cards, and with that many copies of them the cards were quite powerful. 

We started the Allies in *Zendikar* in a spot similar to this. Have a look at Low Level Wizard and Faithful Robot, two Allies from early *Zendikar* design.

![](https://i.ormos.uk/64/9b/649b4552ce40d78eba553b7df1f072f6105d8cebd317d41609e3838362e3d0ef.jpg) 

  

Note that these cards are templated so that they do not give themselves a +1/+1 counter. A Low Level Wizard without a party is actually a two mana 1/2, and a Faithful Robot with no one to be faithful to is a sad four mana 2/3.

This made the Allies look bad, but it had a hidden benefit. In draft playtests, no one would touch the things if they weren't drafting a teamwork deck. That left the door wide open for someone who wanted to draft a dedicated teamwork deck to swoop in and get almost every Ally at the table. I won a playtest draft once with a whopping seven Low Level Wizards and two Faithful Robots, which could only happen because no one else was interested in taking them. Nothing as amazing as that happened again, because after that draft people started to wise up and began to hate draft Allies late in the pack when nothing else was there for them. However, generally speaking the Allies were still making it to the people who wanted them, and everyone else refused to touch them.

This is exactly what allowed people to collect upwards of seven copies of Krovikan Mist and Sound the Call in triple *Coldsnap* drafts. However, there was also a real cost to having the Allies only be appealing to people who were playing Allies. That cost is that, well, they simply looked weak. Two mana 1/3's and four mana 2/3's are not the kind of cards that get most people excited about a mechanic. The Allies were important for conveying the flavor of the set, but they wouldn't do that work if no one wanted to play them in the first place! 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Whipcorder" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Whipcorder&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Exalted Angel" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Exalted%20Angel&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

To accomplish our goals, we needed to include some Allies that were reasonable to play without a big pile of fellow Allies. *Zendikar* developer Erik Lauer observed that a player's journey toward liking a **Magic** mechanic often begins with one or two cards that are obviously powerful enough to play. For example, Whipcorder and Exalted Angel served as flagbearers for morph in *Onslaught*, showing players the fun that was present in the mechanic. We needed to have Allies that mimicked this effect, drawing players into having Allies in their deck. This would both show them that Allies were fun to play with and make all the rest of the Allies more powerful.

Mark Rosewater [talked in his article this week](/en/articles/makingmagic/2009/11-02-true-allies) about the division that the *Zendikar* designers made between "fighters," "clerics," and "wizards." They decreed that every Ally would have an ability that triggered every time an Ally entered the battlefield. However, fighters were Allies whose abilities put +1/+1 counters on themselves, clerics were Allies who gave temporary bonuses to every Ally you controlled, and wizards were Allies whose triggered abilities explicitly counted the number of Allies you controlled. 

![](https://i.ormos.uk/5a/06/5a063888c52647db90b18211f7ed48a8cab55e0ceb1b65fdeac518bab95e2aa6.jpg) 

  

By nature, the clerics and wizards needed lots of other Allies to be powerful. Therefore, it fell to the fighters to carry the flag for the rest of the Allies. We chose to give each of the fighters numbers that would let you play them in any Limited deck with a straight face. For example, Oran-Rief Survivalist and Umara Raptor have the same numbers as Grizzly Bears and Wind Drake, both of which are cards that are more than reasonable to play in any Limited format. However, with only a little help they get significantly better.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Oran-Rief Survivalist" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Oran-Rief%20Survivalist&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Umara Raptor" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Umara%20Raptor&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Making this change did exactly what we wanted in our playtesting. It was not uncommon in *Zendikar* limited for me to take a Nimana Sell-Sword to fill in my black deck's curve, then take a second Nimana Sell-Sword over something that I might have taken over the first one. Suddenly, the next Hagra Diabolist I see has gone up in value even though I didn't go out of my way to make an Ally deck. This is exactly how Erik hoped the Allies would work in practice. 

One of the most exhilarating things I experience as a **Magic** developer is when I interact with players in the real world and watch things happen exactly how we hoped they would. I got to experience that recently when I hosted a draft at my apartment with some friends. I opened a Murasa Pyromancer, which is an extremely strong card in an Ally deck–so strong, in fact, that I decided to move in on Allies with my first pick. It was clear to me by the end of the draft that I was the only pure Ally drafter at the table; I got all of the Stonework Pumas and Tajuru Archers I could handle. However, my friend Jon had picked a Tuktuk Grunts to fill in his curve, which prompted him to take a Murasa Pyromancer just before it got to me in pack two. I was unhappy, but I was satisfied that the Allies were working the way we meant them too. I was also quite satisfied with my deck, which had a whopping fifteen Allies in it! 

### True Stories, Honest Allies

Now, let's investigate a few Allies in particular that have interesting stories. 

### Makindi Shieldmate

![](https://i.ormos.uk/c8/7a/c87abf450531343be9ec6d2833b2df0e2a277a91fba50cddd10dfa5713fb5707.jpg) 

  

One development tool that *Zendikar* lead developer Henry Stern used was something that he called "league". In the Future Future League, we play as though we have access to four copies of every card so that we can get a picture of competitive Standard, but we need to make sure that **Magic** is fun at every level. To get a different picture, Henry gave each of us ten rares, and asked us to build decks using up to one copy of each of those rares, up to two copies of any *Zendikar* uncommon, and up to four copies of any *Zendikar* common. I received both Kazuul Warlord and Turntimber Ranger in my rares, so I tried to build an Ally deck. However, the very first Ally I hit in the file was Makindi Shieldmate. I wanted my deck to attack, so I made this comment, and moved on.

 ![Makindi Shieldmate](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Makindi%20Shieldmate&options=) 

> TML 11/20/2008: This card disappointed me when I went to build a teamwork league deck. :B

This prompted a similar comment from Greg Marques, an experienced designer who has worked on many **Magic** sets. 

> GM 11/21: What's the upside here? If I have a teamwork deck I will have several huge creatures that are big enough to block anything, what does this guy add to the team?

I later returned to the file with a few weeks' perspective, and suddenly I was defending the card. I still don't know what prompted this comment, but **Magic** development is as much an art as it is a science and I suppose I just had a feeling here.

> TML 12/1/2008: I don't really have a good reason why, but I think this is a reasonable thing to have around. Big defenders are fun, and this guy does get big.

Aaron Forsythe and Ken Nagle both have more game design experience than I, and they were able to articulate the reasons why Makindi Shieldmate should exist. 

> AF 1/4: People who like linear scaling mechanics often like to sit around and grow their team. This guy is perfect for that.
> 
> KEN 1/12/2009: It's like SimCity but with Magic cards – as long as you still have stuff in your hand to cast, you're not done building up and thusly not at full fighting capacity. In StarCraft we didn't attack until we had 200 food armies.

![](https://i.ormos.uk/88/09/8809078e098e4e38042fca37d87b2f7793a2d71ebd20a7a96a628645d217e815.jpg) 

  

Ken Nagle is a fascinating person to talk to about games. He's very smart, and many people with his intelligence would have used that skill to become an expert player, then do their best to crush everyone they played against, eventually finding their way to the Pro Tour. It is a little-known fact that Ken *has* played in a Pro Tour; he describes this as an accident, but it still demonstrates that Ken is very good at **Magic**. However, he is extremely self-aware and he uses that self-awareness to maximize his own fun rather than his winning. Many of his casual decks are as carefully tuned as any deck I've ever played in a tournament, with exactly the right numbers of each card to be the most fun to play with.

![](https://i.ormos.uk/29/07/29070ec0db446f77d56b9ff9916a5bfb9fdf3e79af5c38a21ed2d1607c6c5761.jpg) 

  

The kind of insight that Ken conveyed in this comment field is exactly why he is so valuable to **Magic** R&D. In Starcraft, every unit has a "population" cost, and you aren't allowed to build a unit that would put you over 200 "population" across your entire army. As Ken notes here, much of the fun of Starcraft is the buildup of an enormous army while you watch your population count tick higher and higher. Makindi Shieldmate both buys you the time you need in a game of **Magic** to tick your army higher and higher and is fun to watch as it gets bigger and bigger!

### Turntimber Ranger

![](https://i.ormos.uk/a1/40/a140ab90585e927ee03797f56c72b0fc7bd456ac4d56eee3c63ac918dd198005.jpg) 

  

The idea of an Elf Ranger who has "pets" was something that we knew was going to have to be on an Ally somewhere. It's a classic trope that is expressed in games like **Dungeons & Dragons**, which is what we were trying to convey in *Zendikar*. However, putting tokens onto the battlefield would make Ranger fall into the "Wizard" bucket, which meant that we were going to need to somehow count the number of Allies on the battlefield when we put a token onto the battlefield. We thought it would be too weird to have an X/X token with X as the number of Allies on the battlefield, because there wasn't a single creature type that would cover all possible values of X. Instead, we decided to have Turntimber Ranger put X 1/1 Wolves onto the battlefield, because X 2/2's seemed crazy to us. As you can see here, Aaron Forsythe and Doug Beyer found the problem with this plan.

 ![Turntimber Ranger](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Turntimber%20Ranger&options=) 

  

> AF 11/20: Several cards in LRW, MOR, SHM, EVE, and M10 say "Wolves are 2/2." Snakes are 1/1 green tokens in this file...Find a cost that lets the Wolves be 2/2s. I think one 2/2 at a time is enough incentive...It doesn't have to explode exponentially to be really fun.
> 
> DB 11/25/08: Agree with AF, making this guy's Wolves 2/2 would really help me make 1/1 green Snakes.
> 
> AF 1/4: These will somehow be 2/2s; Del's issue to be discussed.

![](https://i.ormos.uk/23/a7/23a7b991a211780bf3226ca2fa90cf1a1ece23c6b008e06fd57ee69ed9a6785b.jpg) 

  

Aaron put his foot down, forcing us to come up with a different ability. We felt quite stuck for a while; we didn't want to put X 2/2's onto the battlefield, but we also needed Ranger to create Wolves, and Wolves are 2/2's. In a frantic meeting, someone came up with the idea of making Turntimber Ranger a "dual-class" Ally; that is, it would be a fighter, but do something else too. We found this satisfying, and now Turntimber Ranger gets both a +1/+1 counter and a Wolf friend every time a new Ally arrives on the battlefield. 

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>When was the last time you played Magic Online?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>I've never played Magic Online.</td>&#10;    <td>4166</td>&#10;    <td>55.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>More than 6 months ago</td>&#10;    <td>1145</td>&#10;    <td>15.3%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Within the last 6 months</td>&#10;    <td>218</td>&#10;    <td>2.9%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Within the last 3 months</td>&#10;    <td>270</td>&#10;    <td>3.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Within the last month</td>&#10;    <td>274</td>&#10;    <td>3.7%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Within the last week</td>&#10;    <td>633</td>&#10;    <td>8.5%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Today</td>&#10;    <td>416</td>&#10;    <td>5.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>I'm logged into Magic Online right now!</td>&#10;    <td>344</td>&#10;    <td>4.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>7466</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

There is no greater meaning to this poll. I was merely curious. Thanks for the feedback!

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>Which of the following <b>Magic</b> products are you most excited about?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtg_daily_ld_63_poll1">&#10;                            <div>&#10;                              &#10;                              &#10;                              <i>Premium Deck Series: Slivers</i>&#10;                              <br>&#10;                              &#10;                              &#10;                              <i>Deckbuilder's Toolkit</i>&#10;                              <br>&#10;                              &#10;                              &#10;                              <i>&#10;                                <b>Magic: The Gathering</b> - Tactics</i>&#10;                              <br>&#10;                              &#10;                              &#10;                              <i>Duel Decks: Phyrexia vs. the Coalition</i>&#10;                              <br>&#10;                              &#10;                              &#10;                              <i>Alara Block Premium Foil Booster Pack</i>&#10;                              <br>&#10;                              &#10;                              None of these excite me.<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>