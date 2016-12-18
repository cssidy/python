#! Python


def collatz_sequence(number):
    memo = {}
    while number != 1:
        if number % 2 == 0:
            print(number / 2)
            number /= 2
            memo[x] = number
        elif number % 2 == 1:
            print(3 * number + 1)
            number = 3 * number + 1
            memo[x] = number
        else:
            break
    print(memo)
collatz_sequence(1000000)