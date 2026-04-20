import random

from collections import Counter


def flip_coin() -> dict:
    cases = []
    for _ in range(10000):
        results = []
        count = 0
        while count < 10:
            if random.randint(0, 1) == 1:
                results.append(1)
            else:
                results.append(0)
            count += 1
        cases.append(sum(results))

    counts = Counter(cases)

    distribution_dict = {k: round((v / 10000) * 100, 2)
                         for k, v in counts.items()}

    return dict(sorted(distribution_dict.items()))
