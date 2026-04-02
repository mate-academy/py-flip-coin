import random


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    res = {i: 0 for i in range(flips_per_trial + 1)}
    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1])
            for _ in range(flips_per_trial)
        )
        res[heads_count] += 1
    res_percentage = {
        key: (value / trials) * 100 for key, value in res.items()
    }
    return res_percentage
