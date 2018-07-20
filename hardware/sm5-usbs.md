# SM5 USB support

Most of this content is "borrowed" from [the StepMania wiki](https://github.com/stepmania/stepmania/wiki) and mute's USB guide.

You may want to create static mount points for USB-based profiles. Doing so will allow you associate a USB port on your PC with a specific player's memorycard slot, as is common on arcade cabinets.

If you are using 5.1 b1 or newer, you will also be able to use custom songs from USB profiles.

---

# Find the USB port `by-path`

The disk names `sda`, `sdb`, etcetera, are not deterministic because they depend on the order in which devices are mounted, so we cannot use them to reliably identify players. Fortunately, Linux allows us to select a disk "by path," which amounts to selecting a drive by a specific USB _port_ (identifier), which is typically what we want for USB profiles.

To find the correct device path, plug a USB drive into the port you wish to associate with PLAYER_1, then run the following command:

```bash
ls -l /dev/disk/by-path
```

This should give you output that looks similar to the following:

```bash
/dev/disk/by-path/:
total 0
lrwxrwxrwx 1 root root  9 Jun  2 00:05 pci-0000:00:14.0-usb-0:10:1.0-scsi-0:0:0:0 -> ../../sdb
lrwxrwxrwx 1 root root 10 Jun  2 00:05 pci-0000:00:14.0-usb-0:10:1.0-scsi-0:0:0:0-part1 -> ../../sdb1
```

Copy this output somewhere, and repeat this process with the USB drive plugged into the port you wish to associate with PLAYER_2. Copy that output as well. You will use the directory names (i.e. the text starting with `pci`, and up to but not including the `->`) in Step 2.

# Create _fstab_ Entries

You will use part of the output from the previous step to create entries in `/etc/fstab`, the file which associates specific devices (in this case, a USB port `by-path`) with named mount points for each player, `/mnt/player1` and `/mnt/player2`, that StepMania can use. 

Open the `/etc/fstab` file in a text editor. Do *not* touch any existing text! Add the below entries at the end of the file. However, your entries will probably look slightly different than this, particularly the numbers after `pci-`. Use the `by-path` directory names you found previously.

```
/dev/disk/by-path/pci-0000:00:14.0-usb-0:10:1.0-scsi-0:0:0:0-part1 	/mnt/player1 auto rw,user,noauto,noatime 0 0
/dev/disk/by-path/pci-0000:00:14.0-usb-0:10:1.0-scsi-0:0:0:0 		/mnt/player1 auto rw,user,noauto,noatime 0 0
/dev/disk/by-path/pci-0000:00:14.0-usb-0:4:1.0-scsi-0:0:0:0-part1 	/mnt/player2 auto rw,user,noauto,noatime 0 0
/dev/disk/by-path/pci-0000:00:14.0-usb-0:4:1.0-scsi-0:0:0:0 		/mnt/player2 auto rw,user,noauto,noatime 0 0
```

Depending on your Linux distribution, you may need to create your named mount points elsewhere. Some distros use `/media/` for this purpose. You can also create an empty directory anywhere in the filesystem to use as a custom mount point.

# Create Mount Points

We need to make sure that the mount points we set above exist in the filesystem, and set their permissions so that StepMania can read and write to them.

Mount points are simply directories, so create them now:

```bash
sudo mkdir /mnt/player1
```

Set their permissions so that anyone (i.e. the non-`root` user that you use to run StepMania) can read and write to them:

```bash
sudo chmod 777 /mnt/player1
```

Repeat for PLAYER_2.

# Set StepMania Preferences

Update your `Preferences.ini` file to include the following values:

```ini
MemoryCardOsMountPointP1=/mnt/player1
MemoryCardOsMountPointP2=/mnt/player2
MemoryCardProfiles=1
MemoryCardUsbBusP1=-1
MemoryCardUsbBusP2=-1
MemoryCardUsbLevelP1=-1
MemoryCardUsbLevelP2=-1
MemoryCardUsbPortP1=-1
MemoryCardUsbPortP2=-1
MemoryCards=1
```

# Misc. Notes

* StepMania does not seem to allow 32 GB or larger drives.
* If you are using a dedicab, you may want to replace the front panel ports, as they use USB 1.1 and are thus intolerably slow.
* StepMania will automatically create an aptly-named directory in the root of your USB drive when you use it for the first time. In that directory there will be an `Editable.ini` file where you can set your display name and high score tag.
* You must plug in a USB drive before you advance past ScreenSelectProfile.


