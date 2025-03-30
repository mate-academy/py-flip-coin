import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads += 1
        result[heads] += 1
    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result
