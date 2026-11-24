---
id: 86w23x9s
kind: article
lang: en
path: /en/articles/makingmagic/2003/11-03-baby-stories
title: Baby Stories
published: '2003-11-03'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr96
    lang_detected: en
    capture_id: 804551
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
    captured_at: '2010-01-02 05:27:00+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr96
    lang_detected: en
    capture_id: 804551
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
    captured_at: '2010-01-02 05:27:00+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr96
    lang_detected: en
    capture_id: 804551
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
    captured_at: '2010-01-02 05:27:00+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr96
    lang_detected: en
    capture_id: 804551
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
    captured_at: '2010-01-02 05:27:00+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 86w23x9s
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr96
  lang: en
  template: aspx
  captured_at: '2010-01-02 05:27:00+00'
  capture_id: 804551
  wayback_url: https://web.archive.org/web/20100102052700id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
- document_id: 86w23x9s
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr96
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr96
  lang: en
  template: classic_asp
  captured_at: '2005-08-04 08:25:08+00'
  capture_id: 1982967
  wayback_url: https://web.archive.org/web/20050804082508id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr96
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 86w23x9s
  capture_id: 804551
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
  wayback_url: https://web.archive.org/web/20100102052700id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr96
  captured_at: '2010-01-02 05:27:00+00'
  template: aspx
  sha256: 2f72859b79357f0facd361e5ee9988cfe5c9d112d728f79db397e73df72330d9
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:alert("Not implemented yet (mail)");
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - makingmagic@wizards.com
  occurrences: 1
---
One Monday morning, R&D all came into the office to find a cupcake with a question mark on top of it. Each cupcake rested on a paper plate with a different picture glued on it. Each cupcake also had a slip of paper with the following message:

### SOMEONE IN R&D

HAS SOME INTERESTING  
 NEWS. PUT THE 25  
 CLUES TOGETHER TO  
 FIND OUT WHO & WHAT

The pictures were of everything from Mr. T to the Chicago elevated train. The key to solving the puzzle was the realization that each picture represented a letter. T and L (as in the "el") for the above examples. When spelled out the secret message was:

### MARK AND LORA ARE HAVING TWINS!

Early next year my wife and I will be expected child #2 followed closely by child #3. If I'm to believe modern science, we'll be having a little baby boy and a little baby girl. And yes, I am quite excited. 

### Baby Pictures

But what does this have to do with a column on **Magic** design? First, **Magic** designers don't reproduce all that often (although a quick congrats to Mike Elliott whose first child, Quinn, was born last week), so when it happens it's big news. But more importantly for all of you, it has to do with this week's theme.

While I've only fathered three children, I have managed to spawn an even greater number of **Magic** expansions. One such expansion is *Mirrodin*. (As always I feel obligated to give props to my design team: Mike Elliott, Brian Tinsman and Tyler Bielman.) And since my mind has been on the thought of babies, I've been thinking a lot about *Mirrodin* as an infant. You see, most of the time I talk about a set, you see the work from the end of the design. That's like the set's adolescence. Today, I'm going to take you back to the set's childhood.

All the cards I will be discussing today come from the very first playtest we did with *Mirrodin*. This particular playtest was just with common cards as I was trying to get a feel for how the set worked at a basic level. Different designers work differently, but I'm a big fan of starting with the commons as they're the backbone of the limited experience.

My plan for today's column was to show you some of the cards that appeared in the first playtest. Some you should recognize, some you may recognize and some aren't anything you've ever seen. The idea here is that I wanted to give you all a chance to see cards in their infancy to see how the whole process begins.

### Baby Steps

Today's column is pretty free-form. I'm simply leafing through the playtest file in order (meaning white, blue, black, red, green, artifacts) and stopping whenever I come to a card that seemed interesting. 

**Armor Master**  
2W  
 Creature – Soldier  
 2/1  
 CARDNAME gets +2/+2 if equipped with armor.

