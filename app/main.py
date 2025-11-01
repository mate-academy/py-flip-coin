# write your code here
import random


def flip_coin() -> dict:
    coins = {}

    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.randint(0, 1):
                count += 1
        coins[count] = coins.get(count, 0) + 1
    coins_sorted = dict(sorted(coins.items()))
    return {key: round(value / 10000 * 100, 2)
            for key, value in coins_sorted.items()}
