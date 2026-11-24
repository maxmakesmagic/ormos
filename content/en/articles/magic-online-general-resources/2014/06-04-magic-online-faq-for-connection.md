---
id: wpzg3en5
kind: article
lang: en
path: /en/articles/magic-online-general-resources/2014/06-04-magic-online-faq-for-connection
title: 'MAGIC ONLINE: FAQ FOR CONNECTION'
published: '2014-06-04'
column_slug: magic-online-general-resources
column: Magic Online General Resources
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    lang_detected: en
    capture_id: 778871
    url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    captured_at: '2016-05-11 00:36:44+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    lang_detected: en
    capture_id: 778871
    url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    captured_at: '2016-05-11 00:36:44+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    lang_detected: en
    capture_id: 778871
    url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    captured_at: '2016-05-11 00:36:44+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    lang_detected: en
    capture_id: 778871
    url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
    captured_at: '2016-05-11 00:36:44+00'
    rule: url.article_section
sources:
- document_id: wpzg3en5
  url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
  page_key: magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
  lang: en
  template: drupal
  captured_at: '2016-05-11 00:36:44+00'
  capture_id: 778871
  wayback_url: https://web.archive.org/web/20160511003644id_/http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
- document_id: wpzg3en5
  url: http://magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04
  page_key: magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04
  lang: en
  template: drupal
  captured_at: '2015-01-11 03:36:12+00'
  capture_id: 949674
  wayback_url: https://web.archive.org/web/20150111033612id_/http://magic.wizards.com/en/articles/archive/mtgo-general-resources/magic-online-faq-connection-2014-06-04
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: wpzg3en5
  capture_id: 778871
  url: http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
  wayback_url: https://web.archive.org/web/20160511003644id_/http://magic.wizards.com/en/articles/archive/magic-online-general-resources/magic-online-faq-connection-2014-06-04
  captured_at: '2016-05-11 00:36:44+00'
  template: drupal
  sha256: 9ce7b54de826aed5d84aee5210828c4520db7fa0b29956eb825455d7dca0845b
render_recovery: []
---
**I can't connect to *Magic Online*. What's going on?**

The first thing to check is whether or not *Magic Online* is currently down. There are two places you can look.

1\. You can [click here](https://web.archive.org/web/20140604000000/http://magic.wizards.com/en/game-info/products/magic-online) and check the server status light near the top of the page. If *Magic Online* is currently live, it will display a green light like so:  

![Magic Online is currently live](https://i.ormos.uk/6c/77/6c77212c992dcf10f07db2f37a21ff795b9d619d4d6ac7ec1f1fe442137dc5cd.png)

2\. For information about any sort of server difficulty, unexpected downtime or *Magic Online* updates you can visit the *Magic Online* Blog on the *Magic Online* [home page](https://web.archive.org/web/20140604000000/http://magic.wizards.com/en/game-info/products/magic-online).

**The servers are up! How do I check my connection to the *Magic Online* servers?** or **How do I run a tracert?**

Windows has a built in program that can give you a report of what is happening when you try and communicate with a site or service on the internet. Below are instructions on using this program known as "tracert".

1.  Press the "Start" button on your Windows task bar and then select "Run".
2.  Type **cmd** and then hit "Enter"
3.  Type **tracert mtgologin1.onlinegaming.wizards.com** and then hit "Enter".

The numbers represent the number of milliseconds it takes to talk to our servers. All of your times should be below 250ms and the total number of lines should be less than twenty. An asterisk (\*) is a bad sign as it means that some of the information you sent did not arrive. If the numbers are over 300ms this means your connection to our servers is slow. If you perform a tracert and you do not get any response, or it fails altogether then it is a problem with your computer or network. If it fails on the first few lines likely it is a problem within your Internet Service Provider (ISP). If it gets out of your ISP's severs and starts failing then it is a problem with the wilds of the Internet.

**What are the most common causes of connection issues? What can I do to fix them?**

Connection trouble can be caused by many different sources.

*   Dial-up, Satellite, Cellular (Tethering), Air Card (EVDO/LTE/4G) or other non-landline or non-broadband internet connections can often times cause the inability to connect to *Magic Online* or cause frequent disconnections. We do not recommend using any of these types of connections to play the game and suggest using a landline broadband service like DSL or Cable instead.
*   Connecting through a wireless router might cause issues. Wireless connections are slower than physical connections and are prone to interference. You can try connecting directly using a physical cable to see if that solves the issue.
*   Security software (like Norton Internet Security), Firewalls (like Zone Alarm or Windows Firewall) and Anti-virus software (like McAfee) can all interfere with the operation of the client and your connection to our severs. We recommend *temporarily* disabling this software to see if it is the source of your connection problems.
*   Faulty or incorrectly setup computer and networking hardware can also cause issues. If you suspect this might be the source of your problem, you will need to contact the manufacturer of that hardware or a computer repair professional for further assistance.
*   Viruses or Malware on your computer may interfere with *Magic Online* software and your connection. You can get the free anti-virus software Microsoft Security essentials by [clicking here](http://windows.microsoft.com/en-US/windows/products/security-essentials). If you suspect that your computer may be infected with a virus or afflicted with malicious programs, please contact a computer repair professional immediately.

**I've tried all of the suggestions I still can't figure out how to fix my connection issues. Can you help?**

You can contact our support team [here](https://wizards.custhelp.com/app/ask). They will need the following two things to help them determine what might be causing your issue.

1.  A screenshot of the error message you are getting and a screenshot of the tracert you ran in the previous step. You can learn how to take screenshots and attach them to incidents through this [page](http://wizards.custhelp.com/app/answers/detail/a_id/2223).
2.  Please include the type of connection you're using (Cable, Dial-up, etc.), which operating system you're using (Windows 7, Vista, etc.) as well any other information you think might be useful in tracking down the source of the problem.

**I'm using a firewall. Can you tell me what ports does *Magic Online* uses?**

If you have a firewall enabled, be sure that the following ports are open: **7730, 7770,** (All TCP). If one of these is blocked, when the game attempts a connection using that particular port, the connection will fail, resulting in the issue you've been experiencing. This may occur even if other aspects of the game appear to be functioning normally. For help with how to open those ports, you will need to contact the maker of your software, router, or network administrator.

**I'm using a Mac. Can I play *Magic Online*?**

The Limited Resources podcast has a great guide on their website about getting *Magic Online* running on a Mac. You can read the whole article [here](http://lrcast.com/magic-online-on-a-mac/).