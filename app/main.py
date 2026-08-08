import random


def flip_coin() -> dict:
    results = {x: 0 for x in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice([True, False]):
                heads_count += 1

        results[heads_count] += 1

    for key, value in results.items():
        results[key] = (value / 10000) * 100

    return results
