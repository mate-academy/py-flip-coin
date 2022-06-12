import random


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        flips = 0
        for _ in range(10):
            toss = random.randint(0, 1)
            if toss == 1:
                flips += 1
        result[flips] += 1

    return {key: value / 100 for key, value in result.items()}


print(flip_coin())
