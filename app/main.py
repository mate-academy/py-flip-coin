import random


def flip_coin() -> dict:
    cases = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1

    return {
        key: round(value / cases * 100, 2) for key, value in result.items()
    }
