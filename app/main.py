import random


def flip_coin() -> dict:
    random.seed(10)
    results = {i: 0 for i in range(11)}

    trials = 10000
    flips_per_trial = 10

    for _ in range(trials):
        heads_count = 0

        for _ in range(flips_per_trial):
            if random.randint(0, 1) == 1:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results
