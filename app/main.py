import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10_000
    num_flips = 10

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] = results.get(heads_count, 0) + 1

    percentages = {k: v / num_trials * 100 for k, v in results.items()}

    return percentages
