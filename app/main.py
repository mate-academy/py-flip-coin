import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(0, 11)}

    for _ in range(0, 10000):
        heads = 0

        for _ in range(0, 10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results
