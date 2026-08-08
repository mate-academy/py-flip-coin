import random


def flip_coin() -> None:

    flips = {case: case for case in range(0, 11)}

    for case in range(0, 10001):
        flips[sum(random.choices([1, 0], k=10))] += 1

    for i in flips:
        flips[i] = flips[i] / 100

    return flips
