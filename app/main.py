import random
from collections import Counter


def flip_coin() -> dict:
    result = []
    for _ in range(10000):
        count = sum([random.choice([0, 1]) for _ in range(10)])
        result.append(count)
    count_heads = Counter(result)
    dict_result = {k: (v / 10000) * 100 for k, v in count_heads.items()}
    return dict(sorted(dict_result.items()))
