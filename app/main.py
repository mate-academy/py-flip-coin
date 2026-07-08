import random


def flip_coin(trials: int = 10000) -> dict:
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    return {k: round(v / trials * 100, 2) for k, v in counts.items()}
