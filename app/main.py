import random


def flip_coin(flips: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(flips):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1

        result[heads] += 1

    for key in result:
        result[key] = round((result[key] / flips) * 100, 2)

    return result
