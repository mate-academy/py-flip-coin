import random


def flip_coin() -> dict:
    result = {elem: 0 for elem in range(11)}
    for _ in range(10_000):
        count_heads = sum(random.randint(0, 1) for _ in range(10))
        result[count_heads] += 1

    for key in result:
        result[key] = round(result[key] / 10_000 * 100, 2)
    return result
