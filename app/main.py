import random


def flip_coin() -> dict:
    num_simulations = 10000
    num_flips = 10
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_simulations):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] += 1

    percentage_results = {
        key: (value / num_simulations) * 100
        for key, value in results.items()
    }

    return percentage_results
