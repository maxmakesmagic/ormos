
---
[Link to Wayback Machine](https://web.archive.org/web/20210429091648/https://magic.wizards.com/en/articles/archive/making-magic/imprints-charming-2010-11-29)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Welcome to Imprint Week. This week we'll be talking about one of my all-time favorite mechanics. Interestingly, even though this is the second block (making it the fourth set) to feature imprint, we've yet to have an Imprint Week! Well, that all gets fixed today.Just because there hasn't been an Imprint Week doesn't mean there hasn't been an imprint column. I was so excited"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "653056"
[_metadata_:publish_date]:- "2010-11-29"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Imprints Charming"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 09:16:48"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429091648id_/https://magic.wizards.com/en/articles/archive/making-magic/imprints-charming-2010-11-29"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/imprints-charming-2010-11-29"
---


Imprints Charming
=================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on November 29, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to Imprint Week. This week we'll be talking about one of my all-time favorite mechanics. Interestingly, even though this is the second block (making it the fourth set) to feature imprint, we've yet to have an Imprint Week! Well, that all gets fixed today.

Just because there hasn't been an Imprint Week doesn't mean there hasn't been an imprint column. I was so excited about [imprint](/en/articles/archive/making-magic/someday-my-imprints-will-come-2003-09-01) that it was the very first thing I talked about during the first *Mirrodin* Preview Week. That means if you are interested how imprint was created, I'd hit the link and go check it out. So how did it get into *Scars of Mirrodin*? We were returning to Mirrodin and I just said it was one of my all-time favorite mechanics. There was never any doubt in my mind it was coming back. 

![Clone Shell](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clone+Shell)  
This all leads to the big question: what am I going to write about today? I've learned when we hit a mechanical theme week where I've already written about the mechanic in question, I like to pull back the scope of the article. Instead of talking about imprint, I'd like to talk about an important part of design that imprint is part of. Combine this with the fact that I've been living and breathing the GDS2 first Design Challenges (where the final 8 had to design commons from their set of a chosen color; judging and elimination in [Show #2](http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/118z) last Wednesday), and I got my topic for the day.

Let me start by giving you a list of mechanics and you telling me what they have in common:

Imprint, proliferate, champion, hideaway, split second, split cards and flip cards.

The answer is that none of them appeared at common. All of these mechanics existed only at uncommon and higher rarities. Why is this? There are a few reasons that I'm going to walk you through.

### Reason #1: Complexity

First and foremost, most of these mechanics are more complicated than the average mechanic. This isn't a bad thing. **Magic** has room for mechanics of various complexities, but be aware that the scale for the game as a whole is not the same as the scale for common. In other words, there are things that the game can handle that the rarity of common cannot. **Magic** still gets to have all the mechanics listed above. It just has to be careful where it uses them.

Whenever I'm asked what the hardest cards are to design for **Magic**, I always answer commons (red commons specifically, if you care). The reason is that the game can handle much more complicated mechanics than we want sitting at the lowest rarity. (Yeah, yeah "basic land" is technically the lowest rarity.) Common design requires boiling down your ideas to their simplest version. While a mechanic like imprint is cool and flavorful, it's hard to boil down.



|  |  |
| --- | --- |
| Mimic Vat | Contagious Nim |

One of the most common comments I made on the first Design Challenge submissions was the desire for the designers to put mechanics at common that had no place there. Here are the most common warning signs that your common mechanics are too complex: (for examples I am going to use mechanics turned in by the GDS2 Top 8 for the first Design Challenge; be aware I'm not trying to pick on these guys—they're doing well given the restraints they're under—it's just the most public example of amateur design we have)


> 
> **The card text is five lines or more (in excess of forty words) when written out in the text box including reminder text.** My example for this guideline will be Jonathan Woodward's swarm mechanic. While this mechanic is somewhat clean conceptually (it allows a bunch of creatures to attack together), it is messing with an aspect of the rules that is very complex. As such, to properly write it out would require a mountain of text—much more than we want to see on a card at common.
> 
> 
> **The rules text has to use a Magic vocabulary word you don't often see written on cards.** I don't have an example of this rule from GDS2 because it was broken a number of times during GDS1 (numerous designers really wanted the word "the stack" on their cards) and the judges came down hard. Because of this, this round of designers mostly avoided this pitfall.
> 
> 
> **The card has a built-in effect that R&D does not typically put at common.** My example for this guideline would be Jonathon Loucks' living reflection mechanic. It makes use of copy effects. Can you think of the last time you saw a copy effect at common? If we're unwilling to put a single one-of card at common, we're not willing to put an entire mechanic that uses it at common. (Note I *am* a fan of this mechanic, it just doesn't have any place at common—well, at least if it's planning to copy things.)
> 
> 
> **The mechanic messes around with an aspect of the rules that has a page or more of notes in the comp rules.** My example for this guideline is Jonathon Loucks' living reflection mechanic again. If you've never read the comp rules write-up on copy effect, click [here](http://www.wizards.com/magic/comprules/MagicCompRules_20101001.txt) and search for "706. Copying Objects". As you can see, it's over a page.
> 
> 
> **The mechanic messes around with an aspect of the game that has appeared on two or more restricted or banned cards.** My example for this guideline is Jonathan Woodward's favored mechanic. Favored allows you to have a chance to cast Auras for free on creatures with this ability. "Casting things for free" has probably created more banned and restricted cards than any other category (I guess "draw a lot of cards" comes close). 
> 
> 
> **The mechanic requires substantial amount of monitoring.** My example for this mechanic is Jonathon Louck's illuminate mechanic. It allows you to exile cards for various effects. Any of the exiled cards can be drawn in place of a normal draw. This means that for every draw you have N +1 options to weigh where N is the number of exiled cards. We only needed one playtest to realize the complexity in processing the information available.
> 
> 
> 

A simpler way to think of it is this. If you showed your design to a player that has never seen it before, would they understand what it does at first glance, in under a minute. I'm not asking would they understand the impact on the game or how to play it correctly, just do they understand what actions the mechanic is doing. If the answer is no, then the mechanic probably doesn't want to be at common.



|  |  |
| --- | --- |
| Gathan Raiders | Knight of Cliffhaven |

But wait, doesn't a mechanic like level up or morph break that rule? They both do. Putting level up at common was a giant fight during *Rise of the Eldrazi* development, and if morph were introduced today there would be long talks about what to do with it (the mechanic requires volume to do what it wants to do). There are times when we will push the boundaries at what's common and I'll talk more about that below.

### Reason #2: Lowering "As Fan"

Developer Erik Lauer hates talking about making guidelines based on rarity because to him (a very mathematically minded person) the issue at hand today isn't rarity but what we in R&D call "as fan." To give an example: Let's take the expansion *Champions of Kamigawa*. Of the 301 cards in the expansion, how many are legendary cards? The answer is 85. Using my handy calculator (I studied words in college, remember?), I discover that legendary cards make up just over twenty-eight percent of the set. So, if I open a pack of *Champions of Kamigawa*, I should expect on average of having four legendary cards (just over twenty-eight percent), right?

![Brothers Yamazaki](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Brothers+Yamazaki)  
I don't. The reason being that most of the legendary cards are rare (65) with the remainder being uncommon (20). Yes, it's possible to open four legendary cards if my one rare and all three uncommons are legendary, but it's far from likely. What "as fan" looks at is what are my percentage chances of opening a card given that ten of the cards are common, three uncommon and one rare. (The fifteenth card is a basic land.) 

Erik's big point is that we have to limit things not by rarity but by "as fan." Two particular uncommon cards show up roughly at the same rate as one particular common card. Putting something on twenty uncommon cards is the same as putting it on ten commons. 

The reason I bring this all up is that sometimes, we pull mechanics out of common because it's the easiest way of getting the "as fan" down. We don't want the mechanic to show up above a certain amount so we put it at uncommon to help lower how much it shows up. This is the big reason behind proliferates pull out of common. It wasn't that the mechanic was too complicated but rather that development felt it needed to show up in smaller numbers. 

### Reason #3: Splash

Not all decisions are game play based. Let's take split cards from *Invasion* (and *Apocalypse*, *Dissension*, and *Planar Chaos*) The reason they don't appear at common isn't one of complexity (although to be fair they do add more complexity to the game than most players realize) or even "as fan," but one of impression. We had this very cool mechanic that had a unique layout and felt more special than the average run of the mill mechanic. 



|  |  |
| --- | --- |
| Assault // Battery | Night // Day |

We wanted to keep the mechanic feeling special, so we made the choice to not put it at common because we wanted the feeling that this mechanic, well, wasn't common. We wanted to create some "splash" (R&D slang for having an appeal above and beyond the card text). 

As I'm drumming into the heads of the GDS2 designers, a design not only has to be played, but it also has to be sold. A designer has to make his mechanics fun and he has to make them attractive. Sometimes to do that, he plays around with the card's rarity to make feel a little more special.

### Common (and Uncommon) Knowledge

The important lesson of today's column is that a designer has to understand what rarities his mechanic needs to be in. A mechanic shouldn't go where the designers want it to go but rather where the mechanic needs to be. This means that it's a designer's job to figure out where each mechanic belongs. One of the harsh lessons for the GDS2 designers is that mechanics don't always play along with your grand vision. Yes, it would be nice if mechanic X went at common but if that isn't where it belongs you are doing a disservice to your design to try and force it there.



|  |  |
| --- | --- |
| Contagion Clasp | Steady Progress |

This also has a much larger implication. I often say that "if your theme isn't at common, then it isn't your theme." Combine that with "mechanics have to go at the rarity they need, not the rarity the designer wants" and what do you get? Yes, there are mechanical themes you can't build a set around because they can't go at common. Not every design can necessarily be done.

That said, often if you have a solid vision you can revisit what mechanics you need. So this isn't saying that because your first pass at mechanics ended up with ones unusable at common that you have to throw your vision out. (Good news GDS2 applicants!) What it means is that you have to get at the core essence of your vision and find a different mechanic execution.

At the core, this is the real skill we're testing in the GDS2. Having vision is important (and it's a skill that many designers aren't particularly good at) but having the ability to find a mechanical tie that connects with your vision is even more important. The reason the second Design Challenge is still about making commons is that until the designers figure out the core of their set, which as I just explained has to live at common, they don't have the foundation they need to build their set.



|  |  |
| --- | --- |
| Qasali Pridemage | Noble Hierarch |

The reason commons are so hard to design is because they are so important to your set, yet have the most restrictions placed upon them. Luckily, "restrictions breed creativity." There is a reason I strongly believe **Magic**'s not going to run out of ideas. Richard Garfield made a game with such depth that each time we approach making a set, if we do so from a different vantage point we will find new swaths of design space.

### Imprinting Press

Which brings us back to imprint, and mechanics like it. These kinds of mechanics are never going to be what you build a set around. That isn't a bad thing. Not every tool is a hammer. My dad is very into woodworking. From time to time I'll ask him what some tool does and it takes him five minutes to explain to me why something has to occasionally be done to even explain what the tool does. Every tool has to have its function and that function can be very specialized.

Imprint is what I like to think of as a "spice mechanic." That is, it adds flavor and seasoning. You don't want too much in your "dish" but a little can go a long way. In fact, the beautiful thing about imprint is that all it takes is one card to do wonderful things. Imprint started with [Soul Foundry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry) (originally called Clone Machine) back in *Urza's Saga* design. 

![Soul Foundry](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul+Foundry)  
The thing I love about [Soul Foundry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry) is that two people can have [Soul Foundry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry) decks (that is decks built around [Soul Foundry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry)), and their decks could be miles apart. One could be a Timmy deck and another a Johnny deck. One could be aggro and another combo. One could be red and another blue. And each new set brings even more things you can do with the card. And I'm just talking about one imprint card. The mechanic can do so much with so little. That is the role of a spice mechanic: to add a lot with a little space. 

### But Wait, There's Morph

Things don't always work out so easily in **Magic** design. Let's take the example of morph. From a complexity standpoint, morph is a bit much for common. It requires you learning a whole slew of new rules and it doesn't work the way you think it does (unlike most other things in the game, turning a creature face up does not use the stack).



|  |  |
| --- | --- |
| Bane of the Living | Chromeshell Crab |

So Rule #1 says to bump morph from common. But, morph is a bluffing mechanic that requires enough cards to allow the ability to bluff. If morph only appeared on one cycle of uncommons, there would be very little suspense when the morph card is played face down. Morph needs volume, which means it fights against Rule #2. Morph needs a higher, not lower, "as fan."

My point talking about morph is that these rules I've laid down are not hard and fast. Some mechanics pull in opposite directions and it's the job of the lead designer to figure out what best serves the mechanic and the set.

### All The News That's Fit To Imprint

I hope my column today has given you a slightly different way to look at mechanics. Imprint does wonderful things, but at the same time brings restrictions with it that the designer has to adapt to. This is something the GDS2 designers are learning, and something that every card designer has to come to grips with. Coming up with a great mechanic is only the first step. The designer then has to figure out how best to use it.

Join me next week when I continue my tiptoe through the tulips of *Scars*.

Until then, may all the things in your life find their rightful place.

[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/Worlds_Chiba_Banner.jpg)](http://www.wizards.com/Magic/TCG/Events.aspx?x=events/magic/worlds)  






