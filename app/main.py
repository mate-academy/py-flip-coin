import random
from typing import Dict


def flip_coin(trials: int = 10000, flips: int = 10) -> Dict[int, float]:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads_count] += 1

    # Переводимо в %
    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results
