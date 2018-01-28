#! python3

import time
import threading

print('Start of program.')


def take_a_nap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=take_a_nap)
threadObj.start()

print('End of program.')