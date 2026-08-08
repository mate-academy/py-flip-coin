import random


def flip_coin(num_flips: int = 10000, num_coins: int = 10) -> float:
    results = {}

    for _ in range(num_flips):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_coins))
        results[heads_count] = results.get(heads_count, 0) + 1

    percentages = {k: v / num_flips * 100 for k, v in results.items()}
    return percentages
