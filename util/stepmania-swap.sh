#!/bin/bash
pkill openitg
sleep 5
export DISPLAY=:0.0
~/stepmania-5.1/stepmania 1>/dev/null 2>/dev/null &
disown
