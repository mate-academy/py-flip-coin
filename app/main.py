import random


def flip_coin(num_experiments: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}
    for i in range(num_experiments):
        heads = 0
        for _ in range(flips):
            flip = random.randint(1, 2)
            if flip == 1:
                heads += 1
        results[heads] += 1

    for key, value in results.items():
        results[key] = (value / num_experiments) * 100

    return results
