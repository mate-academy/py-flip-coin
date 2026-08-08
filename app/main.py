import random


def flip_coin(num_simulations: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_simulations):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flips))
        if heads_count not in results:
            results[heads_count] = 0
        results[heads_count] += 1

    probs = {k: (v / num_simulations) * 100 for k, v in results.items()}
    return probs
