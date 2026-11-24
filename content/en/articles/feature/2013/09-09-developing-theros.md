---
id: h89rtq9c
kind: article
lang: en
path: /en/articles/feature/2013/09-09-developing-theros
title: Developing Theros
published: '2013-09-09'
column_slug: feature
column: Feature
authors:
- slug: eriklauer
  name: Erik Lauer
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    lang_detected: en
    capture_id: 1205746
    url: https://magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    captured_at: '2022-05-20 10:14:22+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    lang_detected: en
    capture_id: 1205746
    url: https://magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    captured_at: '2022-05-20 10:14:22+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    lang_detected: en
    capture_id: 1205746
    url: https://magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
    captured_at: '2022-05-20 10:14:22+00'
    rule: drupal.div_author
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/264
    lang_detected: en
    capture_id: 598084
    url: http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/264
    captured_at: '2014-04-15 02:57:12+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: h89rtq9c
  url: https://magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
  page_key: magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
  lang: en
  template: drupal
  captured_at: '2022-05-20 10:14:22+00'
  capture_id: 1205746
  wayback_url: https://web.archive.org/web/20220520101422id_/https://magic.wizards.com/en/articles/archive/top-decks/developing-theros-2013-09-09
- document_id: h89rtq9c
  url: http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/264
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/264
  lang: en
  template: aspx
  captured_at: '2014-04-15 02:57:12+00'
  capture_id: 598084
  wayback_url: https://web.archive.org/web/20140415025712id_/http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/264
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: h89rtq9c
  capture_id: 598084
  url: http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/264
  wayback_url: https://web.archive.org/web/20140415025712id_/http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/264
  captured_at: '2014-04-15 02:57:12+00'
  template: aspx
  sha256: 9b523019e0e6baad4d8b3850104d0212240feb571deff882528c18ca3b7ac743
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Plague Wind
  - Rusted Relic
  - Thoughtseize
  - Armored Skaab
  - Memory's Journey
  - Runic Repetition
  - Gnaw to the Bone
  occurrences: 12
---
Hello! I'm [Erik Lauer](https://web.archive.org/web/20140223104405/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Erik%20Lauer), and I was the lead developer on *Theros*. I've been on a lot of development teams over the years and have led quite a few as well. The most recent sets I led were *Innistrad*, *Return to Ravnica*, and *Modern Masters*. 

Today, I'm going to tell you some of the stories behind the development of *Theros*. But first, let's meet the development team: 

