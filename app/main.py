import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1

    total_cases = float(num_cases)
    for key, value in results.items():
        results[key] = (value / total_cases) * 100

    return results
