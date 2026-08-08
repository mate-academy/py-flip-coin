import random


def flip_coin() -> dict:
    trials = 10000
    results = {}

    for _ in range(trials):
        heads = 0

        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads += 1

        if heads not in results:
            results[heads] = 1
        else:
            results[heads] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results
