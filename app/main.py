import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for i in range(10000):
        head = 0
        for _ in range(10):
            flipping = random.randint(0, 1)
            if flipping == 1:
                head += 1

        result[head] += 0.01

    return result
