import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    num_trials = 10000
    for _ in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1
    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results
