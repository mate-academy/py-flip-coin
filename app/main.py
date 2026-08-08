import random


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {}
    for _ in range(trials):
        num_heads = sum(random.randint(0, 1) for _ in range(flips))
        results[num_heads] = results.get(num_heads, 0) + 1
    probabilities = {k: v / trials * 100 for k, v in results.items()}
    return probabilities
