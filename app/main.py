import random


def flip_coin(trials: int = 10_000) -> dict:
    results = {i: 0 for i in range(0, 11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    results = {k: v * 100 / trials for k, v in results.items()}

    return results
