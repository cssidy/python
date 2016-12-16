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