import random
from collections import Counter


def flip_coin() -> dict:
    cases = 10000
    amount = 10

    result = []

    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(amount))
        result.append(heads)

    counts = Counter(result)

    percentage = {key: (value / cases) * 100 for key, value in counts.items()}

    return dict(sorted(percentage.items()))
