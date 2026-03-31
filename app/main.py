from random import randint


def flip_coin() -> dict:
    # initialize dict
    result = {}
    for i in range(0, 11):
        result[i] = 0

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if randint(0, 1):
                heads += 1
        result[heads] += 1

    attempts = 10000
    for key in result:
        result[key] = (result[key] / attempts) * 100
    return result
