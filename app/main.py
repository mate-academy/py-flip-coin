import random


def flip_coin(cases: int = 10000, heads: int = 10) -> dict:
    heads_count = {i: 0 for i in range(heads + 1)}
    for _ in range(cases):
        flips = sum(random.choice([0, 1]) for _ in range(heads))
        heads_count[flips] += 1
    for i in range(heads + 1):
        heads_count[i] = round((heads_count[i] / cases * 100), 2)
    return heads_count
