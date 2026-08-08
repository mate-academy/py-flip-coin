import random


def flip_coin() -> dict:
    trials = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    percentages = {k: round(v / trials * 100, 2) for k, v in counts.items()}
    return percentages
