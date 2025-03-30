import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for i in range(1, 10001):
        statistics = 0
        for _ in range(1, 11):
            attempt = random.choice(["up", "down"])
            if attempt == "up":
                statistics += 1
        results[statistics] += 1
    for key in results.keys():
        results[key] /= 100
    return results
