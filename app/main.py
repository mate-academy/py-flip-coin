import random


def flip_coin() -> dict:

    flips = [[random.randint(0, 1)
              for _ in range(10)].count(1)
             for _ in range(10000)]
    return {time: round(flips.count(time) * 0.01, 2) for time in range(0, 11)}
