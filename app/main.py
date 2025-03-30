import random


def flip_coin(num_of_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_of_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: round((v / num_of_cases) * 100, 2)
                   for k, v in results.items()}
    return percentages
