import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        head = sum(random.choice([0, 1]) for _ in range(10))
        result[head] += 1

    total = sum(result.values())
    percent = {k: (v / total) * 100 for k, v in result.items()}
    return percent
