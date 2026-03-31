import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    results = {}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] = results.get(num_heads, 0) + 1

    for key in results:
        results[key] = (results[key] / num_cases) * 100

    return results
