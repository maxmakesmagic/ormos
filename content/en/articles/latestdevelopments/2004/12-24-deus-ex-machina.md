---
id: aprs6bn1
kind: article
lang: en
path: /en/articles/latestdevelopments/2004/12-24-deus-ex-machina
title: Deus Ex Machina
published: '2004-12-24'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    lang_detected: en
    capture_id: 720577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    captured_at: '2022-08-11 01:24:41+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    lang_detected: en
    capture_id: 720577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    captured_at: '2022-08-11 01:24:41+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    lang_detected: en
    capture_id: 720577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    captured_at: '2022-08-11 01:24:41+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    lang_detected: en
    capture_id: 720577
    url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
    captured_at: '2022-08-11 01:24:41+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: aprs6bn1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
  page_key: magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
  lang: en
  template: drupal
  captured_at: '2022-08-11 01:24:41+00'
  capture_id: 720577
  wayback_url: https://web.archive.org/web/20220811012441id_/https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
- document_id: aprs6bn1
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af46&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af46
  lang: en
  template: aspx
  captured_at: '2009-06-04 15:39:34+00'
  capture_id: 253272
  wayback_url: https://web.archive.org/web/20090604153934id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af46&print=true
- document_id: aprs6bn1
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af46,,de
  page_key: wizards.com/default.asp?x=mtgcom/daily/af46
  lang: en
  template: classic_asp
  captured_at: '2005-02-07 18:53:39+00'
  capture_id: 1928774
  wayback_url: https://web.archive.org/web/20050207185339id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af46,,de
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: aprs6bn1
  capture_id: 720577
  url: https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
  wayback_url: https://web.archive.org/web/20220811012441id_/https://magic.wizards.com/en/articles/archive/latest-developments/deus-ex-machina-2004-12-24
  captured_at: '2022-08-11 01:24:41+00'
  template: drupal
  sha256: 66561d7d605d3db0c61241c35bc0aa001594567194f215e649055f34b8e8a75a
render_recovery: []
---
*Two of my favorite elements of the* Fifth Dawn *expansion are the four Stations and the “cog” theme (which revolves around 0- and 1-mana artifacts). In fact, when people ask me my favorite card from the set, the answer is [Trinket Mage](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinket+Mage). The development of these two mechanics was both interesting and amusing, as this article shows…*

*This article originally appeared on May 28th, 2004.*

First off, I'd want to give thanks to local TO Tim Shields for his hospitality at the Seattle *Fifth Dawn* Prerelease last weekend. Tim was great, allowing myself and other members from R&D and the ***Magic** Online* team to battle against players using sealed decks. We all had a blast and learned a lot. Thanks, Tim!

### God in the Machine

On Monday, Mark Rosewater explained the design of the “cog” and “gear” cards from *Fifth Dawn* in his “[Cog Wild](https://web.archive.org/web/20041224000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr125)” column. Here in Latest Developments, I'll finish the tale by explaining what happened to these cards after the design handoff. You may want to keep that link handy to look back at the design versions of the cards as Mark listed them.

### The Cog Helpers

The *Fifth Dawn* design file contained many, many sub themes--quite a few more than what are in the set now. All that extra stuff going on buried the “cog” (read as: “artifact that costs 1 mana or less”) theme, and almost doomed it. The fact that “Cog Bear” (![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif); 2/2; When CARDNAME comes into play, return a cog from your graveyard to your hand) and “Cog Collector” (![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif); 1/1; ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), : Return a cog from your graveyard to your hand) were so similar did little to convince the development team that the theme was robust enough to support more than a card or two, if it should exist at all.

Mark leapt to the defense of the cog helpers, and pleaded that development give them another look. His argument--that they would play very well in limited and would enable some fun (if not competitive) decks--was sound, and the team sat down to see if the theme could be salvaged.

The fixes were subtle but effective. “Cog Bear” and “Cog Prestidigitator” stayed exactly the same, and were printed as [Leonin Squire](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Squire) and [Trinket Mage](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinket+Mage) respectively. “Survival of the Cogs” was simplified (and made better) by removing the restriction on what kinds of artifacts needed to be discarded to activate it, and was printed as [Artificer's Intuition](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Artificer%27s+Intuition). The biggest change, though, was made to “Cog Collector.”

In an attempt to distance it from Cog Bear and create more combo potential, development changed the card to this:

 

![Auriok Salvagers](https://i.ormos.uk/51/7e/517e6524f5b2c407f92852e018a28dfbc2da3bdc52f7e080c4531c158af0826b.jpg)

Cog Collector  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)  
 Creature - Human Archaeologist  
 2/4  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif): Return target cog card from your graveyard to your hand.

