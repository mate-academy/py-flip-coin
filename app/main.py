import random
from typing import Dict


def flip_coin(
    num_trials: int = 10000, flips_per_trial: int = 10
) -> Dict[int, float]:
    """
    Симулирует подбрасывание монеты flips_per_trial раз num_trials раз,
    возвращает распределение в процентах по количеству орлов.
    """
    counts = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(num_trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        counts[heads_count] += 1

    percentages = {
        k: round(v / num_trials * 100, 2) for k, v in counts.items()
    }
    return percentages
