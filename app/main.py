import random


def flip_coin():
    heads_count = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count[sum(random.randint(0, 1) for _ in range(10))] += 1
    return {key: value / 100 for key, value in heads_count.items()}