![White, former color of Equipment - Armor](https://i.ormos.uk/42/9f/429fd1aae798f47735dc7d5da1efbb57e31d8b0e2fdb79b1fb7d7992ce7c534a.jpg) Very early in *Mirrodin* design, all the equipment had a subtype. There were five subtypes and each one was tied to a color: Armor (white) – defined as any item that was worn, Runes (blue) – defined as any written object such as scrolls or books, Weapons (black) – defined as anything kind of physical weapon such as a sword or crossbow, Potions (red) defined as any magical item you drank and Items (green) – the catchall category.

As white was the color of armor, we thought it would be cool to have a creature that was improved when it wore armor. Note that it wasn't until development that the boosted by equipment theme was cemented in white.

**Porcelain Knight**  
1WW  
Creature- Knight  
3/1  
2 or W: Prevent 1 damage to CARDNAME.

We began fooling around with alternative activation costs from the very beginning of the design because we felt they worked so well on artifacts. This is an example where we tried to see if the same mechanic would work on a colored card. By mid-design, we figured out that the two costs had to be further apart than one mana to be interesting, so we decided to just put them on artifacts.

**Zealous Warrior**  
2W  
 Creature — Warrior  
 1/4  
 If you control two or more artifacts, CARDNAME gets +2/+0.

During the early part of design, we experimented a lot with different ways to make artifacts matter to other cards in the set. This theme would later work its way to black on the Nim creatures. 

**Send 'em Farming**  
3W  
 Instant  
 Affinity – Artifacts (*For each artifact you have in play, CARDNAME costs 1 less.*)  
 Remove target attacking creature from the game. 

Early on we also experimented with affinity for artifacts in blue's allies, white and black, as well as in blue and artifact. As the developers started playtesting during design, they convinced the design team that the affinity mechanic, for power reasons, needed to be kept to a minimum number of cards. In addition, we liked the idea of the mechanic focusing on a single color. Thus, we took it out of white and black.

**Bulwark**  
W  
 Enchantment  
 All your creatures get +0/+1. All your artifact creatures get an additional +0/+1. 

Here's another lost card that demonstrates the design team trying to come up with different ways to make "artifact matters" cards in the various colors.

**Gromling**  
U  
 Creature – Illusion  
 1/1  
U, T: Tap or untap target artifact. 

Yes, Auriok Transfixer started as a blue card. The design team found that blue had more design space for artifact friendly cards, so we moved this ability off to white. We took off the "or untap" to fit the card into white's section of the color pie. 

![Fixed: Gromling and Whirlwinders](https://i.ormos.uk/87/41/8741e826ba595ae87b28dd54a12e3fdcab4d3a8ecab55fd2fd6af0ae1285e9ba.jpg)

**Whirlwinders**  
4U  
 Creature – Vedalken  
 3/2  
 Flying  
 Affinity – Artifacts (*For each artifact you have in play, CARDNAME costs 1 less.*) 

For the entire time Somber Hoverguard was in design, it cost one less. 

**Bouncing Beebles**  
2U  
 Creature – Beeble  
 2/2  
 CARDNAME is unblockable if defending player controls an artifact. 

I just wanted the world to know that for at least the first playtest, this card was still a beeble. It's also interesting to note that we seriously considered giving this card artifactwalk. By we I mean the designers as the actual rules and templating people shot me dirty looks for merely suggesting it. 

**The More You Know**  
3U  
 Sorcery  
 Affinity – Artifacts (*For each artifact you have in play, CARDNAME costs 1 less.*)  
 Draw two cards. 

For all of design, Thoughtcast also cost one less mana. You can begin to see why we separate R&D into designers and developers. 

**Smarty Pants**  
XU  
 Instant  
 Counter target spell unless its controller pays an additional X.  
Affinity – Artifacts (*For each artifact rune you have in play, CARDNAME costs 1 less.*) 

I thought this card was clever. With four artifacts in play, I can sink for five for 1U. Having X in an affinity for artifacts spell proved to be a tad confusing. 

**Reconstruction**  
U  
 Sorcery  
 Bring one artifact from your graveyard to your hand. 

Here's a repeat from the first playtest that didn't make it into the final set. 

**Weapon Master**  
2B  
 Creature – Soldier  
 2/1  
 CARDNAME gets +2/+2 if equipped with a weapon. 

Here's the mirror of the Armor Master. Oddly, the black version was much, much better. 

**Life Syphon**  
5B  
 Sorcery  
 Affinity – Artifacts (*For each artifact you have in play, CARDNAME costs 1 less.*)  
 CARDNAME deals 3 damage to target creature or player. You gain 3 life. 

I showed you a white card with affinity for artifacts, so it seems only fair to show you a black one. 

**Mass Fear**  
2B  
 Sorcery  
 All your creatures gain "can't be blocked except by artifact creatures and black creatures" until end of turn. 

For some reason the design team thought it was particularly funny to have more fear than normal in this set. Here's a bland fear card that was luckily put out to pasture early in design. 

**Go Fish**  
1B  
 Sorcery  
 Name a non-land card. Target player reveals his or her hand and discards all copies of the named card. 

I've put variants of this card in designs for the last several years. It was in the first *Mirrodin* playtest because I didn't realize Cabal Therapy had actually made it into *Judgment*. (The card had been cut in development numerous times.) And yes, this is a much suckier version.

**Gung-ho Orc**  
3R  
 Creature- Orc  
 4/1  
 Sacrifice an artifact: CARDNAME gains haste and first strike until end of turn. 

This card would later morph into Krark-Clan Grunt. The red "sacrifice artifacts for effects" ability was one of the themes in the set from the beginning.

**Explosive Goblin**  
2R  
 Creature- Goblin  
 2/2  
 When CARDNAME is put into the graveyard from play, destroy target artifact. 

You think *Mirrodin* has a lot of artifact hate? You should have seen the first playtest. Here's one of many artifact kills built into the early set. 

**Fixed Pixies**  
1G  
 Creature – Elf  
 2/1  
 Protection from artifacts

The early playtest names tend to tell it like it is. Tel-Jilad Chosen is just a cleaned up Argothian Pixies. 

**Spuzzy Bugger**  
1G  
 Creature- Bear  
 2/2  
 If CARDNAME deals damage to an opponent, you may destroy target artifact that player controls. 

Rustmouth Ogre started as a green common. As I said before, early *Mirrodin* playtest had a lot of artifact kill. 

**Spike Drone**  
G  
 Creature – Spike  
 0/0  
 Spike Drone comes into play with one +1/+1 counter on it.  
2, Remove a +1/+1 counter from Spike Drone: Put a +1/+1 counter on target creature. 

With all the +1/+1 counters running around *Mirrodin*, we toyed around early in design with bringing back the spikes. The set ended up being too busy to support them, but I promise someday the spikes will return.

**Crumble**  
G  
 Instant  
 Destroy target artifact; artifact creatures may not regenerate. Artifact's controller gains life points equal to target artifact's casting cost.

Here's a card that matches two ongoing themes: the massive amount of artifact kill and the repeats that showed up early but never made it into the set. 

**Squire Gnome**  
1  
 Artifact Creature – Gnome  
 1/1  
 CARDNAME gets +2/+2 as long as its equipped. 

In the first design, this was the only creature that was enhanced by being equipped by any type of equipment. The card worked out so well (and trust me, this version was a beating in limited) that we later chose to expand the theme and move it to white.

**Clay Soldier**  
4  
 Artifact Creature - Soldier  
 2/2  
 Whenever CARDNAME becomes blocked, regenerate it. 

This card went through seven or eight changes. It's ironic that the card (Duskworker) ended up right back where we started. (Okay with one added activated ability.) 

**Artifact Lover**  
7  
 Artifact Creature  
 4/4  
 Affinity – Artifacts (*For each artifact you have in play, CARDNAME costs 1 less.*) 

Myr Enforcer was one of a few cards that was printed in the set as it appeared in the first playtest. 

**Boots of Speed**  
1  
 Artifact Equipment- Armor  
 Equipped creature has haste and does not tap when attacking.  
 Whenever the creature CARDNAME equips is put into the graveyard from play, return CARDNAME to its owner's hand.

This is the earliest version of Lightning Greaves. Note that at this time, artifact equipment worked exactly like creature enchantments.

**Urza's Fuse**  
2  
 Artifact – Item  
 Sacrifice CARDNAME: Regenerate target permanent. Draw a card. 

Go [Welding Jar](/en/articles/makingmagic/2003/10-20-dear-diary)!

**Cubic Zirconium**  
2  
 Artifact  
T: Each player may untap a land. 

I forget why this card got killed but I assume it was for one of two reasons: 1) It was super weak and ultra lame or 2) It was broken.

