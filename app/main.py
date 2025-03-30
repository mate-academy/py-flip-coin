import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for i in range(10000):
        num_heads = 0
        for attemp in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1
    for i in range(11):
        results[i] = round(results[i] / 100, 2)
    return results
