import random


def flip_coin() -> dict:
    num_simulations = 10000
    flips_per_simulation = 10
    results = {i: 0 for i in range(flips_per_simulation + 1)}

    for _ in range(num_simulations):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_simulation)
        )
        results[heads_count] += 1

    percentages = {k: (v / num_simulations) * 100 for k, v in results.items()}
    return percentages
