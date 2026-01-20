import random
from collections import Counter


def flip_coin(trials: int = 10000) -> dict:
    results = []

    for _ in range(trials):
        heads = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads += 1
        results.append(heads)

    counts = Counter(results)

    return {
        k: round((counts[k] / trials) * 100, 2)
        for k in range(11)
    }


print(flip_coin())
