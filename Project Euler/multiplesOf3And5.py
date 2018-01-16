#! Python3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


# Using a function

def divisibility_test(inte):
    sumOfinte = 0
    for i in range(inte):
        if i % 3 == 0:
            print(i)
            sumOfinte = sumOfinte + i
        elif i % 5 == 0:
            print(i)
            sumOfinte = sumOfinte + i
    print(sumOfinte)

divisibility_test(1000)

# Using a While loop

i = 0
sumOfi = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        sumOfi = sumOfi + i
    i += 1

print(sumOfi)
