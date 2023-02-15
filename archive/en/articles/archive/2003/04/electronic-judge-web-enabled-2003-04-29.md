
---
[Link to Wayback Machine](https://web.archive.org/web/20210501184606/https://magic.wizards.com/en/articles/archive/electronic-judge-web-enabled-2003-04-29)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Kendall Redburn In my last article I thought about serving DCI Reporter to mobile devices at tournaments. I was so excited by the prospect of having a web served to my PDA that allowed me access to DCI Reporter that I decided to go ahead and just do it. I developed the web pages and tested them at a local JSS tournament run by Dorian Anders. For the non-technical here is the"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "938481"
[_metadata_:path_date]:- "2003-04-29"
[_metadata_:publish_date]:- "2015-12-07"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Electronic Judge - Web Enabled"
[_metadata_:wayback_capture_timestamp]:- "2021-05-01 18:46:06"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210501184606id_/https://magic.wizards.com/en/articles/archive/electronic-judge-web-enabled-2003-04-29"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/electronic-judge-web-enabled-2003-04-29"
---


The Electronic Judge - Web Enabled
==================================



 Posted in [NEWS](/en/articles?source=MX_Nav2020)
 on December 7, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_author.jpg)
By Wizards of the Coast











*Kendall Redburn*


In my last article I thought about serving DCI Reporter to mobile devices at tournaments.  

I was so excited by the prospect of having a web served to my PDA that allowed me access to DCI Reporter that I decided to go ahead and just do it. I developed the web pages and tested them at a local JSS tournament run by Dorian Anders.


**For the non-technical here is the scoop**: I walked around the floor of a tournament, and was able to look up on my Toshiba PDA; rules, pairings, standings, penalties and DCI numbers from any of the tournaments being held at the event. You can skip over the semi-technical details now and skip to the pictures from the tournament.


**For the slightly more technical**: I did this by hosting web pages on a laptop that was accessible through radio communication to my PDA. By browsing these web pages with Internet Explorer on my PDA I was able to view live tournament information. This was a local narrow web, as opposed to the World Wide Web.


**For the technical**: I developed a web site that read in and interpreted the data files that DCI reporter generates during tournaments. The web was hosted on the tournament organizer's laptop running IIS under Microsoft Windows XP Professional. The web was broadcast through an 802.11 wireless peer to peer network. I encourage people to try this at home.


**How to do it**  

You need a couple elements in order to create a wireless web server. You need a laptop with web server software, a wireless connector, and a website to broadcast. In my last article I described how to create an ad-hoc network between PDA's and a laptop. Building off of that model I was able to add the other two components and create a laptop serving a website to my Toshiba Pocket PC through WiFi, or 802.11 wireless network.


The first step was to upgrade the tournament laptop to Windows XP professional addition. This cost $199 for the upgrade. It took ninety minutes to install the software, and required me to dial a fifty four-digit number into my phone in order to activate the operating system. Please note that Windows XP home addition does not have web-serving capability, you must purchase the professional version. Upgrading the laptop required me to reinstall and re-configure the drivers for my printer, my wireless adapter, and re-configure my networks. I may also have to upgrade my Microsoft Office application at an additional cost. Consider all this before making the plunge. The total conversion and setup time was in the neighborhood of four hours. At the end of that time I was able to enter a static IP address into my browser software on my PDA and observe that the simple web page would view.


Step two: I needed a web to host. I figured there was a good chance that some useful information could be extracted from the files that DCI reporter generates. I downloaded the latest version of DCI reporter and created a fake tournament. I directly opened the tournament files with a text editor and deciphered them. This allowed me to create scripts to extract and publish tournament information on the little local web I had set up. I developed the web pages to allow me to browse through tournaments on the host computer, select a tournament, and then view information from that event. Fear not technically savvy reader, the DCI Tournament files are opened strictly read only and closed promptly and correctly so as to not interfere with the reporter software.


Besides having live tournament information available; I had the second goal of live access to hypertext linked rules documents. The rules documents are already loaded on my PDA, but can be difficult to navigate through using a word processor. I was asked a rules question about a clone coming into play. I was able to quickly bring up the comprehensive rules, tap on the link to section 5, tap on the link to section 503, and review the rules easily within seconds of the question being asked.


Did it work?


Yes, it worked. In fact it worked very well. I did encounter some problems but understood where they came from and will have fixes for them. There were several situations where the device proved to be valuable. One of our tournament players had a slight physical handicap, and as a courtesy the judges inform that player of his seat assignment. From the floor I could read off that player's table assignment while another judge was posting the pairings. I did not have to brave the crowds, or shout up at the judge's station to get this player his seat. In a similar vein, one player asked me if the Standard tournament had started. I was able to bring up the tournament information, and send him directly to his seat. These only took a few seconds and did not require me to find the judge in charge, walk to the back of the room, or shout at anybody. All throughout the tournament I was able to answer questions about events and their status without bothering the judge at the front.


