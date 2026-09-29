import random


def flip_coin() -> dict[int, float]:
    cases = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads_count += 1

        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = results[heads_count] / cases * 100

    return results
