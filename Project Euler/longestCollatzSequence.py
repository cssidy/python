#! Python

memo = {}


def collatz_sequence(number):
    if n not in memo:

    while number != 1:
        if number % 2 == 0:
            number /= 2
            return memo[number]
        elif number % 2 == 1:
            number = 3 * number + 1
            return memo[number]
        else:
            break

collatz_sequence(100)
print(memo)