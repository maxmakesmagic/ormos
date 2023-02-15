
---
[Link to Wayback Machine](https://web.archive.org/web/20150126050003/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05)

[_metadata_:author]:- "Adam Prosak"
[_metadata_:description]:- "Greetings Everyone! My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make Magic: The Gathering the best game it can be. However, one of the things I've missed during my time here is writing. I harassed Sam Stoddard enough, and he agreed to loan me his digital space for a week. Thanks Sam!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "203086"
[_metadata_:publish_date]:- "2013-12-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Devotion"
[_metadata_:wayback_capture_timestamp]:- "2015-01-26 05:00:03"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150126050003id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/developing-devotion-2013-12-05"
---


Developing Devotion
===================



 Posted in **Latest Developments**
 on December 5, 2013 






![](https://web.archive.org/web/20170709072651im_/http://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Adam Prosak










Greetings Everyone!

 My name is Adam Prosak, and I am a development intern here at Wizards of the Coast. I love working to help make **Magic: The Gathering** the best game it can be. However, one of the things I've missed during my time here is writing. I harassed [Sam Stoddard](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard) enough, and he agreed to loan me his digital space for a week. Thanks Sam! 

The Devotion Mechanic
 Devotion is a mechanic that scales endlessly. Nearly any X spell (such as [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball)) is a good example of a scaling spell. The amount of damage [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) deals is only limited by the amount of mana you are willing to spend. Scaling cards are interesting because they allow you to play different-powered effect depending on the state of the game. Like other scaling cards, cards with devotion are similarly unlimited. Instead of available mana, a card with devotion counts the mana symbols on your permanents. Devotion is different than most scaling mechanics because many of your cards can count multiple times toward your scaling mechanic. A creature that costs ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) counts for two devotion, so it is difficult to plan on a certain amount of devotion. This makes developing devotion cards very tricky, as we want cards to be fun in the most amount of situations possible. 



|  |  |
| --- | --- |
|  |  |

  
 




