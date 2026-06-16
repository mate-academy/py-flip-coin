import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}
    for case in range(10000):
        head_count = 0
        for flip in range(10):
            if random.choice(["head", "tail"]) == "head":
                head_count += 1
        result[head_count] += 1
    result = {key: round(value / 100, 2) for key, value in result.items()}
    return result
