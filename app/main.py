import random


def flip_coin() -> dict:
    keys = {}
    for i in range(11):
        keys[i] = 0
    for _ in range(10000):
        heads = 0
        for i in range(10):
            heads += random.choice([0, 1])
        keys[heads] += 1
    for key in keys:
        keys[key] = keys[key] / 100

    return keys


if __name__ == "__main__":
    flip_coin()
