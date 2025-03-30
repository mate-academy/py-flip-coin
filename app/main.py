import random


def flip_coin() -> None:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        flips = [random.choice(["H", "T"]) for _ in range(10)]
        heads_count = flips.count("H")
        result[heads_count] += 1
    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)
    return result
