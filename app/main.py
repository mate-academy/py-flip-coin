import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    results = {key: round((value / total_cases) * 100, 2)
               for key, value in results.items()}

    return results
