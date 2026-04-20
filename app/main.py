import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {}
    for i in range(11):
        res[i] = 0

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads = heads + 1

        res[heads] = res[heads] + 1

    for key in res:
        res[key] = res[key] / 10000 * 100

    return res

# make_graph()