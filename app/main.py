import random


def flip_coin() -> dict:
    results = {}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1
    percentages = {key: value / 100 for key, value in results.items()}
    return percentages
