---
id: 0qt7st8p
kind: article
lang: en
path: /en/articles/latestdevelopments/2016/03-04-balancing-the-top-commons
title: Balancing the Top Commons
published: '2016-03-04'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    lang_detected: en
    capture_id: 718241
    url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    captured_at: '2022-08-15 22:18:26+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    lang_detected: en
    capture_id: 718241
    url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    captured_at: '2022-08-15 22:18:26+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    lang_detected: en
    capture_id: 718241
    url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    captured_at: '2022-08-15 22:18:26+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    lang_detected: en
    capture_id: 718241
    url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
    captured_at: '2022-08-15 22:18:26+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 0qt7st8p
  url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
  lang: en
  template: drupal
  captured_at: '2022-08-15 22:18:26+00'
  capture_id: 718241
  wayback_url: https://web.archive.org/web/20220815221826id_/https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
- document_id: 0qt7st8p
  url: http://magic.wizards.com/en/node/991301
  page_key: magic.wizards.com/en/node/991301
  lang: en
  template: drupal
  captured_at: '2016-06-12 07:40:39+00'
  capture_id: 2532719
  wayback_url: https://web.archive.org/web/20160612074039id_/http://magic.wizards.com/en/node/991301
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0qt7st8p
  capture_id: 718241
  url: https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
  wayback_url: https://web.archive.org/web/20220815221826id_/https://magic.wizards.com/en/articles/archive/latest-developments/balancing-top-commons-2016-03-04
  captured_at: '2022-08-15 22:18:26+00'
  template: drupal
  sha256: af172c5503077043048df04a895e7fbb9c5f8fa7bcd8cbf80ee2584d5f5933ec
render_recovery: []
---
Commons are the basic building blocks of any Limited format, and since they represent the majority of both the cards you open and the cards that make up your deck, we want them to be pretty even as a whole. While individual cards will differ a lot, the hope is that the colors will be close enough that you can make a deck with any color combination and have the opportunity to get cards of a similar power level to everyone else. Ideally in a draft, people should be rewarded for figuring out which colors are open, rather than just forcing the strongest color and hoping to muscle their neighbors out of them. On this week's Latest Developments, I'm going to talk about how we try to power balance our colors, specifically the top commons, and what that does as a whole to make the Limited experience better.

# A History of Balance

In the old-old days, we used a scale of 0.0 (never play in your sealed deck) to 5.0 (always play in your sealed deck) to rate sets. We tried to make sure each color balanced out when you added up all of their numbers. Taken from one of Randy Buehler's old articles, here was how the scale worked:

***5.0****: I will always play this card. Period.*

***4.5****: I will almost always play this card, regardless of what else I get.*

***4.0****: I will strongly consider playing this as the only card of its color.*

***3.5****: I feel a strong pull into this card's color.*

