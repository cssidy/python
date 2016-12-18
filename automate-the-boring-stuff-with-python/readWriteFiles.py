#! Python3


# call open() function to return a file object
# call read() or write() on the file object
# call close() on a file object to close it

helloFile = open(path + '/automate-the-boring-stuff-with-python/hello.txt')
helloContent = helloFile.read()
print(helloFile, helloContent)

sonnetFile = open(path + '/automate-the-boring-stuff-with-python/sonnet29.txt')
print(sonnetFile.readlines())

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
# 13

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
# 25

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
print(content)
# Hello world!
# Bacon is not a vegetable.
