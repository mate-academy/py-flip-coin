import random


def flip_coin() -> None:
    results = dict.fromkeys(range(11), 0)

    repeats = 10_000
    for _ in range(repeats):
        flips = random.choices((0, 1), k=10)
        results[flips.count(1)] += 1

    return {k: v / repeats * 100 for k, v in results.items()}
