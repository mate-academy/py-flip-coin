import random


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1
    for number in results:
        results[number] = (results[number] / num_trials) * 100

    return results
