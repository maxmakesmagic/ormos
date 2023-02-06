
---
[Link to Wayback Machine](https://web.archive.org/web/20160422021544/http://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16)

[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160422021544id_/http://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16"
[_metadata_:wayback_capture_timestamp]:- "2016-04-22 02:15:44+00:00"
[_metadata_:publish_date]:- "2010-12-16"
[_metadata_:description]:- "Summary Construction of the new Magic Online client is running full-bore, and we are targeting late Q1 2011 for a game play beta focused on the new 2-player duel scene. A beta for the full client would follow when all the scenes have finished construction. We continue to work on infrastructure improvements in order to ensure continued system stability. We are starting to take on feature development projects in addition to the infrastructure updates. The system is continuing to perform well as the user base expands."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Magic Online Development Update Q4 2010
=======================================



 Posted in **Feature**
 on December 16, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











**Summary**   
 Construction of the new ****Magic Online**** client is running full-bore, and we are targeting late Q1 2011 for a game play beta focused on the new 2-player duel scene. A beta for the full client would follow when all the scenes have finished construction. We continue to work on infrastructure improvements in order to ensure continued system stability. We are starting to take on feature development projects in addition to the infrastructure updates. The system is continuing to perform well as the user base expands. 

**New Client**  
 The new client is being built using Windows Presentation Foundation (WPF). WPF was our chosen platform when the design project began. We explored using Silverlight in the hopes of opening up more access to **Magic Online**. In the end, we were unable to find realistic solutions for several issues relating to integrating a Rich Internet Application with our server infrastructure. The shared design environment for WPF and Silverlight means that very little design time was lost in that exploration process. WPF will offer rapid entry into **Magic Online** for new and existing players with a much lighter install and launch process. WPF provides a richer set of user controls, which is helpful to providing a solid user experience. The platform will allow us to respond rapidly to usability findings. WPF also provides very good support for QA testing.

**Infrastructure Update**  
 Our next major infrastructure project will be to deserialize all of the digital objects. Currently the system stores all digital objects individually in the database as part of the original system design. The system currently does not use the serialization, and stacking like digital objects will further reduce the risk of contention in the database. As this is implemented, we will move away from having to ‘print’ collated product such as boosters and store them in the database. This eliminates the possibility of ‘running out’ of a certain class of product. All of these changes will significantly improve the scalability of the greater system, reduce maintenance downtime, and will improve usability. 

**Q4 Maintenance**  
 The single managed connection module that shipped in September has given us a lot of information about the primary issues that users have been reporting. Logging was significantly improved with that module, and we have been able to isolate the majority of the most reported issues to problems with temporary state management in the client. Our client devs are intensly focused on supporting the new client, so we have chosen to take some aggressive action to solve the current client’s bad behavior on logoff and disconnects. We realize this is less than ideal for a subset of users, but we feel that it is a net gain for those folks who previously were having issues with empty sideboards and not reconnecting to drafts after disconnections.

**2011 Development Plan**


- Deliver card set releases

- WPF Client

- Alternate Entry Fees

- Stacked Digital Objects

- Real-time Collation

- Multiplayer Support – Improved player management, new multiplayer duel scene in the WPF client.

- Leagues – Chris (WotC\_K) will talk more about Leagues in Q1 2011. Internal project name = Sandwiches.

- Additional Features – announcement and details in Q2
Gordon Culp  
 Director – Game Systems Design  
**Magic: The Gathering** Digital Studio  
 Wizards of the Coast, LLC  


- **[Discuss on the message boards.](http://community.wizards.com/go/thread/view/75846/26468501/Q4_2010_Development_Update_Discussion)**






