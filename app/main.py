import random


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    heads_count = {i: 0 for i in range(flips + 1)}
    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        heads_count[heads] += 1
    percentages = {k: round((v / cases) * 100, 2)
                   for k, v in heads_count.items()}
    return percentages
