import random


def flip_coin() -> dict:
    coin_flip = {i: 0 for i in range(11)}
    range_coin = 10_000

    for _ in range(range_coin):
        counter = 0

        for _ in range(10):
            counter += random.randint(0, 1)
        coin_flip[counter] += 1

    coin_flip = {k: v / range_coin * 100 for k, v in coin_flip.items()}

    return coin_flip
