import random


def flip_coin(tries: int = 10000, flips: int = 10) -> dict:
    result = {i: 0 for i in range(flips + 1)}

    for _ in range(tries):
        heads = 0
        for _ in range(flips):
            if random.random() < 0.5:
                heads += 1
        result[heads] += 1

    for k in result:
        result[k] = round(result[k] / tries * 100, 2)

    return result
