import random
from typing import Dict


def flip_coin(cases: int = 10_000, flips: int = 10) -> Dict[int, float]:
    results: Dict[int, int] = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads_count = sum(random.choice((0, 1)) for _ in range(flips))
        results[heads_count] += 1

    return {
        heads: count / cases * 100
        for heads, count in results.items()
    }
