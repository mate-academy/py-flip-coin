import random


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(0, 11)}

    for i in range(10000):
        dropped = random.choices([0, 1], k=10)
        heads_count[dropped.count(1)] += 1

    return {k: round(v / 10000 * 100, 2) for k, v in heads_count.items()}
