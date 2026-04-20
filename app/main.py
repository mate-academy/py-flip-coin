import random


def flip_coin(trials: int = 10000) -> dict:
    results = {}
    for test in range(11):
        results[test] = 0
    for trial in range(trials):
        heads = 0
        for experement in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1
    for test in range(11):
        results[test] = round(results[test] / trials * 100, 2)
    return results
