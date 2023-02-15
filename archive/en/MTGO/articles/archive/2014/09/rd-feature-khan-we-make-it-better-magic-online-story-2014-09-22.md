
---
[Link to Wayback Machine](https://web.archive.org/web/20140930004605/http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22)

[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "266921"
[_metadata_:path_date]:- "2014-09-22"
[_metadata_:publish_date]:- "2014-09-16"
[_metadata_:source]:- "div-main"
[_metadata_:title]:- "R&D Feature: “Khan We Make It Better?” A Magic Online Story"
[_metadata_:wayback_capture_timestamp]:- "2014-09-30 00:46:05"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20140930004605id_/http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22"
---





### FEATURED ARTICLE


R&D Feature: “Khan We Make It Better?” A Magic Online Story
===========================================================



![](https://web.archive.org/web/20170709072651im_/http://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)

Allison Medwin




September 16, 2014
 











![](https://web.archive.org/web/20141030155949im_/http://www.wizards.com/mtg/images/digital/magiconline/NEWSITE_MTGO_Logo_reduced.png)

[Download *****Magic Online*****](http://magic.wizards.com/en/content/download) 
  


On the war-torn battlefields of Tarkir, the five clans each use morph magic to hide the strength of their forces from their enemies. This magic involves being surrounded by an imposing swirling ball of light and being face-down until just the right moment.


As the digital editor for *Magic Online*, one of my primary job responsibilities involves working with the rest of the digital design team on the implementation of mechanics, including getting the player experience to line up with what the rules of the game need to do. There are mechanics that create greater challenges than others, but morph wasn’t one of them.


Morph *could* have been very tricky just to get working properly, but fortunately most of the work implementing it properly was done about twelve years ago. The cards were hidden properly behind an image of the card back (more on this later), and they identified the order in which they entered the battlefield. While some recent cards and mechanics are complicated – looking at you, [Whims of the Fates](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates)! – the team had almost no concerns that the rules would be a problem.


Being able to set the rules aside freed up the design team to look at how we could make the *Khans of Tarkir* morph experience easier and more fun to play with. The real design challenge with morph, we felt, was improving the way we showed you the card. Under the old system, we showed you the back of the card and tried to put as much information in front of the card back as possible, with the goal of being helpful. Sometimes this led to us trying too hard to be helpful.


For example, if the face of the card was white, we’d show white pinlines so you could tell at a glance what color it would be. The problem is that this is misleading: a face-down creature isn’t actually white, so in the process of trying to be helpful the client was also being misleading. One of the first bullet points in our *Khans of Tarkir* set spec was to fix those pinlines, and so the morph cards you’ll see once you log in (or if you watched the *Magic Online* Community Cup coverage!) will have colorless frames.




Card Backs

![](https://media.wizards.com/images/magic/tcg/products/ktk/7uhasdf2usnhz/en_01_sldjkfhkdf.jpg)
We wanted to be sure to include a digital equivalent of one of the new tools that face-to-face *Magic* will be using: the morph overlay card. For those of you who haven’t seen one yet, it’s a reminder card with wicked cool art that shows off the basic rules of the mechanic. When you open a pack of physical *Khans of Tarkir* cards, you have a chance to get one of these overlay cards, just as you might get a token. When you play a morph creature face-down on *Magic Online*, you’ll always see it.


We also took the time to touch up a few other things about the way morph works. We updated the reminder text on the face-down cards from the paper experience. After all, the line of text “You can cover a face-down creature with this reminder card” isn’t quite as helpful for *Magic Online* players, but it’s super important to be able to know which face-down creature entered the battlefield first. One of the great advantages that *Magic Online* has is the ability to dynamically update the text on cards, so not only can we show you only relevant information, we can update even that text as you play. That’s why, in the interest of conserving space on a card, when blue text is added to a face-down creature, most of the reminder text vanishes now. All that remains is the line identifying when the creature entered the battlefield.




Card Faces

Before *Khans of Tarkir*, to look at a face-down creature’s face, you had to zoom in on it. Now, there are a few ways to zoom in—while pointing to the card with your cursor, you can hold Z, the middle mouse button, or the left and right mouse buttons at the same time—but it was still an extra step.


Now, thanks to the wizardry of UX designer James Sooy and technical artist Jesse Raymond, you just need to point to the card with your cursor. Forgotten which of your three face-down creatures is your [Ashcloud Phoenix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix)? Just roll your cursor over all three to peek at them in order. Or just press F5 to peek at all your face-down cards at once.


While peeking, face-down cards have a circular fade effect overlaid onto them, so you won’t be able to confuse them with face-up cards. There’s also a helpful “Face-down” label at the bottom of the card, because we wanted to be sure that the information about the card face was as clear as it was accessible.





|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |


While we’re talking about [Ashcloud Phoenix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix), it’s worth pointing out that when you know the identity of a face-down card, whether it’s an [Ashcloud Phoenix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix), a [Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuvan+Shapeshifter), or even a [Mischievous Quanar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mischievous+Quanar), the face-down card will have the name of that card in blue instead of the word “Morph.” The card doesn’t really have that name, so [Echoing Truth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Echoing+Truth) won’t bounce both a face-down Phoenix and a face-up Phoenix, but having the reminder can be very helpful in a crowded board.


![](http://www.wizards.com/mtg/images/digital/magiconline/9-22_morphed_ashcloud_phoenix.png)
Starting on October 3, you’ll all have a chance to play with the new morph cards in the *Khans of Tarkir* Prerelease event. Let us know what you think on Twitter, Reddit, and the forums!


Allison Medwin  




[MTGO](/en/tags/mtgo)





 
 




  







