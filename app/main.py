import random


def flip_coin() -> dict[int]:
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

    for case in range(10000):
        head = 0

        for flip in range(10):
            if random.choice(coin) == "head":
                head += 1

        result[head] += 1 / 100

    return result
