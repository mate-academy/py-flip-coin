import random


def flip_coin() -> dict:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    for k in results:
        results[k] = round(results[k] / cases * 100, 2)

    return results


print(flip_coin())
