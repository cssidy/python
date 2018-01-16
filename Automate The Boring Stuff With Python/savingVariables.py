#! Python3

import shelve
import pprint


shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()

list(shelfFile.keys())
list(ShelfFile.values())
shelfFile.close

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()


import myCats

myCats.cats
# dictionary
myCats[0]
# Zophie, chubby
myCats[0]['name']
# Zophie