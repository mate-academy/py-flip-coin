import random


def flip_coin() -> dict:
    trials, flips = 10000, 10
    results = {}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        if not results.get(heads):
            results[heads] = 0
        results[heads] += 1

    percentages = {key: (value / trials * 100)
                   for key, value in results.items()}

    return percentages
