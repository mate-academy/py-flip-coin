import random
from typing import Dict


def flip_coin(n_cases: int = 10000) -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(n_cases):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    for heads_count in results:
        results[heads_count] = round(results[heads_count] / n_cases * 100, 2)

    return results
