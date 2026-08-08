import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    percentage_results = {
        k: (v / total_cases) * 100 for k, v in results.items()
    }
    return percentage_results
