#! Python3

# Memo-ized DP algorithm

memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    elif n < 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)
        memo[n] = f
    return f

fib(0)

