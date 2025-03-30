import random


def flip_coin() -> dict[int, float]:
    num_cases = 10000
    num_flips = 10
    results = {}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1

        if num_heads not in results:
            results[num_heads] = 0
        results[num_heads] += 1

    percentages = {
        key: (value / num_cases) * 100 for key, value in results.items()}

    return percentages
