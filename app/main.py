from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if randint(0, 1):
                heads += 1
        result[heads] += 1
    for key, value in result.items():
        value /= 100
        result[key] = value
    return result
