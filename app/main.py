from random import randint


def flip_coin() -> dict:
    result = {}

    for _ in range(10000):
        heads = sum(randint(0, 1) for _ in range(10))
        result[heads] = result.get(heads, 0) + 1

        flips = sum(result.values())
    for head, count in result.items():
        result[head] = round(count / flips * 100, 2)
    return result
