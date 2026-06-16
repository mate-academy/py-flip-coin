import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    trials = 10000
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results
