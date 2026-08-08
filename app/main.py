import random


def flip_coin() -> dict:
    num_trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results
