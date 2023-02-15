
---
[Link to Wayback Machine](https://web.archive.org/web/20150321032022/http://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "Arcane spells have their own dirty little secret. I know most of you buy lots and lots of cards from us, or at least pay attention to them all, but there is a significant portion of the Magic-playing audience that experiences new sets a few packs or a few cards at a time. Some of them only spend $10-$20 on each new set, some of them acquire singles just by poking around in commons bins, and most of them don't read the Internet regularly. So let's say you're one of those people. You open your three packs and you see these cards:"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "289426"
[_metadata_:publish_date]:- "2005-06-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Cost of Arcane"
[_metadata_:wayback_capture_timestamp]:- "2015-03-21 03:20:22"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150321032022id_/http://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/cost-arcane-2005-06-17"
---


The Cost of Arcane
==================



 Posted in [Latest Developments](/en/articles/columns/latest-developments-archive)
 on June 17, 2005 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe










Arcane spells have their own dirty little secret. I know most of you buy lots and lots of cards from us, or at least pay attention to them all, but there is a significant portion of the *Magic*-playing audience that experiences new sets a few packs or a few cards at a time. Some of them only spend $10-$20 on each new set, some of them acquire singles just by poking around in commons bins, and most of them don't read the Internet regularly. So let's say you're one of those people. You open your three packs and you see these cards:


![](https://media.wizards.com/legacy/global/images/mtgcom_daily_af71_picmain_en.jpg)
Now, without any context, what do you think of these cards? One is [Boomerang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boomerang), but a sorcery. One is [Fallow Earth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fallow+Earth), but one mana more. And the last is [Demolish](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demolish), but double red. All have the subtype “Arcane,” but that doesn't appear to mean anything!


That's the dirty little secret—having Arcane on a card's typeline isn't “free,” yet the benefits of it aren't readily apparent. That's not a great place to be in from a design and development standpoint.


Of course, sometimes the original spell is enough “below the curve” that we were able to tack on Arcane essentially for free—[Demystify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demystify), [Fugue](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fugue), and [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot) are now [Quiet Purity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quiet+Purity), [Three Tragedies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Three+Tragedies), and [Waking Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waking+Nightmare). That serves to hide the initial problem, but that problem is still evident. Brandon Bozzi of the creative team once told me a story of a discussion he had with his *Magic*-playing friends from back home in New Jersey that they couldn't for the life of them figure out why in the world we made [Reach through Mists](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists). What good is a card that does nothing else but draw another card?!


Of course, most of you know by now that [Reach through Mists](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists) can (a) help summon forth [The Unspeakable](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Unspeakable), (b) be a splice outlet for cards like [Glacial Ray](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Ray) and [Dampen Thought](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dampen+Thought), and (c) trigger “spiritcraft” abilities like those on [Teller of Tales](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teller+of+Tales) and [Thief of Hope](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thief+of+Hope). But none of that is obvious when you open your pack.


### Parasitism, Good and Bad




![Auriok Glaivemaster](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Auriok%20Glaivemaster&options=)

We throw the term “parasitism” around in R&D a lot. To us it means: “when a card's value is solely dependent on other cards in the same set or block.” In other words, cards that are parasitic have little or no use when mixed with cards from throughout *Magic's* past, but are key components to some larger puzzle in the block in which they were printed. Some parasitic cards, like *Darksteel's* [Auriok Glaivemaster](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auriok+Glaivemaster), are obviously so, as they call out the name of the card type or mechanic they need to work with. Others, like *Odyssey's* [Tireless Tribe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tireless+Tribe), just look really bad until you start seeing potential interactions with flashback, madness, and threshold.



There's gray area as well. [Sosuke's Summons](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sosuke%27s+Summons), for instance, needs Snakes to work well, and there have been a handful of Snakes printed prior to this block. So at least you could in theory build a deck that used it without overloading on Kamigawa cards. But the *best* way to make the card work involves lots and lots of cards from *Champions* and *Betrayers*. Cards with “affinity for artifacts” are the same way. Sure, [Frogmite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frogmite) only costs 3 when you have a [Bronze Horse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bronze+Horse) in play, but the obvious way to use the card is with tons of artifact lands. Are those cards really considered parasitic? Technically I guess not, but they sure feel like it.


There's a lot of good that comes from making parasitic cards. Limited formats (sealed deck and draft) feel different from one another when their main themes are lineal, which often implies some level of parasitism. The *Odyssey* UG threshold draft deck feels and plays different from the *Onslaught* WB Cleric deck, the *Mirrodin* UB affinity deck, and the *Kamigawa* UR splice deck. We want different game play from year to year, and one way to accomplish that is by making one zone or card type matter more, and then printing linear (sometimes parasitic) cards that focus on that zone or type.


Block Constructed (and, to an extent, Standard) varies in the same way. Sometimes the block is slow and plodding and filled with giant spells, like the current one, and sometimes it's really fast, like *Odyssey* and *Mirrodin*. And even then, the slow decks feel different than one another—Astral Slide decks and Gifts Ungiven decks are completely separate animals.


The downside of parasitism is what I was talking about in the introduction. If you aren't drafting or playing Standard or Block, the cards can be kind of “meh.” But why?


### Incurring the Cost


Looking just at the *Kamigawa* Arcane stuff, enfranchised players should be able to see that when the ball gets rolling, it gets rolling well. I can play [Reach through Mists](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reach+through+Mists) with a [Glacial Ray](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial+Ray) spliced onto it which triggers my [Soilshaper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soilshaper) and my [Elder Pine of Jukai](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elder+Pine+of+Jukai). Not unheard of in limited games. So for basically no real cost other than a few mana—the Ray is still in my hand, and I've drawn a card to replace the Reach—I have done 2 damage to something, animated a land, and potentially netted up to three extra cards from Mr. Jukai.


These abilities cannot all be given away for free—the cost for such potential power has to be incurred somewhere. Sometimes the creatures with spiritcraft have to cost a little more, sometimes splice cards have to cost a little more, and sometimes the normal run-of-the-mill Arcane cards incur the cost. We mix it up on purpose, so that one category of cards isn't “all above the curve” whereas the other is “all bad.”


### *These abilities cannot all be given away for free—the cost for such potential power has to be incurred somewhere.*



So when Arcane ends up costing some fraction of a mana, some fraction of the Arcane cards end up costing a mana more than what you might expect. That's where [Uproot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Uproot), [First Volley](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Volley), and other similar cards come in. Yes, they unfortunately look bad on the surface, but as you dig deeper into the set we can only hope you understand why.


### Brand New Effects


Of course, my favorite way of hiding the cost of being Arcane is by making cards with abilities that haven't existed before so that no direct comparison is available. Look at cards like [Petals of Insight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Petals+of+Insight), [Cranial Extraction](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cranial+Extraction), and [Rending Vines](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rending+Vines). Which of those, if any, costs more to play simply because it's Arcane? (Hint: not Extraction.) The answer is well hidden, since in theory these cards could have these costs even if they weren't Arcane—who's to know?


Unfortunately we can't reinvent the wheel every time. Every block needs enchantment removal, simple discard, pump spells, land destruction and the like. Some of them got tweaked a little from previously released versions, some were given splice, and some were simply made Arcane.


And the funny thing is, even though some of them cost more than you're used to, it's often worth it… as long as you're playing the right deck.


### Last Week's Poll




|  |
| --- |
| **How do you feel about the number of new cards released each year?** |
| We release about the right number of new cards per year. | 6787 | 50.3% |
| We release too many new cards per year. | 3047 | 22.6% |
| We release too few new cards per year. | 2511 | 18.6% |
| We release WAY too many new cards per year. | 1156 | 8.6% |
| **Total** | **13501** | **100.0%** |

Every so often we revisit how many cards we're making and if that is meeting players' needs. It looks like the people that think we make too many cards are in the minority, but a sizable minority at that. Good to know.







