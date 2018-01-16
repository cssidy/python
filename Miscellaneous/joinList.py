#! python3
# This program takes a list value as an argument and returns a string with all the items separated by a comma and a
# space, with "and" inserted before the last item.


sampleList = ['apples', 'bananas', 'rainbows', 'tofu', 'lizards', 'moccasins']

def manipulate_list(mylist):
    mylist[-1] = 'and ' + mylist[-1]
    mylist = ', '.join(mylist)
    print(mylist)
    
manipulate_list(sampleList)
