import random
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_trials * 100)

    return results
