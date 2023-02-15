
---
[Link to Wayback Machine](https://web.archive.org/web/20140818123856/http://magic.wizards.com/en/articles/archive/technically-speaking-bringing-magic-2015-online-2014-08-11)

[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "255671"
[_metadata_:publish_date]:- "2014-08-11"
[_metadata_:source]:- "div-main"
[_metadata_:title]:- "Technically Speaking: Bringing Magic 2015 Online"
[_metadata_:wayback_capture_timestamp]:- "2014-08-18 12:38:56"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20140818123856id_/http://magic.wizards.com/en/articles/archive/technically-speaking-bringing-magic-2015-online-2014-08-11"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/technically-speaking-bringing-magic-2015-online-2014-08-11"
---





### FEATURED ARTICLE


Technically Speaking: Bringing Magic 2015 Online
================================================



![](https://web.archive.org/web/20140818123859im_/http://magic.wizards.com/sites/mtg/files/styles/auth_small/public/images/person/author-Pic.jpg?itok=pK-Qbman)

Jesse Raymond

Introduced to Magic by a family friend as a child in 1993, Seattle native Jesse Raymond excitedly joined Wizards of the Coast twenty years later as Magic Online's first Technical Artist. Jesse hasn't seen that family friend in years, but hopes Wilhelm stumbles across this one day so Jesse can say "thank you!"


August 11, 2014
 








![](https://web.archive.org/web/20141030155949im_/http://www.wizards.com/mtg/images/digital/magiconline/NEWSITE_MTGO_Logo_reduced.png)

[Download *****Magic Online*****](http://magic.wizards.com/en/content/download) 
  


Hello and welcome! I’m very excited to give you a behind-the-scenes look at how we brought the *Magic 2015* card update to *Magic Online*. We’ll look at what changed on the card faces and walk through how those changes went from the printed card to *Magic Online*. We’ll also talk about why we can’t just use the same process to make print and digital cards simultaneously, and what makes them different.


*Magic 2015* is an exciting milestone in *Magic* history because, for the first time since *Eighth Edition*, the frames and fonts on the faces of *Magic* cards have undergone a makeover. This facelift not only modernizes the look and feel of *Magic* with elements like the sleeker black card border, but also brings some improved functionality to the table, too. To begin with, we’ve switched to using Beleren, our new font designed specifically for *Magic*. We’ve also improved how the collector’s information is organized and displayed, making it easier for human or machine eye alike to sort cards. The most notable change is the addition of the foil stamp of authenticity on rare and mythic rare cards, which also adds some flare to make those cards feel more special than common, uncommon, and basic land cards. In addition to those major changes, the devil was in the details for *Magic 2015*, since every element on the card face had moved or changed, even if slightly. For comparison, here’s how *Magic Online* displays [Hoarding Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hoarding+Dragon) in the *Eighth Edition* and *Magic 2015* frame style:


![](https://web.archive.org/web/20140818123901im_/http://www.wizards.com/mtg/images/digital/magiconline/hoarding_dragon_comparison.png)
One of the biggest challenges we face with digital *Magic* is that our needs are wildly different from printed *Magic* when it’s time for production. Print and digital share the same designs and image assets but, beyond that, they are two very different creatures. While print has to worry about the limitations of ink and presses, digital has to work within the boundaries of code and dynamics. Keeping those differences in mind, we knew very early that we need to break the design files down into individual pieces and then rebuild those pieces into the *Magic Online* version of *Magic 2015*.


We needed a way to track all of those details and changes, and we needed a blueprint so we’d know how to rebuild the card face once the design was broken down into individual elements. So, we created design specs. These specs delved deeply into the design details, including measurements and unit conversions, typeface specifics, styling rules, and other various production notes. By documenting all of these details, the team had a roadmap to success that we could all follow.


![](https://web.archive.org/web/20140818123900im_/http://www.wizards.com/mtg/images/digital/magiconline/Example_Redlines.jpg)
As you’ve probably already guessed at some point in the past, we don’t recreate each card individually. We use frame templates, which are collections of code and image assets. Every element of a card, including the background, text, art, power/toughness, collector’s info, and stamp of authenticity, are layered upon each other piece-by-piece. By using templates, we can reproduce a dynamic version of any card in our database on demand.


To create the template, we separated all of the elements into three majors groups: background, regular size and large size. The template is separated into these three groups to support game play performance, which can be a concern when displaying numerous cards at once.


The background consists of the texture files for the background, title plaque, type plaque, power/toughness plaque, rules textbox and the stamp of authenticity, as well as a vector path for the pinlines that tie it all together. The background has access to textures and color swatches for every color in *Magic*, which means that we only need a single template to create a card of any color. By following hybrid and multicolor rules, the cards are also able to intelligently use gradients and/or gold when a card meets the correct conditions. Since it is more performance-friendly, once the card background is rendered, we flatten the entire background into a single image file and cache it, allowing us to use it numerous times with only a tiny hit to overall rendering speed with every instance on the screen.


The standard and zoom-view groups are partially redundant in that they both have instructions coded for how to style the same elements of the foreground, and both versions overlay onto the same instance of the background. For example, both standard and zoom views include the card name, mana cost, type, expansion symbol, rules text, and power/toughness, but they treat elements very differently. Standard view uses truncation and stricter legibility rules to support cards in the collection and on the battlefield, since these are the scenes that have the potential to display the cards at small scale. The zoom view can be seen in the Preview Pane and when zooming in on a card, and it maintains the “true view” of a card by scaling text instead of truncating it. The goal of the large-sized card is to provide a high-quality view of the card, while the goal of the standard card view is performance-driven game play. With these goals in mind, we chose to only show the collector’s information on the large card. It’s also why we have two foreground groups in our card templates. Here’s an example of the background by itself, the large card and the regular card (image scaled up for comparison sake), respectively:


![](https://web.archive.org/web/20140818123900im_/http://www.wizards.com/mtg/images/digital/magiconline/article_3_soul_spread_v3.png)
The templates are built to be as flexible as possible, and have the potential to be any color, creature or noncreature card, with or without the stamp of authenticity, and with or without any watermark. For example, by having a few switches flipped under-the-hood, a common red sorcery, a green promo creature, and hybrid land can all share the same template, despite the differences that make them distinct from one another.


![](https://web.archive.org/web/20140818123900im_/http://www.wizards.com/mtg/images/digital/magiconline/Example_CardsSharingTemplate.jpg)
Template flexibility also allows a card to change color on the battlefield, something that printed *Magic* simply can’t do. Let’s see this in action by using *Magic 2015*’s favorite color-changing spell, [Turn to Frog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turn+to+Frog):


![](https://web.archive.org/web/20140818123900im_/http://www.wizards.com/mtg/images/digital/magiconline/Example_ColorChange.jpg)
While templates are incredibly useful, there is one thing to consider. Templates are not one-size-fits-all. Even though we’ve done a great job of being able to create nearly every card in an expansion with a single template, cards like Planeswalkers and tokens are simply just not similar enough to fit into the same mold. For the *Magic 2015* release on *Magic Online*, we ended up creating seven new frame templates:



* Standard cards
* Planeswalkers with three abilities
* Planeswalkers with four abilities
* Tokens with rules text
* Tokens without rules textbox
* Full art promos
* Emblems


Many of you are probably as surprised as I was when I found out we had to double up on Planeswalkers and tokens. [Garruk, Apex Predator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Apex+Predator), the only four-ability Planeswalker in the set, is not that different from the rest of the *Magic 2015* Planeswalkers is he? When it comes down to factors like the size of the art window versus the size of the rules text area, Garruk becomes different enough that he and any future four-ability Planeswalkers needed their own template. The same is true about tokens, as the addition of the rules text box is enough to require a second template.


![](https://web.archive.org/web/20140818123900im_/http://www.wizards.com/mtg/images/digital/magiconline/article_planeswalkers.jpg)
As you can probably imagine, creating new frame templates is going to be a high priority for *Magic Online* as fresh content is released. Not only do we need to create templates for brand-new frame types, but we’ll also need to create *Magic 2015* versions of existing frame types as they get reprinted. For example, miracles require a unique template, so the next time we print a miracle card, we’ll have to create a new template for *Magic 2015*–frame miracles. By creating a second miracle template, we can keep all of the *Eighth Edition*–style miracles in your collection looking like they always have while being able to offer the swanky new miracle cards sporting the new *Magic 2015* frames at the same time.


Well, friends, I’m sorry to say, but that concludes our behind-the-scenes tour. I’m Jesse Raymond, *Magic Online*’s Technical Artist, and technically speaking, this has been a blast!



[MTGO](/en/tags/mtgo)





 
 


  







