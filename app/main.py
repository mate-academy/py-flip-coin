import random


def flip_coin(
        trials: int = 10000,
        flips_per_trial: int = 10
) -> dict[int, float]:

    results = {i: 0.0 for i in range(flips_per_trial + 1)}
    for _ in range(trials):
        heads = 0
        for _ in range(flips_per_trial):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] * 100 / trials, 2)
    return results


print(flip_coin())
