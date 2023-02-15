
---
[Link to Wayback Machine](https://web.archive.org/web/20150111033612/http://magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04)

[_metadata_:description]:- "I can't connect to Magic Online. What's going on? The first thing to check is whether or not Magic Online is currently down. There are two places you can look. 1. You can click here and check the server status light near the top of the page. If Magic Online is currently live, it will display a green light like so:  "
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "draft"
[_metadata_:publish_date]:- "2014-06-04"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "MAGIC ONLINE: FAQ FOR CONNECTION"
[_metadata_:wayback_capture_timestamp]:- "2015-01-11 03:36:12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150111033612id_/http://magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04"
---


MAGIC ONLINE: FAQ FOR CONNECTION
================================



 Posted in **MTGO General Resources**
 on June 4, 2014 









**I can't connect to *Magic Online*. What's going on?**


The first thing to check is whether or not *Magic Online* is currently down. There are two places you can look.


1. You can [click here](http://magic.wizards.com/en/game-info/products/magic-online) and check the server status light near the top of the page. If *Magic Online* is currently live, it will display a green light like so:  


![Magic Online is currently live](https://web.archive.org/web/20171025132648im_/http://www.wizards.com/mtg/images/digital/magiconline/MTGO_Server_Status.png)


2. For information about any sort of server difficulty, unexpected downtime or *Magic Online* updates you can visit the *Magic Online* Blog on the *Magic Online* [home page](http://magic.wizards.com/en/game-info/products/magic-online).


**The servers are up! How do I check my connection to the *Magic Online* servers?** or **How do I run a tracert?**


Windows has a built in program that can give you a report of what is happening when you try and communicate with a site or service on the internet. Below are instructions on using this program known as "tracert".


1. Press the "Start" button on your Windows task bar and then select "Run".
2. Type **cmd** and then hit "Enter"
3. Type **tracert mtgologin1.onlinegaming.wizards.com** and then hit "Enter".

The numbers represent the number of milliseconds it takes to talk to our servers. All of your times should be below 250ms and the total number of lines should be less than twenty. An asterisk (\*) is a bad sign as it means that some of the information you sent did not arrive. If the numbers are over 300ms this means your connection to our servers is slow. If you perform a tracert and you do not get any response, or it fails altogether then it is a problem with your computer or network. If it fails on the first few lines likely it is a problem within your Internet Service Provider (ISP). If it gets out of your ISP's severs and starts failing then it is a problem with the wilds of the Internet.


**What are the most common causes of connection issues? What can I do to fix them?**


Connection trouble can be caused by many different sources.


* Dial-up, Satellite, Cellular (Tethering), Air Card (EVDO/LTE/4G) or other non-landline or non-broadband internet connections can often times cause the inability to connect to *Magic Online* or cause frequent disconnections. We do not recommend using any of these types of connections to play the game and suggest using a landline broadband service like DSL or Cable instead.
* Connecting through a wireless router this might cause issues. Wireless connections are slower than physical connections and are prone to interference. You can try connecting directly using a physical cable to see if that solves the issue.
* Security software (like Norton Internet Security), Firewalls (like Zone Alarm or Windows Firewall) and Anti-virus software (like McAfee) can all interfere with the operation of the client and your connection to our severs. We recommend *temporarily* disabling this software to see if it is the source of your connection problems.
* Faulty or incorrectly setup computer and networking hardware can also cause issues. If you suspect this might be the source of your problem, you will need to contact the manufacturer of that hardware or a computer repair professional for further assistance.
* Viruses or Malware on your computer may interfere with *Magic Online* software and your connection. You can get the free anti-virus software Microsoft Security essentials by [clicking here](http://windows.microsoft.com/en-US/windows/products/security-essentials). If you suspect that your computer may be infected with a virus or afflicted with malicious programs, please contact a computer repair professional immediately.

**I've tried all of the suggestions I still can't figure out how to fix my connection issues. Can you help?**


You can contact our support team [here](https://wizards.custhelp.com/app/ask). They will need the following two things to help them determine what might be causing your issue.


1. A screenshot of the error message you are getting and a screenshot of the tracert you ran in the previous step. You can learn how to take screenshots and attach them to incidents through this [page](http://wizards.custhelp.com/app/answers/detail/a_id/2223).
2. Please include the type of connection you're using (Cable, Dial-up, etc.), which operating system you're using (Windows 7, Vista, etc.) as well any other information you think might be useful in tracking down the source of the problem.

**I'm using a firewall. Can you tell me what ports does *Magic Online* uses?**


If you have a firewall enabled, be sure that the following ports are open: **7730, 7770,** (All TCP). If one of these is blocked, when the game attempts a connection using that particular port, the connection will fail, resulting in the issue you've been experiencing. This may occur even if other aspects of the game appear to be functioning normally. For help with how to open those ports, you will need to contact the maker of your software, router, or network administrator.







