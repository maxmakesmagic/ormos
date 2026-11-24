---
id: bq2gddxj
kind: article
lang: en
path: /en/articles/makingmagic/2013/03-18-designing-for-dimir
title: Designing for Dimir
published: '2013-03-18'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    lang_detected: en
    capture_id: 214769
    url: https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    captured_at: '2024-06-19 10:04:32+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    lang_detected: en
    capture_id: 214769
    url: https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    captured_at: '2024-06-19 10:04:32+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    lang_detected: en
    capture_id: 214769
    url: https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    captured_at: '2024-06-19 10:04:32+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    lang_detected: en
    capture_id: 214769
    url: https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
    captured_at: '2024-06-19 10:04:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: bq2gddxj
  url: https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
  page_key: magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
  lang: en
  template: contentful
  captured_at: '2024-06-19 10:04:32+00'
  capture_id: 214769
  wayback_url: https://web.archive.org/web/20240619100432id_/https://magic.wizards.com/en/news/making-magic/designing-dimir-2013-03-18
- document_id: bq2gddxj
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/239
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/239
  lang: en
  template: aspx
  captured_at: '2014-02-18 20:55:06+00'
  capture_id: 650466
  wayback_url: https://web.archive.org/web/20140218205506id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/239
- document_id: bq2gddxj
  url: https://magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-13
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-13
  lang: en
  template: drupal
  captured_at: '2022-09-26 04:14:57+00'
  capture_id: 875389
  wayback_url: https://web.archive.org/web/20220926041457id_/https://magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-13
- document_id: bq2gddxj
  url: https://magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-18
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-18
  lang: en
  template: drupal
  captured_at: '2022-09-26 22:32:08+00'
  capture_id: 875413
  wayback_url: https://web.archive.org/web/20220926223208id_/https://magic.wizards.com/en/articles/archive/making-magic/designing-dimir-2013-03-18
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: bq2gddxj
  capture_id: 650466
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/239
  wayback_url: https://web.archive.org/web/20140218205506id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/239
  captured_at: '2014-02-18 20:55:06+00'
  template: aspx
  sha256: d07c1615ac178c3cd2df8b5dab5005544cdefd8c008e4019e8d6d0f4339166e0
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Dimir Guildgate
  - Duress
  - Coercion
  - Duskmantle Guildmage
  - Deathcult Rogue
  - Perplex
  - Midnight Recovery
  occurrences: 11
---
Welcome to Dimir Week. This is the ninth installment of the *Return to Ravnica* block guild theme weeks. [Selesnya](/en/articles/makingmagic/2012/10-01-designing-for-selesnya), [Azorius](/en/articles/makingmagic/2012/10-29-designing-for-azorius), [Izzet](/en/articles/makingmagic/2012/11-12-designing-for-izzet), [Golgari](/en/articles/makingmagic/2012/11-26-designing-for-golgari), [Rakdos](/en/articles/makingmagic/2012/12-10-designing-for-rakdos), [Boros](/en/articles/makingmagic/2013/02-04-designing-for-boros), [Simic](/en/articles/makingmagic/2013/02-18-designing-for-simic), and [Gruul](/en/articles/makingmagic/2013/03-04-designing-for-gruul) have all had their turn (and Orzhov is next week), so it's time to talk Dimir. During the original *Ravnica* block, I did [a series of ten columns](https://web.archive.org/web/20131105013418/http://www.wizards.com/magic/magazine/features.aspx?tag=color%20pie) about the philosophies of each guild.This time around, instead of talking philosophy, I'm talking the craftsmanship of design. How does one design for blue and black in general and for Dimir in particular? Stick around and I'll tell you. 

Each of these "Designing for" articles follows a similar structure. I'll begin by answering the same four questions and then I will walk you through the design of the guild mechanics, the one from the original *Ravnica* block and the one from the *Return to Ravnica* block. 

### What's the Easiest Thing About This Color Pairing?

Blue and black tend to be the kings of card advantage. Blue is primary in card drawing and black is secondary (tied with green). Blue has counterspells and bounce. Black has discard and creature destruction. The two colors are excellent at slowly, and sometimes not so slowly, gaining the upper hand, often subtly enough that less-experienced players aren't even aware of it.

