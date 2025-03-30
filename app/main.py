import random


def flip_coin(num_experiments: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_experiments):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] = results.get(heads, 0) + 1

    percentages = {
        heads: (count / num_experiments) * 100
        for heads, count in results.items()
    }

    return {i: percentages.get(i, 0) for i in range(num_flips + 1)}
