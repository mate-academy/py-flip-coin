import random


def flip_coin():
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        flip = 0

        for _ in range(10):
            face = random.randint(0, 1)
            if face:
                flip += 1

        result[flip] += 1

    return {key: value / 100 for key, value in result.items()}
