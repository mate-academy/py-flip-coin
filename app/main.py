import random
from collections import Counter


def flip_coin(experiments: int = 10000, flips: int = 10) -> dict:
    results = []

    for i in range(experiments):
        heads = 0
        for i in range(flips):
            coin = random.choice([0, 1])
            heads += coin
        results.append(heads)

    counts = Counter()
    for result in results:
        counts[result] += 1

    percentages = {}
    for key in sorted(counts):
        value = counts[key]
        percent = round((value / experiments) * 100, 2)
        percentages[key] = percent

    return percentages
