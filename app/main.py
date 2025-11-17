import random


def flip_coin() -> dict:
    counts = {i : 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            heads_count += random.choice([0, 1])
        counts[heads_count] += 1

    return {k: round(v / 10000 * 100, 2) for k, v in counts.items()}
