import random


def flip_coin() -> dict:
    num_trials = 10000
    num_coin_flips = 10
    results = {}

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coin_flips))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentages = {k: (v / num_trials) * 100 for k, v in results.items()}

    return percentages