**Marble Golem**  
5  
 Artifact Creature - Golem  
 3/4  
W: CARDNAME does not tap to attack this turn.

Design was close. So very close.

**White Scepter**  
2  
 Artifact - Item  
3, T or W, T: Target player gains 2 life. 

In early playtest, the Shards (then the Scepters) were common. The white one sucked so we changed it from life gain to damage prevention. 

**Blessed Armor**  
1  
 Artifact Equipment – Armor  
2 or W: Equipped creature gets +0/+1 until end of turn.  
 Whenever CARDNAME is put into the graveyard from play, return CARDNAME to its owner's hand. 

To try and make equipment cooler than creature enchantments, we originally tried to build abilities into each sub-type that helped work around the normal vulnerabilities of localized permanents. Armor always returned to your hand when the creature died. It was this flavor of reusable equipment that later led us down the path that ended up with the current equipment. 

**Scroll of Healing**  
1  
 Artifact – Runes  
4, Sacrifice CARDNAME or W, Sacrifice CARDNAME: Prevent all damage to target creature or player from any one source. 

Scrolls were going to function similarly to *Nemesis*' seals although with an alternative activation cost. 

**Metallic Bird**  
3  
 Artifact Creature – Bird  
 1/2  
 Flying  
U, Sacrifice CARDNAME: Counter target spell unless its controller pays an additional 2. 