![](https://i.ormos.uk/a3/b8/a3b88e7d7f0d7e9bc111f4e1149c808d9a8720ad945e30ef48046e924f760e83.jpg)

[Doug Beyer](https://web.archive.org/web/20140518165222/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer) was the creative team member for *Theros*. In addition to making sure the set played well, he was responsible for making sure the alignment of the card file and the creative vision improved as the set was developed. 

  
  
 ![](https://i.ormos.uk/98/ff/98ff84c36158a8091193fe55e8d3028e6e766bb343fd8e5051e08a78fcb62548.jpg)

[Zac Hill](https://web.archive.org/web/20140420071339/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Zac%20Hill) led development on ***Magic** 2013* and *Dragon's Maze* and was on multiple development teams in his years here. Up until about a year ago, he wrote the Latest Developments column here on DailyMTG. 

  
  
 ![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg)

[Dave Humpherys](https://web.archive.org/web/20130913033631/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Humpherys) is the senior development manager and oversees the rest of the development team. He has served on numerous development teams and was also the lead developer of *Avacyn Restored* and *Gatecrash*. 

  
  
 ![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

[Tom LaPille](https://web.archive.org/web/20130921234759/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Tom%20LaPille) is an experienced developer, having been on multiple development teams going back to ***Magic** 2010* ; he also led development of ***Magic** 2012* and *Dark Ascension*. Tom also used to write the Latest Developments column. 

  
  
 ![](https://i.ormos.uk/f8/3b/f83b7c2d164a18a665378b13e7adec05a979b390fc07e360fae3fdfa6f560cab.jpg)

[Shawn Main](https://web.archive.org/web/20130913033636/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Shawn%20Main) was the design-team member for *Theros*. In addition to the play of the set, he was in the meetings to explain why design made certain choices. That way, development could balance the design goals for the cards with the development goals at hand. Shawn is a frequent member of my development teams, having been on *Return to Ravnica*, *Modern Masters*, and *Theros*. 

  
  

### Tales of Card Development

If you have been following [the previews](https://web.archive.org/web/20140413152532/http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/theros/cig), you might wonder how some of the cards ended up with their rules text. Here are some tales of card development. 

Design works on a set, then there is a "devign" period where design continues to work on the set, but with frequent feedback from development. Finally, design hands the set off to development. During development, some cards sail through with little or no changes, some have significant changes, and some others are replaced with entirely different cards.

![](https://i.ormos.uk/e4/4a/e44a285880fe3b1a5ed0bb9b6b263bd6a4c93e7a27d2d4d157ed3b2d9c774e4a.jpg) 

  

When development started, Ordeal of Purphoros was:

> Passionate Journey  
>  R  
>  Enchantment  
>  Enchant creature  
>  Whenever enchanted creature attacks, put a +1/+1 counter on it.  
>  As long as enchanted creature has three or more +1/+1 counters on it, it has trample.

I thought the card had potential. [Mark Rosewater](https://web.archive.org/web/20140409114659/https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater) liked the card a lot. Some members of the development team were not fond of this design. If you couldn't kill the creature before it got three +1/+1 counters, you only have a couple turns to draw a removal card before the enormous creature kills you. Mark wanted the set to have a feeling of accomplishment. I suggested changing it so the enchantment died (so the creature would stop growing), but you would get a handsome reward. The rest of the development team liked the change, so we worked on the proper reward. 

![](https://i.ormos.uk/8c/8a/8c8a6cfc7627ee231722be79ab19936c292e9346f07a69c0b9dc7b01bb659646.jpg) 

  

When development started, Polukranos, World Eater was:

> Fight O' Hydra  
>  2GG  
>  Monstrous—XGGGG: Put X +1/+1 counters on CARDNAME. It fights all creatures target player controls. Activate this ability only once each game. (This ability doesn't work.)  
>  4/4

I was caught off guard by the reminder text, so I read the development comments and found:

> Del 7/6: Waiting on a replacement card.  
>  Del 7/23: Still waiting on a replacement card.

Ah, that is from Del Laugel, the lead editor. It turns out that only two creatures can fight. I asked Mark what he wanted it to do, and he said he wanted it to fight each of an opponent's creatures. So I changed the text to:

> Monstrous—XGGGG: Put X +1/+1 counters on CARDNAME. It deals damage equal to its power to each creature target player controls, then those creatures deal damage equal to their power to CARDNAME. Activate this ability only once each game.  
>  Del 7/31: Yea, a working card!

I talked to Mark about this, and he wanted it to fight each of their creatures in order. Order? I could not think of a way to fit all that on a card, so I asked editing. This seemed to entertain them, but we stuck with fighting all of the creatures at once.

The new problem was that the card didn't play very green. It tended to kill every creature on the other side of the board, and then die itself. It was more like the card Plague Wind than a big green creature. We went through several iterations. After a while, I thought perhaps too much of the strength was in the activation. So we tried toning down the activation but making the Hydra a base 5/5. It was a lot more fun to play, and it seemed to fit green a lot better. 

### Gods and Their Weapons

The design team put a lot of thought into the Gods, but the process to get them to where they are now as cards was very long. The best part of the designs were the stories of what they gods were about, and how they related to the block. There were also some interesting designs. For example, the original black God was:

> Daimon  
>  3BBB  
>  Legendary Enchantment Creature – God  
>  Deity (*If this God would enter the battlefield from anywhere other than Nyx, put it into Nyx instead. Exile it from Nyx when your devotion to its color is 0. At the beginning of combat, if your devotion to its color is 5 or more, you may put this God onto the battlefield with haste, then return it to Nyx at the end of combat.*)  
>  As long as CARDNAME is in Nyx or on the battlefield, you may cast creature cards from your graveyard. 
> 
> 5/4

The part of the card that makes this God feel different from the other Gods is "you may cast creature cards from your graveyard." That is all the room left for the text on the card (and that is at a smaller-than-normal font). The cards were interesting to play, but the problem was that the block is supposed to have fifteen gods, and I was concerned that this amount of text would not lead to fifteen satisfyingly different designs.

I talked to a lot of people to see what they liked or did not like. What did they expect from Gods? The main thing people associated with Gods was immortality. People also liked that a God would only attack or block if you had enough devotion. Commander players were excited that Gods could be commanders.

I wanted to keep all that but reduce the length of the text. The most natural word to signify immortality is "Indestructible." While the Nyx text matched the creative story, it was too complicated. I thought of the *Scars of Mirrodin* card Rusted Relic. With the previous God design, if you cast a spell that killed all your opponent's creatures, that might get the God, too (unless your opponent had noncreature permanents that provided devotion). I wanted there to be a larger distinction between Gods and other creatures, so I removed that text. Those changes left more room for other text. 

The first draft was:

> Daimon  
>  4B  
>  Legendary Enchantment Creature – God  
>  Intimidate  
>  CARDNAME is indestructible.  
>  At the beginning of your upkeep, target opponent loses X life, where X is your devotion to black.  
>  As long as your devotion to black is 5 or less, CARDNAME isn't a creature  
>  8/5

We played with this version and found that, while The template felt right, the rules were wrong. By the time this creature could attack, you were draining your opponent for 5 life per turn; attacking for 8 was superfluous. While the Gods still clearly needed work, I thought we were on the right track. 

We had one more iteration of the black God that allowed you to regenerate any creature by discarding a card. It was super cool but so frustrating. Basically, along with any card-drawing spells, it was an indestructible enchantment that made all your other creatures indestructible.

Eventually, we got to where we are today:

![](https://i.ormos.uk/63/65/6365cdb55ee40e99739d7c759a796b9fe155b64d4fd9230d03a78248fd246b78.jpg) 

  

The weapons had a different problem: the type line!

Design made:

> Sun Javelin  
>  1WW  
>  Enchantment Artifact – Equipment  
>  Equipped creature has "T, Unequip CARDNAME: CARDNAME deals X damage to target attacking or blocking creature, where X equals your devotion to white."  
>  Equip 6

Creative insisted these had to be legendary. Editing pointed out that this would not fit in the type line; we would need a new frame with two lines. However, we were already using new frames, so I wanted to cut a word.

I asked Rules Manager [Matt Tabak](https://web.archive.org/web/20140424061704/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Matt%20Tabak) for advice, and he said if it is Equipment, it must be an artifact. The development team decided that we already had Auras to attach to creatures. By not having these be Equipment, they would feel more distinct in our environment. We decided that each weapon should have a tap ability, because it is an artifact, and a static ability, because it is an enchantment. 

Now that we had our basic ideas of what these cycles would hold, it was time to design some cards.

![](https://i.ormos.uk/1b/44/1b44435b457f78186d9eb6dad78927139ed944c72d586c4a9701b016159f74bb.jpg) 

  

I like to take a week off from our normal development to form "mini-teams." Each member of the set's development team takes a coherent piece of the file and forms a team with three other members. There are several things I like about this. First, it makes the different pieces of the set feel more distinctive. Second, it allows people who might not have time to be on the full development team to bring their ideas. Finally, it allows less-experienced developers a chance to lead for one week, where experience can be gained but the stakes are lower. Each team added a lot to the set.

I led the Gods and Weapons mini-team. The other team members were all talented game designers, but each brought other aspects to the team as well.

[Mark Rosewater](https://web.archive.org/web/20140409114659/https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater), **Magic**'s head designer, brought the vision of what each god was supposed to do. Because he is so busy, he didn't make the last meeting. 

[Aaron Forsythe](https://web.archive.org/web/20140127032524/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Aaron%20Forsythe), director of **Magic** R&D, replaced Mark in the last meeting. In addition to designing cards, if Aaron doesn't like what we end up with, he talks about how to go about making cards he does. Fortunately, that didn't happen this time! 

Charles Rapkin, organized play project manager, is a very experienced and entertaining Commander player. Since the Gods are legendary creatures, he made sure he thought they would be fun additions to the format.

[Ryan Spain](https://web.archive.org/web/20130913040206/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Spain) is a prolific drafter. While these cycles are mythic rares and rares, there are ten cards total, so overall they will have an impact on draft. Ryan added focus to whether they would be appealing for drafting without being oppressive during play. 

Finally, besides being the lead developer, I took the role of the competitive player. Would I want to try building with these cards, and do the weapons make sense in decks with the Gods?

We made ten cards, the five Gods and their respective weapons. Of the weapons, I was most concerned by Nylea's. I wasn't sure we would have a good bow—a bow sounds like a great killing device, but green isn't supposed to be the best at killing creatures. However, Aaron had an awesome idea of having four abilities for the four seasons! Here is what we ended up with:

![](https://i.ormos.uk/f7/59/f75911a0a9c11277f218b16ea819442d3b34a948688b691fa03b8a3eae92f6f1.jpg) 

  

Of course, these were essentially initial designs, and they changed as we played with them. But this team made designs with pride.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/af/d5/afd5096eabc0a5b73554d0642cb8609e1b5777ddd5df3f0a4861cfa4a1467ac0.jpg">&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/2c/25/2c258319edcadc06b07cb6a58a06e7029456a5b679d51d3be8c559c36ca6d891.jpg">&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### Dealing with Enchantments in Black and Red

Neither black nor red can remove an enchantment from the battlefield. I wanted red to be the deck that tried to use speed to overcome enchantments. Black would use a more controlling strategy. Ordinarily, I would think Thoughtseize is too strong for Standard; since it can take any spell, it doesn't matter as much what spells are in the new set or in a particular deck. Thoughtseize pushes the game more toward attrition and card advantage than is typically correct. However, I think it can be right on occasion, and this is such an occasion. 

![](https://i.ormos.uk/2f/4b/2f4b0553ad65ea4ce70710ef8e1756c2ed922dc5af2466f0bb4e5a0050b2d728.jpg) 

  

Unfortunately, as we started [FFL](/en/articles/latestdevelopments/2013/08-16-days-of-future-future-part-2), it became apparent this was not enough. There are artifacts, enchantments, *and* Planeswalkers in *Theros*, and black couldn't remove any of them. So, weeks of [FFL](/en/articles/latestdevelopments/2013/06-14-days-of-future-future) were spent making the black decks faster until they looked more like red decks. I decided something had to change, and I had an idea what. I thought about it some more and decided I really needed to ask Mark for his advice. 

When Mark handed *Innistrad* off to development, he had the observation that green rewards you for having creatures in your graveyard, and blue has the most milling, so the green-blue draft deck could rely on self-milling. Over the course of development, we added creatures such as Armored Skaab that mill you when they enter the battlefield; as well as cards like Memory's Journey to shuffle cards from your graveyard back into your library; Runic Repetition to get back your exiled flashback cards, including Memory's Journey; and Gnaw to the Bone, so you can live long enough to enjoy your engine. When it worked in the real world, I thought this would excite Mark's Johnny sensibilities. Instead, he was disappointed that I had put Runic Repetition in the set. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Runic Repetition" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Runic%20Repetition&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Memory's Journey" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Memory%27s%20Journey&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

I knew Mark generally didn't like getting cards back from exile, but I had thought that this minor exception added enough to the play of the set. After *Innistrad*, then, I learned to check with Mark instead of circumventing his guidelines. 

![](https://i.ormos.uk/c8/44/c844c773dc08413c4545ddc0984e6c071b1ed7a5c73ce4eac26c8984c00f9a9c.jpg) 

Art by [Ryan Pancoast](https://web.archive.org/web/20130909000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22ryan%20pancoast%22])

 

Since Mark maintains the color pie, I told him about black's problems in the [FFL](/en/articles/feature/2011/10-17-greetings-from-the-future-future). Mark paused, then said, "Black can kill Planeswalkers." I told him a card that just killed a Planeswalkers wouldn't be strong enough for Standard, even at one mana. He said it was okay to make a card that could kill a creature or a Planeswalker. I expected that. Then he said something I wasn't expecting: killing Planeswalkers is a rare event. 

![](https://i.ormos.uk/b6/bf/b6bf51ae78d7a30ce36ed46f829cb91e826300ad542a867ab36d9bfee102aa60.jpg) 

  
 

We played with Hero's Downfall in the [FFL](/en/articles/latestdevelopments/2013/06-14-days-of-future-future). We found that the flexibility of the card gave black the tools to deal with enough its problems that it could resume playing a controlling strategy. However, there were also times that removal that cost less mana worked better in decks. That was important to me, and it made Hero's Downfall a successful addition to *Theros* and to our Standard environment. I hope you enjoy it as much as we did! 

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

[![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_Prerelease_Details_Static.png)](/en/events/2008/prerelease-facts/worldwide-prerelease-tournaments) [![](http://media.wizards.com/images/magic/daily/footers/THS/EN_THS_ArticleFooter_Prerelease_Minisite_Static.png)](https://web.archive.org/web/20140515230337/http://www.wizards.com/Magic/TCG/Products.aspx?x=mtg/tcg/products/theros) 

  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/slice2.jpg)

 

![Erik Lauer](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg "Erik Lauer")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Erik Lauer</b>&#10;        <br>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130909000000/http://www.wizards.com/company/emailtoauthor.asp?author=Erik%20Lauer&amp;amp;headline=[Developing%20Theros]">Email Erik</a>&#10;      </td>&#10;      <td>&#10;        <a href="https://web.archive.org/web/20140110115418/http://www.wizards.com/magic/magazine/archive.aspx?author=erik%20lauer">Author Archive</a>&#10;        <br>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Erik Lauer is a senior game designer who works on final game design and development. Recently, he has led the *Return to Ravnica*, *Modern Masters*, and *Theros* development teams. 

 