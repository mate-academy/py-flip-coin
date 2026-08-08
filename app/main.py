import random


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(10):
            coin_flip = random.randint(0, 1)
            heads_count += coin_flip

        results[heads_count] += 1

    total_cases = float(num_cases)
    percentages = {
        key: (value / total_cases) * 100 for key, value in results.items()
    }

    return percentages
