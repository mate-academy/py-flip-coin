import random


def flip_coin() -> dict:
    tossing = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(tossing):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1
    return {ind: round(val / tossing * 100, 2) for ind, val in result.items()}
