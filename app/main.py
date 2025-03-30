from random import randint


def flip_coin() -> dict:
    res = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10001):
        lst = [randint(0, 1) for _ in range(10)]
        res[lst.count(0)] += 1
    for key, value in res.items():
        res[key] = round(value / 10000 * 100, 2)
    return res
