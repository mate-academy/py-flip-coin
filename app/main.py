import random


def flip_coin() -> int:
    results = {}
    for i in range(10000):
        heads = 0
        for flip in range(10):
            if random.random() < 0.5:
                heads += 1
        if heads in results:
            results[heads] += 1
        else:
            results[heads] = 1
    for key, value in results.items():
        results[key] = value / 100
    return results
