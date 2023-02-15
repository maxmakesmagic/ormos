
---
[Link to Wayback Machine](https://web.archive.org/web/20220704224900/https://magic.wizards.com/en/articles/archive/top-decks/duels-planeswalkers-2013-official-terms-2012-06-19)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "function Dotpot() { var prefix = `dotpot`; var currentRegion = `zz`; var currentLanguage = `en-us`; var regionElement = function () { var id = prefix + `-` + currentRegion; return document.getElementById(id); }; var languageElement = function () { var id = prefix + `-` + currentRegion + `-` + currentLanguage; return document.getElementById(id); }; this.showregion = function"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "603876"
[_metadata_:publish_date]:- "2012-06-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duels of the Planeswalkers 2013 Official Terms"
[_metadata_:wayback_capture_timestamp]:- "2022-07-04 22:49:00"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220704224900id_/https://magic.wizards.com/en/articles/archive/top-decks/duels-planeswalkers-2013-official-terms-2012-06-19"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/top-decks/duels-planeswalkers-2013-official-terms-2012-06-19"
---


Duels of the Planeswalkers 2013 Official Terms
==============================================



 Posted in **Top Decks**
 on June 19, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_author.jpg)
By Wizards of the Coast











function Dotpot() { var prefix = "dotpot"; var currentRegion = "zz"; var currentLanguage = "en-us"; var regionElement = function () { var id = prefix + "-" + currentRegion; return document.getElementById(id); }; var languageElement = function () { var id = prefix + "-" + currentRegion + "-" + currentLanguage; return document.getElementById(id); }; this.showregion = function (region) { if (currentRegion != region) { if (currentRegion != "zz") { languageElement().style.display = "none"; regionElement().style.display = "none"; } currentRegion = region; currentLanguage = "en-us"; regionElement().style.display = "block"; languageElement().style.display = "block"; } }; this.showlanguage = function (language) { languageElement().style.display = "none"; currentLanguage = language; var obj = languageElement(); obj.style.display = "block"; }; }; var dotpot = new Dotpot(); //







