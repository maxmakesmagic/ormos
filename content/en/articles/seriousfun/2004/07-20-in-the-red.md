---
id: 0a222aa6
kind: article
lang: en
path: /en/articles/seriousfun/2004/07-20-in-the-red
title: In The Red
published: '2004-07-20'
column_slug: seriousfun
column: Serious Fun
authors:
- slug: anthonyalongi
  name: Anthony Alongi
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    lang_detected: en
    capture_id: 1179783
    url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    captured_at: '2017-09-18 04:53:15+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    lang_detected: en
    capture_id: 1179783
    url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    captured_at: '2017-09-18 04:53:15+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    lang_detected: en
    capture_id: 1179783
    url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    captured_at: '2017-09-18 04:53:15+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    lang_detected: en
    capture_id: 1179783
    url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
    captured_at: '2017-09-18 04:53:15+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 0a222aa6
  url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
  page_key: magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
  lang: en
  template: drupal
  captured_at: '2017-09-18 04:53:15+00'
  capture_id: 1179783
  wayback_url: https://web.archive.org/web/20170918045315id_/https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
- document_id: 0a222aa6
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/aa133&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/aa133
  lang: en
  template: aspx
  captured_at: '2009-06-03 19:22:27+00'
  capture_id: 252829
  wayback_url: https://web.archive.org/web/20090603192227id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/aa133&print=true
- document_id: 0a222aa6
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/aa133
  page_key: wizards.com/default.asp?x=mtgcom/daily/aa133
  lang: en
  template: classic_asp
  captured_at: '2005-02-27 06:11:56+00'
  capture_id: 1918768
  wayback_url: https://web.archive.org/web/20050227061156id_/http://www.wizards.com/default.asp?x=mtgcom/daily/aa133
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0a222aa6
  capture_id: 1179783
  url: https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
  wayback_url: https://web.archive.org/web/20170918045315id_/https://magic.wizards.com/en/articles/archive/serious-fun/red-2004-07-20
  captured_at: '2017-09-18 04:53:15+00'
  template: drupal
  sha256: 690438f2e0f58f69f99334776dd8e3b3cd8fea2ebe6999aefd3e7726b0b7a457
render_recovery: []
---
## The math of Magic's hottest color

Those of you with some accounting experience (or who happen to play with numbers in Microsoft Excel a lot) know that spreadsheets show negative numbers differently. Positive numbers show as black, while negative numbers show as red. The crimson ink or pixels make clear one thing: these numbers are in trouble.

Red is a warning, in countless natural and man-made contexts. It is an indicator that something is in danger. In **Magic**, that something is your opponent's life total.

### Hot Little Numbers

