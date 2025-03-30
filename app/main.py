import random


def flip_coin() -> dict:
    simulation = 10000
    result = {i: 0 for i in range(11)}

    for i in range(simulation):
        head_count = sum(random.choice([0, 1]) for _ in range(10))
        result[head_count] += 1

    for key in result:
        result[key] = (result[key] / simulation) * 100

    return result
