import random


def flip_coin(n_trials: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(n_trials):
        h_count = sum(random.choice([0, 1]) for _ in range(10))
        result[h_count] += 1
    for h_count in result:
        result[h_count] = round((result[h_count] / n_trials) * 100, 2)
    return result
