from random import randint


def flip_coin() -> dict:
    coins = dict()

    for _ in range(10000):
        coin = 0

        for _ in range(10):
            if randint(0, 1):
                coin += 1
        if coin not in coins:
            coins[coin] = 1
        else:
            coins[coin] += 1

    for key, value in coins.items():
        coins[key] = round(value / 100, 2)

    return coins
