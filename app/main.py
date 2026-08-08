import random


def flip_coin() -> dict:
    result = dict()

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() > 0.5:
                heads_count += 1
        if heads_count in result:
            result[heads_count] += 1
        else:
            result[heads_count] = 1

    total_heads_count = sum(result.values())
    percentage_result = dict()

    for key, value in result.items():
        percentage_result[key] = round((value / total_heads_count) * 100, 2)

    return percentage_result
