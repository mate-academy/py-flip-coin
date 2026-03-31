import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for i in range(10000):
        head = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                head += 1

        result[head] += 0.01

    return result
