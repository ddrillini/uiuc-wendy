# set these in .bashrc
# export folder=""
# export localpath=""

alias howdo="echo 'sendsimfiles, reloadsongs.'"
ITGMACHINEIP="5" # change this if the machine's not responding: it means that the IP address changed

# script: check if we're inside his song folder, and then copy the files over if we are.
function sendsimfiles() {

	if [ -z "$folder" ] # if $folder is not set
	then
		printf "\nPlease export \$folder in .bashrc.\n\n"
		return 1
	fi

	printf "\nMake sure you're on the right wifi network.\n\n"

	cd $localpath
	# verify we're inside their song folder.
	currentdir=${PWD##*/}
	if [ "$currentdir" == "$folder" ]; then
		rsync -vru --delete ./ wendy@192.168.1.$ITGMACHINEIP:"/home/wendy/songs/$folder" || return 1
	else
		printf "\nYour folder doesn't exist or isn't in the right place.\n"
		return 1
	fi

	printf "\nSimfiles successfully transferred.\n"
}

function reloadsongs() {
	ssh wendy@192.168.1.$ITGMACHINEIP -t 'exec /home/wendy/util/reload-songs.sh'
}

