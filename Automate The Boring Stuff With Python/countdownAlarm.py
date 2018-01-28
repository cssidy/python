#! /usr/bin/python3

import time
import subprocess

timeleft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# at the end of the countdown play a sound file
subprocess.Popen(['start', 'alarm.wav'], shell=True)