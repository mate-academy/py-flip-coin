import random
from collections import Counter


def flip_coin() -> dict:
    count_heads = []
    for _ in range(10_000):
        count_heads.append(
            sum([random.choice([0, 1]) for _ in range(10)])
        )
    count_mapping = Counter(count_heads)
    return {
        key: round(value / 10_000 * 100, 2)
        for key, value in count_mapping.items()
    }
