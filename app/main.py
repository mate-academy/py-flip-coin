import random
from typing import Dict


def flip_coin(num_experiments: int = 10_000) -> Dict[int, float]:
    heads_counts: Dict[int, int] = {k: 0 for k in range(11)}

    for _ in range(num_experiments):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        heads_counts[heads] += 1

    return {
        heads: (count / num_experiments) * 100
        for heads, count in heads_counts.items()
    }
