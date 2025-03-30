import random


def flip_coin() -> dict:
    result = {}
    sides = [0, 1]
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            choice = random.choice(sides)
            if choice == 1:
                heads += 1
        result[heads] = result.get(heads, 0) + 1
    result = {
        key: value / 10000 * 100
        for key, value in result.items()
    }
    return result
