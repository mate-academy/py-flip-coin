import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    num_simulations = 10000
    results = {i: 0 for i in range(11)}
    for _ in range(num_simulations):
        faces = sum(random.choice([0, 1]) for _ in range(10))
        results[faces] += 1
    percentages = {
        k: round((v / num_simulations) * 100, 2)
        for k, v in results.items()
    }
    return percentages
