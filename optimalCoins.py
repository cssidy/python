#! Python3

# Very inefficient, answer is 6
# takes 67,716,925 recursive calls


def recmc(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + recmc(coin_value_list, change-i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(recmc([1, 5, 10, 25], 63))

