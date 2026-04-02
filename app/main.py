from random import randint


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            throw = randint(1, 2)
            if throw == 1:
                heads += throw
        flips[heads] += 1
    flips = {key: round(value / sum(flips.values()) * 100, 2)
             for key, value in flips.items()}
    return flips
