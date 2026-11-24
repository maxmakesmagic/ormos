---
id: eq69tnk6
kind: article
lang: en
path: /en/articles/makingmagic/2012/11-26-designing-for-golgari
title: Designing for Golgari
published: '2012-11-26'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    lang_detected: en
    capture_id: 214775
    url: https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    captured_at: '2024-05-18 03:49:28+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    lang_detected: en
    capture_id: 214775
    url: https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    captured_at: '2024-05-18 03:49:28+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    lang_detected: en
    capture_id: 214775
    url: https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    captured_at: '2024-05-18 03:49:28+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    lang_detected: en
    capture_id: 214775
    url: https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
    captured_at: '2024-05-18 03:49:28+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: eq69tnk6
  url: https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
  page_key: magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:49:28+00'
  capture_id: 214775
  wayback_url: https://web.archive.org/web/20240518034928id_/https://magic.wizards.com/en/news/making-magic/designing-golgari-2012-11-26
- document_id: eq69tnk6
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/223
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/223
  lang: en
  template: aspx
  captured_at: '2014-02-16 21:46:01+00'
  capture_id: 650125
  wayback_url: https://web.archive.org/web/20140216214601id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/223
- document_id: eq69tnk6
  url: http://magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-20
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-20
  lang: en
  template: drupal
  captured_at: '2017-08-29 03:40:10+00'
  capture_id: 875416
  wayback_url: https://web.archive.org/web/20170829034010id_/http://magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-20
- document_id: eq69tnk6
  url: https://magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-26
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-26
  lang: en
  template: drupal
  captured_at: '2022-09-12 05:30:52+00'
  capture_id: 875441
  wayback_url: https://web.archive.org/web/20220912053052id_/https://magic.wizards.com/en/articles/archive/making-magic/designing-golgari-2012-11-26
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: eq69tnk6
  capture_id: 650125
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/223
  wayback_url: https://web.archive.org/web/20140216214601id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/223
  captured_at: '2014-02-16 21:46:01+00'
  template: aspx
  sha256: e4232643d59572bffed2de9ad4a9dab11a35d31920f36ae9d0a1fd83c8626fd7
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Golgari Guildgate
  - Korozda Guildmage
  - Revive
  - Disentomb
  - Vile Rebirth
  - Boneyard Wurm
  - Village Cannibals
  - Moldgraf Monstrosity
  - Cremate
  - Loaming Shaman
  - Shambling Shell
  - Reclaim
  - Slitherhead
  - Deadbridge Goliath
  - Forest
  - Terrus Wurm
  occurrences: 29
