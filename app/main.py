import random


def flip_coin(cases: int = 10000) -> dict:
    results = {k: 0 for k in range(11)}

    for case in range(cases):
        heads = 0
        for times in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for percent in results:
        results[percent] /= 100

    return results
