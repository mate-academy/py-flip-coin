import random


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    finish_result = {
        key: (value / num_cases) * 100 for key, value in results.items()}

    return finish_result
