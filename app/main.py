import random


def flip_coin(num_trials: int = 10000) -> dict:
    counts = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads_count] += 1

    for key in counts:
        counts[key] = round((counts[key] / num_trials) * 100, 2)

    return counts
