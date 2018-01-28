#! python3

import datetime
import time

halloween2018 = datetime.datetime(2018, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2018:
    time.sleep(1)

