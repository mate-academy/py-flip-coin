import random


def flip_coin() -> dict:
    result = {}
    for i in range(0, 11):
        result[i] = 0

    for _ in range(0, 10000):
        col_head = 0
        for _ in range(0, 10):
            head = random.randint(0, 1)
            if head:
                col_head += 1

        result[col_head] += 1

    for i in range(0, 11):
        result[i] = round(result[i] / 100, 2)

    return result
