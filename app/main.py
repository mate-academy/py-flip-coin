import random


def flip_coin() -> None:
    flip_coin_keys = {key: 0 for key in range(11)}
    coin_side = [1, 2]

    for index in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(coin_side) == 1:
                count += 1
        flip_coin_keys[count] += 1

    return {key: (value / 100) for key, value in flip_coin_keys.items()}
