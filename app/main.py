import random


def flip_coin(num_simulations: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_simulations):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key, value in results.items():
        value /= 100
        results[key] = value
    return results
