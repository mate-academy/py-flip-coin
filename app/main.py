import random


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        num_heads = sum(random.randint(0, 1) for _ in range(10))
        result[num_heads] += 0.01

    return result
