import random


def flip_coin() -> dict:
    flip = {}
    for flips in range(11):
        flip[flips] = flips
    for repeat in range(10000):
        flip[sum(random.choices([0, 1], k=10))] += 1

    for values in flip:
        flip[values] = flip[values] / 100
    return flip
