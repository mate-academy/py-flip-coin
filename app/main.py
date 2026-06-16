import random


def flip_coin() -> dict:

    results = {i: 0 for i in range(11)}
    num_cases = 10000

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(10):
            outcome = random.randint(0, 1)
            if outcome == 0:
                heads_count += 1
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / num_cases) * 100, 2)

    return results
