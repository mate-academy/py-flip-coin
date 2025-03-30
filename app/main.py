import random


def flip_coin() -> dict:
    conducts = 10000

    data = {key: 0 for key in range(11)}
    for _ in range(conducts):
        random_cases = [random.randint(0, 1) for i in range(10)]
        flip = random_cases.count(1)
        data[flip] += 1

    result = {key: (value / conducts) * 100 for key, value in data.items()}

    return result
