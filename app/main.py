import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10_000):
        result[len([1 for _ in range(10) if random.choice([1, 0]) == 1])] += 1
    return {key: round(value / 100, 2) for key, value in result.items()}
