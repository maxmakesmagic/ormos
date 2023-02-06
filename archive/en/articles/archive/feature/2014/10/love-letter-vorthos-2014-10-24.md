
---
[Link to Wayback Machine](https://web.archive.org/web/20141025164957/http://magic.wizards.com/en/articles/archive/feature/love-letter-vorthos-2014-10-24)

[_metadata_:description]:- "Commander (2014 Edition) design and development."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2014-10-24"
[_metadata_:title]:- "A Love Letter to Vorthos"
[_metadata_:wayback_capture_timestamp]:- "2014-10-25 16:49:57+00:00"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20141025164957id_/http://magic.wizards.com/en/articles/archive/feature/love-letter-vorthos-2014-10-24"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/love-letter-vorthos-2014-10-24"
---





### FEATURE


A Love Letter to Vorthos
========================



![](https://web.archive.org/web/20170709072651im_/http://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)

Ethan Fleischer and Ian Duke




October 24, 2014
 










I'm Ethan Fleischer, lead designer of *Commander* (2014 Edition). I am so excited about C14! I have a lot of great stories to tell about how it was designed, and not much space because I'll be sharing this article with Ian Duke, who was the lead developer on the product. Say hello, Ian.


Hi everyone! I'm a core developer in *Magic* R&D, which means I focus on game balance and making sure awesome designs are also fun to play. I led the development of *Vintage Masters* for *Magic Online*, but *Commander* (2014 Edition) is the first physical card set I developed. Having played *Magic* for more than 18 years, I was incredibly excited to do my part in bringing new cards to all of you.


**Ethan:**  *Commander* (2014 Edition) is the latest release in our annual *Commander* series. If you're interested in playing Commander, you can buy one of these five decks and start playing right out of the box. For experienced Commander players, we've included new cards, new commanders, exciting reprints, and other goodies. In this article, Ian and I will talk about how this year's product was designed and developed.


![](https://media.wizards.com/2014/images/daily/logo_c14.jpg)
Nostalgia for Nostalgia's Sake
==============================


**Ethan:** I have a confession to make: I love *Time Spiral*. It was a set that was all about nostalgia for *Magic*'s past, and it included a plethora of references to old *Magic* cards. I've played *Magic* since Alpha, so I was absolutely the target audience of *Time Spiral*. One of my favorite things about the set was the legendary creatures. They were all characters referenced in flavor text on older cards, but who had never appeared as legendary creatures before, such as [Jaya Ballard, Task Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jaya+Ballard%2C+Task+Mage); [Endrek Sahr, Master Breeder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Endrek+Sahr%2C+Master+Breeder); and [Norin the Wary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Norin+the+Wary).


A supplementary product like *Commander* seemed like the perfect place to indulge in such rampant nostalgia again, so before design even began I decided to make a cycle of legendary creatures that were *Time Spiral*-style throwback characters.


**Ian:** In that sense, Ethan and I were the perfect pair to work on the design and development of this set. Among the developers, I'm probably the one who is most fond of early *Magic* story and characters. The epic fantasy feel of early sets like *Antiquities*, *Ice Age*, and *Mirage* are what drew me into the game, so I fell in love with the prospect of bringing some of those characters to life on new cards.


**Ethan:** The first *Commander* release had included three-color "wedge" decks, with commanders that were a color and its two enemies. *Commander* (2013 Edition) had five three-color "arc" or "shard" decks, with commanders that were a color and its two allies. I had recently read an article by Devon Rule, "[1,000 Commander Decks](http://www.gatheringmagic.com/devonrule-040612-1000-commander-decks/)," where my fellow [Great Designer Search 2](http://magic.wizards.com/en/articles/archive/great-designer-search-2-2011-03-07) finalist and current [Commander rules committee](http://mtgcommander.net/rules.php) member broke down 1,000 decklists submitted by members of the [mtgcommander.net community](http://mtgcommander.net/Forum/). Hmmm...monocolored decks were surprisingly popular! I had several monocolored Commander decks myself and had a pretty good handle on what the pitfalls were for such decks. Maybe I could make some monocolored commanders that enabled new types of decks, and provide monocolored decks with a few new tools to help them work a bit more smoothly.


I wasn't sure, though. Monocolored decks would be facing an uphill battle. Multicolored cards are inherently exciting to players, and multicolored legendary creatures are ESPECIALLY exciting to Commander players. Was there some design space that could blow this product into super-land?


Two Super-Teams
===============


**Ethan:** I couldn't go on alone. I needed help to make this thing happen. Fortunately, it was time to start designing, and I was leading a great team:


![](https://media.wizards.com/2014/images/daily/c14devign_emmons.png)
Dan Emmons—Dan recently quit working for Wizards of the Coast so he could become a famous online media star, but when we worked on *Commander* (2014 Edition) he was one of the core *Magic* designers. Dan is a prolific designer, and we had a good rapport going as we had just finished working together on *Journey into Nyx*. Dan was in charge of the blue deck.





![](https://media.wizards.com/2014/images/daily/c14devign_forsythe.png)
Aaron Forsythe—Aaron is the director of *Magic* R&D. He's generally responsible for making the tough calls and steering the ship, philosophically speaking. I'd never had a chance to work with Aaron on a design team prior to C14, and I was in for a treat. Aaron was bursting with exciting and innovative card ideas. Some of them, such as Bat Box, were too weird to print, but we made plenty of them work. Aaron was in charge of the green deck.





![](https://media.wizards.com/2014/images/daily/c14devign_hata.png)
James Hata—James is a designer for *Duel Masters*, our other trading card game. Most of the members of *Duel Masters* R&D play Commander, and I knew I wanted to get one of them onto my team. I basically requested each of them by name, and James was the one with time in his schedule. James proved to be absolutely dependable; he nailed everything on the first try. James was in charge of the black deck.





![](https://media.wizards.com/2014/images/daily/c14devign_rapkin.png)
Charles Rapkin—Charles works in our organized play department and is an avid Commander player. Charles has a great understanding of what makes the format fun and really sunk his teeth into the project. He was in charge of the white deck. He loves Cat tribal.





![](https://media.wizards.com/2014/images/daily/c14devign_fleischer.png)
Ethan Fleischer—I'm a full-time *Magic* designer. I took a week vacation after I finished leading *Journey into Nyx* design and then immediately launched into *Commander* (2014 Edition) design. I felt pretty confident and really enjoyed the process; leading a *Commander* set is a lot easier than leading an expansion release, so I could stop to smell the roses along the way.





**Ian:** While design is responsible for creating the overall vision of the set, the second half of the R&D process (development) focuses on realizing those goals by balancing the cards and the decks and making the set really fun to play. Here's the team that developed the set:


![](https://media.wizards.com/2014/images/daily/c14devign_globus.png)
Mark Globus—Mark is a principal game designer in *Magic* R&D. One of his many roles is to think about the entire suite of *Magic* products we make—from Intro Packs to the *Magic Online* Cube—and make sure they're serving the *Magic* audience as well as possible. He led the development of the original *Commander* release, and his experience and expertise were invaluable to the team.





![](https://media.wizards.com/2014/images/daily/c14devign_lee.png)
Peter Lee—Peter is a game designer who has been with Wizards for many years and worked on a variety of games, including *Dungeons & Dragons*. Among Peter's many strengths is the emphasis he places on simple and elegant design. He was instrumental in keeping us on track when complexity was getting in the way of fun.





![](https://media.wizards.com/2014/images/daily/c14devign_mccall.png)
Max McCall—Max has since moved on from Wizards, but his role at the time was as a liaison between *Magic* R&D and our digital offerings, like *Magic Online* and *Duels of the Planeswalkers*. Max is an avid competitive Commander player. He did a great job tuning the decks and getting their various themes to work. He also helped us design and develop cards to be powerful, but healthy, for both casual and competitive Commander play.





![](https://media.wizards.com/2014/images/daily/c14devign_emmons.png)
Dan Emmons—Dan was also on the development team. We typically have one person carry over from design to development in order to make sure that development stays on course with design's vision for the set. Dan was great at helping us design new cards to replace ones that weren't working during the development process.





Planeswalk the Walk
===================


**Ethan:** The previous *Commander* product had explored the design space of how commanders interact with the command zone. I was interested in seeing what other space was available to us that was unique to the Commander format. I did some brainstorming with the design team, writing various ideas onto the whiteboard. I thought of the line of rules text, "CARDNAME can be your commander." What if there was a living spell, a sorcery that could be your commander? Or what about other card types? Someone in the room behind me said, "Planeswalker." ZING! THAT WAS IT!!!


![](https://media.wizards.com/2014/c14/aakdfnppleih2/en_02o6l1d6f0.png)
Creatively speaking, Planeswalkers are basically the same as legendary creatures, except they can, y'know, planeswalk. Plenty of players had experimented with using Planeswalkers as commanders already; some people wanted to do it and were already doing it. I organized a playtest where we replaced the commanders of some decks with Planeswalkers to sanity-check the idea. It was sane! Completely sane!


We just had to design these Planeswalkers to be a little different from regular Planeswalkers; some effects would be un-fun in Commander, and some of the numbers might need to be different. We started with mechanically inspired designs, not trying to match the flavor of any particular characters. Once we had some designs we were happy with, we judged that some of them were close enough to the mechanical identities we'd established for Ajani, Liliana, and Nissa that we could nudge them a bit to fit those characters. The blue and red Planeswalkers would have to be new characters.


Little did we anticipate the massive upheaval that was in store for our Planeswalkers during development...


**Ian:** We knew that getting the Planeswalkers right would be one of the most important parts of the development process. In *Commander* (2014 Edition), as in many *Magic* sets, the final Planeswalker designs were created during that development process. That's because Planeswalkers have so many knobs. "Knobs" are how development refers to parts of a card that we can change to adjust its overall power level. A typical Planeswalker's knobs include its mana cost, its starting loyalty, what each of its three abilities cost, and what each of those abilities *do*. Within that, each *individual ability* may have one or more knobs on it! Planeswalkers typically get at least partial redesigns several times during the development process.


Early in development we invited the *Magic* creative team into the conversation to discuss just who our Planeswalker characters should be. Design had turned over versions of Ajani, Liliana, and Nissa, along with designs for red and blue Planeswalkers that didn't fit existing characters. Ultimately, we determined that reusing characters would impede our ability to tell coherent stories about where those characters are and what they're doing in the current *Magic* storyline (*Commander* (2014 Edition) itself is sort of "out of place in time," in that it combines snapshots of characters from various times throughout *Magic*'s history).


![](https://media.wizards.com/2014/images/daily/art_pantheon.jpg)
Once we knew we'd be avoiding characters who are already busy elsewhere in the *Magic* storyline, Ethan and I saw an opportunity to play into the set's theme of nostalgia and create Planeswalker cards for characters who have never had them before. The creative team loved the idea. We settled in on five Planeswalker characters that played well with the deck themes design had already handed off. Three are characters you'll recognize from *Magic*'s past, one is a character you know but maybe not by name, and one is a brand-new character but from a plane you've seen before.


Legends of Antiquity
====================


**Ethan:** While creating the Planeswalker commanders was a strange evolutionary process, making the *Time Spiral*-esque legendary creatures was more straightforward. I met up with Ari Levitch from the creative team. He made a list of characters. I made a list of characters. Of course, if I was being ENTIRELY self-indulgent, all of the characters would be from Alpha through *Alliances*. But nostalgia means different things to different players, and I knew I would need to have characters representing different periods of *Magic*'s history.


There were a million black characters to choose from. Members of the creative department were really gung-ho to do Stitcher Geralf and Ghoulcaller Gisa, those feuding necromancer twins from *Innistrad*. The public had really latched onto those characters and was disappointed when *Avacyn Restored* rolled around and we still hadn't made legendary creature cards of them. Dan and James designed them to be opposites. One stitched multiple corpses together to make giant zombies, while the other would gladly chop a zombie in half to get two zombies!




![](https://media.wizards.com/2014/c14/aakdfnppleih2/en_940jsrk3wv.png)


![](https://media.wizards.com/2014/c14/aakdfnppleih2/en_dnk2pp40uf.png)





White was a bit tough, but there were a decent number of good green candidates. One of the red characters on Ari's list really jumped out at me: Feldon, he of [Feldon's Cane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feldon%27s+Cane).


"Feldon's red? How do you know that?"


"I read it on the internet," Ari replied.


"Hmmm..."


Now I am a serious geek culture scholar squirrel. At various points during my life, I've owned more than 100 Star Wars books, wrote [a bibliography of pulp science fiction author E. E. "Doc" Smith](http://www.ethanfleischer.com/lensman/smithbiblio.txt), and compiled an exhaustive timeline chronicling the history of the Ultramarines Space Marines chapter from *Warhammer 40,000*. While I never got bit by the *Magic* fiction bug to that extent, I knew how to hit the books.


My initial research indicated that there were three main sources of information on Feldon: *The Brothers War* novel and "Loran's Smile," a short story in the *Colors of Magic* anthology, both by Jeff Grubb, and the flavor text for [Feldon's Cane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feldon%27s+Cane). I was already well-acquainted with *Antiquities*-era flavor text, so I mosied over to the creative department, where there is a bookshelf with many *Magic: The Gathering* books on it.


*The Brothers War* is a sprawling epic that was written in conjunction with *Urza's Saga* block. It was a sort of retelling of the events from *Antiquities*. It mostly chronicles a decades-long war between the forces of Urza and Mishra, two artificer brothers. There is a third faction, a Third Path, of scientists delving into the powers of mana. Feldon is a glaciologist who can tap into the red mana of the mountains of Ronom. He has access to the fiery powers typical of red mages, but his part in the story was pretty small. Hmmm...I wasn't finding a hook to hang a card design off of yet.


Fortunately, I found what I was looking for in "Loran's Smile," [a story you should definitely read](http://magic.wizards.com/en/articles/archive/arcana/lorans-smile-2014-10-27) to "get" Feldon. It was a pretty touching story and inspired our first preview card of this article. Meet Feldon of the Third Path:



![](https://media.wizards.com/2014/c14/aakdfnppleih2/en_ykkavuw76a.png)
As you can see, this card represents Feldon as he tried to resurrect Loran through artifice, before he started learning colors of magic other than red. I think this card tells the story nicely, and leads to some amusing situations during playtests: "Feldon is so sad. The great love of his life, [Wurmcoil Engine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wurmcoil+Engine), is dead and he just can't let go. 'Why did you have to die, [Wurmcoil Engine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wurmcoil+Engine)?'"


From a design perspective, Feldon is clearly descended from [Kiki-Jiki, Mirror Breaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiki-Jiki%2C+Mirror+Breaker). Like his Goblin forbearer, Feldon is a combo king. While he's not as explosive as Kiki-Jiki, his combos are harder to disrupt. Finding a way to get the creature you want to copy into your graveyard can be solved in various ways, and the fact that his tokens are artifacts in addition to their other types may create interesting possibilities for deck builders.



I admit that I babied the heck out of this card. I clucked over it like a protective mother at every stage of the set's production. I handed copies of *The Colors of Magic* out to various members of the development and creative teams. While the card was changed several times during development, I gave my opinion about whether I thought that this change or that change helped or hindered the story we were trying to tell with it. Some questioned the wisdom of making fan service cards for readers of fifteen-year-old short stories, but I did not let doubt cloud my mind. I poured out my hopes and dreams for the card's illustration to Ari, who was in charge of concepting the card. Once the art description was written, I couldn't resist one last little detail: "I believe," I wrote in an email to Ari, "that [Feldon's Cane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feldon%27s+Cane) is supposed to be silver, not purple." When the finished art came in, I was blown away. All the details were captured there, and more! [Chase Stone](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Chase+Stone%22]) was now on my radar as an Artist to Watch Out For.


The Horizontal Lieutenant Cycle
===============================


**Ethan:** By this, the third *Commander* release, it was clear that we should continue the tradition of making a Commander-relevant mechanic for the set. I was really hung up on the idea of sidekicks for your commander. We started with creatures that started the game in the command zone along with your commander, but we quickly realized that unless the cards were extremely weak or narrow in application they would practically become mandatory inclusions in any deck that ran their color. We tried creatures that improved your commander, but those didn't work with our new Planeswalker commanders. Finally, we hit upon the idea of creatures that improved if your commander was on the battlefield. Great! Nice and simple. We designed some cards, and they weren't working very well. But it was too late! Time to hand the set off to development! Good luck, suckers! Hah hah hah hah hah! We ran away like thieves with our pants on fire.


![](https://media.wizards.com/2014/images/daily/cardart_goblindiplomats.jpg)
*Good luck, suckers!*
**Ian:** As I mentioned earlier, a huge portion of our development effort went toward the Planeswalkers. We knew that many Commander players had already experimented with "house rules" that allow Planeswalkers as commanders, and that those experiments didn't always go well. The trouble is that many existing Planeswalker designs don't lend themselves well to being commanders. However, we had confidence that if we designed Planeswalkers to be commanders from the ground up, we could make them play a lot better in Commander duels and multiplayer games.


Existing Planeswalker abilities have been balanced around one-on-one duels starting at 20 life. In multiplayer Commander, harming a single opponent is a lot less valuable when you may have three or more opponents at the table. Even in a Commander duel, the fact that your opponent starts at a higher life total changes what these Planeswalkers want to look like. We focused our Planeswalker abilities on doing things that are beneficial for you or help defend you (and them!) from multiple opponents. We also looked for abilities that are particularly powerful in the context of a Commander game, like increasing your mana production and card flow, and abilities that scale with multiple opponents.


Previous Planeswalkers have had relatively low loyalty compared to Commander life totals and creature sizes. We knew if we didn't address this, players would behave overly defensive in order to protect their vulnerable Planeswalker commanders. On the other hand, if we gave these Planeswalkers huge starting loyalty totals, every time a player recast one from the command zone, it would effectively increase the "collective life total" of the table, causing games to run very long. We determined through playtesting that moderate starting loyalties but more generous "plus" abilities struck the right balance. We also put in plenty of ways to defend your Planeswalkers, so you don't need to worry about them being constantly killed.


Lastly, we structured the starting loyalty and "minus" abilities to make it difficult to spend the last bit of loyalty then recast your Planeswalker from the command zone, resetting its loyalty and getting two uses in one turn. We found that play pattern frustrating to play against, and it was stopping us from making our Planeswalkers as exciting and powerful as they should be when used conventionally.


As Ethan mentioned, the other new mechanic in the set is the *lieutenant* ability word. Sometimes, highly competitive Commander players choose their commanders mostly for color identity, without the intent of building their decks around them. Lieutenant is meant as a reward for players who actually intend to cast their commanders and try to keep them on the battlefield.


A creature with lieutenant gets (or grants) a bonus as long as you control your commander. It let us create creatures with combat stats that are more generous than we would normally allow for a typical one-on-one duel, because their abilities will only be turned on in a context where players have a higher starting life totals. Moreover, unleashing your lieutenant's full power involves keeping your commander on the battlefield, which isn't always a given. We wanted to make sure we were giving you a creature that's worth that extra effort.


Earlier, I talked about how there are a lot of pressures against traditional creature combat in multiplayer games. My preview card for today, Angelic [Field Marshal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Field+Marshal), helps those of you who like to beat down get back in the red zone. Let's take a look:



![](https://media.wizards.com/2014/c14/aakdfnppleih2/en_hc52fg6r3y.png)
As a potential 5/5 flying, vigilance creature for 2WW, Angelic Field Marshal is...erm...as I said, more *generous* than we'd normally print. Her combination of evasion and granting vigilance to your army means you can dish out some damage without leaving yourself vulnerable. What's more, she's perfect at defending your Planeswalker commander, should you choose to use her.



Beyond our two new mechanics, development made sure to include a tremendous number of exciting individual cards. Specifically, we wanted to mix in some cards with lower mana costs. Often, when players (and even R&D) think of "commander cards," we think of giant creatures or high-cost spells with powerful, splashy effects. While the set has plenty of those, you'll also see some small creatures and utility spells that are particularly effective in multiplayer environments and still hold their value in longer games. We wanted to work against the notion that Commander is only about huge haymakers.


A Token Inclusion
=================


**Ethan:** Last, and in some ways least, I should mention the things in the box that AREN'T *Magic* cards. Aaron Forsythe was pretty unhappy that the previous *Commander* products had not included tokens. I believe that he has a secret agenda: to make printed tokens for every token-making *Magic* card, like, ever. I'm pretty sure that [Skeletal Vampire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Vampire) was in *Modern Masters* so we could print Bat tokens. For my part, I have binders full of tokens that I bring to my Commander games, so I sympathized with Aaron's dissatisfaction with the current state of affairs. Some of the decks in *Commander* (2014 Edition) have a lot of token-producers, and because many of them were reprints, some of them made tokens that were similar, but functionally distinct, from one another. Game states were more difficult to read than we would have liked. I pitched the idea of replacing the two oversized commanders that no one could see from the outside of the packaging with some token cards.


The question was raised, "What should the tokens have on the back?" In regular booster packs, tokens have ads or rules information on the back. In Duel Decks, tokens have a *Magic* card back. We didn't have to share the tokens in *Commander* (2014 Edition) with the brand team, and the production constraints that mandated *Magic* backs on the Duel Decks' tokens didn't apply here. We could do whatever we wanted! What's the best thing to put on the backs of tokens? MORE TOKENS!!! Need a Soldier? Here's one! Would you prefer a Spirit? Look on the other side! I might have to start a third token binder soon.


We'll be showing off some of the tokens this week (tomorrow!), and the rest next week after the full set is revealed.


Sincerely Yours...
==================


**Ethan:** So there you have it, the story of how we wrote a love letter to Vorthos. I hope you all have as much fun playing with these decks as we had making 'em!


**Ian:** Enjoy the rest of preview week, everyone. We hope you enjoy the cards and characters, old and new, and have as much fun playing with them as we did creating them.


[Daily MTG](/en/tags/daily-mtg)[Feature](/en/tags/feature)





 
 




  







