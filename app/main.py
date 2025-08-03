import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            count_heads += random.choice([0, 1])
        results[count_heads] += 1
    for key in results:
        results[key] = results[key] / 10000 * 100
    return results
