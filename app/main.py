import random


def flip_coin() -> dict:
    gauss = {i: 0.0 for i in range(11)}

    for case in range(10000):
        flips = random.choices([0, 1], k=10)
        head = sum(flips)
        gauss[head] += 1

    for key in gauss:
        gauss[key] = round(gauss[key] / 10000 * 100, 2)

    return gauss
