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
os.listdir(path)

os.path.exists('/cassidy/PycharmProjects')
os.path.isdir('/cassidy/PycharmProjects')
os.path.isfile('/cassidy/PycharmProjects')

# find if there is a DVD or flash drive on Windows:
os.path.exists('D:\\')

# find if there is a DVD or flash drive on Linux:
os.path.exists('/mnt')
