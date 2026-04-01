import random


def flip_coin() -> dict:

    coin_flips = 10
    cases = 10000
    heads_count = {i: 0 for i in range(coin_flips + 1)}

    for _ in range(cases):
        heads = 0

        for _ in range(coin_flips):
            if random.random() < 0.5:
                heads += 1

        heads_count[heads] += 1

    for i in range(coin_flips + 1):
        heads_count[i] = round(heads_count[i] / cases * 100, 2)

    return heads_count
