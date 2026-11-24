---
id: q9fqtr5f
kind: article
lang: en
path: /en/articles/makingmagic/2014/01-27-born-to-be-compiled-part-1
title: Born to be Compiled, Part 1
published: '2014-01-27'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    lang_detected: en
    capture_id: 867717
    url: https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    captured_at: '2022-05-27 20:19:18+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    lang_detected: en
    capture_id: 867717
    url: https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    captured_at: '2022-05-27 20:19:18+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    lang_detected: en
    capture_id: 867717
    url: https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    captured_at: '2022-05-27 20:19:18+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    lang_detected: en
    capture_id: 867717
    url: https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
    captured_at: '2022-05-27 20:19:18+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: q9fqtr5f
  url: https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
  page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
  lang: en
  template: drupal
  captured_at: '2022-05-27 20:19:18+00'
  capture_id: 867717
  wayback_url: https://web.archive.org/web/20220527201918id_/https://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27-0
- document_id: q9fqtr5f
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/284
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/284
  lang: en
  template: aspx
  captured_at: '2014-04-27 21:18:33+00'
  capture_id: 652281
  wayback_url: https://web.archive.org/web/20140427211833id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/284
- document_id: q9fqtr5f
  url: http://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27
  page_key: magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27
  lang: en
  template: drupal
  captured_at: '2016-11-17 19:55:04+00'
  capture_id: 867715
  wayback_url: https://web.archive.org/web/20161117195504id_/http://magic.wizards.com/en/articles/archive/making-magic/born-be-compiled-part-1-2014-01-27
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: q9fqtr5f
  capture_id: 652281
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/284
  wayback_url: https://web.archive.org/web/20140427211833id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/284
  captured_at: '2014-04-27 21:18:33+00'
  template: aspx
  sha256: e347dc1cb33ed8720066750057ef83ed05ea9346e5dd3b1ae37e36c29f3537f6
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Wingsteed Rider
  - Didgeridoo
  - Chandra, Pyromaster
  - Kiki-Jiki, Mirror Breaker
  - Staunch-Hearted Warrior
  - Centaur Battlemaster
  - Ral Zarek
  occurrences: 12
---
Previews are over and the set is now [all public](https://web.archive.org/web/20140424025435/http://www.wizards.com/Magic/tcg/article.aspx?x=mtg/tcg/bornofthegods/cig). You know what that means? (To my podcast listeners—no, it means something different.) It means it's time for some card stories, where I tell some design stories a little smaller in scale. I do this every set, so you guys and gals know how this works, which means let's get to it. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/hzmsboGDw1_EN.jpg) 

 

People often ask me what the highlights of design are. "What exactly makes you most happy when you design cards?" There isn't a single answer, as there are many highs of design, but I'm guessing most people would never guess that Akroan Skyguard would be an answer to this question. Let me explain.

One of the hardest things about designing a block is managing the resources of the mechanics you plan to use for the whole block. Heroic is one such mechanic. What happens is that the first set figures out how much it needs and then makes cards. Sometimes, it assigns a particular section of the design, which it will save for future sets (I'll talk about how we did this with bestow next week) but often the first set just tries to make the cards it needs and lets the second and third sets fend for themselves.

While working on *Born of the Gods*, we were searching for simple heroic cards. One of white's things is that it has cheap, small creatures that get a single +1/+1 counter when targeted. I remember the day we figured out that somehow *Theros* didn't have a 1/1 flier with heroic. During *Theros* design we had designed it, but number juggling had ended up turning it into a 2/2 (Wingsteed Rider). That meant that the nice, simple card we needed was available. The discovery that what you need wasn't already done is a great feeling, and after years of doing design, it's one of my favorites. There is one thing that feels even better, though: when you find it while doing the third set. But we'll talk about that during the card stories of *Journey into Nyx*. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/D9ZaGtJnL8_EN.jpg) 

 

One of the things that's important to remember is that the game of **Magic** has certain influences and that it will push players to do certain things. One such influence is the limited number of cards available in a format combined with the four-card restriction. What this tends to do is encourage players to max out with four copies of all their best cards. Usually, one particular card is better than the rest at the same cost, so players will usually opt to play four of that card over diversifying. 

That's why cards like Bile Blight exist, to push a little in the opposite direction. From time to time, we like to design cards that punish players for not diversifying their cards. We don't do cards like this all that often, but we do it enough to make people think about whether swapping out the fourth copy for another card is not sometimes the correct play. 

I also know from looking at this card that its creation might very well be to answer a developmental issue. Bile Blight, for example, is a very good answer to tokens, as all tokens made by the same card have the same name. Regardless, I am always happy to see cards like Bile Blight get printed in sets. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/VkUY48IGj5_EN.jpg) 

 

I'm guessing most players ask the same question when they see Charging Badger? What's the point of a 1/1 trampler? Are we making a joke? No, although on some level there is some humor implied. The reason this card exists in this set is that the *Theros* block is all about building up your creatures. This means that small creatures with abilities that scale well with power, abilities like trample, are stronger than they would normally be. 

That's why Charging Badger is in *Born of the Gods*. A larger question is, "Why do we even make cards like Charging Badger in the first place?" The answer is that in a game about exploration, it is good to have some cards that force you to explore other cards to figure out how to make the original card work. Trample doesn't mean anything on a 1-power creature, so it forces players to solve the problem. Not every player enjoys this kind of problem solving, but enough do that we make cards for them in every set. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/xmhmrwYxfi_EN.jpg) 

 

