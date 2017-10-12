#! python3

# This program is based on a technical skills test that I had to take for a job application. The program asks the user
# to enter any number, then converts that number to its binary equivalent, inverts that new number (010 becomes 101),
# then converts that new number back to decimal and prints the results.


print('Enter a number:')


def conversion(number):

    # convert number to binary
    binary_number = str(bin(number)[2:])
    binary_number = list(binary_number)
    for i in range(len(binary_number)):
        if binary_number[i] == '1':
            binary_number[i] = '0'
        elif binary_number[i] == '0':
            binary_number[i] = '1'
        else:
            break
    binary_number = ''.join(binary_number)
    new_number = (int(binary_number, 2))
    print('Your original input ', number, ' was converted to binary, ', binary_number, ', inverted, then converted back'
          ' to decimal. The new number is ', new_number, '.')

conversion(int(input()))
