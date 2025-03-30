from random import randint


def flip_coin() -> dict:
    rolls = {}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += randint(0, 1)
        if heads not in rolls:
            rolls[heads] = 1
        else:
            rolls[heads] += 1
    for key in rolls:
        rolls[key] /= 100
    return rolls