That change made the Collector a lot harder to kill and opened the door for him to be used more than once per turn. Eventually a mana was shaved off his activation cost so that he'd be more useful earlier in the game, and he was printed as [Auriok Salvagers](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Salvagers).

### The Cogs

With the helpers in place, the team needed to decide at what level the cogs themselves should exist in the set. With *Mirrodin* contributing so many good ones (namely [Chromatic Sphere](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chromatic+Sphere), the cycle of Spellbombs, and the cycle of artifact lands), they felt *Fifth Dawn* didn't need too many powerful cogs, just some neat utility. Here's a look at each cog in the set:

*   ![Razorgrass Screen](https://i.ormos.uk/af/b2/afb23350ec1432eea5de7bab3eab9f731d77f7e46bde99f1ee397d0014bea538.jpg)

    The cycle of colored cogs that Mark mentioned (“Medical Kit,” “Spit Stone,” “Syphon Trinket,” “Energy Pill,” and “Lotus Stem“) were all removed from the file when the cycle of “swords” (equipment that could be moved at instant speed, such as [Cranial Plating](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cranial+Plating)) was moved from uncommon to common. Because the big theme of *Fifth Dawn* was to be multicolored play, the team didn't want more than one cycle of single-color-aligned artifacts. Their removal created a lot of holes, and I was pleased that they chose several cards I designed to fill those holes. [Wayfarer's Bauble](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wayfarer%27s+Bauble) and [Conjurer's Bauble](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conjurer%27s+Bauble) are tweaked versions of cards I came up with, and [Lantern of Insight](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lantern+of+Insight) and [Razorgrass Screen](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Razorgrass+Screen) were printed exactly as I turned them in. It's interesting to note that the latter two are pretty bad cards on their own, but become intriguing when they can be reused multiple times.
*   Mark's “Myr Temp” was given a mana cost of 1 and printed as [Chimeric Coils](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chimeric+Coils).
*   [Avarice Totem](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Avarice+Totem) was submitted as “Vedalken Currency,“ a 5-mana card that exchanged with something when it came into play in addition to having the 5-mana activated ability. The team made it into a cog by removing the first ability.
*   [Myr Servitor](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Myr+Servitor) (originally called “Robo-Roach”) and [Engineered Explosives](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Engineered+Explosives) (originally called “Maximize Keg”) were both printed as they came in from design. The Explosives is perhaps the most versatile of all cogs.
*   [Paradise Mantle](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paradise+Mantle) was created by Mark during development to help the multi-color theme.

### The Gears

On the day the file was handed to development, lead developer Brian Schneider asked me to show him how the cycle of six gear cards (see Mark's article) worked together to form an infinite combo. I had printed out playtest stickers of the six cards, and laid them out on his desk.

"Ok," I started, "first sacrifice an artifact with this one. No, first use this one to make a creature, then it untaps when you use the other one. Now one of these other four should untap…"

As I struggled to explain how it worked, Brian just shook his head. It was way more complicated in play than it was on paper. I also showed it to our resident Johnny, Mark Gottlieb, and asked him to figure out how the six cards worked together on his own. It took him a lot more effort than I was hoping. Brian then asked Mark Rosewater if he could come up with a smaller version of the cycle.

Mark came up with this:

**Throwing Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)  
 Artifact  
 T, Sacrifice an artifact: CARDNAME deals 1 damage to target creature or player. Whenever an artifact comes into play, you may untap CARDNAME.

**Phyrexian Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)  
 Artifact  
, Sacrifice a creature: Target player draws a card.  
 Whenever a creature comes into play, you may untap CARDNAME. 

**Cog Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)  
 Artifact  
: Put a non-creature artifact card with a mana cost of 1 or less from your graveyard into play.  
 Whenever a creature goes to a graveyard from play, you may untap CARDNAME. 

**Breeding Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless7.gif)  
 Artifact  
: Put a 2/2 green NAME token into play.  
 Whenever an artifact is put into the graveyard from play, you may untap CARDNAME.

I talked with Brian about what triggers and effects development liked and didn't like, and what effects the block was already heavy on, and we changed these around a bit. We didn't want card drawing to be part of the infinite engine, so we worked milling your opponent into the mix. That way the combo could beat stuff like [Worship](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worship) or [Leonin Elder](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Elder). We also switched around what was sacrificed for what effect, giving us the following four cards:

