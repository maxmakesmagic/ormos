---
id: g2tnxnyp
kind: article
lang: en
path: /en/articles/feature/2015/12-08-dci-reporter-beyond-the-basics
title: 'DCI Reporter: Beyond the Basics'
published: '2015-12-08'
column_slug: feature
column: Feature
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    lang_detected: en
    capture_id: 295297
    url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    captured_at: '2022-07-01 23:36:30+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    lang_detected: en
    capture_id: 295297
    url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    captured_at: '2022-07-01 23:36:30+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    lang_detected: en
    capture_id: 295297
    url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    captured_at: '2022-07-01 23:36:30+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    lang_detected: en
    capture_id: 295297
    url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
    captured_at: '2022-07-01 23:36:30+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: g2tnxnyp
  url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
  page_key: magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
  lang: en
  template: drupal
  captured_at: '2022-07-01 23:36:30+00'
  capture_id: 295297
  wayback_url: https://web.archive.org/web/20220701233630id_/https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: g2tnxnyp
  capture_id: 295297
  url: https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
  wayback_url: https://web.archive.org/web/20220701233630id_/https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2002-02-20
  captured_at: '2022-07-01 23:36:30+00'
  template: drupal
  sha256: bd45702efe2f9bf44d63d80686e3dbb50b16c95b4e61680821e58d7111bb1532
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:MadMage682@aol.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - MadMage682@aol.com
  occurrences: 1
---
### DCI Tools (v2.7)

*Matt Villamaino*

The most recent Tournament Organizer CD sent out to all judges (November 2001) contains a new software program called DCI Tools to help run tournaments. Used at its most basic function, it is possible to look up a players DCI # by entering their last name and clicking on the **Search** button. There is more that can be done with DCI Tools however than just this. DCI Tools can be used to enter all the names of players in a tournament, including amateur status and awarded byes then export this to a tab delimited file to import into DCI Reporter.

When you launch DCI Tools the following screen appears.

![](http://archive.wizards.com/dci/judge/images/tools_ma.jpg)

If you simply want to look up a player's DCI number, click on the Player Information button.

![](http://archive.wizards.com/dci/judge/images/search.jpg)

Type in the player's last name, then the Continue button (the enter button does not work). DCI Tools will now show a list of all players with that last name sorted by first name. The player's zip code (if available) will also be displayed. Most players will also be listed twice in the database. The reason for this is DCI Tools currently stores two DCI numbers for each player: their original number and the number converted to its eight digit version. If the player is listed more than twice, they have multiple DCI numbers and should contact the DCI to have them combined if they haven't already. You may also look to see at the zip codes listed depending on how common a particular name is (for example: Jim Smith).

Using DCI Tools to enter players into a tournament is fairly straight forward. First click on the Start a New Tournament Button. Only one tournament can be entered at once with DCI Tools, so anything already entered will be lost. Type in the tournament name and the maximum number of players.

Click on the Start Registrations button to begin entering players.

![](http://archive.wizards.com/dci/judge/images/player_e.jpg)

The easiest way to register players is to click on the Search Player button. Type in the player's DCI number then click continue. Assuming that the player is in the database, that players information will now appear in the player entry window. If the player is not in the database then the name will have to be entered manually (the DCI number searched for should be in the appropriate box). Click the registration complete button and the player is entered. DCI Tools will automatically return you to the Search Player window to continue registrations.

After you have entered all the players names you will need to export them to a tab delimited file. Simply click on Export for the DCI Reporter button.

![](http://archive.wizards.com/dci/judge/images/export.jpg)

To make things easier just click on option one, though it may have information you don't need, it will make things easier later. Save the file to a place you will be able to find it.

Next the DCI Reporter tournament will need to be created. It is important that the Use Pro Function box is selected in the initial setup window or DCI Reporter will not be able to import the file.

Once you open the tournament go to edit => Import preregistered players from file.

![](http://archive.wizards.com/dci/judge/images/import.jpg)

Click on both the Pro Flag included and Awarded Byes included checkboxes, then select the file. DCI Reporter will tell you if there is a problem importing anything, however it will not tell you where the error is. Should there be an error you will have to refer back to the list of registered players in DCI Tools, compare the lists and manually correct the problem in DCI Reporter.

Next go to the Player Data window, select all the preregistered players and click Enroll All (or enroll each separately). You are now ready to run your tournament as normal.

As always practice this before using it in a tournament.

### Duplicate Names

There are times that some players in the tournament have the same name (either just the last name or the exact same name) DCI Tools has a feature that will automatically alert the scorekeeper when he or she enters a related name.

![](http://archive.wizards.com/dci/judge/images/names.jpg)

In this example player Robert Dougherty has already been entered. After searching for player Alen Dougherty in the Search Player window his information appears in the player entry window. Looking at the Name-Related Players field on the right side of the screen it shows Robert Dougherty as a name-related player. If two players have the same first and last name call them both up, notify them of the situation and put their middle initial in the first name field to avoid mixing up the pairings.

Questions or suggestions for further columns on DCI Reporter should be sent to me at MadMage682@aol.com.

-Matt