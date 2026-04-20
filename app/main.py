import random


def flip_coin() -> dict:
    simulations = 10000
    flips_per_simulation = 10

    counts = {i: 0 for i in range(flips_per_simulation + 1)}

    for _ in range(simulations):
        heads_count = sum(
            random.randint(0, 1) for _ in range(flips_per_simulation)
        )
        counts[heads_count] += 1

    return {k: (v / simulations) * 100 for k, v in counts.items()}
