import random


def flip_coin() -> dict:
    results = {}
    total_cases = 10000
    for _ in range(total_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentages = {
        heads: count / total_cases * 100
        for heads, count in results.items()
    }
    return percentages
