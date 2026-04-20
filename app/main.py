import random


def flip_coin(
        num_iterations: int = 10000,
        num_sub_iterations: int = 10
) -> dict:
    result = {i: 0 for i in range(num_sub_iterations + 1)}

    for _ in range(num_iterations):
        key = sum(random.choice([0, 1]) for _ in range(num_sub_iterations))
        result[key] += 1

    for key, value in result.items():
        value /= 100
        result[key] = value

    return result
