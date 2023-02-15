
---
[Link to Wayback Machine](https://web.archive.org/web/20170221205138/http://magic.wizards.com/en/articles/archive/making-magic/eldrazi-and-back-2010-04-19)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Today I'm going to walk through some Rise of Eldrazi cards and share design and development stories with you. Development? Isn't this the design column? It is but I have to let you in on a little secret (okay, not exactly a secret since I told you last week): I wasn't on the Rise of Eldrazi design team, I was on the Rise of Eldrazi development team."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "657401"
[_metadata_:publish_date]:- "2010-04-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "To Eldrazi and Back"
[_metadata_:wayback_capture_timestamp]:- "2017-02-21 20:51:38"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170221205138id_/http://magic.wizards.com/en/articles/archive/making-magic/eldrazi-and-back-2010-04-19"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/eldrazi-and-back-2010-04-19"
---


To Eldrazi and Back
===================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on April 19, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Today I'm going to walk through some *Rise of Eldrazi* cards and share design and development stories with you. Development? Isn't this the design column? It is but I have to let you in on a little secret (okay, not exactly a secret since I [told you last week](/en/articles/archive/rise-part-iii-2010-04-12)): I wasn't on the *Rise of Eldrazi* design team, I was on the *Rise of Eldrazi* development team.


How did that happen? Well, I wasn't on the *Rise* design team because I was a little swamped with other design teams. For starters, I was designing back-to-back large fall sets (for the trivia buffs out there, I was the second person to do such; Mike Elliott did so with *Urza's Saga* and *Mercadian Masques*) as well as being on the *Worldwake* design team (it was Ken Nagle's first time as a lead, and I'm also on all sets of a designer's first lead, kind of like how your first parachute jump is normally a tandem jump). 


While I mostly work on design teams, I got my start on development teams (for my first four or so years I was on every **Magic** development team—all of **Magic** R&D, was as there were so few of us). The developers like having a designer on the teams as we're good for fixing cards on the spot in ways other than just tweaking numbers. Since I wasn't involved of the design of *Rise* it seemed like a good time to be on a development team. This would guarantee that I had plenty of opportunity to get to know the set.


With the exposition out of the way, let's get to the stories:


### Dreamstone Hedron


![Dreamstone Hedron](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dreamstone+Hedron)
  
Yes, this was designed to be three [Mind Stone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Stone)s combined into a single card. We took every number on [Mind Stone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Stone) and multiplied by three.


### Explosive Revelation


![Explosive Revelation](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Explosive+Revelation)
  
This card was turned in from design as a repeat of [Erratic Explosion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Erratic+Explosion). The design team loved how [Erratic Explosion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Erratic+Explosion) interacted with the giant converted mana costs in the set. The problem we had with the card was that [Erratic Explosion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Erratic+Explosion) put the revealed card on the bottom of the library. In playtests we would find that players were hoping to not pull their Eldrazi because they wanted to play it, and if [Erratic Explosion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Erratic+Explosion) hit it, they essentially lost it. The development team really liked what this card was trying to do, so we made one small tweak (okay, one big tweak). Instead of losing the card in question, you now got to draw it. This made you doubly excited to get your Eldrazi because you got to do a whole lot of damage *and* draw the Eldrazi. This "little" change did require us to add two mana to the mana cost (one converted to red).


### Goblin Tunneler


![Goblin Tunneler](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Goblin+Tunneler)
  
One day last month as a treat to **Magic** R&D for our work on *Rise of the Eldrazi* (and **Magic** in general) Aaron set aside a Tuesday afternoon to eat pizza and do a draft with actual *Rise of Eldrazi* cards. While we've done many drafts with the set, nothing compares to doing a draft with actual printed cards, so we're always very excited to get our hands on real cards for the first time. I tweeted a teaser about the draft (slang for posting on Twitter—I'm @[maro254](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=twitter.com/maro254) if you'd like to follow me):


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm87_tweet.jpg)  
This was the card I was talking about. The Alpha card was [Dwarven Warriors](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dwarven+Warriors).


![Dwarven Warriors](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dwarven+Warriors)
  
This card is the same except it is a mana cheaper and a Goblin instead of a Dwarf. The deck I was drafting was a blue-red deck that's all about breaking through the stalemate. [Goblin Tunneler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Tunneler) is a key part of the deck. Here are a few other cards the deck likes:




|  |  |
| --- | --- |
| Kiln Fiend | Valakut Fireboar |

### Guul Draz Assassin


