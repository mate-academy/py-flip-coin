import random


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))

        if heads_count not in results:
            results[heads_count] = 1
        else:
            results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results
