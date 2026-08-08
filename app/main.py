import random


def flip_coin() -> dict:

    save = {key: 0 for key in range(0, 11)}

    for _ in range(10000):
        count = sum([random.randint(0, 1) for _ in range(10)])
        save[count] += 1

    return {key: round(value / 10000 * 100, 2) for key, value in save.items()}
