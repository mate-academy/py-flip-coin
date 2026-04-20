import random


def flip_coin() -> dict:
    heads_statistic = {}
    attempts = 10000
    for _ in range(attempts):
        heads = [random.randint(0, 1) for _ in range(10)].count(1)
        heads_statistic[heads] = heads_statistic.get(heads, 0) + 1

    for key, value in heads_statistic.items():
        heads_statistic[key] = round((value / (attempts / 100)), 2)
    return dict(sorted(heads_statistic.items()))
