import random


def flip_coin(cases: int = 9999, times: int = 11) -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for case in range(cases):
        heads_times = sum(random.choice([0, 1]) for _ in range(1, times))
        result[heads_times] = result.get(heads_times, 0) + 1
    for heads, count in result.items():
        result[heads] = round((result[heads] / cases * 100), 2)
    return result
