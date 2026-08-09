from random import choices
from collections import Counter


def flip_coin() -> dict:
    outcomes = []

    for _ in range(10000):
        flips = choices([0, 1], k=10)
        heads_count = sum(flips)
        outcomes.append(heads_count)

    coin_flips = Counter(outcomes)
    percents = {
        key: (value / 10000) * 100 for key, value in coin_flips.items()
    }

    return percents
