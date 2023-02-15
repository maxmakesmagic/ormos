
---
[Link to Wayback Machine](https://web.archive.org/web/20150624072455/http://magic.wizards.com/en/articles/archive/magic-online-technical-troubleshooting)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Please note: If you do not feel comfortable performing any of these steps, we suggest contacting a computer specialist for assistance. Quicklinks Crash and Performance Troubleshooting Clean Installation (Reinstalling) Connection Troubleshooting Crash and Performance Troubleshooting"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "394531"
[_metadata_:publish_date]:- "2015-06-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online: Technical Troubleshooting"
[_metadata_:wayback_capture_timestamp]:- "2015-06-24 07:24:55"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150624072455id_/http://magic.wizards.com/en/articles/archive/magic-online-technical-troubleshooting"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/magic-online-technical-troubleshooting"
---


Magic Online: Technical Troubleshooting
=======================================



 Posted in [Magic Online General Resources](/es/content/mtgo-general-resources)
 on June 2, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











**Please note:** If you do not feel comfortable performing any of these steps, we suggest contacting a computer specialist for assistance.


### Quicklinks


* [Crash and Performance Troubleshooting](#crashtroubleshooting)
* [Clean Installation (Reinstalling)](#reinstalling)
* [Connection Troubleshooting](#connection)



---

Crash and Performance Troubleshooting
=====================================



If you experience a crash or performance problem with *Magic Online*, follow these steps:


### Check System Requirements


Verify that your computer meets the minimum [system requirements](http://magic.wizards.com/en/content/download) for *Magic Online*.


### Connection Troubleshooting


Refer to the the Connection Troubleshooting section [below](#connection) to see if you may be having issues caused by your internet connection. Ultimately any issues with your connection need to be solved by you, a computer repair professional, and/or your Internet Service Provider (ISP).


### Password Management Programs


If you are using a password management program, check your application settings to make sure that it is not automatically attaching to Windows applications. Programs like these can cause serious performance issues with the client.


### Clean Reinstall


For all other issues, follow the steps below to uninstall *Magic Online* and perform a clean install.




---

Clean Installation (Reinstalling)
=================================



These steps should resolve a wide range of issues including (but not limited to) a bad installation, improperly cached files, or corrupted files.


It is important that you follow these steps in order (including restarting your computer) to make sure the cache clearing happens and that the new installation is completely fresh.


### Uninstall Magic Online



1. Press Windows key + R or go to Start -> Run (or Search -> Run, then Click Run in Windows 8)
  
3. In the box type:  

 control appwiz.cpl
  
5. Click “OK”
  
7. This will pull up a list of installed programs. Scroll down to the “M”s and you should see one or more programs that start with “*Magic the Gathering Online*." It should look similar to this:
 ![](https://media.wizards.com/2015/mtgo/Resources_Technical_Troubleshooting_img1.jpg)
8. Right click the “*Magic the Gathering Online*” version and then select “Uninstall/Change” and follow the prompts.
  
10. Repeat this process until all of the *Magic Online* programs have been uninstalled.


### Clear the ClickOnce Cache



1. Press Windows Key + R or go to Start -> Run (Search -> Run, then Click Run in Windows 8)
  
3. In the box type:  

 rundll32 dfshim CleanOnlineAppCache
  
5. Then click “OK” (if prompted)


### Restart your computer


Restart your computer and install the client from the link below: <http://magic.wizards.com/en/content/download>


### If That Doesn't Work, Try These Steps


If you are still having issues with *Magic Online*, continue with the following steps:



1. Uninstall *Magic Online*
  
3. Press Windows key + R
  
5. Type %LocalAppData%\Apps
  
7. Delete the 2.0 folder
  
9. Download and install the client from this link: <http://magic.wizards.com/en/content/download>


### Contact Game Support


If after reinstalling the client you still experience the issue, [contact customer support](http://wizards.custhelp.com/app/ask).




---


Connection Troubleshooting
==========================


### I can't connect to *Magic Online*. What's going on?


The first thing to check is whether or not *Magic Online* is currently down. There are two places you can look.


1. You can [click here](http://magic.wizards.com/en/game-info/products/magic-online) and check the server status light near the top of the page. If *Magic Online* is currently live, it will display a green light like so:  


![Magic Online is currently live](https://web.archive.org/web/20171025132648im_/http://www.wizards.com/mtg/images/digital/magiconline/MTGO_Server_Status.png)


2. For information about any sort of server difficulty, unexpected downtime or *Magic Online* updates you can visit the *Magic Online* Blog on the *Magic Online* [home page](http://magic.wizards.com/en/game-info/products/magic-online).


### The servers are up! How do I check my connection to the *Magic Online* servers? or How do I run a tracert?


Windows has a built in program that can give you a report of what is happening when you try and communicate with a site or service on the internet. Below are instructions on using this program known as "tracert".


1. Press the "Start" button on your Windows task bar and then select "Run".
2. Type **cmd** and then hit "Enter"
3. Type **tracert mtgologin1.onlinegaming.wizards.com** and then hit "Enter".

The numbers represent the number of milliseconds it takes to talk to our servers. All of your times should be below 250ms and the total number of lines should be less than twenty. An asterisk (\*) is a bad sign as it means that some of the information you sent did not arrive. If the numbers are over 300ms this means your connection to our servers is slow. If you perform a tracert and you do not get any response, or it fails altogether then it is a problem with your computer or network. If it fails on the first few lines likely it is a problem within your Internet Service Provider (ISP). If it gets out of your ISP's severs and starts failing then it is a problem with the wilds of the Internet.


### What are the most common causes of connection issues? What can I do to fix them?


Connection trouble can be caused by many different sources.


* Dial-up, Satellite, Cellular (Tethering), Air Card (EVDO/LTE/4G) or other non-landline or non-broadband internet connections can often times cause the inability to connect to *Magic Online* or cause frequent disconnections. We do not recommend using any of these types of connections to play the game and suggest using a landline broadband service like DSL or Cable instead.
* Connecting through a wireless router might cause issues. Wireless connections are slower than physical connections and are prone to interference. You can try connecting directly using a physical cable to see if that solves the issue.
* Security software (like Norton Internet Security), Firewalls (like Zone Alarm or Windows Firewall) and Anti-virus software (like McAfee) can all interfere with the operation of the client and your connection to our severs. We recommend *temporarily* disabling this software to see if it is the source of your connection problems.
* Faulty or incorrectly setup computer and networking hardware can also cause issues. If you suspect this might be the source of your problem, you will need to contact the manufacturer of that hardware or a computer repair professional for further assistance.
* Viruses or Malware on your computer may interfere with *Magic Online* software and your connection. You can get the free anti-virus software Microsoft Security essentials by [clicking here](http://windows.microsoft.com/en-US/windows/products/security-essentials). If you suspect that your computer may be infected with a virus or afflicted with malicious programs, please contact a computer repair professional immediately.

### I've tried all of the suggestions I still can't figure out how to fix my connection issues. Can you help?


You can contact our support team [here](https://wizards.custhelp.com/app/ask). They will need the following two things to help them determine what might be causing your issue.


1. A screenshot of the error message you are getting and a screenshot of the tracert you ran in the previous step. You can learn how to take screenshots and attach them to incidents through this [page](http://wizards.custhelp.com/app/answers/detail/a_id/2223).
2. Please include the type of connection you're using (Cable, Dial-up, etc.), which operating system you're using (Windows 7, Vista, etc.) as well any other information you think might be useful in tracking down the source of the problem.

### I'm using a firewall. Can you tell me what ports does *Magic Online* uses?


If you have a firewall enabled, be sure that the following ports are open: **7730, 7770,** (All TCP). If one of these is blocked, when the game attempts a connection using that particular port, the connection will fail, resulting in the issue you've been experiencing. This may occur even if other aspects of the game appear to be functioning normally. For help with how to open those ports, you will need to contact the maker of your software, router, or network administrator.


### I'm using a Mac. Can I play *Magic Online*?


The Limited Resources podcast has a great guide on their website about getting *Magic Online* running on a Mac. You can read the whole article [here](http://lrcast.com/magic-online-on-a-mac/).







