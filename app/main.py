import random
from collections import Counter


def flip_coin(num_cases: int = 10000) -> dict:
    heads_count = Counter()
    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        heads_count[heads] += 1

    total_cases = sum(heads_count.values())
    heads_percentage = {heads: (count / total_cases) * 100
                        for heads, count in heads_count.items()}

    return heads_percentage
