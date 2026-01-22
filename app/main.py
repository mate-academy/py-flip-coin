import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    total_experiments: int = 10_000
    heads_counts: Dict[int, float] = {heads: 0.0 for heads in range(11)}

    for _ in range(total_experiments):
        heads_result: int = sum(
            random.randint(0, 1) for _ in range(10)
        )
        heads_counts[heads_result] += 1

    for heads_number in heads_counts:
        heads_counts[heads_number] = (
            heads_counts[heads_number] / total_experiments
        ) * 100

    return heads_counts
