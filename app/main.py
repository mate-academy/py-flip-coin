import random


def flip_coin() -> dict:
    flips = {coin: coin for coin in range(0, 11)}

    for coin in range(0, (10000 + 1)):
        flips[sum(random.choices([1, 0], k=10))] += 1

    for i in flips:
        flips[i] = flips[i] / 100

    return flips
