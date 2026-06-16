import random


def flip_coin() -> dict:
    cases = 10000
    times = 10
    coin = ["head", "tail"]
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for case in range(cases):
        head = 0

        for flip in range(times):
            if random.choice(coin) == "head":
                head += 1

        result[head] += 1 / 100

    return result
