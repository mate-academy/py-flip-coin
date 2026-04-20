import random


def flip_coin() -> dict:
    rolls = {}

    for _ in range(10000):
        heads = sum(random.choices([0, 1], k=10))
        if heads in rolls:
            rolls[heads] += 1
        else:
            rolls[heads] = 1

    result = {key: (value / 100) for key, value in rolls.items()}
    return result
