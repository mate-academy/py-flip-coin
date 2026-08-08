import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    for heads in results:
        results[heads] = (results[heads] / trials) * 100

    return results
