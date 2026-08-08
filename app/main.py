import random


def flip_coin() -> dict:
    statistics = {
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
    for _ in range(10000):
        count = 0

        for _ in range(10):
            if random.randint(0, 1):
                count += 1

        statistics[count] += 1

    return {num: drop / 100 for num, drop in statistics.items()}
