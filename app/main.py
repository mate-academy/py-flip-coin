from random import randint


def flip_coin(cases: int = 10000) -> dict:
    res = {i: 0 for i in range(0, 11)}
    for _ in range(cases):
        head = 0
        for _ in range(10):
            if randint(0, 1):
                head += 1
        res[head] += 1 / 100
    return res
