from __future__ import annotations

import random
from typing import Dict


def flip_coin(
    experiments: int = 100_000,
    flips_per_experiment: int = 10,
) -> Dict[int, float]:
    results: Dict[int, int] = {
        heads: 0
        for heads in range(flips_per_experiment + 1)}

    for _ in range(experiments):
        heads_count: int = sum(
            random.choice((0, 1))
            for _ in range(flips_per_experiment))
        results[heads_count] += 1

    return {
        heads: round((count / experiments) * 100, 2)
        for heads, count in results.items()
    }
