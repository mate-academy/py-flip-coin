
import random


def flip_coin() -> dict:
    cases = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    return {
        i: round(counts[i] / cases * 100, 2)
        for i in range(11)
    }
