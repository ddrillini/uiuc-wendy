# SM5 Setup
This guide assumes that you are assembling everything from scratch.

## Hardware
The bare minimum is the [hardware requirements](https://help.ubuntu.com/community/Installation/SystemRequirements) for Ubuntu 16.04 LTS x64.

You should use the following for a pleasant experience:

* GPU: for dedicabs, any _discrete_ GPU made after 2010 will suffice. Higher resolutions will require a better GPU; Dan reports using a GTX 960 for 2560x1440 at 144 fps.
* Storage: 120 GB on a decent SSD
* Networking: Gigabit Ethernet

## Basic Setup

* Install Ubuntu 16.04 LTS. (Driver support isn't there yet for 18.04 LTS.)
* Install `ssh` and `rsync`, and generate SSH keys as needed. This will make transferring files much easier.
* Install all of Stepmania's dependencies.
	* The list on the wiki given is out of date. TODO
* Install `alsamixer`.
* Download, compile, or otherwise obtain a Stepmania binary.
* Configure Stepmania to your heart's content. If you're an ITG purist, you'll probably want Simply Love.

## Cabinet-Specific Setup
You should complete as many of the steps here as practical _before_ moving the computer into the cabinet, because cabinets do not have good default keyboard or mouse placement options. Also, if your cabinet has the original CRT, using Ubuntu's GUI on the 640x480 screen will be frustrating.

* If using the PIUIO, compile, install, and load the [`piuio`](https://github.com/djpohly/piuio) driver.
	* This won't work on 18.04 LTS.
	* Disable Secure Boot unless you want to figure out how to sign kernel modules.
	* Compilation instructions are in the repo.
	* Installation instructions [here](https://askubuntu.com/questions/299676)
* Set the monitor resolution correctly.
	* TODO `xorg.conf` witch magic!
* Setup pad lights (PIUIO instructions only) TODO
* Set Stepmania to run on boot: TODO

## Stepmania Configuration
Unfortunately, a lot of the settings necessary to run Stepmania properly are poorly documented.

TODO. we're figuring this out as we go!

[why does VSync need to be on?](https://www.stepmania.com/forums/general-questions/show/536)