***3.0****: This card makes me want to play this color. (Given that I'm playing that color, I will play this card 100% of the time.)*

***2.5****: Several cards of this power level start to pull me into this color. If playing that color, I essentially always play these. (Given that I'm playing that color, I will play this card 90% of the time.)*

***2.0****: If I'm playing this color, I usually play these. (70%)*

***1.5****: This card will make the cut into the main deck about half the time I play this color. (50%)*

***1.0****: I feel bad when this card is in my main deck. (30%)*

***0.5****: There are situations where I might sideboard this into my deck, but I'll never start it. (10%)*

***0.0****: I will never put this card into my deck (main deck or after sideboarding). (0%)*

For reference, this is how a few older cards stack up on this scale:

*   [Masticore](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore): 5.0—There are very few 5s in the history of the game.
*   [Fireball](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball): 4.3
*   [Agonizing Demise](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agonizing+Demise): 3.9—This is about as good as it should get at common. We no longer print cards that score above 4 at common.
*   [Overrun](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun): 3.5—This would be higher if it weren't triple green, of course.
*   [Mystic Zealot](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Zealot): 2.7
*   [Barbarian Lunatic](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barbarian+Lunatic): 1.8—Though some players I respect think this card is worse than I do, and would score it lower.
*   [Dematerialize](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dematerialize): 1.2
*   [Circle of Protection: Green](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Circle+of+Protection%3A+Green): 0.6
*   [Saprazzan Raider](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saprazzan+Raider): 0.0

There are things this system gets right—it makes sure that if one color has a lot of strong bombs, it doesn't get those for free. That color will have to pay a cost somewhere else. Also, in the time before *Magic Online*, it was very possible that Sealed was the main form of Limited that people played. Ultimately, the goal of this scale is to look at a set in Sealed Deck and ensure that the colors are pretty even, but it has some flaws. The first one is the major quirk that colorless cards and artifacts tend to be very high on the list ([Masticore](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore)'s 5.0 is matched by [Evolving Wilds](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds)). The second one is that, because it is Sealed Deck, it takes for granted the fact that you have all the cards in front of you at one time, not only a fraction of what you will see in one pack. That means that it is a lot more forgiving to colors that are uneven, since it doesn't matter if you open that [Control Magic](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Control+Magic) in pack one or three, you always get to play it if you want to.

I believe the biggest issue with this scale, though, is that most commons ended up in the 0.5 to 2.5 range, while the practical difference between, say, a 0.0 (totally unplayable) and a 1.0 (basically never play) was small on a card-by-card basis but large when looking at the set as a whole. Imagine two colors. One color's top-level commons were in the 3.0 range, but its worse commons were in the 0.0 range. The other color's total was very similar, but its top commons were in the 2.0 range and their bottoms were more like 1.0. It's pretty easy to get enough cards that you won't need to play the 1.0s, so the first color ends up just being stronger.

![](http://media.wizards.com/2016/images/daily/cardart_ORI_Separatist-Voidmage.jpg)

[Separatist Voidmage](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Separatist+Voidmage) | Art by [Jason Rainville](https://web.archive.org/web/20160304000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Jason+Rainville%22%5d)

Now, this system was much better than no rankings at all, but it left a lot to be desired for actually balancing things out. If you look at old sets, they were frequently out of balance. While the nature of Draft helps to even things out, we often ended up with one color being almost unplayable and another being stronger than the rest.

# The New Pointing

Several years ago, Erik Lauer came up with "Quickpointing," which cares less about granular details like if a card is a 2.3 or a 2.4 and instead just puts things into buckets. Imagine taking each whole number, and sticking a bunch of cards into the 2.0 bucket, etc. Each color gets the same number of cards in each bucket. While things are not always mathematically precise, they are precise in the way you are interacting with them. We want the power of the commons to be somewhat flat, and to let things like synergy push one card over another. This system also uses Draft to evaluate the cards, which means you don't get weird things like [Evolving Wilds](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds) being better than any other card in the set.

In an ideal world, the best common for each color isn't removal—but that is hard to get to, and often leads to color imbalance or removal that is too weak as a whole for a fun environment. It's nice to have, but doesn't happen 100% of the time. What we do try to do is make sure that in each set, the colors feel different from each other and line up with their traditional strengths and weaknesses. Each color is good at certain things, and if those things don't come through at common, then we are going to have problems. For example, green should probably have the best fatty at common—ideally, somewhere in its top fifteen. It doesn't need to be the best creature, but at least the four- or five-drop with the best stats and ability to run over the opponent if you ramp into it. Blue should have the best common flyer. Black should have the best "big" removal spell, and red should have the best "small" removal spell. If the best flyer in a set isn't blue, then we try to either weaken it or bump up the blue card to the point where it becomes the best. These small tweaks go a long way toward ensuring that no matter what the set, the colors feel like what you would expect.

Once we have put things in buckets, we take the top commons in each color and stack rank them. The goal here is to make sure that you always have interesting choices at common. Let's say that the top five commons in a set were all black or red (like in original *Zendikar*). Chance are, if you don't first-pick a rare, you will end up in black or red. And then you get to fight everyone for those cards, until they dry up and you need to pick a second color. With the way we put sets together, you will only end up taking a common first pick somewhere between a third and half of the time. So having similar power level in commons means that when you get to the point in a pack where you need to start taking commons, you have interesting decisions.

For example, below was what we listed as the top commons in *Magic Origins*:

1.   [Suppression Bonds](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Suppression+Bonds)
2.   [Claustrophobia](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Claustrophobia)
3.   [Fiery Impulse](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Impulse)
4.   [Reave Soul](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reave+Soul)
5.   [Wild Instincts](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Instincts)
6.   [Unholy Hunger](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Hunger)
7.   [Ghirapur Gearcrafter](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghirapur+Gearcrafter)
8.   [Topan Freeblade](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Topan+Freeblade)
9.   [Leaf Gilder](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaf+Gilder)
10.  [Separatist Voidmage](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Separatist+Voidmage)
11.  [Rhox Maulers](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Maulers)
12.  [Boggart Brute](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Brute)
13.  [Scrapskin Drake](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrapskin+Drake)
14.  [Stalwart Aven](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stalwart+Aven)
15.  [Read the Bones](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Read+the+Bones)

Things are never going to be perfectly balanced, but we strive for something like this—if you take the top three commons of each color and stack rank them, then add up their positions, you want all the colors to have about the same number. For example:

<table><tbody><tr><td> </td>&#10;			<td>White</td>&#10;			<td>Blue</td>&#10;			<td>Black</td>&#10;			<td>Red</td>&#10;			<td>Green</td>&#10;		</tr><tr><td> </td>&#10;			<td>&#10;			<p>1 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Suppression+Bonds">Suppression Bonds</a></p>&#10;			</td>&#10;			<td>&#10;			<p>2 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Claustrophobia">Claustrophobia</a></p>&#10;			</td>&#10;			<td>&#10;			<p>4 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reave+Soul">Reave Soul</a></p>&#10;			</td>&#10;			<td>&#10;			<p>3 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Impulse">Fiery Impulse</a></p>&#10;			</td>&#10;			<td>&#10;			<p>5 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Instincts">Wild Instincts</a></p>&#10;			</td>&#10;		</tr><tr><td> </td>&#10;			<td>&#10;			<p>8 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Topan+Freeblade">Topan Freeblade</a></p>&#10;			</td>&#10;			<td>&#10;			<p>10 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Separatist+Voidmage">Separatist Voidmage</a></p>&#10;			</td>&#10;			<td>&#10;			<p>6 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Hunger">Unholy Hunger</a></p>&#10;			</td>&#10;			<td>&#10;			<p>7 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghirapur+Gearcrafter">Ghirapur Gearcrafter</a></p>&#10;			</td>&#10;			<td>&#10;			<p>9 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaf+Gilder">Leaf Gilder</a></p>&#10;			</td>&#10;		</tr><tr><td> </td>&#10;			<td>&#10;			<p>14 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stalwart+Aven">Stalwart Aven</a></p>&#10;			</td>&#10;			<td>&#10;			<p>13 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrapskin+Drake">Scrapskin Drake</a></p>&#10;			</td>&#10;			<td>&#10;			<p>15 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Read+the+Bones">Read the Bones</a></p>&#10;			</td>&#10;			<td>&#10;			<p>12 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Brute">Boggart Brute</a></p>&#10;			</td>&#10;			<td>&#10;			<p>11 <a href="https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Maulers">Rhox Maulers</a></p>&#10;			</td>&#10;		</tr><tr><td>&#10;			<p>Total</p>&#10;			</td>&#10;			<td>&#10;			<p>23</p>&#10;			</td>&#10;			<td>&#10;			<p>25</p>&#10;			</td>&#10;			<td>&#10;			<p>25</p>&#10;			</td>&#10;			<td>&#10;			<p>22</p>&#10;			</td>&#10;			<td>&#10;			<p>25</p>&#10;			</td>&#10;		</tr></tbody></table>

Now, these were largely our best guesses from a couple dozen playtests through all of development, and through a lot of changes. We knew we were not going to get everything right. Looking at this list now, I think it is pretty accurate as a whole, but I think we overvalued some of the more expensive removal and undervalued [Topan Freeblade](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Topan+Freeblade), among others. *Origins*, being mostly a core set, was a little simpler to evaluate than your average large set, since the synergistic power was lower.

Of course, this was the list from the end of development, not earlier in the process. Usually, after we do a pass of trying to balance the set out and putting cards in buckets, we have to take all of the top commons and make sure there is some room between them. In earlier versions of the set, [Ghirapur Gearcrafter](https://web.archive.org/web/20160304000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghirapur+Gearcrafter) was a 3R 3/2 that made a 1/1 Thopter. While we still had that in our top fifteen, it was lower down. Similarly, other creatures appeared when they were stronger, and we moved cards around to balance things out.

Ultimately, the goal of making all of these changes at common is to ensure we don't end up with colors that people only go into if they open up a bomb rare, or worse yet, still avoid that color even then. We make a lot of sets, and since we are going to have a non-zero margin of error, we are going to get things wrong from time to time. This system helps us to minimize that margin, so ideally, even if one color is too strong and other too weak, the sum of the parts and the nature of Draft allows them to even out pretty well.

That's it for this week. Join me next week when I talk about how development interacts with other teams within both *Magic* R&D and the brand as a whole.

Until next time,

Sam ([@samstod](http://twitter.com/samstod))