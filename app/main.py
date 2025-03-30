import random


def flip_coin() -> dict:
    res = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for i in range(10000):
        num_heads = 0
        for _ in range(10):
            value = random.randint(0, 1)
            if value == 1:
                num_heads += 1
        res[num_heads] += 1

    for key in res:
        res[key] = res[key] / 10000 * 100

    return res


print(flip_coin())
