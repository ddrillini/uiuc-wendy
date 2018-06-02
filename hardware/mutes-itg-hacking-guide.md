# Mute's ITG Hacking Guide ~ UPDATED 2015-06-06

Originally posted [here](http://r21freak.com/phpbb3/viewtopic.php?f=38&t=19437).

This guide is to [hopefully] help anyone who's unclear about the process of adding custom songs and themes to an ITG dedicab. "Hacking" might sound like something that requires highly specific knowledge and lots of time and effort, but in regards to adding custom content to an ITG machine it certainly isn't. The hacking process involves starting up the ITG machine with a special version of Linux from a USB drive, which acts as the vehicle for you to access the machine's hard drive and add the custom content. From there, all you're really doing is copying/pasting the data folders from Stepmania to the ITG machine's hard drive and then ensuring that the game recognizes that extra content. This entire process shouldn't take more than 30 minutes or so, and subsequent "hacks" to add/change custom content should only take 10-15 minutes.

# What You Will Need

* Keyboard (PS2 or USB connection)
* USB drive (8+ GB ideal)
* SLAX Linux 6.1.2 †
* Universal USB Installer 1.5.3 †
* StepMania 3.95
* access to the machine's computer via removing the cabinet's back panel (and permission from the cabinet owner!)

† There are newer versions available, but I've had the best success with these versions.

# Step 1 - Preparing Linux

* Download SLAX & Universal USB Installer here: http://www.r21freak.com/mute/simfiles/ITG_SLAX.zip
* Install SLAX onto your USB drive using the Universal USB Installer program. (It's pretty self-explanatory and hard to mess up. Honest.)

# Step 2 - Preparing Simfiles

* Simfile audio must be in .ogg format.
* Simfile graphics must be in .png format.
* With all simile content properly formatted, cache your custom song content with StepMania 3.95. (StepMania caches all content each time it boots.)
* Copy your StepMania's "Cache" and "Songs" folders (and "Courses", if you're adding any) to your USB drive, putting them into another folder named "custom".

# Step 3 - Booting Linux on the Machine

3a) Does your machine show a "Roxor" screen when it is booting? Follow these steps:

* Plug your USB flash drive into the USB slot on the machine's computer.
* Plug your USB keyboard into the machine's P2 memory card slot (or PS2 keyboard into purple plug on machine's computer).
* Remove the security dongle from the machine's CPU, wait 30 seconds, plug the dongle back in. DO NOT REMOVE THE SECURITY DONGLE'S BATTERY.
* Turn the machine on.
* Enter the Boot Menu by hitting F11 at the "Roxor" screen. (Note: Timing this can be tricky. It may help to just keep rapidly hitting the F11 key as soon as you turn the machine on.)
* Select your USB flash drive from the list of mounted drives. SLAX will boot.
* When the SLAX boot screen shows up choose the second option, "Always Fresh Mode."

3b) Does your machine not show a "Roxor" screen when it is booting? Follow these steps:

* Plug your USB flash drive into the USB slot on the machine's computer.
* Plug your USB keyboard into the machine's P2 memory card slot (or PS2 keyboard into purple plug on machine's computer).
* Turn the machine on.
* At the BIOS loading screen (the one with the Energy Star logo), hit the Delete key. This takes you into the BIOS settings.
* Go down to the second menu option ("Advanced BIOS Settings"), enter it, and change the first boot priority to "USB-HDD".
* Hit F10 to save and exit the BIOS settings.
* When the SLAX boot screen shows up choose the second option, "Always Fresh Mode."

**When you reboot the machine after adding custom content, re-enter this menu and change the first boot priority back to "Hard Drive".**

# Step 4 - Adding Your Custom Songs

* Once SLAX has booted, navigate to your machine's `hda3` partition. (Also called `stats`.) Open up the `Static.ini` file you find there. (If there is none, just create a blank text document named `Static.ini`.) Add the following text to the file:
```
[Options]
AdditionalFolders=/itgdata/custom/
```
* Save and close the `Static.ini` file.
* Navigate to your machine's `hda5` partition. (Also called `itgdata`.) In here, copy your entire "custom" folder that contains your Songs and Cache folders. (This process may take a while, depending on how much stuff you're adding! The USB slots on the back of the machine are USB 2.0, which is why I recommend using them to make this step quicker.)
* If installing a custom theme, proceed to Step 5. If not, reboot the machine by opening up the Terminal in SLAX, entering the command "reboot", then hitting Enter. Once the machine has rebooted past the Roxor screen, it is safe to remove your USB drive.
* That's it! Your custom songs should all show up on the song select wheel.

# Step 5 - Adding A Custom Theme

5a. Are you adding Lara's "Simply Love vFINAL" or Mad Matt's updated Meat/Tactics/Gloomy themes? Follow these steps:

* In `hda5/custom`, create a folder called `Themes`.
* Copy your custom theme folder to `hda5/custom/Themes`.
* Navigate to your machine's `hda3` partition. Open up `Static.ini` and add the following text:

```
[Dance]
Theme=Simply Love (or other theme name)
```

* Save and close the `Static.ini` file.
* Reboot the machine as described in Step 4. ITG should start up with your new theme!

5b. Are you adding an older theme, such as Devon's Chromatic or Altitude? Follow these steps:

* In `hda5/custom`, create a folder called `Themes`.
* Copy your custom theme folder to `hda5/custom/Themes`.
* Ensure that your custom theme's `metrics.ini` file says the following:

```
[Global]
FallbackTheme=fallback

[Preferences-arcade]
Theme=arcade-custom
```

* In `hda5/custom/Themes`, create another folder called `arcade-custom`.
* Create a blank text document there and name it `metrics.ini`.
* Add the following text to the `metrics.ini` file (and change "THEME NAME" to the folder name of your theme, obviously):

```
[Global]
FallbackTheme=THEME NAME

[Common]
InitialScreen=@GetArcadeStartScreen()
```

* Save and close the `metrics.ini` file.
* Navigate to your machine's `hda3` partition. Open up Static.ini and add the following text:

```
[Dance]
Theme=arcade-custom
```

* Save and close the `Static.ini` file.
* Reboot the machine as described in Step 4. ITG should start up with your new theme!

**The second theme folder (`arcade-custom`) is a proxy theme. It is necessary for loading the machine's I/O drivers, which allow all the sensors and cabinet buttons to work. For certain themes (most notably the older Simply Love, Tactics, and Meatboy), you must name your proxy theme `arcade` instead of `arcade-custom`. Not exactly sure why this is, but I and many other people have found it to be the case.**


# Credits

This guide is based on the original ITG2AC hacking tutorial from boxorroxors.net, so credit is due to CMCM and whoever else originally compiled that. Special thanks to Rynker, The Cosmic Pope, and SteveReen for helping with certain aspects of this guide. 
