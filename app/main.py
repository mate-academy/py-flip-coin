import random


def flip_coin() -> dict:
    attempts = {}
    for i in range(10000):
        heads = 0
        for attempt in range(10):
            heads += random.randint(0, 1)
        if heads not in attempts.keys():
            attempts[heads] = 1
        else:
            attempts[heads] += 1
    for key, values in attempts.items():
        attempts[key] = (values / 10000) * 100
    return attempts
