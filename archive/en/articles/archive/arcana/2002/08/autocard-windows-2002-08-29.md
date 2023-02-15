
---
[Link to Wayback Machine](https://web.archive.org/web/20210507020121/https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Have you ever wondered how we make nifty popup card window links like this? Sliver QueenWant to use them on your website?The new Magic® Card Image Database pop-up windowIf you are wondering about the changes to the card image pop-up window (aka AutoCard) that have recently been implemented on the Wizards of the Coast website, let me be the first to explain the method behind"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "604336"
[_metadata_:publish_date]:- "2002-08-29"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "AutoCard windows"
[_metadata_:wayback_capture_timestamp]:- "2021-05-07 02:01:21"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210507020121id_/https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/arcana/autocard-windows-2002-08-29"
---


AutoCard windows
================



 Posted in **Arcana**
 on August 29, 2002 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_author.jpg)
By Wizards of the Coast











Have you ever wondered how we make nifty popup card window links like this? [Sliver Queen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sliver+Queen)

Want to use them on *your* website?

### The new **Magic®** Card Image Database pop-up window

If you are wondering about the changes to the card image pop-up window (aka AutoCard) that have recently been implemented on the Wizards of the Coast website, let me be the first to explain the method behind our madness.

One of the greatest strengths of **Magic** is the visual beauty of the cards themselves, but up until now, it has been a legal nightmare to allow external sites to display visual images of our cards. As early as 1999 we flat out refused to put cards on our OWN website for fear that we would send the wrong message that these card images were "free" to use.

As can be seen in the WWW GUIDELINES in our our **[Legal Corner](http://archive.wizards.com/default.asp?x=contactinfo/legal)** statement on our website, scanning in our cards, and/or using card art imagery to enhance your own site has been prohibited and is considered infringement on Wizards of the Coast copyrights.

So the question of how to allow people to use our card images to enhance their websites without infringement has been a topic that has led to some enhancements to our site that will hopefully solve this dilemma.

We have been in the process of posting all of our cards to our web servers to allow for the use of the **Magic** Card Image Database pop-up window. This enables us to host our own image files and provide an officially sponsored way to use our images. In our previous incarnation of this feature, the pop-up window was not clearly a Wizards of the Coast function as it only showed the card. This new pop-up is our official window (containing our Legal Text).

If you would like to include this fun functionality on your own websites, we request that you use this official method to prevent infringement issues and help us keep track of our bandwidth.

Here is how you can use this feature on your own website:

**Put this in the top of your HTML page:**


```

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
```
**And then you can make a card link like this:**


```

				a href="javascript:WizardsAutoCard('Call of the Herd');"  
Call of the Herd  
/a
```
Just replace "Call of the Herd" in both places with a correctly-spelled card name to add your own AutoCard link.

Keep in mind that moving these images anywhere off of our servers is still a violation however, by having us host the images and using our function to access them, you are in the clear.

We are working towards solutions that will allow for the usage of card images in other ways besides a pop-up and we will post those methods as soon as they become available.

Sincerely,

Daniel Stahl  
 Managing Web Producer  
 Wizards of the Coast







