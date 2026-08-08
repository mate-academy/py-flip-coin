# write your code here
import random


def flip_coin() -> dict:
    num_trials = 10000
    num_flips = 10
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1
    percentages = {k: (v / num_trials) * 100 for k, v in results.items()}

    return percentages
