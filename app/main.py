import random


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100
    return results
