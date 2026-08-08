import random


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}

    for _ in range(10000):
        counter = 0
        for _ in range(10):
            counter += random.randint(0, 1)

        flips[counter] += 1

    result = {key: value / 10000 * 100 for key, value in flips.items()}
    return result
