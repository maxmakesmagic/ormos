
---
[Link to Wayback Machine](https://web.archive.org/web/20160301033045/http://magic.wizards.com/en/articles/archive/barcode-scanning-dci-reporter-2002-04-25)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Catherine Nicoloff Granted, we don't normally manage gigantic events here in Scandinavia, so my fiddling around with the barcode scanning abilities in DCI Reporter was more of a diversion than anything of practical value. Rune (Horvik) is a popular and quite-busy Tournament Organizer in this sector, so as his wife it is my solemn duty to learn the complete ins and outs of DCI Reporter so he can get on with the business of judging. It also helps when he's away, because I can run and manage his weekly events on my own if he can't find anyone else more willing."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "938616"
[_metadata_:publish_date]:- "2002-04-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Barcode Scanning in DCI Reporter"
[_metadata_:wayback_capture_timestamp]:- "2016-03-01 03:30:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160301033045id_/http://magic.wizards.com/en/articles/archive/barcode-scanning-dci-reporter-2002-04-25"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/barcode-scanning-dci-reporter-2002-04-25"
---


Barcode Scanning in DCI Reporter
================================



 Posted in [ARTICLES](/en/articles)
 on April 25, 2002 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











*Catherine Nicoloff*


Granted, we don't normally manage gigantic events here in Scandinavia, so my fiddling around with the barcode scanning abilities in DCI Reporter was more of a diversion than anything of practical value. Rune (Horvik) is a popular and quite-busy Tournament Organizer in this sector, so as his wife it is my solemn duty to learn the complete ins and outs of DCI Reporter so he can get on with the business of judging. It also helps when he's away, because I can run and manage his weekly events on my own if he can't find anyone else more willing.


All that aside, I am pleased to report that barcode scanning does work pretty much as expected in DCI Reporter. To get it running, however, takes a small bit of extra preparation that probably not everyone knows about, so this document is a short essay on what you need to do prior to the event to have a successful barcode-scanning experience.


### STEP 1: GET THE FONT


If you want to print barcodes, you'll need a barcode font. Barcode fonts are apparently a huge industry online. Putting the words "barcode font" into the Google search engine led to a lot of dead ends (and overpriced WebPages) before I finally found what I was looking for.


There are many different types of barcode fonts in the world, and not all of them are suitable for use with DCI Reporter. What you need is called a "3 of 9" font or a "Code 39" font. This is a very simple font that is just numbers and possibly letters.


As quoted from [elsewhere on the net](http://www.idautomation.com/code39faq.html): "Code 39 is commonly used for various bar-coding labels such as name badges, inventory and industrial applications. The Code 39 barcode is the easiest to use of alpha-numeric barcodes and is designed for character self-checking, eliminating the requirement for check character calculations. The 3 of 9 Code and Code 3 of 9 are just other names for the same symbology."


Translated: Code 39 barcodes don't need special programs to generate them, unlike other types of barcodes like UPC. It makes sense that DCI Reporter would choose this type of barcode for its uses.


I didn't download the free font offered on the IDautomation site, as it wasn't a complete Code 39 font (I guess to encourage you to buy their overpriced commercial fonts). Instead, I downloaded the font located at: serv.net/~bobz/zips/z3of9.zip (which is freeware and complete).


Download a font of your choice and put it in a directory you can find later. Unzip it if it's zipped. (Windows XP can do this automatically, others will need WinZip from [http://www.winzip.com](http://www.winzip.com/)).


### STEP 2: INSTALL THE FONT


Since DCI Reporter appears to run only on Windows machines, this step is easy. Load up your Fonts folder (Start->Settings->Control Panel->Fonts in Windows 95/98/ME; Start->Control Panel->Fonts in Windows XP) and choose "Install New Font" from the File Menu.


This brings up a dialog box with a file folder tree at the bottom. Find the folder you downloaded the font to and choose it. Make sure "Copy fonts to Fonts folder" is checked. Select the font you wish to install (Z: 3 of 9 bar-code) and click OK. The font should now be installed on your system.


### STEP 3: OBTAIN A BARCODE SCANNER


There are many types of barcode scanners, such as little hand-held pens and laser scanners and even scanners that use tiny cameras and image-processors to decode the barcodes. For my experiment I used a pen-type scanner. Pen scanners are usually the cheapest (around $100 US) and (some say) most robust because they don't rely on delicate internal mirrors. For instance, those little CueCat scanners they handed out for a while at Radio Shack are pen-type scanners using a little red light source and a photo diode in the tip.


For the purposes of DCI Reporter, it is probably best to get a barcode scanner that uses your computer's keyboard port. These scanners plug directly into the PS/2 keyboard port on the back of your computer and include a passthrough cable that lets you plug your keyboard in as well. These scanners also simply send the decoded barcode data to your computer as if they were typed on the keyboard, which is the form of data entry that DCI Reporter accepts. They require no special software drivers to use, so they will work on any machine. My instructions cover only this type of scanner.


### STEP 4: CONNECT YOUR BARCODE SCANNER


This is split into two sections: for desktops and laptops. Laptops come with a lot of special instructions regarding the use of barcode scanners. Read them carefully or you may have a lot of problems later on.


**DESKTOP PC USERS:**


Nothing could be easier. Turn computer off. Disconnect the keyboard. Connect the scanner to the keyboard port on the back of your computer. Reconnect your keyboard through the passthrough cable on the scanner. Turn computer back on.


**LAPTOP PC USERS:**


Laptops only come with a single PS/2 port on the back, to plug either an external mouse or external keyboard into. This causes some difficulty.


Most laptops do not activate the external keyboard port unless there is a genuine keyboard attached to it. This is an important thing to remember, because plugging in your barcode scanner to your laptop mouse port and then trying to plug the mouse into the barcode scanner will most likely result in a working mouse and a non-working barcode scanner. This is because the laptop does not expect to receive keyboard data from that port, since no keyboard is attached!


1. Laptop configurations requiring just a barcode scanner...


If you don't need to use an external mouse (say your laptop comes with a decent built-in mouse that you're used to), you can just plug the barcode scanner directly into the external keyboard port and then plug a regular PC keyboard into the scanner's passthrough cable.


2. Laptop configurations requiring both a mouse and a barcode scanner...


My solution to this problem was to buy a y-cable for the PS/2 port. These are cables (around $5 US) that split the PS/2 port into two ports: one labeled for the mouse and one labeled for the keyboard. Plug the mouse into the mouse end of the "Y". Plug the barcode scanner into the keyboard end of the "Y". Then plug an external keyboard into the barcode scanner's passthrough cable. (See harbourtownsales.site.yahoo.net/ps2keyysplit.html for an example of a y-cable.)


In both cases, you're stuck with an external keyboard hanging around. Some organizers might like using a normal-sized PC keyboard on the tournament computer. Others, like me, just sort of stuck the external keyboard somewhere out of the way and used the one built into the laptop. Take note, however: some laptops may disable the internal keyboard if an external keyboard is attached.


There are ways to get around the requirement for a bulky external keyboard, but they depend largely on your laptop and your budget. Some laptops have settings in their BIOS by which you can force the laptop to turn on the external keyboard port even if there isn't a keyboard plugged in. If your laptop can do this, you can just plug the barcode scanner in directly and use it. You might also be able to plug the mouse in through the scanner, and maybe they will both work. I'm not sure.


Some scanners offer the option of plugging in via the USB port or even the serial port, eliminating the keyboard hassle entirely. Note that some laptops do not come with a serial port (Rune's Toshiba didn't, for example) and Windows 95 often cannot properly handle USB.


You can also purchase a keyboard terminator ($50 US or so) that emulates the presence of an attached keyboard but takes up far less space. (See pcconnection.com/scripts/productdetail.asp?product\_id=283675 for an example.)


All said, this is not exactly a cheap method of tournament results entry. It is, however, an extremely fast and accurate one.


### STEP 5: USING THIS ALL WITH DCI REPORTER


This is where everything gets fun! Not only can you use your barcode scanner for results entry, but the DCI cards sent out by the Player Rewards program have the player's DCI number encoded in a readable barcode on the back. This is a minimal added benefit, though, since most players in our local area can't even be bothered to remember their own DCI number, much less carry their card with them. Rune's spoiled them by memorizing all their numbers for them.


**PRINTING RESULTS ENTRY SLIPS:**


Getting barcodes onto the results entry slips in DCI Reporter is quite easy. We made sure the following checkboxes were checked: "For Cut Machine", "Judge Signature Required", "Bar Code". In the box under the "Bar Code" checkbox is where your chosen barcode font should be shown. If none is shown, scroll down the list of fonts to the right until you find your barcode font, then double-click it.


Now all results slips will print with barcodes for the most common results. (Intentional draws and other draws will still have to be entered by hand.)


Be careful! Make sure your printer is set to the proper paper size and that your paper margins are small/nonexistent. Otherwise DCI Reporter can get confused and start cutting off the bottom barcode on every page, which is quite annoying.


**SCANNING RESULTS ENTRY SLIPS:**


The results entry slips will have six barcodes on them: four barcodes corresponding to match results (2-0, 2-1, 1-2, 0-2) and two barcodes corresponding to drops (Player 1, Player 2).


To scan these into DCI Reporter, make sure you have the Results Entry screen open, that the "Use Scanner" box is checked, and that the active input field is the "Table" field.


Always scan the match result first, BEFORE SCANNING ANY DROPS. Otherwise Bad Things(tm) might happen. It might take a few tries if you're using a pen-type scanner to get the feel of the scanning motion and speed. You can scan the barcode from right to left or left to right, whichever is most comfortable.


Some barcode scanners will append a final <ENTER> to the barcode sequence. Others require that you do this yourself. (All drops will require a confirmation regardless.) Naturally, scanners that hit <ENTER> themselves after a scan are faster and more efficient in DCI Reporter than those that will require you to hit it yourself.


Take heed: if you click on a table or enter a match result by hand, the "Use Scanner" checkbox will clear itself. You must re-activate it before continuing to scan.


### FINAL THOUGHTS:


I was the scorekeeper for Norwegian Nationals this year, and it was my first test of the barcode scanning abilities in DCI Reporter. My initial impressions are quite positive. (Rune liked it so much he will be bringing our setup with him to Russian and Finnish Nationals.) I was running not only Nationals, but a large Open tournament and four side-events concurrently and I was able to do this without a single results entry error. Moreover, I was able to enter all the results from a round in an extremely short period of time.


(Drops are another matter. Murphy's Law of Magic is that players will always wait until you've paired the next round to come tell you they meant to drop but forgot to check the box on the slip. You always get a few of those.)


The scanning was very robust and accurate, even in the cases where players had marked or otherwise written a bit on the barcodes. The barcodes themselves printed very cleanly. (We were using a laser printer. I'm not sure how the use of an inkjet or bubblejet printer might distort the barcodes.)


### SOME THINGS TO WATCH OUT FOR:


If you're running multiple events, be careful not to scan the wrong results into the wrong copy of DCI Reporter! We made this impossible by having different table numbers for the events. (Main event started with table 1, Open event started with table 60, etc.) This way, even if I did get briefly confused and scan into the wrong DCI Reporter window, it wouldn't accept it because it wasn't a legal table number.


Also, be aware that some players may circle the wrong barcode out of confusion. Always always always check the written results on the slip, and then scan the correct barcode. If possible, educate the players not to circle barcodes at all, and instead let a judge do it. Remind them to circle the "Drop" barcode (or tell the judge when they collect the slip) if they wish to drop, and be sure to check each slip carefully so you don't miss any drops. The "Drop" barcodes are in a strange and cluttered position and are easily overlooked.


Bring extra toner for your printer! The barcodes easily double the amount of toner/ink your printer will use on the results slips. It pays to be prepared, because nothing ruins your day like the prospect of shouting out 200 pairings.


That's about all I can think of to say on this topic, so good luck and happy scanning!







