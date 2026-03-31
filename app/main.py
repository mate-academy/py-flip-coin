import random


def flip_coin() -> dict:
    num_simulations = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_simulations):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_simulations) * 100

    return results
