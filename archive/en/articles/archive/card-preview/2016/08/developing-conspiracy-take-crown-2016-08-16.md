
---
[Link to Wayback Machine](https://web.archive.org/web/20160819173721/http://magic.wizards.com/en/articles/archive/card-preview/developing-conspiracy-take-crown-2016-08-16?tags=Daily%20MTG&lang=en)

[_metadata_:author]:- "Ben Hayes"
[_metadata_:description]:- "Ben dives into a few behind-the-scenes stories from the development of the new mechanics in Conspiracy: Take the Crown."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1052941"
[_metadata_:publish_date]:- "2016-08-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Conspiracy: Take the Crown"
[_metadata_:wayback_capture_timestamp]:- "2016-08-19 17:37:21"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160819173721id_/http://magic.wizards.com/en/articles/archive/card-preview/developing-conspiracy-take-crown-2016-08-16?tags=Daily%20MTG&lang=en"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/card-preview/developing-conspiracy-take-crown-2016-08-16?tags=Daily%20MTG&lang=en"
---


Developing Conspiracy: Take the Crown
=====================================



 Posted in **Card Preview**
 on August 16, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Bio_BenHayes.jpg)
By Ben Hayes




 Ben Hayes has been designing games for over a decade and has been part of the Magic R&D development team since 2013. He led the FFL Team for Khans of Tarkir and the development team for Magic Duels: Origins. 






Before we get started, allow me to introduce the development team.


