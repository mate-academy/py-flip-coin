import random


def flip_coin() -> None:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] += 1

    percentages = {key: (value / total_cases) * 100
                   for key, value in results.items()}

    return percentages
