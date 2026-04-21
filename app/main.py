import random


def flip_coin() -> dict:
    trials, flips = 10000, 10
    results = {}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] = results.get(heads, 0) + 1

    total_trials = trials
    percentages = {key: (value / total_trials * 100)
                   for key, value in results.items()}

    return percentages
