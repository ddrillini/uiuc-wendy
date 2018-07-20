# SM5 Setup
This guide assumes that you are assembling a new, dedicated computer, exclusively for Stepmania, from scratch.

This guide assumes that you know how to add your preferred songs, themes, noteskins, etcetera to Stepmania.

## Hardware
The bare minimum is the [hardware requirements](https://help.ubuntu.com/community/Installation/SystemRequirements) for Ubuntu 16.04 LTS x64.

You should use the following for a pleasant experience:

* GPU: for original cabinet CRTs, any _discrete_ GPU made after 2010 will suffice. Higher resolutions will require a better GPU; Dan reports using a GTX 960 for 2560x1440 at 144 fps.
* Storage: 120 GB on a decent SSD
* Networking: Gigabit Ethernet

## Basic Setup
If you are setting up a cabinet, you should complete as many of the steps here as practical _before_ moving the computer into the cabinet, because cabinets do not have good default keyboard or mouse placement options. Also, if your cabinet has the original CRT, using Ubuntu's GUI on the 640x480 screen will be frustrating.

* Install Ubuntu 16.04 LTS.
* Run the `install.sh` script, which automatically installs necessary dependencies for Stepmania.
* Generate host SSH keys.
* Install Stepmania.
	* Use 5.1 b1 if you need any of the below features. You will need to compile from source TODO instructions, but the installation script should have installed all the necessary dependencies. Themes that support 5.0.12 should run on 5.1 b1 without modification.
		* Custom songs from USB profiles
		* (Some) NotITG modifier support
	* Otherwise, use 5.0.12, as Linux binaries are readily available.
	* 5.2 (what was formerly 5.1 before a change in scope; see 5.1 release notes) is not currently recommended due to lack of themer support.
* Launch and close Stepmania once to generate all the initial save files.
* Run the command `aplay -l` to [find your sound device number](https://askubuntu.com/questions/22031/what-are-my-audio-devices).
* Set the `boot.sh` script to launch on login. Change the last line to execute Stepmania from its installation location on your setup.
* In `Preferences.ini`:
	* `SoundDevice=hw:` followed by the device number you found earlier  
	This prevents microstuttering.
	* `QuirksMode=1`  
	This enables compatibility with some OpenITG/SM3.95-compatible files. You will need to rebuild the cache for changes to this setting to take effect.
* Configure Stepmania to your heart's content.

## PIUIO Setup
As of the time of this writing, compiling the PIUIO driver does not yet work on Ubuntu 18.04 LTS.

* Disable Secure Boot, unless you want to sign the kernel module.
* Clone the [`piuio`](https://github.com/djpohly/piuio) repository, which contains the driver code.
	* Compilation instructions are in the repo.
	* Installation instructions are [here](https://askubuntu.com/questions/299676)
* In `Preferences.ini`:
	* `LightsDriver=PIUIO_Leds`
	* `InputDebounceTime=0.050` \[seconds]  
	This recommendation matches stock ITG 2.
* Fix the polling rate TODO.
* Update your input mappings. Don't forget the coin door and service buttons!

You [should not use](http://aaronin.jp/boards/viewtopic.php?t=9459) a positive `JudgeWindowAdd` value with this setup.

## `xorg.conf`
This is only necessary for ITG 2 dedicabs with original CRTs. Ubuntu will probably autodetect higher resolutions automatically.

TODO: `xorg.conf` modeline, but we haven't found out where it actually goes. Dan has the actual modeline but we need to test it.

Other TODO:
* [does VSync need to be on?](https://www.stepmania.com/forums/general-questions/show/536)
