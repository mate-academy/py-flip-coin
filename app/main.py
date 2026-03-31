import random


def flip_coin() -> dict:
    heads_count = {}
    for _ in range(50000):
        heads = 0
        for i in range(10):
            side = random.randint(0, 1)
            if side == 0:
                heads += 1
        if heads not in heads_count:
            heads_count[heads] = 1
        else:
            heads_count[heads] += 1
    for key in heads_count:
        heads_count[key] /= 500
    return heads_count