This is the main screen. Keep in mind this is still a concept model, and not authorized by Wizards of the Coast. Of course I used their logo to make it look cool. Prices subject to change without notice, offer valid only with approved financing, do not take internally, use as prescribed, void where prohibited. Portions may copyright by Wizards of the Coast, all trademarks are the property of their respective owners.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_1.jpg)


This is the lower half of the front screen, showing the tournament navigation. This is a good reason for tournament organizers to put their events into folders. Judges should not have to scroll through a long list of tournaments looking for the correct one. The large folder is the currently open folder. Sub-folders are shown as the smaller folders. Any available tournaments in the folder are listed with the DCI logo. These tournaments do not need to be opened in DCI Reporter in order to examine their data.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_2.jpg)


Test Tournament 2 was created with fake names and DCI numbers, and fake results entered. This is the main screen judges will work from. The rules are available for quick reference. The player list shows enrolled players and DCI #'s. The Active Round screens shows the pairings and results for the current round. If there are any penalties entered, they will be available to view. Standings and Pairings from each round may also be available. They are only available if the judge entering tournament results cooperates and generates these files each round. DCI Reporter does not create them automatically. To create them, after each pairing, the judge selects "Copy Pairings to file" menu, and saves the file in HTML format in the same folder as the tournament event. Then a similar procedure is used for the standings at the end of each round.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_3.jpg)


This is what a player list would look like. There is no capacity to sort players alphabetically because they are not kept in a database. Adding a SQL like database would severely limit the possible scope of this but is not out of the question.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_4.jpg)


Here is what an active round looks like. The judge should remember to refresh this page each time he or she consults it. In this example, table numbers started at 23. Tables 26, 27, 29 and 30 have reported.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_5.jpg)


In a small tournament it's easy to keep track of who is getting penalties. In a larger tournament, having them at your fingertips can be a real advantage for the judge. It is possible to view penalties from other tournaments that are still on the host computer if there is a question of the player's past history.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_6.jpg)


This is what a standings file looks like. My web adds the gray lines. These files are manually created at the end of each round. My hope is that there will soon be an option to make them automatic.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_7.jpg)


The second but equally important section of this web is the rules section. This may be a surprise to some, but the rules documents published on [www.wizards.com](http://www.wizards.com) are all in Word or plain text format. None of them are in html, the language of the Internet. All of the documents that I wanted available I had to index and link in order to make them useful. In the example below I added a linked table of contents to the floor rules for quick navigation.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_8.jpg)


In the comprehensive rules, I added links to all the referenced rules. This allows the judge to easily move from section to section. As you see below, if you are reading up on how to declare legal attacks and blocks, you can jump right to rule 308, "Declare Attackers Step" and so forth.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419a_9.jpg)


The FAQ's and Recent Rulings are partially available. They only cover the most recent sets for the Standard environment. These files may be better as searchable text documents. They were not well suited for quick browsing.


I did have problems, most were minor, and some require software updates. One problem was refreshing pages. My device would hold a cached version of the tournament status. If the power saving feature on my device shut down the network, then Internet Explorer would show me the cached version of the tournament information. I did not always catch this mistake. Players that dropped were not accounted for in the pairings table, the software would show empty tables as games in progress. I also noticed that browsing was impaired while the tournaments were being backed up to floppy disk.


Some mini web browsers do not include a find function, so some documents are harder to browse via the web than a built in word processor. For instance, the list of all cards printed is not practical to scroll through.


I will be adding the local server time to the top of each page, plus stopping some pages from caching. I will also be looking into adding independent round clocks for the events. The head judge for an event would be able to start the web clock and other judges with connected devices would be able to access one single clock. Each judge, including the one at the head computer, would have a page showing all running event clocks on one screen.


I do want this web to be available for the general Magic judge population to use, and for Wizards of the Coast to distribute it on their DCI CD-ROM. I plan to maintain and improve the site, and hope to work with the DCI Reporter software to better integrate the two. I am going to continue to develop and maintain this technology. I don't know where this is going to end up, but I'm excited about it. I am willing to answer questions and to a limited extent provide technical support. Contact me at [Kendall@professor-oak.com](mailto:Kendall@professor-oak.com).


*Editor's note: I have to admit that I was a bit skeptical as to how useful this would be until I saw it in action. Now I am considering buying myself a PDA. To have at my fingertips the answers to the most frequently asked player questions (How much time is left in the round? Did my opponent report our results? Did the T2 event start yet? etc.) is quite a temptation. -Dorian Anders*







