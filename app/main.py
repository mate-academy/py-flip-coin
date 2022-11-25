import random


def flip_10_times() -> int:
    hed_count = 0
    for _ in range(1, 11):
        if random.choice(["head", "back"]) == "head":
            hed_count += 1
    return hed_count


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}

    range_of_flips = 10000
    for _ in range(range_of_flips + 1):
        if flip_10_times() not in res:
            res[flip_10_times()] = 1
        res[flip_10_times()] += 1

    for keys, values in res.items():
        res[keys] = values * 100 / range_of_flips
    return res
