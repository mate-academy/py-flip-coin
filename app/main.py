import random


def flip_coin(count_cases: int = 10000, count_flips: int = 10) -> dict:
    result = {i: 0 for i in range(count_flips + 1)}
    for _ in range(count_cases):
        heads = sum(random.randint(0, 1) for _ in range(count_flips))
        result[heads] += 1

    return {
        key: (value / count_cases * 100) for key, value in result.items()
    }
