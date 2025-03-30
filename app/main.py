import random


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key, value in results.items():
        results[key] = (value / num_cases) * 100

    return results
