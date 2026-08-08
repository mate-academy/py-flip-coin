import random


def flip_coin() -> dict:
    head_counts = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        head_counts[heads] += 1

    for heads in head_counts:
        head_counts[heads] = round((head_counts[heads] / 10000) * 100, 2)

    return head_counts
