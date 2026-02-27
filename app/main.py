import random


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


print(flip_coin())
