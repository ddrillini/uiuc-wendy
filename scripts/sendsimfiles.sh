# for ben
# put this line in bashrc
# source /path/to/sendsimfiles.sh

# USAGE
# itgwifi: switch to machine's wifi network
# sendsimfiles: send files, should print when done
# rebootitg: reboot the machine to reload simfiles
# rewifi: go back to normal wifi
# also, "pitchbent" will load you into the folder so you can look around/delete stuff.

ITGMACHINEIP="2" # change this if the machine's not responding: it means that the IP address changed

alias itgwifi="networksetup -setairportnetwork en0 SC-00-TA-100 CutieMarkCrusaders\!Yay\!"
alias rewifi="networksetup -setairportpower airport off ; sleep 2 ; networksetup -setairportpower airport on"
alias rebootitg="ssh david@192.168.1.$ITGMACHINEIP -t 'sudo shutdown -r now'"
alias howdo="echo 'itgwifi, sendsimfiles, rebootitg, rewifi'"
alias pitchbent="ssh david@192.168.1.$ITGMACHINEIP -t 'cd /home/david/SM5-extra/ITG\ Songs/Notice\ Me\ BetaPack ; bash'"

# script: check if we're inside his song folder, and then copy the files over if we are.
sendsimfiles() {
        cd ~/Google\ Drive/Notice\ Me\ BetaPack
        currentdir=${PWD##*/}
        if [ "$currentdir" == "Notice Me BetaPack" ]; then
                rsync -vru --delete ./ david@192.168.1.$ITGMACHINEIP:"/home/david/SM5-extra/ITG\ Songs/Notice\ Me\ BetaPack" || failed
                echo "Simfiles successfully transferred."
        else
				failed
        fi
}

failed() {
	echo "something's wrong. contact ian or andrew."
	return 1
}

