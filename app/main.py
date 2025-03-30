import random


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return dict(sorted(results.items()))
