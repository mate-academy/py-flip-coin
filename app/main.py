from random import random


def flip_coin(flipping_coin: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(flipping_coin):
        heads_count = 0
        for _ in range(10):
            if random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    for heads in results:
        results[heads] = round((results[heads] / flipping_coin) * 100, 2)
    return results
