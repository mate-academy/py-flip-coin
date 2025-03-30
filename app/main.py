import random


def flip_coin() -> dict:
    distribution = {i: 0 for i in range(11)}
    for _ in range(0, 10000):
        count = 0

        for _ in range(0, 10):
            flip = random.randint(0, 1)

            if flip == 0:
                count += 1

        distribution[count] += 1

    for i in range(11):
        distribution[i] /= 100

    return distribution
