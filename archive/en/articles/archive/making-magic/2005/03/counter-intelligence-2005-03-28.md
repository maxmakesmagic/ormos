
---
[Link to Wayback Machine](https://web.archive.org/web/20200812004023/https://magic.wizards.com/en/articles/archive/making-magic/counter-intelligence-2005-03-28)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Before I begin I want to make a quick note about last week's column. Often in my column I'll take a fanciful approach to the topic. Last week (“The Troubled One”) I learned I have to be careful what kinds of topics I do that with."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "615666"
[_metadata_:publish_date]:- "2005-03-28"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Counter Intelligence"
[_metadata_:wayback_capture_timestamp]:- "2020-08-12 00:40:23"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200812004023id_/https://magic.wizards.com/en/articles/archive/making-magic/counter-intelligence-2005-03-28"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/counter-intelligence-2005-03-28"
---


Counter Intelligence
====================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on March 28, 2005 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Before I begin I want to make a quick note about last week's column. Often in my column I'll take a fanciful approach to the topic. Last week (“[The Troubled One](/en/articles/archive/making-magic/troubled-one-2005-03-21)”) I learned I have to be careful what kinds of topics I do that with. If you're interested in a serious recap of last week's column, please take a look [here in last week's thread](http://boards1.wizards.com/showthread.php?t=397285&page=3&pp=30#post5732099) where I rewrote the article with a more serious tone. That said, on with today's topic.

Welcome to *Control* Week! This week we'll be discussing the 2005 fall expansion. (The codename for *Ravnica: City of Guilds* was *Control* – followed by *Alt* (real name: *Guildpact*) and *Delete*.) Now personally I think it's a bit early to discuss the fall expansion – I mean, *Saviors of Kamigawa* isn't even out yet – but I don't pick the theme; I just write what I'm told to. Truth be told, I've been dying to talk about the set for over a year. *Control*, I mean *Ravnica*, is awesome, but, wow, I'm not quite sure where to start. Okay, the whole thing revolves around… what? Not *Control* Week. Control Week! Oops. I just about spilled the beans on the next block's big secret. Whew. That was close.

A quick aside – *Control*, *Alt*, *Delete* has taught us an important lesson about codenames. Don't use game-relevant terms. You have no idea how many times two people started talking about a control deck only to realize halfway into the conversation that they're not talking about the same thing. I think we might need to scrap next year's codenames: *Aggro*, *Combo*, and *Permission*. 

Okay, it's Control Week. This week we'll be talking about a particular style of play. The slow one. Well, most often the slow one. I guess before I continue I should define what we mean by Control. A control deck is a deck that puts all its resources into surviving until it establishes control of the game. Once that happens it wins in one of many ways. Control decks by nature tend to be slower as they are not focused (usually) on winning quickly. One of the most popular types of control decks are permission decks. Permission decks are decks that are primarily blue and establish control by countering the key spells in the opponent's deck. Permission decks are named after the fact that the opponent always ends up asking permission to play their spells. (“I want to play [Wild Mongrel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Mongrel). Can I?”)

The articles this week will focus on many aspects of control decks, but I have chosen to focus in on the design of the key component of permission decks: the counterspell. Today, I will tell you all there is to know about designing counterspells. 

### Step I – Making the Mechanic

![Mystic Denial](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mystic+Denial)To make a counterspell you have to start by making a card that counters a spell. (Thank you. Join me in two weeks when I explain how to design a discard spell.) But seriously, counterspells are unique in that they have a term (“counter”) dedicated to the mechanic. In fact, the term “counter” is so much fun, **Magic** uses it twice (once as a noun and once as a verb) to mean two different things. (See *Unhinged*'s [Ambiguity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ambiguity) for me making fun of this fact.) Technically, the use of the verb counter does not strictly make it a counterspell. The term counterspell tends to be used to refer to spells, which are always instants, rather than permanents that have a similar activated or triggered ability. 


> 
> Quick trivia question –   
> **Q: Name the one sorcery counterspell; Hint: It doesn't become legal in *Vintage* until October 20th.**   
>  A: [Mystic Denial](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Denial) from *Portal*, *Portal: Second Age* and *Portal Three Kingdoms*. You see, the Portal sets didn't have instants so they made a sorcery counterspell that just happens to work like an instant. Shh. The card has since been errataed in Oracle to be an instant.
> 
> 
> 

Second, there are spells that counter things, such as activated abilities, that aren't counter spells in the literal sense as they don't counter spells. But I like to think of them as close cousins. 

That said, there are a number of different types of counterspells. Let's take a quick peek, shall we?


> 
> **A. The Hard Counters**
> 
> 
> The term “hard counter” refers to any counterspell that when played guarantees that the targeted spell will be permanently and definitively countered. Huh? Let me give you some examples:
> 
> 
> [Absorb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Absorb) - ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Discombobulate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Discombobulate) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Dismiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Dissipate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dissipate) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Fervent Denial](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fervent+Denial) – ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Foil](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Foil) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Forbid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forbid) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) – ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Last Word](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Word) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Mana Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Mystic Snake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Rewind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Thwart](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thwart) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
> [Undermine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undermine) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)
> 
> 
> With a hard counter in your hand and enough mana to pay for it, you are guaranteed of countering any spell that your opponent plays (with the sole exception, of course, of uncounterable spells – Isn't **Magic** great?)
> 
> 
> **B. The Soft Counters #1 – The Subset Counterspells**
> 
> 
> These are counterspells that only work on some subset of spells. Examples of these would be:
> 
> 
> ![Annul](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Annul)[Annul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annul) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter an Artifact or Enchantment)  
> [Blue Elemental Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blue+Elemental+Blast) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Red Spell)  
> [Envelop](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Envelop) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Sorcery)  
> [Ertai's Trickery](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ertai%27s+Trickery) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Spell That Had a Kicker Paid)  
> [Flash Counter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash+Counter) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter an Instant)  
> [Gainsay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gainsay) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Blue Spell)  
> [Hisoka's Defiance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hisoka%27s+Defiance) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Spirit or Arcane Spell)  
> [Intervene](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intervene) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Spell That Targets a Creature)  
> [Laquatus's Disdain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Laquatus%27s+Disdain) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Spell Played From the Graveyard)  
> [Remove Soul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remove+Soul) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Creature)   
> [Thoughtbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtbind) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Counter a Spell That Cost 4 or Less)
>  These counterspells are very useful but only in the right circumstance. 
> 
> 
> **C. The Soft Counters #2 – The “Give ‘em an Out” Counterspells**
> 
> 
> These are counterspells that give your opponent the ability to somehow get out of having their spell countered, most often by paying mana. Some examples:
> 
> 
> [Evasive Action](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evasive+Action) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay X More Where X Is Equal To Number of Different Basic Lands You Control)  
> [Force Spike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay One More)  
> [Grip of Amnesia](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grip+of+Amnesia) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Remove Their Graveyard From The Game)  
> [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay Three More)  
> [Miscalculation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Miscalculation) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay Two More)  
> [Override](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Override) – ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay 1 More For Each Artifact You Have)  
> [Power Sink](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Power+Sink) – ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Pay X More)
> 
> 
> These counterspells can act like hard counters in certain circumstances but other times are completely useless. 
> 
> 
> **D. The Soft Counters #3 – The Hard to Use Counterspells**
> 
> 
> ![Abjure](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Abjure)These are counterspells that are almost hard counters but only when the caster can meet the conditions of the spell. Some examples:
>  [Abjure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Abjure) – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Have to Sacrifice a Blue Permanent)  
> [Dispersal Shield](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dispersal+Shield) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Can Only Counter A Spell Equal to Or Less Than a CMC On a Permanent You Have In Play)  
> [Spell Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Blast) – ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Must Pay For X)
> 
> 
> **E. The Soft Counterspell #4 – The “It's Coming Back” Counterspell**
> 
> 
> These are counterspells that stop a spell, but only temporarily. Examples:
> 
> 
> [Ertai's Meddling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ertai%27s+Meddling) – ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Delay for Spell For X Turns)  
> [Memory Lapse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory+Lapse) – ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) (Put the Spell On Top of Owner's Library)
> 
> 
> 

Some spells can fit into multiple of the above categories, but they should serve as a good general idea of the kinds of counterspells available to the designers.

So let's make a card. We do this by examining each of the sections above. Group A tends to be created by taking [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) and adding something to it. Most often this is a new mechanic that we are grafting to the card. But as we have no new mechanics today (well, none I'm prepared to share with you anyway), let's skip Group A. Group B wants to find interesting subsets that haven't been touched yet. Group C is interested in finding new ways to make your opponent pay to keep his spell. Group D is looking for new costs you can pay in addition to mana. And Group E is the constant quest for new ways to not quite counter something. It's by far the hardest category to design for. 

