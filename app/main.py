from random import randint


def flip_coin() -> dict:
    coin_flips = {}

    for _ in range(10000):
        heads_count = sum(randint(0, 1) for _ in range(10))
        coin_flips[heads_count] = coin_flips.get(heads_count, 0) + 1

    percents = {key: (value / 10000) * 100 for key,
                value in coin_flips.items()}

    return percents
