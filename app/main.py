import random


def flip_coin() -> dict:
    result = {x: 0 for x in range(11)}
    for i in range(10_000):
        head = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                head += 1
        result[head] += 1

    return {i: result[i] / 100 for i in range(11)}
