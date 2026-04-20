import random


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        result[heads_count] += 0.01

    return result
