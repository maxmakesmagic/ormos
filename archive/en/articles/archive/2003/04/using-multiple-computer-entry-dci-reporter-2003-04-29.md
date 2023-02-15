
---
[Link to Wayback Machine](https://web.archive.org/web/20160923044354/http://magic.wizards.com/en/articles/archive/using-multiple-computer-entry-dci-reporter-2003-04-29)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Kendall Redburn"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "938476"
[_metadata_:path_date]:- "2003-04-29"
[_metadata_:publish_date]:- "2015-12-07"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Using multiple computer entry with DCI Reporter"
[_metadata_:wayback_capture_timestamp]:- "2016-09-23 04:43:54"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160923044354id_/http://magic.wizards.com/en/articles/archive/using-multiple-computer-entry-dci-reporter-2003-04-29"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/using-multiple-computer-entry-dci-reporter-2003-04-29"
---


Using multiple computer entry with DCI Reporter
===============================================



 Posted in [ARTICLES](/en/articles)
 on December 7, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











*Kendall Redburn*


**The problem:**  

The challenge with all very large tournaments is how to register over four hundred players in a timely manner. Currently DCI Reporter does not support, or has not documented support for combining tournament entries from multiple sources. It is possible to do this, but it takes some preparation, planning and a little bit of business acumen. This document is a detailed explanation of the setup and procedures involved. The pay off is not just a tournament that starts on time and finishes on time, but the extra draw that comes from providing a favorable playing experience to your Magic the Gathering customers.


**The solution**:  

The overview of the system resembles a kind of assembly line. Players file into the hall after having filled out a registration form. Their form and entry fee are checked and accepted by the cashiers. The entry forms are routed by a runner to the data entry stations where they are keyed in. Think of a table of computers and in/out baskets filled with forms. At each computer a person repeatedly takes a form from the in-basket, enrolls the player and puts the form in the out-basket. The processed forms are collected and stored for the inevitable player who claims to have paid but is not listed in the tournament. When the data entry is finished, each operator delivers a disk to the main computer where the different tournaments are combined into one.


The requirements for this system are not great. There must be multiple computers available for data entry, all running DCI Reporter. It would be best if each station has the latest software and PIN database. Each computer must have a floppy drive. Each station must also have a blank floppy disk, labeled and inserted. The main data entry computer must have Microsoft Excel. It is assumed that the person who will do the final importing of data into the main tournament computer is fairly skilled with windows, DCI Reporter, and knows the basics of Excel.


**Preliminary setup**:  

Designate one computer as the primary or "Tournament" computer. This computer will host the tournament. Data entry at this computer proceeds as normal. Create the tournament with sanctioning number, max rounds, max players, etc. Enroll players as normal at this station. All data will eventually flow to this computer.


Secondary computers will create fake tournaments for later deletion. For each of the secondary stations, follow these procedures. Create a folder within DCI Reporter to hold the input tournaments. This will make them easy to delete later. Then create a new tournament within this folder. They will not be transmitted to the DCI and will be deleted after the data is transferred.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_1.jpg)


Set up a tournament as normal. It appears that DCI Reporter will not let you connect to the PIN Database unless DCI Sanctioned Tournament is checked, so leave that checked.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_2.jpg)


The most important step in the entire process is to set the tournament to pre-register the players in all the secondary input computers. To repeat: The primary tournament computer is used to enroll players, **all secondary computers are used to pre-register players**.


![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_3.jpg)


After setup is complete the next step is to train the operators. They must understand that the goal at the secondary computers is to successfully pre-register all of their data correctly. They should be familiar with DCI Reporter and should be kept free from distraction. All data entry stations must back up their data onto the floppy disks frequently. DCI Reporter does not automatically backup data, so each operator must remember to back up every five or ten minutes.


**Execution:**


Open the doors and start letting people in. The goal is to have enough staff so that the customers are not kept waiting. Consider how much you like shopping at a store that only has one cashier working and 400+ people in line. Since the transaction time is fairly short, consider three cashiers, four data entry stations, one runner and one supervisor for the operation.


After registration closes, close out each secondary data entry station.


1. Back up the data at the station onto the floppy disk.
2. Close the tournament.
3. Eject the floppy disk and deliver it to the main tournament computer.

Procedure to import pre-registration data into the primary computer.


1. Back up the main computer onto it's designated floppy disk.
2. Eject the floppy disk.
3. Insert the secondary station floppy.
4. Run Excel
5. Open the file a:\xxxxpreg.dat where xxxx is the tournament designation.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_4.jpg)
6. Follow the text import wizard steps. The file is delimited, click next.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_5.jpg)
7. Set the Comma delimiter, click next. (It only matters if you have the Comma checked, Tab can be checked or unchecked - it doesn't matter).  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_6.jpg)
8. Select the column of data with the DCI number, click on the "TEXT" column data format button. Finish the import. If your DCI numbers show up in Excel as 5.239e7 then you skipped this step.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_7.jpg)
9. The data in Excel must now be formatted for import into DCI Reporter. The format is LastName, FirstName, DCI #. Move the columns to accomplish this.  

 From this:  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_8.jpg)  

 To this. Note: Be careful to get the order right! last name, first name, DCI#.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_9.jpg)
