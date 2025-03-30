import random


def flip_coin() -> dict:
    num_trials = 10000
    heads_count = [0] * 11

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        heads_count[heads] += 1

    percentage_distribution = {i: (count / num_trials) * 100
                               for i, count in enumerate(heads_count)}

    return percentage_distribution
