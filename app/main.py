import random


def flip_coin():
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        result[sum([random.randint(0, 1) for _ in range(10)])] += 1

    return {key: (value / 100) for key, value in result.items()}
