---
id: v5rzycs7
kind: article
lang: en
path: /en/articles/feature/2014/04-14-a-developmental-journey
title: A Developmental Journey
published: '2014-04-14'
column_slug: feature
column: Feature
authors:
- slug: dave-humpherys-4a7b522e
  name: Dave Humpherys
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    lang_detected: en
    capture_id: 619195
    url: https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    captured_at: '2022-06-25 02:33:18+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    lang_detected: en
    capture_id: 619195
    url: https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    captured_at: '2022-06-25 02:33:18+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    lang_detected: en
    capture_id: 619195
    url: https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    captured_at: '2022-06-25 02:33:18+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    lang_detected: en
    capture_id: 619195
    url: https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
    captured_at: '2022-06-25 02:33:18+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: v5rzycs7
  url: https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
  page_key: magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
  lang: en
  template: drupal
  captured_at: '2022-06-25 02:33:18+00'
  capture_id: 619195
  wayback_url: https://web.archive.org/web/20220625023318id_/https://magic.wizards.com/en/articles/archive/feature/developmental-journey-2014-04-14
- document_id: v5rzycs7
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/295
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/295
  lang: en
  template: aspx
  captured_at: '2014-04-26 01:08:47+00'
  capture_id: 601467
  wayback_url: https://web.archive.org/web/20140426010847id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/295
- document_id: v5rzycs7
  url: https://magic.wizards.com/en/articles/archive/uncharted-realms/developmental-journey-2014-04-14
  page_key: magic.wizards.com/en/articles/archive/uncharted-realms/developmental-journey-2014-04-14
  lang: en
  template: drupal
  captured_at: '2022-05-20 02:24:21+00'
  capture_id: 1216275
  wayback_url: https://web.archive.org/web/20220520022421id_/https://magic.wizards.com/en/articles/archive/uncharted-realms/developmental-journey-2014-04-14
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: v5rzycs7
  capture_id: 601467
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/295
  wayback_url: https://web.archive.org/web/20140426010847id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/295
  captured_at: '2014-04-26 01:08:47+00'
  template: aspx
  sha256: 017a540b2fd0125868a2062ec01ccd2ab37cd39d292ea2e6352ff40486c77bb5
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Heartbeat of Spring
  - Shadowmage Infiltrator
  - Ghor-Clan Rampager
  occurrences: 4
---
I'd like to share some of the most notable changes of course that *Journey into Nyx* took through development, but first, let's meet the *Journey into Nyx* development team. 

  

### Dave Humpherys (lead)