![Guul Draz Assassin](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Guul+Draz+Assassin)
  
Originally the Assassin leveled up to tap to destroyed tapped creatures (a la [Royal Assassin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Royal+Assassin)) and then at the next level up it tapped to destroy any creature (a la [Visara the Dreadful](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Visara+the+Dreadful)). This turned out to be too good, so we ended changing the effect to -N/-N.


### Heat Ray


![Heat Ray](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Heat+Ray)
  
One of my pet peeves is ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) spells at common. Our research has shown that ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) spells confuse many players and as such I like to keep them out of common. I do like ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) spells, by the way—this campaign is to make them more awesome but less common. Anyway, the design team put this repeat in at common because it matched their goal of removal that was good but worse at destroying larger creatures. The card was so beloved by so many on the design and development teams that it stayed at common even though it was an ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) spell. Don't take this as a precedent though—common ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif) spells are going to be an infrequent thing.


### Hellcarver Demon


![Hellcarver Demon](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hellcarver+Demon)
  
A 6/6 demon with a converted mana cost of 6: 6-6-6. I always talk about the importance of details in design, as little things like this that don't mean much on a grander scale but do add up to positively increase the overall enjoyment of the game. Yes, there is a fourth six in the rules text. I guess we just had six on the brain.


### Knight of Cliffhaven


![Knight of Cliffhaven](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Knight+of+Cliffhaven)
  
One of my favorite **Magic** design topics is the importance of aesthetics in design. Humans crave certain things, and as designers it is our job wherever possible to try and maintain aesthetics so things just "feel better." One of the places I pushed for that in *Rise* was with the power / toughnesses on the levelers. Because each creature with level up had three stats, I tried real hard to make sure that the three evolutions had flow. That is, if you saw the first change in power/toughness stats, you could accurately predict the second one. Here, for example, are a few from white:




|  |  |
| --- | --- |
| Hedron-Field Purists | Ikiral Outrider |



|  |  |
| --- | --- |
| Kabira Vindicator | Transcendent Master |

While some are vaguer than others most of the levelers have a flow to their power/toughness progression. One of the few hold-outs was this card. I tried so hard to make this card 2/2, 3/3, 4/4, but the numbers never quite worked out.


### Might of the Masses


![Might of the Masses](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Might+of+the+Masses)
  
This card was created by the design team ... of *Scars of Mirrodin*. Yes, for about six months this was a card from the fall 2010 set. How did it end up in *Rise of the Eldrazi*? Well, Matt Place was both the lead developer for *Rise* and on the design team for *Scars of Mirrodin*. One day he cut a green card and was looking for something that fit in green that helped a deck with a lot of Eldrazi Spawn creature tokens. He said he wanted something like [Might of the Masses](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Might+of+the+Masses) from *Scars of Mirrodin*. I asked him, "How about [Might of the Masses](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Might+of+the+Masses)?" While the card was doing good work in *Scars*, it wasn't essential to the set. If Matt felt *Rise* needed it, they could have it. It was out of the *Scars* file and into the *Rise* file before the end of the day.


### Mortician Beetle


![Mortician Beetle](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mortician+Beetle)
  
When we build a card to help a particular strategy, sometimes we are blunt and sometimes we are subtle. This is a more subtle "play with Eldrazi Spawn creature tokens" card.


### Near-Death Experience


![Near-Death Experience](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Near-Death+Experience)
  
When we got rid of mana burn, I talked about how there were areas of design that mana burn prevented us from making. Here is one such example. With mana burn gone, you'll see little by little this design space starting to see print.


### Regress


![Regress](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Regress)
  
You'll notice that in *Rise of the Eldrazi* bounce (cards that put permanents back into their owner's hands) are light both in quantity and in quality. The reason for this is that the set is all about getting giant creature onto the battlefield. Plentiful and cheap bounce spells makes such an environment hard to build, so by necessity we excised most of it from the set.


### Shrivel


![Shrivel](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shrivel)
  
The Eldrazi Spawn creature tokens were created as a means to enable players to get the colorless Eldrazi creatures onto the battlefield. Pretty soon the designers and developers were finding lots of other cool ways to make use of all the 0/1 tokens—so much so that development felt a need to make an answer to it. What do you do if your opponent is spitting out a horde of Eldrazi Spawn creature tokens? If you're playing black, you kill them all. 


I'm sure one day I'll write an entire column on this topic, but let me quickly give one paragraph to the cause. A set cannot just have new threats; it must also have the answer to those threats. One of the best things about **Magic** is how it is able to adapt. No one strategy is unbeatable, because the metagame can always shift to fight it. This means that the designers and developers have to always be conscious of how to fight the forces we are unleashing in the same set.