I've decided to try and design for Group B as I discovered a pretty simple idea that had never been done while putting this article together:


> 
> **More Nurture, Less Nature**  
>  ??  
>  Instant  
>  Counter target green spell.
> 
> 
> 

We have our mechanic. Time to move on.

### Step II – Costing the Card

Normally designers don't worry too much about costing. That's development's job. But there is one exception. Sometimes design has to figure out if a space for a card exists at a cost that works. This usually only happens in areas of the game that have been well mined out where the designer can look at the various costs of all the different cards that fill a similar function. Counterspells fall into this camp. There are so many existing counterspells that the designers can examine to see if a certain card fits anywhere on the mana curve without being blatantly better or worse than previous cards.

There are two rules you have to understand when costing a counterspell: 


> 
> ![Vex](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vex)**The First Rule - The ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) Rule**   
>  This is the cardinal rule of costing counterspells. All hard counters must have ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) in its cost. This is true for every hard counterspell in the history of the game save two: *Alliances*' [Arcane Denial](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcane+Denial) and *Darksteel*'s [Vex](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vex) (And hey, **Magic** wouldn't be **Magic** if we didn't break every rule once in a while). This is one of the most consistent rules in all of **Magic** design. The reason behind it is that counterspelling is a very blue ability. If you have access to definitively counter anything R&D believes you ought to be playing a significant amount of blue. 
>  **The Second Rule – Respect Granddad**  
>  Even though [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) is not currently in Standard doesn't mean that it doesn't still have weight around R&D. All costing of counterspells are influenced by the existence of [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell). If the card is worse than [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) it tends to cost less than ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). If it's better, it costs more than ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). 
> 
> 
> 

