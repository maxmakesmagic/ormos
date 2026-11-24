---
id: 3p0045xf
kind: article
lang: en
path: /en/articles/magiconline/2014/09-16-r-d-feature-khan-we-make-it-better-a-magic-online-story
title: 'R&D Feature: “Khan We Make It Better?” A Magic Online Story'
published: '2014-09-16'
column_slug: magiconline
column: Magic Online
authors: []
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
    lang_detected: en
    capture_id: 115152
    url: http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
    captured_at: '2014-12-02 17:50:05+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
    lang_detected: en
    capture_id: 115152
    url: http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
    captured_at: '2014-12-02 17:50:05+00'
    rule: drupal.posted_in_date
sources:
- document_id: 3p0045xf
  url: http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
  page_key: magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
  lang: en
  template: drupal
  captured_at: '2014-12-02 17:50:05+00'
  capture_id: 115152
  wayback_url: https://web.archive.org/web/20141202175005id_/http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3p0045xf
  capture_id: 115152
  url: http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
  wayback_url: https://web.archive.org/web/20141202175005id_/http://magic.wizards.com/en/MTGO/articles/archive/rd-feature-khan-we-make-it-better-magic-online-story-2014-09-22
  captured_at: '2014-12-02 17:50:05+00'
  template: drupal
  sha256: 63ded69c681c87e504d666a9bfeabd7deedce2674886142fbb53bfde0f2d854d
render_recovery: []
---
![](https://i.ormos.uk/71/21/71215c6cdd93aba8a5367611064b29f51ee82c3325f603c0d72bd3ddb047cd7a.png)

[Download *****Magic Online*****](https://web.archive.org/web/20140916000000/http://magic.wizards.com/en/content/download) 

  

October  
 Sept. 24 - Oct. 29

 

MOCS Promo

[![](https://i.ormos.uk/1c/71/1c71ecc0ab205fa958eb929622f61ca4257f98bb28ecbab6353a689ea150ce4e.png)](/en/articles/uncategorised/2014/06-03-2014-mocs-full-rules#schedule)  
[Entomb](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Entomb) 

MOPR Event Promo

[![](https://i.ormos.uk/a2/e6/a2e6904a6eb9f885892fbd8df2a5ce8bce32b6e1d5b9d5591bbbde03b1a84b51.png)](https://web.archive.org/web/20140916000000/http://magic.wizards.com/en/game-info/products/magic-online/2014-magic-online-player-rewards)  
[Prophet of Kruphix](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophet+of+Kruphix) 

On the war-torn battlefields of Tarkir, the five clans each use morph magic to hide the strength of their forces from their enemies. This magic involves being surrounded by an imposing swirling ball of light and being face-down until just the right moment.

As the digital editor for *Magic Online*, one of my primary job responsibilities involves working with the rest of the digital design team on the implementation of mechanics, including getting the player experience to line up with what the rules of the game need to do. There are mechanics that create greater challenges than others, but morph wasn’t one of them.

Morph *could* have been very tricky just to get working properly, but fortunately most of the work implementing it properly was done about twelve years ago. The cards were hidden properly behind an image of the card back (more on this later), and they identified the order in which they entered the battlefield. While some recent cards and mechanics are complicated – looking at you, [Whims of the Fates](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates)! – the team had almost no concerns that the rules would be a problem.

Being able to set the rules aside freed up the design team to look at how we could make the *Khans of Tarkir* morph experience easier and more fun to play with. The real design challenge with morph, we felt, was improving the way we showed you the card. Under the old system, we showed you the back of the card and tried to put as much information in front of the card back as possible, with the goal of being helpful. Sometimes this led to us trying too hard to be helpful.

For example, if the face of the card was white, we’d show white pinlines so you could tell at a glance what color it would be. The problem is that this is misleading: a face-down creature isn’t actually white, so in the process of trying to be helpful the client was also being misleading. One of the first bullet points in our *Khans of Tarkir* set spec was to fix those pinlines, and so the morph cards you’ll see once you log in (or if you watched the *Magic Online* Community Cup coverage!) will have colorless frames.

Card Backs

![](http://media.wizards.com/images/magic/tcg/products/ktk/7uhasdf2usnhz/en_01_sldjkfhkdf.jpg)

We wanted to be sure to include a digital equivalent of one of the new tools that face-to-face *Magic* will be using: the morph overlay card. For those of you who haven’t seen one yet, it’s a reminder card with wicked cool art that shows off the basic rules of the mechanic. When you open a pack of physical *Khans of Tarkir* cards, you have a chance to get one of these overlay cards, just as you might get a token. When you play a morph creature face-down on *Magic Online*, you’ll always see it.

We also took the time to touch up a few other things about the way morph works. We updated the reminder text on the face-down cards from the paper experience. After all, the line of text “You can cover a face-down creature with this reminder card” isn’t quite as helpful for *Magic Online* players, but it’s super important to be able to know which face-down creature entered the battlefield first. One of the great advantages that *Magic Online* has is the ability to dynamically update the text on cards, so not only can we show you only relevant information, we can update even that text as you play. That’s why, in the interest of conserving space on a card, when blue text is added to a face-down creature, most of the reminder text vanishes now. All that remains is the line identifying when the creature entered the battlefield.

Card Faces

Before *Khans of Tarkir*, to look at a face-down creature’s face, you had to zoom in on it. Now, there are a few ways to zoom in—while pointing to the card with your cursor, you can hold Z, the middle mouse button, or the left and right mouse buttons at the same time—but it was still an extra step.

Now, thanks to the wizardry of UX designer James Sooy and technical artist Jesse Raymond, you just need to point to the card with your cursor. Forgotten which of your three face-down creatures is your [Ashcloud Phoenix](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix)? Just roll your cursor over all three to peek at them in order. Or just press F5 to peek at all your face-down cards at once.

While peeking, face-down cards have a circular fade effect overlaid onto them, so you won’t be able to confuse them with face-up cards. There’s also a helpful “Face-down” label at the bottom of the card, because we wanted to be sure that the information about the card face was as clear as it was accessible.

<table><tbody><tr><td></td>&#10;			<td><img src="http://www.wizards.com/mtg/images/digital/magiconline/9-22_img_1.png"></td>&#10;			<td><img src="http://www.wizards.com/mtg/images/digital/magiconline/9-22_img_2.png"></td>&#10;			<td></td>&#10;		</tr></tbody></table>

While we’re talking about [Ashcloud Phoenix](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix), it’s worth pointing out that when you know the identity of a face-down card, whether it’s an [Ashcloud Phoenix](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcloud+Phoenix), a [Vesuvan Shapeshifter](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuvan+Shapeshifter), or even a [Mischievous Quanar](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mischievous+Quanar), the face-down card will have the name of that card in blue instead of the word “Morph.” The card doesn’t really have that name, so [Echoing Truth](https://web.archive.org/web/20140916000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Echoing+Truth) won’t bounce both a face-down Phoenix and a face-up Phoenix, but having the reminder can be very helpful in a crowded board.

![](http://www.wizards.com/mtg/images/digital/magiconline/9-22_morphed_ashcloud_phoenix.png)

Starting on October 3, you’ll all have a chance to play with the new morph cards in the *Khans of Tarkir* Prerelease event. Let us know what you think on Twitter, Reddit, and the forums!

Allison Medwin  
 Digital Editor, *Magic Online*  
 @trulyaliem on Twitter