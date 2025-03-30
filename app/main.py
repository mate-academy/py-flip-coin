import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                heads_count += 1
        results[heads_count] += 1
    for key, value in results.items():
        results[key] = (value / 10000) * 100
    return results
