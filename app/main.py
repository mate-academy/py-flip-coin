import random


def flip_coin() -> dict:
    simuls = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(simuls):
        vers = sum(random.choice([0, 1]) for _ in range(10))
        results[vers] += 1

    result_dict = {
        key: (value / simuls) * 100 for key, value in results.items()
    }

    return result_dict
