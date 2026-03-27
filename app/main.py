import random


def flip_coin():
    n_experiments = 10000
    n_flips = 10
    results = {i: 0 for i in range(n_flips + 1)}
    for _ in range(n_experiments):
        heads_count = 0
        for _ in range(n_flips):
            heads_count += random.randint(0, 1)
            pass
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / n_experiments) * 100

    return results