The net result of these two rules is that most counterspells tend to cost themselves. Let's use More Nurture, Less Nature (shortened to MNLN) as an example. 

So what should it cost? Well, it's worse than [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) so it needs to be less than ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). (Unless, of course, it was stuck in an environment where the ability to counter green was more relevant than normal. This is why in *Mirrodin* design, for instance, we had an [Annul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annul) variant for the same amount of mana that just countered artifacts.) This leaves two options – ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) and ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). 

Next you compare it against existing counterspells. [Annul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annul) (at ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)), for instance, makes the argument that the spell could cost ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) as it allows you the ability to counter a fairly equal amount of cards. But [Gainsay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gainsay) (at ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)) pushes you towards ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) as MNLN is clearly closest in design to [Gainsay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gainsay). In the end, what determines the cost will be the need to leave open design space. Someday we'll probably want to make “Counter target red or green spell” as red and green are blue's two enemies. If we cost MNLN at ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) we cut off our ability to make the second spell. ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) would obsolete MNLN and ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) would be strictly worse than [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell). For this reasons we're going to make the spell cost ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif).

### Step III – Name the Card

Once again, this is really a task left to another team – in this case the Creative Team – but designers usually name their cards and I like to always start by trying to get a real name. Mind you, I don't try for much more than thirty seconds, at which point I give it a funny name or a name that spells out what it is. For the green counterspell above, I chose the former. The name Green Counterspell would be an example of the latter.

Instant names in general want to be verbs (if you're going to use a noun you tend to want to use a metaphor). Inherent in any counterspell name is the flavor that you are trying to stop something. So, let's look at our green counterspell. It obviously needs to tap into the blue/green conflict as it shows one color hosing its enemy. The blue/green conflict is nature vs. nurture. Green believes that everything is born with their destiny preset while blue sees every living thing as a blank slate with the potential to become anything. 

This spell is showing blue trying to hold down green. Thus the name wants to get the sense that it's fighting against green's natural instinct. I start by using a creative writer's best friend, the thesaurus. Here are the synonyms for nurture, the verb, at [www.thesaurus.com](http://www.thesaurus.com):


>  back, bolster, bring up, cherish, cultivate, develop, discipline, drag up, educate, feed, fetch up, foster, instruct, nourish, noursle, nurse, provide, raise, rear, school, support, sustain, tend, train, uphold 

Let's start knocking out names by removing everything that doesn't sound like a counterspell name, that is it doesn't feel like there's any prevention going on. This leaves:


>  discipline, educate, instruct 

Discipline sounds a little too black for my tastes. And instruct feels more like it wants to create change. So we end up with educate. (Not ideal mind you, but the Creative Team will do things like look up more than one word in the thesaurus.) 

### Step IV – Write the Flavor Text

Now I'm going way out of the design process. The only time I ever will put flavor text in a design file is if I come up with something funny that I think will make the other team members laugh. But we've come this far, let's finish the card off right.

For the name we played off the blue/green conflict. It seems only natural to go to the same place for the flavor text. Plus, it's an opportunity to play into the name we've chosen. Okay, so we want to talk about how education plays into blue's strength in the blue/green conflict. Here are a few attempts:

#1 – *Education is a tool that can shape any individual.*   
 #2 – *Those that don't believe in the power of education, simply haven't been taught it yet.*  
 #3 – *You do not know your potential, you are taught it.*  
 #4 – *Your limit is only that of which you are capable of learning.*  
 #5 – *“He thought he knew his place. I taught him otherwise.”*

Because counterspells tend to be a bit confrontational, they tend to like having more aggressive flavor text. This leaves us with #2 or #5. #5 is a little punchier, a little funnier, and a has a little more of the “in your face” feeling that counterspells like to have so I'm going to go with that. This leaves us with the following card:


> 
> **Educate**  
> ![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)  
>  Instant  
>  Counter target green spell.  
> *“He thought he knew his place. I taught him otherwise.”* 
> 
> 
> 

### Counter Intuitive

And thus we come to the end of today's column. As always, I hope it's helped illuminate some areas of the game you haven't had a chance to think about before. If not, well then, there's always next week. 

Speaking of next week, join me when I address a number of comments about R&D. 

Until then, may you have a chance to educate your opponent.

Mark Rosewater







