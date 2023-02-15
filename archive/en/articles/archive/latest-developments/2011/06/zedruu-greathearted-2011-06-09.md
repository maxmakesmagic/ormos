
---
[Link to Wayback Machine](https://web.archive.org/web/20220701171015/https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09)

[_metadata_:author]:- "Mark Globus"
[_metadata_:description]:- "Hello! I am filling in for Tom LaPille while he cavorts around Japan, spellslinging at Pro Tour Nagoya and doing some sightseeing. Today, I'll be sharing with you our experiences with developing Magic: The Gathering Commander.Let me start off by introducing my crack development team.Mark GlobusI joined Wizards of the Coast about four and half years ago at the conclusion of the"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "192386"
[_metadata_:path_date]:- "2011-06-09"
[_metadata_:publish_date]:- "2011-06-10"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Zedruu the Greathearted"
[_metadata_:wayback_capture_timestamp]:- "2022-07-01 17:10:15"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220701171015id_/https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09"
---


Zedruu the Greathearted
=======================



 Posted in **Latest Developments**
 on June 10, 2011 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Mark Globus











Hello! I am filling in for Tom LaPille while he cavorts around Japan, spellslinging at Pro Tour Nagoya and doing some sightseeing. Today, I'll be sharing with you our experiences with developing ***Magic: The Gathering** Commander*.

Let me start off by introducing my crack development team.

**Mark Globus**

![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_markglobus.jpg)I joined Wizards of the Coast about four and half years ago at the conclusion of the original [Great Designer Search](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/designersearch/home), when I tied for fourth. I bounced around digital for a couple of years doing everything from crushing bugs on **Magic Online** to being the lead technical producer for [**Dungeons amp; Dragons** Insider](http://archive.wizards.com/dnd/Tools.aspx). Then, two and half years ago, I joined **Magic** Ramp;D as the Senior Producer. What's that? Well, I make sure that everything is running smoothly within **Magic** Ramp;D. I get new products off the ground and clear roadblocks from projects in flight. Occasionally, I jump on a design or development team as well, including ***Magic** 2011*, *Worldwake*, and *Scars of Mirrodin* design and *Zendikar*, *Rise of the Eldrazi*, and "Roll" development. This was my first development lead, and you'll see the fruits of my first design lead soon: ***Magic** 2012*.

**Peter Knudson**

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_PeterKnudson.jpg)Peter has interned for us in **Magic** Ramp;D twice, and on this second stint I asked him to be a part of this development team. He was a great addition, bringing us his enthusiasm, passion, and strong work ethic. "Political Puppets" was the deck in the roughest shape coming out of design, and I had Peter spearhead our efforts in making this a fun, exciting deck. Peter was unable to join us in Ramp;D this summer, but I look forward to having the opportunity to work with him again in the future.

**Erik Lauer**

![](https://web.archive.org/web/20160113135054im_/http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)Erik's assistance on Commander development was invaluable, and I couldn't have gotten through this without his experience backing me up. He is the most tenured member of the Magic Development team and I greatly appreciated the perspective that his experience brought. Erik was my strong second on the team and I found his counsel to be wise. What was his number one piece of advice? Playtest, playtest, playtest.

**Ryan Miller**

![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_ryanmiller.jpg)Ryan is an awesome designer who focuses more on non-**Magic** games here at Wizards. He's been on quite a tear lately with them, as he has led the design for [REDACTED] and came up with the idea for [REDACTED]. Hmmm... that wasn't fair! Here—how about this? Ryan recently took on the mantle as lead designer for **Duel Masters**, our Japanese TCG. Congratulations, Ryan! Occasionally, we get to borrow him for **Magic** projects as well and he was our representative on the development team from Ken Nagle's design team. His insights into the design vision helped us stay on track and kept us focused on keeping this product fun and not just "interesting."

**Lee Sharpe**

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_LeeSharpe.jpg)Lee's day job is working in the finance department here at Wizards, but he has been an avid Commander player for years. Thus, I was excited to steal him away from his numbers for while to help out on this product. Lee's perspective on the Commander scene helped up focus on what makes Commander fun and make sure that we didn't stray from our target audience.

By the Numbers
This is **Magic**'s first product to feature new cards outside of a booster release, and as such presented some interesting challenges. The first thing that we had to consider was how we were going to sell the cards! While we quickly settled on five decks, there were many discussions in the pit regarding what colors should be featured in those decks. Design settled on wedges (two allied colors and their common enemy, like white and blue with red), though four color decks were considered strongly. Wedges had the advantage that three-color decks have more cohesion than four and that there is not a significant amount of difference between a four-color deck and a five-color deck. We did talk about four-color decks in development, but we liked what we saw coming from design and saw no need to change things.

![](https://media.wizards.com/images/magic/daily/mm/mm146_manaCircle5.gif)  
The next thing to consider was how many new cards were supposed to be in the five decks. Design handed off five decks, with ten new cards in each deck. All of the new cards in each deck were unique, with no overlap in the new cards between the decks. Unfortunately, this didn't work very well in our initial development playtests. We really wanted people to get excited about the new cards, and too frequently people didn't have even one in their opening hands. Some games were played in which no new cards were seen from a deck, and that was definitely a letdown. Furthermore, we wanted to ensure that everyone felt like they were getting a good value from their purchase. Even though we were packing the decks with exciting reprints, it was important to us that the decks felt new.

The tricky part was that we didn't want to increase the number of cards. We liked having around fifty new cards; this product is significantly smaller than a booster release, and we didn't want to overshadow either *New Phyrexia* or ***Magic** 2012*. On the other hand, fifteen new cards seemed to be a lot better than ten—people would usually have a new card in their opening hand. Could we get there? I started to play with some numbers... What if a few of the cards overlapped between the decks? Could we keep the number of new cards at fifty while increasing the number of new cards per deck to fifteen?

Almost. We identified ten mono-color cards that could each go in three decks. These were previously in just one deck each, so we ended up with an additional four cards in each deck. This gave us fourteen. Aha! How about increasing the size of the set of new cards by just one and putting this into every deck! This gave us our fifty-one-card set and fifteen cards in each deck.

Politics, Not as Usual
One of our goals was to ensure that this product had cards that were primarily for multiplayer games, including political cards. Most **Magic** sets have very little room for such cards as they are required to behave nicely in a two player game. Now we had a place to print more of these cards. For example, you may have already seen Death by Dragons, which Aaron Forsythe introduced in [his article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/119k) about ***Magic: The Gathering** Commander*. This is a fairly straightforward political card: you tick me off by attacking me, so I retaliate by giving everyone but you a 5/5 flying dragon! However, the design team wanted to go further than this and handed to development a deck that was completely political in nature.

Without further ado, let me introduce...

![](https://media.wizards.com/images/magic/daily/ld/bvcerrtsdyfghuijkdhuydygdusss.jpg)  
Zedruu is the commander of the "Political Puppets" deck. At first blush, this card may seem pointless or weak, but we found Zedruu to be one of the most subtly powerful commanders in the set. Typically, we'd see people interact with Zedruu something like the following:

**Playtest 1:** "Zedruu's deck is really weak! I don't know why I would want to give away any of my stuff anyway. Can I play another commander?"

**Playtest 2:** "Haha—I cast [Wall of Omens](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Omens) and after I drew my card, I gave it to my opponent. I drew a card off my Wall every turn!"

**Playtest 3:** "That game was awesome! I bribed my opponents to attack each other by giving them creatures and land. I also gave away my [Howling Mine](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howling+Mine)! Before they knew it, I was drawing more cards than everyone else at the table put together and my life total was over 60. I cruised to victory!"

Here is a card that we wouldn't make in a normal **Magic** set, but that feels right at home here. This card only required minor tweaks as it came in from design. Originally, it was a 2/5 that only counted the number of *players* who controlled permanents that you owned, rather than counting the actual number of donated permanents. However, despite the fact that everyone who came into contact with this card read it multiple times, no one read it correctly! We changed it to meet player expectations and balanced this out by reducing the toughness of the card from 5 to 4.

![](https://media.wizards.com/images/magic/daily/ld/lkf4wesdfoiespodshefkegrh.jpg)Zedruu the Greathearted | Illustration by [Mark Zug](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Mark+Zug%22%5D)

Further testing of Zedruu showed it to be in a great spot. Masters of diplomacy worked wonders with this commander. Some opponents loved being showered with gifts, while others feared receiving them and did everything possible to kill off Zedruu—repeatedly. While Zedruu certainly isn't for everyone, I believe she'll be well loved by many. I hope you have as much with Zedruu as I have!

Two weeks from now, Tom LaPille returns to Latest Developments. However, in the meantime, I have a question for all of you...

**Which of the five *Magic: The Gathering Commander* decks are you most excited about so far?**Heavenly Inferno (![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif))Mirror Mastery (![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif))Counterpunch (![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif))Political Puppets (![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif))Devour for Power (![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif))  
  
[![](http://wizards.com//mtg/images/daily/features/Banner_NPHArticleFooter_GameGeneric.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/gameday-facts)





