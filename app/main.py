import random


def flip_coin() -> dict:
    num_simulations = 10000
    num_coin_flips = 10
    results = {i: 0 for i in range(11)}

    for _ in range(num_simulations):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_coin_flips))
        results[heads_count] += 1

    percentages = {k: (v / num_simulations * 100) for k, v in results.items()}
    return percentages
