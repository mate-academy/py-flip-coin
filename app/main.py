import random


def flip_coin() -> dict:
    all_flips = [sum(random.choices([1, 0], k=10)) for _ in range(10000)]
    return {i: (all_flips.count(i) / len(all_flips)) * 100 for i in range(11)}
