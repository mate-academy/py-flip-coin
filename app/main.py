import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        head_coins = 0
        for i in range(10):
            head_coins += random.randint(0, 1)
        if head_coins in result:
            result[head_coins] += 1 / 100
        else:
            result[head_coins] = 1 / 100
    return result
