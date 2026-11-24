---
id: x43kjbq1
kind: article
lang: en
path: /en/articles/feature/2007/09-14-gnarls-barkley
title: Gnarls Barkley
published: '2007-09-14'
column_slug: feature
column: Feature
authors:
- slug: devinlow
  name: Devin Low
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    lang_detected: en
    capture_id: 700124
    url: https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    captured_at: '2022-08-12 14:14:13+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    lang_detected: en
    capture_id: 700124
    url: https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    captured_at: '2022-08-12 14:14:13+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    lang_detected: en
    capture_id: 700124
    url: https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    captured_at: '2022-08-12 14:14:13+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    lang_detected: en
    capture_id: 700124
    url: https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
    captured_at: '2022-08-12 14:14:13+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: x43kjbq1
  url: https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
  page_key: magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
  lang: en
  template: drupal
  captured_at: '2022-08-12 14:14:13+00'
  capture_id: 700124
  wayback_url: https://web.archive.org/web/20220812141413id_/https://magic.wizards.com/en/articles/archive/gnarls-barkley-2007-09-14
- document_id: x43kjbq1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/gnarls-barkley-2007-09-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/gnarls-barkley-2007-09-14
  lang: en
  template: drupal
  captured_at: '2022-01-27 21:36:54+00'
  capture_id: 722803
  wayback_url: https://web.archive.org/web/20220127213654id_/https://magic.wizards.com/en/articles/archive/latest-developments/gnarls-barkley-2007-09-14
- document_id: x43kjbq1
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl2
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/dl2
  lang: en
  template: aspx
  captured_at: '2013-07-07 17:26:06+00'
  capture_id: 788310
  wayback_url: https://web.archive.org/web/20130707172606id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl2
- document_id: x43kjbq1
  url: http://wizards.com/default.asp?x=mtgcom/daily/dl2
  page_key: wizards.com/default.asp?x=mtgcom/daily/dl2
  lang: en
  template: classic_asp
  captured_at: '2008-06-16 00:53:13+00'
  capture_id: 1949268
  wayback_url: https://web.archive.org/web/20080616005313id_/http://wizards.com/default.asp?x=mtgcom/daily/dl2
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: x43kjbq1
  capture_id: 788310
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl2
  wayback_url: https://web.archive.org/web/20130707172606id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl2
  captured_at: '2013-07-07 17:26:06+00'
  template: aspx
  sha256: 7079039e9f1b6ed286ff47977f783bd084c0501127825cd8a1e2fd8d7bc08d55
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Torment
  - Shapeshifter
  - Ravenous Baloth
  - Loxodon Hierarch
  - Burning-Tree Shaman
  - Jade Leech
  - Birds of Paradise
  - Ohran Viper
  - Forbidding Watchtower
  - Tarmogoyf
  - Mire Boa
  - Soltari Priest
  - Giant Solifuge
  - Fatal Frenzy
  - Terror
  occurrences: 18
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - here
  occurrences: 1
---
Hello! Today I'd like to introduce the *Lorwyn* development team, then introduce my first *Lorwyn* preview card. It's the powerful three-color gold legend we nicknamed Gnarls Barkley. I'll talk about the card design that had to die so that Gnarls could live. I'll show you Gnarls himself. Then I'll talk about some of his ups and downs in development before he reached his final form.

### A Tribe of Developers

Gnarls Barkley isn't the actual name of the card, but I'm 90% sure these are the actual names of the *Lorwyn* development team. Whenever I introduce a team, I'll mention the lead first, then go alphabetically by last name.

