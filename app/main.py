import random


def flip_coin() -> dict:
    num_trials = 10000
    num_flips = 10
    results = {}

    for _ in range(num_trials):
        flips = [random.choice(["H", "T"]) for _ in range(num_flips)]
        num_heads = flips.count("H")
        results[num_heads] = results.get(num_heads, 0) + 1

    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results
