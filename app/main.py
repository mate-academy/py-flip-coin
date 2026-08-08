import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for i in range(10000):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    for i in range(11):
        results[i] /= 100

    return results
