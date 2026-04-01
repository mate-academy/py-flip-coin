import random


def flip_coin() -> dict:
    count_of_flipping = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(count_of_flipping):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / count_of_flipping) * 100, 2)

    return results
