import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10000

    for i in range(num_trials):
        num_heads = 0
        for current_try in range(10):
            if random.random() < 0.5:
                num_heads += 1

        if num_heads not in results:
            results[num_heads] = 0
        results[num_heads] += 1

    for key, value in results.items():
        results[key] = round((value / num_trials) * 100, 2)

    return results
