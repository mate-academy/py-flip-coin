import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            coin_side = random.randint(0, 1)
            if coin_side == 1:
                count += 1
        result[count] += 1
    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result