10. **Select the extra columns of data and use the Delete function from the Edit menu to delete them**. If you delete them using the backspace key, the data will not import correctly into DCI Reporter and you will have to repeat this step. DCI Reporter will inform you that the data is not terminated correctly if you mess this step up.
11. Save the data onto the floppy disk (a:). Save it as a comma delimited file. Input.csv is the recommended name. Excel will ask you if it's ok to save it in this format. Answer Yes to the dialog. Saving the data on the floppy allows you to quickly re-build the entire tournament from the floppy disks if you mess up the import along the way. Note that the file type is set to CSV, the default is .TXT.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_10.jpg)
12. Return to DCI Reporter. In the Edit menu, select Pre register players by file...  

 Change the option to Comma Delimited. Click Select file, and locate the input.csv file on the floppy disk.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_11.jpg)
13. If the data was saved correctly, you will see a dialog stating how many players have been imported into the pre-registered players data. For this example only eight registrations were created.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_12.jpg)
14. Open the Players Data Entry screen. You will see your list of imported players now as pre-registered. If you look closely at the following examples, you will see that the players first and last names are in the wrong order.


Adam\*Player should be Player\*Adam


Be sure to check this before enrolling the players. If the names are in the wrong order, correct this in the input.csv file, and re-import them. Existing names in the pre-registered list will be erased when a new list is imported. (This is why you import one list at a time).


  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_13.jpg)
15. Select the first player on the list, but do not double click on the name. You can enroll all of the players at one time, instead of one at a time. Scroll to the bottom of the list of Pre-registered players. Hold down the shift key, and click on the last name on the list. This will select all players in the pre-registered list. There is no keyboard short cut for this task.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_14.jpg)
16. Press the button **Enroll All**. This will bring all selected Pre-registered players into the tournament. Any players that are duplicated or have problems will be left in the pre-registered players list. The most likely cause will be duplicated DCI numbers that will have to be corrected.  
![](https://media.wizards.com/legacy/dci/judge/images/jc20030419c_15.jpg)
17. Verify and Backup your data. First, verify that the enrolled players came in correctly and that there are no players left pre-registered. Once this is confirmed, back up the tournament. Consider backing up the combined data onto a different floppy than the one used for the original data entry. If an error were to be discovered at the end of the import, it would only take a few minutes to recreate the entire tournament from the individual backup disks.
18. Repeat the process for each station. Remember that importing a file into the pre-registered list will erase any names already in that list, so you must complete enrollment and resolve any issues for each station before you can import the next.

Issues:  

DCI Reporter saves the pre-registered data in the xxxxPREG.dat file in a comma delimited text format. It is not hard to remember that the data to import is in the "Pregnant" file. The 'xxxx' is the tournament ID that will be assigned by DCI Reporter to the tournament files.


The data entry people must understand the importance of correctly entering the data. They should be removed from where players may talk to them, and should not be responsible for resolving registration problems, poor handwriting, bad DCI numbers or any other difficulty. With due care, there should be a minimal amount of issues to resolve at the end of data entry.


**Test results and conclusions**: The procedure was tested and fine-tuned at a small tournament. The first attempt to move the data was done using a tab delimited file instead of a comma delimited file. The data would not import and DCI reporter gave no clue as to the reason. When the data was imported using the comma-delimited method, DCI reported indicated that the data was not terminated properly. Inspection of the data file revealed that extra columns of data had been written to the file. For example: "Redburn, Kendall,30002587,,,,,,," This is the reason for using the Delete function in the Edit menu in Excel, instead of the backspace key to remove extra columns as it eliminates the extra commas.


One player decided to drop out of the tournament before registration had completed. In the small tournament it was easy to locate that player and delete him from the pre-registration list. For large tournaments this would be disruptive. Instead consider deleting the player after all registration has been completed and imported.


The procedure is not really very complex, but it does require some attention and common sense. When data entering four hundred plus names and DCI numbers there are bound to be a few mistakes. The worst-case scenario would be to lose all of the data typed in at one station. To prevent that, enforce backing up and eliminate foot traffic around the data entry area. Nothing screws up a tournament more than people trying to talk to the people at the computers. If by some chance one of your data entry people enrolls all of their players instead of pre-registering them, don't panic. For that station the "xxxxDELT.dat" file will contain the enrollment information. Simply open that file instead of the "preg" file in the procedure and go from there.


Practice this procedure at least one time before putting it into operation. If you can, try it at a local tournament where the stakes aren't too high. That way you'll get the feel of trying to do something new and unfamiliar while everyone is standing around asking you questions.


This multiple entry process can be used for any single player Sealed or Constructed tournament (Team tournaments would need different set up instructions).