What this means is that blue and black thematically click together well. The two colors have a clear flavor and feel that mesh well. Blue is sneaky and cunning. Black in underhanded and ruthless. Mix them together and you have a guild you might not want to trust.

![](https://i.ormos.uk/69/07/6907e6b64844fcbd2ae0ff11a3ad37dc0eb80361a4b9dfe32b36c9fd690852f4.jpg) 

Dimir Guildgate | Art by [Cliff Childs](https://web.archive.org/web/20130318000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22cliff%20childs%22])

### What's the Hardest Thing About This Color Pairing?

While philosophically the two colors mesh well, mechanically they are the two ally colors that have the least in common. Now, this is a pain for making hybrid cards, but shouldn't a clear mechanical identity make gold cards easier to design? The problem here is that while blue and black don't overlap much in actual mechanics, they have a lot of abilities that are close to the other but just a little different.

I'll walk through some of them to demonstrate:

**Card Drawing:** As I said above, blue is #1 and black is tied for #2. But blue always does its card drawing straight up, often these days at instant speed. Black always has to trade something for its cards—most often life. Black usually does this at sorcery speed. 

**Evasion:** Blue and black both have flying. Blue also has unblockability and islandwalk. Black has intimidate and swampwalk. Black also has deathtouch, which doesn't technically give it evasion but heavily encourages the opponent not to block. 

**Library Denial** Blue "mills," meaning it makes the opponent put some number of cards from the top of his or her library into his or her graveyard. Black "extorts," meaning that it goes into the library and exiles particular cards. The flavor here is that blue makes you forget in general while black lobotomizes you. 

**Hand Denial:** Blue and black are the only two colors that can easily deal with a threat before it hits the battlefield. Blue has the ability to use counterspells while black has the ability to force the opponent to discard. 

**Tutoring:** Blue and black are the two colors best at getting specific cards out of your library and into your hand. Blue tends to be more focused, with cards directing you what kind of card you can get, while black has the more blanket tutors, sometimes with an additional cost associated. 

**Stealing Creatures:** Blue takes the opponent's creatures while they are alive, while black takes them after they've died. 

**Learning the Opponent's Hand:** Blue has spells that peek. Black gets glances as part of certain discard spells where it needs to see the hand, such as Duress or Coercion, to make choices of what gets discarded. 

In each case, they are similar but a little different. That's great for giving each its own identity but it makes it more difficult to make blue-black cards. The blue ability always feels close to black, and vice versa, often making the cards feel like they'd fit in one color or the other rather than in both.

![](https://i.ormos.uk/c0/b6/c0b606f9564cc94cc2988f547067a607aa74c5712e90291ef58ce8468bef217f.jpg) 

Duskmantle Guildmage | Art by [Slawomir Maniak](https://web.archive.org/web/20130318000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22slawomir%20maniak%22])

### What's the Mechanical Heart of This Color Pair?

Of the ten two-color pairs, this question is the trickiest for blue-black. Why? Because blue-black's mechanical heart is more about a feel than a concrete quality. Boros is about cheap aggressive creatures, Golgari is centered in the graveyard, but Dimir isn't quite as easily pinned down.

The easy answer is that blue-black is about the library. Blue and black are the two colors that interact with it most. They have card drawing, tutoring, milling, extracting, filtering. One of their win conditions is library depletion. But all that is more a secondary strategy in *Gatecrash*. 

No, the thing that ties together blue-black is this sense that it's getting incremental advantage at every turn. If any color combination is the poster child for the two-for-one, it's blue-black. What this means is that when you build a blue-black theme, you have to figure out how it's getting its incremental advantage. Note that the two Dimir mechanics do it in different ways.

Transmute is about trading card utility, upgrading one card for a card more fine-tuned for your needs. Cipher is about setting up a situation where you can create raw card advantage, generating spells without the card. I'll talk about each more as I get to their creation, below.

![](https://i.ormos.uk/ac/7f/ac7f64fb39a763fd3f9a8b7bc91def9046d31b90521f016c38dd4d55a6de860d.jpg) 

Deathcult Rogue | Art by [David Palumbo](https://web.archive.org/web/20130318000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22david%20palumbo%22])

### What's the Focus of This Color Pair?

Blue-black's plans are not as straightforward as some of the other color combinations. Part of this, I believe, is because blue-black wants to keep the opponent guessing. Its advantage comes from the fact that the opponent doesn't know where the attack is coming from. The end result is that blue-black has three main ways to win.

**Evasive Creatures:** Blue and black are two of the colors with the best evasion. Once they take control of the game, they can use their evasive creatures as a kill condition. Because they have the tools to mess with the opponent's plan and slow things down, the small evasive creatures have time to do their thing. The cipher mechanic clearly plays into this space. 

**Library Depletion:** **Magic** has an alternative win condition built into its very core. Blue-black are the two colors that most often win through this strategy. Blue has straight-up milling; black has extracting. All it has to do is stall and use its milling and extracting to win. This strategy is even more powerful in Limited, where the decks are only forty cards. Grind, the unnamed "mill until you get a land" mechanic from *Gatecrash*, plays into this strategy. 

**How'd I Lose?:** The final strategy is the subtlest. Blue-black uses its incremental advantage to eke out every small gain it can. The opponent loses but never has any clear thing to point to. Somehow, he or she just lost. Transmute played in this space. 

These strategies can be mixed together or run separately. They make blue-black extra hard to fight against because you're never quite sure where the danger lies. I know when playing against Dimir in *Gatecrash*, I'm always trying to figure out what strategy my opponent is using. 

This focus is unique and not something I'd want to do a lot, but it philosophically fits blue-black to a T.

### Transmute

![](https://i.ormos.uk/f0/c0/f0c0900633ce71bdac60856b39a338322f6057d2bf621910f370fb1e55802f81.jpg) 

In the initial *Ravnica* block, Dimir was in the first set, **Ravnica*: City of Guilds* . The design team ([Aaron Forsythe](https://web.archive.org/web/20140110115401/http://www.wizards.com/magic/magazine/archive.aspx?author=aaron%20forsythe), [Richard Garfield](https://web.archive.org/web/20140125031340/http://www.wizards.com/magic/magazine/archive.aspx?author=richard%20garfield), [Mike Elliott](https://web.archive.org/web/20130609055227/http://www.wizards.com/magic/magazine/archive.aspx?author=mike%20elliott), and Tyler Bielman, led by myself) approached Dimir as the "library guild," much as we approached the Golgari as the "graveyard guild." As I explained above, this comes about because blue and black have more interaction with the library than any other two-color combination. 

I'll be honest, when I pushed us toward the "library guild" I had one goal in mind. I am a huge fan of alternative-win conditions so, of course, I was a huge fan of the one already built into the game: milling. I didn't know how exactly it was going to work, but I wanted milling to be a part of Dimir's identity. At the time, though, it never dawned on me to make milling itself part of the guild keyword. (That wasn't true for *Gatecrash*.) 

While I was fiddling with milling, someone else on my team, Aaron Forsythe, decided to take a different approach in finding a mechanic for the "library guild." Rather than focus on the opponent's library, Aaron turned his focus onto the player's library. As I explained above, one of the areas where blue and black overlap is tutoring. Aaron wanted to see if he could make a mechanic that gave blue-black the ability to get the cards it needed out of the library.

Aaron's major problems were basically tutoring's major problems. First, we have what R&D calls "repetitive game play." **Magic** is fun if each game plays out differently. When games follow the same pattern, game after game, it becomes monotonous and less fun. The game solves this problem with the library, an item that is randomized such that the players get their cards in an unknown order, making each game play out differently. Tutors undo this tool by eliminating the randomness. 

The second problem is a power-level concern; this is more of a development issue than a design one but design has an obligation to make things that can be developed. A combo deck stalls until it can get the pieces to its combination, which usually allows it to quickly win the game. Because a combo deck requires the player to collect a series of different cards, the randomness of the library tends to slow down the deck. Tutoring once again bypasses this safety valve, allowing a combo player to "go off" with a combo far faster than he or she would normally be able to. Aaron recognized both problems but he thought we could find a way to work around each.

As proof of concept, Aaron turned in a card with his mechanic proposal. You guys know the card as this:

 ![Perplex](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Perplex&options=) 

  

But when Aaron first turned it in, it looked like this:

> Perplex  
>  1UB  
>  Instant  
>  Counter target spell unless its controller discards his or her hand.  
>  Transmute UB (UB, Reveal this card from your hand: Put this card on top of your library, then search your library for a card with converted mana cost three, reveal it, put it into your hand, then shuffle your library.)

There are a few differences between Aaron's original version of transmute (note the name never changed—that was what Aaron called it when he submitted it). Let's walk through them.

**The cost:** In Aaron's original proposal, blue-black cards would transmute for ![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif), blue cards for ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif), and black cards for ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif). In the finished version, the blue-black cards cost ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif), the blue cards ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif), and the black cards ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif). This change was made by development because the design version proved to be a little too strong. 

**What you do with the card with transmute:** In Aaron's original version, you put the card on top of your library, which would then be shuffled in at the end of the effect. The finished version just had you discard the card. Why this change? Mostly because everyone just discarded the card and forgot to put it on top of the library. Usually, in design, when the players keep doing something wrong, but do it consistently wrong, you want to seriously consider just making the mechanic do what everybody instinctively wants it to do. 

**Play only as a sorcery:** The original version could be played any time you could play an instant. While this offered all sorts of cool moments where the card could tutor on the fly, it was just another thing making the mechanic too powerful. Development wisely also made this change. (Note that modern template now says, "Transmute only as a sorcery.") 

Other than those few, mostly power-related issues, transmute was printed as submitted. The trick for the design team was figuring out what kind of cards wanted to have transmute on them. Aaron felt strongly that they had to be cards you would want to main deck but cards whose value would swing as the game progressed. Perplex, as an example, could be powerful early but often could be worthless later in the game, when the opponent doesn't have any cards in hand. 

The other thing we had to monitor was making sure the transmute cards covered a range of converted mana costs. The transmute mechanic was linear, in that it made you want to include other cards with the specified converted mana cost, so we wanted to ensure there was a wide spread.

As mechanics go, we got it in early in the process and it made it cleanly all the way through development (with the few tweaks) to print. Cipher wouldn't be quite as easy.

### Cipher

![](https://i.ormos.uk/49/95/4995df63afa881db7268417ef2810b764704adabc47d6cfd78b22093d6f06679.jpg) 

Let me start by revealing something I've never revealed in an article before: I love grafting things. Let me explain. Grafting is an R&D slang term where you take some aspect, usually a sentence, and stick it into the rules text of another card. (Note that there also is a mechanic called graft used by the Simic in the original *Ravnica* block, but I'm not talking about that.) 

Here's an example of a famous old card from *Urza's Saga* that grafts: 

 ![Hermetic Study](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Hermetic%20Study&options=) 

The point of grafting is that you take an existing card and expand what it can do by grafting on additional words and/or abilities. Why do I enjoy grafting so much? I don't know. My best guess is that it's my Johnny sensibility enjoying turning cards into other cards.

I bring this up because my love of grafting has led me to design numerous mechanics that incorporate it. Two of the most famous are imprint, from *Mirrodin*, and splice, from *Champions of Kamigawa* (best known for its original use, "splice onto Arcane"). 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Isochron Scepter" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Isochron%20Scepter&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Glacial Ray" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Glacial%20Ray&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

I bring these two up because cipher essentially is the love child of these two mechanics. Let me explain. When *Gatecrash* design started I pushed hard for a milling mechanic with the playtest name of "grind." While grind stayed in the set, we decided we wanted a different mechanic to be the Dimir keyword, so I spent some time thinking about a new replacement. (For the full, longer story of grind's creation and ultimate removal as the guild's keyword, check out [this earlier article where I tell the full story](/en/articles/makingmagic/2013/01-07-gatecrashing-the-party-part-2).) 

Much of design is spent realizing that something you'd worked on isn't quite right and then having to search through all the existing parameters to find a solution. When I do this, I find it works to write down as many things as I can that I know to be true. The more restrictions I have to my problem, the more I can figure out which areas I need to explore. Here's what I had when I started trying to find a new mechanic:

1.  **The mechanic had to feel Dimir:** I talk a lot about how I design by feel. I'm a big believer that a game designer has to be very conscious of the emotional reaction his or her game mechanics will create. As such, my number-one priority in finding the replacement mechanic was finding something that just oozed Dimir.
2.  **We couldn't mess with milling:** Grind had been shifted from keyword to nonkeyword status. That meant anything in the similar space was off limits.
3.  **It needed to play into the focus of the guild:** Up above, I outlined three ways Dimir could win. Restriction #2 eliminated the mill option, so that left evasion and card advantage. Card advantage is tricky to work with (and we already went there in original *Ravnica*—see above) so I decided to focus on evasion. What did Dimir creatures want to do? Well, they liked sneaking in and damaging the opponent. Was there a way to make doing that even better?
4.  **It wanted to be a spell mechanic:** Boros? Creature mechanic. Simic? Creature mechanic. Gruul? Creature mechanic. Orzhov? Not totally a creature mechanic but it was on a bunch of creatures. That meant we really needed a spell mechanic, so while I was solving one problem, I might as well solve another.
5.  **It wanted a little bit of splash:** The other guild mechanics were all solid and they played well but none of them tended to jump out at you when you first heard about them (okay, maybe evolve). This was another problem we could solve while finding the replacement.

With all this in my head, I started walking through my options. What follows is a rough approximation of my train of thought:

*Okay, we have rogues and scoundrels who sneak around and hit the opponent. How could I help that strategy? I could help make them harder to block. No, blue and black are already the best at evasion. What if I rewarded them for damaging the opponent? That shows promise. How do I reward them? Saboteur abilities* (what R&D calls the ability that has an effect when it deals combat damage to the opponent). *When you hit the opponent, something happens.*

*So I want to graft saboteur abilities onto my Dimir creatures, many of which would naturally have evasion. How do I do that? Creature Auras seem the cleanest. The problem with that solution, though, is that there's no keyword. Most sets have an Aura that grafts text. How do I make this mechanic something I could keyword? Also, what do I do to make this splashier?* 

This led me to the splice mechanic. What if I had a sorcery that I could graft onto a creature as a saboteur ability? That sounded cool. Also, I channeled imprint with the idea that you would exile the spell itself and then use the actual card as the reminder for what got grafted. [Mark Gottlieb](https://web.archive.org/web/20140110115611/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20gottlieb) (my co-lead for *Gatecrash*) suggested that you get to cast the spell first, before it gets grafted, to allow you one use of your spell—and often two if you set it up correctly. This would help make sure the cards had enough value to play. 

![](https://i.ormos.uk/8c/38/8c38882c3d8c636c4bf2376d94f711a43b63c500d178bb4b25be4e0840202967.jpg) 

Midnight Recovery | Art by [Peter Morbacher](https://web.archive.org/web/20130318000000/http://gatherer.wizards.com/pages/search/default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22peter%20morbacher%22])

With this idea figured out, the next step was to actually make the cards. This proved to be a little more difficult than I initially realized. 

First, we decided we wanted to keep the mechanic on sorceries because the timing with instants had the potential to confuse the players. It also raised the mechanic's power level and development was already scared of cipher (called "encode" in design).

Second, the effects all had to be something that were useful at the tail end of combat, when your creatures dealt damage. This meant they had to be proactive, not reactive, and they had to be effects that were generally useful at most times of the game. We also realized we could essentially make a few creature cards by making them sorceries that generated creature tokens.

Third, we had to keep the effects small enough that a creature with evasion that was doing this every turn would shift the game in the Dimir player's favor rather than just winning it outright.

Fourth, the abilities had to be short (meaning few words) because they had to fit on the card, as cipher was going to take up six lines of reminder text.

Luckily, blue and black's subtle differences helped make it easier to find enough effects, many of which were short enough to fit.

And that is how cipher came to be.

### Black and Blue All Over

That's all the time we have for today. I hope you enjoyed my peek into the mysterious world of blue and black. As always, I would love to hear your feedback in my mail, in this column's thread, or in any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)). 

Join me next week when the world is all black and white.

Until then, may you get in your damage before they even see you coming.

* * *

### Drive to Work #25—*Homelands*

I have said on numerous occasions that I believe *Homelands* is the worst-designed expansion in **Magic**'s history. Today I explore its design and talk about what went wrong. 

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      &#10;      &#10;      <div id="magic1"> Multi </div>&#10;      &#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

*   [**Episode 25**](https://media.ormos.uk/be/94/be946805db32670ad6d74d1497d8b3b497387efa72f0db391808a03162fa60c2.mp3) : *Homelands* (10.8 MB)
*   [**Episode 24**](https://media.ormos.uk/6d/16/6d16405db5b717795df2767a707d7c3a59fa03c25f508cff6ffc12801e0e0859.mp3) : *The Mana System* (9.92 MB)
*   [**Episode 23**](https://media.ormos.uk/be/d0/bed0d40a0ecc8692744bc1f0b74ae6a90396dd63c9eec1734f9c19240a57d11d.mp3) : *The Color Wheel* (10.2 MB)
*   [**Episode 22**](https://media.ormos.uk/c6/ad/c6ad1888c74b9f1bd57392d434324c1e9d3d79f1b9095a5ea7a1b528748b1a81.mp3) : *The Trading Card Game Genre* (9.81 MB)
*   [**Episode 21**](https://media.ormos.uk/ad/83/ad83562258f42b33cc2f9f30ed5f50a7a88d96514eb6b31dce038f08fe3ac84b.mp3) : *Innistrad Part 3* ()
*   [**Episode 20**](https://media.ormos.uk/71/47/7147ec92368a7b8f98fb84531bbc9f7c392bb418aa8734b6f1844e648dd7008a.mp3) : *Innistrad Part 2* (14.6 MB)

  
  

![](https://i.ormos.uk/ae/c0/aec0e7691a77d43b24d9d7b3d09e4801440738bc4e4b6c6bf72bf0cb7f24962c.jpg) 

![](https://i.ormos.uk/d2/e7/d2e71f791c65cdf2356ac3e6081d4ccdf9e2a1f59666204e5204fd80e7c308d9.jpg) [![](https://i.ormos.uk/26/95/2695b2bb507d5fe24582ed4d128fa225368e26fa88c9de28501f29fc109b7b3d.jpg)](/en/events/2011/league-facts/avacyn-restored-league) ![](https://i.ormos.uk/2c/02/2c02ec1873bd94d38416e3306848241b26b0ab4734d2bbe37aefdde35e8e9518.jpg) [![](https://i.ormos.uk/ee/bb/eebb6c15c343bd8da6d69decf1b3523b9e3fa4402a2523b9743d22f4d82025b4.jpg)](https://web.archive.org/web/20140218213728/http://www.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/gatecrash)  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](https://i.ormos.uk/ab/40/ab400592d278d807794078b05168bc55bfeff9fe74a080eb8e83d33e2e0a6bc5.jpg)

 

![Mark Rosewater](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg "Mark Rosewater")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Mark Rosewater</b>&#10;        <br>&#10;        <a href="https://twitter.com/maro254">@maro254</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130318000000/http://www.wizards.com/company/emailtoauthor.asp?author=Mark%20Rosewater&amp;amp;headline=[Designing%20for%20Dimir]">Email Mark</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130318000000/http://staging.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20140410010616/https://www.wizards.com/magic/magazine/archive.aspx?tag=making%20magic&amp;description=making%20magic">Making Magic Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Working for **Magic** R&D since October, 1995, Mark Rosewater is currently the head designer. His hobbies include spending time with his family, talking about **Magic** on every known medium (including [a daily blog](http://markrosewater.tumblr.com/) and a [weekly podcast](https://itunes.apple.com/us/podcast/magic-gathering-drive-to-work/id580709168)), and writing about himself in the third person. 

 