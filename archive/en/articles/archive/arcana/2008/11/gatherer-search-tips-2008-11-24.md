
---
[Link to Wayback Machine](https://web.archive.org/web/20170726082454/http://magic.wizards.com/en/articles/archive/arcana/gatherer-search-tips-2008-11-24)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Thanks to Magic web developer Eric Berglund, we have some ways that you can build searches on the new Beta Gathere directly from your browser. Take it away, Eric!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "653461"
[_metadata_:publish_date]:- "2008-11-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Gatherer Search Tips"
[_metadata_:wayback_capture_timestamp]:- "2017-07-26 08:24:54"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170726082454id_/http://magic.wizards.com/en/articles/archive/arcana/gatherer-search-tips-2008-11-24"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/arcana/gatherer-search-tips-2008-11-24"
---


Gatherer Search Tips
====================



 Posted in **Arcana**
 on November 24, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











Thanks to **Magic** web developer Eric Berglund, we have some ways that you can build searches on the new Beta Gathere directly from your browser. Take it away, Eric!


Modern web browsers these days have built-in ways for you to search different search engines. For example, Firefox and Internet Explorer 7 both have separate search boxes in the upper right hand corner of their window that allow you to search different sites. These can be used for searching the new version of Gatherer as well. Here are instructions for searching Gatherer with different browsers:

### Firefox

 If you would like to add Gatherer to the search box: 1) 1. Download and save this file: <http://www.wizards.com/mtg/misc/gatherer/firefox_search_plugin/gatherer.xml> to your "C:\Program Files\Mozilla Firefox\searchplugins" (where "C:\Program Files\Mozilla Firefox" is the directory you installed Firefox to) directory.
2. Restart Firefox.
3. Now, you should see it in the search dropdown list:  
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_1.bmp)
4. If you wanted to make Gatherer the default search engine, you could do that through the "Manage Search Engines…" dialog.

If you would like to make a search keyword for Gatherer:

1. A search keyword is a quick search you can do from the main Firefox address bar. Firefox provides an automated way to do this by right-clicking on search boxes and clicking "Add a Keyword for this Search…". However, to add one for Gatherer, go to your bookmarks menu and right-click in the folder you want to add the search to and click "New Bookmark":  
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_2.bmp)
2. In the dialog box that comes up, enter the following values:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_3.bmp)  
Where "Name" is the name of the bookmark as it will appear in your bookmarks menu, "Keyword" is what you will type first in the address bar when you want to do a search, and "Location:" is the search you would like to perform. Change the "Location:" field based on what you would like to search:


**Just Card Name:**   
<http://beta.gatherer.wizards.com/pages/search/default.aspx?name=%s>  
**Card Name, Type, Text:**  
<http://beta.gatherer.wizards.com/Pages/Search/Default.aspx?name=%s>||type=%s||subtype=%s||text=%s


The idea here is that you can use any Gatherer search that you’re able to perform and substitute in the search terms into the query. For example, if you wanted to just search artist you can go to the Advanced Search page, and do an artist search. The search string would look like: 


[http://beta.gatherer.wizards.com/Pages/Search/Default.aspx?action=advanc...](http://beta.gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&artist=)**artistnameyoutypedin**


Then, just substitute the "artistnameyoutypedin" with the "%s" value and you have your automatic search.
3. Now, you can try out your new search by typing the keyword and search terms into the address bar:  
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_4.bmp)  
 Which should automatically perform the search for you and take you to the results page.

### Internet Explorer 7

If you would like to add Gatherer to the search box:

1. Click on the little drop down next to the search button and select "Find More Providers…":  
![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_5.bmp)
2. On the webpage that that option takes you to, fill in the following information for the "Create Your Own" section:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/arcana/1727_gathkw_6.bmp)  
**URL:** <http://beta.gatherer.wizards.com/pages/search/default.aspx?name=TEST>  
 Name: Gatherer


Where, same as for Firefox, the URL is customized to the search you would like to make. If you wanted the same name, type, and text search, the URL would look like this:



> <http://beta.gatherer.wizards.com/Pages/Search/Default.aspx?name=TEST>||type=TEST||subtype=TEST||text=TEST
> 
> 
> When finished, click "Install". You can customize your search providers through the "Change Search Defaults" menu option on the menu of step 1.
> 
> 
>

Although the steps and menu options may be slightly different, you should be able to employ the same technique for other browsers which have search boxes.