![](https://media.wizards.com/2016/images/daily/MM20160815_Hayes.png)


**Ben Hayes (lead)**


I was the lead of this team, as well as the lead developer of *Commander (2015 Edition)* and *Magic Duels* before this, and *Commander (2016 Edition)* and *Aether Revolt* afterward*.* I'm a senior game designer in *Magic* R&D and I've been in the department for about three and a half years.


![](https://media.wizards.com/2016/images/daily/MM20160815_Hawley.png)


**Bryan Hawley**   
  

Bryan is a game designer in *Magic* R&D. He was also on the initial design team for this set, so one of his jobs on this team was to make sure we maintained the vision of that team as we iterated on the set. Bryan also works a lot on *Magic Duels* and the Future Future League.


![](https://media.wizards.com/2016/images/daily/MM20160815_Skolnik.png)


**Yoni Skolnik**


Yoni is a game designer in *Magic* R&D. He and I have actually been friends since we were small children, so I was thrilled when he decided to try his hand at our game design test a couple of years ago, and I was even more excited when we decided to hire him. Besides this team, Yoni was also on the development team of *Battle for Zendikar*.


![](https://media.wizards.com/2016/images/daily/MM20160815_Sooy.png)


**James Sooy**


James is a UX designer and an avid *Magic* player. While James mostly works on digital projects for us, he was also on the *Commander 2015* team with me. He was responsible for the development of the white-black *Commander* deck.


![](https://media.wizards.com/2016/images/daily/MM20160815_Verhey.png)


**Gavin Verhey**


Gavin is a game designer in *Magic* R&D. Each development team tries to have at least one person whose main job in the department is early design, and for this set that was Gavin. In this role, Gavin was responsible for making more new cards than other member of the team, and generally making sure we were being consistent with design philosophies and color pie.




---

Conspiracies with a Twist
=========================


Conspiracies were obviously a centerpiece of the original *Magic: The Gathering—Conspiracy* set, and they were received very positively, so we knew early on that we wanted to bring the card type back here. Even though the originals were solid, we wanted to bring a new twist to the table—and we also had some design challenges we discovered after their release that we wanted to try to solve with this second batch.


Primarily the thing we weren't as happy with was how it ended up being the correct choice to first-pick your conspiracy a very high percentage of the time. While this meant that everyone got to play with conspiracies, it also took the drafting element away from those cards and you just saw way fewer of them each draft. We tried to include more synergy-driven conspiracies this time around to mitigate that, but design also handed off a great solution that offered the novelty we were looking for and also did a good job of addressing our "first-pick" issue.


![](https://media.wizards.com/2016/azetllnwjpxztp2b_CN2/en_hm24SAy5Yc.png)


Color!


What mechanic makes it so that you can get a third-pick Serra Angel in Draft? Color! I loved this innovation right off the bat for how it took a concept people are already deeply familiar with in draft and used it to solve our game design challenges. One way, albeit an unsatisfying one, to address our issue would have been to just make all the conspiracies weaker. Instead, this solution let us keep the power level people expected while still getting the conspiracies to float around the table because they were a bigger upfront commitment in pack one, and in the later packs you might not be in that color at all.


We discussed a bunch of different executions, including things like only letting you name a creature of the specific color and writing things like "if you control an Island." However, in the end we felt that this was the most flexible and satisfying execution of the idea, and I'm absolutely thrilled with how they ended up.


Monarchy!
=========


As an avid board game player, I found the monarch mechanic tremendously exciting. I loved the idea of adding this king-of-the-hill element to *Magic*, and it was clear from early playtesting that it had a ton of potential.


As the lead developer of the set, I also love how well the mechanic helped me address some of the fundamental game design challenges associated with multiplayer, the biggest of which is getting people to attack each other. In a multiplayer game, attacking puts you and the player you're attacking at a disadvantage—which translates to an advantage for the rest of the table—so without any external pressure, the dominant strategy in multiplayer is to turtle up.


The monarch allowed us to introduce a target into the game, one that gave players a benefit for attacking and offset the natural disadvantage. It also helped mitigate the problem of the table teaming up on a single person, because the target is continually being passed around.


Another big challenge of multiplayer *Magic* is card flow. *Magic* cards and rules generally function optimally in a one-on-one duel. Drawing a single card when you have three opponents is just going to be a lot less impactful than if you had one opponent. Because we don't want to compensate for this by making a bunch of cards that are three times as powerful, there's pressure to introduce more card flow into the games so that players can feel like they're having as much impact on their four-player game as they would in their heads-up match.


![](https://media.wizards.com/2016/azetllnwjpxztp2b_CN2/en_PZJsbl44r8.png)


Because card draw is generically useful to everyone and we want different decks in an environment to feel unique, we added a couple of cards like Throne Warden to make certain colors care more about being the monarch than others. This mismatch of incentive creates interesting and dynamic gameplay from one draft to the next.


Early in the process, the monarch caused the player with the title to create a 2/2 creature token each turn they managed to stay on the throne. While the monarch itself was fun, this benefit caused lots of snowball games, because your opponents had to outpace both your plays and the free 2/2 you were getting every turn, just trying to find a viable attack that would let them take the crown away from you, and then their "shield" would be down and you could often just take it right back and be in a better position than before. When we switched to drawing a card each turn, everything just seemed to fall into place, and we never looked back.


We also explored whether the monarch benefit should trigger at the end of your turn or the beginning, essentially deciding if you should need to hold onto it for a full turn cycle. I really like getting the cookie immediately after you take it, and going with the end of turn also encouraged players to swoop in and try to grab it on their turn even if they didn't think they would be able to hold onto it.


Grand Melee
===========


Melee is the last new mechanic I'll cover today. As I mentioned before, two design challenges of multiplayer are getting people to attack and avoiding one person getting ganged up on. Melee helps toward both of those goals nicely by making your creatures more effective at attacking than blocking, and by directly encouraging you to spread damage around. "Spread" was even one of the playtest names we used for the mechanic!


![](https://media.wizards.com/2016/azetllnwjpxztp2b_CN2/en_T9DxnmFdEl.png)


Wings of the Guard is a good example of the creature that's better at attacking than blocking. A 1/1 flying creature does not make a particularly good blocker. On the other end of things, it's relatively easy to get this up to a 3/3 or 4/4 attacking flier for two mana, which is far stronger than you'd normally expect to get. All you need to do is attack!


![](https://media.wizards.com/2016/azetllnwjpxztp2b_CN2/en_Ekkwswiemv.png)


Personally, I love the appeal that melee has for both Spike and Timmy/Tammy, which can be a hard overlap to find. For Spike, the mechanic gives you tons of possible combinations of attacks that all result in different amount of damage and levels of commitment, and the challenge of finding that perfect combination hits Spike very well. Meanwhile, the result of attacking multiple opponents with melee creatures is that you're constantly getting to have exciting turns of huge damage swings, especially when Adriana's around.


That's all I've got from the development side of things. I hope you all enjoy playing the set as much as I enjoyed working on it. Thanks for reading!


Ben ([@benbhayes](http://www.twitter.com/benbhayes))







