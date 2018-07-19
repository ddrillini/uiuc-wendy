#!/bin/bash

# used to tell GTK which display to go to
# since cli has no notion of graphics display?
export DISPLAY=:0.0

# needed to ensure that audio drivers are completely loaded
sleep 15

/home/wendy/stepmania-5.1/stepmania