![](http://archive.wizards.com/global/images/mtgcom_daily_aa133_picMain_en.jpg)*[Fireball](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball), art by Dave Dorman*

There are several different ways to win a game of **Magic**. With the exception of a few coin flip cards, red only cares about one: taking the opponent(s) from 20 to zero life. No color is as focused on this path to victory as red. The aggressive creatures, mass destruction, and direct damage all converge on a single goal. When it comes to your opponent, double digits are bad. Single digits are better. Negative numbers are best.

Some players (usually those a bit overly enamored of blue) mistake this focus for simple-mindedness. *Anyone*, they say, can deal three damage to the head with [Lightning Bolt](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt). *Anyone* can set off a massive [Earthquake](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earthquake) for X. *Anyone* can throw a [Ball Lighting](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ball+Lighting) at you. *Anyone* can set off a [Bloodfire Colossus](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodfire+Colossus).

Well, actually, no. Not *anyone* can do those things. Just those people smart enough to play red.

But red isn't just a smart choice because it's often the most direct route to victory. It also has significant depth because of the “new” math it forces on your opponents. In multiplayer, this math gets even more complex, and that's where we'll be spending our time today.

On math problems, that is.

Don't forget to show your work!

### Math Problem #1: Haste

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. Meanwhile, an airplane from Orlando takes off anytime on Monday or Tuesday and beats both trains to Chicago. Dejected, both trains stop halfway and return home. *Why does anyone take a train?*

A typical group game of **Magic** involves a fairly predictable push and pull of attack and defense. Players generally look at the opposing army with the largest number of (blockable) creatures, and then maintain enough blockers to maintain a respectable life total. Normally, three available attackers means you want to keep at least two good blockers back.

Once a player knows how many blockers she wants to hold back, she can spare the rest for an assault somewhere.

![](http://archive.wizards.com/global/images/mtgcom_daily_aa133_pic1_en.jpg)

For example: In a three-player “creatures only” game, Player A has a [Wall of Diffusion](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Diffusion) and a [Hill Giant](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hill+Giant), Player B has a [Fog Bank](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog+Bank), and Player C has three [Trained Armodon](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trained+Armodon)s. Everyone's at 4 life, has six lands of the appropriate color, and no cards in hand. Does anyone attack during their turn? If so, whom?

Player A is unlikely to attack with the [Hill Giant](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hill+Giant): it will either tap uselessly against the [Fog Bank](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog+Bank) or trade with an elephant, leaving Player C the opportunity to deal 3 damage on her turn by swinging with both remaining elephants.

Player B never attacks, because he's playing blue. Bleh.

Player C may attack either opponent, with minor risk. Three elephants would have to assault B for a kill; two would be enough to deal serious damage while holding an elephant back to keep an eye on that Giant. Alternatively, all of the elephants could go at Player A, forcing A to trade a Giant for an Elephant while still taking 3. (Two elephants could also go at A, with decent results.)

Here are the choices in a table, and the worst-case results:

<table><tbody><tr><td> </td>&#10;			<td><b>Attack A</b></td>&#10;			<td><b>Attack B</b></td>&#10;		</tr><tr><td><b>Send 2 Elephants</b></td>&#10;			<td>Deal 3 damage and trade an Elephant for a Hill Giant when A counterattacks.</td>&#10;			<td>Deal 3 damage and trade an Elephant for a Hill Giant when A attacks.</td>&#10;		</tr><tr><td><b>Send 3 Elephants</b></td>&#10;			<td>Deal 3 damage and trade a an Elephant for a Giant. No counterattack possible.</td>&#10;			<td>Deal 6 damage, kill player B, and take 3 damage when A attacks.</td>&#10;		</tr></tbody></table>

Doesn't seem too bad, does it? Looks like C should send some elephants downtown.

But wait. Silly green mage! She forgot about haste. Let's account for Player A top decking a [Lightning Elemental](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Elemental). (It's even bleaker if he gets a [Ball Lighting](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ball+Lighting); but we're leaving trample out of the equation.)

<table><tbody><tr><td> </td>&#10;			<td><b>Attack A</b></td>&#10;			<td><b>Attack B</b></td>&#10;		</tr><tr><td><b>Send 2 Elephants</b></td>&#10;			<td>Deal 3 damage and die when A counterattacks.</td>&#10;			<td>Deal 3 damage and die when A attacks.</td>&#10;		</tr><tr><td><b>Send 3 Elephants</b></td>&#10;			<td>Deal 3 damage and die when A counterattacks.</td>&#10;			<td>Deal 3 damage and die when A attacks.</td>&#10;		</tr></tbody></table>

Now it looks like the elephants ought to stay home.

The situation above is a bit simplistic, but not out of the question. There are many situations where a player with creature superiority (here it's C, with three elephants) has to think differently because she knows the red mage may pull something with haste. As the hasty creatures get larger (e.g., [Rorix Bladewing](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rorix+Bladewing)), the math becomes even more frightening.

Haste gets a bad rap from many casual players who feel the strategy is too reckless for a game with multiple opponents. You need to keep back blockers!

But I believe haste is a terrific strategy, and one that only gets better as your group becomes more familiar with your deck. The guy everyone knows has three [Ball Lightning](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ball+Lightning)s in his deck is in a game with nine red mana on the board, no creatures – but six cards in hand. Who attacks *that* guy?

### Math Problem #2: Borrowing

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. After two days, someone turns the first train around and sends it in the same easterly direction as the train from Los Angeles. *Will those crazy New Yorkers ever make it to Chicago?*

Wizards has recently bestowed the gift of “borrowing” upon red. The flavor rationale is that red's chaotic ways can induce temporary confusion, causing a creature to damage its original controller (or perhaps someone else).

Normally, red's stealing cards bestow the loaned creatures with haste. (See: [Insurrection](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Insurrection), [Threaten](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Threaten), [Grab the Reins](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grab+the+Reins), [Temporary Insanity](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temporary+Insanity).) For that reason, stealing has largely the same impact on combat math as haste, with one important exception: someone just lost a blocker (or attacker) they thought they had.

Let's go back to that three-player example, and look at some more conservative options for the green mage: attacking with *one* or *no* elephants. First, without stealing/haste:

<table><tbody><tr><td> </td>&#10;			<td><b>Attack A</b></td>&#10;			<td><b>Attack B</b></td>&#10;		</tr><tr><td><b>Send 0 Elephants</b></td>&#10;			<td colspan="2">Deal no damage and trade an Elephant for a Giant when A attacks. Keep two elephants.</td>&#10;		</tr><tr><td><b>Send 1 Elephant</b></td>&#10;			<td>Deal no damage and trade an Elephant for a Giant when A counterattacks. Keep two elephants.</td>&#10;			<td>Deal no damage and trade an Elephant for a Giant when A attacks. Keep two elephants.</td>&#10;		</tr></tbody></table>

Player C can't deal damage – but won't take any damage either. Seems safe. Now let's look at the picture if the format allows for a mere sorcery like Threaten (assuming Threaten takes an untapped Elephant in all cases):

<table><tbody><tr><td> </td>&#10;			<td><b>Attack A</b></td>&#10;			<td><b>Attack B</b></td>&#10;		</tr><tr><td><b>Send 0 Elephants</b></td>&#10;			<td colspan="2">Deal no damage. Choose between (a) taking 3 damage and trading an Elephant for a Giant or (b) taking no damage and trading 3 Elephants for a Giant, when A attacks. Keep either two or zero elephants.</td>&#10;		</tr><tr><td><b>Send 1 Elephant</b></td>&#10;			<td>Deal no damage. Take 3 damage and trade an Elephant for a Giant when A counterattacks. Keep two elephants.</td>&#10;			<td>Deal no damage. Take 3 damage and trade an Elephant for a Giant when A attacks. Keep two elephants.</td>&#10;		</tr></tbody></table>

Player C faces 3 damage in virtually every case (or a heap of dead elephants). Granted, C can counterattack – but will only punch through for 3 damage if she goes all out with both remaining elephants. This leaves her open to lethal damage from the next hasty or stolen creature.

In other words, while hasty creatures punish aggression, stolen hasty creatures punish both aggression *and* non-aggression.

Wow, red is *good* in multiplayer! And you haven't even cast [Fireball](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) yet.

### Problem #3: Knocks To The Head

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. After two days, an unexpected meteor that started Monday from behind the Moon slams into Chicago well in advance of either train. *Why wasn't anyone keeping an eye on the meteor?*

“Cheesy burn” gets the worst of blue mages' disdain. It's not clever! It doesn't stop a spell, or redirect it! It doesn't draw you cards! It doesn't change the color or type of a creature! *What are we thinking?*

Well, we're probably thinking we just burned 'em for 20 and won.

Direct damage is the enforcer of sanity in **Magic**. It ends the game when a bunch of dorks clog up the board with 28 variations of [Fog Bank](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog+Bank), [Puppeteer](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer), [Silent Arbiter](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Arbiter), and [Ensnaring Bridge](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ensnaring+Bridge). It puts a clock on combo, evens out ridiculous life gain, and ignores most of the burdensome enchantments and artifacts. You tap enough mana, and someone dies. How refreshing!

***Direct damage is the enforcer of sanity in Magic***.

For this reason, every player in a game where an opponent controls at least one Mountain has to do this math: adjust your life total downward by Y, where Y = \[the number of lands controlled by that opponent\] – 1. That's your *real* life total, if you let the red mage untap again.

Burn is powerful enough to gain unwelcome attention. In fact, playing direct damage often can actually have adverse consequences. A large enough [Fireball](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) is like a five-piece combo: everyone knows they could die, if they give you just a bit more time. So a couple of players with high enough life totals may come at you early, rather than wait for you to play a “friendly” [New Frontiers](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=New+Frontiers) for 13.

Because of this sort of reaction, burn is best done in multiplayer via one of two strategies:

**1) Instant speed**. When possible, replace your [Fireball](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball)s with [Ghitu Fire](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Fire) and [Volcanic Geyser](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Geyser). Even [Incinerate](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) or [Fireblast](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireblast) will often serve you better than an X sorcery. Opponents need to fear you when it's *not* your turn.

**2) Last resort.** Keep burn as your secondary path. Don't let opponents think of your deck as “that Fireball deck.” Instead, let them think of it as that clever little thing with the [Confusion in the Ranks](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks) and [Viashino Sandstalker](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viashino+Sandstalker)s and Defenders of Chaos, which also just happens to carry a secondary path to victory.

### Math Problem #4: Random Walk

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. After two days, the conductors of the two trains exchange places. Then a dozen other trains appear, each traveling in a random direction and at varying speeds. Half of these get replaced by goblin tokens. *Where did all the goblins come from, and why are they Chicago Cubs fans?*

In group play, one of the most devastating effects red can pull is the instigation of huge, chaotic effects. [Pandemonium](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pandemonium), [Grip of Chaos](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grip+of+Chaos), [Radiate](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate), [Thieves' Auction](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thieves%27+Auction), and [Confusion in the Ranks](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks) all do ridiculous things to games. Most opponents' decks don't even come close to having answers, beyond a timely [Counterspell](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) or [Naturalize](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize).

![](http://archive.wizards.com/global/images/mtgcom_daily_aa133_pic2_en.jpg)

Seek ye out the heavy hitters. They make even the simplest of spells and permanents nightmares for the stack, and for your opponents. A well-crafted deck around one of these cards (just one, please!) can be a red-headed beauty.

You may even get the blue mage to admit you're “pretty clever”.

### Math Problem #5: Probability

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. After two days, someone flips a coin and Chicago disappears from the map. *Whatever*.

The one aspect of red in casual **Magic** I *don't* particularly enjoy is coin-flipping. Now, I've seen fairly complicated coin-flipping decks, believe you me. But I have rarely, if ever, found the mechanic adds anything to the game at hand. There's a difference between building and shuffling a randomly distributed deck, and depending upon a whole new layer of random effects in order to win the game. To me, coin-flippers simply look like they're trying to play a completely different game from **Magic**.

I've asked a few times in the past, “does anyone out there even *like* coin flip cards?” I've never gotten more than two lukewarm responses per query. It's not necessary this time, folks. You don't need to impress *me*. My approval is not the issue. Wizards has made clear they'll keep up with the occasional coin flip card, but won't be increasing their power level. That's good enough for now, though I still think it's a bit cruel to put rares like [Krark's Thumb](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krark%27s+Thumb) in booster packs.

For the record, I vastly prefer those cards that depend on revealing cards from the top of your library (e.g., [Kaboom!](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kaboom%21), [Goblin Charbelcher](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Charbelcher)). These allow players who enjoy the game of chance to play the game of chance, while allowing others to try for manipulative strategies (e.g., [Goblin Recruiter](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Recruiter)). Everyone's happier that way, it seems to me.

### Math Problem #6: Counting Down From Ten To Zero

Problem: A train starts west at 8:00 am Monday from New York to Los Angeles at 50 kilometers per hour. At the same time, a train starts east from Los Angeles to New York at 60 kilometers per hour. Two evenings later, David Letterman appears with a Top Ten List. *What will the topic be?*

Most of the best cards in red have been there for a few years (though [Confusion in the Ranks](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks) and [Radiate](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate) are clear exceptions). It seems classics like [Mana Flare](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Flare) and [Furnace of Rath](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+of+Rath) are hard to top. (Wizards has released variations on both, including [Overburden](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overburden) and [Gratuitous Violence](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gratuitous+Violence).)

This past year hasn't added much, so far. While recent cards like [Savage Beating](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savage+Beating), [Bringer of the Red Dawn](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bringer+of+the+Red+Dawn), and [Shunt](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shunt) make for excellent additions to red's multiplayer arsenal, the top of this color's list is dominated by heavy-duty enchantments. The list below is taken from my annual Hall of Fame, which you may reference in [the archives](https://web.archive.org/web/20040720000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/columnarchive&column=SeriousFun) if you need help with the codes and numbers.

<table><tbody><tr><td> </td>&#10;			<td><b>Card</b></td>&#10;			<td><b>RS</b></td>&#10;			<td><b>GO</b></td>&#10;			<td><b>SP</b></td>&#10;			<td><b>PG</b></td>&#10;			<td><b>PL</b></td>&#10;			<td><b>CK</b></td>&#10;			<td><b>AVG</b></td>&#10;		</tr><tr><td>10</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grip+of+Chaos">Grip of Chaos</a></td>&#10;			<td>3</td>&#10;			<td>5</td>&#10;			<td>2</td>&#10;			<td>7</td>&#10;			<td>1</td>&#10;			<td>5</td>&#10;			<td>3.88</td>&#10;		</tr><tr><td>9</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Repercussion">Repercussion</a></td>&#10;			<td>7</td>&#10;			<td>4</td>&#10;			<td>2</td>&#10;			<td>2</td>&#10;			<td>4</td>&#10;			<td>4</td>&#10;			<td>4.03</td>&#10;		</tr><tr><td>8</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Flare">Mana Flare</a></td>&#10;			<td>5</td>&#10;			<td>4</td>&#10;			<td>2</td>&#10;			<td>2</td>&#10;			<td><b>8</b></td>&#10;			<td>3</td>&#10;			<td>4.07</td>&#10;		</tr><tr><td>7</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Hellkite">Shivan Hellkite</a></td>&#10;			<td>7</td>&#10;			<td>4</td>&#10;			<td>2</td>&#10;			<td>2</td>&#10;			<td>2</td>&#10;			<td><b>8</b></td>&#10;			<td>4.29</td>&#10;		</tr><tr><td>6</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodfire+Colossus">Bloodfire Colossus</a></td>&#10;			<td>7</td>&#10;			<td>7</td>&#10;			<td>3</td>&#10;			<td>2</td>&#10;			<td>2</td>&#10;			<td>3</td>&#10;			<td>4.33</td>&#10;		</tr><tr><td>5</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pandemonium">Pandemonium</a></td>&#10;			<td>5</td>&#10;			<td>6</td>&#10;			<td>1</td>&#10;			<td>3</td>&#10;			<td>7</td>&#10;			<td>4</td>&#10;			<td>4.48</td>&#10;		</tr><tr><td>4</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thieves%27+Auction">Thieves' Auction</a></td>&#10;			<td>2</td>&#10;			<td>7</td>&#10;			<td>5</td>&#10;			<td>7</td>&#10;			<td>4</td>&#10;			<td>2</td>&#10;			<td>4.52</td>&#10;		</tr><tr><td>3</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks">Confusion in the Ranks</a></td>&#10;			<td>5</td>&#10;			<td>6</td>&#10;			<td>1</td>&#10;			<td>6</td>&#10;			<td>4</td>&#10;			<td>5</td>&#10;			<td>4.65</td>&#10;		</tr><tr><td>2</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate">Radiate</a></td>&#10;			<td>1</td>&#10;			<td>7</td>&#10;			<td><b>8</b></td>&#10;			<td><b>8</b></td>&#10;			<td>2</td>&#10;			<td>3</td>&#10;			<td>4.73</td>&#10;		</tr><tr><td>1</td>&#10;			<td><a href="https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+of+Rath">Furnace of Rath</a></td>&#10;			<td><b>8</b></td>&#10;			<td>6</td>&#10;			<td>2</td>&#10;			<td>1</td>&#10;			<td>6</td>&#10;			<td>4</td>&#10;			<td>4.78</td>&#10;		</tr></tbody></table>

A word or two on this list: it is very, very hard to imagine red creatures that will be better in multiplayer than [Bloodfire Colossus](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodfire+Colossus) and [Shivan Hellkite](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Hellkite). In fact, I'm not certain Wizards should try. [Bloodfire Colossus](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodfire+Colossus) with [Dawn of the Dead](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dawn+of+the+Dead) borders on ridiculous, while [Shivan Hellkite](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Hellkite) can start throwing out instant-speed [Arc Lightning](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arc+Lightning)s as soon as you untap.

Finally, does [Pandemonium](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pandemonium) get sillier and sillier as time goes on, or what? First [Pangosaur](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pangosaur), then gating creatures, and now imprint. “I'll pay 4 and use my [Soul Foundry](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry) to make another [Desecration Elemental](https://web.archive.org/web/20040720000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Desecration+Elemental)…”

Thanks for taking my little math test. I hope the word problems weren't too hard. If they were, you might consider a simpler color…maybe blue?

*Anthony cannot provide help with decks; nor can he tolerate the dryness of the word problems found in most junior high algebra texts.*