The Replica cycle was in *Mirrodin* since the first playtest. Somehow turning into a wizard from a bird got the creature an extra toughness. Hmm, perhaps proof of Wizards' greater conspiracy to keep birds down? (Just take a look at Kangee, Aerie Keeper if you want more proof.) 

**Blue Scepter**  
3  
 Artifact - Item  
3, T or U, T: Target player draws a card and discards a card. 

The original blue shard also did something different. Once again, the change made the card stronger. 

**Orb of Frost**  
2  
 Artifact Equipment - Item  
1, Tap equipped creature: Tap or untap target creature.  
2U: Untap equipped creature. 

I really liked this card. It shouldn't have been common, but I thought it was real cool. The card was killed when we decided to bring back Icy Manipulator.

**Robo-Minion**  
2  
 Artifact Creature – Minion  
 1/1  
3, T or B, T: Target creature gets –2/-0 until end of turn. 

Besides having a golem cycle with colored activations and a shard cycle with alternative activation costs, the original playtest file had a cycle of creatures with an alternative activation cost (all with a tap). 

**Black Scepter**  
3  
 Artifact - Item  
3, T or B, T: Look at target player's hand and choose a non-land card. No copy of the chosen card may be played this turn. 

We struggled with the black shard for a long time. This version was ultra-lame. We thought up the raise dead variant early on, but it simply didn't feel common. Development later solved this problem when the shards got moved to uncommon.

**Gauntlet of Pain**  
3  
 Artifact Equipment - Armor  
 Equipped creature gets +1/-1.  
B: Equipped creature gets an additional +1/-1 until end of turn. 

Here's a piece of equipment from back in the day when you could put equipment on the opponent's creatures. I'm not sure the flavor of this card. You leave the shiny gauntlet lying on the battlefield and some dumb goblin feels compelled to put it on? 

**Red Scepter**  
3  
 Artifact - Item  
4, T or R, T: CARDNAME deals 1 damage to target creature or player. 

![Green Scepter](https://i.ormos.uk/60/d1/60d184ff74ff8b3531152a1afe3df4d5428ffe41a85d18647c4fc5861c92b97e.jpg)

The earliest version of the red shard cost 4 to activate as I was trying to not strictly obsolete Rod of Ruin. It's also interesting to note that this is the only shard whose ability stayed the same through design and development. 

**Green Scepter**  
2  
 Artifact - Item  
3, T or G, T: Target creature gets +2/+2 until end of turn.

I felt it was important for all the green mages out there to know that early on the green shard was a force to be reckoned with. All the designers were playing this in their decks regardless of if they were playing green. The card was later changed as the development team needed to swap around certain abilities.

### Baby Talk

I hope you enjoyed the tour through *Mirrodin*'s infancy. As you can see, some ideas started from the beginning while others had a long journey ahead of them. 

Join me next week when I make a mistake or two...

Until then, may you know the joy of watching your own baby grow up.

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*