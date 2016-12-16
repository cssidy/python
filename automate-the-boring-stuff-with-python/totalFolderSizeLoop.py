#! Python3

import os


totalSize = 0
for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path))
print(totalSize)
# 36864