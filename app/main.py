import random


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))

        results[num_heads] += 1

    for key in results:
        results[key] = (results[key] / num_cases) * 100

    return results
