import random


def flip_coin(flips: int = 10, cases: int = 10000) -> dict:
    start_dict = {num: 0 for num in range(flips + 1)}

    for _ in range(cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(flips))
        start_dict[num_heads] += 1

    result = {key: (value / cases) * 100 for key, value in start_dict.items()}

    return result
