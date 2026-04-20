import random


def flip_coin() -> dict:
    heads = []
    ten_flips = []

    for _ in range(10001):
        ten_flips.append([random.choice((0, 1)) for _ in range(10)])

    for ten_flip in ten_flips:
        heads.append(ten_flip.count(0))

    return {head: heads.count(head) / len(heads) * 100
            for head in range(0, 11)}
