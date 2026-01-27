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
        10: 0,
    }
    heads = 0
    for _ in range(10000):
        for i in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        results[heads] += 1
        heads = 0
    for i in range(11):
        results[i] = results[i] / 100
    return results
