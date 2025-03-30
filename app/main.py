import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    result = {num: 0 for num in range(num_flips + 1)}
    percentages_per_case = round(100 / num_cases, 2)
    for _ in range(num_cases):
        heads = sum(random.randint(0, 1) for _ in range(num_flips))
        result[heads] += percentages_per_case
    return result
