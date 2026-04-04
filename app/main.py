import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    for key, value in results.items():
        results[key] = round((value / total_cases) * 100, 2)

    return results
