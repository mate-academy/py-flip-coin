import random


def flip_coin(cases: int = 10_000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            heads += random.choice([0, 1])

        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / cases * 100, 2)
    return results
