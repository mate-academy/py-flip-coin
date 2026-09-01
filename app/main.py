import random


def flip_coin() -> dict:
    cases = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    for heads in results:
        results[heads] = round(results[heads] / cases * 100, 2)

    return results
