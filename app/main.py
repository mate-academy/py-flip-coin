import random


def flip_coin() -> dict:
    result = {}
    head_or_tail = [0, 1]
    for i in range(10000):
        head_count = [random.choice(head_or_tail) for j in range(10)].count(1)
        if result.get(head_count):
            result[head_count] += 1
        else:
            result[head_count] = 1
    result = {key: value / 100 for key, value in result.items()}
    return result
