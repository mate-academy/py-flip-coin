import random


def flip_coin() -> dict:
    result = {}
    total_flips = 10
    cases = 10000

    for _ in range(cases):
        eagles = 0
        for _ in range(total_flips):
            if random.random() < 0.5:
                eagles += 1
        if eagles not in result:
            result[eagles] = 1
        else:
            result[eagles] += 1

    percents = {}
    for key, value in result.items():
        percent = round(value / cases * 100, 2)
        percents[key] = percent
    return {k: percents[k] for k in sorted(percents)}