One of the things that often happens in design is that you are solving two different design problems when you discover that they intersect. Claim of Erebos and other cards like it in *Born of the Gods* is one such overlap. Here were the two problems at hand: First, we were trying to find new things for Auras to do. Most of the Auras in *Theros* were more combat-oriented but, as this block has a strong Aura theme, we wanted to find other things Auras could do. Second, we had a new mechanic called inspired that triggered when creatures untapped. Obviously, attacking was one way for creatures to get themselves tapped, but we were looking for some other ways for creatures to tap themselves as well. 

Our search found us at the intersection of this Venn Diagram. Auras that grafted on activated abilities that required a tap allowed players to use Auras in a way other than attacking and gave us another tool for creatures with inspired to use. Playtesting showed that it did a very good job for each problem, making it a single elegant solution.

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/tODyHDABmO_EN.jpg) 

 

A modal card is what we call any card that gives the players two or more options when played. Some modal cards have a specific effect but let the player choose the type of target, while other modal spells just do multiple things and let the player choose which one he or she wants. The trick when designing modal cards (well, two-mode modal cards—three+ modes get a little more leeway) is that the modes want to feel like they connect.

The first type of modal cards do that automatically because you're just choosing the type of target. The effect is always the same. The second type requires a little more care. Dawn to Dusk is an interesting modal card in that its two effects are very different. The connection in this case is not what it is doing, but to what. Both effects affect enchantments, one negatively destroying them and one positively getting them back from the graveyard. This card gets bonus aesthetic points for having the two effects mirror one another. One puts an enchantment into the graveyard while the other takes it out.

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/xbNjecKm8C_EN.jpg) 

 

This card was created during *Theros* design but it just wasn't able to find a home. When this happens, I always talk to the lead designer of the second set (remember that the second set's lead designer is always on the design team of the first set) and say, "I've got a card for you." Ken liked the card so he was happy to put it into his set. I told Ken if for some reason it got kicked out of his set that he needed to give it to Ethan, the lead designer of *Journey into Nyx*. 

The reason I am so insistent on getting cards like this into the block is twofold. First, I believe that you need a certain number of cards like this that just ooze flavor and really stand out when you first see them. Second, one of my jobs as head designer (as opposed to lead designer of the first set) is to watch design resources, and Eye Gouge is the perfect example of a card that shines in *Theros* block and is mostly unusable anywhere else. The card's mechanic has to be carried by its flavor and that flavor only works on *Theros*. Therefore, I work very hard to make sure that good cards that only have one home make it into the block where they fit. This is one of many things done to help preserve future design space. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/2Sin5OMLEz_EN.jpg) 

 

If you divide up the elements of a card, it is pretty clear which parts are under design and development's domain and which ones are under the creative team's. Design and development care about mana cost, rules text, and power/toughness. The creative team cares about name, art, and flavor text. The only major area of overlap falls on the card's type line, specifically with the creature subtypes. Minotaurs are a good example.

Design and development hadn't planned on a lot of tribal in *Theros* block, but we always have a little and it was clear what tribe players were most excited about—Minotaurs. I say it was clear because when we announced we were doing a Greek mythology–inspired block, players scrambled to get the card Didgeridoo from *Homelands*. 

 ![Didgeridoo](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Didgeridoo&options=) 

  

I like to say that when players show great interest in a bad card, pay attention. Didgeridoo has a low power level, yet many players have gone out of their way to get one. Why? Because there was this pent-up demand for Minotaur tribal. As far as I was concerned, that meant it was something we had to deliver with the block. 

There was one problem, though. What design and development wanted to make Minotaurs work mechanically fought with what the creative team wanted to have them match their flavor. The problem was power and toughness (which I guess is another overlap issue). Design and development needed Minotaurs to have a curve, meaning that they existed at every mana cost. Creative, though, didn't want the Minotaurs to get too small. During *Theros* design, they laid down what I call the "five rule of Minotaurs." The five rule said in order for Minotaurs to feel substantial enough, their combined power and toughness had to be at least be 5. 

