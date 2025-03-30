import random


def flip_coin(
        number_of_cases: int = 10000,
        times_of_fliping: int = 10
) -> dict:
    results = {i: 0 for i in range(times_of_fliping + 1)}

    for _ in range(number_of_cases):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(times_of_fliping))
        results[heads_count] += 1

    percentages = {heads: (count / number_of_cases) * 100
                   for heads, count in results.items()}

    return percentages
