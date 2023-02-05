
---
[Link to Wayback Machine](https://web.archive.org/web/20140911031817/http://magic.wizards.com/en/articles/archive/feature/developing-khans-2014-09-08)

[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/developing-khans-2014-09-08"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20140911031817id_/http://magic.wizards.com/en/articles/archive/feature/developing-khans-2014-09-08"
[_metadata_:wayback_capture_timestamp]:- "2014-09-11 03:18:17+00:00"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:description]:- "Developing the common land cycle and something for the control mirror in Khans of Tarkir."
---





### FEATURE


Developing Khans
================



![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_eriklauer.jpg)

Erik Lauer

Erik Lauer is a senior game designer who works on final game design and development. Recently, he has led the Return to Ravnica, Modern Masters, and Theros development teams. 


September 8, 2014
 










I'm Erik Lauer, the head developer of *Magic*. I was the lead developer on *Khans of Tarkir*. The most recent sets I led are *Theros*, *Return to Ravnica*, *Modern Masters*, and *Innistrad*.


First, let's meet the development team for *Khans of Tarkir*.


![](https://media.wizards.com/images/magic/daily/features/2014/askl67dfue_beyer.jpg)
Doug Beyer was the creative team member assigned to *Khans of Tarkir*. In addition to making sure the set plays well, he was responsible for making sure the alignment of the card file and the creative vision improves as the set was developed.





![](https://media.wizards.com/images/magic/daily/features/2014/askl67dfue_humpherys.jpg)
Dave Humpherys is the senior development manager and was the lead developer of*Journey into Nyx*, *Gatecrash*, and *Avacyn Restored*.





![](https://media.wizards.com/images/magic/daily/features/2014/askl67dfue_lapille.jpg)
Tom LaPille is an experienced developer, having led development of *Born of the Gods*, *Dark Ascension*, and *Magic 2012*.





![](https://media.wizards.com/images/magic/daily/features/2014/askl67dfue_prozak.jpg)
Adam Prosak is a developer who writes Daily Decks and was on the *Vintage Masters* development team.





![](https://media.wizards.com/images/magic/daily/features/2014/askl67dfue_main.jpg)
Shawn Main was the design team member assigned to *Khans of Tarkir*. In addition to the play of the set, he was in the meetings explaining why design made certain choices. That way, development can balance the design goals for the card with the development goals at hand.





Design, "Devign," Development
=============================


Design works on a set. Then there is a "devign" period—where design continues to work on the set, but with frequent feedback from development. Finally, design hands the set off to development.


One of the big topics for devign was making the three-color structure work. Mark Rosewater and I discussed how much of the play of the set should be three-color. For a draft, I thought the ideal would be if five or six people drafted three-color decks (one per wedge), one or two people drafted two-color decks, and sometimes someone drafted more than three colors. There was no expectation that this exact distribution would occur frequently. Rather, it would be more of a target of what a draft would look like on average if the set themes were working. Mark agreed that was a healthy mix.


![](https://media.wizards.com/images/magic/daily/features/2014/cardart_jfkaeesdf.jpg)
Art by [Eytan Zana](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Eytan+Zana%22])


When a set enters devign, the set themes are normally very strong. The design team wants to find the correct themes, and having a lot of games where they aren't makes design's tests less productive. This set fell along those lines, with people picking a wedge and doing little else. So we tried making the synergy and three-color cards somewhat less powerful.


After the first batch of changes, the wedge themes were clearly too weak; the proportion of people playing three-color wedges was far below 5/8ths. For instance, Tom LaPille was doing well playing three-color arcs, but his favorite seemed to be Esper.


Again, this is normal. When an aspect of the set is too strong, and it isn't clear what the right strength is, we normally go quite far in the opposite direction the first time we change it. We often end up with the aspect being too weak the next time, but that gives us a range of how strong to make that theme. Our next try, we try something about halfway between. And if that isn't correct, at least we have cut our range in half. Repeatedly cutting the range in half is an efficient method to finding a good spot.


In addition to the three-color cards, we needed to find the correct mana fixing. We were looking for a good cycle of common, three-color lands. Design had tried to find the right lands a few times, and Mark decided I should work on the lands while he worked on other cards. We were looking for lands that were good enough to make three-color decks work, but not so strong that people frequently played five-color decks.


Abundantly Colorful
===================


At first, the mana was abundant. While designers tended to play three colors in the set themes, developers tended to play four or five colors, scooping up lots of powerful cards. To address that issue, weaker lands were put in, and (sure enough) people retreated to two-color decks or played three colors with very inconsistent mana. In fact, people weren't playing the weaker lands at all. Again, this was a process of designing lands about "half the distance" from the first to the second, in a sense. My hope was to once again reach the sweet spot where all the goals were met. But, something different happened.


We had a playtest where the designers thought the lands were too weak to play. The developers thought it was better to play these than to play a three-color deck without them. But, on top of that, the developers played lots of the "weak" lands in their five-color decks. By the end of the playtest, designers generally agreed they should have played the lands that had all three colors of their wedges.


![](https://media.wizards.com/images/magic/daily/features/2014/cardart_87ejbsdf.jpg)
Art by [Eytan Zana](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Eytan+Zana%22])


This is part of the reason why devign is so important. Designers and developers often have different perspectives on what is happening in the set, and getting every perspective means we get a more well-rounded sense of how the set can play.


I needed to know which was right: to play three colors, or to play all five. So I took two pools, built the first as a five-color deck, and the second as a three-color deck. After watching developers play both, it was clear the five-color deck was stronger. Then I took the same pools, built the first as a three-color deck and the second as a five-color deck. Again, the five-color deck was stronger, despite coming from what was previously the losing pool.


I was still looking for the correct three-color lands that would look good enough that everyone would play them, but not so good that the correct strategy was to play lots of them and build a five-color deck. Apparently, I wasn't even close. The problem seemed to be that it was right to play unappealing three-color lands, even if only two of the colors were in your wedge. The extra color of mana outside your wedge just made it more appealing to splash a fourth color.


I decided we should try two-color lands instead. I was looking for a two-color land that would give you more time to draw your third color. I asked Mark about the [Refuges from *Zendikar*](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+[%22Zendikar%22]&name=+[Refuge]); what if we put enemy-colored refuges at common? He reiterated that I should figure out the lands; he was working on big-picture issues. So we tried those.


Sure enough, designers and developers alike would put their "on color" Refuges in their decks. The designers generally picked their best wedge, and their decks worked reasonably well. The developers sometimes played more than three colors, sometimes fewer, but usually played a three-color wedge. At the end of devign, our common lands were the five enemy-colored Refuges.


Over the course of development, people's opinions changed. As more drafts were held, people found the mana situation was very tight. Players drafted the mana fixing very high, because of the number of games where the first person to draw all three colors would win. Shawn Main was finding the set less fun to draft and was adamant something should change. I really liked the Refuges and decided we should try making room for more. We tried it and liked the results. So our common land cycle has all ten of the Refuges!


We weren't actually able to keep them as Refuges and simply reprint the ones from *Zendikar*. Those had *Zendikar*-specific names, but the new ones are (for all intents and purposes) the same cards, all of which you can see here!




![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_jxwoo59fvy.png)


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_kx5tq2x0qf.png)




![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_pusvo75pef.png)


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_37z6pxjevm.png)




![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_jdlkss1bzm.png)


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_lctyntabx5.png)




![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_nxdkswl3ur.png)


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_lhzynt0cou.png)




![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_fg237t67ee.png)


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_agscypux1s.png)





He Knows Prowess
================


Later in development, Khans was being testing in our FFL. Much like real-world Standard, the metagame can change from aggressive decks to control decks. At this point, control decks were doing well. But when one control deck played another, the matches took way too long. Control decks didn't have any threats that were sufficiently strong against other control decks. Since control decks were doing so well at this point, it didn't seem correct to create a threat that was strong against a wide variety of decks. Instead, we wanted something that was specifically good for control decks against control decks.


After talking to some designers and developers, I put this card in the set:


Enlightened Djinn  



At the time, prowess was called "kung fu."


Ken Nagle created the "return three lands you control to their owner's hand" cost. He liked the idea that you can protect your creature if you really need to, but it sets you back a lot.


We tested this Djinn and it was fun. However, the mechanic of casting a spell to make your 6/7 creature slightly stronger seemed out of place to some people. We removed it, and resumed testing. About a week later, we had games between control decks where each player had an Enlightened Djinn on the battlefield, but nothing was happening; the 6/7 bodies created a stalemate. We tried the same games with the Djinns once again having prowess. Soon enough, there were two Djinns on the table, and a flurry of spells ensued. While seemingly out of place, prowess was a lot of fun on a 6/7!


![](https://media.wizards.com/images/magic/daily/features/2014/cardart_jfkajbsdf.jpg)
Art by [Richard Wright](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Richard+Wright%22])


A lot of development comes down to trying different versions of cards and picking the ones that create the most fun environment. Sometimes, the original is right.


So here is our final card: Pearl Lake Ancient. I hope you enjoy it!


![](https://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_x4p59deuyk.png)

[Daily MTG](/en/tags/daily-mtg)[Feature](/en/tags/feature)





 
 




  







