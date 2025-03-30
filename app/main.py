import random


def flip_coin() -> dict[int, float]:
    result = {i: 0 for i in range(11)}
    experiments = 10000
    for _ in range(experiments):
        head_count = sum(random.choice([0, 1]) for _ in range(10))
        result[head_count] += 1

    for key in result:
        result[key] = (result[key] / experiments) * 100

    return result
