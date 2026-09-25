import random


def flip_coin() -> dict[int, float]:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1

        result[heads_count] += 1

    for key, value in result.items():
        result[key] = round(value / 10000, 2)

    return result
