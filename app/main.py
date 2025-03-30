import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice([0, 1]):
                heads += 1
        result[heads] += 1
    return {k: v / 100 for k, v in result.items()}
