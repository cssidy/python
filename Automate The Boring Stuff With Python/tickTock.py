#! python3

import time


def clock_sound(seconds):
    for i in range(seconds):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)

clock_sound(100)        