#!/bin/bash

# ssh in (in .zshrc)

# execute this script:
export DISPLAY=:0.0
sleep 1
xdotool key "Scroll_Lock"
sleep 2
xdotool key "Delete"
sleep .2
xdotool key "Delete"
sleep .2
xdotool key "Return"

