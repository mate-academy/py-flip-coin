import random


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        flips_result = sum([random.randint(0, 1) for _ in range(10)])
        result[flips_result] += 1
    for i in range(11):
        result[i] = round(result[i] / 10000 * 100, 2)
    return result
