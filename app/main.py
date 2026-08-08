import random


def flip_coin(num_cases: int = 10000) -> dict:
    num_flips = 10
    counts = {i: 0 for i in range(num_flips + 1)}
    for _ in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flips))
        counts[heads_count] += 1
    results = {}
    for heads, count in counts.items():
        percentage = round((count / num_cases) * 100, 2)
        results[heads] = percentage
    return results
