import random


def one_case() -> list:
    return [random.randint(0, 1) for _ in range(10)].count(1)


def flip_coin() -> dict:
    all_casses = [one_case() for _ in range(10_000)]
    how_much = [all_casses.count(x) for x in range(11)]
    return {key: (how_much[key] / 100) for key in range(11)}
