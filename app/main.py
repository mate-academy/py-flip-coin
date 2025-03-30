import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        num_heads = sum(random.randint(0, 1) for _ in range(10))
        results[num_heads] += 1

    for key in results:
        results[key] = round((results[key] / num_cases) * 100, 2)

    return results
