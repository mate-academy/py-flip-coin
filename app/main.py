import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    for i in results:
        results[i] = round(results[i] / cases * 100, 2)

    return results