The problem was that the Minotaur deck really wanted two-drops, and it's hard to make a two-drop 2/3 or 3/2. During *Born of the Gods*, the development team went to creative and asked nicely if we could find a way to push the "five rule" on a few cards. Felhide Brawler is one of the results of this conversation. The compromise was that there could be a few Minotaurs that were compromised in some way to flavorfully justify them being slightly smaller (and thus cheaper). And thus, *Born of the Gods* has the first *Theros* block two-drop Minotaur. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/YE2fRYjttn_EN.jpg) 

 

If you read my blog ([called Blogatog](http://markrosewater.tumblr.com/)) you know that there is an ongoing conversation about red's share of the color pie. Many suggestions have been made how to make it bigger. One of the ideas I liked was allowing red to stretch more into other colors' areas but only for a short duration. That, for example, is where the idea for Chandra, Pyromaster's second ability came from. 

Felhide Spiritbinder is messing in similar space. Normally, blue is the cloning color (although to be fair, red has dipped its toe into this over the years, with Kiki-Jiki, Mirror Breaker being one of the most high-profile cards), but we are toying around with letting red copy just for the turn—much like it gets to draw but has to cast the cards right away. If you're interested in where red is moving, keep your eye on this aspect. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/vDfoa3Y3AS_EN.jpg) 

 

One of the themes of today's article is how many things got designed in *Theros* design but then didn't end up in the file. Another such card was [King Midas](http://en.wikipedia.org/wiki/King_Midas). He is the man who was granted the ability by the gods to turn anything he touched into gold, only to realize the horrible deal he had struck. In *Theros*, we had a white creature representing King Midas (which obviously didn't make it all the way through to print), but Gild is representing the story through a different means. Instead of a creature card, Gild turns the gold-changing ability into a kill spell. Want to stop a bothersome creature? Well, just turn it into gold. You then choose to trade the valuable, but no longer useful, creature into a commodity. As **Magic**'s currency is mana, that is what you get. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/cm4wXsKaSn_EN.jpg) 

 

I often talk about which color is primary or secondary in an ability. What I talk less about is what effects are primary or secondary within a color. A primary ability is something that the color uses all the time, most often in every set. A primary white ability, for instance, would be enchantment removal. In every set (or maybe almost every set in case we missed it once), white has a card, usually at common, that destroys enchantments.

Regrowing enchantments (getting them from your graveyard back into your hand), though, is a secondary ability in white. What that means is white can do it, but it's not something we do every set or necessarily every block. It's something white has access to when we need it. What does that mean exactly? Let's use Griffin Dreamfinder as our example. *Theros* has an enchantment theme, which means that enchantments play a larger role than normal. To make sure the set has enough interaction with enchantments, the designers will look for all abilities that make use of enchantments, whether or not those abilities are primary or secondary (one could call things we do super infrequently tertiary). 

White was looking for enchantment-relevant things to do and regrowing enchantments is a secondary ability. Interestingly, the other time we use enchantment regrowing is in a set where the graveyard is very relevant.

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/bCVoeX47D8_EN.jpg) 

 

Sometimes the role of the second or third set is figuring out how to top the set(s) that came before. *Theros* had the following two cards: 

  

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Staunch-Hearted Warrior" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Staunch-Hearted%20Warrior&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Centaur Battlemaster" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Centaur%20Battlemaster&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Common Staunch-Hearted Warrior gave you two +1/+1 counters when targeted. Uncommon Centaur Battlemaster gave you three +1/+1 counters when targeted. How do you top that? Well, you could go to four or you could get a little creative. That's the choice made for the design of Hero of Leina Tower. 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/mp4Hig7bV3_EN.jpg) 

 

Several years ago, development had created a number of decks for *Duels of the Planeswalkers*. The problem was that two of them didn't make any sense for any of the Planeswalkers we had. [Brady Dommermuth](https://web.archive.org/web/20140205144527/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Brady%20Dommermuth), the then-creative director, suggested we make up a few new ones that matched the flavor of the decks in question and if they proved popular we could later find a home for them in sets. 

Kiora came about because there was a green-blue deck with a water theme. Did players like her (and Ral Zarek, the other Planeswalker made to fulfill this need)? Absolutely. So much so that we almost immediately got questions about when she and Ral were going to appear. 

Here was the problem. We planned to wait to see if they were going to be popular, so that meant no upcoming set had them in it. And we work years ahead of time. So getting Ral and Kiora into sets proved to be quite a task. We also made the decision not to shoehorn them in but to put them in sets where they made sense.

When we returned to Ravnica, it seemed like a perfect time for Ral Zarek. He was an Izzet mage from Ravnica so he fit perfectly. There was some talk of having Kiora fit into *Gatecrash*, as the Simic were there but her sensibility didn't match Simic at all. Once we knew we were doing a Greek world, though, we knew we'd found our answer. Greek mythology was all about the monsters of the sea, which would prove to be a great draw to get her to the plane. (Kiora is not from *Theros*.) 

All we had to do was to wait for years as players asked again and again for Kiora. The fact that we hadn't made a green-blue Planeswalker only made the desire stronger, so I am happy to finally have her come out in *Born of the Gods*. She has quickly become one of my favorite Planeswalkers. (My blog followers know I probably shouldn't have said that.) 

![](http://media.wizards.com/images/magic/tcg/products/bng/KDJ%29D%28jk2m2389/8vTAGZkqQ9_EN.jpg) 

 

Devotion is what's known as a scaling mechanic. (Development intern Adam Prosak [talked about this back in December](/en/articles/latestdevelopments/2013/12-06-developing-devotion).) When designing for devotion you are always on the lookout for effects that can scale how big they are. If you have one mana symbol of the relevant color you do one increment, if you have two you do two, and so on. Most of the time, that means you put it on effects that can increment as high as you can have mana symbols. Marshmist Titan, though, shows that there are a few other ways to use devotion. 

Marshmist Titan is different in a few ways. First, it is not generating an effect. The devotion is not used to make anything. Rather, it is used as a means to take something away—in this case, mana to cast it. Second, it is not a limitless effect. Once you have six black mana symbols on your permanents, the spell cannot get any better. This allows you to consider putting it into a deck other than a mono-black deck (not that it won't still work just fine in mono-black).

As a designer, it is cards like Marshmist Titan that fascinate me, because it shows how you can take things that seem like givens about a mechanic and still play around with them.

### More Stories to Tell

That's all the time I have for today. As I only got to M, you'll have to join me next time, when I complete my tales of *Born of the Gods* design. As always, I'm eager to hear your feedback on today's column. You can email me, respond in the thread to this column, or talk to me through my various social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and recently added [Instagram](http://instagram.com/mtgmaro#)). 

Join me next time when... well, I just said above.

Until then, may *Born of the Gods* cards make stories for all of you as well. 

  

* * *

  

### Drive to Work #90—The Stages of Design

The first podcast this week is me discussing the five stages that I believe **Magic** design has gone through in the last twenty years. 

### Drive to Work #91—Names

For my second podcast this week, Matt Cavotta had car trouble and needed a ride to work, so we chat all about the role of names on **Magic** cards. As we have both been in charge of names at one point, the two of us have a lot to say on the topic. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      &#10;      &#10;      <div id="magic1"> Multi </div>&#10;      &#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*   [**Episode 91**](https://media.ormos.uk/0b/a3/0ba3d1e3ef98a1d3c512aa98105ad5671ffc44575aff7405380372483db220e8.mp3) : *Names* (19.2 MB)
*   [**Episode 90**](https://media.ormos.uk/bb/09/bb09421bb2f61773d3ff6689d0ec54c407c3a3be8006b045b3334cd826859408.mp3) : *Stages of Design* (22.7 MB)
*   [**Episode 89**](https://media.ormos.uk/18/a1/18a1855ed81124ff0ebad2bc989ca61d1b12aae29cfc461210cbed1335304e74.mp3) : *Theros, Part 8* (29.9 MB)
*   [**Episode 88**](https://media.ormos.uk/d5/e7/d5e72f47e99f4fc90696136f862d767bda218023fed60f69f4c281f81bf1f500.mp3) : *Theros, Part 7* (15.9 MB)
*   [**Episode 87**](https://media.ormos.uk/b1/37/b13738ede50e7e4ce3790f56f4c2b19982b3a8306702458f2d1083b4b6f39c7e.mp3) : *Year 1995* (15.4 MB)  

*   [**Complete Drive To Work Podcast Archive**](/en/articles/makingmagic/undated/drive-to-work-podcast-archive)

  
  

* * *

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_Prerelease_Details_Static.png)](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments) [![](http://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_Prerelease_Minisite_Static.png)](https://web.archive.org/web/20140424103615/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/bornofthegods) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Mark Rosewater](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg "Mark Rosewater")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Mark Rosewater</b>&#10;        <br>&#10;        <a href="https://twitter.com/maro254">@maro254</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140127000000/http://www.wizards.com/company/emailtoauthor.asp?author=Mark%20Rosewater&amp;headline=[Born%20to%20be%20Compiled,%20Part%201]">Email Mark</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140415025705/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140410010616/https://www.wizards.com/magic/magazine/archive.aspx?tag=making%20magic&amp;description=making%20magic">Making Magic Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Working for **Magic** R&D since October, 1995, Mark Rosewater is currently the head designer. His hobbies include spending time with his family, talking about **Magic** on every known medium (including [a daily blog](http://markrosewater.tumblr.com/) and a [weekly podcast](https://itunes.apple.com/us/podcast/magic-gathering-drive-to-work/id580709168)), and writing about himself in the third person. 

 