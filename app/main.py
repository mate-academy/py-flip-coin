import random
from collections import Counter


def flip_coin(num_flips: int = 10000,
              num_coins: int = 10) -> dict:
    results = Counter()

    for _ in range(num_flips):
        num_heads = sum(random.choice([0, 1])
                        for _ in range(num_coins))
        results[num_heads] += 1

    percentages = {key: value / num_flips * 100
                   for key, value in results.items()}
    return percentages
