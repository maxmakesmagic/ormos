
---
[Link to Wayback Machine](https://web.archive.org/web/20160113074431/http://magic.wizards.com/en/articles/archive/news/magic-online-faq-connection-2013-12-08)

[_metadata_:description]:- "I can't connect to Magic Online. What's going on? The first thing to check is whether or not Magic Online is currently down. There are two places you can look.       1. You can click here and check the server status light near the bottom of the page. If Magic Online is currently live, it will display a green light like so:  "
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "119016"
[_metadata_:publish_date]:- "2013-12-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online: FAQ for Connection"
[_metadata_:wayback_capture_timestamp]:- "2016-01-13 07:44:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160113074431id_/http://magic.wizards.com/en/articles/archive/news/magic-online-faq-connection-2013-12-08"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/news/magic-online-faq-connection-2013-12-08"
---


Magic Online: FAQ for Connection
================================



 Posted in **News**
 on December 8, 2013 










**I can't connect to Magic Online. What's going on?**  

The first thing to check is whether or not Magic Online is currently down. There are two places you can look.  

      1. You can [click here](http://archive.wizards.com/Magic/Digital/MagicOnline.aspx) and check the server status light near the bottom of the page. If Magic Online is currently live, it will display a green light like so:  

 




|  |  |
| --- | --- |
|  | Magic Online is currently live |

      2. For information about any sort of server difficulty, unexpected downtime or Magic Online updates you can visit the Magic Online Blog by [clicking here](http://community.wizards.com/magiconline/blog/).  
  
**The servers are up! How do I check my connection to the Magic Online servers?** or **How do I run a tracert?**  

Windows has a built in program that can give you a report of what is happening when you try and communicate with a site or service on the internet. Below are instructions on using this program known as "tracert".




|  |  |
| --- | --- |
|       1. Press the "Start" button on your Windows task bar and then select "Run".
       2. Type **cmd** and then hit "Enter"
       3. This should open a command prompt that looks like the picture on the right.
       4. Type **tracert mtgologin1.onlinegaming.wizards.com** and then hit "Enter". | Command prompt - C:\ |

The numbers represent the number of milliseconds it takes to talk to our servers. All of your times should be below 250ms and the total number of lines should be less than twenty. An asterisk (\*) is a bad sign as it means that some of the information you sent did not arrive. If the numbers are over 300ms this means your connection to our servers is slow. If you perform a tracert and you do not get any respons, or it fails altogether then it is a problem with your computer or network. If it fails on the first few lines likely it is a problem within your Internet Service Provider (ISP). If it gets out of your ISP's severs and starts failing then it is a problem with the wilds of the Internet.  
  
**What are the most common causes of connection issues? What can I do to fix them?**  

Connection trouble can be caused by many different sources.  

• Dial-up, Satellite, Cellular (Tethering), Air Card (EVDO/LTE/4G) or other non-landline or non-broadband internet connections can often times cause the inability to connect to Magic Online or cause frequent disconnections. We do not recommend using any of these types of connections to play the game and suggest using a landline broadband service like DSL or Cable instead.  

• Connecting through a wireless router this might cause issues. Wireless connections are slower than physical connections and are prone to interfereance. You can try connecting directly using a physical cable to see if that sovles the issue.  

• Security software (like Norton Internet Security), Firewalls (like Zone Alarm or Windows Firewall) and Anti-virus software (like McAfee) can all interfere with the operation of the client and your connection to our severs. We recommend *temporarily* disabling this software to see if it is the source of your connection problems.  

• Faulty or incorrectly setup computer and networking hardware can also cause issues. If you suspect this might be the source of your problem, you will need to contact the manufacturer of that hardware or a computer repair professional for further assistance.  

• Viruses or Malware on your computer may interfere with Magic Online software and your connection. You can get the free anti-virus software Microsoft Security essentials by [clicking here](http://windows.microsoft.com/en-US/windows/products/security-essentials). If you suspect that your computer may be infected with a virus or afflicted with malicious programs, please contact a computer repair professional immediately.  
  
**I've tried all of the suggestions I still can't figure out how to fix my connection issues. Can you help?**  

You can contact our support team by clicking the "Email Us" tab at the top of this page. They will need the following two things to help them determine what might be causing your issue.  

      1. A screenshot of the error message you are getting and a screenshot of the tracert you ran in the previous step. You can learn how to take screenshots and attach them to incidents by [clicking here](http://wizards.custhelp.com/app/answers/detail/a_id/2223).  

      2. Please include the type of connection you're using (Cable, Dial-up, etc.), which operating system you're using (Windows XP, Vista, etc.) as well any other information you think might be useful in tracking down the source of the problem.  
  
**I'm using a firewall. Can you tell me what ports does Magic Online uses?**  

If you have a firewall enabled, be sure that the following ports are open: **7730, 7770,** (All TCP). If one of these is blocked, when the game attempts a connection using that particular port, the connection will fail, resulting in the issue you've been experiencing. This may occur even if other aspects of the game appear to be functioning normally. For help with how to open those ports, you will need to contact the maker of your software, router, or network administrator.







