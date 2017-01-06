#! Python3

# The key to cutting down on the amount of work we do is to remember some of the past results so we
# can avoid recomputing results we already know.

# Much faster
# 'memoization' or 'caching'


def recdc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + recdc(coin_value_list, change-i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins

print(recdc([1, 5, 10, 25], 63, [0]*64))
