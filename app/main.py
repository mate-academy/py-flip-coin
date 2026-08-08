import random


def flip_coin():
    res = {el: 0 for el in range(11)}

    for _ in range(1000):
        flips = 0

        for _ in range(10):
            face_side = random.randint(0, 1)
            if face_side:
                flips += 1

        res[flips] += 1

    return {key: value / 100 for key, value in res.tems()}
