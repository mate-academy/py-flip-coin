from random import random


def flip_coin() -> dict:
    res = {}
    attempts = 10000

    for i in range(attempts):
        head = 0
        for attemp in range(10):
            if random() > 0.5:
                head += 1
        if head in res:
            res[head] += 1
        else:
            res[head] = 1
    return {head: round((counter / attempts) * 100, 2)
            for head, counter in res.items()}
