from typing import Dict

import random


def flip_coin() -> Dict[int, float]:
    count = [0] * 11
    trials = 10000

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        count[heads] += 1

    frequencies = list((i / trials) * 100 for i in count)

    return dict(zip(range(11), frequencies))


results = flip_coin()
for head_count, frequency in results.items():
    print(f"{head_count} heads: {frequency}%")
