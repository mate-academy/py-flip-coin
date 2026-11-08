import random


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    heads_counts = {heads: 0 for heads in range(flips + 1)}
    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        heads_counts[heads] += 1
    return {
        heads: round(count / cases * 100, 2)
        for heads, count in heads_counts.items()
    }
