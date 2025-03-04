import random


def flip_coin(
    trials: int = 10000,
    flips_per_trial: int = 10
) -> dict:

    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = 0

        for _ in range(flips_per_trial):
            if random.choice([0, 1]) == 0:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results
