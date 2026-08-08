import random
from typing import Dict


def flip_coin(num_flips: int = 10,
              num_trials: int = 10000) -> Dict[int, float]:

    counts = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        counts[heads_count] += 1

    percentages = {k: (v / num_trials) * 100 for k, v in counts.items()}
    return percentages