![Devin Low](https://i.ormos.uk/b4/cb/b4cb1dbc8b6ce71bfe038cb69426ccfbcc17b7781c40cd762bbfe20c243502e3.jpg) **Devin Low (lead developer)** – Up until *Lorwyn*, I had been a balanced multiclass Wizard (Designer) / Cleric (Developer), having done 5 teams of each. When I led *Lorwyn* development, my developer half pulled ahead to 6 teams.

  
  

![Doug Beyer](https://i.ormos.uk/36/ec/36ec6013327716582eaca4dccd0e02a5ff23310016e218e4b883d659190f9844.jpg) **Doug Beyer** – **Magic** Development teams often include an envoy from the creative team to help the development side and the creative side of the department communicate, especially on big sets. This helps the development team dramatically. When we try to change a creature's subtype from Kithkin to Merfolk in a meeting, the creative liaison knows when to halt the change because the art is already commissioned as a Merfolk. The liaison can explain the flavor of a planeswalker so we know whether a proposed ability change fits. And when we're selecting which hole submission to use for a story character from the novels, the liaison can give that character's detailed back story. Doug Beyer, new author of the [Taste the Magic](https://web.archive.org/web/20130702142219/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/columnarchive) column on this site, was an excellent creative envoy, and he went beyond that by also being a high-quality developer. Doug has been head-over-heels into *Magic* for many years, as you can tell from his series of articles (available [in his archive](https://web.archive.org/web/20130702095626/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/authorarchive)) about the most fun cards that each set adds to the 5-color 250-card **Magic Online** "Prismatic" format. Doug also provided a great non-Spike viewpoint to the team.

![Matt Place](https://i.ormos.uk/3d/d4/3dd458e4ffc2ff85d5fa278d0ce011053e5cbf45dba76b6c93dbdf63ad209dde.jpg) **Matt Place** – Matt is one of the core **Magic** developers, and he brought the Rakdos, Simic, and Azorius to life by leading the development team for *Dissension*. Before joining **Magic** R&D four years ago, Matt played many Pro Tours, made Top 8 multiple times, and won the entire Pro Tour playing *Tempest* draft at PT–Mainz in 1997. Matt is especially valuable on a development team because he questions assumptions that others take for granted, often convincing the rest of us that we should reconsider what we thought was locked in and do things a better way. He specializes in multicolor control decks. He was a tireless champion for Elves in Lorwyn, making sure that we stayed true to the spirit of Elves from *Onslaught* and earlier that so many players have enjoyed so much, while also adding new twists.

![Bill Rose](https://i.ormos.uk/00/f0/00f0ed808bf783593fa50dc0bb62b0a3c5205959711abf74935e2494c1da60a7.jpg) **Bill Rose** – Before his current job as a vice-president of Wizards and head of R&D, Bill Rose was lead designer of the fan favorite set *Invasion*, as well as a designer and/or developer on many other **Magic** sets. Bill has a million demands on his time, and wasn't able to come to very many meetings, so his strategy for Lorwyn development was to keep asking people in the department "Is *Lorwyn* fun?" If someone said "It's just okay," he'd come and ask a lot of questions. When people said "It's fun!" he'd fade back and let things proceed without him. Fortunately, as Lorwyn development went forward, everyone said "It's fun!" so Bill was content to let us run the show.

![Henry Stern](https://i.ormos.uk/a4/ea/a4eab60e0bf3ff384241dc49d6f55a554f39573dcf76c5689f312d50a5fd9578.jpg) **Henry Stern** – Henry is a veteran **Magic** developer who was leading the development for sets like *Torment* while the rest of us were still in the outside world playing them. Wizards hired him after his success in **Magic**'s earliest World Championships. Henry has an uncanny knack for identifying early in a development cycle which mechanics will sink and which will swim. He now focuses on New Business games, and he recently won Games Magazine's Game of the Year award for his board game *[Vegas Showdown](https://web.archive.org/web/20130219155641/http://www.wizards.com/Magic/Magazine/Article.aspx?x=ah/prod/vegasshowdown)*. Though his duties are primarily non-**Magic** these days, Henry has led more **Magic** development teams than anyone else in the department, and he has a palpable Aura of Wisdom that ensures we always give his opinions a lot of weight. Henry likes to adopt pet cards that he identifies as nuggets of fun and make sure they survive the development process.

![Mike Turian](https://i.ormos.uk/2b/09/2b094d288b20f58968d51834eb02b2ed1381ae876700918a5c14f07004174e55.jpg) **Mike Turian** – Mike is another of **Magic**'s core developers. As the lead developer of *Future Sight*, Mike successfully wove all the crazy madness of the future into a cohesive, fun tapestry. Before he came to Wizards, Mike crowned an incredible Pro Tour career, including five Top 8s, by winning Pro Tour–New York with team Potato Nation. Mike has excellent intuition for bringing out the excitement of **Magic**, and he promotes cards that will create really exciting moments in gameplay. He loves the beatdown and encourages making awesome one-drops and two-drops that turn sideways and bash. I've seen Mike build every tribal deck under the sun, though he has a special place in his heart for the fierce, come-out-swinging style of Kithkin and Goblins.

I also want to emphasize the huge improvements to Lorwyn generated by some of our most dedicated *Lorwyn* playtesters, who were all in **Magic** R&D but weren't on this development team: Mons Johnson, Steve Warner, Noah Weil, and Erik Lauer. All four were constantly building and testing all kinds of combo, beatdown, control, midrange, and aggro-control decks in the *Lorwyn* Future Future League, helping us to see where we needed to make cards more powerful and where we needed to reign them in. I'll focus more specifically on these key playtesters and their personal styles in a future article.

### Beyond Baobab

Now I'd like to focus on the personal style of my preview card. Aptly enough for this column, the card was made not in design, but during development. Let's set the stage. The *Lorwyn* file was handed off with a very different three-color Treefolk legend named Baobab Thornton, who was designed at the end of July 2006. Here he is:

> Baobab Thornton  
>  GWB  
>  Creature - Treefolk  
>  0/7  
>  CARDNAME comes into play with any number of branch counters.  
>  Each Treefolk gets +1/-1 for each branch counter on CARDNAME.  
>  2: Add or remove a branch counter from CARDNAME.

That design is just okay. It plays a lot like the *Fourth* and *Fifth Edition* card Shapeshifter, which could have any power and toughness as long as they added up to 7. This guy pays a lot of mana to change his power / toughness instead of doing it during your upkeep, and he takes all other Treefolk along for the P/T-shifting ride. It's a downside that the card is so mathy; if you have three Treefolk out, and you start adding and removing branch counters from Baobab, it doesn't take long before you and your opponent both have to do a lot of adding and subtracting and bead counting and remembering every time you want to attack or block. In terms of power level, Baobab can be a 4/3 or a 3/4 for three mana. Both of those are better than you usually get for three mana, but not by a lot, and the triple-color mana cost is pretty restrictive. And sometimes you would want to pump him to 6/1, but that would kill a bunch of your other Treefolk, which was really annoying. Overall pretty ho hum. 

The good parts about this early design are that it's a fairly unique ability, he feels appropriately three colors, he helps all your Treefolk fight better, and in particular he lets all your 1/3, 2/4, 3/4 and 5/7 Treefolk fight a little better because he lets them trade in their toughness (which they have in abundance) for more power. A card as ho-hum as this does not pass muster for a three-color rare gold legend. The card was also too similar to a monoblack Treefolk in the set at the time. We flagged Baobab Thornton for replacement on September 22, 2006, a whopping three hundred fifty-seven days ago today.

By November 16th, *Lorwyn* development had been moving merrily along, and that monoblack treefolk witch had changed into something more awesome that wasn't very close to Baobab Thornton design anymore. No one wanted to go back to the original Baobab design, and we still hadn't found a good replacement design yet. In a memorable departure from normal hole-filling procedures, *Lorwyn* lead designer Aaron Forsythe, notorious designer / rules manager Mark Gottlieb, and I went down to the first floor cafe to fill this and a couple of other holes. What new rare gold Treefolk legend could we come up with that captured all the upsides of the old design, in some cleaner, more awesome way? What kind of power level could we put on a card that was rare, three colors and a legend? Once someone said it out loud, we knew we had our winner. Click here to show the three-color Treefolk legend that's actually printed in the set.

![Doran, the Siege Tower](https://i.ormos.uk/fc/03/fc0372fc752d1bca3ee7c108c2b8a87d44bb1aae3604c097f07d64d60980ec80.jpg) 

What a beautiful line of text. What sick numbers. It deals 5 damage in combat. It takes 5 damage to kill it. It costs three mana. Yup, this is as much of a three-mana 5/5 as you are ever likely to see in your life. What's the closest point of comparison? It's hard to even know where to begin to find something in **Magic**'s history that compares to a three-mana 5/5. Remember Standard and Extended powerhouses Ravenous Baloth and Loxodon Hierarch? On top of the lifegain, a lot of Baloth and Hierarch's value was their being fat 4/4s for four mana. If Doran the Siege Tower were solely fatter than Baloth and Hierarch (like being effectively 5/5 for four mana) or solely cheaper than Baloth and Hierarch (like effectively 4/4 for three mana), then Doran would definitely be a very attractive alternative choice to Baloth and Hierarch in ![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif) decks. In Constructed, dealing extra damage or having a significantly cheaper mana cost is usually more powerful than lifegain. But the thing is, Doran isn't solely cheaper than Baloth / Hierarch or solely fatter than Baloth / Hierarch. He's both cheaper *and* fatter than those two linebackers. Burning-Tree Shaman beat a lot of people up as a three-mana gold 3/4 with a symmetrical damage-dealing ability. How much more damage do you think you can deal with a three-mana 5/5? Jade Leech popularized fatty beatdown across *Invasion* as a four-mana 5/5 with a drawback. Doran the Siege Tower is a whole turn faster and doesn't have that drawback. What can you do with the extra turn you get from the cheaper mana cost? Hey, I've got an idea: How about 5 more damage?

Fortunately, bashing people as a three-mana 5/5 isn't enough to satisfy Doran: he's got two other amazing categories of tricks he can do too. 

 ![Ohran Viper](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Ohran%20Viper&options=) 

First, his ability reaches across your entire army. What's a fantastic way to accelerate out Doran the Siege Tower *and* get the three colors you need? I'm sure Bird of Paradise sprang to a lot of your minds as soon as you saw the card. You know, to get out your turn-*two* 5/5 creature. But Birds of Paradise isn't just Doran's perfect buddy because of the Birds' color-fixing and mana-acceleration abilities. When Doran is on the board, Birds of Paradise deal combat damage equal to their toughness too. So when the Birds are done speeding out Doran, they can fly in for a point a turn themselves. You know your Ohran Vipers? Well you just upgraded the old 1/3 Ophidian body to a ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) 3/3 that still draws cards. Forbidding Watchtower can deal an enormous 5 damage. And your little old Tarmogoyfs that were only 5/6 all start dealing 1 extra damage. If you start brainstorming high-toughness creatures that you can—for free—turn into *high-power* high-toughness creatures, you'll probably find a lot of seemingly normally costed creatures that go totally insane when Doran is on the scene. And let Doran be the first to mention that *Lorwyn* has some serious-business Treefolk creatures—about a dozen in all—and almost all of them have toughness higher than power. So all your 1/3s, 2/4s, and 5/7s suddenly act a lot like 3/3s, 4/4s and 7/7s.

The second category is that Doran's ability reaches across your *opponents'* entire armies. Except that they probably didn't plan ahead for the Siege Tower being on the board like you did. So your opponents' 2/1 Mire Boas and Soltari Priests? More like 1/1s. In older formats, watch opponents cry when their prized Giant Solifuge starts acting like a four-mana 1/1. And Doran's ability extends across power-pumping effects too. Just watch your opponent play Fatal Frenzy and have it do nothing at all. Well ok, their Fatal Frenzy still does one thing: make them cut their own guy for no benefit.

If you play Timber Protector ([previewed by Mark Rosewater](/en/articles/makingmagic/2007/09-10-a-lorwyn-lorwyn-situation)) a couple of turns after Doran the Siege Tower, the Timberwatch Protector plays as a five-mana 6/6, while Doran plays as a three-mana 6/6... who's indestructible. Lorwyn also gives each one of them a lot of other high-toughness Treefolk friends. And while Doran is already immune to Terror and most burn spells, Gaddock Teeg ([previewed by Rei Nakazawa](/en/articles/feature/2007/09-10-lorwyn-lore)) can make him immune to basically everything else.

### From Acorn to Oak

Fortunately, developing Doran wasn't quite as high-toughness as Doran himself. That November 16th, I typed him in like this:

> Gnarls Barkley  
>  GWB  
>  Creature - Treefolk  
>  0/5  
>  If a creature would deal combat damage, it deals combat damage equal to its toughness instead  
>  o2: CARDNAME gets +0/+1 until end of turn.

I was trying to find a ancient Treefolky legendy sounding placeholder name, something gnarled, and I realized that name of the band Gnarls Barkley randomly evokes Treefolkiness *two* different ways. How lucky. I mean what are the chances? Our templating team knew templating the ability would be a challenge, but found a way to work it out. People had fun both putting Gnarls in random decks and building decks around him. But he was obviously way over the line in power level. On December 6th, we brought his power/toughness down to 0/4 and kept the toughness-pumping. 

We played more and he was still way too powerful. Furthermore, another problem was that his toughness-pumping was so awesome by itself that it encouraged you to play him alone and pump all your mana through him, instead of playing other creatures that his ability would pump up. And we really liked the fun of him pumping other guys up. On December 12th, we cut the toughness-pumping, and kept his stats at a powerful three-mana 0/4.

Some people say card flavor doesn't affect power level. Those people couldn't be more wrong. Over Christmas break, maybe the Christmas Treefolk warmed our hearts, and several people independently thought that Doran had so much mechanical flavor for what an ancient Treefolk legend would do (ensuring that all battles would be determined on toughness alone) and he was so well-liked by playtesters, that 4 toughness wasn't good enough. On January 2 the *Lorwyn* team wished each other a happy New Year and moved Doran back up to 0/5. 

And that's the story behind the biggest zero-power beater ever. Long after his name in the file was changed to "Doran, the Siege Tower," we still call him Gnarls Barkley.

Next Week: A new *Lorwyn* preview card: A tribal take on a big set cycle staple.

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b>How many years have you been playing Magic?</b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>0-1</td>&#10;    <td>634</td>&#10;    <td>4.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>1-2</td>&#10;    <td>1360</td>&#10;    <td>9.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>3-4</td>&#10;    <td>2554</td>&#10;    <td>17.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>5-6</td>&#10;    <td>2310</td>&#10;    <td>15.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>7+</td>&#10;    <td>8112</td>&#10;    <td>54.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>14970</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

The biggest reaction here was a lot of people saying "Hey, why do the bubbles stop at 7+? I've played for 11 years, and I want to click an 11-12 bubble!" I also enjoy the street cred of having played for a long time, and I should have included more bubbles. To remedy that, here's a new version of the poll that breaks it down further:

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>How many years have you been playing Magic?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtgcom_dl2_howlong">&#10;                            <div>&#10;                              &#10;                              0-1<br>1-2<br>3-4<br>5-6<br>7-8<br>9-10<br>11-12<br>13-14<br>Over 14<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

### This Week's Poll

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>&#10;              <table>&#10;                <tbody><tr>&#10;                  <td>&#10;                 <b>If a friend wanted to buy something to learn Magic for the first time, what would you recommend?</b></td>&#10;                  <td> </td>&#10;                  <td>&#10;                    <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;                  </td>&#10;                </tr>&#10;                <tr>&#10;                  <td colspan="3">&#10;                    <table>&#10;                      <tbody><tr>&#10;                        <td>&#10;                          <div id="pollmtgcom_dl2_learn">&#10;                            <div>&#10;                              &#10;                              &#10;                              <i>Tenth Edition</i> Starter Game<br><i>Tenth Edition</i> preconstructed decks<br><i>Tenth Edition</i> booster packs<br><i>Tenth Edition</i> Fat Pack<br>Expert-level set preconstructed decks<br>Expert-level set booster packs<br>Expert-level set Fat Pack<br><b>Magic Online</b> cards<br>Another <b>Magic</b> product<br>Free downloadable interactive tutorial at <a href="http://www.playmagic.com/"><b>www.playmagic.com</b></a><br>None of the above<br></div>&#10;                            <div>&#10;                              &#10;                            </div>&#10;                            <div></div>&#10;                          </div>&#10;                        </td>&#10;                      </tr>&#10;                    </tbody></table>&#10;                  </td>&#10;                </tr>&#10;              </tbody></table>&#10;            </td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>