**Milling Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)  
 Artifact  
, Sacrifice an artifact: Target player puts the top X cards of his or her library into his or her graveyard, where X is the converted mana cost of the artifact sacrificed.  
 Whenever an artifact comes into play, untap CARDNAME.

**Flinging Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)  
 Artifact  
, Sacrifice a creature: CARDNAME deals 1 damage to target creature or player.  
 Whenever a creature comes into play, you may untap CARDNAME. 

**Reinforcing Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)  
 Artifact  
: Put a non-creature artifact card with a mana cost of 1 or less from your graveyard into play.  
 Whenever a creature goes to a graveyard from play, you may untap CARDNAME. 

**Breeding Gear**  
![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless7.gif)  
 Artifact  
: Put a 2/2 green NAME token into play.  
 Whenever an artifact is put into the graveyard from play, you may untap CARDNAME.

And that is how they were playtested. Note that the "noncreature" clause was already in place on the Reinforcing Gear because of the potential ease of abuse with [Atog](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Atog) and [Ornithopter](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter).

### Putting Them Together

At that point the cogs and the gears were tried out in various decks. My favorite story involves playing with the prototype of the "Nuts & Bolts" theme deck. Brian asked me how the deck was playing. "Great," I replied, "I just gained infinite life."

The combo at fault was Reinforcing Gear, [Leonin Elder](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Elder), and Myr Temp (aka [Chimeric Coils](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chimeric+Coils)). With the Elder and the Gear in play, the Temp could be activated for 0, making it a 0/0 creature which would then die. Its death would trigger the untapping of the Gear, which could then be tapped to put the Temp back into play. Repeat.

A mean person might try this same combo using [Disciple of the Vault](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault) to end the game, so something had to be done about the Temp. And that is why [Chimeric Coils](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chimeric+Coils) has the goofy activation cost of 1X.

Brian continued to test Reinforcing Gear in constructed. Of note is the fact that many of the cogs in the set lacked the "Tap" symbol in their activations. [Lantern of Insight](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lantern+of+Insight), for example, was just "Sacrifice CARDNAME" instead of ", Sacrifice CARDNAME."

 

