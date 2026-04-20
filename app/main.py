import random


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    results = {}
    for num in range(num_trials):
        num_heads = 0
        for flip in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1
        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1
    for num_heads in results:
        results[num_heads] = results[num_heads] / num_trials * 100
    return results
