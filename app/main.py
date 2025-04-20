import random


def flip_coin() -> dict:

    result = {i: 0 for i in range(11)}

    for _ in range(10000):

        heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 2:
                heads += 1

        result[heads] += 1 / 100

        result = {key: round(value, 2) for key, value in result.items()}

    return result
