from random import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10000

    for _ in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for num in results:
        results[num] = round(results[num] / num_trials * 100, 2)

    return results
