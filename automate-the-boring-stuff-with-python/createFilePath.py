#! Python3

import os

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('/Users/cassidy', filename))

print(os.getcwd())
os.chdir('/home/cassidy/Documents')
print(os.getcwd())

# os.makedirs('/delicious/walnut/waffles')

print(os.path.abspath('.'))

path = os.getcwd()
print(os.path.basename(path))
print(os.path.dirname(path))

calcFilePath = 'Windows/System32/calc.exe'
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.path.sep),
      ('/usr/bin'.split(os.path.sep)),
      )

os.path.getsize(path)
os.path.listdir(path)


totalSize = 0
for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path))
print(totalSize)
# 36864