### Sphinx of Magosi


![Sphinx of Magosi](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sphinx+of+Magosi)
  
Design goes through fads just like any creative endeavor. A current trend is "get A & B, either of which you'd be happy to get." This is most often used in the activation of Timmy-friendly giant monsters, almost exclusively at rare and mythic rare.


### Time of Heroes


![Time of Heroes](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Time+of+Heroes)
  
The earliest version of this card gave +1/+1 to each creature for each level counter on it. Besides needing to cost a lot, it had a bigger problem. Right now, once you've reached the third level-up plateau there is no need to keep adding level counters, meaning you can stop worrying about leveling up the creature. If a card like the original [Time of Heroes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+of+Heroes) existed, though, it would force you to keep growing your levelers "just in case." We tried hard in design and development to weed that kind of activity (mostly meaningless but necessary to eke every advantage out of the card) out of the set.


### Ulamog's Crusher


![Ulamog's Crusher](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ulamog%27s+Crusher)
  
[Ulamog's Crusher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulamog%27s+Crusher) is one of two common colorless Eldrazi (note that for the rest of this blurb when I say "Eldrazi," I mean the big colorless Eldrazi). It features in my favorite developer story of the set. One of the things we do during development is to bring **Magic** players from elsewhere in Wizards to playtest our sets. It's important to get a sense how people react to the set when they play it for the first time, so we like to hold playtests with fresh eyes and a more casual sensibility. During the first such playtest, we noticed that when players got an Eldrazi out, they wouldn't attack with it. R&D had quickly realized the power of the annihilator mechanic, but the less experienced players didn't seem to feel safe throwing their giant creatures into the fray.


We took notes and talked about it, but changed nothing. The next playtest the same thing happened, and the playtest after that. During one development meetings we had a discussion about what we could do to make less experienced players realize that you should be attacking with the Eldrazi. (Quick aside—Less experienced players: When you get an Eldrazi on the battlefield, attack with it.) How about, I suggested, we take the cheapest common Eldrazi and add the text "CARDNAME attacks each turn if able." Once players saw how much damage the Eldrazi did when they attacked, hopefully that would encourage them to attack with the other Eldrazi. And that is how [Ulamog's Crusher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulamog%27s+Crusher) got its second line of text.


### Vendetta


![Vendetta](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vendetta)
  
This was one of the first cards Brian put into the file once the idea of "battlecruiser **Magic**" was decided upon. Brian loved how the card was good at killing creatures but much painful when used against the giant creatures of the set. The card never left the file.


### Wall of Omens


![Wall of Omens](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wall+of+Omens)
  
I'll admit I was a little surprised how many players got upset that we made [Wall of Blossoms](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Blossoms) into a white card rather than a blue card. So what is this doing in white? For starters, everything that the card is doing is white from a color pie perspective. White is the most defensive color and is one of the primary defender colors (although less so in *Rise of the Eldrazi*, where defenders are more spread out. Every color gets cantrips. All cantrips on permanents are done as "enter the battlefield" triggers. Traditionally we've done most of our creature cantrips in green. Blue is number two, as we often do draw triggers in blue and "enter the battlefield" is an often used trigger in design. 


Why then did we do it in white? Because at the time we were finding more ways to pump up white. When this set was in design and most of development, the Faerie deck was tearing up the tournament scene. No one was complaining about the power of blue at the time. Players were complaining about white. It's easy to forget that we work far ahead, and as such do not have the ability to react as quickly as people sometimes assume we can.


There's also one other major reason why the card went to white instead of blue. This card:


![Mnemonic Wall](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mnemonic+Wall)
  
Blue already had a 0/4 Wall that drew it a card when it entered the battlefield. We wanted a [Wall of Blossoms](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Blossoms). Green didn't need it because it had some other walls we wanted. Blue couldn't use it because of [Mnemonic Wall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mnemonic+Wall), so we put it in the color that made the most sense, white. It was defensive and it helped give white some power in a different place than it currently had. *That* is why [Wall of Omens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Omens) is white.


### In the Cards


That's all I got for today. I hope you enjoyed my jaunt through the cards. Join me next week when I talk about pulling out the big guns.


Until then, may you create some stories of your own with *Rise of Eldrazi* cards.


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/LAUNCH_ROE-Article-Banner-620-Wide-Template.jpg)](http://www.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prerelease-facts)
  






