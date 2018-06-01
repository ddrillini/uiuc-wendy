# SM5 Setup
This guide assumes that you are assembling a new, dedicated computer for Stepmania, from scratch.

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
* Install `ssh` and `rsync`, and generate SSH keys as needed. This will make transferring files much easier.
* Install all of Stepmania's dependencies.
	* The list on the wiki given is out of date. TODO
* Install `alsamixer`.
* Install Stepmania. For ease, you should use the 5.0.12 binaries.
* Launch Stepmania once to generate all the initial save files.
* Find your sound device using `alsamixer` TODO.
* Set the script TODO to launch on login.
* In `Preferences.ini`:
	* `SoundDevice=hw:` followed by the device number you found earlier from `alsamixer`.
* Configure Stepmania to your heart's content.

Other useful scripts (particularly for dedicabs) are located TODO.

## PIUIO Setup
As of the time of this writing, compiling the PIUIO driver does not yet work on Ubuntu 18.04 LTS.

* Disable Secure Boot, unless you want to sign the kernel module.
* Clone the [`piuio`](https://github.com/djpohly/piuio) repository, which contains the driver code.
	* Compilation instructions are in the repo.
	* Installation instructions are [here](https://askubuntu.com/questions/299676)
* In `Preferences.ini`:
	* `LightsDriver=PIUIO_Leds`
	* `InputDebounceTime=0.050` if you want to match stock ITG 2.
* Update your input mappings as needed.

You should not need to use a positive `JudgeWindowAdd` value with this setup.

## `xorg.conf`
This is only necessary for ITG 2 dedicabs with original CRTs. Ubuntu will probably autodetect higher resolutions automatically.

TODO: `xorg.conf` modeline, but we haven't found out where it actually goes. Dan has the actual modeline but we need to test it.

Other TODO:
* [does VSync need to be on?](https://www.stepmania.com/forums/general-questions/show/536)
