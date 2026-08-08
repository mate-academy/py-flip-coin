import random


def flip_coin() -> dict:
    result = {}

    flip_times = [[random.randint(0, 1) for flip in range(10)]
                  for _ in range(10000)]

    for times in range(11):
        counter = 0
        for step in flip_times:
            if step.count(0) == times:
                counter += 1
        result[times] = round((counter / 10000) * 100, 2)

    return result
