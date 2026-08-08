import random


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {}
    for _ in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] = results.get(heads_count, 0) + 1

    total_cases = float(num_cases)
    for key in results:
        results[key] = (results[key] / total_cases) * 100

    return results
