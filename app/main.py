import random


def flip_coin() -> dict:
    heads = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice([True, False]):
                count += 1
        if count not in heads:
            heads[count] = 0
        heads[count] += 1
    result = {key: round(value / 100, 2) for key, value in heads.items()}
    return result
