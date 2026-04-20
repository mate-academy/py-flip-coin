import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = sum([1 for _ in range(10) if random.random() < 0.5])
        results[heads] += 1
    for heads in results:
        results[heads] = round(results[heads] / 10000 * 100, 2)
    return results
