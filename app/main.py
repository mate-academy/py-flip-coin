import random
from typing import Dict


def flip_coin(trials: int = 10000, flips: int = 10) -> Dict[int, float]:
    outcomes = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        outcomes[heads_count] += 1

    for heads in outcomes:
        outcomes[heads] = (outcomes[heads] / trials) * 100

    return outcomes
