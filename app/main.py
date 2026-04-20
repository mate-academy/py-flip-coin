import random


def flip_coin(cases: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        head = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                head += 1
        result[head] += 1

    for key in result:
        result[key] = round((result[key] / cases) * 100, 2)
    return result
