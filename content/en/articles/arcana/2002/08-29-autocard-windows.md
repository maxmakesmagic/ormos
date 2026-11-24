---
id: 0pbkfhat
kind: article
lang: en
path: /en/articles/arcana/2002/08-29-autocard-windows
title: AutoCard windows
published: '2002-08-29'
column_slug: arcana
column: Arcana
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    lang_detected: en
    capture_id: 152534
    url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    captured_at: '2022-07-04 00:27:38+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    lang_detected: en
    capture_id: 152534
    url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    captured_at: '2022-07-04 00:27:38+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    lang_detected: en
    capture_id: 152534
    url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    captured_at: '2022-07-04 00:27:38+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    lang_detected: en
    capture_id: 152534
    url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
    captured_at: '2022-07-04 00:27:38+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: 0pbkfhat
  url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
  page_key: magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
  lang: en
  template: drupal
  captured_at: '2022-07-04 00:27:38+00'
  capture_id: 152534
  wayback_url: https://web.archive.org/web/20220704002738id_/https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
- document_id: 0pbkfhat
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/arcana/172
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/arcana/172
  lang: en
  template: aspx
  captured_at: '2012-10-23 01:30:23+00'
  capture_id: 751631
  wayback_url: https://web.archive.org/web/20121023013023id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/arcana/172
- document_id: 0pbkfhat
  url: http://www.wizards.com/default.asp?x=mtgcom/arcana/172
  page_key: wizards.com/default.asp?x=mtgcom/arcana/172
  lang: en
  template: classic_asp
  captured_at: '2008-05-03 18:56:00+00'
  capture_id: 1862287
  wayback_url: https://web.archive.org/web/20080503185600id_/http://www.wizards.com/default.asp?x=mtgcom/arcana/172
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0pbkfhat
  capture_id: 152534
  url: https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
  wayback_url: https://web.archive.org/web/20220704002738id_/https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29
  captured_at: '2022-07-04 00:27:38+00'
  template: drupal
  sha256: 1dafba250caa1cac47bcecc31aa1538c31d7110117d7d4869701d758e2ff85ef
render_recovery: []
---
Have you ever wondered how we make nifty popup card window links like this? [Sliver Queen](https://web.archive.org/web/20020829000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sliver+Queen)

Want to use them on *your* website?

### The new **Magic®** Card Image Database pop-up window

If you are wondering about the changes to the card image pop-up window (aka AutoCard) that have recently been implemented on the Wizards of the Coast website, let me be the first to explain the method behind our madness.

One of the greatest strengths of **Magic** is the visual beauty of the cards themselves, but up until now, it has been a legal nightmare to allow external sites to display visual images of our cards. As early as 1999 we flat out refused to put cards on our OWN website for fear that we would send the wrong message that these card images were "free" to use.

As can be seen in the WWW GUIDELINES in our our **[Legal Corner](https://web.archive.org/web/20020829000000/http://archive.wizards.com/default.asp?x=contactinfo/legal)** statement on our website, scanning in our cards, and/or using card art imagery to enhance your own site has been prohibited and is considered infringement on Wizards of the Coast copyrights.

So the question of how to allow people to use our card images to enhance their websites without infringement has been a topic that has led to some enhancements to our site that will hopefully solve this dilemma.

We have been in the process of posting all of our cards to our web servers to allow for the use of the **Magic** Card Image Database pop-up window. This enables us to host our own image files and provide an officially sponsored way to use our images. In our previous incarnation of this feature, the pop-up window was not clearly a Wizards of the Coast function as it only showed the card. This new pop-up is our official window (containing our Legal Text).

If you would like to include this fun functionality on your own websites, we request that you use this official method to prevent infringement issues and help us keep track of our bandwidth.

Here is how you can use this feature on your own website:

**Put this in the top of your HTML page:**

				script language="Javascript"  
 function WizardsAutoCard (cardname) {   

				  windowName = "WotCWindow";  

				  params = "toolbar=0, location=0, directories=0, status=0,  

				 
				  menubar=0, scrollbars=0, resizable=0, width=450, height=400";  

				  win = window.open  
("http://www.wizards.com/magic/autocard.asp?name="+cardname,   

				 
				  windowName, params);  
 }  
/script

**And then you can make a card link like this:**

				a href="javascript:WizardsAutoCard('Call of the Herd');"  
Call of the Herd  
/a

Just replace "Call of the Herd" in both places with a correctly-spelled card name to add your own AutoCard link.

Keep in mind that moving these images anywhere off of our servers is still a violation however, by having us host the images and using our function to access them, you are in the clear.

We are working towards solutions that will allow for the usage of card images in other ways besides a pop-up and we will post those methods as soon as they become available.

Sincerely,

Daniel Stahl  
 Managing Web Producer  
 Wizards of the Coast