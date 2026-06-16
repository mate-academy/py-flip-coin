import random


def flip_coin(flips: int = 10000) -> dict:
    result = {key: 0 for key in range(11)}

    for _ in range(flips):
        flip_count = sum(random.randint(0, 1) for _ in range(10))
        result[flip_count] += 1

    for key, value in result.items():
        result[key] = round(value / flips * 100, 2)

    return result
