import random


def flip_coin(num_flips: int=10, num_trials: int=10000) -> float: # noqa
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results
