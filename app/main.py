import random


def flip_coin() -> None:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {key: (value / trials) * 100
                   for key, value in results.items()}
    return percentages
