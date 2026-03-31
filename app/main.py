from random import randint


def flip_coin() -> dict:
    res = []
    for i in range(10000):
        number = 0
        for num in range(10):
            if randint(0, 1) == 1:
                number += 1
        res.append(number)
    return {d: res.count(d) / len(res) * 100 for d in range(11)}
