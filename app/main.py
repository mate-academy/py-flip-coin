import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        num = sum([random.randint(0, 1) for _ in range(10)])
        if num in result:
            result[num] += 1
        else:
            result[num] = 0

    return {
        num: round(count / 10000 * 100, 2) for num, count in result.items()
    }
