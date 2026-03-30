import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                count_heads += 1
        results[count_heads] += 1
    for key in results:
        results[key] = round(results[key] / 100, 2)
    return results