![](https://i.ormos.uk/62/65/6265a4d0e30ea9b06a914b492759a2bf1ecbe8471261802d1cdfca262427bfb4.jpg)

My role at Wizards of the Coast is to manage the development team for **Magic** R&D. I've led set development for *Gatecrash* and *Avacyn Restored*, as well as for the upcoming *Conspiracy*. I'll boast here that I was inducted into the **Magic: The Gathering** Pro Tour Hall of Fame way back in 2006. 

  

### Erik Lauer

![](https://i.ormos.uk/1c/76/1c76b8f51726ca5146415f2b1cacd688a94bff52ba816fdb8323805f2b4df57e.jpg)

While I manage the development team, Erik is the technical lead for development in **Magic** R&D. He's most recently led set development for *Theros*, *Return to Ravnica*, *Innistrad*, and *Modern Masters*. He was the "strong second" on this set. This is a role we've recently been more formally assigning to someone on each team to serve as the backup to the lead, either to help share experience, as in his case, or in other cases for someone more junior to gain insights into leading a set in the future. In this case, he played an especially crucial role on the development of this set, as we'll get to in this article. He was also the representative from the *Journey into Nyx* design team. 

  

### Ian Duke

![](https://i.ormos.uk/76/54/76547bdd4a875649c2dcda79a69d843378c9c4ea12e06a80caf0d99dbee11a4d.jpg)

Ian has been working with **Magic** R&D development for a couple of years. We are still trying to figure out if he or his brother, Reid, is the stronger player. Ian was the lead developer for [*Vintage Masters* for **Magic Online**](https://web.archive.org/web/20140512215325/http://www.wizards.com/magic/magazine/article.aspx?x=mtg_daily_other_10212013_vintagemasters). He also helped create the vision for the Clash Pack and led development of [**Magic** 2015's Clash Pack](/en/articles/arcana/2014/03-05-introducing-m15s-clash-pack) . 

  

### Tom Jenkot

![](https://i.ormos.uk/e2/d6/e2d6b4a23ec49b6004df9d194a99c1739d85a06c362bca24e048cda05ad35964.jpg)

Tom comes to us from the web team, where he directs a group of graphic designers working on DailyMTG and the visuals of the site overall. He also worked on the packaging design for the *Theros* block and wrote flavor text for *Theros*. *Journey into Nyx* is the first time he contributed to the development of a set. Besides having a soft spot for [minotaurs](https://web.archive.org/web/20140419052945/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Tom%20Jenkot), he is a longtime casual player, which provided a unique perspective on the team. 

  

### Ken Nagle

![](https://i.ormos.uk/bb/24/bb242f94967ffa62f8f696d33e5b58581f523b7f503daefb80a20fffa05ac7c4.jpg)

Ken is on the design team within **Magic** R&D. His most recent lead-designer credits are for *Born of the Gods*, *Return to Ravnica*, and *Commander*. Ken was also the lead designer for all of [the Challenge Decks for the Hero's Path experiences](/en/articles/feature/2013/09-16-heros-path-faq-2#challenge) during *Theros* block. If you wonder where all of the large creatures in any given draft vanished, especially the green ones, it's best to look in his card pool. 

  

### Three Pillars

It's been a few years since we've finished off a block in our formally traditional Large-Small-Small set model. It had been long enough that we reevaluated many of the assumptions about what this set should deliver. Beyond our goals to help convey the changing story in the block, we also had many ideas for tweaks to overall play patterns to keep things new. One of the most significant changes we ultimately made as the development team was to return more mechanics than design had initially handed off. At the risk of there being too many things going on, we felt we needed to revisit certain mechanics to round out decks for Limited, casual, and competitive.

As with the rest of the block, let's take a look at the pillars of our focus for design and development: Gods, Heroes, and Monsters.

**Gods** 

There wasn't really much doubt that we'd round out the fifteen Gods in the block with the five enemy-colored Gods. There also wasn't much reason to have these differ from the mold established by the two-color Gods for the allied-color pairs in *Born of the Gods*. From there, it was largely a matter of trying to tread some new ground while hitting the creative identity of the gods. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/a7/5b/a75b1975f63b5cae9aa62e4808607046e2cb35179001414bef439809ccef588f.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/89/b4/89b4a06c3abeee8dee9875b72908d2d3177582bf37d4cda8dd57e3b5e5b78ac7.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Beyond the Gods, we wanted to have a lot of change when it came to anything enchantment related that could be associated with the gods and Nyx. We were focusing on playing up the heightened conflict between the gods and the mortals. This led us to focus on including two new mechanics, one for each side of the struggle. [Constellation](/en/articles/feature/2014/04-07-mechanics-of-journey-into-nyx#anchor1) felt like a natural fit. It rewarded you for playing each and every enchantment, including the card with constellation itself. The more cards with constellation you have on the battlefield, the more and more crazy things can get. The implementation of the mechanic didn't really change at all from design. That's not to say there wasn't a lot of reworking of individual cards to make sure the potentially repetitive nature of the mechanic stayed fun in both Limited in Constructed. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/3c/62/3c6275c8d9a2a764c7a9f74525ce9fa2555d457f71a16a9e410c1f696f7d4398.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/b4/e0/b4e0ebc51cecd84f3b6faf4f54c36e7c3c9028dffd24486021d927fa29ec5f0f.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Bestow was a relatively big challenge. Since the gods were battling the mortals, there was a desire from design for these to largely be negative Auras. During design, a bestow creature might, for example, make the enchanted creature gain defender. If that creature eventually blocked, the bestow creature would take your side as a defender. Design didn't have these bestow creatures granting their power/toughness bonuses like they did earlier in the block. This change was deemed too odd by most players here. Also, there wasn't much incentive for your opponent to block in the example above, so you'd rarely get your creature back. When it looked like we might abandon the malevolent bestow creatures for something more straightforward, I thought we should try them with drawbacks but also with the stat bonuses. We then reworked the drawbacks accordingly so you'd at least occasionally put them on your opponent's creatures. Given their drawbacks, we could cost them and their bestow costs more aggressively.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/4f/75/4f754e389792bb4fa4860f02bbde012b87ac3507a2cde16a58ca24da01f37dbe.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/e8/cd/e8cd93249fccaa67da268316423a769ca3e562bd4eca2de7d4fe3f2db7b0db26.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*Born of the Gods* started toying with the space of more enchantment creatures than the Gods and the bestow creatures. I spent a lot of time thinking about what else we could add. In my free time, I'd search through old cards to find enchantments that could be "creature-ified" and for creatures that could have made sense as enchantment creatures. Many of these haven't been previewed yet, but keep an eye, or ear, out for them, and think about their inspirations. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/f3/76/f376f369d081e16c675492f32947386868425de3c1d0b933eb17d773ad6ba7cb.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Pyrostatic Pillar" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Pyrostatic%20Pillar&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

Since *Journey into Nyx* was the final payoff for an enchantment-heavy block, I also looked for other new cool and fun things to do with enchantments. I'd been on the development teams for both *Theros* and *Born of the Gods*. During each of those teams, I'd pitched the idea of flash enchantments, with idea being that they'd all be mutually beneficial symmetrical effects like Heartbeat of Spring, except now you might have the first chance to use them. They didn't make it into the earlier sets, but I was determined have others playtest them here. We were having a hard time finishing out the cycle and eventually decided it was best to loosen up the cycle a bit and simply find enchantments that would be the most interesting if they had flash, rather than restricting these all to symmetric effects. These cards were exciting a lot of our internal playtesters and I'm happy how they turned out. I'm also pleased with how our creative team tied them all together as dictates of the gods. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/de/b1/deb1ca7b4be9e61296990b95b853b26ede148097b9c0c11898fb72d6df5e8c7d.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/7b/16/7b1635c244bd9d36d6462aa50d107afdc8ae4d6bd8a4d3425747bba68bcca00f.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

**Heroes** 

Before I dive into the many changes that took place on the mortal side of things, let's take a look at one of my favorite cards in the set and my preview card for today. While the card features no new mechanic, it feels a lot like a hero card in the play style. It is a card that came through from design, from [Ethan Fleischer and his design team](/en/articles/feature/2014/04-07-my-journey). It entered development as a ![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif) 2/4 creature. I found the card adorable and wanted to see it in action earlier in games, so two weeks into development I changed the card to a ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif) 1/4. Two months later, Erik Lauer had taken control of the card file for me at my request for a few weeks. Erik, who incidentally might have been the initial designer of the card, then made another significant change to the card's game play; he made the card into a ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif) 1/3. He did so on a special day in my life. On that day, my first—and currently only—child was born. So, apparently, Erik went immediately to task in helping lead changes for the file in my absence. A week later he also gave the card trample—a bit unusual for a 1/3 creature, you might think. 

Now that I've teased the card, for those of you who haven't already clicked on the link below, think of what you'd expect of a red version of Shadowmage Infiltrator. How about a mythic rare one? It uses mechanical space that we've explored for red on at least one other high-profile red card. Now click here to see how you think we did. 

![](https://i.ormos.uk/4b/68/4b6857ff4bb6191da78e0ce8885dc5d32d22feb429c8ff68028a1742cac3b204.jpg) 

  

When I first saw these changes the team had made while I was out, I was very excited to try this card. All through development, I continued to expect that we might have to weaken the card on some axis, but the card continued to play beautifully. Prophetic Flamespeaker was versatile and played satisfyingly with a number of recent mechanics and cards, including—probably most notably—Ghor-Clan Rampager. He could alternatively be explosive or be a continuous source of extra resources. In any case, he generated a lot of excitement each turn he survived on the board. 

While I was out on paternity leave, Erik also started trying out a new mortals' mechanic. Between design and development time, we tried quite a few different mechanics. We knew what we wanted from the mechanic in general. 

We foremost wanted something that would pair well with the heroic mechanic. We were particularly interested in a way for players to use extra mana in the late game, since there weren't as many outlets for mana as we'd like. We also wanted, with this set, for there to exist greater incentives for "going wide"—that is, for having a bunch of creatures in play rather than piling evermore Auras on a single creature on your side. We wanted to encourage going wide to provide more game-play strategies and to play up a better sense of a war between many individuals on the mortals' side against the gods' side. Finally, we were interested in a mechanic that made great one-shot moments, since there were a number of mechanics creating incremental repetitive effects already present in the set and block. 

The [strive](/en/articles/feature/2014/04-07-mechanics-of-journey-into-nyx#anchor2) mechanic really hits all of the goals very well. We then made a lot of cards that target your own creatures to maximize getting as many heroic triggers as possible. We also made cards geared to going after your opponent's permanents to give the mechanic more scope and appeal. Fortunately, our other previous mechanics had enough similarities in goals that we could use a lot of the earlier general card designs. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/ee/33/ee33afee5f1c28e98fa057f82320159a737b6809c7dcd37a1a3c00f56c660ea6.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/c4/a6/c4a64f1fa34acee9aceb2c537b8fa1624a17c3b565bc1453c3599684be1b71a1.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

On the mortals' side of things, we also chose during development to return with inspired. As we finished up developing *Born of the Gods*, we realized there was more space to explore with inspired and we felt it was important to provide more tools for inspired drafters, especially for the sake of the blue-black color pair, and for Constructed. 

**Monsters** 

Much of the new excitement for the set was centered around building up the conflict between the mortals and the gods. But what about the monsters? There were a lot of cool designs that were coming from the design team, but there wasn't as much coherence to the monsters as in the earlier sets in the block, where, among other things, they were tied together by mechanics.

After a number of Limited playtests, we decided we needed to do something more with monsters. We didn't want to add another new keyword mechanic, though. Could we justify returning yet another mechanic to the set, in terms of complexity? First off, there was the question of which mechanic to return. While tribute led to some very exciting individual monsters, it lends itself less well to cohesive deck strategies in Limited and Constructed. Monstrosity cards encouraged you to ramp rewarded you for having lots of mana. As we did more and more Limited playtests without monstrosity, the lack of reliable outlets and rewards for ramping were quite noticeable. Adding monstrosity back into the colors we wanted promoted monster-based strategies significantly.

The design had handed off a number of exciting monster cards that cared about the number of basic lands their controller had, corresponding to that creature's color. The development team liked these so much that we filled out the cycle for all colors across uncommon and rare. These cards were another way to highlight monsters and to have them both reward lots of lands in play and to reward potentially finding homes form them in monocolor devotion decks for Limited and Constructed.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/6a/1a/6a1adeedd7e1e93926a2cce7c988831d8bcd308f5931b0f2d03fd9e1d6900574.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/b9/d8/b9d80f7c1643a99b320f60c5b4e2be4db29e9b966cabaa47a50cb5e7b0201661.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

When all was said and done, for our work in the set, we did our best to pack it with a lot of cards and themes for a lot of players. There's hopefully plenty of different cards for you to latch on to. Best of luck exploring the new set. We hope you enjoy it.

Thanks for reading,  
 Dave Humpherys 

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/JOU/EN_JOU_ArticleFooter_Prerelease_Details_Static.png)](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments) [![](http://media.wizards.com/images/magic/daily/footers/JOU/EN_JOU_ArticleFooter_Prerelease_Minisite_Static.png)](https://web.archive.org/web/20140427050043/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/journeyintonyx) 

  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Dave Humpherys](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg "Dave Humpherys")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Dave Humpherys</b>&#10;        <br>&#10;        &#10;        <br>&#10;        <a href="https://web.archive.org/web/20140414000000/http://www.wizards.com/company/emailtoauthor.asp?author=Dave%20Humpherys&amp;amp;headline=[A%20Developmental%20Journey]">Email Dave</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20140110115411/http://www.wizards.com/magic/magazine/archive.aspx?author=dave%20humpherys">Author Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Dave Humpherys has been managing the development team for **Magic** R&D since 2010. He led development for the *Avacyn Restored* and *Gatecrash sets*. He was inducted into the **Magic** Pro Tour Hall of Fame in 2006. 

 