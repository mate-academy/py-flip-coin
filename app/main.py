import random


def flip_coin() -> dict:
    flips = [
        sum(
            1 for _ in range(10)
            if random.randint(0, 1) == 1
        )
        for _ in range(10000)
    ]
    return {i: (flips.count(i) / 100) for i in range(11)}
