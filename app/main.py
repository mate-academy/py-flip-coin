from random import randint


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
    for _ in range(10000):
        head_count = 0
        for i in range(10):
            if randint(0, 1):
                head_count += 1
        results[head_count] += 1 / 100
    return results
