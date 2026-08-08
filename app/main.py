import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}

    for _ in range(10000):
        count = sum(random.choice([0, 1]) for _ in range(10))
        result[count] += 1

    return {key: (value / 10000) * 100 for key, value in result.items()}
