import random


def flip_coin() -> dict:
    sample = {num: 0 for num in range(11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for __ in range(10))
        sample[heads] += 0.01

    return sample
