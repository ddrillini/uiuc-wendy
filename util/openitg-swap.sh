#!/bin/bash
pkill stepmania
sleep 10
export DISPLAY=:0.0
sleep 1
~/openitg/openitg  2>/dev/null &
disown
