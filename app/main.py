import random
from collections import Counter
from copy import copy


def flip_coin() -> dict[int, float]:
    flip_tests = []
    for _ in range(10000):
        coins = []
        for _ in range(10):
            coins.append(random.randint(0, 1))
        flip_tests.append(coins)

    head_counts = {}
    for coins in flip_tests:
        head_count = dict(Counter(coins).most_common()).get(1, 0)
        head_counts[head_count] = head_counts.get(head_count, 0) + 1

    result = copy(head_counts)
    for head_count, count in result.items():
        result[head_count] = (count / 10000) * 100

    return result
