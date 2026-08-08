import random


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] = results.get(heads_count, 0) + 1

    for key in results:
        results[key] = (results[key] / 10000) * 100

    return results
