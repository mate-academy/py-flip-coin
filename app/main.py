import random


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results = {count: 0 for count in range(11)}
    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1
    for head_total in results:
        results[head_total] = round(results[head_total] * 100 / trials, 2)
    return results
