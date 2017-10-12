
#! Python3
# Takes a list of strings and displays it in a well-organized table with each column right-justified.


table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):

    # TODO: find the longest string in each list
    # TODO: store the longest string as a list of integers
    col_widths = [0] * len(table_data)

    i = max(data[0], key=len)
    col_widths[0] = len(i)

    i = max(data[1], key=len)
    col_widths[1] = len(i)

    i = max(data[2], key=len)
    col_widths[2] = len(i)

    # TODO: find the largest value in the above ^ list of integers and pass it to the rjust() function
    i = max(col_widths)

    # TODO: print table
    # for x in range(len(data)):
    #     for y in data[x]:
    #         print(y.rjust(i))

    for x, y, z in zip(table_data[0], table_data[1], table_data[2]):
        print(x.rjust(i), y.rjust(i), z.rjust(i))

print_table(table_data)
