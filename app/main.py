import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for flip in range(10000):
        heads = sum(random.choice([0, 1]) for throw in range(10))
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / 10000) * 100

    return results
