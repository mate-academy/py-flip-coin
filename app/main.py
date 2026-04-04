import random


def flip_coin() -> dict:
    cases = 10000
    result = {i: 0 for i in range(11)}
    for _ in range(cases):
        head = sum(random.randint(0, 1) for _ in range(10))
        result[head] += 1

    return {k: (v / cases) * 100 for k, v in result.items()}
