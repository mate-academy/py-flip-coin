import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads_count += 1
        results[heads_count] += 1
    percent_results = {}
    for i in results:
        percent_results[i] = round((results[i] / 10000) * 100, 2)
    return percent_results