---
Welcome to Golgari Week. This is the fourth installment of the *Return to Ravnica* block guild theme weeks. (We've already done [Selesnya](/en/articles/makingmagic/2012/10-01-designing-for-selesnya), [Azorius](/en/articles/makingmagic/2012/10-29-designing-for-azorius), and [Izzet](/en/articles/makingmagic/2012/11-12-designing-for-izzet).) Ravnica block also had a cycle of ten guild theme weeks, but I used those to talk about the philosophy of all the two-color combinations. (You can [see those columns here](https://web.archive.org/web/20131105013418/http://www.wizards.com/magic/magazine/features.aspx?tag=color%20pie).) This time around, instead of talking color philosophy, I'm talking design. How exactly do we design cards that are black and green in general and Golgari specifically? 

For each of these articles, I'm answering the same four questions and then exploring how the two guild mechanics (the one from Ravnica block and the one from *Return to Ravnica* block) were created. Hopefully, as this is the fourth time out, we've got this whole thing down. 

![](https://i.ormos.uk/c2/83/c2837fd8d248f56c254a746f393b1b78d3b8e426b4f47e2d01ecd249e8489b0a.jpg) 

Golgari Guildgate | Art by [Eytan Zana](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22eytan%20zana%22])

### What's the Easiest Thing About This Color Pairing?

After green-white, black-green has the most overlap of any two colors. For example, they have not one but two creature keyword overlaps—deathtouch and regeneration. In general, the range of their creatures is similar. Green on average is larger than black but black definitely has access to larger creatures, especially at higher rarities.

The other giant overlap is that black and green are the two colors that have the most to do with the graveyard. There are a bunch of different areas of graveyard design (I'll talk about them in a moment) and black and green overlap in pretty much all of them.

In addition, black and green tend to have a set of abilities that interconnect well with one another. Green has the muscle to hit hard and black has the means to remove any threats that try to get in those creatures' way.

### What's the Hardest Thing About This Color Pairing?

I like to say that your greatest flaw is your greatest strength pushed too far. Green-black's synergy is so good that it tends to want to pull all the cards into a very similar space. This space, while flavorful, isn't all that large mechanically. For example, in a normal set, black and green might each have one card that cares about the graveyard.

Get black and green together and they start to warp the environment because they push the designer to up the amount of graveyard interaction. Obviously, the Golgari have just embraced this and run with it, but it does mean that black-green tends to have a narrower band of things it can do than many of the other two-color combinations.

The overlap also causes problems because a lot of time, when you make a black-green card, you discover you've made a card that one of the two colors could do alone. Obviously, you can have a little of overlapping mechanics on gold cards (what I call "Venn Diagram cards" in [my article on designing gold card](/en/articles/makingmagic/2005/11-14-midas-touch)) but it's something we have to keep at a low volume (especially because it eats into hybrid design space).

![](https://i.ormos.uk/47/3a/473adb25cbc98a5e6217daa3f5fa2721a1461cfac852c47948a670869fe7d525.jpg) 

Korozda Guildmage | Art by [Ryan Pancoast](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22ryan%20pancoast%22])

### What's the Mechanical Heart of This Color Pair?

This one's pretty easy. Black-green loves the graveyard. Designwise, it's a very robust vein of design. Note that there is a difference between how many cards can be designed for a mechanic and how many make sense within any one set. Graveyard design is deep but narrow, meaning that unless you have a set with a graveyard focus, it's hard to put a lot of these cards in a set together.

Here's the different areas you can play around with in the graveyard:

> ### Ability to Get Things Back from the Graveyard
> 
> This is the simple ability to play with dead things. In other words, this is the ability to take things that have gone to the graveyard and bring them back. When you talk about returning cards from the graveyard directly to the hand, this is green's domain. It has cards like Revive (from **Magic** 2013) that let you return any card type you wish (Revive limits itself to green cards but green's ability here doesn't have to self-limit in the color). Black's niche in this area is getting back creature cards with spells like Disentomb (also from **Magic** 2013). 
> 
> <table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="276223" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=276223&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="259701" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=259701&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>
> 
>   
> 
> When you talk about bringing cards from the graveyard back to the battlefield, you get into black's domain. Note that black only tends to bring back creatures. This is flavored as reanimation and plays into black's fondness for death. Also note that black, and green to a lesser extent, has the ability on some creatures for them to get themselves back onto the battlefield.
> 
> When you talk about bringing things back to the library, this is green's domain. Sometimes these cards go to the top of the library but more often are shuffled directly into the library. Black also has some ability to put creature cards from the graveyard on top of the library. This is more of a Disentomb tweak than what green is up to. 
> 
> ### Graveyard as a Resource
> 
> Part of the strategy of **Magic** is learning how to maximize the resources you have available in order to win. The graveyard is one such resource. Black tends to use this resource by eating it up to fuel whatever it's up to. Vile Rebirth from **Magic** 2013 is a good example of this. Green, in contrast, tends to like looking at what is in the graveyard and drawing strength from that. A good example of this would be Boneyard Wurm from *Innistrad*. The contrast between these two different styles is that black is faster to use the graveyard but depletes itself while green tends to grow in strength over time. 
> 
> <table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Vile Rebirth" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Vile%20Rebirth&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="220050" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=220050&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>
> 
>   
> 
> ### Caring About Things Going to the Graveyard
> 
> There are two basic ways to care about things dying. First, you can care about when other things die. Black is king of this area, as black enjoys watching things die (often having a hand in the act). Black cards will often have effects that trigger when other things die. Village Cannibals from *Innistrad* is a good example of this kind of effect. Note the mechanic morbid in *Innistrad* block, which cared about something having died that turn, rested mostly in black and green. The second way to care about death is what is known as a death trigger. A death trigger goes on a creature and triggers when that creature dies. An example is Moldgraf Monstrosity from *Innistrad*. While all the colors can get death triggers, green and (especially) black get more of them. 
> 
> <table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Village Cannibals" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Village%20Cannibals&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Moldgraf Monstrosity" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Moldgraf%20Monstrosity&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>
> 
>   
> 
> ### Ability to Remove Things from the Graveyard
> 
> Another way to interact with the graveyard is to remove things from it—usually your opponent's cards (unless you are using it as a cost, as seen above). Black is the best at removing specific cards from a graveyard. A good example of this is Cremate from *Return to Ravnica*. Green tends to remove cards from the graveyard by shuffling them into their owner's library. Loaming Shaman from *Dissension* is an example of this. 
> 
> <table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Cremate" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Cremate&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Loaming Shaman" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Loaming%20Shaman&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>
> 
>   
> 
> ### Things Active in the Graveyard
> 
> The last category is one we tend to only do in the expansions. These are cards that are usable while in your graveyard. Most often, this is an activated ability, but sometimes it's triggered. The reason we are careful with how often we do these cards is because they require players to pay attention to an area they normally do not have to. In expansions, we can make the graveyard a theme and thus help train players to pay attention to it, but we tend to not do that if there is not at least a minor graveyard theme. While every color can have these types of cards they tend to show up more in black and green. Both of the Golgari mechanics play in this space.

### What's the Focus of This Color Pair?

As I've explained in previous articles, the mechanical heart is about what the color pair is mechanically built around. The focus is about how the colors win. What is their strategy? For black-green, the route to victory is through exhausting the resources of the opponent. You win because you keep coming at your opponent until he or she no longer has any defense. If you like, you can think of this like a horde of zombies. Early on, they're not hard to beat, but they just keep coming until they eventually overwhelm you.

The key to this route to victory is that black-green is good at not running out of resources. How? By utilizing the graveyard to keep getting back the resources. Sure, the opponent can kill your creatures, but black-green can reanimate them. The opponent can stop your spells but black-green can regrow them. No matter what answers your opponent has, black-green keeps bringing back threats. Thematically, this plays into black-green connecting life and death. The Golgari are the ultimate recyclers. Death is not an end but just a new beginning.

What this means for design is that black-green want to find different ways to overwhelm. One popular way to do this is also through card advantage. Black and green are both secondary at card drawing, both are decent at token creation (although green is a bit stronger in this department), and both are good at destruction—although what they are capable of destroying varies between the colors (black is good at destroying creatures and land while green is good at destroying artifacts, enchantments, and land).

Black-green is one of the slower of the two-color combinations, but once it gains inertia, watch out.

### Dredge

Every guild set I've ever designed seemed to have one guild that was a pain in the neck. Interestingly, it's never been the same guild. For the original Ravnica, the guild that caused us the most trouble was Golgari. The interesting thing is that we knew out of the gate the parameters for the Golgari mechanic, but finding the right one took a long time and a lot of tries.

![](https://i.ormos.uk/02/95/029591419febb347c51bded5322883e7ad76b91d46ef5493387aaea026376fac.jpg) 

Shambling Shell | Art by [Joel Thomas](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22joel%20thomas%22])

We knew two things when we started looking: (1) the mechanic had to involve the graveyard (see mechanical heart above), and (2) the mechanic had to be recursive in some way; you were recycling (see focus above). With these two clear-cut goals in mind, we started making mechanics. For those who are unaware (and welcome to the column), I'm a Johnny. Of the four guilds in Ravnica, Golgari was the Johnniest, so it pulled my focus. As such, I made it my mission to find a Golgari mechanic.

The details are all a blur but here's what I remember happening again and again:

1.  I design a new Golgari mechanic that fits the criteria above.
2.  I show it to the team (Tyler Bielman, [Mike Elliott](https://web.archive.org/web/20130609055227/http://www.wizards.com/magic/magazine/archive.aspx?author=mike%20elliott), [Aaron Forsythe](https://web.archive.org/web/20140110115401/http://www.wizards.com/magic/magazine/archive.aspx?author=aaron%20forsythe), [Richard Garfield](https://web.archive.org/web/20140125031340/http://www.wizards.com/magic/magazine/archive.aspx?author=richard%20garfield), and myself) and the team gives the mechanic a thumbs up.
3.  We playtest it.
4.  The graveyard-focused recursive mechanic is broken and smashes the playtest.
5.  I go back to the drawing board.

How many iterations did this go through? About forty. Note that not every mechanic was broken. Some would be boring or confusing or not Golgari enough. Forty mechanics? Am I exaggerating for comic effect? No. We went through a lot of mechanics for Golgari. A lot. It was, as I said above, a pain in the neck. During this time we were designing a lot of individual cards and many of those were working well, so it wasn't that we didn't have Golgari moving along; we just didn't have our keyword mechanic.

![](https://i.ormos.uk/71/27/7127cbfb20ad9e60555964c68eb3e5e92a6bdbacafaebb9c57dd2c7af5eb46cc.jpg) *Occam's Razor: Not for Shaving.* 

One day I got fed up, so I turned to [Occam's Razor](http://en.wikipedia.org/wiki/occam%27s_razor). Occam's Razor is a principle that basically says the simplest form of something is usually the best answer. So, I sat down and thought. I wanted a mechanic that worked in the graveyard and had a recursive component. What was the absolute simplest version of that concept?

What if I could just play the card out of the graveyard? No, that was flashback.

What if I could just draw the card from the graveyard? Interesting, I thought. What would that entail? It would have to be at a time I normally drew a card. Also, drawing two cards seemed too powerful. What if the mechanic allowed me to draw it instead of a card from the top of my library any time I could draw a card? Perfect!

I named my mechanic reclaim. The idea behind reclaim was that the cards were overcosted but the ability to get them back might be good situationally. For example, imagine a ![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 3/3. As green can get 3/3 for as little as three mana, six mana is overpaying by quite a bit. But late game, at times, especially in Limited, you would be overjoyed to be able to draw a 3/3 for six mana. Reclaim in that form is what I handed off in the Ravnica design handoff to development. 

Development worried that if they costed reclaim the way they had to, to keep it from being broken, it was going to appear very sucky. Also, they wanted a cost associated with getting the card back that guaranteed players weren't just going to keep getting back the same card turn after turn for the entire game. The novel idea Brian and his team (Aaron Forsythe, [Mark Gottlieb](https://web.archive.org/web/20140110115611/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20gottlieb), [Matt Place](https://web.archive.org/web/20130520094714/http://www.wizards.com/magic/magazine/archive.aspx?author=matt%20place), [Paul Sottosanti](https://web.archive.org/web/20130520104034/http://www.wizards.com/magic/magazine/archive.aspx?author=paul%20sottosanti), and [Henry Stern](https://web.archive.org/web/20130520104049/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater%20and%20henry%20stern)) had was to use self-milling as an additional cost. This would limit how many times players could get back the card and would also create a cute synergy where paying the mill cost could help you get more dredge cards. (Obviously, at some point reclaim got renamed as dredge.) 

I thought the redesign was clever and gave it my thumbs up. I trusted Brian's instincts on what was dangerous to print. In the end, the "cute" synergy turned out to be a bit better than anyone expected and dredge became a powerhouse mechanic that has shown up in just about every format in which it's legal. I have a soft spot for dredge but I understand that it's one of our more broken mechanics.

I will say this, though: it's awfully Golgari.

![](https://i.ormos.uk/4f/68/4f68d2107ca4ce8ab027489b0be573a737e09db64387627463a6e3ebe09b9cd8.jpg) 

Slitherhead | Art by [Greg Staples](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22greg%20staples%22])

### Scavenge

Ken talked about scavenge's design in a feature article, so if you'd like another take on the story, feel free to [check it out](/en/articles/feature/2012/09-03-on-the-origin-of-scavenge-and-overload). I'll be telling it from my perspective. In one of the early design meetings (the team consisted of lead [Ken Nagle](https://web.archive.org/web/20130702035545/https://www.wizards.com/magic/magazine/archive.aspx?author=kenneth%20nagle), [Zac Hill](https://web.archive.org/web/20130921121442/http://www.wizards.com/magic/magazine/archive.aspx?author=zac%20hill), [Alexis Janson](https://web.archive.org/web/20130520111221/http://www.wizards.com/magic/magazine/archive.aspx?author=alexis%20janson), [Ken Troop](https://web.archive.org/web/20130520111830/http://www.wizards.com/magic/magazine/archive.aspx?author=ken%20troop), and myself), Ken (Nagle) said it was time to talk about Golgari. Once again, we were looking for a graveyard mechanic that had some recursive element and would allow you to ultimately overwhelm your opponent. Ken informed us he had an idea for the Golgari mechanic. "What if," he said, "you could eat the creatures once they died?" 

For those unaware, during *Shards of Alara* block, Ken designed a mechanic called devour. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="186329" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=186329&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="174975" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;MultiverseId=174975&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

The devour mechanic was for the shard of Jund, the red-centered world that also had black and green. In the vicious eat-or-be-eaten world of Jund, Ken liked the idea that the bigger creatures liked to eat the smaller creatures. I'm not sure if the devour mechanic influenced his new Golgari mechanic but I like to think it did. Ken called his mechanic digestible.

In the original version of digestible, the card could be eaten by an attacking creature to temporarily boost its power and toughness and gain the eaten card's abilities (all of the boosts and abilities matched those of the creature digested and all only lasted until end of turn). That version proved both unimpressive and lacking in flavor. Why was the mechanic limited to an attacking creature? Creatures in Ravnica liked to eat on the go?

![](https://i.ormos.uk/4d/23/4d230c2dfa644274892d4bc9c42cce3d46086db39270dd501f64a4b63dd27473.jpg) 

  

The mechanic went through a few iterations but the next important one had two key shifts. First, the boost was now +1/+1 counters rather than temporary bonuses until the end of the turn. Second, instead of limiting the use to an attacking creature, the ability now could be used any time a sorcery could be cast.

Let me quickly answer a question I've received a few times on my blog. Why did we choose to limit scavenge to sorcery speed? Basically, any time we limit a mechanic to sorcery speed I get the same question. Doesn't more choice lead to a better game? The answer is no. The idea that options improve a game actually flies against the entire concept of how games are designed.

I talk a lot about how a designer's job isn't to make it easier for the player, but rather harder. Games thrive when the players have to figure out how to accomplish the goal at hand. Besides breeding creativity, restrictions force the players to have to make hard decisions. For example, if I could activate scavenge at any time, the correct answer is always to wait until the last moment when it's necessary. By restricting the mechanic to sorcery speed, you now force players to have to make decisions rather than waiting to see what happens.

The other issue we had to deal with for scavenge is that it's what I call a false negative mechanic. What I mean is that it's more powerful than it looks, so when development costs it correctly, it seems weak at first glance. For example, here's the card we first previewed scavenge with, Deadbridge Goliath: 

 ![Deadbridge Goliath](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Deadbridge%20Goliath&options=) 

  

The first reaction to the card was "Six mana to use the ability. Worthless!" Let's take a step back. For starters, the card is a ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 5/5. If this was a vanilla creature, it's a shoo-in in any Limited deck with enough Forests to handle the double green in the mana cost. So what's been added? Would you play this card in Limited? 

![](https://i.ormos.uk/d8/a9/d8a9e5e1ca089e8f25e35f7fbfb2ac68e75323b9305dce43c9973ac1ffec39c7.jpg) 

  

Maybe. Now how about if it magically appeared for free when you played a ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 5/5? 

Because **Magic** is at its heart a game about discovery, we don't mind doing a few false negative mechanics. It's fun for players to learn that some things in the game are better than they appear at first glance. The trick is to make sure the set is balanced with other mechanics that do pop when the audience first sees them. 

All in all, I felt dredge and scavenge both did a nice job of capturing the essence of the Golgari.

### Grave Concerns

That's all I have to say about the Golgari. As always, I'm curious to hear what you all have to say about the black-green guild and our take on it. Feel free to drop me an email, respond in the thread, or contact me on any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)).

Join me next week when I look back at looking forward.

Until then, may you find new uses for old things.

![](https://i.ormos.uk/9f/b2/9fb24b6cbc78f9c8431222bc68fb3b916a45215e47b5485ad3d9a5123e4a774d.jpg) 

Terrus Wurm | Art by [Cliff Childs](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22cliff%20childs%22])

### Drive to Work

I've written two different articles about the player psychographics of Timmy, Johnny, and Spike ([here](/en/articles/makingmagic/2002/03-11-timmy-johnny-and-spike-2) and [here](/en/articles/makingmagic/2006/03-20-timmy-johnny-and-spike-revisited-3)). Today, I finally talk about them. I dig in deep and explain them in some ways I've never done before. If you are at all interested in the player psychographics, I urge you to give the podcast a listen. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      &#10;      &#10;      <div id="magic1"> Multi </div>&#10;      &#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*   [**Episode 9**](https://media.ormos.uk/50/a7/50a70e9a2441972702ff71b71e1359203e4364d400f881e3d71e876d2dd5937a.m4a) : *Psychographics* (14.0 MB)

*   [**Episode 8**](https://media.ormos.uk/9f/89/9f89573d8de26e8c2d51e9a4683905ec46baa137276666222bb162307a919139.m4a) : *Cycling* (14.0 MB)

*   [**Episode 7**](https://media.ormos.uk/78/63/78630763314671f4db3ed309eefa1b3556ae6075a6f065412ece61ef69f5613d.m4a) : *Alliances* (14.0 MB)

*   [**Episode 6**](https://media.ormos.uk/8f/d8/8fd8ad0eb46eda1c3a460ff80556719b22fa0edfb78f56956f1b7f47916d82f7.m4a) : *Gold Cards* (16.9 MB)

*   [**Episode 5**](https://media.ormos.uk/07/2e/072e5c111882c73d3ff718837a4e86fb2a8faac4ae8496a16c2a6cad5a5d313d.m4a) : *Ravnica* (12.9 MB)

*   [**Episode 4**](https://media.ormos.uk/3e/25/3e25a9da6c30b60fbe51c205522343261d96fd08b744e21afcc21c0c3976710e.m4a) : *Invasion* (14.2 MB)

*   [**Episode 3**](https://media.ormos.uk/a7/2e/a72e03e752bad94f2452c36961a6f084834039cdbd9d852c5a1545be042fad70.m4a) : *Planeswalkers* (15.0 MB)

*   [**Episode 2**](https://media.ormos.uk/37/fb/37fb50b67b14247a6839529acd6801fea440183a9cd8cf6dd7af2f48c920c413.m4a) : *Zendikar* (15.3 MB)

*   [**Episode 1**](http://media.wizards.com/podcasts/magic/drivetoworkep1.m4a) : *Tempest* (13.8 MB)

  

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

![](http://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_FNM_Top.jpg) 

[![](http://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_FNM_Button01_Static.jpg)](https://web.archive.org/web/20140217130302/http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/returntoravnica/productinfo) [![](http://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_FNM_Button02_Static.jpg)](https://web.archive.org/web/20121126000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&set=[%22Return%20to%20Ravnica%22])