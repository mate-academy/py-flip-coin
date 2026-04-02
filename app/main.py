import random


def flip_coin():
    flip_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        flips = 0
        for _ in range(10):
            eagle = random.randint(0, 1)
            if eagle:
                flips += 1

        flip_dict[flips] += 1

    return {key: value / 100 for key, value in flip_dict.items()}
