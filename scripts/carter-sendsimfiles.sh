# put this line in bashrc
# source /path/to/sendsimfiles.sh

# USAGE
# sendsimfiles: send files, should print when done
# rebootitg: reboot the machine to reload simfiles
# rewifi: go back to normal wifi

ITGMACHINEIP="5" # change this if the machine's not responding: it means that the IP address changed

alias howdo="echo 'sendsimfiles, reloadsongs.'"

# script: check if we're inside his song folder, and then copy the files over if we are.
function sendsimfiles() {
        cd ~/charts/CarterTheQ
        currentdir=${PWD##*/}
        if [ "$currentdir" == "CarterTheQ" ]; then
				printf "\nMake sure you're on the right wifi network.\n"
                rsync -vru --delete ./ wendy@192.168.1.$ITGMACHINEIP:"/home/wendy/songs/CarterTheQ" || failed
                echo "Simfiles successfully transferred."
        else
				failed
        fi
}

function reloadsongs() {
	ssh wendy@192.168.1.$ITGMACHINEIP -t 'exec /home/wendy/util/reload-songs.sh'
}

function failed() {
	echo "something's wrong. does the folder exist? contact ian or andrew."
	return 1
}

