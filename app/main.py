import random


def flip_coin() -> dict:
    result_of_heads = {}
    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        result_of_heads[heads] = result_of_heads.get(heads, 0) + 1

    result = {key: (value / 100) for key, value in result_of_heads.items()}
    return result
