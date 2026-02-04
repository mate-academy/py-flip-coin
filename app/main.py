import random
from collections import defaultdict


def flip_coin(
    num_flips: int = 10,
    num_trials: int = 10000,
) -> dict[int, float]:
    counts: defaultdict[int, int] = defaultdict(int)

    for _ in range(num_trials):
        heads = sum(
            random.choice([0, 1])
            for _ in range(num_flips)
        )
        counts[heads] += 1

    percentages: dict[int, float] = {
        k: round(v / num_trials * 100, 2)
        for k, v in counts.items()
    }

    for i in range(num_flips + 1):
        percentages.setdefault(i, 0.0)

    return dict(sorted(percentages.items()))
