import random


def flip_coin() -> dict:
    results = {
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
    for cases in range(10000):
        count = 0
        for flip in range(10):
            number = random.randint(0, 1)
            if number == 1:
                count += 1
        results[count] += 1
    for key, value in results.items():
        results[key] = (value / 10000) * 100
    return results
