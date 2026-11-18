
import random


def flip_coin() -> dict[int, float]:
    cases = 10000
    results = {number: 0 for number in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    for number in results:
        results[number] = round(results[number] / cases * 100, 2)

    return results
