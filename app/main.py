import random


def flip_coin(flips: int = 10000) -> dict:
    result = {}
    for i in range(flips):
        nums = 0
        for time in range(10):
            if random.random() < 0.5:
                nums += 1
        if nums not in result:
            result[nums] = 0
        result[nums] += 1
    for res in result:
        result[res] = round(result[res] / flips * 100, 2)
    return result
