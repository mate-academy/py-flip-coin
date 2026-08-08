from random import random


def flip_coin() -> dict:
    result = {}
    cases = 10000
    times = 10

    for case in range(cases):
        head = 0

        for time in range(times):
            if random() < 0.5:
                head += 1

        if head in result:
            result[head] += 1
        else:
            result[head] = 1
    return {
        head: round((count / cases) * 100, 2)
        for head, count in result.items()
    }
