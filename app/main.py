import random


def flip_coin() -> None:
    results = {}
    flips = 10000
    for i in range(11):
        results[i] = 0
    for i in range(flips):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1
    for key in results:
        results[key] = round((results[key] / flips) * 100, 2)
    return results
