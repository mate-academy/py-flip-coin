import random
from collections import defaultdict


def flip_coin() -> dict:
    counts = defaultdict(int)
    for _ in range(10000):
        flips = [random.choice(["Heads", "Tails"]) for _ in range(10)]
        counts[flips.count("Heads")] += 1
    return {k: v / 100 for k, v in sorted(counts.items())}
