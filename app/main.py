import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    total_trials = 10000
    result = {i: 0.0 for i in range(11)}
    for _ in range(total_trials):
        heads = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round((result[key] / total_trials) * 100, 1)
    return result
