from __future__ import annotations

import random


EXPERIMENTS_COUNT = 10_000
FLIPS_PER_EXPERIMENT = 10


def flip_coin() -> dict[int, float]:
    heads_distribution = {heads_count: 0 for heads_count in range(11)}

    for _ in range(EXPERIMENTS_COUNT):
        heads_count = sum(
            random.randint(0, 1) for _ in range(FLIPS_PER_EXPERIMENT)
        )
        heads_distribution[heads_count] += 1

    return {
        heads_count: round(
            experiments_count / EXPERIMENTS_COUNT * 100,
            2
        )
        for heads_count, experiments_count in heads_distribution.items()
    }
