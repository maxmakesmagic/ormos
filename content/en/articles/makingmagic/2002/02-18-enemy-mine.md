---
id: 2wnhbe5z
kind: article
lang: en
path: /en/articles/makingmagic/2002/02-18-enemy-mine
title: Enemy Mine
published: '2002-02-18'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    lang_detected: en
    capture_id: 215169
    url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    captured_at: '2024-03-16 08:43:49+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    lang_detected: en
    capture_id: 215169
    url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    captured_at: '2024-03-16 08:43:49+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    lang_detected: en
    capture_id: 215169
    url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    captured_at: '2024-03-16 08:43:49+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    lang_detected: en
    capture_id: 215169
    url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
    captured_at: '2024-03-16 08:43:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 2wnhbe5z
  url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
  page_key: magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
  lang: en
  template: contentful
  captured_at: '2024-03-16 08:43:49+00'
  capture_id: 215169
  wayback_url: https://web.archive.org/web/20240316084349id_/https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
- document_id: 2wnhbe5z
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr8
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr8
  lang: en
  template: aspx
  captured_at: '2014-05-24 19:14:23+00'
  capture_id: 804241
  wayback_url: https://web.archive.org/web/20140524191423id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr8
- document_id: 2wnhbe5z
  url: https://magic.wizards.com/en/articles/archive/making-magic/enemy-mine-2002-02-18
  page_key: magic.wizards.com/en/articles/archive/making-magic/enemy-mine-2002-02-18
  lang: en
  template: drupal
  captured_at: '2022-10-04 21:14:57+00'
  capture_id: 877892
  wayback_url: https://web.archive.org/web/20221004211457id_/https://magic.wizards.com/en/articles/archive/making-magic/enemy-mine-2002-02-18
- document_id: 2wnhbe5z
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr8
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr8
  lang: en
  template: classic_asp
  captured_at: '2005-04-04 07:59:20+00'
  capture_id: 1981575
  wayback_url: https://web.archive.org/web/20050404075920id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr8
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2wnhbe5z
  capture_id: 215169
  url: https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
  wayback_url: https://web.archive.org/web/20240316084349id_/https://magic.wizards.com/en/news/making-magic/enemy-mine-2002-02-18
  captured_at: '2024-03-16 08:43:49+00'
  template: contentful
  sha256: 2a9510a907e3719f109b12d6b031722ba9e0372c1860f95cc82f54a602d965c6
render_recovery: []
---
Welcome to Color Hoser Week. For those unfamiliar with the term, “color hosers” are cards that punish players for playing a particular color. Examples of color hosers would be [Boil](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boil) or [Hibernation](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hibernation). Since “Making Magic” is a design column, I thought it might be cool to talk about the design of color hosers. (Radical, I know.)

In order to talk to you about color hoser design, I’m going to have to let you on a dirty little secret. Design has rules. Lots and lots of rules, which constantly evolve. They’re a lot like **Magic** rules except that there’s more of them and no one has ever bothered to write them down. So how do I know them? Well, first I have to admit that I don’t know all of them. But what I do know I learned from working in the design trenches for the last six years.

I often talk about how designers love to break the rules. That’s because there are so many of them for us to follow that it’s fun every once in a while to run around R&D laughing hysterically, screaming, “Not today, my little rule! Not today!” at the tops of our lungs.

But rules shouldn’t be broken until they’re understood, so let me start by going over the basic rules (the extended rules would take more time to write than I have available) of color hoser design. As I talk about each rule, I’ll also cover the exceptions. As an extra bonus, I’ll bring up some examples of R&D mistakes where we didn’t follow the rules.

But first, let me begin by explaining in a nutshell why color hosers exist.

### WHY COLOR HOSERS EXIST

The mechanics of **Magic** create certain forces in the game. Mana consistency, for instance, is so important that players are rewarded by playing decks of only one color. But R&D feels **Magic** is a better game if players are encouraged to play multiple colors. So how do we accomplish that? In many ways, actually. We create a strict separation of color flavor to create weaknesses for each color. We create synergies between colors. We create cards that require two or more colors to play (gold cards being the best example). The list is quite long.

One of the easiest ways to punish mono-color play is to create color hosers. Every strategy in **Magic** should have a counter strategy, and mono-color decks are no different. In addition, color hosers have the side benefit of helping keep the metagame balanced. If black, for instance, is getting too powerful, the black hosers will help keep it in check.

That said, on with rules:

### Rule #1: Color Hosers Should Penalize (Hose) Enemy Colors

This one’s pretty obvious but it’s the most basic rule. Each color has two allies and two enemies. You help your allies and hurt your enemies. Simple.

Rule #1 is broken often. First, **Magic** has a flavor of colors hosing themselves. For example, many of black’s creature-destruction spells don’t affect black creatures. Blue has to worry about being attacked by islandhome creatures. And forestwalk and mountainwalk are common abilities in their respective colors.

