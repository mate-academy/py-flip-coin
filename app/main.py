from random import randint


def flip_coin() -> dict:
    cases = sorted(
        [sum(1 for _ in range(10) if randint(0, 1) == 1) for _ in range(10000)]
    )
    return {key: (cases.count(key) / 10000) * 100 for key in set(cases)}
