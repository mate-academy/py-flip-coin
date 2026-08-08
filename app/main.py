import random
from collections import defaultdict


def flip_coin() -> dict:
    result = defaultdict(int)

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1

    for heads in result:
        result[heads] = round((result[heads] / 10000) * 100, 2)

    return dict(result)