![Chromatic Sphere](https://i.ormos.uk/23/b4/23b44e7e2cd6c147b30cf0d053b0aa57eb74ad5523dc248167d7bbba61eb10f0.jpg)

Our editing department was trying to clean up extraneous symbols, and there was no real reason to have them. *Mirrodin*'s [Chromatic Sphere](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chromatic+Sphere) does have an "extraneous" tap symbol, but that's because it is a repeat of the *Invasion* version, which is based off the *Ice Age* card [Barbed Sextant](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barbed+Sextant), which was made before our templating was as advanced as it is now. But the *Mirrodin* Spellbombs all have no tap symbols because there's really no reason for them to.

Brian built the deck that put the tap symbol back on some of the cards in this set. It involved Reinforcing Gear, [Lantern of Insight](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lantern+of+Insight) (or [Conjurer's Bauble](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conjurer%27s+Bauble)), and [March of the Machines](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=March+of+the+Machines). With that combo (using the Lantern), you could control what card every player in the game would draw every turn. And with [Conjurer's Bauble](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conjurer%27s+Bauble), you could just draw your deck. (Or just kill your opponent with everyone's favorite man, [Disciple of the Vault](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault).) Editing said they didn't want to put tap symbols on the Baubles unless we gave them good reason, and Brian's deck was reason enough. [Wayfarer's Bauble](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wayfarer%27s+Bauble) probably doesn't need a tap symbol, but it was given one to sync up with the other cogs in the set, and with its predecessor, [Braidwood Sextant](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Braidwood+Sextant).

Further testing of the Reinforcing Gear showed that five mana was probably too little for the effect, and development raised it to 6 (I protested, since I was such a fan of the 1 – 3 – 5 – 7 pattern of costs for the gears). With the cost pattern broken, they also moved the cost of Milling Gear from 1 to 2 so that the gear itself wouldn't be useable as fuel for the combo… you needed another piece—any noncreature cog—to get it up and running. The number of cards milled was also changed, from X to 3.

### Naming Names

The most fun story involving the Gears is about how they got their real names. They were the last cards in the set to get real names—the names and flavor text team was stumped. Brandon Bozzi, **Magic's** creative coordinator, brought the sketches of the four gears into the middle of R&D one day and all but begged for help. (Greg Staples' and Stephen Tappin's art on these four cards is fantastic. It's a bit of a departure from the "living metal" in the rest of the *Mirrodin* block, but it certainly captures the "Great Machine" feel we were after. They are reminiscent of some of the machine-like artifacts from the early days of **Magic**.)

  
*The Great Machine*

The four pieces were obviously all stops on an assembly line, but what would those be called? "Stops?" "Modules?" A quick search on the internet showed that the most "correct" name for different points on an assembly line was "stations." Not the most exciting name, but Brandon conceded that at least it made more sense than other options. So what then?

Someone—and my guess is on Mark Rosewater—then suggested that all the names rhyme with "station." The Flinging Gear, for instance would be the "Incineration Station." And the Breeding Gear would be the "Replication Station." Perhaps it was simply end-of-the-week fatigue, but all the people in the vicinity were tickled pink by that idea. So there we were, perhaps six to eight of us, paging through thesauruses and looking at web pages for anything that ended with "-ation." Our lists grew massive, and included everything under the sun, from the scientific to the obscene.

Some samples:

Annihilation Station  
 Gestation Station  
 Aggravation Station  
 Reinvigoration Station  
 Incubation Station  
 Devastation Station  
 Restoration Station

Trust me, it was funny at the time. Picture all of us—Buehler, Gottlieb, Rosewater, Dommermuth, and more—tears streaming from our eyes as we proposed name after name.

The Richard Garfield walked in—he had dinner plans with Bill Rose and had come by to meet him. We stopped him and told him our ideas for this cycle of names, hoping to get a rise out of him.

Instead, he looked at all of us like we were stupid and shrugged his shoulders. What a party pooper!

Come Monday, the joke wasn't quite as funny anymore, and Brandon had quietly put together a list of less silly names. I suppose we should be thankful.

### Tidbits

Some final remarks on cogs and gears:

*   The goal behind the gears all along was to make a group of cards that combined to win the game, but were all useful and interesting on their own. I believe we accomplished that. The best way to use any one of the Stations is not by building the "Great Machine," but by finding other unique ways to abuse its reusability.
*   ![Steelshaper's Gift](https://i.ormos.uk/12/16/1216e95ff23d27b0384e53030f052009b320a455e38a0f0bf851d4e24027d3aa.jpg)

    [Steelshaper's Gift](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steelshaper%27s+Gift) at one point in design read: "Search your library for an equipment or gear card" and it had scry 2. (It cost ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) then.) The scry and gear-tutoring were deemed unnecessary and were cut, thus eliminating the need for the gears to have a subtype.
*   [Summoning Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summoning+Station) does not make artifact creatures – the tokens are colorless 2/2 Pinchers, but are not artifacts. [Sliver Queen](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sliver+Queen) and [Brood Sliver](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brood+Sliver) are other examples of cards that make colorless tokens.
*   If more than one creature comes into play at one time (via [Beacon of Creation](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beacon+of+Creation), for example), [Blasting Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasting+Station) triggers that many times. You can respond in between the resolution of each trigger by activating the Station.
*   [Trinket Mage](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinket+Mage) can be used as a blue “mana fixer" by searching up artifact lands from your deck.
*   Still don't know how the Stations work? Get all four in play along with any artifact land. Tap [Summoning Statio](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summoning+Statio)n to make a 2/2. Sacrifice the token to [Blasting Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasting+Station) to deal one damage to your opponent. Sac the land to [Grinding Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grinding+Station) to mill your opponent for 3, and [Summoning Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summoning+Station) untaps. Tap [Salvaging Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Salvaging+Station) to put the land back into play, and [Grinding Station](https://web.archive.org/web/20041224000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grinding+Station) untaps. At this point you're basically back to square one. Wow, that's still pretty complicated, and I now realize that you can generate infinite mana as well by tapping and reusing the artifact land fuel. Crazy. I can't wait for these to be on ***Magic** Online*.

Enjoy! I'll be back next week to talk about one particular powerful cog.

### Last Week's Poll

<table><thead><tr><th colspan="3">Are you going/did you go to the <i>Fifth Dawn</i> Prerelease?</th>&#10;		</tr></thead><tbody><tr><td>Yes</td>&#10;			<td>7193</td>&#10;			<td>50.7%</td>&#10;		</tr><tr><td>No</td>&#10;			<td>7003</td>&#10;			<td>49.3%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>14196</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

More than half! Great to see! The rest of you… what could possibly have been more important? For shame!

*Aaron may be reached at latestdevelopments@wizards.com.*