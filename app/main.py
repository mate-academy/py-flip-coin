import random


def flip_coin() -> dict:
    flips = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for i in range(1, 10001):
        count = 0
        for i in range(10):
            choice = random.randint(0, 1)
            if choice:
                count += 1
        flips[count] += 1
    for key, value in flips.items():
        flips[key] = round((value / 10000) * 100, 2)
    return flips
