#! Python3


# call open() function to return a file object
# call read() or write() on the file object
# call close() on a file object to close it

helloFile = open(path + '/automate-the-boring-stuff-with-python/hello.txt')
helloContent = helloFile.read()
print(helloFile, helloContent)

sonnetFile = open(path + '/automate-the-boring-stuff-with-python/sonnet29.txt')
print(sonnetFile.readlines())

