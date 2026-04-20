import random


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = flip_ten_times()
        heads_count[heads] += 1

    for i in range(11):
        heads_count[i] = heads_count[i] / 100

    return heads_count


def flip_ten_times() -> int:
    heads = 0
    tails = 0

    for _ in range(10):
        coin = random.randint(0, 1)

        if coin == 1:
            heads += 1
        else:
            tails += 1

    return heads
