import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        coin_flip = [random.choice(["head", "tail"]) for _ in range(10)]
        head_count = coin_flip.count("head")
        if head_count in result:
            result[head_count] += 1
        else:
            result[head_count] = 1

    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result
