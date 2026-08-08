import random
from collections import Counter
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    outcomes = []

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        outcomes.append(heads_count)

    counts = Counter(outcomes)
    percentages = {
        outcome: (count / num_trials) * 100 for outcome,
        count in counts.items()
    }

    return percentages
