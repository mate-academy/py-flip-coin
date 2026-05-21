import random


def flip_coin() -> dict:
    trials = 10000
    flips_per_trial = 10

    counts = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        counts[heads_count] += 1

    return {key: (value / trials) * 100 for key, value in counts.items()}
