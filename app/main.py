import random


def flip_coin():
    coin = [True, False]
    results = {}
    for i in range(11):
        count = sum(
            1 for _ in range(10000)
            if sum(1 for _ in range(10) if random.choice(coin)) == i
        )
        results[i] = count / 100
    return results
