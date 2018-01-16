#! Python3

# Keeps track of not only how many coins were used, but which coins where used.


def dp_make_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j]+1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


def main():
    amnt = 63
    c_list = [1, 5, 10, 25]
    coins_used = [0]*(amnt+1)
    coin_count = [0]*(amnt+1)

    print("Making change for", amnt, "requires")
    print(dp_make_change(c_list, amnt, coin_count, coins_used),"coins")
    print("They are:")
    print_coins(coins_used, amnt)
    # print("The used list is as follows:")
    # print(coins_used)

main()
