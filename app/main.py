import random


def flip_coin() -> dict:
    results = {}
    num_trials = 10000

    for i in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                num_heads += 1

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results
