import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10_000):
        count_head = 0
        for _ in range(10):
            if random.choice(["head", "tails"]) == "head":
                count_head += 1
        result[count_head] = result.get(count_head, 0) + 1
    return {key: value / 100 for key, value in sorted(result.items())}
