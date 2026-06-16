import random
from typing import Dict


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, float] = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] * 100 / trials, 2)

    return results
