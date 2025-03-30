import random


def flip_coin() -> dict:
    results = {}
    for _ in range(11000):
        head_count = sum(random.choice([0, 1]) for _ in range(10))
        results[head_count] = results.get(head_count, 0) + 1

    for result in results:
        results[result] = (results[result] / 11000) * 100

    return results
