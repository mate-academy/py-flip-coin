import random


def flip_coin() -> dict:
    flipping_coin = {i: 0 for i in range(11)}
    for i in range(10000):
        cnt = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                cnt += 1
        flipping_coin[cnt] += 1
    return {key: value / 100 for key, value in flipping_coin.items()}