Second, white, as a defensive color, tends to have hosers against all colors including itself. The best examples of this would be the [Circle of Protection: White](https://web.archive.org/web/20020218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Circle%2Bof%2BProtection%253A%2BWhite).

Third, R&D occasionally makes cards that attack allies. The most recent examples of this would be [Coral Net](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coral+Net) and [Flash of Defiance](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash+of+Defiance) from *Torment*. To play up the black theme of the set, both cards hurt an ally that is also an enemy of black. The most famous example before *Torment* would be *Apocalypse* where the theme was topsy-turvy color interactions (allies are enemies and enemies are allies).

### Rule #2: Color Hosers Should Be True to Their Color's Flavor

In *Alpha*, Richard Garfield played around with the idea that colors could tap into their opponent’s abilities to hose them. The most famous example would be the Elemental Blasts ([Blue Elemental Blast](https://web.archive.org/web/20020218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Blue%2BElemental%2BBlast) and [Red Elemental Blast](https://web.archive.org/web/20020218000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Red%2BElemental%2BBlast)). Both Blasts could counter the opposite color (a blue thing) and destroy permanents of that color in play (more of a red thing). The problem with this idea was that it watered down the flavor of the colors. Red, for example, was powerless against white’s enchantments but had an easy answer to blue’s.

In modern day design, color hosers are no longer allowed to “bleed” (R&D’s term for doing something in a color not natural to that color’s theme). Colors need to punish the opponent in a manner that makes sense for the color.

A good example of where R&D messed this up in the past was the card [Anarchy](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anarchy) (from *Ice Age*). Red should punish white but not in a way completely antithetical to what red is about. Red is good at blowing up tangible things. Red can bolt creatures, scorch lands, or shatter artifacts, but enchantments are meant to be red’s bane. Enchantments don’t have substance. Red can’t handle them because they aren’t things red can just smash. Anarchy took this cool quality of red and just threw it out the window.

### Rule #3: Color Hosers Should Scale In Their Effectiveness

The point of this rule is that a card that hoses a color should be more effective the more of that color the opponent is playing. As an example, [Perish](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perish) is better against a mono-green deck than a two-color deck using green. It’s important to note that a one-shot hoser, such as [Slay](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slay), still fits this criteria as its usefulness grows (in options of creatures it can destroy as opposed to the total number of creatures it does destroy) the more green an opponent is playing.

The corollary to this rule is that sweeping color hosers should also penalize the player using the spell if they are playing the appropriate color. For instance, [Flashfires](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flashfires) is much more dangerous to a player playing a red/white deck than one playing a non-white deck.

### Rule #4: Color Hosers Should Prey on the Enemy Color’s Weakness

The best color hosers are the ones that find the enemy color’s weakness and turn the screws. [Circle of Protection: Red](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Circle+of+Protection%3A+Red), for example, causes red great headaches because red does not have any easy way to deal with enchantments. [Compost](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compost) hurts black as black is all about putting cards in the graveyard through destruction and discard.

Many of R&D’s biggest failures with color hosers have been when we neglected this rule. The most famous example is probably [Warthog](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warthog), green’s "black hoser" in *Sixth Edition*. What did black get to hose green? [Perish](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perish)! Perish vs. Warthog: a little like pitting Mike Tyson against Gary Coleman. Warthog shows off the point of Rule #4. Black is the creature-killing color. A green creature (without protection from black or untargetability) isn’t going to cause black any problems.

As an aside (as an aside to this aside; I love asides so expect a lot of asides in my column), while its fun to poke a stick at R&D’s past follies, I do feel a need to explain how [Warthog](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warthog) ended up in *Sixth Edition*. When the *Sixth Edition* team sat down to choose cards for the set, they knew they wanted a cycle of color hosers at uncommon. They were free to use cards up through *Weatherlight* (a few common and uncommon *Tempest* cards did get used). What follows are the choices available in uncommon (besides each card is the strikes against it):

*   ![Lifeforce](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lifeforce)

    **Lifeforce (*Alpha*)** – as “Ask Wizards” explained a few weeks ago, green isn’t about countering
*   ![Whirling Dervish](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Whirling+Dervish)

    **Whirling Dervish (*Legends*)** – protection isn’t used in the basic set
*   ![Thelon's Chant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thelon%27s+Chant)

    **Thelon's Chant (*Fallen Empires*)** – the basic set doesn’t mention upkeep on cards (a few exceptions were made for rare cards in *Sixth*); also the basic set doesn’t use counters
*   ![Freyalise's Charm](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Freyalise%27s+Charm)

    **Freyalise's Charm (*Ice Age*)** – card drawing isn’t very green, plus the card was a bit complicated for the basic set
*   ![Spectral Bears](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Spectral+Bears)

    **Spectral Bears (*Homelands*)** – the basic set doesn’t mention upkeep on non-rare cards
*   ![Decomposition](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Decomposition)

    **Decomposition (*Mirage*)** – cumulative upkeep isn’t used in the basic set
*   ![Roots of Life](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Roots+of+Life)

    **Roots of Life (*Mirage*)** – the card hoses blue as well as black.
*   ![Elephant Grass](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elephant+Grass)

    **Elephant Grass (*Visions*)** – cumulative upkeep isn’t used in the basic set
*   ![Reap](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reap)

    **Reap (*Tempest*)** – the basic set avoided cards with multiple targets; also, this card proved a bit too complicated for the basic set

Not a single uncommon green hose black card was useable. So the team turned to common. The only card available: [Warthog](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warthog). Thus the answer to why Warthog was chosen is that not a single other valid choice existed.

### Rule #5: Color Hosers Shouldn’t Automatically Win

Color hosers should be good. They shouldn’t say: “Win the game if opponent is playing Color X.” A good color hoser should punish a player for playing a certain color but there should be some room for that player to play around the disability. Some of R&D’s mistakes in the past with color hosers has been making ones that are simply too good. Examples of this would be [Perish](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perish) (the mana cost was too low for the effect) and [Dystopia](https://web.archive.org/web/20020218000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dystopia) (the spell allowed black to destroy things it should have problems destroying such as enchantments and creatures with protection from black).

### A Final Note

As you can see, a lot of thought goes into creating color hosers. So the next time one is beating you down, take a moment to admire the aesthetics and subtlety of the card smashing your head in.

Next week, I jump back into the fire to talk about how R&D decides which cards are rare.

Until then, may you mana curve be smooth.

Sincerely,

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*