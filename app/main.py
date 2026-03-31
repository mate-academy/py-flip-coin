from typing import Dict
import random


def flip_coin() -> Dict:
    result = {}
    counts = [0] * 11
    for i in range(10000):
        result_count = 0
        for _ in range(10):
            flip = random.choice(["heads", "tails"])
            if flip == "heads":
                result_count += 1
        counts[result_count] += 1

    for head_count in range(11):
        result[head_count] = (counts[head_count] / 10000) * 100
    return result
