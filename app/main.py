import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(0, 11)}
    for i in range(0, 10000):
        heads = 0
        for flip in range(0, 10):
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result
