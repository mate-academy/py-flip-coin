import random
from collections import defaultdict
from typing import Dict


def flip_coin() -> Dict[int, float]:
    experiments: int = 10_000
    results: Dict[int, int] = defaultdict(int)

    for _ in range(experiments):
        heads: int = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads += 1

        results[heads] += 1

    final_result: Dict[int, float] = {}

    for i in range(11):
        final_result[i] = round((results[i] / experiments) * 100, 2)

    return final_result


print(flip_coin())
