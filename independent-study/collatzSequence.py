#! python3
# This program explores the Collatz Sequence. Enter any number, and you'll magically end at 1.


print('Enter any number:')


def collatzSequence(number):
    # ToDO: Input Validation
    # try:
    #     return number / 1
    # except ZeroDivisionError:
    #     print('Please enter an integer.')

    while number != 1:
        if number % 2 == 0:
            print(number / 2)
            number /= 2
        elif number % 2 == 1:
            print(3 * number + 1)
            number = 3 * number + 1
        else:
            break


collatzSequence(int(input()))
