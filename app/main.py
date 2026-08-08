from random import randint
from collections import Counter


def flip_coin() -> dict:
    results = []
    for flip in range(10000):
        one = 0
        for _ in range(10):
            one += randint(0, 1)
        results.append(one)
    dct = Counter(results)
    for num in range(11):
        dct[num] /= 100
    return dct
