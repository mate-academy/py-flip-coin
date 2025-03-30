import random


def flip_coin(flips_count: int = 10000, rounds: int = 10) -> dict:
    results = {i: 0.0 for i in range(rounds + 1)}
    for _ in range(flips_count):
        heads_count = sum(random.choice([0, 1]) for _ in range(rounds))
        results[heads_count] += 1
    for key in results:
        results[key] = (results[key] / flips_count) * 100
    return results
