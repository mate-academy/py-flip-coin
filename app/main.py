import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flip = 10
    result = {}

    for i in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flip))
        result[heads_count] = result.get(heads_count, 0) + 1

    for key, value in result.items():
        result[key] = (value / num_cases) * 100

    return result
